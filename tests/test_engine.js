#!/usr/bin/env node
/* Diagnostic engine tests: node tests/test_engine.js (no dependencies; uses assert). */
'use strict';
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const E = require('../diagnose/engine.js');

let passed = 0;
let failed = 0;
function test(name, fn) {
  try { fn(); passed++; console.log('  ok   ' + name); }
  catch (e) { failed++; console.log('  FAIL ' + name + '\n       ' + (e && e.stack || e).split('\n').slice(0, 4).join('\n       ')); }
}
const sorted = (it) => Array.from(it).sort();

/* ------------------------------------------------------------ Hand-built graph
 *   X(external) <- F <- E <- C <---hard--- T
 *              F <- D <---hard--- T
 *              F <- B <---soft--- T
 *   Z is unrelated to T.
 * Topic order: X F E C D B T Z (prerequisites at the same level are asked in this order).
 */
function mk(id, extra) {
  return Object.assign({
    id: id, name: id, external: false,
    diagnostic_question: { question: id + '?', answer: '1' }
  }, extra || {});
}
const smallTopics = [
  mk('X', { external: true, diagnostic_question: undefined }),
  mk('F'), mk('E'), mk('C'), mk('D'), mk('B'), mk('T'), mk('Z')
];
const smallDeps = [
  { topicId: 'F', prerequisiteId: 'X', strength: 'hard' },
  { topicId: 'E', prerequisiteId: 'F', strength: 'hard' },
  { topicId: 'C', prerequisiteId: 'E', strength: 'hard' },
  { topicId: 'D', prerequisiteId: 'F', strength: 'hard' },
  { topicId: 'B', prerequisiteId: 'F', strength: 'hard' },
  { topicId: 'T', prerequisiteId: 'B', strength: 'soft' },   // Deliberately place soft before hard.
  { topicId: 'T', prerequisiteId: 'D', strength: 'hard' },
  { topicId: 'T', prerequisiteId: 'C', strength: 'hard' }
];
const G = E.buildGraph(smallTopics, smallDeps);

function run(session, script) {
  // script: {id: 'correct'|'wrong'|'skip'}; answer in engine question order and return [session, question order].
  const asked = [];
  let s = session;
  for (let guard = 0; guard < 100; guard++) {
    const q = E.nextQuestion(G, s);
    if (!q) break;
    asked.push(q);
    assert.ok(script[q], 'Script has no answer for ' + q);
    s = E.applyAnswer(G, s, q, script[q]);
  }
  return [s, asked];
}

function assertTopological(order, graph) {
  const pos = new Map(order.map((id, i) => [id, i]));
  order.forEach((id) => {
    graph.prereqs[id].forEach((p) => {
      if (pos.has(p.id)) assert.ok(pos.get(p.id) < pos.get(id), p.id + ' should come before ' + id);
    });
  });
}

console.log('Small hand-built graph (one question per topic — fallback mode: an incorrect answer immediately marks the topic weak)');

test('Ancestor subgraph: target plus all ancestors (including external nodes), excluding unrelated topics', () => {
  assert.deepStrictEqual(sorted(E.ancestors(G, 'T')), ['B', 'C', 'D', 'E', 'F', 'X']);
  assert.deepStrictEqual(sorted(E.ancestors(G, 'E')), ['F', 'X']);
  assert.deepStrictEqual(sorted(E.ancestors(G, 'X')), []);
  const sub = E.subgraph(G, ['T']);
  assert.deepStrictEqual(sorted(sub.nodes), ['B', 'C', 'D', 'E', 'F', 'T', 'X']);
});

test('Topological order: every prerequisite comes before the topic that depends on it', () => {
  const sub = E.subgraph(G, ['T']);
  assertTopological(sub.nodes, G);
  assert.strictEqual(sub.nodes[0], 'X');
  assert.strictEqual(sub.nodes[sub.nodes.length - 1], 'T');
  const multi = E.subgraph(G, ['C', 'D']);
  assertTopological(multi.nodes, G);
  assert.deepStrictEqual(sorted(multi.nodes), ['C', 'D', 'E', 'F', 'X']);
});

test('Hard prerequisites are ordered before soft prerequisites', () => {
  assert.deepStrictEqual(G.prereqs.T.map((p) => p.id + ':' + p.strength), ['C:hard', 'D:hard', 'B:soft']);
});

test('The first question assesses the target itself', () => {
  const s = E.createSession(G, ['T']);
  assert.strictEqual(E.nextQuestion(G, s), 'T');
});

test('Correct answer: mark the topic and all ancestors (including external nodes) as mastered and skip them', () => {
  let s = E.createSession(G, ['T']);
  s = E.applyAnswer(G, s, 'T', 'correct');
  assert.strictEqual(E.nextQuestion(G, s), null);
  ['B', 'C', 'D', 'E', 'F', 'X', 'T'].forEach((id) => assert.strictEqual(E.statusOf(s, id), 'mastered', id));
  assert.strictEqual(s.status.T.src, 'direct');
  assert.strictEqual(s.status.F.src, 'inferred');
  assert.strictEqual(E.statusOf(s, 'Z'), 'unknown');
  const sum = E.summarize(G, s);
  assert.deepStrictEqual(sum.weak, []);
  assert.deepStrictEqual(sum.roots, []);
  assert.deepStrictEqual(sum.path, []);
  assert.strictEqual(sum.asked, 1);
});

test('Incorrect answer: trace prerequisites depth-first, with hard before soft', () => {
  const s0 = E.createSession(G, ['T']);
  const [s, asked] = run(s0, { T: 'wrong', C: 'wrong', E: 'correct', D: 'correct', B: 'correct' });
  // T miss -> hard prerequisites C and D (in file order), then soft B; after C is missed, ask its prerequisite E before returning to D and B.
  assert.deepStrictEqual(asked, ['T', 'C', 'E', 'D', 'B']);
  assert.strictEqual(E.nextQuestion(G, s), null);
});

test('After a miss, the first follow-up is a hard prerequisite and soft prerequisites come last', () => {
  let s = E.createSession(G, ['T']);
  s = E.applyAnswer(G, s, 'T', 'wrong');
  assert.strictEqual(E.nextQuestion(G, s), 'C');
  s = E.applyAnswer(G, s, 'C', 'correct'); // Correct on C -> E, F, and X are mastered.
  assert.strictEqual(E.nextQuestion(G, s), 'D');
  s = E.applyAnswer(G, s, 'D', 'correct');
  assert.strictEqual(E.nextQuestion(G, s), 'B');
});

test('Skip is equivalent to an incorrect answer', () => {
  const [a] = run(E.createSession(G, ['T']), { T: 'skip', C: 'skip', E: 'correct', D: 'correct', B: 'correct' });
  const [b] = run(E.createSession(G, ['T']), { T: 'wrong', C: 'wrong', E: 'correct', D: 'correct', B: 'correct' });
  assert.deepStrictEqual(a.status, b.status);
});

test('Do not repeat decided topics; ask shared prerequisites only once', () => {
  const [, asked] = run(E.createSession(G, ['T']), { T: 'wrong', C: 'wrong', E: 'wrong', F: 'correct', D: 'wrong', B: 'wrong' });
  assert.strictEqual(new Set(asked).size, asked.length);
  assert.deepStrictEqual(asked, ['T', 'C', 'E', 'F', 'D', 'B']);
});

test('Question limit is enforced and remaining topics are marked untested', () => {
  const s0 = E.createSession(G, ['T'], { limit: 2 });
  const [s, asked] = run(s0, { T: 'wrong', C: 'wrong' });
  assert.deepStrictEqual(asked, ['T', 'C']);
  assert.strictEqual(E.nextQuestion(G, s), null);
  const sum = E.summarize(G, s);
  assert.strictEqual(sum.asked, 2);
  assert.strictEqual(sum.limitReached, true);
  assert.deepStrictEqual(sorted(sum.untested), ['B', 'D', 'E', 'F', 'X']);
  assert.deepStrictEqual(sorted(sum.weak), ['C', 'T']);
  // Root cause C has an untested prerequisite E; report it.
  assert.deepStrictEqual(sum.roots.map((r) => r.id), ['C']);
  assert.deepStrictEqual(sum.roots[0].pendingPrereqs, ['E']);
});

test('Default limit is 16; limit=1 asks only the target', () => {
  assert.strictEqual(E.DEFAULT_LIMIT, 16);
  assert.strictEqual(E.createSession(G, ['T']).limit, 16);
  const s0 = E.createSession(G, ['T'], { limit: 1 });
  const [, asked] = run(s0, { T: 'wrong' });
  assert.deepStrictEqual(asked, ['T']);
});

test('Root cause: a weak topic with no weak prerequisites; path is topological and excludes mastered topics', () => {
  const [s] = run(E.createSession(G, ['T']), { T: 'wrong', C: 'wrong', E: 'correct', D: 'correct', B: 'correct' });
  const sum = E.summarize(G, s);
  assert.deepStrictEqual(sorted(sum.weak), ['C', 'T']);
  assert.deepStrictEqual(sum.roots.map((r) => r.id), ['C']);
  assert.deepStrictEqual(sum.path.map((p) => p.id), ['C', 'T']);
  assert.strictEqual(sum.path[0].isRoot, true);
  assert.strictEqual(sum.path[1].isTarget, true);
  assert.deepStrictEqual(sorted(sum.mastered), ['B', 'D', 'E', 'F', 'X']);
  assert.strictEqual(sum.finished, true);
  assert.strictEqual(sum.limitReached, false);
});

test('Multiple root causes: path includes all unmastered topics between root causes and target, in topological order', () => {
  // T, C, E, and D are weak; F and B are mastered, so E and D are root causes.
  const [s] = run(E.createSession(G, ['T']), { T: 'wrong', C: 'wrong', E: 'wrong', F: 'correct', D: 'wrong', B: 'correct' });
  const sum = E.summarize(G, s);
  assert.deepStrictEqual(sorted(sum.roots.map((r) => r.id)), ['D', 'E']);
  assert.deepStrictEqual(sorted(sum.path.map((p) => p.id)), ['C', 'D', 'E', 'T']);
  assertTopological(sum.path.map((p) => p.id), G);
  sum.path.forEach((p) => assert.notStrictEqual(p.status, 'mastered'));
  assert.deepStrictEqual(sum.path.filter((p) => p.isRoot).map((p) => p.id).sort(), ['D', 'E']);
});

test('External elementary nodes are not assessed; external prerequisites of root causes are reported separately', () => {
  const [s, asked] = run(E.createSession(G, ['T']), { T: 'wrong', C: 'wrong', E: 'wrong', F: 'wrong', D: 'wrong', B: 'wrong' });
  assert.ok(!asked.includes('X'));
  const sum = E.summarize(G, s);
  assert.deepStrictEqual(sum.roots.map((r) => r.id), ['F']);
  assert.deepStrictEqual(sum.roots[0].externalPrereqs, ['X']);
  assert.deepStrictEqual(sum.roots[0].pendingPrereqs, []);
  assert.deepStrictEqual(sum.untested, ['X']);
});

test('Multiple targets: ask the closest target first; a correct answer covers its ancestor targets', () => {
  const s0 = E.createSession(G, ['C', 'T', 'D']);
  assert.strictEqual(E.nextQuestion(G, s0), 'T');
  const s1 = E.applyAnswer(G, s0, 'T', 'correct');
  assert.strictEqual(E.nextQuestion(G, s1), null);
  assert.deepStrictEqual(E.summarize(G, s1).path, []);
});

test('Multiple unrelated targets are all assessed', () => {
  const s0 = E.createSession(G, ['T', 'Z']);
  const [, asked] = run(s0, { T: 'correct', Z: 'correct' });
  assert.deepStrictEqual(sorted(asked), ['T', 'Z']);
});

test('A direct answer is not overwritten by an inferred status', () => {
  let s = E.createSession(G, ['T']);
  s = E.applyAnswer(G, s, 'E', 'wrong');
  s = E.applyAnswer(G, s, 'T', 'correct');
  assert.strictEqual(E.statusOf(s, 'E'), 'weak');
  assert.strictEqual(E.statusOf(s, 'C'), 'mastered');
});

test('applyAnswer does not mutate inputs; replay matches step-by-step answers', () => {
  const s0 = E.createSession(G, ['T']);
  const snap = JSON.stringify(s0);
  const s1 = E.applyAnswer(G, s0, 'T', 'wrong');
  assert.strictEqual(JSON.stringify(s0), snap);
  const s2 = E.applyAnswer(G, s1, 'C', 'correct');
  const r = E.replay(G, ['T'], [{ id: 'T', result: 'wrong' }, { id: 'C', result: 'correct' }]);
  assert.deepStrictEqual(r, s2);
  assert.deepStrictEqual(JSON.parse(JSON.stringify(s2)), s2); // JSON serializable.
  assert.throws(() => E.applyAnswer(G, s0, 'T', 'maybe'));
  assert.throws(() => E.createSession(G, ['nope']));
});

test('Path graph layout: prerequisites are above dependents, and edges do not run backward', () => {
  const [s] = run(E.createSession(G, ['T']), { T: 'wrong', C: 'wrong', E: 'wrong', F: 'correct', D: 'wrong', B: 'correct' });
  const sum = E.summarize(G, s);
  const lay = E.layout(G, s, sum);
  const layer = Object.fromEntries(lay.nodes.map((n) => [n.id, n.layer]));
  lay.edges.forEach((e) => assert.ok(layer[e.from] < layer[e.to], e.from + '->' + e.to));
  assert.ok(lay.nodes.some((n) => n.id === 'T' && n.isTarget));
  assert.ok(lay.nodes.some((n) => n.id === 'E' && n.isRoot));
});


