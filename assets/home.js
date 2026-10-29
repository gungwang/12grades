/* Home page: calculate statistics and grade links from data/*.json instead of hard-coding counts. */
(function () {
  'use strict';
  var raw = location.hash.replace(/^#/, '');
  try { raw = decodeURIComponent(raw); } catch (e) { /* Leave the value unchanged. */ }
  if (/^(?:cnm|cne|cnp|cnc)_[A-Za-z0-9]+$/.test(raw)) return;

  var GRADE_LABELS = ['', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9'];
  var subjectParam = new URLSearchParams(location.search).get('subject');
  var subject = subjectParam === 'english' || subjectParam === 'physics' || subjectParam === 'chinese' ? subjectParam : 'math';
  var PREFIX = { math: 'cnm_', english: 'cne_', physics: 'cnp_', chinese: 'cnc_' };
  var STD_PREFIX = { math: 'cms-', english: 'ces-', physics: 'cps-', chinese: 'ccs-' };

  function withSubject(href) {
    if (subject === 'math' || !href || href.indexOf('subject=') >= 0 || href.indexOf('http') === 0) return href;
    return href + (href.indexOf('?') >= 0 ? '&' : '?') + 'subject=' + subject;
  }

  document.body.classList.toggle('subject-english', subject === 'english');
  document.body.classList.toggle('subject-physics', subject === 'physics');
  document.body.classList.toggle('subject-chinese', subject === 'chinese');
  document.querySelectorAll('.subject-link').forEach(function (link) {
    var on = link.getAttribute('data-subject') === subject;
    link.classList.toggle('on', on);
    if (on) link.setAttribute('aria-current', 'true');
    else link.removeAttribute('aria-current');
  });
  document.querySelectorAll('.site-nav a:not(.subject-link), a.brand').forEach(function (link) {
    var href = link.getAttribute('href');
    var next = withSubject(href);
    if (next && next !== href) link.setAttribute('href', next);
  });
  if (subject === 'english') {
    document.title = 'English · 12Grades Knowledge Graph';
    var eye = document.querySelector('.eyebrow');
    if (eye) eye.textContent = 'English: Grade 3 through high school';
    var primary = document.querySelector('.hero-actions a.btn-primary');
    var browse = document.querySelector('.hero-actions a.btn:not(.btn-primary)');
    if (primary) primary.setAttribute('href', 'diagnose/?subject=english');
    if (browse) browse.setAttribute('href', 'explore/?subject=english');
    var demo = document.querySelector('.quiet-link a');
    if (demo) {
      demo.setAttribute('href', 'diagnose/?subject=english&grade=' + encodeURIComponent('四上') + '&demo=1');
      demo.textContent = 'Preview a demo: English, Grade 4, Semester 1';
    }
  } else if (subject === 'physics') {
    document.title = 'Physics · 12Grades Knowledge Graph';
    var peye = document.querySelector('.eyebrow');
    if (peye) peye.textContent = 'Physics: Middle School Grades 8–9 · High School Required and Selective Courses';
    var pprimary = document.querySelector('.hero-actions a.btn-primary');
    var pbrowse = document.querySelector('.hero-actions a.btn:not(.btn-primary)');
    if (pprimary) pprimary.setAttribute('href', 'diagnose/?subject=physics');
    if (pbrowse) pbrowse.setAttribute('href', 'explore/?subject=physics');
    var pdemo = document.querySelector('.quiet-link a');
    if (pdemo) {
      pdemo.setAttribute('href', 'diagnose/?subject=physics&grade=' + encodeURIComponent('八上') + '&demo=1');
      pdemo.textContent = 'Preview a demo: Physics, Grade 8, Semester 1';
    }
  } else if (subject === 'chinese') {
    document.title = 'Chinese · 12Grades Knowledge Graph';
    var zeye = document.querySelector('.eyebrow');
    if (zeye) zeye.textContent = 'Chinese: Grades 1–6 · Unified Edition';
    var zprimary = document.querySelector('.hero-actions a.btn-primary');
    var zbrowse = document.querySelector('.hero-actions a.btn:not(.btn-primary)');
    if (zprimary) zprimary.setAttribute('href', 'diagnose/?subject=chinese');
    if (zbrowse) zbrowse.setAttribute('href', 'explore/?subject=chinese');
    var zdemo = document.querySelector('.quiet-link a');
    if (zdemo) {
      zdemo.setAttribute('href', 'diagnose/?subject=chinese&grade=' + encodeURIComponent('一上') + '&demo=1');
      zdemo.textContent = 'Preview a demo: Chinese, Grade 1, Semester 1';
    }
  }

  function setText(id, value) {
    var node = document.getElementById(id);
    if (node) node.textContent = value;
  }

  function fail(message) {
    var box = document.getElementById('load-error');
    if (!box) return;
    box.hidden = false;
    box.textContent = message;
  }

  Promise.all([
    fetch('data/topics.json'),
    fetch('data/dependencies.json'),
    fetch('data/questions.json'),
    fetch('data/cn-curriculum-standards.json')
  ]).then(function (responses) {
    responses.forEach(function (response, index) {
      if (!response.ok) throw new Error('HTTP ' + response.status);
    });
    return Promise.all(responses.map(function (response) { return response.json(); }));
  }).then(function (data) {
    var topics = data[0];
    var deps = data[1];
    var questions = data[2];
    var standards = data[3];
    if (!Array.isArray(topics) || !Array.isArray(deps) || !Array.isArray(questions)) {
      throw new Error('Unrecognized data format');
    }
    var items = standards && Array.isArray(standards.items) ? standards.items : [];
    function subjectOfId(id) {
      id = String(id || '');
      if (id.indexOf('cne_') === 0) return 'english';
      if (id.indexOf('cnp_') === 0) return 'physics';
      if (id.indexOf('cnc_') === 0) return 'chinese';
      return 'math';
    }
    function subjectOfStd(id) {
      id = String(id || '');
      if (id.indexOf('ces-') === 0) return 'english';
      if (id.indexOf('cps-') === 0) return 'physics';
      if (id.indexOf('ccs-') === 0) return 'chinese';
      return 'math';
    }
    var wantEnglish = subject === 'english';
    var wantPhysics = subject === 'physics';
    var wantChinese = subject === 'chinese';
    topics = topics.filter(function (topic) { return (topic.subject || subjectOfId(topic.id)) === subject; });
    deps = deps.filter(function (edge) { return subjectOfId(edge.topicId) === subject; });
    questions = questions.filter(function (question) { return subjectOfId(question.topicId) === subject; });
    items = items.filter(function (item) { return subjectOfStd(item.id) === subject; });
    setText('n-topics', String(topics.length));
    setText('n-edges', String(deps.length));
    setText('n-questions', String(questions.length));
    setText('n-standards', String(items.length));

    var grades = document.getElementById('grades');
    if (!grades) return;
    grades.replaceChildren();
    grades.removeAttribute('aria-busy');
    function addCard(g, stageName, title, klass, splitText, href) {
      var list = topics.filter(function (topic) { return topic.grade === g; });
      var link = document.createElement('a');
      link.className = 'grade-card ' + klass;
      link.href = href;
      var stage = document.createElement('span');
      stage.className = 'grade-stage';
      stage.textContent = stageName;
      var name = document.createElement('strong');
      name.textContent = title;
      var count = document.createElement('span');
      count.className = 'grade-count';
      count.textContent = list.length + (list.length === 1 ? ' topic' : ' topics');
      var split = document.createElement('span');
      split.className = 'grade-stage';
      split.textContent = splitText;
      link.append(stage, name, count, split);
      grades.append(link);
    }
    var from = wantPhysics ? 8 : (wantEnglish ? 3 : 1);
    var to = wantChinese ? 6 : 9;
    for (var g = from; g <= to; g++) {
      var list = topics.filter(function (topic) { return topic.grade === g; });
      var up = list.filter(function (topic) { return topic.semester === '上'; }).length;
      var down = list.filter(function (topic) { return topic.semester === '下'; }).length;
      var whole = list.filter(function (topic) { return topic.semester === '全'; }).length;
      var splitText = whole ? 'Full volume: ' + whole : 'Semester 1: ' + up + ' · Semester 2: ' + down;
      var href = subject !== 'math' ? 'explore/?subject=' + subject + '&grade=' + g : 'explore/?grade=' + g;
      addCard(g, g <= 6 ? 'Elementary' : (wantPhysics ? 'Middle School Physics' : 'Middle School'), GRADE_LABELS[g], g <= 6 ? 'is-primary' : 'is-junior', splitText, href);
    }
    if (wantChinese) {
      /* Chinese-language topics are available through Grade 6. */
    } else if (wantPhysics) {
      addCard(10, 'High School Physics', 'Required 1', 'is-senior', 'Required Volume 1', 'explore/?subject=physics&grade=10');
      addCard(11, 'High School Physics', 'Required 2', 'is-senior', 'Required Volume 2', 'explore/?subject=physics&grade=11');
      addCard(12, 'High School Physics', 'Required 3', 'is-senior', 'Required Volume 3', 'explore/?subject=physics&grade=12');
      addCard(13, 'High School Physics', 'Selective 1', 'is-senior', 'Selective Required Volume 1', 'explore/?subject=physics&grade=13');
      addCard(14, 'High School Physics', 'Selective 2', 'is-senior', 'Selective Required Volume 2', 'explore/?subject=physics&grade=14');
      addCard(15, 'High School Physics', 'Selective 3', 'is-senior', 'Selective Required Volume 3', 'explore/?subject=physics&grade=15');
    } else if (wantEnglish) {
      addCard(10, 'High School', 'Required 1', 'is-senior', 'Required Volume 1', 'explore/?subject=english&grade=10');
      addCard(11, 'High School', 'Required 2', 'is-senior', 'Required Volume 2', 'explore/?subject=english&grade=11');
      addCard(12, 'High School', 'Required 3', 'is-senior', 'Required Volume 3', 'explore/?subject=english&grade=12');
      addCard(13, 'High School', 'Selective 1', 'is-senior', 'Selective Required Volume 1', 'explore/?subject=english&grade=13');
      addCard(14, 'High School', 'Selective 2', 'is-senior', 'Selective Required Volume 2', 'explore/?subject=english&grade=14');
      addCard(15, 'High School', 'Selective 3', 'is-senior', 'Selective Required Volume 3', 'explore/?subject=english&grade=15');
      addCard(16, 'High School', 'Selective 4', 'is-senior', 'Selective Required Volume 4', 'explore/?subject=english&grade=16');
    } else {
      addCard(10, 'High School', 'Year 1', 'is-senior', 'Required Volume 1', 'explore/?grade=10');
      addCard(11, 'High School', 'Year 2', 'is-senior', 'Required Volume 2', 'explore/?grade=11');
      addCard(12, 'High School', 'Selective 1', 'is-senior', 'Selective Required Volume 1', 'explore/?grade=12');
      addCard(13, 'High School', 'Selective 2', 'is-senior', 'Selective Required Volume 2', 'explore/?grade=13');
      addCard(14, 'High School', 'Selective 3', 'is-senior', 'Selective Required Volume 3', 'explore/?grade=14');
    }
  }).catch(function (error) {
    fail('Could not load data (' + (error && error.message ? error.message : error) + '). Run python3 -m http.server 8000 from the project root, then open the site in a browser instead of opening the HTML file directly.');
  });
})();
