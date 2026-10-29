#!/usr/bin/env node
/* Whole-grade / full-textbook diagnostic demo: node scripts/demo_grade.js [一年级|七上] [limit] [seed]
 * Uses data/*.json to simulate a student who knows about 2/3 of the topics, is unsure of about 1/6, and does not know the rest, then prints chapter summaries. */
'use strict';
const fs = require('fs');
const path = require('path');
const E = require('../diagnose/engine.js');

const dir = path.join(__dirname, '..', 'data');
const read = (f) => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
const G = E.buildGraph(read('topics.json'), read('dependencies.json'), read('questions.json'));

// These Chinese scope tokens are required by E.gradeTargets in diagnose/engine.js.
const scope = process.argv[2] || '七年级';
const limit = process.argv[3] ? parseInt(process.argv[3], 10) : undefined;
const seed = process.argv[4] || 'demo';
const g = E.gradeTargets(G, scope);
if (!g) { console.error('Unknown scope: ' + scope + ' (use e.g. 一年级 / 七上)'); process.exit(1); }

const oracle = (id, attempt) => {
  const i = G.index[id];
  if (i % 6 === 0) return 'wrong';
  if (i % 6 === 3) return attempt === 1 ? 'wrong' : 'correct';
  return 'correct';
};

let s = E.createSession(G, g.ids, { mode: 'screen', limit, seed });
for (let n = 0; n < 1000; n++) {
  const it = E.nextItem(G, s);
  if (!it) break;
  s = E.applyAnswer(G, s, it.topicId, oracle(it.topicId, it.attempt));
}
const sum = E.summarize(G, s);
const name = (id) => G.byId[id].name;
console.log(g.label + ': ' + g.ids.length + ' topics; question limit ' + s.limit + '; asked ' + sum.asked + (sum.limitReached ? ' (limit reached)' : ' (complete)'));
console.log('Mastered ' + sum.mastered.length + ' / shaky ' + sum.shaky.length + ' / weak ' + sum.weak.length + ' / untested ' + sum.untested.length + '; root causes ' + sum.roots.length + '\n');
E.chapterSummary(G, s).forEach((c) => {
  console.log(c.label + '  Total ' + c.total + ': mastered ' + c.mastered + ' shaky ' + c.shaky + ' weak ' + c.weak + ' untested ' + c.untested +
    (c.weakIds.length ? '\n    Weak: ' + c.weakIds.map(name).join(', ') : ''));
});
