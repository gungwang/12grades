#!/usr/bin/env node
/* Child-profile backup and restore tests: node tests/test_children.js (no dependencies; does not access real browser storage). */
'use strict';
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const source = fs.readFileSync(path.join(__dirname, '../assets/children.js'), 'utf8');
const PROFILE_KEY = 'cnmChildren.v1';
const RECORD_KEY = 'cnmChildren.records.v1';
let passed = 0;

function test(name, fn) {
  fn();
  passed++;
  console.log('  ok   ' + name);
}

function load(entries, failKey, options = {}) {
  const storage = new Map(Object.entries(entries || {}));
  const writes = [];
  const context = {
    window: {},
    localStorage: {
      getItem(key) {
        if (key === failKey) throw new Error('Storage access denied');
        return storage.has(key) ? storage.get(key) : null;
      },
      setItem(key, value) {
        writes.push(key);
        if (options.failWrite && options.failWrite(key, value)) throw new Error('QuotaExceededError');
        storage.set(key, value);
      },
      removeItem(key) { storage.delete(key); }
    }
  };
  vm.runInNewContext(source, context, { filename: 'assets/children.js' });
  return { api: context.window.CnmChildren, storage, writes };
}

function exported(api) { return JSON.parse(JSON.stringify(api.exportBackup())); }
const profiles = {
  v: 1, current: 'child-b', children: [
    { id: 'child-a', name: 'Mia', grade: '三年级', textbook: '人教版', createdAt: '2026-10-01T00:00:00.000Z' },
    { id: 'child-b', name: 'Noah', grade: '五年级', textbook: '沪教版', createdAt: '2026-10-02T00:00:00.000Z' }
  ]
};
const records = {
  'child-a': ['math', 'chinese', 'english', 'physics'].map((subject, i) => ({
    key: subject + '|seed|target', subject, label: 'Test scope ' + i, mode: 'target', asked: 8,
    targets: ['topic-' + i], counts: { weak: 1, shaky: 1, mastered: 1, untested: 2 },
    weak: ['weak-' + i], roots: ['weak-' + i], shaky: ['shaky-' + i], mastered: ['mastered-' + i],
    savedAt: '2026-10-20T00:00:00.000Z', updatedAt: '2026-10-21T00:00:00.000Z'
  })),
  'child-b': [{ key: 'screen|seed|targets', subject: 'math', mode: 'screen', targets: null, weak: [], savedAt: '2026-10-20T00:00:00.000Z' }]
};
function fixture() {
  return { [PROFILE_KEY]: JSON.stringify(profiles), [RECORD_KEY]: JSON.stringify(records) };
}

test('Backup exports all profiles, the active child, four subject histories, version, and timestamp', () => {
  const { api } = load(fixture());
  const before = Date.now();
  const backup = exported(api);
  assert.equal(backup.format, '12grades.children');
  assert.equal(backup.version, 1);
  assert.ok(Date.parse(backup.exportedAt) >= before && Date.parse(backup.exportedAt) <= Date.now());
  assert.deepStrictEqual(backup.profiles, profiles);
  assert.deepStrictEqual(backup.records, records);
});

test('Export does not modify storage, the active child, or record timestamps', () => {
  const entries = fixture();
  const { api, storage, writes } = load(entries);
  api.exportBackup();
  assert.deepStrictEqual(Object.fromEntries(storage), entries);
  assert.deepStrictEqual(writes, []);
});

test('Preserves a null active child, unknown extension fields, and more than 40 stored records', () => {
  const entries = fixture();
  const extraProfiles = { ...profiles, current: null, futureMetadata: { note: 'preserved' } };
  const extraRecords = { 'child-a': Array.from({ length: 45 }, (_, i) => ({ key: 'record-' + i, extra: i })) };
  entries[PROFILE_KEY] = JSON.stringify(extraProfiles);
  entries[RECORD_KEY] = JSON.stringify(extraRecords);
  const backup = exported(load(entries).api);
  assert.deepStrictEqual(backup.profiles, extraProfiles);
  assert.deepStrictEqual(backup.records, extraRecords);
});