/* ------------------------------------------------------------ Two-attempt evaluation (hand-built question bank) */
console.log('Two-attempt evaluation');

const DIFFS = { b: 'basic', s: 'standard', a: 'advanced' };
function mq(topicId, n, diff, extra) {
  return Object.assign({
    id: topicId + '_q' + n, topicId: topicId, difficulty: DIFFS[diff] || diff, type: 'numeric',
    prompt: topicId + ' question ' + n, answer: '1', explanation: 'Explanation'
  }, extra || {});
}
// T prerequisites: P1 (hard) <- R and P2 (hard); four questions per topic: q1 standard, q2 standard, q3 basic, q4 advanced.
const bankTopics = ['R', 'P1', 'P2', 'T'].map((id) => mk(id, { diagnostic_question: undefined }));
const bankDeps = [
  { topicId: 'P1', prerequisiteId: 'R', strength: 'hard' },
  { topicId: 'T', prerequisiteId: 'P1', strength: 'hard' },
  { topicId: 'T', prerequisiteId: 'P2', strength: 'hard' }
];
const bankQs = [];
['R', 'P1', 'P2', 'T'].forEach((id) => {
  bankQs.push(mq(id, 1, 's'), mq(id, 2, 's'), mq(id, 3, 'b'), mq(id, 4, 'a'));
});
const G2 = E.buildGraph(bankTopics, bankDeps, bankQs);

/** Answer from a script: script[id] = [first result, second result]; return [session, sequence of (topic#attempt)]. */
function run2(session, script) {
  const seq = [];
  let s = session;
  for (let guard = 0; guard < 100; guard++) {
    const it = E.nextItem(G2, s);
    if (!it) break;
    seq.push(it.topicId + '#' + it.attempt);
    const r = script[it.topicId][it.attempt - 1];
    assert.ok(r, 'Script is missing answer for ' + it.topicId + ' question ' + it.attempt);
    s = E.applyAnswer(G2, s, it.topicId, r);
  }
  return [s, seq];
}

test('Question bank: isTestable uses the bank; hasBank is true with a bank and false in fallback mode', () => {
  assert.strictEqual(G2.hasBank, true);
  assert.strictEqual(G.hasBank, false);
  assert.strictEqual(G2.bank.T.length, 4);
  assert.strictEqual(G.bank.T[0].type, 'legacy');
});

test('confirm=1: one correct answer marks the topic and its ancestors mastered; asks one question', () => {
  const [s, seq] = run2(E.createSession(G2, ['T'], { confirm: 1 }), { T: ['correct'] });
  assert.deepStrictEqual(seq, ['T#1']);
  ['T', 'P1', 'P2', 'R'].forEach((id) => assert.strictEqual(E.statusOf(s, id), 'mastered', id));
  assert.strictEqual(s.status.T.src, 'direct');
  assert.strictEqual(s.status.R.src, 'inferred');
});

test('Default confirm=3: three consecutive correct answers are required for mastery; one correct answer is not enough', () => {
  let s = E.createSession(G2, ['T']);
  assert.strictEqual(s.confirm, 3);
  assert.strictEqual(E.needConfirm(G2, s, 'T'), 3);
  s = E.applyAnswer(G2, s, 'T', 'correct');
  assert.strictEqual(s.status.T, undefined);
  assert.strictEqual(E.nextQuestion(G2, s), 'T');
  assert.strictEqual(E.nextItem(G2, s).attempt, 2);
  s = E.applyAnswer(G2, s, 'T', 'correct');
  assert.strictEqual(s.status.T, undefined);
  s = E.applyAnswer(G2, s, 'T', 'correct');
  assert.strictEqual(E.statusOf(s, 'T'), 'mastered');
  ['P1', 'P2', 'R'].forEach((id) => assert.strictEqual(E.statusOf(s, id), 'mastered', id));
  assert.strictEqual(E.nextQuestion(G2, s), null);
});

test('With confirm=3 and only two bank questions, two correct answers are enough for mastery', () => {
  const topics2 = [mk('M', { diagnostic_question: undefined })];
  const qs2 = [mq('M', 1, 's'), mq('M', 2, 'b')];
  const Gx = E.buildGraph(topics2, [], qs2);
  let s2 = E.createSession(Gx, ['M'], { confirm: 3 });
  assert.strictEqual(E.needConfirm(Gx, s2, 'M'), 2);
  s2 = E.applyAnswer(Gx, s2, 'M', 'correct');
  assert.strictEqual(s2.status.M, undefined);
  s2 = E.applyAnswer(Gx, s2, 'M', 'correct');
  assert.strictEqual(E.statusOf(s2, 'M'), 'mastered');
});

test('Invalid confirm values fall back to 3; valid options are 2/3/5', () => {
  assert.strictEqual(E.clampConfirm(2), 2);
  assert.strictEqual(E.clampConfirm(5), 5);
  assert.strictEqual(E.clampConfirm(4), 3);
  assert.strictEqual(E.clampConfirm('x'), 3);
  assert.strictEqual(E.createSession(G2, ['T'], { confirm: 5 }).confirm, 5);
});

test('After a miss on the first question, ask a second question for the same topic without deciding or tracing prerequisites yet', () => {
  let s = E.createSession(G2, ['T']);
  s = E.applyAnswer(G2, s, 'T', 'wrong');
  assert.strictEqual(E.nextQuestion(G2, s), 'T');
  const it = E.nextItem(G2, s);
  assert.strictEqual(it.attempt, 2);
  assert.notStrictEqual(it.question.id, s.answers[0].qid);
  assert.strictEqual(s.status.T, undefined);
  assert.strictEqual(E.isUnconfirmed(s, 'T'), true);
});

test('Two misses mark a topic weak and trace prerequisites (P1, P2, then R)', () => {
  // confirm=1: one correct answer masters a prerequisite, making trace order easy to verify.
  const [s, seq] = run2(E.createSession(G2, ['T'], { confirm: 1 }), {
    T: ['wrong', 'skip'], P1: ['wrong', 'wrong'], R: ['correct'], P2: ['correct']
  });
  assert.deepStrictEqual(seq, ['T#1', 'T#2', 'P1#1', 'P1#2', 'R#1', 'P2#1']);
  assert.strictEqual(E.statusOf(s, 'T'), 'weak');
  assert.strictEqual(E.statusOf(s, 'P1'), 'weak');
  assert.strictEqual(E.statusOf(s, 'R'), 'mastered');
  const sum = E.summarize(G2, s);
  assert.deepStrictEqual(sum.roots.map((r) => r.id), ['P1']);
  assert.deepStrictEqual(sum.shaky, []);
});

test('A miss followed by a correct answer marks the topic shaky without tracing prerequisites', () => {
  const [s, seq] = run2(E.createSession(G2, ['T']), { T: ['wrong', 'correct'] });
  assert.deepStrictEqual(seq, ['T#1', 'T#2']);
  assert.strictEqual(E.statusOf(s, 'T'), 'shaky');
  assert.strictEqual(E.nextQuestion(G2, s), null);
  ['P1', 'P2', 'R'].forEach((id) => assert.strictEqual(E.statusOf(s, id), 'unknown', id));
  const sum = E.summarize(G2, s);
  assert.deepStrictEqual(sum.shaky, ['T']);
  assert.deepStrictEqual(sum.weak, []);
  assert.deepStrictEqual(sum.roots, []);
  assert.deepStrictEqual(sorted(sum.untested), ['P1', 'P2', 'R']);
  // Topics needing review belong in the study path.
  assert.deepStrictEqual(sum.path.map((p) => [p.id, p.status]), [['T', 'shaky']]);
});

test('A shaky prerequisite that is weak in another branch and its descendants remain in the path', () => {
  const [s] = run2(E.createSession(G2, ['T'], { confirm: 1 }), {
    T: ['wrong', 'wrong'], P1: ['wrong', 'correct'], P2: ['wrong', 'wrong'], R: ['correct']
  });
  assert.strictEqual(E.statusOf(s, 'P1'), 'shaky');
  assert.strictEqual(E.statusOf(s, 'P2'), 'weak');
  const sum = E.summarize(G2, s);
  assert.deepStrictEqual(sum.roots.map((r) => r.id), ['P2']);
  assert.deepStrictEqual(sorted(sum.path.map((p) => p.id)), ['P1', 'P2', 'T']);
  assert.strictEqual(sum.path.find((p) => p.id === 'P1').status, 'shaky');
  assertTopological(sum.path.map((p) => p.id), G2);
});

test('Prefer standard for the first question, challenge after a correct answer, and basic after a miss', () => {
  for (let i = 0; i < 60; i++) {
    const s0 = E.createSession(G2, ['P2'], { seed: 'k' + i });
    const first = E.nextItem(G2, s0).question;
    assert.strictEqual(first.difficulty, 'standard', 'First question should be standard when available');
    const sWrong = E.applyAnswer(G2, s0, 'P2', 'wrong');
    assert.strictEqual(E.nextItem(G2, sWrong).question.id, 'P2_q3', 'After a miss, ask the only basic question');
    const sRight = E.applyAnswer(G2, s0, 'P2', 'correct');
    assert.strictEqual(E.nextItem(G2, sRight).question.difficulty, 'advanced', 'After a correct answer, use the advanced tier');
  }
  // Without standard questions, use basic first (not advanced).
  const topics3 = [mk('M', { diagnostic_question: undefined })];
  const qsB = [mq('M', 1, 'b'), mq('M', 2, 'b'), mq('M', 3, 'a')];
  const GB = E.buildGraph(topics3, [], qsB);
  for (let i = 0; i < 20; i++) {
    const it = E.nextItem(GB, E.createSession(GB, ['M'], { seed: i }));
    assert.strictEqual(it.question.difficulty, 'basic');
  }
  // Without basic questions, use a standard question after a miss.
  const qs3 = [mq('M', 1, 's'), mq('M', 2, 's'), mq('M', 3, 's'), mq('M', 4, 'a')];
  const G3 = E.buildGraph(topics3, [], qs3);
  for (let i = 0; i < 20; i++) {
    const s1 = E.applyAnswer(G3, E.createSession(G3, ['M'], { seed: i }), 'M', 'wrong');
    assert.strictEqual(E.nextItem(G3, s1).question.difficulty, 'standard');
  }
  // Use advanced questions when they are the only tier available.
  const qs4 = [mq('M', 1, 'a'), mq('M', 2, 'a')];
  const G4 = E.buildGraph(topics3, [], qs4);
  const s4 = E.applyAnswer(G4, E.createSession(G4, ['M'], { seed: 1 }), 'M', 'wrong');
  assert.strictEqual(E.nextItem(G4, s4).question.difficulty, 'advanced');
});

test('A fixed seed produces deterministic questions; different seeds can produce different selections', () => {
  const trace = (seed) => {
    const [s] = run2(E.createSession(G2, ['T'], { seed: seed }), {
      T: ['wrong', 'wrong'], P1: ['wrong', 'wrong'], R: ['wrong', 'wrong'], P2: ['wrong', 'wrong']
    });
    return s.answers.map((a) => a.qid).join(',');
  };
  assert.strictEqual(trace('abc'), trace('abc'));
  assert.strictEqual(trace(42), trace('42'));
  const variants = new Set();
  for (let i = 0; i < 40; i++) variants.add(trace('s' + i));
  assert.ok(variants.size > 5, 'Different seeds should produce different question sequences (got ' + variants.size + ')');
  // Replay matches step-by-step answers, including question IDs.
  const [s2] = run2(E.createSession(G2, ['T'], { seed: 9 }), { T: ['wrong', 'correct'] });
  const r = E.replay(G2, ['T'], s2.answers, { seed: 9 });
  assert.deepStrictEqual(r, s2);
});

test('Avoid previously asked questions when possible; do not get stuck when all have been used', () => {
  const avoid = ['T_q1', 'T_q2'];
  for (let i = 0; i < 40; i++) {
    const s0 = E.createSession(G2, ['T'], { seed: i, avoid: avoid });
    const first = E.nextItem(G2, s0).question;
    assert.ok(!avoid.includes(first.id), 'First question should avoid a previously used question: ' + first.id);
  }
  const all = G2.bank.T.map((q) => q.id);
  const s1 = E.createSession(G2, ['T'], { seed: 1, avoid: all });
  const it = E.nextItem(G2, s1);
  assert.ok(it && all.includes(it.question.id));
  // For the second question, basic takes precedence over unused: q3 is the only basic question, so use it even if already asked.
  let hit = 0;
  for (let i = 0; i < 40; i++) {
    const s0 = E.createSession(G2, ['T'], { seed: i, avoid: ['T_q3'] });
    const a1 = E.nextItem(G2, s0).question;
    if (a1.difficulty !== 'standard') continue;
    const s2 = E.applyAnswer(G2, s0, 'T', 'wrong');
    assert.strictEqual(E.nextItem(G2, s2).question.id, 'T_q3');
    hit++;
  }
  assert.ok(hit > 5);
  // Do not repeat a question within the same session.
  const [s3] = run2(E.createSession(G2, ['T']), { T: ['wrong', 'wrong'], P1: ['wrong', 'wrong'], P2: ['wrong', 'wrong'], R: ['wrong', 'wrong'] });
  const qids = s3.answers.map((a) => a.qid);
  assert.strictEqual(new Set(qids).size, qids.length);
});

