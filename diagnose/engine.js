/* Diagnostic engine: pure functions with no DOM or dependencies. Exposed as window.DiagEngine in browsers and available through require() in Node.
 *
 * Data flow:
 *   buildGraph(topics, deps, questions?) -> graph (if questions are missing, use topics.diagnostic_question)
 *   createSession(graph, targets, {limit, seed, avoid}) -> session (plain data that can be serialized as JSON)
 *   nextQuestion(graph, session) -> topicId | null (the next topic to assess)
 *   nextItem(graph, session) -> {topicId, question, attempt} | null (the next question; attempt starts at 1)
 *   applyAnswer(graph, session, id, 'correct'|'wrong'|'skip', {text}) -> new session (does not mutate inputs)
 *   summarize(graph, session) -> results (root gaps, study path, mastered/uncertain/weak/untested)
 *   gradeTargets(graph, '一年级'|'七上'|'高一'|'选必二', subject?) -> {ids, volumes, label} | null
 *     The default subject is math. Do not mix English high-school volumes into math; 'english' selects only English (including 九全), 'physics' selects only physics (八上、八下、九全), and 'all' includes every subject.
 *   createSession(graph, ids, {mode:'screen', confirm}) -> screening session whose scope is the targets themselves; prerequisites are not traced outside the scope; default question limit is SCREEN_LIMIT
 *   chapterSummary(graph, session) -> chapter summary (weakest chapters first)
 *   layout(graph, session, summary) -> layered layout for the path graph
 *   judgeQuestion(question, userText) -> {verdict:'correct'|'wrong'|'manual', reason}
 *   judgeAnswer(user, reference) -> same behavior (legacy interface that compares answer text only)
 *
 * A topic is mastered after confirm consecutive correct answers (default 3; options are 2/3/5, capped by the number of available questions):
 *   Reaching the threshold marks the topic and its ancestors as mastered (ancestors are inferred); an incorrect or skipped answer triggers an easier confirmation question.
 *   A correct confirmation marks the topic uncertain (shaky, without tracing prerequisites); another incorrect or skipped answer marks it weak (weak, tracing hard prerequisites before soft ones).
 *   Question selection: prefer standard difficulty first; after consecutive correct answers, use challenge to confirm mastery; after a miss, use basic first.
 */