test('Exports profiles even when a child has no diagnostic records', () => {
  const backup = exported(load({ [PROFILE_KEY]: JSON.stringify(profiles) }).api);
  assert.deepStrictEqual(backup.profiles, profiles);
  assert.deepStrictEqual(backup.records, {});
});

test('Exports only profiles and history, not sessions, analytics, or other site storage', () => {
  const entries = { ...fixture(), unrelated: 'private', 'cnmDiagnose.session.v2': '{"seed":"x"}', 'cnmStats.v1': '{}' };
  const backup = exported(load(entries).api);
  assert.deepStrictEqual(Object.keys(backup).sort(), ['exportedAt', 'format', 'profiles', 'records', 'version']);
  assert.ok(!JSON.stringify(backup).includes('private'));
});

test('Each export reads current data; editing a snapshot does not alter stored profiles', () => {
  const { api, storage } = load(fixture());
  const backup = api.exportBackup();
  backup.profiles.children[0].name = 'Modified snapshot';
  backup.records['child-a'][0].weak.push('extra');
  assert.deepStrictEqual(exported(api).profiles, profiles);
  assert.deepStrictEqual(exported(api).records, records);
  const next = { ...profiles, current: 'child-a' };
  storage.set(PROFILE_KEY, JSON.stringify(next));
  assert.deepStrictEqual(exported(api).profiles, next);
});

test('Does not create an empty backup when there are no profiles', () => {
  assert.throws(() => load().api.exportBackup(), /no child profiles to export/);
  assert.throws(() => load({ [PROFILE_KEY]: '{"v":1,"current":null,"children":[]}' }).api.exportBackup(), /no child profiles to export/);
});

test('Reports storage read failures without falling back to empty data', () => {
  for (const key of [PROFILE_KEY, RECORD_KEY]) {
    const { api, writes } = load(fixture(), key);
    assert.throws(() => api.exportBackup(), /Could not read profile data/);
    assert.deepStrictEqual(writes, []);
  }
});

test('Rejects damaged JSON instead of creating a partial backup', () => {
  for (const key of [PROFILE_KEY, RECORD_KEY]) {
    assert.throws(() => load({ ...fixture(), [key]: '{broken' }).api.exportBackup(), /Could not read profile data/);
  }
});

test('Rejects malformed data structures rather than silently dropping profiles or history', () => {
  for (const value of [null, [], {}, { children: [null] }, { children: [{ id: '' }] }]) {
    assert.throws(() => load({ ...fixture(), [PROFILE_KEY]: JSON.stringify(value) }).api.exportBackup(), /invalid format/);
  }
  for (const value of [null, [], 'bad', { 'child-a': {} }]) {
    assert.throws(() => load({ ...fixture(), [RECORD_KEY]: JSON.stringify(value) }).api.exportBackup(), /invalid format/);
  }
});

function backup() { return exported(load(fixture()).api); }
function importInto(api, data) { return api.importBackup(data, api.previewImport(data).token); }
function stored(storage, key) { return JSON.parse(storage.get(key)); }

test('Restores profiles, the active child, and all four subject histories in a new browser; status summaries remain available', () => {
  const data = backup();
  const { api, storage } = load();
  const result = importInto(api, api.parseBackup(JSON.stringify(data)));
  assert.equal(result.addedChildren, 2);
  assert.equal(result.addedRecords, 5);
  assert.deepStrictEqual(stored(storage, PROFILE_KEY), profiles);
  assert.deepStrictEqual(stored(storage, RECORD_KEY), records);
  assert.equal(api.current().id, 'child-b');
  assert.equal(api.latestStatus('child-a', 'math')['weak-0'].status, 'weak');
  assert.equal(api.latestStatus('child-a', 'math')['weak-0'].root, true);
});