test('Question limit counts questions: after one miss and reaching the limit, mark the topic weak and unconfirmed', () => {
  const [s, seq] = run2(E.createSession(G2, ['T'], { limit: 3 }), {
    T: ['wrong', 'wrong'], P1: ['wrong', 'wrong'], R: ['wrong', 'wrong'], P2: ['wrong', 'wrong']
  });
  assert.deepStrictEqual(seq, ['T#1', 'T#2', 'P1#1']);
  assert.strictEqual(s.answers.length, 3);
  assert.strictEqual(E.nextQuestion(G2, s), null);
  assert.strictEqual(E.statusOf(s, 'P1'), 'weak');
  const sum = E.summarize(G2, s);
  assert.deepStrictEqual(sum.unconfirmed, ['P1']);
  assert.strictEqual(sum.limitReached, true);
  assert.deepStrictEqual(sorted(sum.untested), ['P2', 'R']);
});

test('If a topic has only one question, a miss marks it weak immediately', () => {
  const G5 = E.buildGraph(bankTopics, bankDeps, [mq('T', 1, 's'), mq('P1', 1, 's'), mq('P2', 1, 's'), mq('R', 1, 's')]);
  let s = E.applyAnswer(G5, E.createSession(G5, ['T']), 'T', 'wrong');
  assert.strictEqual(E.statusOf(s, 'T'), 'weak');
  assert.strictEqual(E.nextQuestion(G5, s), 'P1');
});

test('applyAnswer does not mutate inputs (including attempts); answer records include qid and user answer', () => {
  const s0 = E.createSession(G2, ['T'], { seed: 5 });
  const snap = JSON.stringify(s0);
  const s1 = E.applyAnswer(G2, s0, 'T', 'wrong', { text: '42' });
  assert.strictEqual(JSON.stringify(s0), snap);
  assert.strictEqual(s1.answers[0].text, '42');
  assert.ok(/^T_q\d$/.test(s1.answers[0].qid));
  const snap1 = JSON.stringify(s1);
  E.applyAnswer(G2, s1, 'T', 'correct');
  assert.strictEqual(JSON.stringify(s1), snap1);
  assert.deepStrictEqual(JSON.parse(JSON.stringify(s1)), s1);
});

test('Question-type evaluation: choice accepts a key or option text; numeric checks equivalence; short uses exact match plus accept; self is manual', () => {
  const ch = { type: 'choice', answer: 'B', choices: [{ key: 'A', text: '1/2' }, { key: 'B', text: '-3' }, { key: 'C', text: '相切' }] };
  const j = (q, u) => E.judgeQuestion(q, u).verdict;
  assert.strictEqual(j(ch, 'B'), 'correct');
  assert.strictEqual(j(ch, ' b '), 'correct');
  assert.strictEqual(j(ch, '(B)'), 'correct');
  assert.strictEqual(j(ch, 'B.'), 'correct');
  assert.strictEqual(j(ch, 'A'), 'wrong');
  assert.strictEqual(j(ch, '-3'), 'correct');
  assert.strictEqual(j(ch, '－３'), 'correct');
  assert.strictEqual(j(ch, '1/2'), 'wrong');
  assert.strictEqual(j(ch, '相切'), 'wrong');
  assert.strictEqual(j(ch, 'E'), 'manual');
  assert.strictEqual(j(ch, '随便写'), 'manual');
  assert.strictEqual(j(ch, ''), 'manual');
  const num = { type: 'numeric', answer: '-1/2' };
  assert.strictEqual(j(num, '-0.5'), 'correct');
  assert.strictEqual(j(num, '－１/２'), 'correct');
  assert.strictEqual(j(num, '1/2'), 'wrong');
  const ord = { type: 'numeric', answer: '3，-2' };
  assert.strictEqual(j(ord, '3，-2'), 'correct');
  assert.strictEqual(j(ord, '3, -2'), 'correct');
  assert.strictEqual(j(ord, '-2，3'), 'wrong');       // Ordered answers: incorrect order.
  assert.strictEqual(j(ord, '3'), 'wrong');
  const unord = { type: 'numeric', answer: '3，-2', unordered: true };
  assert.strictEqual(j(unord, '-2，3'), 'correct');
  assert.strictEqual(j(unord, '-2 和 3'), 'correct');
  assert.strictEqual(j(unord, '-2，4'), 'wrong');
  const sh = { type: 'short', answer: 'y=2x+1', accept: ['2x+1', 'f(x)=2x+1'] };
  assert.strictEqual(j(sh, 'y = 2x + 1'), 'correct');
  assert.strictEqual(j(sh, 'Y＝2X+1'), 'correct');
  assert.strictEqual(j(sh, 'f(x)=2x+1'), 'correct');
  assert.strictEqual(j(sh, 'y=1+2x'), 'manual');       // Equivalent forms cannot be evaluated reliably; require self-assessment.
  const quad = { type: 'short', answer: '第三象限' };
  assert.strictEqual(j(quad, '第三象限'), 'correct');
  assert.strictEqual(j(quad, '第二象限'), 'manual');
  assert.strictEqual(j({ type: 'self', answer: '略' }, '略'), 'manual');
  assert.strictEqual(j({ type: 'legacy', answer: '3' }, '3.0'), 'correct');
});

test('PRNG: mulberry32 produces the same sequence for the same seed and values in [0,1)', () => {
  const a = E.mulberry32(123), b = E.mulberry32(123);
  for (let i = 0; i < 100; i++) { const x = a(); assert.strictEqual(x, b()); assert.ok(x >= 0 && x < 1); }
});

/* ------------------------------------------------------------ Answer normalization and evaluation */
console.log('Answer normalization and evaluation');

function verdict(user, ref) { return E.judgeAnswer(user, ref).verdict; }

test('Normalization: full-width to half-width, whitespace, Chinese punctuation, and degrees', () => {
  assert.strictEqual(E.normalizeText('　１／２ '), '1/2');
  assert.strictEqual(E.normalizeText('90 度'), '90°');
  assert.strictEqual(E.normalizeText('－３，（２）'), '-3,(2)');
  assert.strictEqual(E.normalizeText('x²'), 'x^2');
  assert.strictEqual(E.normalizeText('A、B；C'), 'a,b;c');
  assert.strictEqual(E.normalizeText('答：60°。'), '60°');
});

test('Fractions and decimals are equivalent: "１/２" vs "0.5"', () => {
  assert.strictEqual(verdict('１/２', '0.5'), 'correct');
  assert.strictEqual(verdict('0.5', '1/2'), 'correct');
  assert.strictEqual(verdict('2/4', '1/2'), 'correct');
  assert.strictEqual(verdict('-1/2', '-0.5'), 'correct');
  assert.strictEqual(verdict('－１／２', '-(1/2)'), 'correct');
  assert.strictEqual(verdict('1/3', '0.333'), 'wrong');
  assert.strictEqual(verdict('1又1/2', '3/2'), 'correct');
  assert.strictEqual(verdict('1 1/2', '1.5'), 'correct');
  assert.strictEqual(verdict('50%', '1/2'), 'correct');
  assert.strictEqual(verdict('3/5', '3/5'), 'correct');
  assert.strictEqual(verdict('3/5', '5/3'), 'wrong');
});

test('Angles: Chinese degree unit "90 度" is equivalent to "90°"', () => {
  assert.strictEqual(verdict('90 度', '90°'), 'correct');
  assert.strictEqual(verdict('90', '90°'), 'correct');
  assert.strictEqual(verdict('６０°', '60度'), 'correct');
  assert.strictEqual(verdict('50°', '60°'), 'wrong');
});

test('Multiple answers are order-independent, including Chinese separators: "-3 和 -1/2" vs "-1/2，-3"', () => {
  assert.strictEqual(verdict('-3 和 -1/2', '-1/2，-3'), 'correct');
  assert.strictEqual(verdict('-1/2、-3', '-3 和 -1/2'), 'correct');
  assert.strictEqual(verdict('-3', '-3 和 -1/2'), 'wrong');
  assert.strictEqual(verdict('-3，-1/2，0', '-3 和 -1/2'), 'wrong');
  assert.strictEqual(verdict('x=3 或 x=2', 'x=2 或 x=3'), 'correct');
  assert.strictEqual(verdict('2,3', 'x=2 或 x=3'), 'correct');
  assert.strictEqual(verdict('3；3', '3；3'), 'correct');
});

test('Variable names may be omitted, but x and y cannot be swapped', () => {
  assert.strictEqual(verdict('3', 'x=3'), 'correct');
  assert.strictEqual(verdict('x=3', '3'), 'correct');
  assert.strictEqual(verdict('y=2，x=3', 'x=3，y=2'), 'correct');
  assert.strictEqual(verdict('3，2', 'x=3，y=2'), 'correct');
  assert.strictEqual(verdict('x=2，y=3', 'x=3，y=2'), 'wrong');
  assert.strictEqual(verdict('2，3', 'x=3，y=2'), 'wrong');
});

test('Units: aliases are equivalent, omitted units are accepted, and mismatched units are incorrect', () => {
  assert.strictEqual(verdict('12米', '12 m'), 'correct');
  assert.strictEqual(verdict('12', '12 m'), 'correct');
  assert.strictEqual(verdict('12 cm', '12 m'), 'wrong');
  assert.strictEqual(verdict('25 平方米', '25 m²'), 'correct');
  assert.strictEqual(verdict('1,000', '1000'), 'correct');
});

test('Coordinates and other parenthesized multi-value answers', () => {
  assert.strictEqual(verdict('（１，２）', '(1,2)'), 'correct');
  assert.strictEqual(verdict('(1, 2)', '(1,2)'), 'correct');
  assert.strictEqual(verdict('(2,1)', '(1,2)'), 'wrong');
  assert.strictEqual(verdict('(0.5,2)', '(1/2,2)'), 'correct');
});

test('Unreliable text and algebraic answers are correct only when identical; otherwise require self-assessment', () => {
  assert.strictEqual(verdict('相切', '相切'), 'correct');
  assert.strictEqual(verdict('相离', '相切'), 'manual');
  assert.strictEqual(verdict('y=2x+3', 'y=2x+3'), 'correct');
  assert.strictEqual(verdict('2x+3', 'y=2x+3'), 'correct');
  assert.strictEqual(verdict('y=3x+2', 'y=2x+3'), 'manual');
  assert.strictEqual(verdict('(x-2)^2-1', 'y=(x-2)²-1'), 'correct');
  assert.strictEqual(verdict('共 11 种', '共 11 种，每种有 6 个正方形'), 'manual');
  assert.strictEqual(verdict('', '3'), 'manual');
  assert.strictEqual(verdict('不知道', '3'), 'manual');
});

test('Answer evaluation does not throw on unusual input', () => {
  ['', ' ', '(', ')))', '1/0', '/', '--1', '1/2/3', '％', '😀', null, undefined, '１２３４５６７８９０１２３４５６７８９０/３'].forEach((u) => {
    ['3', '1/2', '相切', 'x=2 或 x=3', '', '(1,2)'].forEach((r) => {
      const v = E.judgeAnswer(u, r).verdict;
      assert.ok(['correct', 'wrong', 'manual'].includes(v));
    });
  });
});

/* ------------------------------------------------------------ Real data */
console.log('Real data');

const dataDir = path.join(__dirname, '..', 'data');
const topics = JSON.parse(fs.readFileSync(path.join(dataDir, 'topics.json'), 'utf8'));
const deps = JSON.parse(fs.readFileSync(path.join(dataDir, 'dependencies.json'), 'utf8'));
const stdFile = JSON.parse(fs.readFileSync(path.join(dataDir, 'cn-curriculum-standards.json'), 'utf8'));
const RG = E.buildGraph(topics, deps);
const formal = topics.filter((t) => !t.external);

function bfsAncestors(id) {
  const pre = new Map();
  deps.forEach((d) => { (pre.get(d.topicId) || pre.set(d.topicId, []).get(d.topicId)).push(d.prerequisiteId); });
  const seen = new Set();
  const q = [id];
  while (q.length) { (pre.get(q.shift()) || []).forEach((p) => { if (!seen.has(p)) { seen.add(p); q.push(p); } }); }
  return seen;
}

test('Data loads: 253 elementary + 315 middle-school + 143 required high-school + 128 selective high-school topics; no external nodes; standards include Stage 1', () => {
  const mathTopics = topics.filter((t) => String(t.id).startsWith('cnm_'));
  const mathDeps = deps.filter((d) => String(d.topicId).startsWith('cnm_'));
  assert.strictEqual(mathTopics.length, 839);
  assert.strictEqual(mathDeps.length, 1397);
  assert.strictEqual(topics.filter((t) => t.external).length, 0);
  assert.strictEqual(mathTopics.filter((t) => t.grade <= 6).length, 253);
  assert.strictEqual(mathTopics.filter((t) => t.grade >= 7 && t.grade <= 9).length, 315);
  assert.strictEqual(mathTopics.filter((t) => t.grade === 10 || t.grade === 11).length, 143);
  assert.strictEqual(mathTopics.filter((t) => t.grade >= 12).length, 128);
  assert.strictEqual(mathTopics.filter((t) => t.grade >= 10).length, 271);
  assert.ok(mathTopics.filter((t) => t.grade >= 10).every((t) => /^cnm_h\d{3,}$/.test(t.id)));
  assert.ok(formal.every((t) => E.isTestable(RG, t.id)));
  assert.ok(stdFile.items.length > 200);
  assert.ok(stdFile.items[0].id.indexOf('cms-2022:1.') === 0);
  assert.deepStrictEqual(mathTopics.map((t) => t.id + '\t' + t.name), topics.filter((t) => String(t.id).startsWith('cnm_')).map((t) => t.id + '\t' + t.name));
});

