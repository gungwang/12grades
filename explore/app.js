/* Knowledge graph explorer: search, filters, and a local prerequisite graph for the selected topic. */
(function () {
  'use strict';

  var FONT = '"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", "Noto Sans SC", sans-serif';
  var GRADE_LABELS = ['', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9'];
  var TYPE_ZH = {
    conceptual: 'Conceptual Understanding', procedural: 'Procedural Skills', reasoning: 'Reasoning and Proof',
    application: 'Application', modeling: 'Mathematical Modeling'
  };
  var DOMAIN_ORDER = ['数与代数', '图形与几何', '统计与概率', '综合与实践'];
  var ZH_DOMAIN_ORDER = ['拼音', '识字写字', '词语', '句子', '阅读理解', '古诗文积累', '习作基础'];
  var DOMAIN_LABELS = {
    '数与代数': 'Numbers and Algebra',
    '图形与几何': 'Geometry and Measurement',
    '统计与概率': 'Statistics and Probability',
    '综合与实践': 'Integrated Practice',
    '拼音': 'Pinyin',
    '识字写字': 'Characters and Writing',
    '词语': 'Vocabulary',
    '句子': 'Sentences',
    '阅读理解': 'Reading Comprehension',
    '古诗文积累': 'Classical Poetry and Prose',
    '习作基础': 'Writing Skills',
    '日常表达': 'Everyday Expressions',
    '词汇': 'Vocabulary',
    '语法': 'Grammar',
    '语音': 'Pronunciation',
    '读写': 'Reading and Writing',
    '物质': 'Matter',
    '能量': 'Energy',
    '跨学科实践': 'Interdisciplinary Practice',
    '运动和相互作用': 'Motion and Interaction'
  };

  var topics = [];
  var deps = [];
  var aliases = {};
  var byId = new Map();
  var indexOf = new Map();
  var pre = new Map();
  var post = new Map();
  var stdById = new Map();
  var mathNames = {};
  var selected = null;
  var currentAlias = null;
  var stage = '';
  var grade = '';
  var domain = '';
  var query = '';
  var aliasHitIds = new Set();
  var subject = 'math';
  var upDepth = 2;
  var ancestorsOpen = false;
  var tipFromTap = false;
  var cy = null;
  var graphToken = 0;
  var dagreReady = false;
  var FOLD_AT = 40;
  var questionsByTopic = new Map();

  function $(id) { return document.getElementById(id); }

  function el(tag, attrs) {
    var node = document.createElement(tag);
    var a = attrs || {};
    Object.keys(a).forEach(function (key) {
      var value = a[key];
      if (value == null || value === false) return;
      if (key === 'class') node.className = value;
      else if (key === 'text') node.textContent = value;
      else node.setAttribute(key, value === true ? '' : String(value));
    });
    for (var i = 2; i < arguments.length; i++) append(node, arguments[i]);
    return node;
  }
  function append(node, child) {
    if (child == null || child === false) return;
    if (Array.isArray(child)) { child.forEach(function (item) { append(node, item); }); return; }
    node.append(child.nodeType ? child : document.createTextNode(String(child)));
  }
  function figureEl(svg) {
    if (typeof svg !== 'string' || svg.indexOf('<svg') !== 0) return null;
    if (/<\s*script|foreignObject|<\s*image\b|https?:\/\//i.test(svg.replace('xmlns="http://www.w3.org/2000/svg"', ''))) return null;
    var wrap = el('div', { class: 'q-figure' });
    wrap.innerHTML = svg;
    var node = wrap.querySelector('svg');
    if (!node) return null;
    node.setAttribute('role', 'img');
    node.setAttribute('aria-hidden', 'true');
    node.setAttribute('focusable', 'false');
    return wrap;
  }
  function sampleFigureNodes(topic) {
    var list = questionsByTopic.get(topic.id) || [];
    var q1 = null;
    for (var i = 0; i < list.length; i++) {
      if (list[i].id === topic.id + '_q1') q1 = list[i];
    }
    if (!q1) return [];
    var nodes = [];
    var stem = q1.figure ? figureEl(q1.figure) : null;
    if (stem) nodes.push(stem);
    var choices = q1.choices || [];
    var anyFig = choices.some(function (c) { return c && c.figure; });
    if (!anyFig) return nodes;
    var box = el('div', { class: 'sample-choices' + (q1.hideChoiceText ? ' fig-icons' : '') });
    choices.forEach(function (c) {
      var hideName = !!(q1.hideChoiceText && c.figure);
      var item = el('div', { class: 'sample-choice' });
      item.append(el('b', { text: hideName ? c.key : (c.key + '.') }));
      if (!hideName) item.append(document.createTextNode(' ' + c.text));
      if (c.figure) {
        var fig = figureEl(c.figure);
        if (fig) item.append(fig);
      }
      box.append(item);
    });
    nodes.push(box);
    return nodes;
  }

  function stageKind(grade) {
    if (grade <= 6) return 'primary';
    if (grade <= 9) return 'junior';
    return 'senior';
  }
  function stageLabel(grade) {
    if (grade <= 6) return 'Elementary School';
    if (grade <= 9) return 'Middle School';
    return 'High School';
  }
  var EN_BOOK = {
    10: ['Required 1', 'Required Volume 1'],
    11: ['Required 2', 'Required Volume 2'],
    12: ['Required 3', 'Required Volume 3'],
    13: ['Selective 1', 'Selective Required Volume 1'],
    14: ['Selective 2', 'Selective Required Volume 2'],
    15: ['Selective 3', 'Selective Required Volume 3'],
    16: ['Selective 4', 'Selective Required Volume 4']
  };
  function gradeWord(grade) {
    if ((subject === 'english' || subject === 'physics') && EN_BOOK[grade]) return EN_BOOK[grade][0];
    if (grade === 10) return 'High School Year 1';
    if (grade === 11) return 'High School Year 2';
    if (grade === 12) return 'Selective 1';
    if (grade === 13) return 'Selective 2';
    if (grade === 14) return 'Selective 3';
    return GRADE_LABELS[grade];
  }
  function gradeLabel(topic) {
    if ((subject === 'english' || subject === 'physics') && EN_BOOK[topic.grade]) return EN_BOOK[topic.grade][1];
    if (topic.grade === 10) return 'High School Year 1 · Required Volume 1';
    if (topic.grade === 11) return 'High School Year 2 · Required Volume 2';
    if (topic.grade === 12) return 'Selective 1 · Selective Required Volume 1';
    if (topic.grade === 13) return 'Selective 2 · Selective Required Volume 2';
    if (topic.grade === 14) return 'Selective 3 · Selective Required Volume 3';
    if (topic.semester === '全') return GRADE_LABELS[topic.grade] + ' · Full-Year Volume';
    return GRADE_LABELS[topic.grade] + ' · ' + (topic.semester === '上' ? 'Semester 1' : 'Semester 2');
  }
  function domainLabel(value) { return DOMAIN_LABELS[value] || value; }
  function displayChapter(value) {
    var text = String(value || '');
    var match = /^([一二三四五六七八九])年级(上册|下册|全一册)(?:\s+|$)/.exec(text);
    if (match) {
      var term = match[2] === '上册' ? 'Semester 1' : match[2] === '下册' ? 'Semester 2' : 'Full-Year Volume';
      var number = { '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9 }[match[1]];
      return 'Grade ' + number + ' · ' + term + text.slice(match[0].length);
    }
    match = /^([一二三四五六七八九])([上下全])(?:\s+|$)/.exec(text);
    if (match) {
      var semester = match[2] === '上' ? 'Semester 1' : match[2] === '下' ? 'Semester 2' : 'Full-Year Volume';
      return 'Grade ' + ({ '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9 }[match[1]]) + ' · ' + semester + text.slice(match[0].length);
    }
    match = /^(必修第([一二三])册|选择性必修第([一二三四])册)(?:\s+|$)/.exec(text);
    if (match) {
      var book = match[2] ? 'Required Volume ' + ({ '一': 1, '二': 2, '三': 3 }[match[2]]) : 'Selective Required Volume ' + ({ '一': 1, '二': 2, '三': 3, '四': 4 }[match[3]]);
      return book + text.slice(match[0].length);
    }
    match = /^(高[一二]|选必[一二三])(?:\s+|$)/.exec(text);
    if (match) {
      var highSchool = { '高一': 'High School Year 1', '高二': 'High School Year 2', '选必一': 'Selective 1', '选必二': 'Selective 2', '选必三': 'Selective 3' }[match[1]];
      return highSchool + text.slice(match[0].length);
    }
    return text;
  }
  function paint(grade, colors) {
    if (grade <= 6) return { bg: colors.primaryBg, border: colors.primary, cls: 'primary' };
    if (grade <= 9) return { bg: colors.juniorBg, border: colors.junior, cls: 'junior' };
    return { bg: colors.seniorBg, border: colors.senior, cls: 'senior' };
  }

  function chapterOf(topic) {
    var text = topic.chapter || 'Unassigned chapter';
    var primary = /^[一二三四五六七八九]年级[上下全]册\s+(.+)$/.exec(text);
    if (primary) return primary[1];
    var enHs = /^(?:必修第[一二三]册|选择性必修第[一二三四]册) ((?:欢迎单元|第\d+单元) .+)$/.exec(text);
    if (enHs) return enHs[1];
    var model = /^(高[一二]|选必[一二三]) (数学建模|数学探究) (\S+)$/.exec(text);
    if (model) return model[2] + ' ' + model[3];
    var junior = /^\S+\s+(第\S+章)\s+(.+)$/.exec(text);
    if (junior) return junior[1] + ' ' + junior[2].replace(/\s+\d+(?:\.\d+)*$/, '');
    return text;
  }

  function readHash() {
    var hash = location.hash.replace(/^#/, '');
    if (!hash) return '';
    try { hash = decodeURIComponent(hash);     } catch (error) { /* Leave the value unchanged. */ }
    return hash;
  }

  function resolveId(raw) {
    if (!raw) return null;
    if (byId.has(raw)) return { id: raw, alias: null };
    var spec = aliases[raw];
    if (spec && Array.isArray(spec.targets) && spec.targets.length && byId.has(spec.targets[0])) {
      return {
        id: spec.targets[0],
        alias: { id: raw, name: spec.name || raw, targets: spec.targets.slice() }
      };
    }
    return null;
  }

  function writeHash(id) {
    if (readHash() === id) return;
    history.replaceState(null, '', location.pathname + location.search + '#' + id);
  }

  function cssVar(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  }
  function theme() {
    return {
      primary: cssVar('--node-primary'),
      primaryBg: cssVar('--node-primary-bg'),
      junior: cssVar('--node-junior'),
      juniorBg: cssVar('--node-junior-bg'),
      senior: cssVar('--node-senior'),
      seniorBg: cssVar('--node-senior-bg'),
      currentBg: cssVar('--node-current-bg'),
      currentBorder: cssVar('--node-current-border'),
      text: cssVar('--node-text'),
      edge: cssVar('--edge'),
      edgeSoft: cssVar('--edge-soft')
    };
  }

  function restoreDepth() {
    try {
      var saved = sessionStorage.getItem('cnmExplore.depth');
      if (saved === '1' || saved === '2' || saved === '3') upDepth = parseInt(saved, 10);
      else if (saved === 'all') upDepth = 'all';
    } catch (error) { /* Private browsing mode. */ }
  }

  function syncControls() {
    document.querySelectorAll('#stage-tabs [data-stage]').forEach(function (button) {
      var on = button.getAttribute('data-stage') === stage;
      button.classList.toggle('on', on);
      button.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    $('fGrade').value = grade;
    var domainSelect = $('fDomain');
    if (Array.prototype.some.call(domainSelect.options, function (option) { return option.value === domain; })) {
      domainSelect.value = domain;
    }
    syncDepthButtons();
  }

  function syncDepthButtons() {
    var current = upDepth === 'all' ? 'all' : String(upDepth);
    document.querySelectorAll('#depth-switch [data-depth]').forEach(function (button) {
      var on = button.getAttribute('data-depth') === current;
      button.classList.toggle('on', on);
      button.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }

  function closeDrawerIfMobile() {
    if (!window.matchMedia('(max-width: 900px)').matches) return;
    $('side').classList.remove('open');
    var toggle = $('list-toggle');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.textContent = 'Topic List';
  }

  function recomputeAliasHits() {
    aliasHitIds = new Set();
    if (query.length < 2) return;
    Object.keys(aliases).forEach(function (id) {
      var spec = aliases[id];
      var name = ((spec && spec.name) || '').toLowerCase();
      if (id.toLowerCase().indexOf(query) >= 0 || name.indexOf(query) >= 0) {
        ((spec && spec.targets) || []).forEach(function (target) { aliasHitIds.add(target); });
      }
    });
  }

  function topicSubject(topic) {
    if (!topic) return 'math';
    if (topic.subject === 'english' || topic.subject === 'physics' || topic.subject === 'chinese') return topic.subject;
    var id = String(topic.id || '');
    if (id.indexOf('cne_') === 0) return 'english';
    if (id.indexOf('cnp_') === 0) return 'physics';
    if (id.indexOf('cnc_') === 0) return 'chinese';
    return 'math';
  }

  function withSubject(href) {
    if (subject === 'math' || !href || href.indexOf('subject=') >= 0 || href.indexOf('http') === 0) return href;
    return href + (href.indexOf('?') >= 0 ? '&' : '?') + 'subject=' + subject;
  }

  function passFilter(topic) {
    if (subject === 'english') {
      if (stage === 'p' && topic.grade > 6) return false;
      if (stage === 'j' && (topic.grade < 7 || topic.grade > 9)) return false;
      if (stage === 'h' && topic.grade < 10) return false;
    } else {
      if (stage === 'p' && topic.grade > 6) return false;
      if (stage === 'j' && (topic.grade < 7 || topic.grade > 9)) return false;
      if (stage === 'h' && topic.grade < 10) return false;
    }
    if (grade && String(topic.grade) !== grade) return false;
    if (domain && topic.domain !== domain) return false;
    if (query) {
      var blob = (topic.name + '\n' + topic.description + '\n' + (topic.chapter || '') + '\n' + topic.id + '\n' + topic.domain).toLowerCase();
      if (blob.indexOf(query) < 0 && !aliasHitIds.has(topic.id)) return false;
    }
    return true;
  }

  function renderList() {
    recomputeAliasHits();
    var volumes = [];
    var volumeMap = new Map();
    topics.forEach(function (topic) {
      if (!passFilter(topic)) return;
      var key = topic.grade + topic.semester;
      var volume = volumeMap.get(key);
      if (!volume) {
        volume = { label: gradeLabel(topic), grade: topic.grade, semester: topic.semester, chapters: [], chapterMap: new Map() };
        volumeMap.set(key, volume);
        volumes.push(volume);
      }
      var chapterKey = chapterOf(topic);
      var chapter = volume.chapterMap.get(chapterKey);
      if (!chapter) {
        chapter = { label: chapterKey, topics: [] };
        volume.chapterMap.set(chapterKey, chapter);
        volume.chapters.push(chapter);
      }
      chapter.topics.push(topic);
    });
    volumes.sort(function (a, b) {
      return a.grade - b.grade || (a.semester === b.semester ? 0 : a.semester === '上' ? -1 : 1);
    });

    var shown = 0;
    var box = $('list');
    box.replaceChildren();
    var filtering = !!(query || grade || stage || domain);
    volumes.forEach(function (volume) {
      var count = volume.chapters.reduce(function (sum, chapter) { return sum + chapter.topics.length; }, 0);
      shown += count;
      var volumeHas = volume.chapters.some(function (chapter) {
        return chapter.topics.some(function (topic) { return topic.id === selected; });
      });
      var details = el('details', { class: 'vol' });
      details.open = filtering || volumeHas;
      details.append(el('summary', null, volume.label, el('span', { class: 'count-pill', text: ' ' + count })));
      volume.chapters.forEach(function (chapter) {
        var chapterHas = chapter.topics.some(function (topic) { return topic.id === selected; });
        var chapterDetails = el('details', { class: 'chap' });
        chapterDetails.open = !!query || chapterHas;
        chapterDetails.append(el('summary', { text: chapter.label }));
        chapter.topics.forEach(function (topic) {
          chapterDetails.append(el('button', {
            type: 'button',
            class: 'topic-item' + (topic.id === selected ? ' sel' : ''),
            'data-jump': topic.id
          }, el('span', { class: 'nm', text: topic.name }), el('span', { class: 'meta', text: topic.domain })));
        });
        details.append(chapterDetails);
      });
      box.append(details);
    });
    if (!shown) box.append(el('p', { class: 'muted', text: 'No matching topics found.', style: 'padding:12px' }));
    $('count').textContent = 'Showing ' + shown + ' / ' + topics.length;
  }

  function sideVisible() {
    var side = $('side');
    return side.offsetParent !== null && side.getBoundingClientRect().height > 0;
  }

  function highlight(scroll) {
    document.querySelectorAll('#list .topic-item').forEach(function (button) {
      var on = button.getAttribute('data-jump') === selected;
      button.classList.toggle('sel', on);
      if (on) button.setAttribute('aria-current', 'true');
      else button.removeAttribute('aria-current');
    });
    var current = document.querySelector('#list .topic-item.sel');
    if (!current) return;
    var parent = current.parentElement;
    while (parent && parent.id !== 'list') {
      if (parent.tagName === 'DETAILS') parent.open = true;
      parent = parent.parentElement;
    }
    if (scroll && sideVisible()) current.scrollIntoView({ block: 'nearest' });
  }

  function countReach(map, id) {
    var seen = new Set();
    var stack = [id];
    while (stack.length) {
      var current = stack.pop();
      (map.get(current) || []).forEach(function (edge) {
        if (!seen.has(edge.id)) { seen.add(edge.id); stack.push(edge.id); }
      });
    }
    return seen.size;
  }

  function badge(strength) {
    var hard = strength === 'hard';
    return el('span', { class: 'badge ' + (hard ? 'hard' : 'soft'), text: hard ? 'Hard prerequisite' : 'Soft prerequisite' });
  }

  function relButton(edge) {
    var other = byId.get(edge.id);
    return el('button', { type: 'button', class: 'rel-row', 'data-jump': edge.id },
      badge(edge.strength),
      el('span', { class: 'rel-name', text: other ? other.name : edge.id }),
      el('span', { class: 'rel-where', text: other ? gradeLabel(other) : '' }),
      edge.reason ? el('span', { class: 'why', text: edge.reason }) : null);
  }

  function metaItem(label, value, wide) {
    return el('div', { class: wide ? 'span-2' : '' }, el('dt', { text: label }), el('dd', { text: value || '—' }));
  }

  function renderDetail() {
    var box = $('detail');
    if (!selected || !byId.has(selected)) {
      box.replaceChildren(el('div', { class: 'detail-empty' },
        el('h1', { text: 'Choose a Topic' }),
        el('p', { text: 'Search or browse by grade, volume, and chapter. Once selected, the graph shows nearby prerequisites and the next layer of topics that depend on it.' })));
      document.title = subject === 'english' ? 'Knowledge Graph · English' : subject === 'physics' ? 'Knowledge Graph · Physics' : subject === 'chinese' ? 'Knowledge Graph · Chinese' : 'Knowledge Graph · 12Grades';
      return;
    }
    var topic = byId.get(selected);
    var kind = stageKind(topic.grade);
    var parts = [];
    if (currentAlias) {
      parts.push(el('div', { class: 'alias-note' },
        'Legacy ID ', el('code', { text: currentAlias.id }),
        ' (“' + (currentAlias.name || 'Unnamed') + '”) maps to this topic. Starting a diagnostic with this ID includes all ' + currentAlias.targets.length + ' mapped elementary topics. ',
        el('a', { href: '../diagnose/?target=' + encodeURIComponent(currentAlias.id) }, 'Diagnose with this legacy ID')));
    }
    parts.push(el('h1', { class: 'detail-title', text: topic.name }));
    parts.push(el('div', { class: 'pills' },
      el('span', { class: 'pill pill-' + (kind === 'primary' ? 'p' : kind === 'junior' ? 'j' : 'h'), text: stageLabel(topic.grade) }),
      el('code', { class: 'id-code', text: topic.id })));
    var diagHref = '../diagnose/?target=' + encodeURIComponent(topic.id);
    if (subject !== 'math') diagHref = '../diagnose/?subject=' + subject + '&target=' + encodeURIComponent(topic.id);
    parts.push(el('a', {
      class: 'btn btn-primary btn-lg diag-btn',
      href: diagHref
    }, 'Diagnose This Topic'));
    parts.push(el('dl', { class: 'meta-grid' },
      metaItem('Grade and Volume', gradeLabel(topic)),
      metaItem('Domain', domainLabel(topic.domain)),
      metaItem('Type', TYPE_ZH[topic.type] || topic.type),
      metaItem('Chapter', displayChapter(topic.chapter), true)));
    if (topic.description) parts.push(el('p', { class: 'desc', text: topic.description }));
    if (topic.root_reason) parts.push(el('p', { class: 'root-reason', text: topic.root_reason }));

    if (topic.mastery_criteria && topic.mastery_criteria.length) {
      parts.push(el('section', null,
        el('h2', { text: 'Mastery Criteria' }),
        el('ul', { class: 'plain' }, topic.mastery_criteria.map(function (item) { return el('li', { text: item }); }))));
    }

    var standards = topic.standards || [];
    var standardNodes = standards.length ? standards.map(function (entry) {
      var item = stdById.get(entry.id);
      return el('div', { class: 'std' },
        el('div', { class: 'std-id' }, el('code', { text: entry.id }), ' · ' + (entry.confidence === 'exact' ? 'Exact match' : 'Inferred match')),
        el('p', { text: item ? item.text : '(This item was not found in the standards file.)' }),
        entry.note ? el('p', { class: 'muted', text: 'Note: ' + entry.note }) : null);
    }) : [el('p', { class: 'muted', text: 'No matching standards entries.' })];
    parts.push(el('section', null, el('h2', { text: 'Standards' }), standardNodes));

    if (topic.mathLinks && topic.mathLinks.length) {
      parts.push(el('section', null,
        el('h2', { text: 'Related Math Topics' }),
        el('p', { class: 'muted', text: 'Physics and math use separate graphs. These math topics are listed for reference, not as prerequisites, and diagnostics will not trace into math.' }),
        el('ul', { class: 'plain' }, topic.mathLinks.map(function (link) {
          return el('li', null,
            el('a', { href: '../explore/#' + encodeURIComponent(link.id) }, mathNames[link.id] || link.id),
            el('span', { class: 'muted', text: ': ' + link.reason }));
        }))));
    }

    if (topic.diagnostic_question && topic.diagnostic_question.question) {
      var answer = el('details', { class: 'ans' });
      answer.append(el('summary', { text: 'Show Answer' }), el('p', { text: topic.diagnostic_question.answer || '' }));
      parts.push(el('section', null,
        el('h2', { text: 'Sample Question' }),
        el('p', { class: 'sample-q', text: topic.diagnostic_question.question }),
        sampleFigureNodes(topic),
        answer));
    }

    var pres = pre.get(topic.id) || [];
    parts.push(el('section', null,
      el('h2', { text: 'Prerequisites' }),
      el('p', { class: 'muted', text: pres.length + ' direct; ' + countReach(pre, topic.id) + ' upstream in total. The graph shows 2 upstream levels by default; when showing all with more than ' + FOLD_AT + ' topics, it collapses by grade.' }),
      pres.length ? pres.map(relButton) : el('p', { text: 'This is a starting point with no earlier prerequisites.' })));

    var posts = post.get(topic.id) || [];
    parts.push(el('section', null,
      el('h2', { text: 'Topics That Depend on This' }),
      el('p', { class: 'muted', text: posts.length + ' direct; ' + countReach(post, topic.id) + ' downstream in total. The graph shows 1 downstream level.' }),
      posts.length ? posts.map(relButton) : el('p', { text: 'No later topics depend on this one yet.' })));

    box.replaceChildren.apply(box, parts);
    document.title = topic.name + ' · Knowledge Graph';
  }

  function upstream(id, depth) {
    var seen = new Set([id]);
    var frontier = [id];
    var limit = depth === Infinity ? 10000 : depth;
    for (var step = 0; step < limit; step++) {
      var next = [];
      frontier.forEach(function (current) {
        (pre.get(current) || []).forEach(function (edge) {
          if (!seen.has(edge.id)) { seen.add(edge.id); next.push(edge.id); }
        });
      });
      if (!next.length) break;
      frontier = next;
    }
    return seen;
  }

  function labelLimit() {
    return window.matchMedia('(max-width: 700px)').matches ? 8 : 10;
  }

  function clipLabel(name) {
    var chars = Array.from(name || '');
    var limit = labelLimit();
    if (chars.length <= limit) return name || '';
    return chars.slice(0, limit - 1).join('') + '…';
  }

  function hideTip() {
    var tip = $('node-tip');
    if (tip) tip.hidden = true;
  }

  function showTip(node) {
    var tip = $('node-tip');
    var stage = $('graph-stage');
    if (!tip || !stage || !cy || !node || node.empty()) return;
    var text = node.data('full') || node.data('label') || '';
    if (!text) { tip.hidden = true; return; }
    tip.textContent = text;
    tip.hidden = false;
    var stageRect = stage.getBoundingClientRect();
    var cyRect = cy.container().getBoundingClientRect();
    var bb = node.renderedBoundingBox({ includeLabels: true });
    var tipW = tip.offsetWidth;
    var tipH = tip.offsetHeight;
    var cx = cyRect.left - stageRect.left + (bb.x1 + bb.x2) / 2;
    var top = cyRect.top - stageRect.top + bb.y1;
    var left = Math.max(8, Math.min(cx - tipW / 2, Math.max(8, stageRect.width - tipW - 8)));
    var y = top - tipH - 8;
    if (y < 4) y = cyRect.top - stageRect.top + bb.y2 + 8;
    if (y + tipH > stageRect.height - 4) y = Math.max(4, stageRect.height - tipH - 4);
    tip.style.left = left + 'px';
    tip.style.top = y + 'px';
  }

  function ensureDagre() {
    if (dagreReady) return;
    if (!window.cytoscape || !window.dagre || !window.cytoscapeDagre) {
      throw new Error('The graph libraries did not load.');
    }
    window.cytoscape.use(window.cytoscapeDagre);
    dagreReady = true;
  }

  function topicElement(id, colors) {
    var topic = byId.get(id);
    var tone = paint(topic.grade, colors);
    var current = id === selected;
    var name = topic.name;
    return {
      data: {
        id: id,
        name: name,
        full: name,
        label: clipLabel(name),
        bg: current ? colors.currentBg : tone.bg,
        border: current ? colors.currentBorder : tone.border,
        color: colors.text
      },
      classes: tone.cls + (current ? ' current' : '')
    };
  }

  function edgeElement(id, source, target, soft, colors) {
    return {
      data: {
        id: id,
        source: source,
        target: target,
        color: soft ? colors.edgeSoft : colors.edge
      },
      classes: soft ? 'soft' : 'hard'
    };
  }

  function updateFold(total, folded) {
    var box = $('graph-fold');
    if (upDepth !== 'all' || total <= FOLD_AT) {
      box.hidden = true;
      box.replaceChildren();
      return;
    }
    box.hidden = false;
    if (folded) {
      box.replaceChildren(
        document.createTextNode('Many ancestors; collapsed by grade.'),
        el('button', { type: 'button', id: 'btn-expand-all', 'data-total': String(total), text: total + ' total · Expand all' })
      );
    } else {
      box.replaceChildren(
        document.createTextNode('All ' + total + ' topics are expanded.'),
        el('button', { type: 'button', id: 'btn-collapse-all', text: 'Collapse by Grade' })
      );
    }
  }

  function buildFoldedElements(nodeSet, colors) {
    var downIds = {};
    (post.get(selected) || []).forEach(function (edge) { downIds[edge.id] = edge.strength; });
    var gradeMembers = new Map();
    nodeSet.forEach(function (id) {
      if (id === selected || downIds[id]) return;
      var grade = byId.get(id).grade;
      if (!gradeMembers.has(grade)) gradeMembers.set(grade, []);
      gradeMembers.get(grade).push(id);
    });
    var gradeOf = new Map();
    var elements = [];
    gradeMembers.forEach(function (ids, grade) {
      var tone = paint(grade, colors);
      var word = gradeWord(grade);
      var name = word + ' · ' + ids.length;
      ids.forEach(function (id) { gradeOf.set(id, grade); });
      elements.push({
        data: {
          id: 'grade-' + grade,
          name: name,
          full: word + ' · ' + ids.length + ' prerequisites',
          label: clipLabel(name),
          bg: tone.bg,
          border: tone.border,
          color: colors.text
        },
        classes: tone.cls + ' grade'
      });
    });
    elements.push(topicElement(selected, colors));
    Object.keys(downIds).forEach(function (id) {
      if (nodeSet.has(id)) elements.push(topicElement(id, colors));
    });
    var between = new Map();
    deps.forEach(function (edge) {
      var fromG = gradeOf.get(edge.prerequisiteId);
      var toG = gradeOf.get(edge.topicId);
      if (fromG == null || toG == null || fromG === toG) return;
      var key = fromG + '>' + toG;
      if (edge.strength !== 'soft') between.set(key, 'hard');
      else if (!between.has(key)) between.set(key, 'soft');
    });
    between.forEach(function (kind, key) {
      var parts = key.split('>');
      elements.push(edgeElement('g-' + parts[0] + '-' + parts[1], 'grade-' + parts[0], 'grade-' + parts[1], kind === 'soft', colors));
    });
    var into = new Map();
    (pre.get(selected) || []).forEach(function (edge) {
      var grade = gradeOf.get(edge.id);
      if (grade == null) return;
      if (edge.strength !== 'soft') into.set(grade, 'hard');
      else if (!into.has(grade)) into.set(grade, 'soft');
    });
    into.forEach(function (kind, grade) {
      elements.push(edgeElement('gs' + grade, 'grade-' + grade, selected, kind === 'soft', colors));
    });
    Object.keys(downIds).forEach(function (id) {
      if (!nodeSet.has(id)) return;
      elements.push(edgeElement('sd-' + id, selected, id, downIds[id] === 'soft', colors));
    });
    return elements;
  }

  function buildFullElements(nodeSet, colors) {
    var elements = [];
    nodeSet.forEach(function (id) { elements.push(topicElement(id, colors)); });
    deps.forEach(function (edge, edgeIndex) {
      if (!nodeSet.has(edge.topicId) || !nodeSet.has(edge.prerequisiteId)) return;
      elements.push(edgeElement('e' + edgeIndex, edge.prerequisiteId, edge.topicId, edge.strength === 'soft', colors));
    });
    return elements;
  }

  function renderGraph() {
    var token = ++graphToken;
    tipFromTap = false;
    hideTip();
    if (cy) { cy.destroy(); cy = null; window.__cy = null; }
    var cyEl = $('cy');
    var emptyEl = $('graph-empty');
    var meta = $('graph-meta');
    if (!selected || !byId.has(selected)) {
      cyEl.hidden = true;
      cyEl.dataset.ready = '0';
      cyEl.dataset.mode = '';
      cyEl.dataset.total = '';
      emptyEl.hidden = false;
      meta.textContent = '';
      updateFold(0, false);
      return;
    }
    var depth = upDepth === 'all' ? Infinity : upDepth;
    var upSet = upstream(selected, depth);
    var nodeSet = new Set(upSet);
    (post.get(selected) || []).forEach(function (edge) { nodeSet.add(edge.id); });
    var total = nodeSet.size;
    var folded = upDepth === 'all' && total > FOLD_AT && !ancestorsOpen;
    var edgeCount = 0;
    if (!folded) {
      deps.forEach(function (edge) {
        if (nodeSet.has(edge.topicId) && nodeSet.has(edge.prerequisiteId)) edgeCount++;
      });
    }
    var depthLabel = upDepth === 'all' ? 'all ancestors' : (upDepth + ' levels');
    var note = ' Long names are shortened; hover or tap to see the full name.';
    if (folded) meta.textContent = 'Collapsed by grade: ' + total + ' topics. Upstream: ' + depthLabel + '; downstream: 1 level.' + note;
    else meta.textContent = 'Local graph: ' + total + ' topics, ' + edgeCount + ' prerequisites. Upstream: ' + depthLabel + '; downstream: 1 level.' + note;
    updateFold(total, folded);
    cyEl.hidden = false;
    emptyEl.hidden = true;
    cyEl.dataset.ready = '0';
    cyEl.dataset.mode = folded ? 'grade' : 'full';
    cyEl.dataset.total = String(total);
    var heavy = !folded && total > 80;
    if (heavy) meta.textContent = 'Arranging all ' + total + ' topics…';

    var kick = heavy ? function (fn) { setTimeout(fn, 40); } : requestAnimationFrame;
    kick(function () {
      if (token !== graphToken) return;
      try {
        ensureDagre();
        if (cyEl.clientHeight < 40) cyEl.style.minHeight = '420px';
        var colors = theme();
        var narrow = labelLimit() <= 8;
        var textMax = narrow ? 104 : 126;
        var boxW = narrow ? 118 : 142;
        var elements = folded ? buildFoldedElements(nodeSet, colors) : buildFullElements(nodeSet, colors);
        var dense = heavy;
        var cyOptions = {
          container: cyEl,
          elements: elements,
          // If a large graph is scaled to fit one screen, nodes become only a few pixels and Cytoscape may render a nearly blank whole-graph texture.
          minZoom: heavy ? 0.5 : 0.05,
          maxZoom: 2.8,
          wheelSensitivity: 0.28,
          boxSelectionEnabled: false,
          autoungrabify: true,
          userPanningEnabled: true,
          userZoomingEnabled: true
        };
        cyOptions.style = [
          { selector: 'node', style: {
            label: 'data(label)', 'text-wrap': 'ellipsis', 'text-max-width': textMax + 'px',
            'text-overflow-wrap': 'anywhere',
            'text-valign': 'center', 'text-halign': 'center',
            'font-size': 13, 'font-family': FONT, color: 'data(color)',
            'background-color': 'data(bg)', 'border-width': 2, 'border-color': 'data(border)',
            shape: 'round-rectangle', width: boxW, height: 34, padding: 0, 'corner-radius': 8
          } },
          { selector: 'node.current', style: { 'border-width': 4, 'z-index': 10 } },
          { selector: 'edge', style: {
            width: 1.6, 'line-color': 'data(color)', 'target-arrow-color': 'data(color)',
            'target-arrow-shape': 'triangle', 'curve-style': dense ? 'straight' : 'bezier',
            'arrow-scale': 0.8, 'line-style': 'solid'
          } },
          { selector: 'edge.soft', style: { 'line-style': 'dashed', width: 1.5 } }
        ];
        cy = window.cytoscape(cyOptions);
        window.__cy = cy;
        cy.on('mouseover', 'node', function (event) { showTip(event.target); });
        cy.on('mouseout', 'node', function () { if (!tipFromTap) hideTip(); });
        cy.on('tap', 'node', function (event) {
          var id = event.target.id();
          tipFromTap = true;
          showTip(event.target);
          if (!id || String(id).indexOf('grade-') === 0 || id === selected) return;
          select(id, 'user');
        });
        cy.on('tap', function (event) {
          if (event.target === cy) { tipFromTap = false; hideTip(); }
        });
        var layout = cy.layout({
          name: 'dagre', rankDir: 'TB',
          rankSep: dense ? 48 : 64,
          nodeSep: dense ? 18 : 26,
          edgeSep: dense ? 8 : 12,
          ranker: dense ? 'longest-path' : 'network-simplex',
          padding: 16, animate: false, fit: true,
          nodeDimensionsIncludeLabels: false, spacingFactor: dense ? 1.02 : 1.05
        });
        layout.one('layoutstop', function () {
          if (token !== graphToken) return;
          requestAnimationFrame(function () {
            if (token !== graphToken || !cy) return;
            cy.resize();
            cy.fit(undefined, dense ? 24 : 28);
            var framed = false;
            if (heavy && cy.zoom() < 0.72) {
              cy.zoom(0.85);
              var focus = cy.getElementById(selected);
              if (focus && !focus.empty()) cy.center(focus);
              framed = true;
            }
            if (!folded) {
              meta.textContent = 'Local graph: ' + total + ' topics, ' + edgeCount + ' prerequisites. Upstream: ' + depthLabel + '; downstream: 1 level.'
                + (framed ? ' Centered on the current topic; drag to explore the rest.' : '')
                + note;
            }
            cyEl.dataset.ready = '1';
          });
        });
        layout.run();
      } catch (error) {
        cyEl.dataset.ready = 'err';
        meta.textContent = 'Could not render the graph: ' + (error && error.message ? error.message : error);
      }
    });
  }

  function select(raw, source) {
    var hit = resolveId(raw);
    if (!hit) {
      if (source === 'hash') {
        $('detail').replaceChildren(el('div', { class: 'detail-empty' },
          el('h1', { text: 'Topic Not Found' }),
          el('p', { text: 'ID "' + raw + '" is not in the graph and is not a registered legacy ID.' })));
      }
      return;
    }
    var same = hit.id === selected && !currentAlias && !hit.alias;
    if (hit.id !== selected) ancestorsOpen = false;
    selected = hit.id;
    currentAlias = source === 'user' ? null : hit.alias;
    if (source === 'user') {
      writeHash(selected);
      closeDrawerIfMobile();
    }
    highlight(true);
    renderDetail();
    if (!same) renderGraph();
  }

  function zoomBy(factor) {
    if (!cy) return;
    var rect = cy.container().getBoundingClientRect();
    cy.zoom({
      level: Math.max(cy.minZoom(), Math.min(cy.maxZoom(), cy.zoom() * factor)),
      renderedPosition: { x: rect.width / 2, y: rect.height / 2 }
    });
  }

  function showLoadError(message) {
    $('count').textContent = '';
    $('list').replaceChildren(el('p', { class: 'muted', text: message, style: 'padding:12px' }));
    $('detail').replaceChildren(el('div', { class: 'detail-empty' },
      el('h1', { text: 'Could Not Load Data' }),
      el('p', { text: message })));
    $('graph-meta').textContent = '';
  }

  function fillDomain() {
    var seen = {};
    topics.forEach(function (topic) { if (topic.domain) seen[topic.domain] = true; });
    var domainOrder = subject === 'chinese' ? ZH_DOMAIN_ORDER : DOMAIN_ORDER;
    var names = domainOrder.filter(function (name) { return seen[name]; });
    Object.keys(seen).forEach(function (name) { if (names.indexOf(name) < 0) names.push(name); });
    var select = $('fDomain');
    names.forEach(function (name) { select.append(el('option', { value: name, text: domainLabel(name) })); });
    if (domain && !seen[domain]) domain = '';
  }

  function readSubject() {
    var params = new URLSearchParams(location.search);
    var explicit = params.get('subject');
    if (explicit === 'english' || explicit === 'math' || explicit === 'physics' || explicit === 'chinese') return explicit;
    var hash = readHash();
    if (/^cnc_[A-Za-z0-9]+$/.test(hash)) {
      params.set('subject', 'chinese');
      history.replaceState(null, '', location.pathname + '?' + params.toString() + '#' + hash);
      return 'chinese';
    }
    if (/^cnp_[A-Za-z0-9]+$/.test(hash)) {
      params.set('subject', 'physics');
      history.replaceState(null, '', location.pathname + '?' + params.toString() + '#' + hash);
      return 'physics';
    }
    if (/^cne_[A-Za-z0-9]+$/.test(hash)) {
      params.set('subject', 'english');
      history.replaceState(null, '', location.pathname + '?' + params.toString() + '#' + hash);
      return 'english';
    }
    return 'math';
  }

  function configureSubject() {
    document.body.classList.toggle('subject-english', subject === 'english');
    document.body.classList.toggle('subject-physics', subject === 'physics');
    document.body.classList.toggle('subject-chinese', subject === 'chinese');
    document.querySelectorAll('.site-nav a:not(.subject-link), a.brand').forEach(function (link) {
      var href = link.getAttribute('href');
      var next = withSubject(href);
      if (next && next !== href) link.setAttribute('href', next);
    });
    document.querySelectorAll('.subject-link').forEach(function (link) {
      var on = link.getAttribute('data-subject') === subject;
      link.classList.toggle('on', on);
      if (on) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    });
    if (subject === 'physics') {
      document.querySelectorAll('#stage-tabs [data-stage]').forEach(function (button) {
        button.hidden = button.getAttribute('data-stage') === 'p';
      });
      var physicsGrade = $('fGrade');
      physicsGrade.replaceChildren();
      physicsGrade.append(el('option', { value: '', text: 'All grades' }));
      physicsGrade.append(el('option', { value: '8', text: 'Grade 8 (Semesters 1 and 2)' }));
      physicsGrade.append(el('option', { value: '9', text: 'Grade 9 (Full-Year Volume)' }));
      [
        [10, 'Required Volume 1'], [11, 'Required Volume 2'], [12, 'Required Volume 3'],
        [13, 'Selective Required Volume 1'], [14, 'Selective Required Volume 2'], [15, 'Selective Required Volume 3']
      ].forEach(function (row) {
        physicsGrade.append(el('option', { value: String(row[0]), text: row[1] }));
      });
      var physicsSample = $('pick-sample');
      if (physicsSample) physicsSample.textContent = "Try a sample: Ohm's Law";
      document.title = 'Knowledge Graph · Physics';
      return;
    }
    if (subject === 'chinese') {
      document.querySelectorAll('#stage-tabs [data-stage]').forEach(function (button) {
        var stageName = button.getAttribute('data-stage');
        button.hidden = stageName === 'j' || stageName === 'h';
      });
      var zhGrade = $('fGrade');
      zhGrade.replaceChildren();
      zhGrade.append(el('option', { value: '', text: 'All grades' }));
      [1, 2, 3, 4, 5, 6].forEach(function (g) {
        zhGrade.append(el('option', { value: String(g), text: GRADE_LABELS[g] }));
      });
      var zhSample = $('pick-sample');
      if (zhSample) zhSample.textContent = 'Try a sample: Quiet Night Thought';
      document.title = 'Knowledge Graph · Chinese';
      return;
    }
    if (subject !== 'english') return;
    var tabs = document.querySelectorAll('#stage-tabs [data-stage]');
    var spec = [['', 'All'], ['p', 'Elementary'], ['j', 'Middle School'], ['h', 'High School']];
    tabs.forEach(function (button, index) {
      if (index < spec.length) {
        button.setAttribute('data-stage', spec[index][0]);
        button.textContent = spec[index][1];
        button.hidden = false;
      } else {
        button.hidden = true;
      }
    });
    $('stage-tabs').setAttribute('aria-label', 'School level');
    var gradeSelect = $('fGrade');
    gradeSelect.replaceChildren();
    gradeSelect.append(el('option', { value: '', text: 'All grades' }));
    [3, 4, 5, 6, 7, 8, 9].forEach(function (g) {
      gradeSelect.append(el('option', { value: String(g), text: GRADE_LABELS[g] }));
    });
    [
      [10, 'Required Volume 1'], [11, 'Required Volume 2'], [12, 'Required Volume 3'],
      [13, 'Selective Required Volume 1'], [14, 'Selective Required Volume 2'],
      [15, 'Selective Required Volume 3'], [16, 'Selective Required Volume 4']
    ].forEach(function (row) {
      gradeSelect.append(el('option', { value: String(row[0]), text: row[1] }));
    });
    var sample = $('pick-sample');
    if (sample) sample.textContent = 'Try a sample: Present Continuous';
    document.title = 'Knowledge Graph · English';
  }

  function applyQuery() {
    var params = new URLSearchParams(location.search);
    var gradeValue = params.get('grade') || '';
    var gradeOk = subject === 'english' ? /^(?:[3-9]|1[0-6])$/ : subject === 'physics' ? /^(?:[89]|1[0-5])$/ : subject === 'chinese' ? /^[1-6]$/ : /^(?:[1-9]|1[0-4])$/;
    if (gradeOk.test(gradeValue)) grade = gradeValue;
    var stageValue = params.get('stage') || '';
    if (stageValue === 'p' || stageValue === 'j' || stageValue === 'h') stage = stageValue;
    domain = params.get('domain') || '';
  }

  function bootSelection() {
    var hash = readHash();
    if (hash && resolveId(hash)) { select(hash, 'hash'); return; }
    if (grade) {
      var first = topics.filter(passFilter)[0];
      if (first) { select(first.id, 'user'); return; }
    }
    renderDetail();
    renderGraph();
  }

  function bind() {
    $('q').addEventListener('input', function () {
      query = $('q').value.trim().toLowerCase();
      renderList();
      highlight(false);
    });
    $('stage-tabs').addEventListener('click', function (event) {
      var button = event.target.closest('[data-stage]');
      if (!button || button.hidden) return;
      stage = button.getAttribute('data-stage');
      if (subject === 'english') {
        var enGrade = parseInt(grade, 10);
        if (stage === 'p' && enGrade >= 7) grade = '';
        if (stage === 'j' && (enGrade <= 6 || enGrade >= 10)) grade = '';
        if (stage === 'h' && enGrade > 0 && enGrade <= 9) grade = '';
        syncControls();
        renderList();
        highlight(false);
        return;
      }
      var gradeNumber = parseInt(grade, 10);
      if (stage === 'p' && gradeNumber >= 7) grade = '';
      if (stage === 'j' && (gradeNumber <= 6 || gradeNumber >= 10)) grade = '';
      if (stage === 'h' && gradeNumber <= 9) grade = '';
      syncControls();
      renderList();
      highlight(false);
    });
    $('fGrade').addEventListener('change', function () {
      grade = $('fGrade').value;
      if (subject === 'english') {
        var enGrade = parseInt(grade, 10);
        if (enGrade >= 3 && enGrade <= 6 && (stage === 'j' || stage === 'h')) stage = 'p';
        if (enGrade >= 7 && enGrade <= 9 && (stage === 'p' || stage === 'h')) stage = 'j';
        if (enGrade >= 10 && (stage === 'p' || stage === 'j')) stage = 'h';
        syncControls();
        renderList();
        highlight(false);
        return;
      }
      var gradeNumber = parseInt(grade, 10);
      if (gradeNumber >= 1 && gradeNumber <= 6 && (stage === 'j' || stage === 'h')) stage = 'p';
      if (gradeNumber >= 7 && gradeNumber <= 9 && (stage === 'p' || stage === 'h')) stage = 'j';
      if (gradeNumber >= 10 && (stage === 'p' || stage === 'j')) stage = 'h';
      syncControls();
      renderList();
      highlight(false);
    });
    $('fDomain').addEventListener('change', function () {
      domain = $('fDomain').value;
      renderList();
      highlight(false);
    });
    $('depth-switch').addEventListener('click', function (event) {
      var button = event.target.closest('[data-depth]');
      if (!button) return;
      var value = button.getAttribute('data-depth');
      upDepth = value === 'all' ? 'all' : parseInt(value, 10);
      ancestorsOpen = false;
      try { sessionStorage.setItem('cnmExplore.depth', value); } catch (error) { /* Ignore storage errors. */ }
      syncDepthButtons();
      renderGraph();
    });
    $('graph-fold').addEventListener('click', function (event) {
      if (event.target.closest('#btn-expand-all')) ancestorsOpen = true;
      else if (event.target.closest('#btn-collapse-all')) ancestorsOpen = false;
      else return;
      renderGraph();
    });
    $('list-toggle').addEventListener('click', function () {
      var open = $('side').classList.toggle('open');
      $('list-toggle').setAttribute('aria-expanded', open ? 'true' : 'false');
      $('list-toggle').textContent = open ? 'Hide Topic List' : 'Topic List';
    });
    $('btn-fit').addEventListener('click', function () {
      if (!cy) return;
      cy.resize();
      var many = cy.nodes().length > 80;
      if (many) cy.minZoom(0.5);
      cy.fit(undefined, 36);
      if (many && cy.zoom() < 0.5) {
        cy.zoom(0.5);
        cy.center();
      }
    });
    $('btn-zoom-in').addEventListener('click', function () { zoomBy(1.25); });
    $('btn-zoom-out').addEventListener('click', function () { zoomBy(0.8); });
    $('pick-sample').addEventListener('click', function () {
      if (subject === 'physics') {
        var phyHit = topics.find(function (topic) { return topic.name === '欧姆定律'; });
        if (phyHit) select(phyHit.id, 'user');
        return;
      }
      if (subject === 'english') {
        var hit = topics.find(function (topic) { return String(topic.name).indexOf('现在进行时') >= 0; });
        if (hit) select(hit.id, 'user');
        return;
      }
      if (subject === 'chinese') {
        var zhHit = topics.find(function (topic) { return String(topic.name).indexOf('静夜思') >= 0; });
        if (zhHit) select(zhHit.id, 'user');
        return;
      }
      select('cnm_221', 'user');
    });
    document.body.addEventListener('click', function (event) {
      var jump = event.target.closest('[data-jump]');
      if (!jump) return;
      select(jump.getAttribute('data-jump'), 'user');
    });
    window.addEventListener('hashchange', function () {
      var hash = readHash();
      if (hash) select(hash, 'hash');
    });
    if (window.ResizeObserver) {
      new ResizeObserver(function () { if (cy) cy.resize(); }).observe($('cy'));
    }
    var colorScheme = window.matchMedia('(prefers-color-scheme: dark)');
    if (colorScheme.addEventListener) {
      colorScheme.addEventListener('change', function () { if (selected) renderGraph(); });
    }
    var narrow = window.matchMedia('(max-width: 700px)');
    if (narrow.addEventListener) {
      narrow.addEventListener('change', function () { if (selected) renderGraph(); });
    }
  }

  async function loadQuestions() {
    questionsByTopic = new Map();
    try {
      var response = await fetch('../data/questions.json');
      if (!response.ok) return;
      var rows = await response.json();
      if (!Array.isArray(rows)) return;
      rows.forEach(function (q) {
        if (!q || !q.topicId) return;
        var bucket = questionsByTopic.get(q.topicId);
        if (!bucket) questionsByTopic.set(q.topicId, bucket = []);
        bucket.push(q);
      });
    } catch (e) { /* If the question bank is unavailable, show the existing sample text only. */ }
  }

  async function load() {
    var files = ['topics.json', 'dependencies.json', 'id-aliases.json', 'cn-curriculum-standards.json'];
    var responses = await Promise.all(files.map(function (file) { return fetch('../data/' + file); }));
    responses.forEach(function (response, responseIndex) {
      if (!response.ok) throw new Error(files[responseIndex] + ' HTTP ' + response.status);
    });
    var json = await Promise.all(responses.map(function (response) { return response.json(); }));
    topics = json[0].filter(function (topic) { return topicSubject(topic) === subject; });
    mathNames = {};
    if (subject === 'physics') {
      json[0].forEach(function (topic) { if (topicSubject(topic) === 'math') mathNames[topic.id] = topic.name; });
    }
    var allow = {};
    topics.forEach(function (topic) { allow[topic.id] = true; });
    deps = json[1].filter(function (edge) { return allow[edge.topicId] && allow[edge.prerequisiteId]; });
    aliases = (json[2] && json[2].aliases) || {};
    (json[3].items || []).forEach(function (item) { stdById.set(item.id, item); });
    topics.forEach(function (topic, topicIndex) {
      byId.set(topic.id, topic);
      indexOf.set(topic.id, topicIndex);
      pre.set(topic.id, []);
      post.set(topic.id, []);
    });
    deps.forEach(function (edge) {
      if (!pre.has(edge.topicId) || !post.has(edge.prerequisiteId)) return;
      pre.get(edge.topicId).push({ id: edge.prerequisiteId, strength: edge.strength, reason: edge.reason || '' });
      post.get(edge.prerequisiteId).push({ id: edge.topicId, strength: edge.strength, reason: edge.reason || '' });
    });
    pre.forEach(function (list) {
      list.sort(function (a, b) {
        return ((a.strength === 'hard' ? 0 : 1) - (b.strength === 'hard' ? 0 : 1)) || ((indexOf.get(a.id) || 0) - (indexOf.get(b.id) || 0));
      });
    });
    post.forEach(function (list) {
      list.sort(function (a, b) { return (indexOf.get(a.id) || 0) - (indexOf.get(b.id) || 0); });
    });
  }

  subject = readSubject();
  configureSubject();
  restoreDepth();
  syncDepthButtons();
  applyQuery();
  bind();
  load().then(function () { return loadQuestions(); }).then(function () {
    fillDomain();
    syncControls();
    renderList();
    bootSelection();
  }).catch(function (error) {
    showLoadError('Could not read data (' + (error && error.message ? error.message : error) + '). Run python3 -m http.server 8000 from the project root instead of opening the page directly with file://.');
  });
})();
