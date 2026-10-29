/* Child profiles page: add, edit, and remove profiles, and choose the active child. Data comes from assets/children.js (localStorage). */
(function () {
  'use strict';
  var CC = window.CnmChildren;
  var listBox = document.getElementById('list');
  var form = document.getElementById('form');
  var nameIn = document.getElementById('f-name');
  var gradeSel = document.getElementById('f-grade');
  var bookSel = document.getElementById('f-book');
  var errBox = document.getElementById('f-error');
  var submitBtn = document.getElementById('f-submit');
  var cancelBtn = document.getElementById('f-cancel');
  var formTitle = document.getElementById('form-title');
  var exportBtn = document.getElementById('export-backup');
  var exportStatus = document.getElementById('export-status');
  var importFile = document.getElementById('import-backup');
  var importPreview = document.getElementById('import-preview');
  var importError = document.getElementById('import-error');
  var importStatus = document.getElementById('import-status');
  var confirmImport = document.getElementById('confirm-import');
  var pendingBackup = null;
  var pendingPreview = null;
  var fileRequest = 0;
  var editing = null;

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

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
  function fillSelect(sel, items, placeholder, labels) {
    sel.textContent = '';
    if (placeholder) { var o = el('option', null, placeholder); o.value = ''; sel.appendChild(o); }
    items.forEach(function (x) { var o = el('option', null, displayValue(x, labels || {})); o.value = x; sel.appendChild(o); });
  }
  fillSelect(gradeSel, CC.GRADES, 'Select a grade', GRADE_LABELS);
  fillSelect(bookSel, CC.TEXTBOOKS, null, TEXTBOOK_LABELS);

  var params = new URLSearchParams(location.search);
  if (params.get('from') === 'diagnose') {
    var back = document.getElementById('back');
    var sub = params.get('subject');
    var href = '../diagnose/' + (sub === 'english' || sub === 'physics' || sub === 'chinese' ? '?subject=' + sub : '');
    var a = el('a', null, '← Back to diagnostics');
    a.href = href;
    back.appendChild(a);
    back.hidden = false;
  }

  function showError(msg) { errBox.textContent = msg || ''; errBox.hidden = !msg; }

  function resetForm() {
    editing = null;
    nameIn.value = '';
    gradeSel.value = '';
    bookSel.value = CC.TEXTBOOKS[0];
    formTitle.textContent = 'Add a Child';
    submitBtn.textContent = 'Add a Child';
    cancelBtn.hidden = true;
    showError('');
  }

  function startEdit(c) {
    editing = c.id;
    nameIn.value = c.name;
    gradeSel.value = c.grade;
    bookSel.value = c.textbook;
    formTitle.textContent = 'Edit “' + c.name + '”';
    submitBtn.textContent = 'Save Changes';
    cancelBtn.hidden = false;
    showError('');
    document.getElementById('form-card').scrollIntoView({ block: 'center' });
    nameIn.focus();
  }

  function stats(c) {
    var recs = CC.recordsOf(c.id);
    var by = CC.latestStatus(c.id);
    var weak = 0;
    Object.keys(by).forEach(function (id) { if (by[id].status === 'weak') weak++; });
    return { runs: recs.length, weak: weak };
  }

  function card(c, isCurrent) {
    var st = stats(c);
    var art = el('article', 'kid-card' + (isCurrent ? ' is-current' : ''));
    var head = el('div', 'kid-head');
    head.appendChild(el('h3', null, c.name));
    if (isCurrent) head.appendChild(el('span', 'kid-badge', 'Current'));
    art.appendChild(head);
    art.appendChild(el('p', 'kid-meta', displayValue(c.grade, GRADE_LABELS) + ' · ' + displayValue(c.textbook, TEXTBOOK_LABELS)));
    art.appendChild(el('p', 'kid-stat', st.runs
      ? 'Diagnosed ' + st.runs + ' time' + (st.runs === 1 ? '' : 's') + '; ' + st.weak + ' weak topic' + (st.weak === 1 ? '' : 's')
      : 'No diagnostic records yet'));
    var row = el('div', 'kid-actions');
    if (!isCurrent) {
      var use = el('button', 'primary', 'Set as Current');
      use.type = 'button';
      use.addEventListener('click', function () { CC.setCurrent(c.id); render(); });
      row.appendChild(use);
    }
    var hist = el('a', 'btn', 'History & Learning Gaps');
    hist.href = 'history.html?child=' + encodeURIComponent(c.id);
    row.appendChild(hist);
    var edit = el('button', null, 'Edit');
    edit.type = 'button';
    edit.addEventListener('click', function () { startEdit(c); });
    row.appendChild(edit);
    var del = el('button', 'danger', 'Delete');
    del.type = 'button';
    del.addEventListener('click', function () {
      if (!confirm('Delete the profile for “' + c.name + '” and all diagnostic records? This cannot be undone.')) return;
      CC.remove(c.id);
      if (editing === c.id) resetForm();
      render();
    });
    row.appendChild(del);
    art.appendChild(row);
    return art;
  }

  function render() {
    var kids = CC.list();
    var cur = CC.current();
    exportBtn.disabled = !kids.length;
    exportStatus.hidden = true;
    listBox.textContent = '';
    if (!kids.length) {
      listBox.appendChild(el('p', 'kid-empty', 'No child profiles yet. Enter a name and grade below to add the first one.'));
    } else {
      kids.forEach(function (c) { listBox.appendChild(card(c, !!cur && cur.id === c.id)); });
    }
    var full = kids.length >= CC.MAX_CHILDREN && !editing;
    document.getElementById('form-card').hidden = full;
    if (full) {
      var note = el('p', 'muted small', 'You have reached the limit of ' + CC.MAX_CHILDREN + ' child profiles. Delete an unused profile before adding another.');
      listBox.appendChild(note);
    }
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var f = { name: nameIn.value, grade: gradeSel.value, textbook: bookSel.value };
    var res = editing ? CC.update(editing, f) : CC.add(f);
    if (!res.ok) { showError(res.error); return; }
    if (!editing && window.cnmTrack) window.cnmTrack('child_added');
    resetForm();
    render();
  });
  cancelBtn.addEventListener('click', function () { resetForm(); render(); });

  function clearImport(keepFile) {
    fileRequest++;
    pendingBackup = null;
    pendingPreview = null;
    if (keepFile !== true) importFile.value = '';
    importPreview.hidden = true;
    importError.hidden = true;
    importStatus.hidden = true;
    confirmImport.disabled = true;
  }
  function showImportError(error) {
    importError.textContent = (error && error.message) || 'Import failed; profiles were not changed.';
    importError.hidden = false;
  }
  function previewBackup(backup) {
    var preview = CC.previewImport(backup);
    pendingBackup = backup;
    pendingPreview = preview;
    document.getElementById('import-summary').textContent =
      'Added ' + preview.addedChildren + ' children, matched ' + preview.matchedChildren + ' existing profiles; ' +
      'added ' + preview.addedRecords + ' records and updated ' + preview.updatedRecords + ' records.';
    var children = document.getElementById('import-children');
    children.textContent = '';
    preview.children.forEach(function (c) {
      var action = c.action === 'rename' ? 'Name conflict; rename to “' + c.name + '”' : c.action === 'merge' ? 'Merge into existing profile' : 'Add profile';
      children.appendChild(el('li', null, c.sourceName + ': ' + action + ' (' + c.records + ' records after merge)'));
    });
    importPreview.hidden = false;
    confirmImport.disabled = false;
  }
  importFile.addEventListener('change', function () {
    var file = importFile.files[0];
    clearImport(true);
    if (!file) return;
    var request = fileRequest;
    if (file.size > CC.MAX_BACKUP_BYTES) { importFile.value = ''; showImportError(new Error('Backup files cannot exceed 10 MB.')); return; }
    importStatus.textContent = 'Reading backup file…';
    importStatus.hidden = false;
    file.text().then(function (text) {
      if (request !== fileRequest) return;
      importStatus.hidden = true;
      previewBackup(CC.parseBackup(text));
    }).catch(function (error) {
      if (request !== fileRequest) return;
      importStatus.hidden = true;
      importFile.value = '';
      showImportError(error);
    });
  });
  document.getElementById('cancel-import').addEventListener('click', clearImport);
  confirmImport.addEventListener('click', function () {
    if (!pendingBackup || !pendingPreview) return;
    confirmImport.disabled = true;
    importError.hidden = true;
    try {
      var result = CC.importBackup(pendingBackup, pendingPreview.token);
      clearImport();
      resetForm();
      render();
      importStatus.textContent = 'Import complete: added ' + result.addedChildren + ' children, matched ' + result.matchedChildren +
        ' existing profiles, added ' + result.addedRecords + ' records, and updated ' + result.updatedRecords + ' records.';
      importStatus.hidden = false;
    } catch (error) {
      // Recalculate the preview after a failure so changes from another page cannot leave it stale.
      try { previewBackup(pendingBackup); }
      catch (previewError) { pendingPreview = null; importPreview.hidden = true; }
      showImportError(error);
    }
  });

  exportBtn.addEventListener('click', function () {
    var url = null;
    var link = null;
    try {
      var backup = CC.exportBackup();
      var blob = new Blob([JSON.stringify(backup, null, 2)], { type: 'application/json;charset=utf-8' });
      url = URL.createObjectURL(blob);
      link = el('a');
      link.href = url;
      link.download = 'children-backup-' + backup.exportedAt.replace(/[:.]/g, '-') + '.json';
      document.body.appendChild(link);
      link.click();
      exportStatus.className = 'small';
      exportStatus.textContent = 'Backup created. Check your browser downloads.';
    } catch (e) {
      exportStatus.className = 'small err';
      exportStatus.textContent = (e && e.message) || 'Export failed. Please try again.';
    } finally {
      if (link) link.remove();
      // Give the browser time to start the download before revoking the temporary URL.
      if (url) setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
      exportStatus.hidden = false;
    }
  });

  resetForm();
  render();
})();