test('English data: 197 elementary, 180–260 middle-school, and 220–320 high-school topics; no math edges; non-starting topics have prerequisites; volumes stay subject-specific', () => {
  const enTopics = topics.filter((t) => String(t.id).startsWith('cne_'));
  const primary = enTopics.filter((t) => String(t.id).startsWith('cne_p'));
  const junior = enTopics.filter((t) => String(t.id).startsWith('cne_j'));
  const seniorEn = enTopics.filter((t) => String(t.id).startsWith('cne_h'));
  assert.strictEqual(primary.length, 208);
  assert.ok(junior.length >= 180 && junior.length <= 260, 'Middle-school English topics: ' + junior.length);
  assert.ok(seniorEn.length >= 220 && seniorEn.length <= 320, 'High-school English topics: ' + seniorEn.length);
  assert.strictEqual(enTopics.length, primary.length + junior.length + seniorEn.length);
  assert.ok(primary.every((t) => t.subject === 'english' && t.grade >= 3 && t.grade <= 6 && !t.external && (t.semester === '上' || t.semester === '下')));
  assert.ok(junior.every((t) => t.subject === 'english' && t.grade >= 7 && t.grade <= 9 && !t.external));
  assert.ok(junior.every((t) => (t.grade === 9 ? t.semester === '上' || t.semester === '全' : t.semester === '上' || t.semester === '下')));
  assert.ok(seniorEn.every((t) => t.subject === 'english' && t.grade >= 10 && t.grade <= 16 && t.semester === '上' && !t.external));
  assert.ok(seniorEn.some((t) => t.name === 'Subjunctive Mood'));
  assert.ok(enTopics.every((t) => ['语音', '词汇', '语法', '日常表达', '读写'].includes(t.domain)));
  const enDeps = deps.filter((d) => String(d.topicId).startsWith('cne_'));
  assert.ok(deps.every((d) => String(d.topicId).startsWith('cne_') === String(d.prerequisiteId).startsWith('cne_')));
  const cross = enDeps.filter((d) => String(d.topicId).startsWith('cne_j') && String(d.prerequisiteId).startsWith('cne_p'));
  assert.ok(cross.length >= 1, 'Middle-school English should link to elementary English');
  assert.ok(!cross.some((d) => String(d.prerequisiteId).startsWith('cnm_')));
  const crossH = enDeps.filter((d) => String(d.topicId).startsWith('cne_h') && String(d.prerequisiteId).startsWith('cne_j'));
  assert.ok(crossH.length >= 8, 'High-school English should link to middle-school English');
  assert.ok(enDeps.filter((d) => String(d.topicId).startsWith('cne_h')).every((d) => String(d.prerequisiteId).startsWith('cne_')));
  const pre = new Map();
  enDeps.forEach((d) => { (pre.get(d.topicId) || pre.set(d.topicId, []).get(d.topicId)).push(d); });
  enTopics.forEach((t) => {
    if (t.id === 'cne_p001') {
      assert.ok(t.root_reason);
      return;
    }
    assert.ok(pre.get(t.id) && pre.get(t.id).length >= 1, t.id + ' has no prerequisite');
    pre.get(t.id).forEach((d) => {
      const src = RG.byId[t.id];
      const dst = RG.byId[d.prerequisiteId];
      const ra = src.grade * 2 + (src.semester === '下' ? 1 : 0);
      const rb = dst.grade * 2 + (dst.semester === '下' ? 1 : 0);
      assert.ok(rb <= ra, t.id + ' has a later prerequisite ' + d.prerequisiteId);
    });
  });
  const math4 = E.gradeTargets(RG, '四上');
  const en4 = E.gradeTargets(RG, '四上', 'english');
  assert.ok(math4.ids.length > 0 && math4.ids.every((id) => id.startsWith('cnm_') && RG.byId[id].grade === 4 && RG.byId[id].semester === '上'));
  assert.ok(en4.ids.length > 0 && en4.ids.every((id) => id.startsWith('cne_p') && RG.byId[id].grade === 4 && RG.byId[id].semester === '上'));
  assert.deepStrictEqual(E.gradeTargets(RG, '四上').ids, E.gradeTargets(RG, '四上', 'math').ids);
  const en8 = E.gradeTargets(RG, '八上', 'english');
  assert.strictEqual(en8.label, '八年级上册');
  assert.ok(en8.ids.length > 0 && en8.ids.every((id) => id.startsWith('cne_j') && RG.byId[id].grade === 8 && RG.byId[id].semester === '上'));
  assert.ok(E.gradeTargets(RG, '八上').ids.every((id) => id.startsWith('cnm_')));
  const en9 = E.gradeTargets(RG, '九全', 'english');
  assert.strictEqual(en9.label, '九年级全一册');
  assert.ok(en9.ids.length > 0 && en9.ids.every((id) => id.startsWith('cne_j') && RG.byId[id].grade === 9 && RG.byId[id].semester === '全'));
  const enGrade9 = E.gradeTargets(RG, '九年级', 'english');
  assert.ok(enGrade9.volumes.indexOf('九全') >= 0 && enGrade9.ids.every((id) => id.startsWith('cne_')));
  const mathGrade9 = E.gradeTargets(RG, '九年级');
  assert.ok(mathGrade9.ids.length > 0 && mathGrade9.ids.every((id) => id.startsWith('cnm_') && RG.byId[id].semester !== '全'));
  assert.deepStrictEqual(
    E.parseChapter('Grade 8, Semester 2, Unit 8: Have you read Treasure Island yet', { id: 'cne_j001', grade: 8, semester: '下' }),
    { volume: '八下', chapterNo: 'Unit 8', chapterName: 'Have you read Treasure Island yet', section: '' }
  );
  assert.deepStrictEqual(
    E.parseChapter('Compulsory Volume 1 Welcome Unit Welcome Unit', { id: 'cne_h001', grade: 10, semester: '上' }),
    { volume: '必修一', chapterNo: 'Welcome Unit', chapterName: 'Welcome Unit', section: '' }
  );
  assert.deepStrictEqual(
    E.parseChapter('Compulsory Volume 1 Unit 1 Teenage Life', { id: 'cne_h001', grade: 10, semester: '上' }),
    { volume: '必修一', chapterNo: 'Unit 1', chapterName: 'Teenage Life', section: '' }
  );
  assert.deepStrictEqual(
    E.parseChapter('Selective Compulsory Volume 1 Unit 1 People of Achievement', { id: 'cne_h201', grade: 13, semester: '上' }),
    { volume: '选必一', chapterNo: 'Unit 1', chapterName: 'People of Achievement', section: '' }
  );
  assert.strictEqual(E.gradeTargets(RG, '必修一'), null);
  assert.strictEqual(E.gradeTargets(RG, '选择性必修第四册'), null);
  const enB1 = E.gradeTargets(RG, '必修一', 'english');
  assert.strictEqual(enB1.label, '必修一（必修第一册）');
  assert.ok(enB1.ids.length > 0 && enB1.ids.every((id) => id.startsWith('cne_h') && RG.byId[id].grade === 10));
  const enS1 = E.gradeTargets(RG, '选必一', 'english');
  assert.strictEqual(enS1.label, '选必一（选择性必修第一册）');
  assert.ok(enS1.ids.length > 0 && enS1.ids.every((id) => id.startsWith('cne_h') && RG.byId[id].grade === 13));
  assert.ok(E.gradeTargets(RG, '选必一').ids.every((id) => id.startsWith('cnm_')));
  assert.ok(E.gradeTargets(RG, '选择性必修第一册').ids.every((id) => id.startsWith('cnm_')));
  const enS4 = E.gradeTargets(RG, '选必四', 'english');
  assert.strictEqual(enS4.label, '选必四（选择性必修第四册）');
  assert.ok(enS4.ids.every((id) => id.startsWith('cne_h') && RG.byId[id].grade === 16));
  assert.strictEqual(E.subjectOf(enTopics[0]), 'english');
  assert.strictEqual(E.subjectOf(topics.find((t) => t.id === 'cnm_p001')), 'math');
  const ces = stdFile.items.filter((it) => String(it.id).startsWith('ces-2022:'));
  const ces3 = ces.filter((it) => String(it.id).indexOf('ces-2022:3.') === 0);
  assert.ok(ces.length >= 20 && ces3.length >= 20, 'English Level 3 standards: ' + ces3.length);
  assert.ok(ces.every((it) => it.verbatim === false && it.page_or_ref === 'To be verified'));
  const cesH = stdFile.items.filter((it) => String(it.id).startsWith('ces-2017:H.'));
  assert.ok(cesH.length >= 20, 'High-school English standards: ' + cesH.length);
  assert.ok(cesH.every((it) => it.verbatim === false && it.page_or_ref === 'To be verified'));
  assert.ok(cesH.some((it) => String(it.id).indexOf('ces-2017:H.B.') === 0));
  assert.ok(cesH.some((it) => String(it.id).indexOf('ces-2017:H.S.') === 0));
  assert.strictEqual(stdFile.english.senior.year, 2025);
});

test('Real data: ancestor sets match an independent breadth-first search for every topic', () => {
  topics.forEach((t) => {
    assert.deepStrictEqual(sorted(E.ancestors(RG, t.id)), sorted(bfsAncestors(t.id)), t.id);
  });
});

test('Real data: prerequisite subgraphs exclude external nodes, middle-school targets trace to elementary topics, and topological order is valid', () => {
  let sawPrimary = false;
  formal.forEach((t) => {
    const sub = E.subgraph(RG, [t.id]);
    assert.strictEqual(sub.nodes[sub.nodes.length - 1], t.id);
    assertTopological(sub.nodes, RG);
    assert.ok(sub.nodes.every((id) => !RG.byId[id].external));
    if (t.grade >= 7 && sub.nodes.some((id) => RG.byId[id].grade <= 6)) sawPrimary = true;
  });
  assert.ok(sawPrimary, 'At least one middle- or high-school topic should have an elementary ancestor');
  const senior = formal.filter((t) => t.grade >= 10 && String(t.id).startsWith('cnm_'));
  assert.ok(senior.length === 271);
  assert.ok(senior.every((t) => E.subgraph(RG, [t.id]).nodes.length > 1), 'Every high-school topic should have a prerequisite');
  assert.ok(senior.some((t) => E.subgraph(RG, [t.id]).nodes.some((id) => RG.byId[id].grade >= 7 && RG.byId[id].grade <= 9)),
    'At least one high-school topic should have a middle-school ancestor');
});

test('Legacy ID aliases: cnm_ext_* IDs are absent from the graph; resolveTargets maps them to official elementary topics', () => {
  const aliases = JSON.parse(fs.readFileSync(path.join(dataDir, 'id-aliases.json'), 'utf8')).aliases;
  assert.strictEqual(Object.keys(aliases).length, 18);
  for (let i = 1; i <= 18; i++) {
    const key = 'cnm_ext_' + String(i).padStart(3, '0');
    assert.ok(!RG.byId[key], key + ' should no longer be a topic');
    assert.ok(aliases[key] && aliases[key].name && aliases[key].targets.length);
    const ids = E.resolveTargets([key], aliases);
    assert.ok(ids.length >= 1 && ids.length === new Set(ids).size, key);
    ids.forEach((id) => {
      const t = RG.byId[id];
      assert.ok(t && t.grade <= 6 && !t.external, key + ' -> ' + id);
    });
    const s = E.createSession(RG, ids, { limit: 2 });
    assert.ok(ids.indexOf(E.nextQuestion(RG, s)) >= 0, key);
  }
  const mixed = E.resolveTargets(['cnm_ext_002', 'cnm_001'], aliases);
  assert.ok(mixed.indexOf('cnm_001') >= 0);
  assert.ok(mixed.some((id) => RG.byId[id].grade <= 6));
  assert.deepStrictEqual(E.resolveTargets(['nope'], aliases), ['nope']);
  assert.deepStrictEqual(E.resolveTargets(['cnm_221'], null), ['cnm_221']);
});

test('Real data: cnm_221 (Completing the Square) is asked first; after a miss, hard prerequisites come first', () => {
  let s = E.createSession(RG, ['cnm_221']);
  assert.strictEqual(E.nextQuestion(RG, s), 'cnm_221');
  s = E.applyAnswer(RG, s, 'cnm_221', 'wrong');
  const prereqs = RG.prereqs.cnm_221;
  const firstHard = prereqs.find((p) => p.strength === 'hard').id;
  assert.strictEqual(E.nextQuestion(RG, s), firstHard);
});