(function (root, factory) {
  if (typeof module !== 'undefined' && module.exports) module.exports = factory();
  else root.DiagEngine = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ------------------------------------------------------------------ Graph */

  const DIFF_RANK = { basic: 0, standard: 1, challenge: 2, advanced: 2 };

  function qNum(q) { const m = /_q(\d+)$/.exec(q.id); return m ? parseInt(m[1], 10) : 0; }

  function buildGraph(topics, deps, questions) {
    const byId = Object.create(null);
    const index = Object.create(null);
    topics.forEach(function (t, i) { byId[t.id] = t; index[t.id] = i; });
    const prereqs = Object.create(null);
    const dependents = Object.create(null);
    topics.forEach(function (t) { prereqs[t.id] = []; dependents[t.id] = []; });
    const seen = Object.create(null);
    deps.forEach(function (d) {
      if (!byId[d.topicId] || !byId[d.prerequisiteId]) return;
      const k = d.topicId + '<' + d.prerequisiteId;
      if (seen[k]) return;
      seen[k] = true;
      const strength = d.strength === 'soft' ? 'soft' : 'hard';
      prereqs[d.topicId].push({ id: d.prerequisiteId, strength: strength, reason: d.reason });
      dependents[d.prerequisiteId].push({ id: d.topicId, strength: strength });
    });
    // Order prerequisites by hard before soft; preserve topic-file order within each group for deterministic question selection.
    const rank = function (e) { return (e.strength === 'hard' ? 0 : 1) * 1e6 + index[e.id]; };
    Object.keys(prereqs).forEach(function (id) {
      prereqs[id].sort(function (a, b) { return rank(a) - rank(b); });
      dependents[id].sort(function (a, b) { return index[a.id] - index[b.id]; });
    });
    // Sort each topic's question bank by question number; fall back to diagnostic_question if the bank or a topic's questions are missing.
    const bank = Object.create(null);
    topics.forEach(function (t) { bank[t.id] = []; });
    let fromFile = 0;
    (Array.isArray(questions) ? questions : []).forEach(function (q) {
      if (q && bank[q.topicId] && !byId[q.topicId].external) { bank[q.topicId].push(q); fromFile++; }
    });
    topics.forEach(function (t) {
      const dq = t.diagnostic_question;
      if (!t.external && !bank[t.id].length && dq && dq.question) {
        bank[t.id].push({ id: t.id + '_q1', topicId: t.id, difficulty: 'standard', type: 'legacy', prompt: dq.question, answer: dq.answer, explanation: '' });
      }
    });
    Object.keys(bank).forEach(function (id) { bank[id].sort(function (a, b) { return qNum(a) - qNum(b); }); });
    return {
      topics: topics, byId: byId, index: index, prereqs: prereqs, dependents: dependents, bank: bank,
      hasBank: fromFile > 0, _anc: Object.create(null)
    };
  }

  /** Strict ancestor set (excluding the topic itself), cached. */
  function ancestorSet(graph, id) {
    const memo = graph._anc;
    if (memo[id]) return memo[id];
    const visiting = graph._visiting || (graph._visiting = Object.create(null));
    if (visiting[id]) throw new Error('Cycle in prerequisite graph: ' + id);
    visiting[id] = true;
    const out = new Set();
    graph.prereqs[id].forEach(function (p) {
      out.add(p.id);
      ancestorSet(graph, p.id).forEach(function (a) { out.add(a); });
    });
    visiting[id] = false;
    memo[id] = out;
    return out;
  }

  function ancestors(graph, ids) {
    const list = Array.isArray(ids) ? ids : [ids];
    const out = new Set();
    list.forEach(function (id) { ancestorSet(graph, id).forEach(function (a) { out.add(a); }); });
    return out;
  }

  /** Topologically sort a node subset (prerequisites first); preserve topic-file order within each layer for determinism. */
  function topoSort(graph, ids) {
    const set = new Set(ids);
    const indeg = Object.create(null);
    set.forEach(function (id) {
      indeg[id] = graph.prereqs[id].filter(function (p) { return set.has(p.id); }).length;
    });
    const ready = [];
    set.forEach(function (id) { if (indeg[id] === 0) ready.push(id); });
    const byIndex = function (a, b) { return graph.index[a] - graph.index[b]; };
    const order = [];
    while (ready.length) {
      ready.sort(byIndex);
      const id = ready.shift();
      order.push(id);
      graph.dependents[id].forEach(function (d) {
        if (!set.has(d.id)) return;
        indeg[d.id] -= 1;
        if (indeg[d.id] === 0) ready.push(d.id);
      });
    }
    if (order.length !== set.size) throw new Error('Topological sort failed: the subgraph contains a cycle.');
    return order;
  }

  /** Prerequisite subgraph for a target set: targets plus all ancestors (including external elementary topics), in topological order. */
  function subgraph(graph, targets) {
    const set = new Set(targets);
    ancestors(graph, targets).forEach(function (a) { set.add(a); });
    return { nodes: topoSort(graph, set), set: set };
  }

  function isTestable(graph, id) {
    const t = graph.byId[id];
    return !!(t && !t.external && graph.bank[id] && graph.bank[id].length);
  }

  function questionById(graph, qid) {
    const m = /^(.*)_q\d+$/.exec(qid || '');
    const list = m ? graph.bank[m[1]] : null;
    return (list || []).find(function (q) { return q.id === qid; }) || null;
  }

  /* ------------------------------------------------------------------ Sessions */

  const RESULTS = { correct: 1, wrong: 1, skip: 1 };
  const DEFAULT_LIMIT = 16;
  const SCREEN_LIMIT = 40;
  const DEFAULT_CONFIRM = 3;
  const CONFIRM_CHOICES = [2, 3, 5];

  /** UI options: accept only 2 / 3 / 5; use the default for other values. */
  function clampConfirm(n) {
    const v = Math.floor(Number(n));
    return CONFIRM_CHOICES.indexOf(v) >= 0 ? v : DEFAULT_CONFIRM;
  }

  /** Engine-internal setting: any confirmation count >= 1 (tests may use 1; the UI still uses clampConfirm). */
  function normalizeConfirm(n) {
    const v = Math.floor(Number(n));
    return v >= 1 && v <= 10 ? v : DEFAULT_CONFIRM;
  }

  /** Consecutive correct answers required to master a topic: the smaller of confirm and the available question count (minimum 1). */
  function needConfirm(graph, session, id) {
    const bankLen = (graph.bank[id] || []).length;
    const conf = session && session.confirm != null ? session.confirm : DEFAULT_CONFIRM;
    return Math.max(1, Math.min(conf, bankLen || 1));
  }

  function createSession(graph, targets, opts) {
    opts = opts || {};
    const ts = Array.from(new Set(targets));
    if (!ts.length) throw new Error('At least one target topic is required.');
    ts.forEach(function (id) { if (!graph.byId[id]) throw new Error('Unknown topic: ' + id); });
    const screen = opts.mode === 'screen';
    const limit = Math.max(1, Math.floor(opts.limit == null ? (screen ? SCREEN_LIMIT : DEFAULT_LIMIT) : opts.limit));
    const confirm = normalizeConfirm(opts.confirm == null ? DEFAULT_CONFIRM : opts.confirm);
    // Screening mode uses the target set as the diagnostic scope (do not add prerequisite ancestors); trace only within the scope.
    const sub = screen ? { nodes: topoSort(graph, ts) } : subgraph(graph, ts);
    const pos = Object.create(null);
    sub.nodes.forEach(function (id, i) { pos[id] = i; });
    // Ask the target closest to the end of the topological order first; keep the other targets on the stack as fallbacks.
    const stack = ts.filter(function (id) { return isTestable(graph, id); })
      .sort(function (a, b) { return pos[b] - pos[a]; });
    return {
      targets: ts, limit: limit, confirm: confirm, order: sub.nodes, status: {}, stack: stack, answers: [], attempts: {},
      mode: screen ? 'screen' : 'target', scope: screen ? ts.slice() : null,
      seed: opts.seed == null ? 'default' : String(opts.seed),
      avoid: Array.from(new Set(opts.avoid || []))
    };
  }

  function cloneSession(s) {
    const attempts = {};
    Object.keys(s.attempts).forEach(function (k) { attempts[k] = s.attempts[k].slice(); });
    return {
      targets: s.targets.slice(), limit: s.limit, confirm: s.confirm, order: s.order, stack: s.stack.slice(),
      status: Object.assign({}, s.status), answers: s.answers.slice(), attempts: attempts,
      seed: s.seed, avoid: s.avoid, mode: s.mode, scope: s.scope ? s.scope.slice() : null
    };
  }

  /* ---- Seeded pseudo-randomness: the same (seed, topic, attempt) always yields the same value, so sessions can be replayed. ---- */
  function hashStr(str) {
    let h = 2166136261 >>> 0;
    for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
    return h >>> 0;
  }

  function mulberry32(a) {
    return function () {
      a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function rand01(seed, key) {
    const f = mulberry32(hashStr(String(seed) + '|' + key));
    f();
    return f();
  }

  const rankOf = function (q) { return DIFF_RANK[q.difficulty] == null ? 1 : DIFF_RANK[q.difficulty]; };

  /**
   * Select the attempt-th question for a topic ID.
   *  - Do not repeat questions already asked in this session.
   *  - First question: prefer standard; fall back to basic if unavailable, and avoid challenge when possible.
   *  - After consecutive correct answers with no misses: prefer challenge to confirm mastery, then standard, then basic.
   *  - After a miss, choose a confirmation question at the same or lower difficulty: basic first, then the first question's difficulty, then other easier questions, and finally the easiest harder question.
   *    Difficulty takes precedence over whether a question has been used; within a difficulty, prefer unused questions (excluding session.avoid).
   *  - Use the seeded pseudo-random value to select a question within the chosen tier.
   */
  function pickQuestion(graph, session, id, attempt) {
    const all = graph.bank[id] || [];
    const tried = (session.attempts[id] || []).map(function (a) { return a.qid; });
    const pool = all.filter(function (q) { return tried.indexOf(q.id) < 0; });
    if (!pool.length) return null;
    const avoid = new Set(session.avoid || []);
    const freshFirst = function (list) {
      const f = list.filter(function (q) { return !avoid.has(q.id); });
      return f.length ? f : list;
    };
    const pickRank = function (list, ranks) {
      for (let i = 0; i < ranks.length; i++) {
        const hit = list.filter(function (q) { return rankOf(q) === ranks[i]; });
        if (hit.length) return freshFirst(hit);
      }
      return freshFirst(list);
    };
    const prev = session.attempts[id] || [];
    const hadFail = prev.some(function (a) { return a.result !== 'correct'; });
    let cand;
    if (attempt <= 1 || !hadFail) {
      const base = freshFirst(pool);
      if (attempt <= 1) cand = pickRank(base, [1, 0]);
      else cand = pickRank(base, [2, 1, 0]);
    } else {
      const first = all.find(function (q) { return q.id === tried[0]; });
      const r0 = first ? rankOf(first) : 1;
      const tiers = [
        pool.filter(function (q) { return rankOf(q) === 0; }),
        pool.filter(function (q) { return rankOf(q) === r0; }),
        pool.filter(function (q) { return rankOf(q) < r0; })
      ];
      const hit = tiers.find(function (t) { return t.length; });
      if (hit) cand = freshFirst(hit);
      else {
        const lo = Math.min.apply(null, pool.map(rankOf));
        cand = freshFirst(pool.filter(function (q) { return rankOf(q) === lo; }));
      }
    }
    const idx = Math.min(cand.length - 1, Math.floor(rand01(session.seed, id + '|' + attempt) * cand.length));
    return cand[idx];
  }

  /**
   * Record an answer to the question returned by nextItem.
   *  - Reaching needConfirm consecutive correct answers marks the topic and all undecided ancestors as mastered (ancestors are inferred).
   *  - Correct answers below the threshold produce no conclusion; ask the next question for the same topic.
   *  - An incorrect or skipped answer triggers a confirmation question (mark weak immediately if none is available).
   *  - A correct confirmation marks the topic uncertain (shaky) without tracing prerequisites.
   *  - An incorrect or skipped confirmation marks the topic weak and pushes its prerequisites (hard first, then soft) to the top of the question stack.
   * Direct answer status is never overwritten by an inferred status. extra.text is the user's answer, stored only for the record.
   */
  function applyAnswer(graph, session, id, result, extra) {
    if (!RESULTS[result]) throw new Error('Answer result must be correct, wrong, or skip.');
    if (!graph.byId[id]) throw new Error('Unknown topic: ' + id);
    const s = cloneSession(session);
    if (s.status[id]) { delete s.status[id]; s.attempts[id] = []; } // Answering a decided topic again starts it over.
    const prev = s.attempts[id] || [];
    const q = pickQuestion(graph, s, id, prev.length + 1);
    const rec = { id: id, qid: q ? q.id : null, result: result };
    if (extra && extra.text != null && extra.text !== '') rec.text = String(extra.text);
    s.answers.push(rec);
    s.attempts[id] = prev.concat([{ qid: rec.qid, result: result }]);
    const attempts = s.attempts[id];
    const fails = attempts.filter(function (a) { return a.result !== 'correct'; }).length;
    const corrects = attempts.filter(function (a) { return a.result === 'correct'; }).length;
    const need = needConfirm(graph, s, id);
    if (result === 'correct') {
      if (fails === 0 && corrects >= need) {
        s.status[id] = { s: 'mastered', src: 'direct' };
        ancestorSet(graph, id).forEach(function (a) {
          if (!s.status[a]) s.status[a] = { s: 'mastered', src: 'inferred' };
        });
      } else if (fails > 0) {
        s.status[id] = { s: 'shaky', src: 'direct' };
      }
      // Otherwise, the correct-answer streak is below the threshold; continue asking questions.
    } else if (fails === 1 && pickQuestion(graph, s, id, attempts.length + 1)) {
      // The first attempt was not passed; wait for the confirmation question before deciding.
    } else {
      s.status[id] = { s: 'weak', src: 'direct' };
      const scope = s.scope ? new Set(s.scope) : null;
      const push = graph.prereqs[id]
        .map(function (p) { return p.id; })
        .filter(function (p) { return isTestable(graph, p) && !s.status[p] && (!scope || scope.has(p)); });
      const pushed = new Set(push);
      s.stack = push.concat(s.stack.filter(function (x) { return !pushed.has(x); }));
    }
    return s;
  }

  function nextQuestion(graph, session) {
    if (session.answers.length >= session.limit) return null;
    for (let i = 0; i < session.stack.length; i++) {
      const id = session.stack[i];
      if (!session.status[id] && isTestable(graph, id)) return id;
    }
    return null;
  }

  function nextItem(graph, session) {
    const id = nextQuestion(graph, session);
    if (!id) return null;
    const attempt = (session.attempts[id] || []).length + 1;
    const q = pickQuestion(graph, session, id, attempt);
    return q ? { topicId: id, question: q, attempt: attempt } : null;
  }

  /** Rebuild a session from answer records (for refresh recovery, undo, and corrections). */
  function replay(graph, targets, answers, opts) {
    let s = createSession(graph, targets, opts);
    answers.forEach(function (a) { s = applyAnswer(graph, s, a.id, a.result, { text: a.text }); });
    return s;
  }

  /** Status: mastered / shaky / weak / unknown. A topic that misses once and hits the question limit is treated as weak (see isUnconfirmed). */
  function statusOf(session, id) {
    const st = session.status[id];
    if (st) return st.s;
    return isUnconfirmed(session, id) ? 'weak' : 'unknown';
  }

  /** Topics with a missed answer but no confirmation question because the question limit was reached. */
  function isUnconfirmed(session, id) {
    const a = session.attempts[id];
    if (session.status[id] || !a || !a.length) return false;
    return a.some(function (x) { return x.result !== 'correct'; });
  }

  /* ------------------------------------------------------------------ Results */

  function summarize(graph, session) {
    const nodes = session.order;
    const st = function (id) { return statusOf(session, id); };
    const mastered = nodes.filter(function (id) { return st(id) === 'mastered'; });
    const shaky = nodes.filter(function (id) { return st(id) === 'shaky'; });
    const weak = nodes.filter(function (id) { return st(id) === 'weak'; });
    const unconfirmed = weak.filter(function (id) { return isUnconfirmed(session, id); });
    const untested = nodes.filter(function (id) { return st(id) === 'unknown'; });
    const scope = session.scope ? new Set(session.scope) : null;
    const inScope = function (id) { return !scope || scope.has(id); };

    const roots = weak.filter(function (id) {
      return !graph.prereqs[id].some(function (p) { return st(p.id) === 'weak'; });
    }).map(function (id) {
      const unk = graph.prereqs[id].filter(function (p) { return st(p.id) === 'unknown'; });
      const testableUnk = unk.filter(function (p) { return isTestable(graph, p.id); });
      return {
        id: id,
        // Untested prerequisites (question limit reached); one of these may be the actual root gap.
        pendingPrereqs: testableUnk.filter(function (p) { return inScope(p.id); }).map(function (p) { return p.id; }),
        // Prerequisites outside a screening scope (not included or assessed in this session).
        outOfScopePrereqs: testableUnk.filter(function (p) { return !inScope(p.id); }).map(function (p) { return p.id; }),
        // External elementary topics (no diagnostic question, so they are not assessed).
        externalPrereqs: unk.filter(function (p) { return !isTestable(graph, p.id); }).map(function (p) { return p.id; })
      };
    });

    // Study path: descendants within the subgraph of root gaps and uncertain topics, plus those topics themselves; remove mastered topics and use topological order.
    const inSub = new Set(nodes);
    const reach = new Set();
    const queue = roots.map(function (r) { return r.id; }).concat(shaky);
    queue.forEach(function (id) { reach.add(id); });
    while (queue.length) {
      const id = queue.shift();
      graph.dependents[id].forEach(function (d) {
        if (inSub.has(d.id) && !reach.has(d.id)) { reach.add(d.id); queue.push(d.id); }
      });
    }
    const rootSet = new Set(roots.map(function (r) { return r.id; }));
    const targetSet = new Set(scope ? [] : session.targets); // In screening mode every topic is a target, so do not mark all topics as targets.
    const topoPos = Object.create(null);
    nodes.forEach(function (id, i) { topoPos[id] = i; });
    const path = nodes.filter(function (id) { return reach.has(id) && st(id) !== 'mastered'; })
      .map(function (id) {
        return { id: id, status: st(id), isRoot: rootSet.has(id), isTarget: targetSet.has(id) };
      });
    // Sort the study path by grade, then preserve topological order within each grade. Leave hand-built graphs without grades in their original order.
    path.sort(function (a, b) {
      return gradeRank(graph, a.id) - gradeRank(graph, b.id) || topoPos[a.id] - topoPos[b.id];
    });

    const pending = session.stack.filter(function (id) { return !session.status[id] && isTestable(graph, id); });
    const next = nextQuestion(graph, session);
    return {
      mode: session.mode || 'target',
      targets: session.targets.slice(),
      asked: session.answers.length,
      limit: session.limit,
      finished: next === null,
      limitReached: session.answers.length >= session.limit && pending.length > 0,
      mastered: mastered, shaky: shaky, weak: weak, unconfirmed: unconfirmed, untested: untested,
      roots: roots, path: path
    };
  }

  /* ------------------------------------------------------------------ Path graph layout */

  /**
   * Select nodes to draw: study path, targets, root gaps, and topics actually asked about.
   * Edges use the transitive reduction of reachability among selected nodes; non-direct prerequisites are marked direct:false (dashed).
   * Layer vertically, with prerequisites above targets.
   */
  function layout(graph, session, summary) {
    const S = new Set();
    const screen = !!session.scope;
    summary.path.forEach(function (p) { S.add(p.id); });
    if (!screen) session.targets.forEach(function (id) { S.add(id); });
    summary.roots.forEach(function (r) { S.add(r.id); });
    session.answers.forEach(function (a) { S.add(a.id); });
    if (S.size < 3 && !screen) {
      session.targets.forEach(function (id) {
        graph.prereqs[id].slice(0, 6).forEach(function (p) { S.add(p.id); });
      });
    }
    const ids = topoSort(graph, S);
    const edges = [];
    ids.forEach(function (b) {
      const anc = ancestorSet(graph, b);
      ids.forEach(function (a) {
        if (a === b || !anc.has(a)) return;
        const between = ids.some(function (c) {
          return c !== a && c !== b && anc.has(c) && ancestorSet(graph, c).has(a);
        });
        if (between) return;
        const direct = graph.prereqs[b].find(function (p) { return p.id === a; });
        edges.push({ from: a, to: b, direct: !!direct, strength: direct ? direct.strength : 'hard' });
      });
    });
    const layer = Object.create(null);
    ids.forEach(function (id) {
      let l = 0;
      edges.forEach(function (e) { if (e.to === id) l = Math.max(l, layer[e.from] + 1); });
      layer[id] = l;
    });
    const nLayers = ids.reduce(function (m, id) { return Math.max(m, layer[id] + 1); }, 1);
    const rows = [];
    for (let i = 0; i < nLayers; i++) rows.push([]);
    ids.forEach(function (id) { rows[layer[id]].push(id); });
    // Use barycentric ordering to reduce edge crossings.
    const slot = Object.create(null);
    rows.forEach(function (r) { r.forEach(function (id, i) { slot[id] = i; }); });
    const bary = function (id, nbrs) {
      if (!nbrs.length) return slot[id];
      return nbrs.reduce(function (s, n) { return s + slot[n]; }, 0) / nbrs.length;
    };
    for (let it = 0; it < 4; it++) {
      for (let l = 1; l < nLayers; l++) {
        rows[l].sort(function (a, b) {
          return bary(a, edges.filter(function (e) { return e.to === a; }).map(function (e) { return e.from; })) -
                 bary(b, edges.filter(function (e) { return e.to === b; }).map(function (e) { return e.from; }));
        });
        rows[l].forEach(function (id, i) { slot[id] = i; });
      }
      for (let l = nLayers - 2; l >= 0; l--) {
        rows[l].sort(function (a, b) {
          return bary(a, edges.filter(function (e) { return e.from === a; }).map(function (e) { return e.to; })) -
                 bary(b, edges.filter(function (e) { return e.from === b; }).map(function (e) { return e.to; }));
        });
        rows[l].forEach(function (id, i) { slot[id] = i; });
      }
    }
    const rootSet = new Set(summary.roots.map(function (r) { return r.id; }));
    const targetSet = new Set(screen ? [] : session.targets);
    const nodes = [];
    rows.forEach(function (r, l) {
      r.forEach(function (id, i) {
        nodes.push({
          id: id, layer: l, col: i, cols: r.length,
          status: statusOf(session, id), isTarget: targetSet.has(id), isRoot: rootSet.has(id)
        });
      });
    });
    return { nodes: nodes, edges: edges, layers: nLayers, maxCols: rows.reduce(function (m, r) { return Math.max(m, r.length); }, 1) };
  }

  /* ------------------------------------------------------------------ Chapter parsing */

  /** Grade number × 2 + semester, used to sort the study path. Returns 0 when grade is missing. */
  function gradeRank(graph, id) {
    const t = graph.byId[id];
    if (!t || typeof t.grade !== 'number') return 0;
    return t.grade * 2 + (t.semester === '下' ? 1 : 0);
  }

  /** Parse a chapter label and use topic metadata to resolve its internal volume code. */
  function parseChapter(chapter, topic) {
    const s = String(chapter || '');
    const pm = /^([一二三四五六七八九])年级([上下全])册 (第\d+单元|预备单元\d) (.+)$/.exec(s);
    if (pm) return { volume: pm[1] + pm[2], chapterNo: pm[3], chapterName: pm[4], section: '' };
    const pi = /^([一二三四五六])年级([上下])册 (综合与实践) (.+)$/.exec(s);
    if (pi) return { volume: pi[1] + pi[2], chapterNo: pi[3], chapterName: pi[4], section: '' };
    // Parse high-school English by volume name to avoid splitting "第1单元 Teenage Life" at the space.
    const enHs = /^(必修第([一二三])册|选择性必修第([一二三四])册) (欢迎单元|第\d+单元) (.+)$/.exec(s);
    if (enHs) {
      return {
        volume: enHs[2] ? ('必修' + enHs[2]) : ('选必' + enHs[3]),
        chapterNo: enHs[4],
        chapterName: enHs[5],
        section: ''
      };
    }
    const compactEnglish = /^(Selective Compulsory|Compulsory) Volume \d+ (Welcome Unit|Unit \d+) (.+)$/i.exec(s);
    if (compactEnglish) {
      return {
        volume: englishChapterVolume(s, topic),
        chapterNo: compactEnglish[2],
        chapterName: compactEnglish[3],
        section: ''
      };
    }
    const hs = /^(高[一二]|选必[一二三]) (数学建模|数学探究) (\S+)$/.exec(s);
    if (hs) return { volume: hs[1], chapterNo: hs[2], chapterName: hs[3], section: '' };
    const m = /^(\S+) (第\S+章) (\S+?)(?: (\S+))?$/.exec(s);
    if (m) return { volume: m[1], chapterNo: m[2], chapterName: m[3], section: m[4] || '' };

    const volume = englishChapterVolume(s, topic);
    let body = s.replace(/^Grade \d+,\s*/i, '');
    body = body.replace(/^(?:Semester 1|Semester 2|First semester|Second semester|Full year)\s*,\s*/i, '');
    body = body.replace(/^(?:(?:Selective )?(?:Required|Compulsory) Volume (?:\d+|I|II|III|IV))\s*,\s*/i, '');

    let section = '';
    const sectionMatch = /,\s*Section\s+(.+)$/i.exec(body);
    if (sectionMatch) {
      section = sectionMatch[1].trim();
      body = body.slice(0, sectionMatch.index).trim();
    } else {
      const trailingSection = /\s+(\d+(?:\.\d+)+)\.?$/.exec(body);
      if (trailingSection) {
        section = trailingSection[1];
        body = body.slice(0, trailingSection.index).trim();
      }
    }

    const label = /^((?:Unit|Chapter|Module)\s+(?:\d+|[IVXLCDM]+|[A-Za-z]+)|Welcome Unit|Integrated Study and Practice|Integrated Learning|Integrated Practice|Mathematical Modeling|Mathematical Inquiry|Synthesis and Practice)(?::\s*|\s+)?(.*)$/i.exec(body);
    if (label) {
      const chapterNo = normalizeChapterNo(label[1]);
      return { volume: volume, chapterNo: chapterNo, chapterName: middleSchoolMathChapterName(topic, chapterNo, label[2].trim()), section: section };
    }
    const chapterLabel = /\b(?:Chapter|chap\.?)\s+(One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|[IVXLCDM]+|\d+)\b/i.exec(body);
    if (chapterLabel) {
      const chapterNo = normalizeChapterNo('Chapter ' + chapterLabel[1]);
      const name = body.slice(chapterLabel.index + chapterLabel[0].length).replace(/^[\s:.,\-–—]+/, '').trim();
      return { volume: volume, chapterNo: chapterNo, chapterName: middleSchoolMathChapterName(topic, chapterNo, name), section: section };
    }
    const unitLabel = /\b(Unit|Module)\s+(\d+)\b/i.exec(body);
    if (unitLabel) {
      const name = body.slice(unitLabel.index + unitLabel[0].length).replace(/^[\s:.,\-–—]+/, '').trim();
      return { volume: volume, chapterNo: unitLabel[1] + ' ' + unitLabel[2], chapterName: name, section: section };
    }
    const gradeSevenChapter = topic && subjectOf(topic) === 'math' && topic.grade === 7 && topic.semester === '上'
      ? /^VII[,.\s]+(VI|V|IV|III|II|I)\b/i.exec(body)
      : null;
    if (gradeSevenChapter) {
      const chapterNo = normalizeChapterNo('Chapter ' + gradeSevenChapter[1]);
      return { volume: volume, chapterNo: chapterNo, chapterName: middleSchoolMathChapterName(topic, chapterNo, ''), section: section };
    }
    return { volume: volume, chapterNo: '', chapterName: body.trim() || s, section: section };
  }

  function normalizeChapterNo(label) {
    const match = /^Chapter\s+(.+)$/i.exec(label);
    if (!match) return label;
    const token = match[1];
    const words = { One: 1, Two: 2, Three: 3, Four: 4, Five: 5, Six: 6, Seven: 7, Eight: 8, Nine: 9, Ten: 10 };
    if (words[token[0].toUpperCase() + token.slice(1).toLowerCase()]) {
      return 'Chapter ' + words[token[0].toUpperCase() + token.slice(1).toLowerCase()];
    }
    if (/^\d+$/.test(token)) return 'Chapter ' + Number(token);
    if (/^[IVXLCDM]+$/i.test(token)) {
      const values = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
      const roman = token.toUpperCase();
      let total = 0;
      for (let i = 0; i < roman.length; i++) {
        const current = values[roman[i]];
        const next = values[roman[i + 1]] || 0;
        total += current < next ? -current : current;
      }
      return 'Chapter ' + total;
    }
    return label;
  }

  function middleSchoolMathChapterName(topic, chapterNo, name) {
    if (!topic || subjectOf(topic) !== 'math' || topic.grade !== 7 || topic.semester !== '上') return name;
    const number = Number(/^Chapter (\d+)$/.exec(chapterNo)?.[1]);
    const names = {
      1: 'Rational Numbers',
      2: 'Operations with Rational Numbers',
      3: 'Algebraic Expressions',
      4: 'Simplifying Algebraic Expressions',
      5: 'Linear Equations in One Variable',
      6: 'Basic Geometric Figures'
    };
    return names[number] || name;
  }

  function englishChapterVolume(chapter, topic) {
    const text = String(chapter || '');
    const gradeMatch = /^Grade (\d+)\b/i.exec(text);
    const grade = Number(topic && topic.grade) || (gradeMatch ? Number(gradeMatch[1]) : 0);
    const subject = topic ? subjectOf(topic) : (/Selective Compulsory|Compulsory Volume/i.test(text) ? 'english' : /Volume (?:I|II|III|IV)\b/i.test(text) ? 'physics' : 'math');
    const gradeDigit = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九'];
    const termMatch = /\b(Semester 1|First semester|Semester 2|Second semester|Full year)\b/i.exec(text);
    const term = topic && ['上', '下', '全'].includes(topic.semester)
      ? topic.semester
      : termMatch
        ? (/semester 1|first semester/i.test(termMatch[1]) ? '上' : /semester 2|second semester/i.test(termMatch[1]) ? '下' : '全')
        : '';
    if (grade >= 1 && grade <= 9 && term) return gradeDigit[grade] + term;

    const volumeNumber = { I: 1, II: 2, III: 3, IV: 4 };
    const selectiveMatch = /Selective (?:Required|Compulsory) Volume (IV|III|II|I|\d+)/i.exec(text);
    const requiredMatch = /(?:Required|Compulsory) Volume (IV|III|II|I|\d+)/i.exec(text);
    const numberOf = function (match) {
      if (!match) return 0;
      return Number(volumeNumber[match[1].toUpperCase()] || match[1]);
    };
    if (subject === 'math') {
      if (grade === 10) return '高一';
      if (grade === 11) return '高二';
      if (grade >= 12 && grade <= 14) return '选必' + gradeDigit[grade - 11];
      if (selectiveMatch) return '选必' + gradeDigit[numberOf(selectiveMatch)];
      if (requiredMatch && /Compulsory Volume/i.test(text)) return '必修' + gradeDigit[numberOf(requiredMatch)];
    } else {
      if (selectiveMatch) return '选必' + gradeDigit[numberOf(selectiveMatch)];
      if (requiredMatch) return '必修' + gradeDigit[numberOf(requiredMatch)];
      if (subject === 'english' && grade >= 10 && grade <= 16) {
        return grade <= 12 ? '必修' + gradeDigit[grade - 9] : '选必' + gradeDigit[grade - 12];
      }
      if (subject === 'physics' && grade >= 10 && grade <= 15) {
        return grade <= 12 ? '必修' + gradeDigit[grade - 9] : '选必' + gradeDigit[grade - 12];
      }
    }
    return '';
  }

  /** Subject: prefer the explicit subject; otherwise cne_ means English, cnp_ means physics, cnc_ means Chinese, and other IDs default to math. */
  function subjectOf(topic) {
    if (!topic) return 'math';
    if (topic.subject === 'english' || topic.subject === 'math' || topic.subject === 'physics' || topic.subject === 'chinese') return topic.subject;
    if (String(topic.id || '').indexOf('cne_') === 0) return 'english';
    if (String(topic.id || '').indexOf('cnp_') === 0) return 'physics';
    if (String(topic.id || '').indexOf('cnc_') === 0) return 'chinese';
    return 'math';
  }

  /**
   * Full-grade / full-volume topics: '一年级' = 一上 + 一下; '七上' = Grade 7, semester 1.
   * High-school courses are not split into semesters: '高一' / '高一必修' = required volume 1; '高二' / '高二必修' = required volume 2.
   * '选必一' / '选择性必修第一册', '选必二', and '选必三' refer to the three selective-required volumes.
   * High-school English uses '必修一', '必修二', '必修三', and '选必四', not math's '高一' and '高二'.
   * The default subject is math so that English scopes such as 三上, 四上, and 选必一 are not mixed with math.
   * Without a subject, '必修一' has no math topics and returns null.
   * Returns {ids, volumes, label} (IDs in topic-file order, containing official topics only); unrecognized formats return null.
   */
  function gradeTargets(graph, scope, subject) {
    const subj = subject == null || subject === '' ? 'math' : subject;
    const key = String(scope == null ? '' : scope).trim();
    const books = {
      '高一': ['高一', '高一（必修第一册）'],
      '高一必修': ['高一', '高一（必修第一册）'],
      '高二': ['高二', '高二（必修第二册）'],
      '高二必修': ['高二', '高二（必修第二册）'],
      '选必一': ['选必一', '选必一（选择性必修第一册）'],
      '选择性必修第一册': ['选必一', '选必一（选择性必修第一册）'],
      '选必二': ['选必二', '选必二（选择性必修第二册）'],
      '选择性必修第二册': ['选必二', '选必二（选择性必修第二册）'],
      '选必三': ['选必三', '选必三（选择性必修第三册）'],
      '选择性必修第三册': ['选必三', '选必三（选择性必修第三册）'],
      '必修一': ['必修一', '必修一（必修第一册）'],
      '必修第一册': ['必修一', '必修一（必修第一册）'],
      '必修二': ['必修二', '必修二（必修第二册）'],
      '必修第二册': ['必修二', '必修二（必修第二册）'],
      '必修三': ['必修三', '必修三（必修第三册）'],
      '必修第三册': ['必修三', '必修三（必修第三册）'],
      '选必四': ['选必四', '选必四（选择性必修第四册）'],
      '选择性必修第四册': ['选必四', '选必四（选择性必修第四册）']
    };
    let volumes = null;
    let label = '';
    if (books[key]) {
      volumes = [books[key][0]];
      label = books[key][1];
    } else {
      const g = /^([一二三四五六七八九])年级$/.exec(key);
      const v = /^([一二三四五六七八九])([上下])$/.exec(key);
      const whole = /^([一二三四五六七八九])全$/.exec(key);
      if (g) {
        volumes = [g[1] + '上', g[1] + '下'];
        if (g[1] === '九') volumes.push('九全');
        label = g[1] + '年级';
      } else if (whole) {
        volumes = [whole[1] + '全'];
        label = whole[1] + '年级全一册';
      } else if (v) { volumes = [key]; label = v[1] + '年级' + (v[2] === '上' ? '上册' : '下册'); }
    }
    if (!volumes) return null;
    const ids = graph.topics.filter(function (t) {
      if (t.external) return false;
      if (subj !== 'all' && subjectOf(t) !== subj) return false;
      return volumes.indexOf(parseChapter(t.chapter, t).volume) >= 0;
    }).map(function (t) { return t.id; });
    return ids.length ? { ids: ids, volumes: volumes, label: label } : null;
  }

  /**
   * Chapter summary: counts of mastered / shaky / weak / untested topics in each chapter, plus IDs of weak and shaky topics in scope.
   * Chapters follow textbook order, then use a stable sort by number of weak and shaky topics, with weaker chapters first.
   */
  function chapterSummary(graph, session) {
    const inOrder = new Set(session.order);
    const byKey = Object.create(null);
    const list = [];
    graph.topics.forEach(function (t) {
      if (t.external || !inOrder.has(t.id)) return;
      const c = parseChapter(t.chapter, t);
      const key = c.volume + ' ' + c.chapterNo + ' ' + c.chapterName;
      let ch = byKey[key];
      if (!ch) {
        ch = byKey[key] = {
          key: key, volume: c.volume, chapterNo: c.chapterNo, chapterName: c.chapterName,
          label: [c.volume, c.chapterNo, c.chapterName].filter(Boolean).join(' '),
          total: 0, mastered: 0, shaky: 0, weak: 0, untested: 0, weakIds: [], shakyIds: [], untestedIds: [], _i: list.length
        };
        list.push(ch);
      }
      const st = statusOf(session, t.id);
      ch.total++;
      if (st === 'mastered') ch.mastered++;
      else if (st === 'shaky') { ch.shaky++; ch.shakyIds.push(t.id); }
      else if (st === 'weak') { ch.weak++; ch.weakIds.push(t.id); }
      else { ch.untested++; ch.untestedIds.push(t.id); }
    });
    list.sort(function (a, b) { return b.weak - a.weak || b.shaky - a.shaky || a._i - b._i; });
    list.forEach(function (ch) { delete ch._i; });
    return list;
  }

  /**
   * Expand IDs from URLs or selectors into graph topics.
   * Aliases look like { "cnm_ext_002": { targets: ["cnm_p010", ...] } } or { id: ["cnm_p010"] }.
   * Preserve unknown IDs so createSession can report the error.
   */
  function resolveTargets(rawIds, aliases) {
    const map = aliases || {};
    const out = [];
    const seen = Object.create(null);
    (Array.isArray(rawIds) ? rawIds : [rawIds]).forEach(function (id) {
      if (!id) return;
      let targets = null;
      const spec = map[id];
      if (spec && Array.isArray(spec.targets)) targets = spec.targets;
      else if (Array.isArray(spec)) targets = spec;
      const list = targets && targets.length ? targets : [id];
      list.forEach(function (tid) {
        if (!seen[tid]) { seen[tid] = true; out.push(tid); }
      });
    });
    return out;
  }

  /* ------------------------------------------------------------------ Answer evaluation */

  function normalizeText(input) {
    let s = String(input == null ? '' : input);
    s = s.replace(/²/g, '^2').replace(/³/g, '^3').replace(/[º˚∘゜]/g, '°');
    s = s.normalize('NFKC'); // Convert full-width characters to half-width (digits, letters, punctuation, and operators).
    s = s.replace(/[−‐-―﹣]/g, '-')
      .replace(/[、]/g, ',')
      .replace(/[。]/g, '.')
      .replace(/[“”‘’]/g, '"')
      .replace(/[×·⋅∙]/g, '*')
      .replace(/÷/g, '/')
      .replace(/[≦⩽]/g, '≤').replace(/[≧⩾]/g, '≥')
      .replace(/<=/g, '≤').replace(/>=/g, '≥')
      .replace(/[\[\]{}]/g, function (c) { return c === '[' || c === '{' ? '(' : ')'; });
    s = s.replace(/(\d)\s*度/g, '$1°');
    s = s.replace(/(\d)\s+(\d+\s*\/\s*\d+)/g, '$1又$2'); // Mixed number, e.g. "1 1/2".
    s = s.replace(/\s+/g, '').toLowerCase();
    s = s.replace(/^(答案|答)[:=]/, '').replace(/或者/g, '或');
    s = s.replace(/[.!]+$/, '');
    if (/^[+-]?\d{1,3}(,\d{3})+(\.\d+)?$/.test(s)) s = s.replace(/,/g, ''); // Thousands separators.
    return s;
  }

  function splitTop(s, seps) {
    const parts = [];
    let depth = 0;
    let cur = '';
    for (let i = 0; i < s.length; i++) {
      const c = s[i];
      if (c === '(') depth++;
      else if (c === ')') depth = Math.max(0, depth - 1);
      if (depth === 0 && seps.indexOf(c) >= 0) { parts.push(cur); cur = ''; } else cur += c;
    }
    parts.push(cur);
    return parts.filter(function (p) { return p !== ''; });
  }

  function gcd(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { const t = a % b; a = b; b = t; } return a; }

  function ratio(n, d) {
    if (d === 0n) return null;
    if (d < 0n) { n = -n; d = -d; }
    const g = gcd(n, d) || 1n;
    return [n / g, d / g];
  }

  function decToRatio(str) {
    const i = str.indexOf('.');
    if (i < 0) return ratio(BigInt(str), 1n);
    const frac = str.slice(i + 1);
    const whole = str.slice(0, i) || '0';
    return ratio(BigInt(whole + frac), 10n ** BigInt(frac.length));
  }

  function isWrapped(t) {
    if (t[0] !== '(' || t[t.length - 1] !== ')') return false;
    let depth = 0;
    for (let i = 0; i < t.length; i++) {
      if (t[i] === '(') depth++;
      else if (t[i] === ')') { depth--; if (depth === 0 && i < t.length - 1) return false; }
    }
    return depth === 0;
  }

  const UNIT_ALIASES = {
    '米': 'm', 'm': 'm', '厘米': 'cm', 'cm': 'cm', '毫米': 'mm', 'mm': 'mm', '千米': 'km', '公里': 'km', 'km': 'km',
    '千克': 'kg', '公斤': 'kg', 'kg': 'kg', '克': 'g', 'g': 'g', '秒': 's', 's': 's', '分钟': 'min', 'min': 'min',
    '小时': 'h', 'h': 'h', '平方米': 'm^2', 'm^2': 'm^2', '平方厘米': 'cm^2', 'cm^2': 'cm^2',
    '立方米': 'm^3', 'm^3': 'm^3', '立方厘米': 'cm^3', 'cm^3': 'cm^3', '元': '元', '度': '°', '°': '°',
    // Physics: accept only multi-letter units; single letters (a, v, w, n, j) could be confused with math answers.
    'm/s': 'm/s', '米/秒': 'm/s', 'km/h': 'km/h', '千米/时': 'km/h', 'kg/m^3': 'kg/m^3', 'g/cm^3': 'g/cm^3',
    'pa': 'Pa', '帕': 'Pa', '帕斯卡': 'Pa', 'kpa': 'kPa', 'hz': 'Hz', '赫兹': 'Hz', 'db': 'dB', '分贝': 'dB',
    'kw*h': 'kW·h', '千瓦时': 'kW·h', 'ml': 'mL', '毫升': 'mL', 'n/kg': 'N/kg', 'j/kg': 'J/kg'
  };

  function canonUnit(u) {
    if (!u) return { name: '', known: true };
    if (UNIT_ALIASES[u]) return { name: UNIT_ALIASES[u], known: true };
    if (/^[一-龥]{1,4}$/.test(u)) return { name: u, known: false };
    return null; // Not a recognized unit, so this is not a "number + unit" answer.
  }

  /** Parse an integer, decimal, fraction a/b, mixed number, percentage, signed or parenthesized value, optionally followed by a unit. Return null on failure. */
  function parseNumeric(str) {
    let t = str;
    let neg = false;
    for (let guard = 0; guard < 4; guard++) {
      if (isWrapped(t)) { t = t.slice(1, -1); continue; }
      if ((t[0] === '-' || t[0] === '+') && isWrapped(t.slice(1))) { if (t[0] === '-') neg = !neg; t = t.slice(2, -1); continue; }
      break;
    }
    const m = /^([+-]?)(?:(\d+)又)?(\d+(?:\.\d+)?|\.\d+)(?:\/(\d+(?:\.\d+)?|\.\d+))?(%|°)?(.*)$/.exec(t);
    if (!m) return null;
    const whole = m[2], numS = m[3], denS = m[4], mark = m[5];
    let rest = m[6];
    if (whole && !denS) return null;
    let val;
    if (whole) {
      const n = decToRatio(numS), d = decToRatio(denS);
      if (!n || !d || d[0] === 0n) return null;
      const f = ratio(n[0] * d[1], n[1] * d[0]);
      const w = ratio(BigInt(whole), 1n);
      val = ratio(w[0] * f[1] + f[0], f[1]);
    } else if (denS) {
      const n = decToRatio(numS), d = decToRatio(denS);
      if (!n || !d || d[0] === 0n) return null;
      val = ratio(n[0] * d[1], n[1] * d[0]);
    } else {
      val = decToRatio(numS);
    }
    if (!val) return null;
    if (m[1] === '-') neg = !neg;
    let n = neg ? -val[0] : val[0];
    let d = val[1];
    let unit = { name: '', known: true };
    if (mark === '%') {
      const r = ratio(n, d * 100n);
      n = r[0]; d = r[1];
      if (rest) return null;
    } else if (mark === '°') {
      unit = { name: '°', known: true };
      if (!/^[一-龥]{0,2}$/.test(rest)) return null;
    } else if (rest) {
      unit = canonUnit(rest);
      if (!unit) return null;
    }
    return { key: n + '/' + d, unit: unit };
  }

  function analyzePart(p) {
    let variable = '';
    let body = p;
    const m = /^([a-z](?:\([a-z]\))?)=(.+)$/.exec(p);
    if (m) { variable = m[1]; body = m[2]; }
    const num = parseNumeric(body);
    if (num) return { raw: p, variable: variable, kind: 'num', key: num.key, unit: num.unit };
    const tm = /^\((.+)\)$/.exec(body);
    if (tm) {
      const items = splitTop(tm[1], ',');
      const nums = items.map(parseNumeric);
      if (items.length > 1 && nums.every(Boolean)) {
        return { raw: p, variable: variable, kind: 'tuple', key: 't:' + nums.map(function (x) { return x.key; }).join(','), unit: { name: '', known: true } };
      }
    }
    return { raw: p, variable: variable, kind: 'text', key: body, unit: { name: '', known: true } };
  }

  function parseAnswer(input) {
    const norm = normalizeText(input);
    const parts = splitTop(norm.replace(/[和或与及]/g, ','), ',;').map(analyzePart);
    return { norm: norm, parts: parts };
  }

  // 'eq' | 'ne' | 'unsure'
  function partCompare(a, b) {
    if (a.kind !== b.kind || a.key !== b.key) return 'ne';
    const ua = a.unit, ub = b.unit;
    if (!ua.name || !ub.name || ua.name === ub.name) return 'eq';
    return ua.known && ub.known ? 'ne' : 'unsure';
  }

  function sameMultiset(as, bs, ignoreVar) {
    if (as.length !== bs.length) return null;
    const left = bs.slice();
    let fuzzy = false;
    for (let i = 0; i < as.length; i++) {
      let hit = -1;
      for (let j = 0; j < left.length; j++) {
        if (!ignoreVar && as[i].variable !== left[j].variable) continue;
        const c = partCompare(as[i], left[j]);
        if (c === 'ne') continue;
        if (c === 'unsure') fuzzy = true;
        hit = j;
        break;
      }
      if (hit < 0) return null;
      left.splice(hit, 1);
    }
    return fuzzy ? 'unsure' : 'eq';
  }

  function allNumeric(parts) { return parts.every(function (p) { return p.kind === 'num' || p.kind === 'tuple'; }); }

  function compareParsed(u, r) {
    let res = null;
    if (u.parts.length === r.parts.length) {
      const refVars = r.parts.map(function (p) { return p.variable; });
      const refVarsDistinct = r.parts.length > 1 && refVars.every(Boolean) && new Set(refVars).size === refVars.length;
      if (refVarsDistinct) {
        if (u.parts.every(function (p) { return p.variable; })) res = sameMultiset(u.parts, r.parts, false);
        else if (u.parts.every(function (p) { return !p.variable; })) {
          // When variable names are omitted, match values in the reference-answer order (x before y).
          res = 'eq';
          for (let i = 0; i < u.parts.length; i++) {
            const c = partCompare(u.parts[i], r.parts[i]);
            if (c === 'ne') { res = null; break; }
            if (c === 'unsure') res = 'unsure';
          }
        } else return { relation: 'unsure' };
      } else {
        res = sameMultiset(u.parts, r.parts, true);
      }
    }
    if (res === 'eq') return { relation: 'equal' };
    if (res === 'unsure') return { relation: 'unsure' };
    return { relation: allNumeric(u.parts) && allNumeric(r.parts) ? 'different' : 'unsure' };
  }

  /**
   * Evaluate answers only when the comparison is reliable; otherwise return manual for the user to compare with the reference.
   *  - Identical after normalization, or equivalent numeric / unordered multi-answer values -> correct
   *  - Both parse as numeric values (including coordinates) but are not equivalent -> wrong
   *  - All other cases (algebraic expressions, text, multiple valid forms) -> manual
   */
  function judgeAnswer(user, reference) {
    const u = parseAnswer(user);
    const r = parseAnswer(reference);
    if (!u.norm) return { verdict: 'manual', reason: 'empty' };
    if (u.norm === r.norm) return { verdict: 'correct', reason: 'identical' };
    if (!r.parts.length) return { verdict: 'manual', reason: 'no-reference' };
    const c = compareParsed(u, r);
    if (c.relation === 'equal') return { verdict: 'correct', reason: 'equivalent' };
    if (c.relation === 'different') return { verdict: 'wrong', reason: 'numeric-mismatch' };
    return { verdict: 'manual', reason: 'unsure' };
  }

  /* ------------------------------------------------------------------ Type-specific evaluation */

  const MANUAL_EMPTY = { verdict: 'manual', reason: 'empty' };

  function judgeChoice(user, q) {
    const raw = String(user == null ? '' : user).trim();
    if (!raw) return MANUAL_EMPTY;
    const choices = q.choices || [];
    const keys = choices.map(function (c) { return c.key; });
    let letter = null;
    const m = /^[(（]?([A-Za-z])[)）.．、:：]?$/.exec(raw);
    if (m) letter = m[1].toUpperCase();
    else {
      const n = normalizeText(raw);
      const hit = choices.find(function (c) { return normalizeText(c.text) === n; });
      if (hit) letter = hit.key;
    }
    if (!letter || keys.indexOf(letter) < 0) return { verdict: 'manual', reason: 'unrecognized' };
    return letter === q.answer ? { verdict: 'correct', reason: 'choice' } : { verdict: 'wrong', reason: 'choice' };
  }

  function judgeNumeric(user, q) {
    const u = parseAnswer(user);
    if (!u.norm) return MANUAL_EMPTY;
    const refs = [q.answer].concat(q.accept || []);
    for (let i = 0; i < refs.length; i++) {
      if (parseAnswer(refs[i]).norm === u.norm) return { verdict: 'correct', reason: 'identical' };
    }
    const main = parseAnswer(q.answer);
    if (!q.unordered && main.parts.length > 1) {
      // When answer order matters, compare each value in order (ignoring variable names).
      if (u.parts.length !== main.parts.length) {
        return allNumeric(u.parts) ? { verdict: 'wrong', reason: 'count-mismatch' } : { verdict: 'manual', reason: 'unsure' };
      }
      let res = 'eq';
      for (let i = 0; i < u.parts.length; i++) {
        const c = partCompare(u.parts[i], main.parts[i]);
        if (c === 'ne') { res = 'ne'; break; }
        if (c === 'unsure') res = 'unsure';
      }
      if (res === 'eq') return { verdict: 'correct', reason: 'equivalent' };
      if (res === 'ne' && allNumeric(u.parts) && allNumeric(main.parts)) return { verdict: 'wrong', reason: 'numeric-mismatch' };
      return { verdict: 'manual', reason: 'unsure' };
    }
    const r = judgeAnswer(user, q.answer);
    if (r.verdict === 'correct') return r;
    for (let i = 1; i < refs.length; i++) {
      if (judgeAnswer(user, refs[i]).verdict === 'correct') return { verdict: 'correct', reason: 'accept' };
    }
    return r;
  }

  function judgeShort(user, q) {
    const u = normalizeText(user);
    if (!u) return MANUAL_EMPTY;
    const refs = [q.answer].concat(q.accept || []);
    for (let i = 0; i < refs.length; i++) {
      if (normalizeText(refs[i]) === u) return { verdict: 'correct', reason: i ? 'accept' : 'identical' };
    }
    for (let i = 0; i < refs.length; i++) {
      if (judgeAnswer(user, refs[i]).verdict === 'correct') return { verdict: 'correct', reason: 'equivalent' };
    }
    return { verdict: 'manual', reason: 'unsure' }; // Text and algebraic answers have too many valid forms for reliable automatic evaluation.
  }

  /** Evaluate by question type: choice compares a letter or option text; numeric checks numeric equivalence; short uses normalized exact match plus accept; self is always manual. */
  /**
   * For questions with percent:true (currently only physics efficiency questions), answer is the numeric percentage value, e.g. 50 means 50%.
   * Accept 50 or 50% (including full-width ％); do not accept 0.5 because the question asks for a percentage and 0.5 may mean 0.5%.
   * Questions without percent (all math questions) do not use this path; 50% is still interpreted as 0.5.
   */
  function stripPercent(user) {
    const s = String(user == null ? '' : user).trim();
    return s.replace(/\s*[%％]$/, '');
  }

  function judgeQuestion(q, user) {
    switch (q.type) {
      case 'choice': return judgeChoice(user, q);
      case 'numeric': return judgeNumeric(q.percent === true ? stripPercent(user) : user, q);
      case 'short': return judgeShort(user, q);
      case 'self': return { verdict: 'manual', reason: 'self' };
      default: return judgeAnswer(user, q.answer); // Legacy question from diagnostic_question.
    }
  }

  return {
    DEFAULT_LIMIT: DEFAULT_LIMIT,
    SCREEN_LIMIT: SCREEN_LIMIT,
    DEFAULT_CONFIRM: DEFAULT_CONFIRM,
    CONFIRM_CHOICES: CONFIRM_CHOICES.slice(),
    clampConfirm: clampConfirm,
    normalizeConfirm: normalizeConfirm,
    needConfirm: needConfirm,
    gradeTargets: gradeTargets,
    subjectOf: subjectOf,
    chapterSummary: chapterSummary,
    buildGraph: buildGraph,
    questionById: questionById,
    pickQuestion: pickQuestion,
    nextItem: nextItem,
    isUnconfirmed: isUnconfirmed,
    mulberry32: mulberry32,
    judgeQuestion: judgeQuestion,
    ancestors: ancestors,
    topoSort: topoSort,
    subgraph: subgraph,
    isTestable: isTestable,
    createSession: createSession,
    applyAnswer: applyAnswer,
    nextQuestion: nextQuestion,
    replay: replay,
    statusOf: statusOf,
    summarize: summarize,
    layout: layout,
    parseChapter: parseChapter,
    gradeRank: gradeRank,
    resolveTargets: resolveTargets,
    normalizeText: normalizeText,
    judgeAnswer: judgeAnswer
  };
});
