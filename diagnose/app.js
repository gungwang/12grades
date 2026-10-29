/* Diagnostic UI. Core logic lives in engine.js; this file handles data loading, rendering, and local storage. */
(function () {
  'use strict';
  const E = window.DiagEngine;
  const LS_SESSION = 'cnmDiagnose.session.v2';
  const LS_SESSION_EN = 'cneDiagnose.session.v2';
  const LS_SESSION_PHY = 'cnpDiagnose.session.v2';
  const LS_SESSION_ZH = 'cncDiagnose.session.v2';
  const LS_SETTINGS = 'cnmDiagnose.settings.v2';
  const LS_SEEN = 'cnmDiagnose.seen.v1';
  const LIMIT_MIN = 8, LIMIT_MAX = 30;
  const SCREEN_MIN = 20, SCREEN_MAX = 60;
  const GRADES = '一二三四五六七八九'.split('');
  const VOLUMES = [
    ['一上', 'Grade 1, Semester 1'], ['一下', 'Grade 1, Semester 2'], ['二上', 'Grade 2, Semester 1'], ['二下', 'Grade 2, Semester 2'],
    ['三上', 'Grade 3, Semester 1'], ['三下', 'Grade 3, Semester 2'], ['四上', 'Grade 4, Semester 1'], ['四下', 'Grade 4, Semester 2'],
    ['五上', 'Grade 5, Semester 1'], ['五下', 'Grade 5, Semester 2'], ['六上', 'Grade 6, Semester 1'], ['六下', 'Grade 6, Semester 2'],
    ['七上', 'Grade 7, Semester 1'], ['七下', 'Grade 7, Semester 2'], ['八上', 'Grade 8, Semester 1'], ['八下', 'Grade 8, Semester 2'],
    ['九上', 'Grade 9, Semester 1'], ['九下', 'Grade 9, Semester 2'], ['九全', 'Grade 9, Full-Year Volume'],
    ['必修一', 'Required Volume 1'], ['必修二', 'Required Volume 2'], ['必修三', 'Required Volume 3'],
    ['高一', 'High School Year 1 · Required Volume 1'], ['高二', 'High School Year 2 · Required Volume 2'],
    ['选必一', 'Selective Required Volume 1'], ['选必二', 'Selective Required Volume 2'],
    ['选必三', 'Selective Required Volume 3'], ['选必四', 'Selective Required Volume 4']
  ];
  const RESULT_LABEL = { correct: 'Correct', wrong: 'Incorrect', skip: "I don't know" };
  const STATUS_LABEL = { mastered: 'Mastered', shaky: 'Needs Review', weak: 'Weak', unknown: 'Not Tested' };
  const DIFF_LABEL = { basic: 'Foundation', standard: 'Intermediate', challenge: 'Advanced', advanced: 'Advanced' };
  const TYPE_LABEL = { numeric: 'Numeric', choice: 'Multiple Choice', short: 'Short Answer', self: 'Open Response', legacy: 'Diagnostic' };
  const GRADE_NUMBER = { '一': '1', '二': '2', '三': '3', '四': '4', '五': '5', '六': '6', '七': '7', '八': '8', '九': '9' };
  const SCOPE_LABELS = {
    '高一（必修第一册）': 'High School Year 1 · Required Volume 1',
    '高二（必修第二册）': 'High School Year 2 · Required Volume 2',
    '选必一（选择性必修第一册）': 'Selective Required Volume 1',
    '选必二（选择性必修第二册）': 'Selective Required Volume 2',
    '选必三（选择性必修第三册）': 'Selective Required Volume 3',
    '选必四（选择性必修第四册）': 'Selective Required Volume 4',
    '必修一（必修第一册）': 'Required Volume 1',
    '必修二（必修第二册）': 'Required Volume 2',
    '必修三（必修第三册）': 'Required Volume 3',
    '高一': 'High School Year 1', '高二': 'High School Year 2',
    '必修一': 'Required Volume 1', '必修二': 'Required Volume 2', '必修三': 'Required Volume 3',
    '选必一': 'Selective Required Volume 1', '选必二': 'Selective Required Volume 2',
    '选必三': 'Selective Required Volume 3', '选必四': 'Selective Required Volume 4'
  };
  const DOMAIN_LABELS = {
    '数与代数': 'Numbers and Algebra',
    '图形与几何': 'Geometry and Measurement',
    '统计与概率': 'Statistics and Probability',
    '综合与实践': 'Integrated Practice',
    '拼音': 'Pinyin', '识字写字': 'Characters and Writing', '词语': 'Vocabulary',
    '句子': 'Sentences', '阅读理解': 'Reading Comprehension',
    '古诗文积累': 'Classical Poetry and Prose', '习作基础': 'Writing Skills',
    '日常表达': 'Everyday Expressions', '词汇': 'Vocabulary', '语法': 'Grammar',
    '语音': 'Pronunciation', '读写': 'Reading and Writing',
    '物质': 'Matter', '能量': 'Energy', '跨学科实践': 'Interdisciplinary Practice',
    '运动和相互作用': 'Motion and Interaction'
  };

  function displayScopeLabel(value) {
    let text = String(value || '');
    text = text.replace(/（整体筛查）/g, ' (full-grade screening)')
      .replace(/（整章）/g, ' (entire chapter)')
      .replace(/（旧编号已对应到小学知识点）/g, ' (legacy ID mapped to elementary topics)');
    const labels = Object.keys(SCOPE_LABELS).sort(function (a, b) { return b.length - a.length; });
    for (let i = 0; i < labels.length; i++) {
      if (text.indexOf(labels[i]) === 0) return SCOPE_LABELS[labels[i]] + text.slice(labels[i].length);
    }
    let match = /^([一二三四五六七八九])年级(全一册|上册|下册)?/.exec(text);
    if (match) {
      const suffix = match[2] === '上册' ? ', Semester 1' : match[2] === '下册' ? ', Semester 2' : match[2] === '全一册' ? ' (Full-Year Volume)' : '';
      return 'Grade ' + GRADE_NUMBER[match[1]] + suffix + text.slice(match[0].length);
    }
    match = /^([一二三四五六七八九])([上下全])(?=\s|$|（)/.exec(text);
    if (match) {
      const suffix = match[2] === '上' ? ', Semester 1' : match[2] === '下' ? ', Semester 2' : ' (Full-Year Volume)';
      return 'Grade ' + GRADE_NUMBER[match[1]] + suffix + text.slice(match[0].length);
    }
    match = /^(必修第([一二三])册|选择性必修第([一二三四])册)(?=\s|$)/.exec(text);
    if (match) {
      const volume = match[2] ? ({ '一': 1, '二': 2, '三': 3 }[match[2]]) : ({ '一': 1, '二': 2, '三': 3, '四': 4 }[match[3]]);
      const label = match[2] ? 'Required Volume ' + volume : 'Selective Required Volume ' + volume;
      return label + text.slice(match[0].length);
    }
    match = /^(高[一二]|选必[一二三四])(?=\s|$)/.exec(text);
    if (match) {
      const labels = { '高一': 'High School Year 1', '高二': 'High School Year 2', '选必一': 'Selective 1', '选必二': 'Selective 2', '选必三': 'Selective 3', '选必四': 'Selective 4' };
      return labels[match[1]] + text.slice(match[0].length);
    }
    return text;
  }
  function displayGrade(value) {
    const text = String(value || '');
    return GRADE_NUMBER[text] ? 'Grade ' + GRADE_NUMBER[text] : displayScopeLabel(text);
  }
  function displayDomain(value) { return DOMAIN_LABELS[value] || value; }

  const root = document.getElementById('root');
  let D = null;            // Data: {topics, deps, stdById, graph, tree}
  let session = null;      // Engine session.
  let sessionMeta = null;  // {label, chapterKey?}
  let demo = null;         // Demo mode: {oracle}.
  let ui = { key: null, phase: 'ask', answer: '', verdict: null };
  let subject = 'math';
  let startQuery = '';
  let startStage = '';
  let chapterOpen = false;
  let gradeSel = '七';     // Grade selected for full-grade screening on the start page.
  let volSel = '';         // '' means full grade; '上' and '下' select a semester.
  let seedParam = null;    // URL seed parameter for deterministic question selection.
  let pathCy = null;
  let pathToken = 0;
  let pathTipLock = false;
  let pathExpanded = false;
  const PATH_FOLD_AT = 40;
  let shareBlobUrl = null;
  let shareToken = 0;

  /* ------------------------------------------------------------ Utilities */
  function h(tag, attrs) {
    const el = document.createElement(tag);
    const a = attrs || {};
    Object.keys(a).forEach(function (k) {
      const v = a[k];
      if (v == null || v === false) return;
      if (k === 'class') el.className = v;
      else if (k === 'text') el.textContent = v;
      else if (k.slice(0, 2) === 'on') el.addEventListener(k.slice(2), v);
      else if (k === 'open' || k === 'disabled' || k === 'selected' || k === 'value') el[k] = v === true ? true : v;
      else el.setAttribute(k, v === true ? '' : v);
    });
    for (let i = 2; i < arguments.length; i++) append(el, arguments[i]);
    return el;
  }
  function append(el, c) {
    if (c == null || c === false) return;
    if (Array.isArray(c)) { c.forEach(function (x) { append(el, x); }); return; }
    el.append(c.nodeType ? c : document.createTextNode(String(c)));
  }
  function figureEl(svg) {
    if (typeof svg !== 'string' || svg.indexOf('<svg') !== 0) return null;
    if (/<\s*script|foreignObject|<\s*image\b|https?:\/\//i.test(svg.replace('xmlns="http://www.w3.org/2000/svg"', ''))) return null;
    const wrap = h('div', { class: 'q-figure' });
    wrap.innerHTML = svg;
    const node = wrap.querySelector('svg');
    if (!node) return null;
    node.setAttribute('role', 'img');
    node.setAttribute('aria-hidden', 'true');
    node.setAttribute('focusable', 'false');
    return wrap;
  }
  function sessionKey() {
    if (subject === 'english') return LS_SESSION_EN;
    if (subject === 'physics') return LS_SESSION_PHY;
    if (subject === 'chinese') return LS_SESSION_ZH;
    return LS_SESSION;
  }
  function withSubject(href) {
    if (subject === 'math' || !href || href.indexOf('subject=') >= 0 || href.indexOf('http') === 0) return href;
    return href + (href.indexOf('?') >= 0 ? '&' : '?') + 'subject=' + subject;
  }
  function detectSubject() {
    const params = new URLSearchParams(location.search);
    const explicit = params.get('subject');
    if (explicit === 'english' || explicit === 'math' || explicit === 'physics' || explicit === 'chinese') return explicit;
    const target = params.get('target') || '';
    let hashId = (location.hash || '').replace(/^#/, '');
    try { hashId = decodeURIComponent(hashId); } catch (e) { /* Leave the value unchanged. */ }
    if (/(^|,)\s*cne_/.test(target) || /^cne_/.test(hashId)) {
      params.set('subject', 'english');
      history.replaceState(null, '', location.pathname + '?' + params.toString() + location.hash);
      return 'english';
    }
    if (/(^|,)\s*cnp_/.test(target) || /^cnp_/.test(hashId)) {
      params.set('subject', 'physics');
      history.replaceState(null, '', location.pathname + '?' + params.toString() + location.hash);
      return 'physics';
    }
    if (/(^|,)\s*cnc_/.test(target) || /^cnc_/.test(hashId)) {
      params.set('subject', 'chinese');
      history.replaceState(null, '', location.pathname + '?' + params.toString() + location.hash);
      return 'chinese';
    }
    return 'math';
  }
  function applySubjectChrome() {
    document.body.classList.toggle('subject-english', subject === 'english');
    document.body.classList.toggle('subject-physics', subject === 'physics');
    document.body.classList.toggle('subject-chinese', subject === 'chinese');
    document.querySelectorAll('.site-nav a:not(.subject-link), a.brand').forEach(function (link) {
      const href = link.getAttribute('href');
      const next = withSubject(href);
      if (next && next !== href) link.setAttribute('href', next);
    });
    document.querySelectorAll('.subject-link').forEach(function (link) {
      const on = link.getAttribute('data-subject') === subject;
      link.classList.toggle('on', on);
      if (on) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    });
    if (subject === 'english') {
      document.title = 'Diagnostics · English';
      var juniorOk = '三四五六七八九'.indexOf(gradeSel) >= 0;
      var seniorOk = gradeSel.indexOf('必修') === 0 || gradeSel.indexOf('选必') === 0;
      if (!juniorOk && !seniorOk) gradeSel = '四';
    }
    if (subject === 'physics') {
      document.title = 'Diagnostics · Physics';
      if (gradeSel !== '八' && gradeSel !== '九' && !/^(必修[一二三]|选必[一二三])$/.test(gradeSel)) gradeSel = '八';
      if (gradeSel === '九') volSel = '全';
    }
    if (subject === 'chinese') {
      document.title = 'Diagnostics · Chinese';
      if ('一二三四五六'.indexOf(gradeSel) < 0) gradeSel = '一';
      if (volSel === '全') volSel = '';
    }
  }
  function lsGet(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* For example, private browsing mode. */ } }
  function lsDel(k) { try { localStorage.removeItem(k); } catch (e) { /* ignore */ } }
  function nameOf(id) { const t = D.graph.byId[id]; return t ? t.name : id; }
  function getSettings() {
    const st = lsGet(LS_SETTINGS) || {};
    let limit = parseInt(st.limit, 10);
    if (!(limit >= LIMIT_MIN && limit <= LIMIT_MAX)) limit = E.DEFAULT_LIMIT;
    let screenLimit = parseInt(st.screenLimit, 10);
    if (!(screenLimit >= SCREEN_MIN && screenLimit <= SCREEN_MAX)) screenLimit = E.SCREEN_LIMIT;
    const confirm = E.clampConfirm(st.confirm);
    return { limit: limit, screenLimit: screenLimit, confirm: confirm };
  }
  function setSetting(k, v) { const o = getSettings(); o[k] = v; lsSet(LS_SETTINGS, o); }
  function seenList() { const v = lsGet(LS_SEEN); return Array.isArray(v) ? v : []; }
  function markSeen(qid) {
    if (!qid || demo) return;
    const v = seenList();
    if (v.indexOf(qid) < 0) { v.push(qid); lsSet(LS_SEEN, v); }
  }
  function newSeed() { return seedParam != null ? seedParam : Math.random().toString(36).slice(2, 10); }
  function resetUi() { ui = { key: null, phase: 'ask', answer: '', verdict: null, picked: null }; }
  function clearRoot() { while (root.firstChild) root.removeChild(root.firstChild); }
  function teardownPath() {
    pathToken++;
    pathTipLock = false;
    if (pathCy) { pathCy.destroy(); pathCy = null; window.__pathCy = null; }
  }
  function show(node) { teardownPath(); closeShare(); clearRoot(); root.append(node); window.scrollTo(0, 0); }
  function cssVar(name) { return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); }
  function theme() {
    return {
      primary: cssVar('--node-primary'), primaryBg: cssVar('--node-primary-bg'),
      junior: cssVar('--node-junior'), juniorBg: cssVar('--node-junior-bg'),
      senior: cssVar('--node-senior'), seniorBg: cssVar('--node-senior-bg'),
      currentBg: cssVar('--node-current-bg'), currentBorder: cssVar('--node-current-border'),
      text: cssVar('--node-text'), edge: cssVar('--edge'), edgeSoft: cssVar('--edge-soft'),
      bad: cssVar('--diagram-bad'), badBg: cssVar('--diagram-bad-bg')
    };
  }
  function labelLimit() { return window.matchMedia('(max-width: 700px)').matches ? 8 : 10; }
  function clipLabel(name) {
    const chars = Array.from(name || '');
    const limit = labelLimit();
    if (chars.length <= limit) return name || '';
    return chars.slice(0, limit - 1).join('') + '…';
  }

  /* ------------------------------------------------------------ Data */
  async function loadData() {
    const urls = ['../data/topics.json', '../data/dependencies.json', '../data/cn-curriculum-standards.json', '../data/id-aliases.json'];
    const rs = await Promise.all(urls.map(function (u) { return fetch(u); }));
    rs.forEach(function (r, i) { if (!r.ok) throw new Error(urls[i] + ' → HTTP ' + r.status); });
    const js = await Promise.all(rs.map(function (r) { return r.json(); }));
    // The question bank is optional: if missing (404) or invalid, fall back to diagnostic_question in topics.json.
    let questions = null;
    try {
      const qr = await fetch('../data/questions.json');
      if (qr.ok) questions = await qr.json();
    } catch (e) { questions = null; }
    const topics = js[0].filter(function (t) { return E.subjectOf(t) === subject; });
    const allow = {};
    topics.forEach(function (t) { allow[t.id] = true; });
    const deps = js[1].filter(function (d) { return allow[d.topicId] && allow[d.prerequisiteId]; });
    if (questions) questions = questions.filter(function (q) { return allow[q.topicId]; });
    const stdById = {};
    js[2].items.forEach(function (x) { stdById[x.id] = x; });
    const graph = E.buildGraph(topics, deps, questions);
    D = { topics: topics, deps: deps, stdById: stdById, graph: graph, tree: buildTree(topics), aliases: (js[3] && js[3].aliases) || {} };
  }

  function buildTree(topics) {
    const vols = {};
    topics.forEach(function (t) {
      if (t.external) return;
      const c = E.parseChapter(t.chapter, t);
      const v = vols[c.volume] || (vols[c.volume] = { chapters: [], byKey: {} });
      const key = c.chapterNo + ' ' + c.chapterName;
      let ch = v.byKey[key];
      if (!ch) {
        ch = v.byKey[key] = { volume: c.volume, key: c.volume + ' ' + c.chapterNo, label: c.chapterNo + ' ' + c.chapterName, topics: [] };
        v.chapters.push(ch);
      }
      ch.topics.push({ t: t, section: c.section });
    });
    return vols;
  }

  /* ------------------------------------------------------------ Child profiles */
  const CC = window.CnmChildren;
  function childLabel(c) { return c.name + (c.grade ? ' (' + displayGrade(c.grade) + ')' : ''); }
  function childrenHref(path) { return '../children/' + (path || ''); }
  function fromQuery() { return '?from=diagnose' + (subject !== 'math' ? '&subject=' + subject : ''); }
  function childSelect(onPick) {
    const cur = CC.current();
    const sel = h('select', { id: 'child-select', 'aria-label': 'Current child' },
      h('option', { value: '' }, "Don't save to a profile"),
      CC.list().map(function (c) { return h('option', { value: c.id, selected: !!cur && cur.id === c.id }, childLabel(c)); }));
    sel.value = cur ? cur.id : '';
    sel.addEventListener('change', function () { onPick(sel.value || null); });
    return sel;
  }
  function childBar(mode) {
    if (demo) return null;
    const kids = CC.list();
    const cur = CC.current();
    if (!kids.length) {
      return h('div', { class: 'banner child-bar no-print', id: 'child-bar' },
        h('b', { text: 'No child profiles yet.' }),
        ' Add a profile to save diagnostic results separately and review each session and its learning gaps later. ',
        h('a', { class: 'btn btn-primary', href: childrenHref(fromQuery()), text: 'Add a Child' }));
    }
    if (mode === 'question') {
      return h('div', { class: 'child-bar compact row no-print', id: 'child-bar' },
        h('span', { class: 'muted small' }, 'Current child'),
        childSelect(function (id) { CC.setCurrent(id); }));
    }
    if (mode === 'result') {
      const key = recordKey();
      return h('div', { class: 'card child-bar no-print', id: 'child-bar' },
        h('p', { style: 'margin:0 0 8px' }, cur
          ? [h('b', { text: 'Saved to ' + cur.name + '’s profile.' }), ' Changing the selected child will move this record too.']
          : [h('b', { text: 'These results have not been saved to a profile.' }), ' Select a child to save them.']),
        h('div', { class: 'row' },
          h('label', { for: 'child-select' }, 'Save to'),
          childSelect(function (id) {
            if (cur && id !== cur.id) { if (id) CC.moveRecord(key, cur.id, id); else CC.removeRecord(cur.id, key); }
            CC.setCurrent(id);
            renderResult();
          }),
          cur ? h('a', { class: 'btn', href: childrenHref('history.html?child=' + encodeURIComponent(cur.id)), text: 'History & Learning Gaps' }) : null));
    }
    return h('div', { class: 'card child-bar no-print', id: 'child-bar' },
      h('div', { class: 'row' },
        h('label', { for: 'child-select' }, 'Current child'),
        childSelect(function (id) { CC.setCurrent(id); renderStart(); }),
        h('span', { class: 'grow' }),
        cur ? h('a', { class: 'btn', href: childrenHref('history.html?child=' + encodeURIComponent(cur.id)), text: 'History & Learning Gaps' }) : null,
        h('a', { class: 'btn', href: childrenHref(fromQuery()), text: 'Profiles' })),
      h('p', { class: 'muted small', style: 'margin:8px 0 0' },
        cur ? 'Results will be saved to ' + cur.name + '’s profile when the diagnostic is complete.' : 'Results are not saved when “Don’t save to a profile” is selected.'));
  }
  function recordKey() { return [subject, session.seed, session.targets.join(',')].join('|'); }
  function saveToChild(sum) {
    const cur = CC.current();
    if (demo || !cur || !sum.asked) return;
    CC.saveRecord(cur.id, {
      key: recordKey(), subject: subject, label: displayScopeLabel(sessionMeta.label), mode: sum.mode, asked: sum.asked,
      targets: sum.mode === 'screen' || sum.targets.length > 6 ? null : sum.targets,
      counts: { weak: sum.weak.length, shaky: sum.shaky.length, mastered: sum.mastered.length, untested: sum.untested.length },
      weak: sum.weak, roots: sum.roots.map(function (r) { return r.id; }), shaky: sum.shaky, mastered: sum.mastered
    });
  }

  /* ------------------------------------------------------------ Session */
  function save() {
    if (demo || !session) return;
    lsSet(sessionKey(), {
      v: 2, mode: session.mode, targets: session.targets, limit: session.limit, confirm: session.confirm,
      label: displayScopeLabel(sessionMeta.label), answers: session.answers,
      seed: session.seed, avoid: session.avoid, savedAt: new Date().toISOString()
    });
  }

  function startSession(targets, label, limit, mode) {
    pathExpanded = false;
    const screen = mode === 'screen';
    const st = getSettings();
    session = E.createSession(D.graph, targets, {
      mode: mode, limit: limit || (screen ? st.screenLimit : st.limit), confirm: st.confirm, seed: newSeed(), avoid: seenList()
    });
    sessionMeta = { label: label };
    resetUi();
    save();
    render();
  }

  function restoreSession(saved) {
    try {
      session = E.replay(D.graph, saved.targets, saved.answers, {
        mode: saved.mode, limit: saved.limit, confirm: saved.confirm, seed: saved.seed, avoid: saved.avoid
      });
      sessionMeta = { label: saved.label || saved.targets.map(nameOf).join('、') };
      return true;
    } catch (e) { return false; }
  }

  function restart() {
    pathExpanded = false;
    session = null; demo = null;
    lsDel(sessionKey());
    history.replaceState(null, '', location.pathname + (subject !== 'math' ? '?subject=' + subject : ''));
    render();
  }

  function commit(result) {
    const item = E.nextItem(D.graph, session);
    session = E.applyAnswer(D.graph, session, item.topicId, result, { text: ui.answer });
    markSeen(item.question.id);
    resetUi();
    save();
    render();
  }

  function rebuild(answers, limit) {
    session = E.replay(D.graph, session.targets, answers, {
      mode: session.mode, limit: limit == null ? session.limit : limit, confirm: session.confirm,
      seed: session.seed, avoid: session.avoid
    });
    resetUi();
    save();
    render();
  }

  /* ------------------------------------------------------------ Demo mode */
  // Simulated student: misses the target twice (weak) and also misses its first assessable prerequisite; one miss followed by a correct answer on an earlier or alternate prerequisite marks it for review; answers the rest correctly.
  function makeOracle(targets, mode) {
    const G = D.graph;
    if (mode === 'screen') {
      // Full-grade screening: based on topic index, simulate about 1/6 weak, 1/6 needing review, and the rest mastered (as in scripts/demo_grade.js).
      return function (id, attempt) {
        const i = G.index[id];
        if (i % 6 === 0) return 'wrong';
        if (i % 6 === 3) return attempt === 1 ? 'wrong' : 'correct';
        return 'correct';
      };
    }
    const t0 = E.createSession(G, targets).stack[0];
    const testablePre = function (id) { return G.prereqs[id].filter(function (x) { return E.isTestable(G, x.id); }).map(function (x) { return x.id; }); };
    const weak = new Set([t0]);
    const shaky = new Set();
    const p = testablePre(t0);
    if (p.length) {
      const q = testablePre(p[0]);
      if (q.length) { weak.add(p[0]); shaky.add(q[0]); }
      else if (p.length > 1) { weak.add(p[0]); shaky.add(p[1]); }
      else shaky.add(p[0]);
    }
    return function (id, attempt) {
      if (weak.has(id)) return 'wrong';
      if (shaky.has(id)) return attempt === 1 ? 'wrong' : 'correct';
      return 'correct';
    };
  }

  function runDemo(steps) {
    let n = 0;
    while (n < steps) {
      const item = E.nextItem(D.graph, session);
      if (!item) break;
      session = E.applyAnswer(D.graph, session, item.topicId, demo.oracle(item.topicId, item.attempt));
      n++;
    }
  }

  /* ------------------------------------------------------------ Render entry point */
  function render() {
    if (!session) return renderStart();
    const item = E.nextItem(D.graph, session);
    if (item) renderQuestion(item); else renderResult();
  }

  /* ------------------------------------------------------------ Start page */
  function stageButton(value, label) {
    return h('button', {
      type: 'button',
      class: 'stage-tab' + (startStage === value ? ' on' : ''),
      role: 'tab',
      'aria-selected': startStage === value ? 'true' : 'false',
      onclick: function () { startStage = value; renderStart(); }
    }, label);
  }

  function renderStart(errMsg) {
    const page = h('div');
    const saved = lsGet(sessionKey());
    if (saved && saved.targets && D.graph.byId[saved.targets[0]]) {
      page.append(h('div', { class: 'banner' },
        h('b', { text: 'An unfinished diagnostic was found:' }), displayScopeLabel(saved.label) || saved.targets.map(nameOf).join(', '),
        ' (' + (saved.answers || []).length + ' answered) ',
        h('button', { class: 'primary', onclick: function () { if (restoreSession(saved)) render(); else { lsDel(sessionKey()); renderStart('The saved session could not be restored and was cleared.'); } } }, 'Resume'),
        ' ', h('button', { onclick: function () { lsDel(sessionKey()); renderStart(); } }, 'Discard')));
    }
    if (errMsg) page.append(h('p', { class: 'err', text: errMsg }));
    page.append(childBar('start'));

    const st = getSettings();
    const limitInput = h('input', { type: 'number', min: LIMIT_MIN, max: LIMIT_MAX, step: 1, value: String(st.limit), id: 'limit-input', 'aria-label': 'Question limit' });
    limitInput.addEventListener('change', function () {
      let v = parseInt(limitInput.value, 10);
      if (!(v >= LIMIT_MIN)) v = LIMIT_MIN;
      if (v > LIMIT_MAX) v = LIMIT_MAX;
      limitInput.value = String(v);
      setSetting('limit', v);
    });
    const confirmSelect = h('select', { id: 'confirm-select', 'aria-label': 'Confirmation questions per topic' },
      E.CONFIRM_CHOICES.map(function (n) {
        return h('option', { value: String(n), selected: st.confirm === n }, String(n) + ' questions');
      }));
    confirmSelect.addEventListener('change', function () {
      const v = E.clampConfirm(confirmSelect.value);
      setSetting('confirm', v);
      renderStart();
    });
    const listBox = h('div', { id: 'target-list' });
    const browser = h('details', { class: 'chapter-browser', id: 'chapter-browser', open: chapterOpen || !!startQuery },
      h('summary', null, 'Browse by Volume and Chapter'),
      h('p', { class: 'muted small', text: 'Topics are grouped by grade, volume, and chapter. To start right away, use the search above.' }),
      listBox);
    browser.addEventListener('toggle', function () { chapterOpen = browser.open; });
    const confirmHelp = 'Answer ' + st.confirm + ' questions about a topic correctly in a row to master it (choose 2, 3, or 5 below; fewer questions in the bank take precedence). After a miss, another question at the same or an easier level confirms the result: another miss marks the topic weak and traces its prerequisites; a correct answer marks it for review.';
    page.append(h('div', { class: 'card' },
      h('h1', { text: 'Choose a Diagnostic Target' }),
      h('p', { class: 'muted' }, subject === 'physics'
        ? 'Choose a physics topic to learn or assess. ' + confirmHelp
        : subject === 'english'
        ? 'Choose an English topic to learn or assess. ' + confirmHelp
        : subject === 'chinese'
        ? 'Choose a Chinese topic to learn or assess. ' + confirmHelp
        : 'Choose a topic to learn or assess. ' + confirmHelp),
      h('div', { class: 'stage-tabs', role: 'tablist', 'aria-label': 'School level' },
        subject === 'physics' ? [stageButton('', 'All'), stageButton('j', 'Middle School'), stageButton('h', 'High School')]
          : subject === 'chinese' ? [stageButton('', 'All'), stageButton('p', 'Elementary')]
          : [stageButton('', 'All'), stageButton('p', 'Elementary'), stageButton('j', 'Middle School'), stageButton('h', 'High School')]),
      h('input', {
        type: 'search', class: 'search-lg', id: 'search',
        placeholder: subject === 'physics' ? "Search topics, e.g. Ohm's law, buoyancy, Newton's second law, Lenz's law" : subject === 'english' ? 'Search topics, e.g. present continuous, subjunctive mood, there is' : subject === 'chinese' ? 'Search topics, e.g. initial consonants, classical poetry, Chinese particles' : 'Search topics, e.g. completing the square, addition within 20, linear functions',
        value: startQuery, autocomplete: 'off', 'aria-label': 'Search topics',
        oninput: function (e) {
          startQuery = e.target.value;
          fillList(listBox);
          if (startQuery.trim()) { browser.open = true; chapterOpen = true; }
        }
      }),
      h('p', { class: 'muted small', id: 'match-count' }),
      h('div', { class: 'row' },
        h('label', null, 'Question limit per topic or chapter (' + LIMIT_MIN + '–' + LIMIT_MAX + ')', limitInput),
        h('label', null, 'Confirmation questions per topic', confirmSelect),
        h('span', { class: 'muted small' }, 'Answer this many questions correctly in a row to be marked as mastered. A miss triggers a confirmation question. Topics not assessed before the limit are marked “Not Tested.”'))));
    page.append(gradeCard());
    page.append(h('div', { class: 'card' }, browser));
    page.append(h('p', { class: 'muted small' },
      'Topics available for diagnostics: ' + D.topics.length + '. Progress and questions already shown are stored only in this browser.'));
    show(page);
    fillList(listBox);
    if (startQuery) { const el = document.getElementById('search'); if (el) el.focus(); }
  }

  function seniorGrade(sel) {
    return sel === '高一' || sel === '高二' || String(sel).indexOf('选必') === 0 || String(sel).indexOf('必修') === 0;
  }
  function seniorRangeLabel(sel) { return String(sel).indexOf('选必') === 0 ? 'Full Volume' : 'Full Required Volume'; }
  function gradeScope() {
    if (seniorGrade(gradeSel)) return gradeSel;
    if (subject === 'physics' && gradeSel === '九') return '九全';
    if (subject === 'english' && gradeSel === '九') return volSel === '上' ? '九上' : (volSel === '全' ? '九全' : '九年级');
    return gradeSel + (volSel ? volSel : '年级');
  }

  function gradeCard() {
    const box = h('div', { class: 'card', id: 'grade-card' });
    const fill = function () {
      while (box.firstChild) box.removeChild(box.firstChild);
      const g = E.gradeTargets(D.graph, gradeScope(), subject);
      const tabs = function (label, items, current, set) {
        return h('div', { class: 'stage-tabs', role: 'tablist', 'aria-label': label }, items.map(function (it) {
          return h('button', {
            type: 'button', class: 'stage-tab' + (current === it[0] ? ' on' : ''), role: 'tab',
            'aria-selected': current === it[0] ? 'true' : 'false', 'data-value': it[0],
            onclick: function () { set(it[0]); fill(); }
          }, it[1]);
        }));
      };
      const limitInput = h('input', {
        type: 'number', min: SCREEN_MIN, max: SCREEN_MAX, step: 1, value: String(getSettings().screenLimit), id: 'screen-limit-input', 'aria-label': 'Full-grade screening question limit'
      });
      limitInput.addEventListener('change', function () {
        let v = parseInt(limitInput.value, 10);
        if (!(v >= SCREEN_MIN)) v = SCREEN_MIN;
        if (v > SCREEN_MAX) v = SCREEN_MAX;
        limitInput.value = String(v);
        setSetting('screenLimit', v);
      });
      box.append(
        h('h2', { text: 'Full-Grade Screening' }),
        h('p', { class: 'muted' }, 'This screening checks mastery of topics at the selected grade; it is not an advanced or competition test. Questions progress from intermediate to advanced, then move to foundational questions after a miss. A topic is mastered after ' + getSettings().confirm + ' consecutive correct answers (change this above). Results include a chapter-by-chapter summary of learning gaps. Use it for an early-term check-in or end-of-term review.'),
        tabs('Grade', subject === 'physics'
          ? [['八', 'Grade 8'], ['九', 'Grade 9'], ['必修一', 'Required 1'], ['必修二', 'Required 2'], ['必修三', 'Required 3'],
            ['选必一', 'Selective 1'], ['选必二', 'Selective 2'], ['选必三', 'Selective 3']]
          : subject === 'english'
          ? '三四五六七八九'.split('').map(function (x) { return [x, displayGrade(x)]; }).concat([
            ['必修一', 'Required 1'], ['必修二', 'Required 2'], ['必修三', 'Required 3'],
            ['选必一', 'Selective 1'], ['选必二', 'Selective 2'], ['选必三', 'Selective 3'], ['选必四', 'Selective 4']
          ])
          : subject === 'chinese'
          ? '一二三四五六'.split('').map(function (x) { return [x, displayGrade(x)]; })
          : GRADES.map(function (x) { return [x, displayGrade(x)]; }).concat([
            ['高一', 'High School Year 1'], ['高二', 'High School Year 2'], ['选必一', 'Selective 1'], ['选必二', 'Selective 2'], ['选必三', 'Selective 3']
          ]), gradeSel, function (v) {
          gradeSel = v;
          if (seniorGrade(v)) volSel = '';
          else if (subject === 'physics' && v === '九') volSel = '全';
          else if (subject === 'english' && v === '九') volSel = '';
          else if (volSel === '全') volSel = '';
        }),
        h('div', { style: 'margin-top:8px' }),
        seniorGrade(gradeSel)
          ? tabs('Scope', [['', seniorRangeLabel(gradeSel)]], '', function () { volSel = ''; })
          : (subject === 'physics' && gradeSel === '九')
            ? tabs('Scope', [['全', 'Full-Year Volume']], '全', function () { volSel = '全'; })
          : (subject === 'english' && gradeSel === '九')
            ? tabs('Scope', [['', 'Full Grade'], ['上', 'Semester 1 (current edition)'], ['全', 'Full-Year Volume (legacy edition; used until Semester 2 is available)']], volSel, function (v) { volSel = v; })
            : tabs('Scope', [['', 'Full Grade'], ['上', 'Semester 1'], ['下', 'Semester 2']], volSel, function (v) { volSel = v; }),
        h('p', { class: 'muted', id: 'grade-info' }, g ? displayScopeLabel(g.label) + ': ' + g.ids.length + ' topics.' : 'No topics are available in this scope.'),
        h('div', { class: 'row' },
          h('label', null, 'Question limit (' + SCREEN_MIN + '–' + SCREEN_MAX + ')', limitInput),
          h('button', {
            class: 'primary', id: 'btn-grade-start', disabled: !g,
            onclick: function () { if (g) startSession(g.ids, displayScopeLabel(g.label) + ' (Full-grade screening)', null, 'screen'); }
          }, 'Start Full-Grade Screening')),
        h('p', { class: 'muted small' }, 'If there are more topics than questions, remaining topics are marked “Not Tested” when the limit is reached. You can add questions on the results page. Default: ' + E.SCREEN_LIMIT + ' questions.'));
    };
    fill();
    return box;
  }

  function fillList(box) {
    while (box.firstChild) box.removeChild(box.firstChild);
    const q = startQuery.trim().toLowerCase();
    let shown = 0;
    function volumeStage(key) {
      if (key === '高一' || key === '高二' || key.indexOf('选必') === 0 || key.indexOf('必修') === 0) return 'h';
      if ('一二三四五六'.indexOf(key.charAt(0)) >= 0) return 'p';
      return 'j';
    }
    VOLUMES.forEach(function (vv) {
      if (startStage && volumeStage(vv[0]) !== startStage) return;
      const v = D.tree[vv[0]];
      if (!v) return;
      const chapters = [];
      v.chapters.forEach(function (ch) {
        const chHit = q && ch.label.toLowerCase().indexOf(q) >= 0;
        const rows = ch.topics.filter(function (x) {
          if (!q || chHit) return true;
          return (x.t.name + ' ' + x.t.description + ' ' + x.t.chapter).toLowerCase().indexOf(q) >= 0;
        });
        if (rows.length) chapters.push({ ch: ch, rows: rows });
      });
      if (!chapters.length) return;
      const count = chapters.reduce(function (n, c) { return n + c.rows.length; }, 0);
      shown += count;
      const openVol = subject === 'physics' ? '八上' : subject === 'english' ? '三上' : '一上';
      const seniorOpen = subject === 'english' || subject === 'physics' ? '必修一' : '高一';
      const det = h('details', { class: 'vol', open: !!q || (startStage === 'j' ? vv[0] === '七上' : startStage === 'h' ? vv[0] === seniorOpen : vv[0] === openVol) },
        h('summary', null, vv[1] + ' (' + count + ' topics)'));
      chapters.forEach(function (c) {
        const ch = c.ch;
        det.append(h('div', { class: 'chap' },
          h('div', { class: 'chap-head' },
            h('span', { class: 't', text: ch.label }),
            h('button', {
              class: 'primary', title: 'Use all ' + ch.topics.length + ' topics in this chapter as the target',
              onclick: function () { startSession(ch.topics.map(function (x) { return x.t.id; }), displayScopeLabel(ch.volume) + ' ' + ch.label + ' (entire chapter)'); }
            }, 'Use Entire Chapter')),
          c.rows.map(function (x) {
            return h('div', { class: 'topic-row', title: x.t.description },
              h('span', { class: 'nm', text: x.t.name }),
              h('span', { class: 'sec', text: x.section }),
              h('button', { onclick: function () { startSession([x.t.id], x.t.name); } }, 'Select as Target'));
          })));
      });
      box.append(det);
    });
    if (!shown) box.append(h('p', { class: 'muted', text: 'No matching topics found.' }));
    const mc = document.getElementById('match-count');
    if (mc) mc.textContent = q ? 'Found ' + shown + ' topics' : shown + ' topics in the chapter list';
    const browser = document.getElementById('chapter-browser');
    if (browser && q) browser.open = true;
  }

  /* ------------------------------------------------------------ Question page */
  function targetMinGrade() {
    let m = Infinity;
    (session.targets || []).forEach(function (tid) {
      const x = D.graph.byId[tid];
      if (x && typeof x.grade === 'number' && x.grade < m) m = x.grade;
    });
    return m;
  }
  function isPrereqKnowledge(id) {
    const t = D.graph.byId[id];
    if (!t || !session || (session.targets || []).indexOf(id) >= 0) return false;
    return typeof t.grade === 'number' && t.grade < targetMinGrade();
  }
  function reasonFor(item) {
    const id = item.topicId;
    const need = E.needConfirm(D.graph, session, id);
    const prev = session.attempts[id] || [];
    const hadFail = prev.some(function (a) { return a.result !== 'correct'; });
    const diff = item.question && item.question.difficulty;
    if (isPrereqKnowledge(id)) {
      return 'This is a prerequisite from an earlier grade. Review it because a related topic at the selected grade has not been mastered yet.';
    }
    if (hadFail) return 'A previous answer was incorrect. Try another ' + (diff === 'basic' ? 'foundational' : 'same-level or easier') + ' question to confirm: another miss marks this topic weak; a correct answer marks it for review.';
    if (item.attempt > 1) {
      if (diff === 'challenge' || diff === 'advanced') {
        return 'The previous answer was correct. This advanced question confirms mastery (' + item.attempt + ' of ' + need + ' consecutive correct answers required).';
      }
      return 'Answer ' + need + ' questions about this topic correctly in a row to master it (question ' + item.attempt + ').';
    }
    for (let i = session.answers.length - 1; i >= 0; i--) {
      const a = session.answers[i];
      if (a.result === 'correct') continue;
      const p = D.graph.prereqs[a.id].find(function (x) { return x.id === id; });
      if (p && E.statusOf(session, a.id) === 'weak') return 'Because "' + nameOf(a.id) + '" was still not passed after confirmation, this checks one of its ' + (p.strength === 'hard' ? 'hard' : 'soft') + ' prerequisites.';
    }
    if (session.mode === 'screen') return 'Full-grade screening assesses topics near the end of each chapter first. Questions progress from intermediate to advanced; after a miss, foundational questions come next.';
    if (session.targets.length > 1) return 'This topic is part of the selected chapter. Topics nearest the end of a chapter are assessed first; mastering one can skip its prerequisites.';
    return session.targets.indexOf(id) >= 0 ? 'This is your selected target. Start here (' + need + ' consecutive correct answers are required for mastery).' : 'This checks a prerequisite of the target.';
  }

  function judgeAndGo(item) {
    const q = item.question;
    const val = ui.answer.trim();
    if (!val) { const el = document.getElementById('ans'); if (el) el.focus(); return; }
    const r = E.judgeQuestion(q, val);
    ui.verdict = r;
    ui.phase = r.verdict === 'manual' ? 'self' : 'auto';
    renderQuestion(item);
  }

  function answerText(q) {
    if (q.type === 'choice') {
      const c = (q.choices || []).find(function (x) { return x.key === q.answer; });
      return q.answer + (c ? '. ' + c.text : '');
    }
    return q.answer;
  }

  function feedbackBlock(q) {
    return h('div', { class: 'feedback' },
      h('div', { class: 'refans' }, h('b', null, 'Reference Answer: '), answerText(q)),
      q.explanation ? h('div', { class: 'explain', id: 'explain' }, h('b', null, 'Explanation: '), q.explanation) : null);
  }

  function renderQuestion(item) {
    const id = item.topicId;
    const q = item.question;
    const t = D.graph.byId[id];
    const key = id + '#' + item.attempt;
    const confirmCount = E.needConfirm(D.graph, session, id);
    const topicProgress = item.attempt > confirmCount
      ? 'Retest question ' + (item.attempt - confirmCount)
      : 'Topic question ' + item.attempt + ' / ' + confirmCount;
    if (ui.key !== key) ui = { key: key, phase: 'ask', answer: '', verdict: null, picked: null };
    const n = session.answers.length;
    const card = h('div', { class: 'card' });
    card.append(
      h('div', { class: 'row' },
        h('span', { class: 'muted' }, 'Target: ' + displayScopeLabel(sessionMeta.label)),
        h('span', { class: 'grow' }),
        h('span', { class: 'muted' }, 'Question ' + (n + 1) + ' / ' + session.limit)),
      h('div', { class: 'progress' }, h('i', { style: 'width:' + Math.round(n / session.limit * 100) + '%' })),
      h('h2', { class: 'q-title' }, t.name, ' ', h('span', { class: 'tag', text: t.chapter })),
      h('div', { class: 'row small', style: 'margin:2px 0' },
        isPrereqKnowledge(id) ? h('span', { class: 'tag ext', text: 'Prerequisite' }) : null,
        h('span', { class: 'tag diff-' + q.difficulty, text: DIFF_LABEL[q.difficulty] || q.difficulty }),
        h('span', { class: 'tag', text: TYPE_LABEL[q.type] || q.type }),
        h('span', { class: 'tag', text: topicProgress })),
      h('div', { class: 'reason', text: reasonFor(item) }),
      h('div', { class: 'q-text', id: 'q-text', text: q.prompt }));
    const stemFig = figureEl(q.figure);
    if (stemFig) {
      const qt = card.querySelector('#q-text');
      if (qt) qt.insertAdjacentElement('afterend', stemFig);
    }

    if (ui.phase === 'ask') {
      if (q.type === 'choice') {
        card.append(h('div', { class: 'choices' + (q.hideChoiceText ? ' fig-icons' : ''), id: 'choices' }, (q.choices || []).map(function (c) {
          const hideName = !!(q.hideChoiceText && c.figure);
          const kids = [h('b', { class: 'choice-key', text: hideName ? c.key : (c.key + '.') })];
          if (!hideName) kids.push(document.createTextNode(' ' + c.text));
          const fig = c.figure ? figureEl(c.figure) : null;
          if (fig) kids.push(fig);
          return h('button', {
            class: 'choice' + (c.figure ? ' fig-choice' : '') + (ui.picked === c.key ? ' picked' : ''),
            id: 'choice-' + c.key, 'data-key': c.key,
            'aria-label': hideName ? ('Option ' + c.key) : null,
            onclick: function () { ui.picked = c.key; ui.answer = c.key; renderQuestion(item); }
          }, kids);
        })));
      } else if (q.type === 'self') {
        card.append(h('textarea', {
          class: 'ans-input', id: 'ans', rows: 3, placeholder: 'Open response: write your reasoning (it is not graded automatically), then select “Show Reference Answer and Self-Assess.”', value: ui.answer,
          oninput: function (e) { ui.answer = e.target.value; }
        }));
      } else {
        card.append(h('input', {
          type: 'text', class: 'ans-input', id: 'ans', autocomplete: 'off', placeholder: 'Enter an answer (use commas or “and” to separate multiple answers).', value: ui.answer,
          oninput: function (e) { ui.answer = e.target.value; },
          onkeydown: function (e) { if (e.key === 'Enter' && !e.isComposing) judgeAndGo(item); }
        }));
      }
      card.append(h('div', { class: 'row', style: 'margin-top:10px' },
        q.type === 'self' ? null : h('button', { class: 'primary', id: 'btn-submit', onclick: function () { judgeAndGo(item); } }, 'Submit Answer'),
        q.type === 'choice' ? null : h('button', { id: 'btn-peek', onclick: function () { ui.phase = 'self'; ui.verdict = null; renderQuestion(item); } }, 'Show Reference Answer and Self-Assess'),
        h('button', { id: 'btn-skip', onclick: function () { ui.phase = 'skip'; renderQuestion(item); } }, "I Don't Know")));
    } else if (ui.phase === 'auto') {
      const ok = ui.verdict.verdict === 'correct';
      card.append(
        h('div', { class: 'muted' }, 'Your answer: ' + (q.type === 'choice' ? answerOfKey(q, ui.answer) : ui.answer)),
        h('div', { class: 'verdict ' + (ok ? 'ok' : 'no') }, ok ? 'Automatic result: Correct' : 'Automatic result: Incorrect'),
        feedbackBlock(q),
        h('div', { class: 'row' },
          h('button', { class: 'primary', id: 'btn-next', onclick: function () { commit(ok ? 'correct' : 'wrong'); } }, 'Next Question'),
          h('button', { id: 'btn-flip', onclick: function () { commit(ok ? 'wrong' : 'correct'); } }, ok ? 'Mark Incorrect — I Was Wrong' : 'Mark Correct — I Was Right'),
          h('button', { onclick: function () { ui.phase = 'ask'; renderQuestion(item); } }, 'Try Again')));
    } else if (ui.phase === 'skip') {
      card.append(
        h('div', { class: 'muted' }, 'You selected “I don’t know.” Review the answer and explanation before continuing:'),
        feedbackBlock(q),
        h('div', { class: 'row' }, h('button', { class: 'primary', id: 'btn-next', onclick: function () { commit('skip'); } }, 'Next Question')));
    } else {
      card.append(
        ui.answer ? h('div', { class: 'muted' }, 'Your answer: ' + ui.answer) : null,
        q.type === 'self' ? h('div', { class: 'muted' }, 'Open response: compare your work with the reference answer and assess it yourself.')
          : (ui.verdict ? h('div', { class: 'muted' }, 'This answer cannot be graded reliably automatically. Compare it with the reference answer and assess it yourself.') : null),
        feedbackBlock(q),
        h('div', { class: 'row' },
          h('button', { class: 'good', id: 'btn-right', onclick: function () { commit('correct'); } }, 'Correct (I got it right)'),
          h('button', { class: 'bad', id: 'btn-wrong', onclick: function () { commit('wrong'); } }, 'Incorrect'),
          h('button', { id: 'btn-skip2', onclick: function () { commit('skip'); } }, "I Don't Know")));
    }

    card.append(h('div', { class: 'notice' }, 'Note: automatic grading is approximate (numbers, fractions, and multiple answers are normalized before comparison). The reference answer is authoritative; you can correct an automatic result.'));
    card.append(h('div', { class: 'row no-print', style: 'margin-top:12px' },
      n > 0 ? h('button', { class: 'small', onclick: function () { rebuild(session.answers.slice(0, -1)); } }, 'Undo Previous Answer') : null,
      h('button', { class: 'small', onclick: function () { if (confirm('Discard this diagnostic and return to the start page?')) restart(); } }, 'Restart')));
    const page = h('div');
    if (demo) page.append(demoBanner());
    const childNotice = childBar('question');
    if (childNotice) page.append(childNotice);
    page.append(card);
    show(page);
    const inp = document.getElementById('ans');
    if (inp && inp.setSelectionRange && inp.tagName === 'INPUT') { inp.focus(); inp.setSelectionRange(inp.value.length, inp.value.length); }
    else if (inp) inp.focus();
  }

  function answerOfKey(q, key) {
    const c = (q.choices || []).find(function (x) { return x.key === key; });
    return c ? c.key + '. ' + c.text : key;
  }

  function demoBanner() {
    return h('div', { class: 'banner demo no-print' }, 'Demo mode: answers are simulated and progress is not saved.',
      h('a', { href: location.pathname }, 'Exit Demo'));
  }

  function onShareKey(e) { if (e.key === 'Escape') closeShare(); }
  function closeShare() {
    shareToken++;
    document.removeEventListener('keydown', onShareKey);
    var modal = document.getElementById('share-modal');
    if (modal) modal.remove();
    document.body.classList.remove('share-open');
    if (shareBlobUrl) { URL.revokeObjectURL(shareBlobUrl); shareBlobUrl = null; }
  }
  function shareScopeText() {
    var raw = sessionMeta && sessionMeta.label ? String(sessionMeta.label) : 'This Diagnostic';
    raw = displayScopeLabel(raw).replace(/\s+/g, ' ').trim();
    return raw || 'This Diagnostic';
  }
  function buildShareModel(sum, chapters) {
    var subjectName = subject === 'english' ? 'English' : subject === 'physics' ? 'Physics' : subject === 'chinese' ? 'Chinese' : 'Math';
    var spots = [];
    var spotKind = 'topic';
    if (chapters && chapters.length) {
      spotKind = 'chapter';
      var hot = chapters.filter(function (c) { return c.weak > 0 || c.shaky > 0; });
      if (!hot.length) hot = chapters.slice(0, 3);
      spots = hot.slice(0, 3).map(function (c) {
        return { title: displayScopeLabel(c.label), detail: 'Weak ' + c.weak + ' · Needs review ' + c.shaky + ' · Not tested ' + c.untested };
      });
    } else {
      var seen = Object.create(null);
      var ids = [];
      var pushId = function (id) {
        if (!id || seen[id] || ids.length >= 3) return;
        seen[id] = true;
        ids.push(id);
      };
      sum.roots.forEach(function (r) { pushId(r.id); });
      sum.weak.forEach(pushId);
      sum.shaky.forEach(pushId);
      spots = ids.map(function (id) {
        return { title: nameOf(id), detail: STATUS_LABEL[E.statusOf(session, id)] || '' };
      });
    }
    var now = new Date();
    return {
      siteName: '12Grades Knowledge Graph',
      subject: subjectName,
      scope: shareScopeText(),
      mastered: sum.mastered.length,
      shaky: sum.shaky.length,
      weak: sum.weak.length,
      untested: sum.untested.length,
      spotKind: spotKind,
      spots: spots,
      roots: sum.roots.slice(0, 2).map(function (r) { return nameOf(r.id); }),
      date: now.toLocaleDateString('en-US')
    };
  }
  function mountShareModal(url) {
    var old = document.getElementById('share-modal');
    if (old) old.remove();
    var img = h('img', { id: 'share-preview', alt: 'Diagnostic results share image', src: url });
    var modal = h('div', {
      id: 'share-modal', class: 'share-modal no-print', role: 'dialog', 'aria-modal': 'true', 'aria-labelledby': 'share-title',
      onclick: function (e) { if (e.target === modal) closeShare(); }
    }, h('div', { class: 'share-panel', onclick: function (e) { e.stopPropagation(); } },
      h('div', { class: 'share-bar' },
        h('h2', { id: 'share-title', text: 'Share Results' }),
        h('button', { type: 'button', id: 'share-close', onclick: closeShare }, 'Close')),
      h('p', { id: 'share-hint', class: 'share-hint', text: 'Press and hold the image to save it.' }),
      h('div', { class: 'share-scroll' }, img),
      h('div', { class: 'share-actions' },
        h('a', { id: 'share-download', class: 'btn btn-primary', href: url, download: 'knowledge-graph-diagnostic-share.png' }, 'Download Image'))));
    document.body.classList.add('share-open');
    document.body.append(modal);
    document.addEventListener('keydown', onShareKey);
  }
  function openShare() {
    if (!window.ShareCard) {
      var host0 = document.getElementById('summary');
      if (host0) host0.append(h('p', { id: 'share-error', class: 'err', text: 'Could not create the share image: the component did not load.' }));
      return;
    }
    var token = ++shareToken;
    var sum = E.summarize(D.graph, session);
    var chapters = session.mode === 'screen' ? E.chapterSummary(D.graph, session) : null;
    var model = buildShareModel(sum, chapters);
    window.__shareModel = model;
    var canvas = document.createElement('canvas');
    try { window.ShareCard.draw(canvas, model); }
    catch (err) {
      var host = document.getElementById('summary');
      if (host) host.append(h('p', { id: 'share-error', class: 'err', text: 'Could not create the share image: ' + (err && err.message ? err.message : err) }));
      return;
    }
    var finish = function (url) {
      if (token !== shareToken) {
        if (String(url).indexOf('blob:') === 0) URL.revokeObjectURL(url);
        return;
      }
      if (shareBlobUrl && shareBlobUrl !== url) URL.revokeObjectURL(shareBlobUrl);
      shareBlobUrl = String(url).indexOf('blob:') === 0 ? url : null;
      mountShareModal(url);
    };
    if (canvas.toBlob) {
      canvas.toBlob(function (blob) {
        if (token !== shareToken) return;
        if (!blob) { finish(canvas.toDataURL('image/png')); return; }
        finish(URL.createObjectURL(blob));
      }, 'image/png');
    } else finish(canvas.toDataURL('image/png'));
  }

  /* ------------------------------------------------------------ Results page */
  function standardsBlock(id) {
    const t = D.graph.byId[id];
    const list = t.standards || [];
    if (!list.length) return h('div', { class: 'muted small', text: t.external ? 'Elementary topic; no standards entry is mapped for this level.' : 'No matching standards entries.' });
    return h('div', null, h('b', null, 'Standards: '), list.map(function (sd) {
      const item = D.stdById[sd.id];
      return h('div', { class: 'std' },
        h('code', { text: sd.id }), h('span', { class: 'conf', text: sd.confidence === 'exact' ? 'Exact match' : 'Inferred match' }),
        h('div', { text: item ? item.text : '(This item was not found in the standards file.)' }),
        sd.note ? h('div', { class: 'muted small', text: 'Note: ' + sd.note }) : null);
    }));
  }

  function topicBody(id, extra) {
    const t = D.graph.byId[id];
    const body = h('div', { class: 'body' });
    body.append(h('div', { class: 'muted' }, (t.external ? 'Elementary prerequisite topic (no diagnostic question)' : displayScopeLabel(t.chapter)) + (t.domain ? ' · ' + displayDomain(t.domain) : '')));
    body.append(h('div', { text: t.description }));
    if (t.mastery_criteria && t.mastery_criteria.length) {
      body.append(h('div', null, h('b', null, 'Mastery Criteria: '), h('ul', null, t.mastery_criteria.map(function (m) { return h('li', { text: m }); }))));
    }
    if (extra) body.append(extra);
    body.append(standardsBlock(id));
    return body;
  }

  function topicItem(id, tags, extra) {
    const t = D.graph.byId[id];
    return h('details', { class: 'topic' },
      h('summary', null, tags, h('span', { text: t.name }), ' ', h('span', { class: 'muted small', text: t.external ? 'Elementary' : displayScopeLabel(t.chapter) })),
      topicBody(id, extra));
  }

  function tag(cls, text) { return h('span', { class: 'tag ' + cls, text: text }); }
  function statusTags(id, rootSet, targetSet) {
    const st = E.statusOf(session, id);
    const out = [];
    if (targetSet.has(id)) out.push(tag('target', 'Target'));
    if (rootSet.has(id)) out.push(tag('root', 'Root cause'));
    if (isPrereqKnowledge(id)) out.push(tag('ext', 'Prerequisite'));
    out.push(tag(st, STATUS_LABEL[st]));
    if (D.graph.byId[id].external) out.push(tag('ext', 'Elementary'));
    return out;
  }

  function renderResult() {
    const sum = E.summarize(D.graph, session);
    const rootSet = new Set(sum.roots.map(function (r) { return r.id; }));
    const screen = session.mode === 'screen';
    const targetSet = new Set(screen ? [] : session.targets);
    const page = h('div');
    if (demo) page.append(demoBanner());
    saveToChild(sum);
    const childNotice = childBar('result');
    if (childNotice) page.append(childNotice);

    const targetsMastered = session.targets.every(function (id) { return E.statusOf(session, id) === 'mastered'; });
    const chapters = screen ? E.chapterSummary(D.graph, session) : null;
    const outOfScope = screen ? sum.roots.filter(function (r) { return r.outOfScopePrereqs.length; }) : [];
    let headline;
    if (screen) {
      if (!sum.weak.length && !sum.shaky.length) headline = sum.untested.length
        ? 'No weak or uncertain topics were found among the topics assessed; ' + sum.untested.length + ' remain untested.'
        : 'All topics in this scope are mastered. No learning gaps were found.';
      else headline = 'Of ' + session.targets.length + ' topics in this scope: ' + sum.weak.length + ' weak, ' + sum.shaky.length + ' needing review, and ' + sum.untested.length +
        ' untested. See the chapter summary below; chapters with more learning gaps appear first.';
    }
    else if (!sum.roots.length && !sum.shaky.length && targetsMastered) headline = 'The target topics are mastered. No prerequisites need attention.';
    else if (!sum.roots.length && !sum.shaky.length) headline = 'No weak topics were identified, but not all targets have been assessed.';
    else if (!sum.roots.length) headline = 'No weak topics were identified, but ' + sum.shaky.length + ' need review (a miss followed by a correct confirmation).';
    else headline = 'Found ' + sum.roots.length + ' foundational gaps' + (sum.shaky.length ? ' and ' + sum.shaky.length + ' topics that need review' : '') + '. Follow the study path below from top to bottom.';

    const more = screen ? 10 : 4;
    const summaryCard = h('div', { class: 'card', id: 'summary' },
      h('h2', { text: 'Diagnostic Results: ' + displayScopeLabel(sessionMeta.label) }),
      h('p', null, headline),
      h('div', { class: 'stats' },
        stat('ask', sum.asked, 'Questions Answered'),
        stat('bad', sum.weak.length, 'Weak'),
        stat('shaky', sum.shaky.length, 'Needs Review'),
        stat('ok', sum.mastered.length, 'Mastered'),
        stat('unk', sum.untested.length, 'Not Tested')),
      sum.unconfirmed.length ? h('p', { class: 'notice' }, sum.unconfirmed.map(nameOf).join(', ') + ' had an incorrect answer but reached the question limit before confirmation; they are temporarily marked weak.') : null,
      sum.limitReached ? h('p', { class: 'notice' }, 'Question limit reached (' + session.limit + '). Remaining topics are marked “Not Tested.” An untested prerequisite may mean that a foundational gap is further upstream.',
        session.limit >= 60 ? null : h('button', { class: 'no-print', style: 'margin-left:8px', onclick: function () { rebuild(session.answers, Math.min(session.limit + more, 60)); } }, 'Answer ' + Math.min(more, 60 - session.limit) + ' More')) : null,
      h('p', { class: 'muted small' }, 'Automatic grading is approximate; you can correct any answer in the session history. Generated: ' + new Date().toLocaleString('en-US')),
      h('div', { class: 'row no-print' },
        h('button', { class: 'primary', id: 'btn-share', onclick: openShare }, 'Create Share Image'),
        h('button', { id: 'btn-export', onclick: exportJson }, 'Export JSON'),
        h('button', { id: 'btn-print', onclick: printPage }, 'Print / Save as PDF'),
        h('button', { onclick: function () { if (confirm('Restarting will clear your current progress. Continue?')) restart(); } }, 'Restart'),
        session.answers.length ? h('button', { onclick: function () { rebuild(session.answers.slice(0, -1)); } }, 'Undo Previous Answer') : null));
    page.append(summaryCard);
    if (screen) page.append(chaptersCard(chapters, outOfScope));

    page.append(h('div', { class: 'card', id: 'roots' },
      h('h2', { text: 'Weak Prerequisites (Root Causes)' }),
      h('p', { class: 'muted small' }, 'A root cause is a weak topic whose direct prerequisites are not weak. Expand a topic to see its description, mastery criteria, and curriculum standards.'),
      sum.roots.length ? sum.roots.map(function (r) {
        const notes = h('div');
        if (r.pendingPrereqs.length) notes.append(h('div', { class: 'notice', text: 'These prerequisites (' + r.pendingPrereqs.map(nameOf).join(', ') + ') were not assessed because the question limit was reached; the actual root cause may be further upstream.' }));
        if (r.outOfScopePrereqs.length) notes.append(h('div', { class: 'notice', text: 'These prerequisites (' + r.outOfScopePrereqs.map(nameOf).join(', ') + ') are outside the selected scope and were not assessed.' }));
        if (r.externalPrereqs.length) notes.append(h('div', { class: 'muted small', text: 'Elementary prerequisites (no diagnostic questions; not assessed): ' + r.externalPrereqs.map(nameOf).join(', ') }));
        return topicItem(r.id, statusTags(r.id, rootSet, targetSet), notes);
      }) : h('p', { text: targetsMastered ? 'None.' : 'None found yet.' })));

    page.append(h('div', { class: 'card', id: 'shaky' },
      h('h2', { text: 'Topics Needing Review (' + sum.shaky.length + ')' }),
      h('p', { class: 'muted small' }, 'These topics had a miss followed by a correct confirmation. This may indicate a careless mistake or uncertain mastery. They appear in the study path for reinforcement, but the diagnostic does not trace their prerequisites unless the confirmation answer is also incorrect.'),
      sum.shaky.length ? sum.shaky.map(function (id) { return topicItem(id, statusTags(id, rootSet, targetSet)); }) : h('p', { text: 'None.' })));

    page.append(h('div', { class: 'card', id: 'path' },
      h('h2', { text: 'Recommended Study Path' }),
      h('p', { class: 'muted small' }, 'Topics between root causes (and topics needing review) and the target that are not yet mastered, ordered from earlier to later grades with prerequisites first. Work from top to bottom. Topics marked “Needs Review” or “Not Tested” are included for reinforcement or self-checking.'),
      sum.path.length ? h('ol', { class: 'path' }, sum.path.map(function (p) {
        return h('li', null, topicItem(p.id, statusTags(p.id, rootSet, targetSet)));
      })) : h('p', { text: 'No additional study is needed.' })));

    page.append(h('div', { class: 'card', id: 'graph' },
      h('h2', { text: 'Study Path Graph' }),
      h('p', { class: 'muted small' }, 'Elementary, middle, and high school topics use different colors. Hard prerequisites use solid lines; soft prerequisites use dashed lines; dotted lines indicate omitted intermediate topics. Red outlines mark root causes, and orange outlines mark targets. Large graphs collapse intermediate topics by grade; expand them as needed. Long names are shortened; hover or tap to see the full name. Use the wheel to zoom and drag to pan. The list above shows the complete study sequence.'),
      h('div', { class: 'path-tools no-print' },
        h('button', { type: 'button', id: 'path-zoom-out', onclick: function () { pathZoom(0.8); } }, 'Zoom Out'),
        h('button', { type: 'button', id: 'path-zoom-in', onclick: function () { pathZoom(1.25); } }, 'Zoom In'),
        h('button', { type: 'button', id: 'path-fit', onclick: pathFit }, 'Fit Graph')),
      h('p', { id: 'path-fold', class: 'graph-fold no-print', hidden: true }),
      h('ul', { class: 'legend' },
        h('li', null, h('i', { class: 'swatch sw-p' }), 'Elementary'),
        h('li', null, h('i', { class: 'swatch sw-j' }), 'Middle School'),
        h('li', null, h('i', { class: 'swatch sw-h' }), 'High School'),
        h('li', null, h('i', { class: 'swatch sw-root' }), 'Weak root cause'),
        h('li', null, h('i', { class: 'swatch sw-target' }), 'Target'),
        h('li', null, h('i', { class: 'swatch line-hard' }), 'Hard prerequisite (solid line)'),
        h('li', null, h('i', { class: 'swatch line-soft' }), 'Soft prerequisite (dashed line)'),
        h('li', null, h('i', { class: 'swatch line-skip' }), 'Omitted intermediate topic (dotted line)')),
      h('div', { class: 'path-graph' },
        h('div', { id: 'path-cy', role: 'img', 'aria-label': 'Prerequisite study path graph' }),
        h('div', { id: 'node-tip', class: 'node-tip', role: 'tooltip', hidden: true }))));

    page.append(h('details', { class: 'card', id: 'mastered' },
      h('summary', null, h('b', null, 'Mastered Topics (' + sum.mastered.length + ')')),
      sum.mastered.map(function (id) {
        const src = session.status[id].src === 'direct' ? 'Answered correctly' : 'Inferred from a later topic';
        return topicItem(id, [tag('mastered', src)].concat(D.graph.byId[id].external ? [tag('ext', 'Elementary')] : []));
      })));

    page.append(h('details', { class: 'card', id: 'untested' },
      h('summary', null, h('b', null, 'Untested Topics (' + sum.untested.length + ')')),
      h('p', { class: 'muted small' }, 'Topics that were not asked because the question limit was reached or no further questions were needed. Elementary topics can also be assessed.'),
      sum.untested.map(function (id) { return topicItem(id, statusTags(id, rootSet, targetSet)); })));

    page.append(standardsCard(sum));
    page.append(logCard());
    page.append(h('p', { class: 'iq-line', id: 'iq-line' },
      'Finished the math diagnostic? Try an IQ test next. → ',
      h('a', {
        href: 'https://12grades.gungwang.com/?from=math-result',
        target: '_blank',
        rel: 'noopener',
        text: 'IQ Test for Kids'
      })));
    show(page);
    mountPathGraph(sum);
  }

  function nameList(ids) { return ids.map(nameOf).join(', '); }

  function chaptersCard(chapters, outOfScope) {
    const seg = function (cls, n, total) { return n ? h('i', { class: cls, style: 'width:' + (n / total * 100) + '%' }) : null; };
    return h('div', { class: 'card', id: 'chapters' },
      h('h2', { text: 'Chapter Summary' }),
      h('p', { class: 'muted small' }, 'Topics are summarized by chapter, with chapters containing more weak topics first. Expand a chapter to see the individual topics. Bar segments are ordered: mastered, needs review, weak, not tested.'),
      outOfScope.length ? h('p', { class: 'notice', id: 'out-of-scope' }, 'Some prerequisites of weak topics are outside the selected grade and were not assessed (' + outOfScope.length + ' weak topics affected, including ' +
        outOfScope.slice(0, 3).map(function (r) { return nameOf(r.id); }).join(', ') + '). You can diagnose these topics separately to continue tracing prerequisites.' ) : null,
      chapters.map(function (c) {
        return h('details', { class: 'topic chap-sum', open: c.weak > 0 || c.shaky > 0 },
          h('summary', null,
            h('span', { class: 'chap-name', text: displayScopeLabel(c.label) }),
            h('span', { class: 'chap-counts' },
              tag('mastered', 'Mastered ' + c.mastered), tag('shaky', 'Review ' + c.shaky), tag('weak', 'Weak ' + c.weak), tag('unknown', 'Not tested ' + c.untested)),
            h('span', { class: 'chap-bar', 'aria-hidden': 'true' },
              seg('m', c.mastered, c.total), seg('s', c.shaky, c.total), seg('w', c.weak, c.total), seg('u', c.untested, c.total))),
          h('div', { class: 'body' },
            h('div', { class: 'muted small', text: c.total + ' topics' }),
            c.weakIds.length ? h('div', { class: 'chap-names' }, tag('weak', 'Weak'), nameList(c.weakIds)) : null,
            c.shakyIds.length ? h('div', { class: 'chap-names' }, tag('shaky', 'Needs Review'), nameList(c.shakyIds)) : null,
            !c.weakIds.length && !c.shakyIds.length ? h('div', { class: 'muted small', text: c.untested ? 'No weak or uncertain topics; ' + c.untested + ' remain untested.' : 'No weak or uncertain topics found.' }) : null));
      }));
  }

  function stat(cls, n, label) { return h('div', { class: 'stat ' + cls }, h('b', { text: String(n) }), label); }

  function standardsCard(sum) {
    const ids = new Set(session.mode === 'screen' ? [] : session.targets);
    sum.path.forEach(function (p) { ids.add(p.id); });
    const by = {};
    ids.forEach(function (id) {
      (D.graph.byId[id].standards || []).forEach(function (sd) { (by[sd.id] || (by[sd.id] = [])).push(id); });
    });
    const keys = Object.keys(by).sort();
    return h('div', { class: 'card', id: 'standards' },
      h('h2', { text: 'Related Curriculum Standards' }),
      h('p', { class: 'muted small' }, subject === 'physics'
        ? 'Curriculum requirements mapped to target and study-path topics from the Compulsory Education Physics Curriculum Standards (2022 edition, revised 2025) and the General High School Physics Curriculum Standards (2017 edition, revised 2020). IDs match the standards clauses.'
        : subject === 'english'
        ? 'Public paraphrases of requirements mapped to target and study-path topics from the Compulsory Education English Curriculum Standards (2022 edition) and the General High School English Curriculum Standards (2017 edition, revised 2025), covering Levels 1–3 and high-school required and selective courses.'
        : subject === 'chinese'
        ? 'Public paraphrases of the first three stages of the Compulsory Education Chinese Language Arts Curriculum Standards (2022 edition), mapped to target and study-path topics.'
        : 'Curriculum requirements from the Compulsory Education Mathematics Curriculum Standards (2022 edition), covering Stages 1–4 and mapped to target and study-path topics.'),
      keys.length ? keys.map(function (k) {
        const item = D.stdById[k];
        return h('div', { class: 'std' }, h('code', { text: k }),
          h('div', { text: item ? item.text : '' }),
          h('div', { class: 'muted small', text: 'Mapped topics: ' + by[k].map(nameOf).join(', ') }));
      }) : h('p', { class: 'muted', text: 'None.' }));
  }

  function logCard() {
    const rows = session.answers.map(function (a, i) {
      const q = E.questionById(D.graph, a.qid) || { prompt: '', answer: '' };
      const sel = h('select', {
        onchange: function (e) {
          const next = session.answers.map(function (x, j) { return j === i ? Object.assign({}, x, { result: e.target.value }) : x; });
          rebuild(next);
        }
      }, ['correct', 'wrong', 'skip'].map(function (r) { return h('option', { value: r, selected: r === a.result }, RESULT_LABEL[r]); }));
      return h('tr', null, h('td', { text: String(i + 1) }),
        h('td', null, nameOf(a.id), h('div', { class: 'muted small', text: q.prompt.length > 60 ? q.prompt.slice(0, 59) + '…' : q.prompt })),
        h('td', { class: 'muted', text: a.text || '' }),
        h('td', null, sel), h('td', { class: 'muted', text: q.answer }));
    });
    return h('div', { class: 'card', id: 'log' },
      h('h2', { text: 'Answer History (Editable)' }),
      h('p', { class: 'muted small' }, 'Automatic grading may be incorrect. Changing a result here recalculates the entire diagnostic, including whether follow-up questions are needed.'),
      session.answers.length ? h('table', { class: 'log' },
        h('thead', null, h('tr', null, h('th', { text: '#' }), h('th', { text: 'Topic / Question' }), h('th', { text: 'Your Answer' }), h('th', { text: 'Result' }), h('th', { text: 'Reference Answer' }))),
        h('tbody', null, rows)) : h('p', { class: 'muted', text: 'No answers yet.' }));
  }

  /* ------------------------------------------------------------ Study path graph (Cytoscape + dagre) */
  function stageKind(grade) { return grade <= 6 ? 'primary' : grade <= 9 ? 'junior' : 'senior'; }
  function gradeWord(grade) {
    if (grade >= 1 && grade <= 9) return 'Grade ' + grade;
    if (subject === 'english') {
      const english = { 10: 'Required 1', 11: 'Required 2', 12: 'Required 3', 13: 'Selective 1', 14: 'Selective 2', 15: 'Selective 3', 16: 'Selective 4' };
      return english[grade] || ('Volume ' + grade);
    }
    if (subject === 'physics') {
      const physics = { 10: 'Required 1', 11: 'Required 2', 12: 'Required 3', 13: 'Selective 1', 14: 'Selective 2', 15: 'Selective 3' };
      return physics[grade] || ('Volume ' + grade);
    }
    const math = { 10: 'High School Year 1', 11: 'High School Year 2', 12: 'Selective 1', 13: 'Selective 2', 14: 'Selective 3' };
    return math[grade] || ('Grade ' + grade);
  }
  function toneOf(kind, colors) {
    if (kind === 'primary') return [colors.primaryBg, colors.primary];
    if (kind === 'junior') return [colors.juniorBg, colors.junior];
    return [colors.seniorBg, colors.senior];
  }
  function pathNodeElement(n, colors) {
    const topic = D.graph.byId[n.id];
    const grade = topic && typeof topic.grade === 'number' ? topic.grade : 7;
    const kind = stageKind(grade);
    const name = nameOf(n.id);
    const bits = [name];
    if (n.isRoot) bits.push('Weak root cause');
    if (n.isTarget) bits.push('Target');
    bits.push(STATUS_LABEL[n.status] || n.status);
    const tone = toneOf(kind, colors);
    let bg = tone[0];
    let border = tone[1];
    if (n.isTarget) { bg = colors.currentBg; border = colors.currentBorder; }
    if (n.isRoot) { bg = colors.badBg; border = colors.bad; }
    const classes = [kind];
    if (n.isRoot) classes.push('root');
    if (n.isTarget) classes.push('target', 'current');
    return {
      data: { id: n.id, name: name, full: bits.join(' · '), label: clipLabel(name), bg: bg, border: border, color: colors.text },
      classes: classes.join(' ')
    };
  }
  function buildPathElements(lay, colors, folded) {
    const elements = [];
    const bucket = new Map();
    const gradeMembers = new Map();
    lay.nodes.forEach(function (n) {
      if (!folded || n.isRoot || n.isTarget) {
        bucket.set(n.id, n.id);
        elements.push(pathNodeElement(n, colors));
        return;
      }
      const topic = D.graph.byId[n.id];
      const grade = topic && typeof topic.grade === 'number' ? topic.grade : 0;
      if (!gradeMembers.has(grade)) gradeMembers.set(grade, []);
      gradeMembers.get(grade).push(n.id);
    });
    gradeMembers.forEach(function (ids, grade) {
      const id = 'grade-' + grade;
      const kind = stageKind(grade);
      const tone = toneOf(kind, colors);
      const name = gradeWord(grade) + ' · ' + ids.length;
      elements.push({
        data: {
          id: id, name: name, full: gradeWord(grade) + ' · ' + ids.length + ' topics',
          label: clipLabel(name), bg: tone[0], border: tone[1], color: colors.text
        },
        classes: kind + ' grade'
      });
      ids.forEach(function (topicId) { bucket.set(topicId, id); });
    });
    const seen = new Map();
    lay.edges.forEach(function (e) {
      const a = bucket.get(e.from);
      const b = bucket.get(e.to);
      if (!a || !b || a === b) return;
      const key = a + '>' + b;
      const kind = !e.direct ? 'indirect' : (e.strength === 'soft' ? 'soft' : 'hard');
      const rank = kind === 'hard' ? 3 : kind === 'soft' ? 2 : 1;
      const prev = seen.get(key);
      if (!prev || rank > prev.rank) seen.set(key, { kind: kind, rank: rank });
    });
    let edgeIndex = 0;
    seen.forEach(function (info, key) {
      const parts = key.split('>');
      const color = info.kind === 'hard' ? colors.edge : colors.edgeSoft;
      elements.push({
        data: { id: 'e' + (edgeIndex++), source: parts[0], target: parts[1], color: color },
        classes: info.kind
      });
    });
    return elements;
  }
  function updatePathFold(total, folded) {
    const box = document.getElementById('path-fold');
    if (!box) return;
    if (total <= PATH_FOLD_AT) {
      box.hidden = true;
      box.replaceChildren();
      return;
    }
    box.hidden = false;
    if (folded) {
      box.replaceChildren(
        document.createTextNode('Long path collapsed by grade. Root causes and targets remain visible.'),
        h('button', { type: 'button', id: 'btn-path-expand', text: 'Expand All ' + total })
      );
    } else {
      box.replaceChildren(
        document.createTextNode('All ' + total + ' topics are expanded.'),
        h('button', { type: 'button', id: 'btn-path-collapse', text: 'Collapse by Grade' })
      );
    }
  }
  function pathZoom(factor) {
    if (!pathCy) return;
    const rect = pathCy.container().getBoundingClientRect();
    pathCy.zoom({
      level: Math.max(pathCy.minZoom(), Math.min(pathCy.maxZoom(), pathCy.zoom() * factor)),
      renderedPosition: { x: rect.width / 2, y: rect.height / 2 }
    });
  }
  function pathFit() {
    if (!pathCy) return;
    pathCy.resize();
    const many = pathCy.nodes().length > 48;
    if (many) pathCy.minZoom(0.45);
    pathCy.fit(undefined, 28);
    if (many && pathCy.zoom() < 0.45) {
      pathCy.zoom(0.55);
      pathCy.center();
    }
  }
  function hidePathTip() {
    const tip = document.getElementById('node-tip');
    if (tip) tip.hidden = true;
  }
  function showPathTip(node) {
    const tip = document.getElementById('node-tip');
    const stage = document.querySelector('.path-graph');
    if (!tip || !stage || !pathCy || !node || node.empty()) return;
    const text = node.data('full') || node.data('label') || '';
    if (!text) { tip.hidden = true; return; }
    tip.textContent = text;
    tip.hidden = false;
    const stageRect = stage.getBoundingClientRect();
    const cyRect = pathCy.container().getBoundingClientRect();
    const bb = node.renderedBoundingBox({ includeLabels: true });
    const tipW = tip.offsetWidth;
    const tipH = tip.offsetHeight;
    const cx = cyRect.left - stageRect.left + (bb.x1 + bb.x2) / 2;
    const top = cyRect.top - stageRect.top + bb.y1;
    let left = Math.max(8, Math.min(cx - tipW / 2, Math.max(8, stageRect.width - tipW - 8)));
    let y = top - tipH - 8;
    if (y < 4) y = cyRect.top - stageRect.top + bb.y2 + 8;
    if (y + tipH > stageRect.height - 4) y = Math.max(4, stageRect.height - tipH - 4);
    tip.style.left = left + 'px';
    tip.style.top = y + 'px';
  }
  function ensureDagre() {
    if (!window.cytoscape || !window.dagre || !window.cytoscapeDagre) throw new Error('The graph libraries did not load.');
    if (!ensureDagre.ready) { window.cytoscape.use(window.cytoscapeDagre); ensureDagre.ready = true; }
  }
  function mountPathGraph(sum) {
    const token = ++pathToken;
    if (pathCy) { pathCy.destroy(); pathCy = null; window.__pathCy = null; }
    const cyEl = document.getElementById('path-cy');
    if (!cyEl) return;
    cyEl.dataset.ready = '0';
    hidePathTip();
    const lay = E.layout(D.graph, session, sum);
    requestAnimationFrame(function () {
      if (token !== pathToken || !document.body.contains(cyEl)) return;
      try {
        ensureDagre();
        const colors = theme();
        const narrow = labelLimit() <= 8;
        const textMax = narrow ? 104 : 126;
        const boxW = narrow ? 118 : 142;
        const FONT = '"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", "Noto Sans SC", sans-serif';
        const total = lay.nodes.length;
        const folded = total > PATH_FOLD_AT && !pathExpanded;
        const heavy = !folded && total > 48;
        updatePathFold(total, folded);
        cyEl.dataset.mode = folded ? 'grade' : 'full';
        cyEl.dataset.total = String(total);
        const elements = buildPathElements(lay, colors, folded);
        pathCy = window.cytoscape({
          container: cyEl,
          elements: elements,
          minZoom: heavy ? 0.45 : 0.2,
          maxZoom: 2.8,
          boxSelectionEnabled: false,
          autoungrabify: true,
          userPanningEnabled: true,
          userZoomingEnabled: true,
          style: [
            { selector: 'node', style: {
              label: 'data(label)', 'text-wrap': 'ellipsis', 'text-max-width': textMax + 'px',
              'text-overflow-wrap': 'anywhere',
              'text-valign': 'center', 'text-halign': 'center',
              'font-size': 13, 'font-family': FONT, color: 'data(color)',
              'background-color': 'data(bg)', 'border-width': 2, 'border-color': 'data(border)',
              shape: 'round-rectangle', width: boxW, height: 34, padding: 0, 'corner-radius': 8
            } },
            { selector: 'node.current', style: { 'border-width': 4, 'z-index': 8 } },
            { selector: 'node.root', style: {
              'background-color': colors.badBg, 'border-color': colors.bad, 'border-width': 4, 'z-index': 11
            } },
            { selector: 'edge', style: {
              width: 1.6, 'line-color': 'data(color)', 'target-arrow-color': 'data(color)',
              'target-arrow-shape': 'triangle', 'curve-style': heavy ? 'straight' : 'bezier', 'arrow-scale': 0.8, 'line-style': 'solid'
            } },
            { selector: 'edge.soft', style: { 'line-style': 'dashed', width: 1.5 } },
            { selector: 'edge.indirect', style: { 'line-style': 'dotted', width: 1.4 } }
          ]
        });
        window.__pathCy = pathCy;
        pathCy.on('mouseover', 'node', function (event) { showPathTip(event.target); });
        pathCy.on('mouseout', 'node', function () { if (!pathTipLock) hidePathTip(); });
        pathCy.on('tap', 'node', function (event) { pathTipLock = true; showPathTip(event.target); });
        pathCy.on('tap', function (event) {
          if (event.target === pathCy) { pathTipLock = false; hidePathTip(); }
        });
        const layout = pathCy.layout({
          name: 'dagre', rankDir: 'TB',
          rankSep: heavy ? 46 : 64,
          nodeSep: heavy ? 16 : 22,
          edgeSep: heavy ? 8 : 10,
          ranker: heavy ? 'longest-path' : 'network-simplex',
          padding: 16, animate: false, fit: true, nodeDimensionsIncludeLabels: false, spacingFactor: heavy ? 1.02 : 1.05
        });
        layout.one('layoutstop', function () {
          if (token !== pathToken || !pathCy) return;
          requestAnimationFrame(function () {
            if (token !== pathToken || !pathCy) return;
            pathCy.resize();
            pathCy.fit(undefined, heavy ? 20 : 24);
            if (heavy && pathCy.zoom() < 0.7) {
              pathCy.zoom(0.8);
              const focusNode = lay.nodes.find(function (n) { return n.isRoot; }) || lay.nodes.find(function (n) { return n.isTarget; }) || lay.nodes[0];
              const focus = focusNode ? pathCy.getElementById(focusNode.id) : null;
              if (focus && !focus.empty()) pathCy.center(focus);
            }
            cyEl.dataset.ready = '1';
          });
        });
        layout.run();
      } catch (error) {
        cyEl.dataset.ready = 'err';
        cyEl.append(h('p', { class: 'muted', text: 'Could not render the graph: ' + (error && error.message ? error.message : error) }));
      }
    });
  }

  /* ------------------------------------------------------------ Export / print */
  function exportJson() {
    const sum = E.summarize(D.graph, session);
    const stdIds = new Set();
    const brief = function (id) { return { id: id, name: nameOf(id) }; };
    sum.path.concat(session.mode === 'screen' ? [] : session.targets.map(function (id) { return { id: id }; })).forEach(function (p) {
      (D.graph.byId[p.id].standards || []).forEach(function (sd) { stdIds.add(sd.id); });
    });
    const chapters = session.mode === 'screen' ? E.chapterSummary(D.graph, session) : null;
    const out = {
      tool: '12grades/diagnose', version: 2, mode: session.mode || 'target', generatedAt: new Date().toISOString(),
      note: 'Automatic grading is approximate; the reference answer is authoritative.',
      label: displayScopeLabel(sessionMeta.label),
      targets: session.targets.map(brief),
      limit: session.limit, seed: session.seed, asked: sum.asked, finished: sum.finished, limitReached: sum.limitReached,
      answers: session.answers.map(function (a, i) {
        const q = E.questionById(D.graph, a.qid) || {};
        return {
          order: i + 1, topicId: a.id, name: nameOf(a.id), questionId: a.qid, difficulty: q.difficulty, type: q.type,
          prompt: q.prompt, userAnswer: a.text == null ? null : a.text, result: a.result,
          referenceAnswer: q.answer, explanation: q.explanation || ''
        };
      }),
      chapters: chapters ? chapters.map(function (c) {
        return {
          label: c.label, total: c.total, mastered: c.mastered, shaky: c.shaky, weak: c.weak, untested: c.untested,
          weakTopics: c.weakIds.map(brief), shakyTopics: c.shakyIds.map(brief), untestedTopics: c.untestedIds.map(brief)
        };
      }) : undefined,
      weakRoots: sum.roots.map(function (r) {
        return Object.assign(brief(r.id), {
          pendingPrereqs: r.pendingPrereqs, outOfScopePrereqs: r.outOfScopePrereqs, externalPrereqs: r.externalPrereqs,
          masteryCriteria: D.graph.byId[r.id].mastery_criteria || [],
          standards: (D.graph.byId[r.id].standards || []).map(function (sd) { return sd.id; })
        });
      }),
      path: sum.path.map(function (p, i) { return Object.assign({ order: i + 1 }, brief(p.id), { status: p.status, isRoot: p.isRoot, isTarget: p.isTarget }); }),
      weak: sum.weak.map(brief),
      shaky: sum.shaky.map(brief),
      mastered: sum.mastered.map(function (id) { return Object.assign(brief(id), { source: session.status[id].src }); }),
      untested: sum.untested.map(function (id) { return Object.assign(brief(id), { external: !!D.graph.byId[id].external }); }),
      standards: Array.from(stdIds).sort().map(function (k) { return { id: k, text: D.stdById[k] ? D.stdById[k].text : '' }; })
    };
    const blob = new Blob([JSON.stringify(out, null, 2)], { type: 'application/json' });
    const a = h('a', { href: URL.createObjectURL(blob), download: 'diagnosis-' + new Date().toISOString().slice(0, 10) + '.json' });
    document.body.append(a);
    a.click();
    a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
  }

  function printPage() { window.print(); }
  window.addEventListener('beforeprint', function () {
    document.querySelectorAll('details:not([open])').forEach(function (d) { d.setAttribute('open', ''); d.dataset.autoOpen = '1'; });
    if (pathCy) { pathCy.resize(); pathCy.fit(undefined, 20); }
  });
  window.addEventListener('afterprint', function () {
    document.querySelectorAll('details[data-auto-open]').forEach(function (d) { d.removeAttribute('open'); delete d.dataset.autoOpen; });
  });

  /* ------------------------------------------------------------ Startup */
  function resolveTargets(params) {
    const t = params.get('target');
    if (t) {
      const raw = t.split(',').map(function (x) { return x.trim(); }).filter(Boolean);
      const ids = E.resolveTargets(raw, D.aliases);
      const bad = ids.filter(function (id) { return !D.graph.byId[id] || D.graph.byId[id].external; });
      if (bad.length) throw new Error('Invalid topic ID in the URL target parameter: ' + bad.join(', '));
      const aliased = raw.filter(function (id) { return D.aliases[id]; });
      let label = ids.map(nameOf).join(', ');
      if (aliased.length) {
        label = aliased.map(function (id) { return (D.aliases[id].name || id); }).join(', ') + ' (legacy ID mapped to elementary topics)';
        if (ids.length <= 6) label += ': ' + ids.map(nameOf).join(', ');
      }
      return { ids: ids, label: label };
    }
    const c = params.get('chapter');
    if (c) {
      const hit = [];
      VOLUMES.forEach(function (vv) {
        ((D.tree[vv[0]] || {}).chapters || []).forEach(function (ch) { if (ch.key === c.trim()) hit.push(ch); });
      });
      if (!hit.length) throw new Error('No chapter matches the URL chapter parameter: ' + c + ' (expected a format such as "七上 第一章").');
      return { ids: hit[0].topics.map(function (x) { return x.t.id; }), label: displayScopeLabel(hit[0].volume) + ' ' + hit[0].label + ' (entire chapter)' };
    }
    const grade = (params.get('grade') || '').trim();
    const volume = (params.get('volume') || '').trim();
    if (grade || volume) {
      let scope = volume || grade;
      const seniorUrl = {
        '高一': '高一', '高一必修': '高一', '高二': '高二', '高二必修': '高二',
        '选必一': '选必一', '选择性必修第一册': '选必一',
        '选必二': '选必二', '选择性必修第二册': '选必二',
        '选必三': '选必三', '选择性必修第三册': '选必三',
        '选必四': '选必四', '选择性必修第四册': '选必四',
        '必修一': '必修一', '必修第一册': '必修一',
        '必修二': '必修二', '必修第二册': '必修二',
        '必修三': '必修三', '必修第三册': '必修三'
      };
      if (seniorUrl[grade]) {
        if (volume && volume !== '必修' && volume !== '整册' && volume !== '必修整册') {
          throw new Error(subject === 'english'
            ? 'High-school English uses full volumes rather than semesters: ' + grade + ' / ' + volume + ' (use grade=必修一 or grade=选必一).'
            : subject === 'physics'
            ? 'High-school physics uses full volumes rather than semesters: ' + grade + ' / ' + volume + ' (use grade=必修一 or grade=选必一).'
            : 'High-school math uses full volumes rather than semesters: ' + grade + ' / ' + volume + ' (use grade=高一, grade=高二, or grade=选必二).');
        }
        scope = seniorUrl[grade];
      } else if (grade && volume) {
        const gch = /^[一二三四五六七八九]$/.test(grade) ? grade : grade.charAt(0);
        scope = (volume === '全' || volume === '全一册') ? gch + '全' : (/^[上下]$/.test(volume) ? gch + volume : volume);
        if (scope.charAt(0) !== gch) throw new Error('The URL grade and volume parameters do not match: ' + grade + ' / ' + volume);
      }
      if (/^[一二三四五六七八九]$/.test(scope)) scope += '年级';
      const g = E.gradeTargets(D.graph, scope, subject);
      if (!g) throw new Error('Unrecognized URL grade or volume parameter: ' + (volume || grade) + ' (examples: grade=七年级, volume=七上).');
      return { ids: g.ids, label: displayScopeLabel(g.label) + ' (Full-grade screening)', mode: 'screen' };
    }
    return null;
  }

  async function init() {
    subject = detectSubject();
    applySubjectChrome();
    try { await loadData(); } catch (e) {
      clearRoot();
      root.append(h('div', { class: 'card' }, h('h2', { class: 'err', text: 'Could Not Load Data' }),
        h('p', null, String(e.message || e)),
        h('p', null, 'Run ', h('code', { text: 'python3 -m http.server 8000' }), ' from the project root, then open http://localhost:8000/diagnose/ in a browser (do not open it directly with file://).')));
      return;
    }
    const params = new URLSearchParams(location.search);
    let resolved = null;
    try { resolved = resolveTargets(params); } catch (e) { renderStart(e.message); return; }
    if (params.get('seed')) seedParam = params.get('seed');
    const paramLimit = parseInt(params.get('limit'), 10);
    const limit = paramLimit > 0 ? paramLimit : undefined;
    if (resolved && params.get('demo')) {
      demo = { oracle: makeOracle(resolved.ids, resolved.mode) };
      session = E.createSession(D.graph, resolved.ids, {
        mode: resolved.mode, limit: limit || (resolved.mode === 'screen' ? getSettings().screenLimit : getSettings().limit),
        confirm: getSettings().confirm, seed: seedParam == null ? 'demo' : seedParam
      });
      sessionMeta = { label: resolved.label };
      const step = parseInt(params.get('step'), 10);
      runDemo(step >= 0 ? step : Infinity);
      render();
      return;
    }
    if (resolved) {
      const saved = lsGet(sessionKey());
      const same = saved && JSON.stringify(saved.targets) === JSON.stringify(Array.from(new Set(resolved.ids))) &&
        (saved.mode || 'target') === (resolved.mode || 'target') && (seedParam == null || saved.seed === seedParam);
      if (same && restoreSession(saved)) { render(); return; }
      startSession(resolved.ids, resolved.label, limit, resolved.mode);
      return;
    }
    renderStart();
  }

  document.addEventListener('click', function (event) {
    const origin = event.target && event.target.closest ? event.target : (event.target && event.target.parentElement);
    if (!origin || !origin.closest) return;
    if (!origin.closest('#btn-path-expand') && !origin.closest('#btn-path-collapse')) return;
    pathExpanded = !!origin.closest('#btn-path-expand');
    if (session && D) mountPathGraph(E.summarize(D.graph, session));
  });

  if (window.matchMedia) {
    const scheme = window.matchMedia('(prefers-color-scheme: dark)');
    const relayout = function () {
      if (!session || !document.getElementById('path-cy')) return;
      mountPathGraph(E.summarize(D.graph, session));
    };
    if (scheme.addEventListener) scheme.addEventListener('change', relayout);
    const narrow = window.matchMedia('(max-width: 700px)');
    if (narrow.addEventListener) narrow.addEventListener('change', relayout);
  }

  init();
})();