test('Real data: a correct target answer skips all ancestors', () => {
  const s = E.applyAnswer(RG, E.createSession(RG, ['cnm_221']), 'cnm_221', 'correct');
  assert.strictEqual(E.nextQuestion(RG, s), null);
  const anc = bfsAncestors('cnm_221');
  assert.ok(anc.size > 30);
  anc.forEach((id) => assert.strictEqual(E.statusOf(s, id), 'mastered', id));
});

// Simple reproducible pseudo-random number generator.
function rng(seed) { let x = seed >>> 0; return () => { x = (Math.imul(x, 1664525) + 1013904223) >>> 0; return x / 4294967296; }; }

/** A consistent simulated student: the mastered set is closed over ancestors. */
function makeStudent(rand, p) {
  const known = new Set();
  topics.forEach((t) => {
    if (rand() < p) { known.add(t.id); bfsAncestorsCached(t.id).forEach((a) => known.add(a)); }
  });
  return known;
}
const ancCache = new Map();
function bfsAncestorsCached(id) { if (!ancCache.has(id)) ancCache.set(id, bfsAncestors(id)); return ancCache.get(id); }

function simulate(targets, known, limit) {
  let s = E.createSession(RG, targets, { limit: limit });
  const asked = [];
  for (let guard = 0; guard < 500; guard++) {
    const q = E.nextQuestion(RG, s);
    if (!q) break;
    asked.push(q);
    s = E.applyAnswer(RG, s, q, known.has(q) ? 'correct' : 'wrong');
  }
  return { s: s, asked: asked };
}

test('Real data: with a consistent student and no question limit, weak topics and root causes are reconstructed exactly', () => {
  const rand = rng(20261017);
  let cases = 0;
  for (let round = 0; round < 3; round++) {
    const known = makeStudent(rand, [0.04, 0.12, 0.3][round]);
    formal.forEach((t) => {
      const { s, asked } = simulate([t.id], known, 9999);
      cases++;
      assert.strictEqual(new Set(asked).size, asked.length, 'Questions should not repeat for ' + t.id);
      assert.ok(asked.every((id) => !RG.byId[id].external));
      const sum = E.summarize(RG, s);
      const sub = E.subgraph(RG, [t.id]);
      const unknown = sub.nodes.filter((id) => E.isTestable(RG, id) && !known.has(id));
      assert.deepStrictEqual(sorted(sum.weak), sorted(unknown), 'Weak-topic set for ' + t.id);
      sum.mastered.forEach((id) => assert.ok(known.has(id), id + ' was marked mastered although the student does not know it'));
      const expectRoots = unknown.filter((id) => RG.prereqs[id].every((p) => !unknown.includes(p.id)));
      assert.deepStrictEqual(sorted(sum.roots.map((r) => r.id)), sorted(expectRoots), 'Root causes for ' + t.id);
      // Path is topological, excludes mastered topics, covers every weak topic, and includes every root cause.
      const pathIds = sum.path.map((p) => p.id);
      assertTopological(pathIds, RG);
      sum.path.forEach((p) => assert.notStrictEqual(p.status, 'mastered'));
      sum.weak.forEach((id) => assert.ok(pathIds.includes(id), 'Weak topic should be in the path: ' + id));
      sum.roots.forEach((r) => assert.ok(pathIds.includes(r.id)));
      if (unknown.length) assert.strictEqual(pathIds[pathIds.length - 1], t.id);
      // Either all answers are correct (one question) or hard/soft prerequisites are traced.
      if (known.has(t.id)) assert.strictEqual(asked.length, 1);
      assert.strictEqual(sum.finished, true);
      assert.strictEqual(sum.limitReached, false);
    });
  }
  assert.ok(cases >= 900);
});

test('Real data: question limits (8/12/20) are never exceeded and root/path definitions still hold', () => {
  const rand = rng(7);
  [8, 12, 20].forEach((limit) => {
    const known = makeStudent(rand, 0.02);
    let capped = 0;
    formal.forEach((t) => {
      const { s, asked } = simulate([t.id], known, limit);
      assert.ok(asked.length <= limit);
      if (asked.length === limit) capped++;
      const sum = E.summarize(RG, s);
      assert.strictEqual(sum.asked, asked.length);
      sum.roots.forEach((r) => {
        assert.strictEqual(E.statusOf(s, r.id), 'weak');
        RG.prereqs[r.id].forEach((p) => assert.notStrictEqual(E.statusOf(s, p.id), 'weak'));
      });
      const pathIds = sum.path.map((p) => p.id);
      assertTopological(pathIds, RG);
      sum.path.forEach((p) => assert.notStrictEqual(p.status, 'mastered'));
      if (sum.limitReached) assert.ok(sum.untested.length > 0);
      const all = new Set(sum.mastered.concat(sum.weak, sum.untested));
      assert.strictEqual(all.size, s.order.length);
    });
    if (limit === 8) assert.ok(capped > 0, 'At least one target should reach the limit');
  });
});

test('Real data: a student who knows nothing stops at the limit and remaining topics are marked untested', () => {
  const none = new Set();
  const { s, asked } = simulate(['cnm_221'], none, 12);
  assert.strictEqual(asked.length, 12);
  const sum = E.summarize(RG, s);
  assert.strictEqual(sum.limitReached, true);
  assert.ok(sum.untested.length > 0);
  assert.ok(sum.roots.length >= 1);
});

test('Real data: when a full chapter is the target, a knowledgeable student is asked only about maximal topics', () => {
  const chapter = formal.filter((t) => t.grade === 7 && t.semester === '上' && E.parseChapter(t.chapter, t).chapterNo === 'Chapter 1');
  const ids = chapter.map((t) => t.id);
  assert.ok(ids.length >= 5);
  const known = new Set(topics.map((t) => t.id));
  const { s, asked } = simulate(ids, known, 12);
  const idSet = new Set(ids);
  const maximal = ids.filter((id) => !ids.some((o) => o !== id && bfsAncestorsCached(o).has(id) && idSet.has(o)));
  assert.strictEqual(asked.length, maximal.length);
  ids.forEach((id) => assert.strictEqual(E.statusOf(s, id), 'mastered'));
  // A student who knows nothing: every target is either assessed or marked untested.
  const r = simulate(ids, new Set(), 20);
  const sum = E.summarize(RG, r.s);
  ids.forEach((id) => assert.ok(sum.weak.includes(id) || sum.untested.includes(id), id));
});

test('Real data: replay and JSON round-trip reproduce the same session', () => {
  const known = makeStudent(rng(3), 0.1);
  const { s } = simulate(['cnm_232'], known, 12);
  const r = E.replay(RG, ['cnm_232'], s.answers, { limit: 12 });
  assert.deepStrictEqual(r, s);
  assert.deepStrictEqual(E.replay(RG, JSON.parse(JSON.stringify(s.targets)), JSON.parse(JSON.stringify(s.answers)), { limit: 12 }), s);
});

test('Real data: path graph layout keeps edge directions consistent and all nodes', () => {
  const { s } = simulate(['cnm_232'], new Set(), 12);
  const sum = E.summarize(RG, s);
  const lay = E.layout(RG, s, sum);
  const layer = Object.fromEntries(lay.nodes.map((n) => [n.id, n.layer]));
  lay.edges.forEach((e) => assert.ok(layer[e.from] < layer[e.to]));
  sum.path.forEach((p) => assert.ok(layer[p.id] !== undefined));
  assert.ok(layer.cnm_232 === lay.layers - 1);
});

test('Real data: each diagnostic answer is accepted by the answer evaluator', () => {
  let bad = [];
  formal.forEach((t) => {
    const a = t.diagnostic_question.answer;
    if (E.judgeAnswer(a, a).verdict !== 'correct') bad.push(t.id);
  });
  assert.deepStrictEqual(bad, []);
});

test('Real data: chapter names can be parsed', () => {
  formal.forEach((t) => {
    const c = E.parseChapter(t.chapter, t);
    assert.ok(c.volume && (c.chapterNo || c.chapterName), t.chapter);
  });
});

/* ------------------------------------------------------------ Question bank data (data/questions.json) */
console.log('Question bank data');

const questions = JSON.parse(fs.readFileSync(path.join(dataDir, 'questions.json'), 'utf8'));
const RGQ = E.buildGraph(topics, deps, questions);
const qByTopic = {};
questions.forEach((q) => { (qByTopic[q.topicId] = qByTopic[q.topicId] || []).push(q); });
const NUM_RE = /^-?\d+(\.\d+)?(\/\d+(\.\d+)?)?$/;

test('Question bank: each official topic has at least three questions; IDs are unique and valid; external topics have none; basic and standard tiers are present', () => {
  const ids = new Set();
  questions.forEach((q) => {
    assert.ok(!ids.has(q.id), 'Duplicate ID: ' + q.id);
    ids.add(q.id);
    assert.ok(new RegExp('^' + q.topicId + '_q[1-9]\\d*$').test(q.id), q.id);
    assert.ok(RG.byId[q.topicId] && !RG.byId[q.topicId].external, q.id + ' has an invalid topicId');
  });
  formal.forEach((t) => {
    const qs = qByTopic[t.id] || [];
    assert.ok(qs.length >= 3, t.id + ' has only ' + qs.length + ' questions');
    const ds = new Set(qs.map((q) => q.difficulty));
    assert.ok(ds.has('basic') && ds.has('standard'), t.id + ' is missing basic or standard');
    if (t.grade >= 1 && t.grade <= 6 && String(t.id).startsWith('cnm_p')) {
      assert.ok(ds.has('challenge'), t.id + ' is missing challenge');
    }
    assert.ok(qs.some((q) => q.id === t.id + '_q1'), t.id + ' has no q1');
    assert.ok(qs.filter((q) => q.id !== t.id + '_q1').some((q) => q.difficulty === 'basic'), t.id + ' has no basic question other than q1');
  });
});

test('Question bank: valid types and difficulty levels, nonempty required fields, and at least 60% numeric or choice questions', () => {
  let auto = 0;
  questions.forEach((q) => {
    assert.ok(['numeric', 'choice', 'short', 'self'].includes(q.type), q.id);
    assert.ok(['basic', 'standard', 'challenge', 'advanced'].includes(q.difficulty), q.id);
    ['prompt', 'answer', 'explanation'].forEach((f) => assert.ok(typeof q[f] === 'string' && q[f].trim(), q.id + ' ' + f));
    if (q.type === 'numeric' || q.type === 'choice') auto++;
  });
  assert.ok(auto / questions.length >= 0.6, 'Numeric + choice share: ' + (auto / questions.length));
});