test('Preview and cancel do not write to local storage', () => {
  const { api, storage, writes } = load(fixture());
  const before = Object.fromEntries(storage);
  const preview = api.previewImport(backup());
  assert.equal(preview.matchedChildren, 2);
  assert.equal(preview.addedRecords, 0);
  assert.deepStrictEqual(writes, []);
  assert.deepStrictEqual(Object.fromEntries(storage), before);
});

test('Repeated import does not duplicate profiles or history or change original timestamps', () => {
  const { api, storage } = load(fixture());
  importInto(api, backup());
  const before = Object.fromEntries(storage);
  importInto(api, backup());
  assert.deepStrictEqual(Object.fromEntries(storage), before);
});

test('Merge preserves local data and active selection, keeps old records, adds new records, and selects the newer duplicate', () => {
  const localProfiles = { ...profiles, current: 'child-a', children: [{ ...profiles.children[0], grade: '六年级' }] };
  const localRecords = { 'child-a': [
    { ...records['child-a'][0], updatedAt: '2026-10-26T00:00:00.000Z', label: 'Newer local record' },
    { ...records['child-a'][1], updatedAt: '2026-10-19T00:00:00.000Z', label: 'Older local record' },
    { ...records['child-a'][0], key: 'local-only', label: 'Local-only record' }
  ] };
  const { api, storage } = load({ [PROFILE_KEY]: JSON.stringify(localProfiles), [RECORD_KEY]: JSON.stringify(localRecords) });
  const result = importInto(api, backup());
  const outProfiles = stored(storage, PROFILE_KEY);
  const outRecords = stored(storage, RECORD_KEY);
  assert.equal(outProfiles.current, 'child-a');
  assert.equal(outProfiles.children[0].grade, '六年级');
  assert.equal(outRecords['child-a'].length, 5);
  assert.equal(outRecords['child-a'].find(r => r.key === records['child-a'][0].key).label, 'Newer local record');
  assert.equal(outRecords['child-a'].find(r => r.key === records['child-a'][1].key).label, records['child-a'][1].label);
  assert.ok(outRecords['child-a'].find(r => r.key === 'local-only'));
  assert.equal(result.addedChildren, 1);
  assert.equal(result.updatedRecords, 1);
});

test('Merge keeps the local record when timestamps match', () => {
  const data = backup();
  data.records['child-a'][0].label = 'Different backup result';
  const { api, storage } = load(fixture());
  importInto(api, data);
  assert.equal(stored(storage, RECORD_KEY)['child-a'][0].label, records['child-a'][0].label);
});

test('Import preserves the explicit choice to save to no profile', () => {
  const entries = fixture();
  entries[PROFILE_KEY] = JSON.stringify({ ...profiles, current: null });
  const { api, storage } = load(entries);
  importInto(api, backup());
  assert.equal(stored(storage, PROFILE_KEY).current, null);
});

test('Same name with different IDs keeps both profiles and renames the incoming one; repeated imports still merge by ID', () => {
  const data = backup();
  data.profiles.children = [{ ...profiles.children[1], name: profiles.children[0].name }];
  data.records = { 'child-b': records['child-b'] };
  const entries = { [PROFILE_KEY]: JSON.stringify({ ...profiles, current: 'child-a', children: [profiles.children[0]] }) };
  const { api, storage } = load(entries);
  const preview = api.previewImport(data);
  assert.equal(preview.renamedChildren, 1);
  assert.equal(preview.children[0].name, 'Mia (Copy)');
  importInto(api, data);
  const first = Object.fromEntries(storage);
  importInto(api, data);
  assert.deepStrictEqual(Object.fromEntries(storage), first);
  assert.deepStrictEqual(stored(storage, PROFILE_KEY).children.map(c => c.id), ['child-a', 'child-b']);
});

