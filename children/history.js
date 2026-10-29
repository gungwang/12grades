/* History and learning gaps page: a child's diagnostic history and topics currently marked weak or needing review, linked to the knowledge graph. */
(function () {
  'use strict';
  var CC = window.CnmChildren;
  var picker = document.getElementById('picker');
  var content = document.getElementById('content');
  var SUBJECTS = [['', 'All'], ['math', 'Math'], ['chinese', 'Chinese'], ['english', 'English'], ['physics', 'Physics']];
  var SUBJECT_NAME = { math: 'Math', chinese: 'Chinese', english: 'English', physics: 'Physics' };
  var GRADE_LABELS = {
    '一年级': 'Grade 1', '二年级': 'Grade 2', '三年级': 'Grade 3',
    '四年级': 'Grade 4', '五年级': 'Grade 5', '六年级': 'Grade 6',
    '七年级': 'Grade 7', '八年级': 'Grade 8', '九年级': 'Grade 9',
    '高一': 'High School Year 1', '高二': 'High School Year 2', '高三': 'High School Year 3'
  };
  var TEXTBOOK_LABELS = {
    '人教版': "People's Education Press",
    '北师大版': 'Beijing Normal University Press',
    '苏教版': 'Jiangsu Education Press',
    '沪教版': 'Shanghai Education Press',
    '外研版': 'Foreign Language Teaching and Research Press',
    '译林版': 'Yilin Press',
    '其他': 'Other'
  };
  function displayValue(value, labels) { return labels[value] || value; }
  function displayScopeLabel(value) {
    var text = String(value || '').replace(/（整体筛查）/g, ' (full-grade screening)')
      .replace(/（整章）/g, ' (entire chapter)')
      .replace(/（旧编号已对应到小学知识点）/g, ' (legacy ID mapped to elementary topics)');
    if (text === '诊断') return 'Diagnostic';
    var books = {
      '高一（必修第一册）': 'High School Year 1 · Required Volume 1',
      '高二（必修第二册）': 'High School Year 2 · Required Volume 2',
      '选必一（选择性必修第一册）': 'Selective Required Volume 1',
      '选必二（选择性必修第二册）': 'Selective Required Volume 2',
      '选必三（选择性必修第三册）': 'Selective Required Volume 3',
      '选必四（选择性必修第四册）': 'Selective Required Volume 4',
      '必修一（必修第一册）': 'Required Volume 1',
      '必修二（必修第二册）': 'Required Volume 2',
      '必修三（必修第三册）': 'Required Volume 3'
    };
    var keys = Object.keys(books).sort(function (a, b) { return b.length - a.length; });
    for (var i = 0; i < keys.length; i++) {
      if (text.indexOf(keys[i]) === 0) return books[keys[i]] + text.slice(keys[i].length);
    }
    var digits = { '一': '1', '二': '2', '三': '3', '四': '4', '五': '5', '六': '6', '七': '7', '八': '8', '九': '9' };
    var match = /^([一二三四五六七八九])年级(全一册|上册|下册)?/.exec(text);
    if (match) {
      var suffix = match[2] === '上册' ? ', Semester 1' : match[2] === '下册' ? ', Semester 2' : match[2] === '全一册' ? ' (Full-Year Volume)' : '';
      return 'Grade ' + digits[match[1]] + suffix + text.slice(match[0].length);
    }
    match = /^([一二三四五六七八九])([上下全])(?=\s|$|（)/.exec(text);
    if (match) {
      var volume = match[2] === '上' ? ', Semester 1' : match[2] === '下' ? ', Semester 2' : ' (Full-Year Volume)';
      return 'Grade ' + digits[match[1]] + volume + text.slice(match[0].length);
    }
    match = /^(必修第([一二三])册|选择性必修第([一二三四])册)(?=\s|$)/.exec(text);
    if (match) {
      var bookNumber = match[2] ? ({ '一': 1, '二': 2, '三': 3 }[match[2]]) : ({ '一': 1, '二': 2, '三': 3, '四': 4 }[match[3]]);
      var bookLabel = match[2] ? 'Required Volume ' + bookNumber : 'Selective Required Volume ' + bookNumber;
      return bookLabel + text.slice(match[0].length);
    }
    match = /^(高[一二]|选必[一二三四])(?=\s|$)/.exec(text);
    if (match) {
      var highSchoolLabels = { '高一': 'High School Year 1', '高二': 'High School Year 2', '选必一': 'Selective 1', '选必二': 'Selective 2', '选必三': 'Selective 3', '选必四': 'Selective 4' };
      return highSchoolLabels[match[1]] + text.slice(match[0].length);
    }
    return text;
  }
  var topics = null;
  var childId = null;
  var subjectSel = '';

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function subjectOfId(id) {
    id = String(id || '');
    return id.indexOf('cne_') === 0 ? 'english' : id.indexOf('cnp_') === 0 ? 'physics' : id.indexOf('cnc_') === 0 ? 'chinese' : 'math';
  }
  function exploreHref(id) {
    var sub = subjectOfId(id);
    return '../explore/' + (sub === 'math' ? '' : '?subject=' + sub) + '#' + encodeURIComponent(id);
  }
  function pad(n) { return ('0' + n).slice(-2); }
  function fmt(iso) {
    var d = new Date(iso);
    if (isNaN(d)) return '';
    return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()) + ' ' + pad(d.getHours()) + ':' + pad(d.getMinutes());
  }
  function nameOf(id) { return topics && topics[id] ? topics[id].name : id; }
  function chapterOf(id) { return topics && topics[id] && topics[id].chapter ? displayScopeLabel(topics[id].chapter) : ''; }
  function tag(cls, text) { return el('span', 'kid-tag ' + cls, text); }

  function retestHref(ids) { return '../diagnose/?target=' + ids.map(encodeURIComponent).join(','); }

  function topicRow(id, info) {
    var li = el('li', 'wk-item');
    var top = el('div', 'wk-top');
    var a = el('a', 'wk-name', nameOf(id));
    a.href = exploreHref(id);
    top.appendChild(a);
    top.appendChild(tag(info.status === 'weak' ? 'weak' : 'shaky', info.status === 'weak' ? 'Weak' : 'Needs Review'));
    if (info.root) top.appendChild(tag('root', 'Root cause'));
    top.appendChild(tag('sub', SUBJECT_NAME[subjectOfId(id)]));
    li.appendChild(top);
    var meta = [];
    var ch = chapterOf(id);
    if (ch) meta.push(ch);
    meta.push(fmt(info.at) + ' diagnostic');
    li.appendChild(el('p', 'wk-meta', meta.join(' · ')));
    var re = el('a', 'wk-retest', 'Retest');
    re.href = retestHref([id]);
    li.appendChild(re);
    return li;
  }

  function weakSection(child) {
    var by = CC.latestStatus(child.id, subjectSel || null);
    var ids = Object.keys(by).filter(function (id) { return by[id].status === 'weak' || by[id].status === 'shaky'; });
    var rank = function (id) { return (by[id].status === 'weak' ? 0 : 2) + (by[id].root ? 0 : 1); };
    ids.sort(function (a, b) {
      return rank(a) - rank(b) || ((topics && topics[a] && topics[a].grade) || 99) - ((topics && topics[b] && topics[b].grade) || 99) || String(by[b].at).localeCompare(String(by[a].at));
    });
    var sec = el('section', 'kid-section');
    var weakN = ids.filter(function (id) { return by[id].status === 'weak'; }).length;
    sec.appendChild(el('h2', null, 'Current Learning Gaps'));
    if (!CC.recordsOf(child.id).length) {
      sec.appendChild(el('p', 'kid-empty', 'No diagnostic records yet. Learning gaps will appear here after a diagnostic.'));
      return sec;
    }
    if (!ids.length) {
      sec.appendChild(el('p', 'kid-empty', 'The latest results show no weak or uncertain topics.'));
      return sec;
    }
    sec.appendChild(el('p', 'muted small', 'The latest result is used when a topic has been tested more than once. ' + weakN + ' weak, ' + (ids.length - weakN) + ' needing review. Select a topic to view its prerequisites and learning content.'));
    var ul = el('ul', 'wk-list');
    ids.forEach(function (id) { ul.appendChild(topicRow(id, by[id])); });
    sec.appendChild(ul);
    return sec;
  }

  function recordCard(child, r) {
    var det = el('details', 'rec');
    var sum = el('summary');
    var line1 = el('div', 'rec-top');
    line1.appendChild(tag('sub', SUBJECT_NAME[r.subject] || 'Math'));
    line1.appendChild(el('b', 'rec-label', displayScopeLabel(r.label || 'Diagnostic')));
    sum.appendChild(line1);
    var c = r.counts || {};
    var line2 = el('div', 'rec-counts');
    line2.appendChild(el('span', 'rec-date', fmt(r.savedAt)));
    line2.appendChild(tag('weak', 'Weak ' + (c.weak || 0)));
    line2.appendChild(tag('shaky', 'Review ' + (c.shaky || 0)));
    line2.appendChild(tag('ok', 'Mastered ' + (c.mastered || 0)));
    if (c.untested) line2.appendChild(tag('unk', 'Not tested ' + c.untested));
    sum.appendChild(line2);
    det.appendChild(sum);

    var body = el('div', 'rec-body');
    body.appendChild(el('p', 'muted small', 'Answered ' + (r.asked || 0) + ' question' + ((r.asked || 0) === 1 ? '' : 's') + (r.mode === 'screen' ? ' in a full-grade screen' : '') + '.'));
    var rootSet = {};
    (r.roots || []).forEach(function (id) { rootSet[id] = true; });
    var group = function (title, ids, status) {
      if (!ids || !ids.length) return;
      body.appendChild(el('h4', null, title + '（' + ids.length + '）'));
      var ul = el('ul', 'rec-topics');
      ids.forEach(function (id) {
        var li = el('li');
        var a = el('a', null, nameOf(id));
        a.href = exploreHref(id);
        li.appendChild(a);
        if (status === 'weak' && rootSet[id]) li.appendChild(tag('root', 'Root cause'));
        ul.appendChild(li);
      });
      body.appendChild(ul);
    };
    group('Weak', r.weak, 'weak');
    group('Needs Review', r.shaky, 'shaky');
    if (!(r.weak || []).length && !(r.shaky || []).length) body.appendChild(el('p', 'kid-empty', 'No weak or uncertain topics were found in this session.'));

    var row = el('div', 'rec-actions');
    if (r.targets && r.targets.length) {
      var re = el('a', 'btn', 'Retest');
      re.href = retestHref(r.targets);
      row.appendChild(re);
    }
    var del = el('button', 'danger', 'Delete This Record');
    del.type = 'button';
    del.addEventListener('click', function () {
      if (!confirm('Delete this diagnostic record?')) return;
      CC.removeRecord(child.id, r.key);
      render();
    });
    row.appendChild(del);
    body.appendChild(row);
    det.appendChild(body);
    return det;
  }

  function recordsSection(child) {
    var recs = CC.recordsOf(child.id).filter(function (r) { return !subjectSel || r.subject === subjectSel; });
    var sec = el('section', 'kid-section');
    sec.appendChild(el('h2', null, 'Diagnostic History (' + recs.length + ')'));
    if (!recs.length) {
      sec.appendChild(el('p', 'kid-empty', subjectSel ? 'No records for this subject yet.' : 'No diagnostic records yet.'));
    } else {
      recs.forEach(function (r) { sec.appendChild(recordCard(child, r)); });
    }
    var go = el('a', 'btn btn-primary', 'Start a Diagnostic');
    go.href = '../diagnose/' + (subjectSel === 'english' || subjectSel === 'physics' || subjectSel === 'chinese' ? '?subject=' + subjectSel : '');
    sec.appendChild(go);
    return sec;
  }

  function renderPicker(kids) {
    picker.textContent = '';
    if (!kids.length) return;
    var label = el('label', null, 'Child');
    label.setAttribute('for', 'kid-select');
    var sel = el('select');
    sel.id = 'kid-select';
    kids.forEach(function (c) {
      var o = el('option', null, c.name + ' (' + displayValue(c.grade, GRADE_LABELS) + ')');
      o.value = c.id;
      sel.appendChild(o);
    });
    sel.value = childId;
    sel.addEventListener('change', function () {
      childId = sel.value;
      CC.setCurrent(childId);
      history.replaceState(null, '', location.pathname + '?child=' + encodeURIComponent(childId));
      render();
    });
    var manage = el('a', 'btn', 'Manage Profiles');
    manage.href = './';
    picker.appendChild(label);
    picker.appendChild(sel);
    picker.appendChild(manage);
  }

  function renderTabs() {
    var row = el('div', 'stage-tabs kid-tabs');
    row.setAttribute('role', 'tablist');
    row.setAttribute('aria-label', 'Subject');
    SUBJECTS.forEach(function (s) {
      var b = el('button', 'stage-tab' + (subjectSel === s[0] ? ' on' : ''), s[1]);
      b.type = 'button';
      b.setAttribute('role', 'tab');
      b.setAttribute('aria-selected', subjectSel === s[0] ? 'true' : 'false');
      b.addEventListener('click', function () { subjectSel = s[0]; render(); });
      row.appendChild(b);
    });
    return row;
  }

  function render() {
    var kids = CC.list();
    renderPicker(kids);
    content.textContent = '';
    if (!kids.length) {
      content.appendChild(el('p', 'kid-empty', 'No child profiles yet. Add a child to save diagnostic results by profile.'));
      var add = el('a', 'btn btn-primary', 'Add a Child');
      add.href = './';
      content.appendChild(add);
      return;
    }
    var child = CC.get(childId) || kids[0];
    childId = child.id;
    var head = el('p', 'kid-meta', child.name + ' · ' + displayValue(child.grade, GRADE_LABELS) + ' · ' + displayValue(child.textbook, TEXTBOOK_LABELS));
    content.appendChild(head);
    content.appendChild(renderTabs());
    content.appendChild(weakSection(child));
    content.appendChild(recordsSection(child));
  }

  function init() {
    var kids = CC.list();
    var want = new URLSearchParams(location.search).get('child');
    var cur = CC.current();
    childId = (want && CC.get(want) && want) || (cur && cur.id) || (kids[0] && kids[0].id) || null;
    if (!kids.length) { render(); return; }
    fetch('../data/topics.json').then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    }).then(function (rows) {
      topics = {};
      rows.forEach(function (t) { topics[t.id] = t; });
    }).catch(function () { topics = null; }).then(render);
  }
  init();
})();