test('Question bank: figure questions use parseable inline SVG without external references; diagram choices omit option names from the image', () => {
  let n = 0;
  questions.forEach((q) => {
    const blobs = [];
    if (q.figure != null) blobs.push(['prompt', q.figure]);
    (q.choices || []).forEach((c) => { if (c.figure != null) blobs.push(['option ' + c.key, c.figure]); });
    if (!blobs.length && q.hideChoiceText == null) return;
    n++;
    if (q.hideChoiceText != null) {
      assert.strictEqual(q.hideChoiceText, true, q.id);
      assert.strictEqual(q.type, 'choice', q.id);
      q.choices.forEach((c) => {
        assert.ok(c.figure, q.id + ' option ' + c.key + ' is missing a figure');
        assert.ok(!c.text || c.figure.indexOf(c.text) < 0, q.id + ' includes an option name in its figure: ' + c.text);
      });
    }
    blobs.forEach((pair) => {
      const svg = pair[1];
      assert.strictEqual(typeof svg, 'string', q.id + pair[0]);
      assert.ok(svg.indexOf('<svg') === 0 && svg.indexOf('viewBox=') > 0, q.id + ' ' + pair[0] + ' is not an SVG with viewBox');
      assert.ok(!/<\s*script|foreignObject|<\s*image\b/i.test(svg), q.id + ' figure contains a disallowed element');
      const probe = svg.replace('xmlns="http://www.w3.org/2000/svg"', '');
      assert.ok(!/https?:\/\//i.test(probe), q.id + ' figure references an external URL');
      assert.ok(!/url\(\s*(?!#)/i.test(svg), q.id + ' figure contains an external url()');
    });
  });
  assert.ok(n >= 80, 'Too few questions with figures: ' + n);
});

test('Question bank: choice questions have 3–4 unique option keys and answer matches an option key', () => {
  let n = 0;
  questions.filter((q) => q.type === 'choice').forEach((q) => {
    n++;
    assert.ok(Array.isArray(q.choices) && q.choices.length >= 3 && q.choices.length <= 4, q.id);
    const keys = q.choices.map((c) => c.key);
    assert.strictEqual(new Set(keys).size, keys.length, q.id + ' has duplicate option keys');
    assert.ok(keys.includes(q.answer), q.id + ' answer is not an option key');
    assert.strictEqual(new Set(q.choices.map((c) => c.text.trim())).size, keys.length, q.id + ' has duplicate option text');
  });
  assert.ok(n > 100);
});

test('Question bank: numeric answers parse as integers, decimals, fractions, negatives, or comma-separated values', () => {
  let n = 0;
  questions.filter((q) => q.type === 'numeric').forEach((q) => {
    n++;
    const parts = q.answer.split(/[，,]/).map((x) => x.replace(/\s/g, ''));
    parts.forEach((x) => assert.ok(NUM_RE.test(x), q.id + ' answer=' + q.answer));
    if (q.unordered) assert.ok(parts.length > 1, q.id + ' is unordered but has only one answer');
  });
  assert.ok(n > 500);
});

test('English questions are self-contained, do not refer to standards or prior questions, and accept their reference answers', () => {
  const enQs = questions.filter((q) => String(q.topicId).startsWith('cne_'));
  const juniorTopics = topics.filter((t) => String(t.id).startsWith('cne_j')).length;
  assert.ok(enQs.length >= 197 * 4 + juniorTopics * 3, 'English questions: ' + enQs.length);
  enQs.forEach((q) => {
    assert.ok(!/^(同一|上题|该题|同上)/.test(String(q.prompt).trim()), q.id);
    assert.ok(!/本知识点|课标|是否要求/.test(q.prompt), q.id);
    assert.ok(q.type === 'numeric' || q.type === 'choice', q.id);
    const verdict = E.judgeQuestion(q, q.type === 'choice' ? q.answer : q.answer).verdict;
    assert.strictEqual(verdict, 'correct', q.id);
  });
});

test('Physics data: 28 topics in 八上, 24 in 八下, and 40 in 九全; physics-only edges; mathLinks point to math; volumes stay subject-specific', () => {
  const phy = topics.filter((t) => /^cnp_\d/.test(String(t.id)));
  const count = (g, s) => phy.filter((t) => t.grade === g && t.semester === s).length;
  assert.strictEqual(phy.length, 92);
  assert.strictEqual(count(8, '上'), 28);
  assert.strictEqual(count(8, '下'), 24);
  assert.strictEqual(count(9, '全'), 40);
  assert.ok(phy.every((t) => t.subject === 'physics' && E.subjectOf(t) === 'physics' && !t.external));
  assert.ok(phy.every((t) => ['物质', '运动和相互作用', '能量', '跨学科实践'].includes(t.domain)));
  assert.ok(phy.every((t) => E.parseChapter(t.chapter, t).section && /^(八上|八下|九全)$/.test(E.parseChapter(t.chapter, t).volume)));
  assert.ok(phy.every((t) => (t.standards || []).length >= 1 && t.standards.every((s) => s.id.startsWith('cps-2022:'))));
  const order = new Map(phy.map((t, i) => [t.id, i]));
  const phyDeps = deps.filter((d) => /^cnp_\d/.test(String(d.topicId)));
  assert.ok(phyDeps.length >= 92);
  phyDeps.forEach((d) => {
    assert.ok(/^cnp_\d/.test(String(d.prerequisiteId)), 'Middle-school physics prerequisites must also be middle-school physics: ' + d.topicId);
    assert.ok(order.get(d.prerequisiteId) < order.get(d.topicId), d.topicId + ' prerequisite is later in the textbook');
  });
  const links = phy.flatMap((t) => t.mathLinks || []);
  assert.ok(links.length >= 20);
  assert.ok(links.every((l) => String(l.id).startsWith('cnm_') && RG.byId[l.id] && l.reason));
  const p8 = E.gradeTargets(RG, '八上', 'physics');
  assert.strictEqual(p8.ids.length, 28);
  assert.ok(E.gradeTargets(RG, '八上').ids.every((id) => id.startsWith('cnm_')));
  assert.strictEqual(E.gradeTargets(RG, '九年级', 'physics').ids.length, 40);
  assert.strictEqual(E.gradeTargets(RG, '九全', 'physics').label, '九年级全一册');
  assert.strictEqual(stdFile.items.filter((it) => String(it.id).startsWith('cps-2022:')).length, 89);
  assert.ok(stdFile.physics && /2025/.test(stdFile.physics.title));
});

test('High-school physics data: expected counts per required/selective volume; prerequisites stay within physics and do not point to later volumes', () => {
  const sen = topics.filter((t) => /^cnp_h\d/.test(String(t.id)));
  const vols = ['必修一', '必修二', '必修三', '选必一', '选必二', '选必三'];
  const want = [27, 25, 37, 28, 26, 34];
  assert.strictEqual(sen.length, 177);
  sen.forEach((t) => {
    assert.ok(t.subject === 'physics' && E.subjectOf(t) === 'physics' && !t.external && t.semester === '上', t.id);
    assert.ok(t.grade >= 10 && t.grade <= 15, t.id);
    assert.ok(vols[t.grade - 10] === E.parseChapter(t.chapter, t).volume && E.parseChapter(t.chapter, t).section, t.id + ' chapter');
    assert.ok(['物质', '运动和相互作用', '能量', '跨学科实践'].includes(t.domain), t.id);
    assert.ok((t.standards || []).length >= 1 && t.standards.every((x) => x.id.startsWith('cps-hs-2017:')), t.id + ' standards');
  });
  vols.forEach((v, i) => {
    assert.strictEqual(sen.filter((t) => t.grade === 10 + i).length, want[i], v);
    const g = E.gradeTargets(RG, v, 'physics');
    assert.strictEqual(g.ids.length, want[i], v + ' full volume');
    assert.ok(E.gradeTargets(RG, v, 'english') === null || E.gradeTargets(RG, v, 'english').ids.every((id) => id.startsWith('cne_')));
  });
  assert.strictEqual(E.gradeTargets(RG, '必修一', 'physics').label, '必修一（必修第一册）');
  assert.strictEqual(E.gradeTargets(RG, '选必三', 'physics').ids.length, 34);
  assert.ok(E.gradeTargets(RG, '八上', 'physics').ids.every((id) => /^cnp_\d/.test(id)));
  const rank = new Map(topics.filter((t) => String(t.id).startsWith('cnp_')).map((t) => [t.id, /^cnp_h/.test(t.id) ? 100 + t.grade : t.grade]));
  const order = new Map(sen.map((t, i) => [t.id, i]));
  const senDeps = deps.filter((d) => /^cnp_h\d/.test(String(d.topicId)));
  assert.ok(senDeps.length >= 400);
  senDeps.forEach((d) => {
    assert.ok(String(d.prerequisiteId).startsWith('cnp_'), 'Cross-subject edge: ' + d.topicId);
    assert.ok(rank.get(d.prerequisiteId) <= rank.get(d.topicId), d.topicId + ' has a prerequisite in a later volume');
    if (/^cnp_h/.test(d.prerequisiteId)) assert.ok(order.get(d.prerequisiteId) < order.get(d.topicId), d.topicId + ' prerequisite is later in the textbook');
  });
  assert.ok(deps.filter((d) => /^cnp_\d/.test(String(d.topicId))).every((d) => /^cnp_\d/.test(String(d.prerequisiteId))), 'Middle-school physics cannot depend on high school');
  assert.ok(senDeps.some((d) => /^cnp_\d/.test(String(d.prerequisiteId))), 'High-school physics should link back to middle-school physics');
  const links = sen.flatMap((t) => t.mathLinks || []);
  assert.ok(links.length >= 40 && links.every((l) => String(l.id).startsWith('cnm_') && RG.byId[l.id] && l.reason));
  const hs = stdFile.items.filter((it) => String(it.id).startsWith('cps-hs-2017:'));
  assert.strictEqual(hs.length, 108);
  assert.ok(hs.every((it) => it.verbatim === false && it.page_or_ref === 'To be verified'));
  assert.ok(stdFile.physics_senior && /2020/.test(stdFile.physics_senior.title) && /2019/.test(stdFile.physics_senior.textbook));
  const sq = questions.filter((q) => /^cnp_h\d/.test(String(q.topicId)));
  assert.strictEqual(sq.length, 177 * 4);
  sq.forEach((q) => assert.ok(q.verify && !/免费|AI ?初稿/.test(q.prompt + q.explanation), q.id));
});

test('Physics questions: four per topic; numeric answers with units accept numbers only; reference answers are accepted', () => {
  const phyAll = topics.filter((t) => String(t.id).startsWith('cnp_'));
  const pq = questions.filter((q) => String(q.topicId).startsWith('cnp_'));
  assert.strictEqual(pq.length, phyAll.length * 4);
  pq.forEach((q) => {
    assert.ok(q.type === 'numeric' || q.type === 'choice', q.id);
    assert.ok(q.verify, q.id + ' has no verify flag');
    if (q.type === 'numeric') assert.ok(/enter (?:(?:a |the )?number (?:only|without the percent sign)|only the number)/i.test(q.prompt), q.id + ' prompt should request a numeric value only');
    assert.strictEqual(E.judgeQuestion(q, q.answer).verdict, 'correct', q.id);
  });
  const speedQ = { id: 'x', type: 'numeric', answer: '20', prompt: '' };
  assert.strictEqual(E.judgeQuestion(speedQ, '20 m/s').verdict, 'correct');
  assert.strictEqual(E.judgeQuestion(speedQ, '20m/s').verdict, 'correct');
  assert.strictEqual(E.judgeQuestion({ id: 'y', type: 'numeric', answer: '15000', prompt: '' }, '15000Pa').verdict, 'correct');
});

test('Percentage questions accept 50 and 50%, reject 0.5, and leave non-percent questions unchanged', () => {
  const pq = questions.filter((q) => q.percent === true);
  assert.ok(pq.length >= 2, 'Percentage questions: ' + pq.length);
  pq.forEach((q) => {
    assert.ok(String(q.topicId).startsWith('cnp_') && q.type === 'numeric' && /percent|percentage|%/i.test(q.prompt), q.id);
    const a = q.answer;
    assert.strictEqual(E.judgeQuestion(q, a).verdict, 'correct', q.id + ' ' + a);
    assert.strictEqual(E.judgeQuestion(q, a + '%').verdict, 'correct', q.id + ' ' + a + '%');
    assert.strictEqual(E.judgeQuestion(q, a + ' %').verdict, 'correct', q.id + ' ' + a + ' %');
    assert.strictEqual(E.judgeQuestion(q, a + '％').verdict, 'correct', q.id + ' full-width percent');
    assert.strictEqual(E.judgeQuestion(q, String(Number(a) / 100)).verdict, 'wrong', q.id + ' decimal');
    assert.strictEqual(E.judgeQuestion(q, String(Number(a) + 1) + '%').verdict, 'wrong', q.id + ' incorrect value');
  });
  assert.ok(questions.every((q) => q.percent !== true || String(q.topicId).startsWith('cnp_')));
  const plain = { id: 'm', type: 'numeric', answer: '0.5', prompt: '' };
  assert.strictEqual(E.judgeQuestion(plain, '50%').verdict, 'correct');
  assert.strictEqual(E.judgeQuestion({ id: 'n', type: 'numeric', answer: '50', prompt: '' }, '50%').verdict, 'wrong');
});

test('Question bank: q1 is migrated from diagnostic_question (prompt starts with the original or is marked fixed_from_source)', () => {
  formal.forEach((t) => {
    const q1 = qByTopic[t.id].find((q) => q.id === t.id + '_q1');
    assert.ok(q1.prompt.startsWith(t.diagnostic_question.question) || q1.fixed_from_source, t.id);
  });
});

test('Question bank: evaluator accepts each reference answer; self questions always require manual assessment', () => {
  const bad = [];
  questions.forEach((q) => {
    const v = E.judgeQuestion(q, q.type === 'choice' ? q.answer : q.answer).verdict;
    const want = q.type === 'self' ? 'manual' : 'correct';
    if (v !== want) bad.push(q.id + ':' + v);
    if (q.type === 'choice') {
      const text = q.choices.find((c) => c.key === q.answer).text;
      // If option text is a single letter (such as x or D), it is indistinguishable from the option key; treat it as the key. The UI uses clickable options.
      if (!/^[A-Za-z]$/.test(text.trim()) && E.judgeQuestion(q, text).verdict !== 'correct') bad.push(q.id + ':text');
      q.choices.filter((c) => c.key !== q.answer).forEach((c) => {
        if (E.judgeQuestion(q, c.key).verdict !== 'wrong') bad.push(q.id + ':wrong-' + c.key);
      });
    }
    if (q.type === 'numeric' && !q.unordered && E.judgeQuestion(q, '999999').verdict === 'correct') bad.push(q.id + ':999999');
  });
  assert.deepStrictEqual(bad.slice(0, 20), []);
});

test('Graph with a question bank: every official topic is testable, external topics are not, and hasBank is true', () => {
  assert.strictEqual(RGQ.hasBank, true);
  assert.ok(formal.every((t) => E.isTestable(RGQ, t.id)));
  assert.ok(topics.filter((t) => t.external).every((t) => !E.isTestable(RGQ, t.id)));
});

console.log('Real diagnostics with a question bank');

/** Student simulation: known answers are correct; flaky answers miss once then pass; all other answers are incorrect. */
function simulateBank(targets, known, flaky, limit, seed, confirm) {
  let s = E.createSession(RGQ, targets, {
    limit: limit, seed: seed == null ? 'sim' : seed,
    confirm: confirm == null ? E.DEFAULT_CONFIRM : confirm
  });
  const asked = [];
  for (let guard = 0; guard < 2000; guard++) {
    const it = E.nextItem(RGQ, s);
    if (!it) break;
    asked.push(it.topicId + '#' + it.attempt);
    let r = 'wrong';
    if (known.has(it.topicId)) r = 'correct';
    else if (flaky.has(it.topicId)) r = it.attempt === 1 ? 'wrong' : 'correct';
    s = E.applyAnswer(RGQ, s, it.topicId, r);
  }
  return { s: s, asked: asked };
}

test('Elementary backtracking: a miss on middle-school "Positive and Negative Numbers" reaches elementary topics, with the path ordered by grade', () => {
  const { s, asked } = simulateBank(['cnm_001'], new Set(), new Set(), 80, 'primary');
  const ids = asked.map((x) => x.split('#')[0]);
  assert.ok(ids.indexOf('cnm_001') >= 0);
  assert.ok(ids.filter((id) => id === 'cnm_001').length <= 2);
  assert.ok(ids.some((id) => RGQ.byId[id].grade === 6), 'Should assess Grade 6');
  assert.ok(ids.some((id) => RGQ.byId[id].grade === 1), 'Should continue to Grade 1');
  const per = {};
  ids.forEach((id) => { per[id] = (per[id] || 0) + 1; });
  Object.keys(per).forEach((id) => assert.ok(per[id] <= 2, id + ' exceeds two questions'));
  const sum = E.summarize(RGQ, s);
  const ranks = sum.path.map((p) => E.gradeRank(RGQ, p.id));
  for (let i = 1; i < ranks.length; i++) {
    assert.ok(ranks[i] >= ranks[i - 1], 'Path should be ordered by grade: ' + sum.path[i - 1].id + ' -> ' + sum.path[i].id);
  }
  assert.ok(sum.path.some((p) => RGQ.byId[p.id].grade <= 6));
  assert.strictEqual(sum.path[sum.path.length - 1].id, 'cnm_001');
  assertTopological(sum.path.map((p) => p.id), RGQ);
});

test('With a question bank: unlimited questions reconstruct weak topics and root causes; mastered topics use confirm questions and others use two', () => {
  const rand = rng(20261018);
  let cases = 0;
  const conf = E.DEFAULT_CONFIRM;
  for (let round = 0; round < 3; round++) {
    const known = makeStudent(rand, [0.04, 0.12, 0.3][round]);
    formal.forEach((t) => {
      const { s, asked } = simulateBank([t.id], known, new Set(), 9999);
      cases++;
      const sum = E.summarize(RGQ, s);
      const sub = E.subgraph(RGQ, [t.id]);
      const unknown = sub.nodes.filter((id) => E.isTestable(RGQ, id) && !known.has(id));
      assert.deepStrictEqual(sorted(sum.weak), sorted(unknown), 'Weak-topic set for ' + t.id);
      assert.deepStrictEqual(sum.shaky, []);
      assert.deepStrictEqual(sum.unconfirmed, []);
      sum.mastered.forEach((id) => assert.ok(known.has(id), id + ' was marked mastered although the student does not know it'));
      const expectRoots = unknown.filter((id) => RGQ.prereqs[id].every((p) => !unknown.includes(p.id)));
      assert.deepStrictEqual(sorted(sum.roots.map((r) => r.id)), sorted(expectRoots), 'Root causes for ' + t.id);
      const perTopic = {};
      asked.forEach((a) => { const id = a.split('#')[0]; perTopic[id] = (perTopic[id] || 0) + 1; });
      Object.keys(perTopic).forEach((id) => {
        const want = known.has(id) ? E.needConfirm(RGQ, s, id) : 2;
        assert.strictEqual(perTopic[id], want, id);
      });
      const pathIds = sum.path.map((p) => p.id);
      assertTopological(pathIds, RGQ);
      sum.weak.forEach((id) => assert.ok(pathIds.includes(id), 'Weak topic should be in the path: ' + id));
      assert.strictEqual(sum.finished, true);
    });
  }
  assert.ok(cases >= 900);
  assert.strictEqual(conf, 3);
});

test('With a question bank: a miss on question one followed by a correct answer on question two marks any topic for review, asks two questions, and does not trace prerequisites', () => {
  let withPrereq = 0;
  formal.forEach((t) => {
    const { s, asked } = simulateBank([t.id], new Set(), new Set([t.id]), 9999);
    assert.deepStrictEqual(asked, [t.id + '#1', t.id + '#2'], t.id);
    assert.strictEqual(E.statusOf(s, t.id), 'shaky');
    const sum = E.summarize(RGQ, s);
    assert.deepStrictEqual(sum.shaky, [t.id]);
    assert.deepStrictEqual(sum.weak, []);
    assert.deepStrictEqual(sum.roots, []);
    assert.deepStrictEqual(sum.path.map((p) => p.id), [t.id]);
    assert.strictEqual(sum.path[0].status, 'shaky');
    if (RGQ.prereqs[t.id].length) withPrereq++;
  });
  assert.ok(withPrereq > 200);
});

test('With a question bank: mixed student (known / shaky / unknown) uses at most confirm questions for known topics and two for others; statuses match the student', () => {
  const rand = rng(99);
  const known = makeStudent(rand, 0.1);
  const flaky = new Set(topics.filter((t) => !t.external && !known.has(t.id) && rand() < 0.3).map((t) => t.id));
  formal.forEach((t) => {
    const { s, asked } = simulateBank([t.id], known, flaky, 9999);
    const cnt = {};
    asked.forEach((a) => { const id = a.split('#')[0]; cnt[id] = (cnt[id] || 0) + 1; });
    Object.keys(cnt).forEach((id) => {
      const maxN = known.has(id) ? E.needConfirm(RGQ, s, id) : 2;
      assert.ok(cnt[id] <= maxN, id + ' ' + cnt[id] + ' > ' + maxN);
    });
    Object.keys(s.status).forEach((id) => {
      const st = s.status[id];
      if (st.src !== 'direct') { assert.strictEqual(st.s, 'mastered'); return; }
      const want = known.has(id) ? 'mastered' : flaky.has(id) ? 'shaky' : 'weak';
      assert.strictEqual(st.s, want, id);
    });
    const sum = E.summarize(RGQ, s);
    sum.shaky.forEach((id) => assert.ok(sum.path.some((p) => p.id === id), 'Topic needing review should be in the path: ' + id));
    const all = new Set(sum.mastered.concat(sum.shaky, sum.weak, sum.untested));
    assert.strictEqual(all.size, s.order.length);
    assert.strictEqual(sum.mastered.length + sum.shaky.length + sum.weak.length + sum.untested.length, s.order.length);
  });
});

test('With a question bank: limits (8/16/30) count questions and are never exceeded; unconfirmed topics are reported', () => {
  const rand = rng(11);
  [8, 16, 30].forEach((limit) => {
    const known = makeStudent(rand, 0.02);
    let capped = 0;
    formal.forEach((t) => {
      const { s, asked } = simulateBank([t.id], known, new Set(), limit);
      assert.ok(asked.length <= limit, t.id);
      if (asked.length === limit) capped++;
      const sum = E.summarize(RGQ, s);
      assert.strictEqual(sum.asked, asked.length);
      sum.unconfirmed.forEach((id) => assert.ok(sum.weak.includes(id)));
      const all = new Set(sum.mastered.concat(sum.shaky, sum.weak, sum.untested));
      assert.strictEqual(all.size, s.order.length);
    });
    if (limit === 8) assert.ok(capped > 0, 'At least one target should reach the limit');
  });
});

test('With a question bank: a fixed seed makes the full question sequence deterministic; changing the seed changes it; replay matches', () => {
  const known = new Set(); // Student knows nothing: two misses produce the longest sequence and make question-selection randomness obvious.
  const a = simulateBank(['cnm_232'], known, new Set(), 16, 'fixed');
  const b = simulateBank(['cnm_232'], known, new Set(), 16, 'fixed');
  assert.deepStrictEqual(a.s.answers.map((x) => x.qid), b.s.answers.map((x) => x.qid));
  const qs = new Set();
  for (let i = 0; i < 30; i++) qs.add(simulateBank(['cnm_232'], known, new Set(), 16, 'seed' + i).s.answers.map((x) => x.qid).join());
  assert.ok(qs.size > 3);
  const r = E.replay(RGQ, ['cnm_232'], a.s.answers, { limit: 16, seed: 'fixed' });
  assert.deepStrictEqual(r, a.s);
});

test('With a question bank: retests avoid previously asked questions when possible', () => {
  const known = makeStudent(rng(8), 0.1);
  const first = simulateBank(['cnm_232'], known, new Set(), 16, 'one');
  const seen = first.s.answers.map((x) => x.qid);
  let s = E.createSession(RGQ, ['cnm_232'], { limit: 16, seed: 'two', avoid: seen });
  let repeats = 0, total = 0;
  for (let guard = 0; guard < 100; guard++) {
    const it = E.nextItem(RGQ, s);
    if (!it) break;
    total++;
    if (it.attempt === 1 && seen.includes(it.question.id)) {
      // Repetition is possible only when every non-advanced question for this topic has already been used.
      const fresh = RGQ.bank[it.topicId].filter((q) => !seen.includes(q.id) && q.difficulty !== 'advanced' && q.difficulty !== 'challenge');
      assert.strictEqual(fresh.length, 0, it.topicId + ' repeated a question despite having an unused one');
      repeats++;
    }
    s = E.applyAnswer(RGQ, s, it.topicId, known.has(it.topicId) ? 'correct' : 'wrong');
  }
  assert.ok(total > 0);
});

console.log('Full-grade / full-volume screening');

function screenRun(spec, student, limit, seed, confirm) {
  let s = E.createSession(RGQ, spec.ids, {
    mode: 'screen', limit: limit, seed: seed == null ? 'scr' : seed,
    confirm: confirm == null ? E.DEFAULT_CONFIRM : confirm
  });
  for (let guard = 0; guard < 2000; guard++) {
    const it = E.nextItem(RGQ, s);
    if (!it) break;
    s = E.applyAnswer(RGQ, s, it.topicId, student(it.topicId, it.attempt));
  }
  return s;
}
const allWrong = () => 'wrong';
const allRight = () => 'correct';
const indexStudent = (id, attempt) => {
  const i = RGQ.index[id];
  if (i % 6 === 0) return 'wrong';
  if (i % 6 === 3) return attempt === 1 ? 'wrong' : 'correct';
  return 'correct';
};

test('gradeTargets: Grade 1 = 一上 + 一下; 七上 includes only 七上; invalid syntax returns null', () => {
  const g1 = E.gradeTargets(RGQ, '一年级');
  const up = E.gradeTargets(RGQ, '一上');
  const down = E.gradeTargets(RGQ, '一下');
  assert.deepStrictEqual(g1.volumes, ['一上', '一下']);
  assert.strictEqual(g1.ids.length, up.ids.length + down.ids.length);
  assert.deepStrictEqual(sorted(g1.ids), sorted(up.ids.concat(down.ids)));
  const want = formal.filter((t) => t.grade === 1 && E.subjectOf(t) === 'math').length;
  assert.strictEqual(g1.ids.length, want);
  const g1zh = E.gradeTargets(RGQ, '一年级', 'chinese');
  assert.strictEqual(g1zh.ids.length, 79); // 一上 41 + 一下 38.
  assert.ok(g1zh.ids.every((id) => id.startsWith('cnc_')));
  const g7 = E.gradeTargets(RGQ, '七年级');
  assert.strictEqual(g7.ids.length, formal.filter((t) => t.grade === 7 && String(t.id).startsWith('cnm_')).length);
  assert.ok(g7.ids.every((id) => id.startsWith('cnm_')));
  E.gradeTargets(RGQ, '七上').ids.forEach((id) => {
    const t = RGQ.byId[id];
    assert.ok(id.startsWith('cnm_') && t.grade === 7 && t.semester === '上' && !t.external, id);
  });
  assert.strictEqual(E.gradeTargets(RGQ, '十年级'), null);
  assert.strictEqual(E.gradeTargets(RGQ, '七'), null);
  assert.strictEqual(E.gradeTargets(RGQ, ''), null);
  const g10 = E.gradeTargets(RGQ, '高一');
  assert.strictEqual(g10.label, '高一（必修第一册）');
  assert.deepStrictEqual(g10.volumes, ['高一']);
  assert.strictEqual(g10.ids.length, 78);
  g10.ids.forEach((id) => assert.strictEqual(RGQ.byId[id].grade, 10));
  const g11 = E.gradeTargets(RGQ, '高二必修');
  assert.strictEqual(g11.label, '高二（必修第二册）');
  assert.strictEqual(g11.ids.length, 65);
  g11.ids.forEach((id) => assert.strictEqual(RGQ.byId[id].grade, 11));
  assert.deepStrictEqual(E.parseChapter('Grade 10, Required Volume 1, Chapter 1: Sets and Common Logical Notation, Section 1.1'), {
    volume: '高一', chapterNo: 'Chapter 1', chapterName: 'Sets and Common Logical Notation', section: '1.1'
  });
  assert.deepStrictEqual(E.parseChapter('Grade 11, Mathematical Inquiry: Study Triangles with Vectors', { id: 'cnm_h143', grade: 11, semester: '上' }), {
    volume: '高二', chapterNo: 'Mathematical Inquiry', chapterName: 'Study Triangles with Vectors', section: ''
  });
  const g12 = E.gradeTargets(RGQ, '选必一');
  assert.strictEqual(g12.label, '选必一（选择性必修第一册）');
  assert.deepStrictEqual(g12.volumes, ['选必一']);
  assert.strictEqual(g12.ids.length, 53);
  g12.ids.forEach((id) => assert.strictEqual(RGQ.byId[id].grade, 12));
  const g13 = E.gradeTargets(RGQ, '选择性必修第二册');
  assert.strictEqual(g13.label, '选必二（选择性必修第二册）');
  assert.strictEqual(g13.ids.length, 33);
  g13.ids.forEach((id) => assert.strictEqual(RGQ.byId[id].grade, 13));
  const g14 = E.gradeTargets(RGQ, '选必三');
  assert.strictEqual(g14.label, '选必三（选择性必修第三册）');
  assert.strictEqual(g14.ids.length, 42);
  g14.ids.forEach((id) => assert.strictEqual(RGQ.byId[id].grade, 14));
  assert.deepStrictEqual(E.parseChapter('Grade 13, Selective Required Volume 2, Chapter 5: Derivatives and Their Applications for One-Variable Functions, Section 5.1'), {
    volume: '选必二', chapterNo: 'Chapter 5', chapterName: 'Derivatives and Their Applications for One-Variable Functions', section: '5.1'
  });
  assert.deepStrictEqual(E.parseChapter('Grade 14, Mathematical Inquiry: Properties and Applications of Pascal’s Triangle', { id: 'cnm_h217', grade: 14, semester: '上' }), {
    volume: '选必三', chapterNo: 'Mathematical Inquiry', chapterName: 'Properties and Applications of Pascal’s Triangle', section: ''
  });
  assert.deepStrictEqual(E.parseChapter('Grade 14, Mathematical Modeling: Build a Statistical Model to Make Predictions', { id: 'cnm_h218', grade: 14, semester: '上' }), {
    volume: '选必三', chapterNo: 'Mathematical Modeling', chapterName: 'Build a Statistical Model to Make Predictions', section: ''
  });
  const pre = new Map();
  deps.forEach((d) => { (pre.get(d.topicId) || pre.set(d.topicId, []).get(d.topicId)).push(d.prerequisiteId); });
  topics.filter((t) => /^cnm_h(\d+)$/.test(t.id) && Number(t.id.slice(5)) >= 144).forEach((t) => {
    assert.ok(pre.get(t.id) && pre.get(t.id).length >= 1, t.id + ' should have at least one prerequisite');
  });
  assert.strictEqual(RGQ.byId.cnm_h001.name, 'Meaning of a Set');
  assert.strictEqual(RGQ.byId.cnm_h143.name, 'Estimating Probability from Frequency');
  assert.strictEqual(RGQ.byId.cnm_h217.name, 'Definition of a Derivative');
});

test('Screening session scope is exactly the target set and defaults to SCREEN_LIMIT; ordinary sessions are unchanged', () => {
  const g = E.gradeTargets(RGQ, '七年级');
  const s = E.createSession(RGQ, g.ids, { mode: 'screen' });
  assert.strictEqual(s.limit, E.SCREEN_LIMIT);
  assert.ok(E.SCREEN_LIMIT > E.DEFAULT_LIMIT);
  assert.deepStrictEqual(sorted(s.order), sorted(g.ids));
  assert.strictEqual(s.mode, 'screen');
  const n = E.createSession(RGQ, g.ids);
  assert.strictEqual(n.limit, E.DEFAULT_LIMIT);
  assert.strictEqual(n.mode, 'target');
  assert.strictEqual(n.scope, null);
  assert.ok(n.order.length > s.order.length, 'Ordinary session subgraph includes earlier-grade prerequisites');
  assert.strictEqual(E.createSession(RGQ, g.ids, { mode: 'screen', limit: 60 }).limit, 60);
});

test('Screening never exceeds its question limit (一年级 / 七年级 / 七上; all-wrong, all-correct, and mixed students)', () => {
  ['一年级', '七年级', '七上'].forEach((scope) => {
    const g = E.gradeTargets(RGQ, scope);
    [[allWrong, 40], [allRight, 40], [indexStudent, 40], [indexStudent, 25], [indexStudent, 60]].forEach(([stu, limit]) => {
      const s = screenRun(g, stu, limit);
      assert.ok(s.answers.length <= limit, scope + ' ' + s.answers.length + ' > ' + limit);
      const ids = new Set(g.ids);
      s.answers.forEach((a) => assert.ok(ids.has(a.id), 'Assessed a topic outside the scope: ' + a.id));
      const sum = E.summarize(RGQ, s);
      assert.strictEqual(sum.mastered.length + sum.shaky.length + sum.weak.length + sum.untested.length, g.ids.length);
      assert.strictEqual(sum.asked, s.answers.length);
    });
  });
});

test('Screening: an all-correct student needs few questions because mastery is inferred for prerequisites; Grade 1 fits the default limit', () => {
  // confirm=1 verifies that inferring mastery for prerequisites keeps a full-grade screen short.
  const g7 = E.gradeTargets(RGQ, '七年级');
  const s = screenRun(g7, allRight, 40, 'scr', 1);
  const sum = E.summarize(RGQ, s);
  assert.ok(sum.asked < g7.ids.length / 2, 'All-correct student was asked ' + sum.asked + ' questions');
  assert.strictEqual(sum.mastered.length, g7.ids.length);
  // With the default confirm=3, Grade 1 can still be completed when enough questions are allowed (indexStudent).
  const g1 = E.gradeTargets(RGQ, '一年级');
  const s1 = screenRun(g1, indexStudent, Math.max(E.SCREEN_LIMIT, g1.ids.length * E.DEFAULT_CONFIRM));
  assert.strictEqual(E.summarize(RGQ, s1).finished, true);
  assert.strictEqual(E.summarize(RGQ, s1).untested.length, 0);
  // With confirm=3 and a limit of 40, Grade 7 cannot be completed under the old one-question mastery rule, but asked is still below topics × confirm.
  const s3 = screenRun(g7, allRight, 40);
  const sum3 = E.summarize(RGQ, s3);
  assert.ok(sum3.asked <= 40);
  assert.ok(sum3.mastered.length > 0);
});

test('Screening marks remaining topics untested when the question limit is reached', () => {
  const g = E.gradeTargets(RGQ, '七年级');
  const s = screenRun(g, allWrong, 20);
  const sum = E.summarize(RGQ, s);
  assert.strictEqual(sum.asked, 20);
  assert.strictEqual(sum.limitReached, true);
  assert.ok(sum.untested.length > 0);
});

test('Screening traces only within scope: out-of-scope prerequisites are not asked and appear in outOfScopePrereqs', () => {
  const g = E.gradeTargets(RGQ, '七上');
  const s = screenRun(g, allWrong, 60);
  const inScope = new Set(g.ids);
  assert.ok(s.answers.every((a) => inScope.has(a.id)));
  const sum = E.summarize(RGQ, s);
  assert.ok(sum.roots.length > 0);
  const outside = new Set();
  sum.roots.forEach((r) => {
    r.pendingPrereqs.forEach((p) => assert.ok(inScope.has(p)));
    r.outOfScopePrereqs.forEach((p) => { assert.ok(!inScope.has(p)); outside.add(p); });
  });
  assert.ok(outside.size > 0, '七上 root causes should have prerequisites from earlier than Grade 7');
  // Out-of-scope topics should not appear in the summary.
  sum.mastered.concat(sum.shaky, sum.weak, sum.untested).forEach((id) => assert.ok(inScope.has(id)));
  assert.ok(sum.path.every((p) => inScope.has(p.id) && p.isTarget === false));
});

test('Screening with unlimited questions and a consistent student marks exactly the unknown in-scope topics weak', () => {
  const g = E.gradeTargets(RGQ, '七上');
  const inScope = new Set(g.ids);
  [0.3, 0.6, 0.9].forEach((p, k) => {
    const known = makeStudent(rng(100 + k), p);
    const s = screenRun(g, (id) => (known.has(id) ? 'correct' : 'wrong'), 1000);
    const sum = E.summarize(RGQ, s);
    assert.deepStrictEqual(sorted(sum.weak), sorted(g.ids.filter((id) => !known.has(id))));
    assert.strictEqual(sum.untested.length, 0);
    // A root cause is unknown while all in-scope prerequisites are known; out-of-scope prerequisites do not count.
    const wantRoots = g.ids.filter((id) => !known.has(id) &&
      !RGQ.prereqs[id].some((x) => inScope.has(x.id) && !known.has(x.id)));
    assert.deepStrictEqual(sorted(sum.roots.map((r) => r.id)), sorted(wantRoots));
  });
});

test('Screening: the same seed reproduces the question sequence; replay matches; a different seed changes the sequence', () => {
  const g = E.gradeTargets(RGQ, '七年级');
  const a = screenRun(g, indexStudent, 40, 'fixed');
  const b = screenRun(g, indexStudent, 40, 'fixed');
  assert.deepStrictEqual(a.answers.map((x) => x.qid), b.answers.map((x) => x.qid));
  const r = E.replay(RGQ, g.ids, a.answers, { mode: 'screen', limit: 40, seed: 'fixed' });
  assert.deepStrictEqual(r, a);
  const c = screenRun(g, indexStudent, 40, 'other');
  assert.notDeepStrictEqual(a.answers.map((x) => x.qid), c.answers.map((x) => x.qid));
  // Session survives a JSON round-trip.
  assert.deepStrictEqual(JSON.parse(JSON.stringify(a)), a);
});

test('Chapter summary groups topics correctly, matches summary counts, ranks weak chapters first, and is reproducible', () => {
  ['一年级', '七年级', '八上'].forEach((scope) => {
    const g = E.gradeTargets(RGQ, scope);
    const s = screenRun(g, indexStudent, 40);
    const sum = E.summarize(RGQ, s);
    const chs = E.chapterSummary(RGQ, s);
    // Each topic belongs to exactly one chapter; chapter totals equal the number of in-scope topics.
    assert.strictEqual(chs.reduce((n, c) => n + c.total, 0), g.ids.length);
    const seen = new Set();
    chs.forEach((c) => {
      assert.strictEqual(c.mastered + c.shaky + c.weak + c.untested, c.total, c.label);
      assert.strictEqual(c.weakIds.length, c.weak);
      assert.strictEqual(c.shakyIds.length, c.shaky);
      c.weakIds.concat(c.shakyIds, c.untestedIds).forEach((id) => {
        assert.ok(!seen.has(id)); seen.add(id);
        const p = E.parseChapter(RGQ.byId[id].chapter, RGQ.byId[id]);
        assert.strictEqual(c.volume + ' ' + c.chapterNo + ' ' + c.chapterName, p.volume + ' ' + p.chapterNo + ' ' + p.chapterName);
        assert.ok(g.volumes.includes(p.volume));
      });
      c.weakIds.forEach((id) => assert.strictEqual(E.statusOf(s, id), 'weak'));
      c.shakyIds.forEach((id) => assert.strictEqual(E.statusOf(s, id), 'shaky'));
    });
    assert.strictEqual(chs.reduce((n, c) => n + c.weak, 0), sum.weak.length);
    assert.strictEqual(chs.reduce((n, c) => n + c.shaky, 0), sum.shaky.length);
    assert.strictEqual(chs.reduce((n, c) => n + c.mastered, 0), sum.mastered.length);
    assert.strictEqual(chs.reduce((n, c) => n + c.untested, 0), sum.untested.length);
    for (let i = 1; i < chs.length; i++) {
      const a = chs[i - 1], b = chs[i];
      assert.ok(a.weak > b.weak || (a.weak === b.weak && a.shaky >= b.shaky), 'Sort order: ' + a.label + ' / ' + b.label);
    }
    assert.ok(chs[0].weak >= 1, scope + ' first chapter should contain a weak topic');
    assert.deepStrictEqual(chs, E.chapterSummary(RGQ, screenRun(g, indexStudent, 40)));
  });
});

test('Chapter summary: 七上 has six chapters; an unanswered session marks all topics untested and preserves textbook order', () => {
  const g = E.gradeTargets(RGQ, '七上');
  const s = screenRun(g, allWrong, 60);
  const chs = E.chapterSummary(RGQ, s);
  assert.strictEqual(chs.length, 6);
  const tiny = E.chapterSummary(RGQ, E.createSession(RGQ, g.ids, { mode: 'screen' }));
  assert.ok(tiny.every((c) => c.untested === c.total && c.weak === 0));
  assert.deepStrictEqual(tiny.map((c) => c.label).slice(0, 2), ['七上 Chapter 1 Rational Numbers', '七上 Chapter 2 Operations with Rational Numbers']);
});

test('Screening path graph contains only topics with learning gaps, not the entire grade', () => {
  const g = E.gradeTargets(RGQ, '七年级');
  const s = screenRun(g, indexStudent, 40);
  const sum = E.summarize(RGQ, s);
  const lay = E.layout(RGQ, s, sum);
  assert.ok(lay.nodes.length < g.ids.length);
  assert.ok(lay.nodes.every((n) => n.isTarget === false));
  const allOk = E.summarize(RGQ, screenRun(g, allRight, 40));
  assert.strictEqual(allOk.path.length, 0);
});

test('Ordinary chapter and single-topic diagnostics are unchanged; sessions without mode still trace to elementary topics', () => {
  const s = E.createSession(RGQ, ['cnm_232'], { limit: 16 });
  assert.strictEqual(s.mode, 'target');
  assert.ok(s.order.length > 1);
  const sum = E.summarize(RGQ, s);
  assert.strictEqual(sum.mode, 'target');
  sum.roots.forEach((r) => assert.deepStrictEqual(r.outOfScopePrereqs, []));
});

console.log('\n' + passed + ' passed, ' + failed + ' failed');
process.exit(failed ? 1 : 0);