test('Automatic renaming avoids names reserved by other incoming profiles and stays within the 12-character limit', () => {
  const name = 'ABCDEFGHIJKL';
  const data = backup();
  data.profiles.children[0].name = name;
  data.profiles.children[1].name = name.slice(0, 5) + ' (Copy)';
  const localProfiles = { ...profiles, current: 'local', children: [{ ...profiles.children[0], id: 'local', name }] };
  const { api } = load({ [PROFILE_KEY]: JSON.stringify(localProfiles) });
  const preview = api.previewImport(data);
  const names = preview.children.map(c => c.name);
  assert.ok(names[0].length <= 12);
  assert.notEqual(names[0], names[1]);
  assert.equal(names[1], data.profiles.children[1].name);
});

test('Rejects a merge of more than eight profiles without changing existing data', () => {
  const children = Array.from({ length: 8 }, (_, i) => ({ ...profiles.children[0], id: 'local-' + i, name: 'Child ' + i }));
  const entries = { [PROFILE_KEY]: JSON.stringify({ v: 1, current: null, children }) };
  const { api, storage, writes } = load(entries);
  assert.throws(() => api.previewImport(backup()), /exceed 8/);
  assert.deepStrictEqual(Object.fromEntries(storage), entries);
  assert.deepStrictEqual(writes, []);
});

test('Merge preserves 80 historical records; subsequent saves and moves do not truncate them', () => {
  const makeRecords = prefix => Array.from({ length: 40 }, (_, i) => ({ ...records['child-a'][0], key: prefix + i }));
  const data = backup();
  data.records['child-a'] = makeRecords('import-');
  const entries = { [PROFILE_KEY]: JSON.stringify(profiles), [RECORD_KEY]: JSON.stringify({ 'child-a': makeRecords('local-') }) };
  const { api, storage } = load(entries);
  importInto(api, data);
  assert.equal(stored(storage, RECORD_KEY)['child-a'].length, 80);
  api.saveRecord('child-a', { key: 'new-run', subject: 'math' });
  assert.equal(stored(storage, RECORD_KEY)['child-a'].length, 81);
  api.moveRecord(records['child-b'][0].key, 'child-b', 'child-a');
  assert.equal(stored(storage, RECORD_KEY)['child-a'].length, 82);
});

test('A normal profile still keeps only its most recent 40 diagnostic records', () => {
  const { api, storage } = load({ [PROFILE_KEY]: JSON.stringify(profiles) });
  for (let i = 0; i < 41; i++) api.saveRecord('child-a', { key: 'run-' + i, subject: 'math' });
  assert.equal(stored(storage, RECORD_KEY)['child-a'].length, 40);
});

test('Merge preserves extension fields and does not write sessions, settings, or analytics', () => {
  const data = backup();
  data.profiles.extension = { note: 'Extended profile data' };
  data.profiles.children[0].custom = { data: [1, 2] };
  data.records['child-a'][0].custom = 'Extended record';
  const { api, storage, writes } = load({ 'cnmDiagnose.session.v2': '{"seed":"local"}' });
  importInto(api, data);
  assert.deepStrictEqual(stored(storage, PROFILE_KEY), data.profiles);
  assert.deepStrictEqual(stored(storage, RECORD_KEY), data.records);
  assert.equal(storage.get('cnmDiagnose.session.v2'), '{"seed":"local"}');
  assert.deepStrictEqual(writes, [RECORD_KEY, PROFILE_KEY]);
});

test('Stops import if another page changes profiles after preview; requires a new preview', () => {
  const { api, storage, writes } = load(fixture());
  const data = backup();
  const preview = api.previewImport(data);
  storage.set(PROFILE_KEY, JSON.stringify({ ...profiles, current: 'child-a' }));
  assert.throws(() => api.importBackup(data, preview.token), /Local profiles have changed/);
  assert.equal(stored(storage, PROFILE_KEY).current, 'child-a');
  assert.deepStrictEqual(writes, []);
  importInto(api, data);
  assert.equal(stored(storage, PROFILE_KEY).current, 'child-a');
});

test('Import without preview cannot write the backup', () => {
  const { api, writes } = load(fixture());
  assert.throws(() => api.importBackup(backup()), /Preview the backup again/);
  assert.deepStrictEqual(writes, []);
});

test('Does not treat unreadable or damaged local storage as an empty browser', () => {
  for (const key of [PROFILE_KEY, RECORD_KEY]) {
    const { api, writes } = load(fixture(), key);
    assert.throws(() => api.previewImport(backup()), /Could not read local profiles/);
    assert.deepStrictEqual(writes, []);
    const broken = load({ ...fixture(), [key]: '{broken' });
    assert.throws(() => broken.api.previewImport(backup()), /Could not read local profiles/);
    assert.deepStrictEqual(broken.writes, []);
  }
});

test('First write failure leaves profiles and records unchanged', () => {
  const entries = fixture();
  const { api, storage } = load(entries, null, { failWrite: key => key === RECORD_KEY });
  assert.throws(() => importInto(api, backup()), /Existing profiles and records were not changed/);
  assert.deepStrictEqual(Object.fromEntries(storage), entries);
});

test('Second write failure restores original records and preserves their stored bytes', () => {
  const entries = fixture();
  entries[RECORD_KEY] = JSON.stringify(records, null, 2);
  const { api, storage } = load(entries, null, { failWrite: key => key === PROFILE_KEY });
  const data = backup(); data.records['child-a'][0].updatedAt = '2026-10-28T00:00:00.000Z';
  assert.throws(() => importInto(api, data), /Existing profiles and records were not changed/);
  assert.deepStrictEqual(Object.fromEntries(storage), entries);
});

test('Write failure in an empty browser rolls back to no storage keys', () => {
  const { api, storage } = load({}, null, { failWrite: key => key === PROFILE_KEY });
  assert.throws(() => importInto(api, backup()), /Existing profiles and records were not changed/);
  assert.equal(storage.size, 0);
});

test('If rollback also fails, reports a restore failure and does not claim success or unchanged data', () => {
  let calls = 0;
  const { api } = load(fixture(), null, { failWrite: () => ++calls > 1 });
  assert.throws(() => importInto(api, backup()), /could not be restored/);
});

test('Rejects invalid files, unknown versions, duplicate IDs, and orphan records', () => {
  const cases = [
    data => { data.format = 'diagnosis'; },
    data => { data.version = 2; },
    data => { data.profiles.v = 2; },
    data => { data.exportedAt = 'bad'; },
    data => { data.profiles.children[1].id = data.profiles.children[0].id; },
    data => { data.profiles.current = 'missing'; },
    data => { data.records.orphan = []; },
    data => { data.records['child-a'].push(data.records['child-a'][0]); },
    data => { data.records['child-a'][0].weak = 'wrong'; },
    data => { data.records['child-a'][0].counts.weak = -1; },
    data => { data.records['child-a'][0].savedAt = 'bad'; },
    data => { data.profiles.children[0].grade = 'Invalid grade'; }
  ];
  for (const mutate of cases) {
    const data = backup(); mutate(data);
    const { api, writes } = load(fixture());
    assert.throws(() => api.parseBackup(JSON.stringify(data)));
    assert.deepStrictEqual(writes, []);
  }
});

test('Rejects unsafe object keys and oversized files; accepts a UTF-8 BOM', () => {
  const { api } = load();
  const data = backup();
  const json = JSON.stringify(data);
  assert.equal(api.parseBackup('\uFEFF' + json).format, data.format);
  assert.throws(() => api.parseBackup('{broken'), /valid JSON/);
  assert.throws(() => api.parseBackup(' '.repeat(api.MAX_BACKUP_BYTES + 1)), /10 MB/);
  const unsafe = json.replace('"profiles":{', '"profiles":{"__proto__":{"polluted":true},');
  assert.throws(() => api.parseBackup(unsafe), /disallowed data field/);
  assert.equal({}.polluted, undefined);
});

console.log('\n' + passed + ' passed, 0 failed');
