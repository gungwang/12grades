#!/usr/bin/env node
/* Headless Chrome smoke test + screenshots (no dependencies; uses Node's built-in WebSocket to speak the Chrome DevTools Protocol directly).
 *
 *   node scripts/screenshot.js
 *
 * Starts a Python http.server and launches the system Chrome in headless mode.
 *   1) Open /diagnose/, choose a target, click “Don't know” twice (show question 2 → mark weak → trace prerequisites),
 *      refresh to verify saved progress, answer through the results page, export JSON, and generate a PDF.
 *      Then use fixed seeds to test automatic grading and explanation display for a choice question
 *      (select an option) and a numeric question (enter an answer); monitor console errors throughout.
 *   2) Use demo mode ?target=cnm_221&demo=1 (showing mastered / unstable / weak states) to capture
 *      screenshots/01-start.png, 02-question.png, 03-result.png, and 04-graph.png,
 *      plus 05-explanation.png after the explanation appears (1280×900).
 *   3) At widths 1280 and 375, check the home page and knowledge graphs
 *      (cnm_221 / cnm_p001 / cnm_ext_002 and root-path #cnm_219) for local graphs,
 *      horizontal overflow, and external script/style/font/image requests; capture 06–16.
 *   4) Capture graph ancestors for “All” (cnm_234: collapsed by grade by default, then expanded and centered
 *      on the current node), a long name at 375 px (cnm_124), and a 375 px diagnostic path graph; capture 17–20.
 *      Capture the home-page children's IQ test card as 36 and the results-page footer entry as 37.
 *      Capture the site-wide top banner at 1280 px as 41-top-banner.png and at 375 px as 42-top-banner-375.png.
 *      Save math (Grade 5, Book 1) and English (present continuous) diagnostic share images as
 *      38-share-math.png and 39-share-en.png; capture the 375 px share modal as 40-share-modal-375.png,
 *      and decode the QR code with jsQR.
 *      Capture the elementary English graph and Grade 4, Book 1 diagnosis as 32–35; middle-school English
 *      “present perfect” as 43–44; the full Grade 8, Book 1 English diagnosis as 45–46;
 *      high-school English “subjunctive mood” as 51–52; and the full Selective Required Course 1 English
 *      diagnosis as 53–54.
 * Environment variables: CHROME=/path/to/chrome  OUT=/path/to/output  PORT=8765  DEBUG_PORT=9333
 */
'use strict';
const { spawn } = require('child_process');
const WebSocket = globalThis.WebSocket || require('undici').WebSocket;
const fs = require('fs');
const os = require('os');
const path = require('path');
const http = require('http');
const zlib = require('zlib');
const E = require('../diagnose/engine.js');
const jsQR = require('./vendor/jsQR.js');
const SHARE_URL = 'https://math.pansgo.com/?from=share';

const ROOT = path.join(__dirname, '..');
const OUT = process.env.OUT || path.join(ROOT, 'screenshots');
const PORT = parseInt(process.env.PORT || '8765', 10);
const DEBUG_PORT = parseInt(process.env.DEBUG_PORT || '9333', 10);
const BASE = 'http://127.0.0.1:' + PORT;

// The engine is deterministic: use the same seed in Node to predict which question will appear in the browser.
const DATA = path.join(ROOT, 'data');
const readJson = (f) => JSON.parse(fs.readFileSync(path.join(DATA, f), 'utf8'));
const TOPIC_ROWS = readJson('topics.json');
const DEP_ROWS = readJson('dependencies.json');
const QUESTION_ROWS = readJson('questions.json');
const STD_ITEMS = readJson('cn-curriculum-standards.json').items;
const N_TOPICS = String(TOPIC_ROWS.filter((t) => String(t.id).startsWith('cnm_')).length);
const N_EDGES = String(DEP_ROWS.filter((d) => String(d.topicId).startsWith('cnm_')).length);
const N_QUESTIONS = String(QUESTION_ROWS.filter((q) => String(q.topicId).startsWith('cnm_')).length);
const N_STANDARDS = String(STD_ITEMS.filter((it) => String(it.id).startsWith('cms-')).length);
const N_GRADE_CARDS = 14;
// Topic names, assessment content, and canonical grade/semester tokens remain in Chinese until the source data is translated.
const TOP_BANNER_EXPR = `(() => {
  const a = document.querySelector('a.top-banner');
  if (!a) return 'missing';
  const rel = (a.getAttribute('rel') || '').split(/\\s+/);
  const text = (a.textContent || '').replace(/\\s+/g, ' ').trim();
  if (a.getAttribute('href') !== 'https://12grades.gungwang.com/?from=math-top') return 'href';
  if (a.target !== '_blank') return 'target';
  if (rel.indexOf('noopener') < 0) return 'rel';
  if (text !== '🧠 IQ Test for Kids') return 'text:' + text;
  const header = document.querySelector('.site-header');
  if (!header || (a.compareDocumentPosition(header) & Node.DOCUMENT_POSITION_PRECEDING)) return 'order';
  const ar = a.getBoundingClientRect();
  const hr = header.getBoundingClientRect();
  if (ar.top > 1) return 'not-top:' + Math.round(ar.top);
  if (ar.bottom > hr.top + 1) return 'overlap-nav';
  const cs = getComputedStyle(a);
  const lh = parseFloat(cs.lineHeight);
  const range = document.createRange();
  range.selectNodeContents(a);
  const rh = range.getBoundingClientRect().height;
  if (!(lh > 0) || rh > lh * 1.45) return 'wrap:' + Math.round(rh) + '/' + lh;
  const probe = document.createElement('span');
  probe.textContent = a.textContent;
  probe.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden;white-space:nowrap;font:' + cs.font;
  document.body.appendChild(probe);
  const textW = probe.getBoundingClientRect().width;
  probe.remove();
  const innerW = a.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
  if (textW > innerW + 1) return 'clip:' + Math.round(textW) + '/' + Math.round(innerW);
  const navLinks = document.querySelectorAll('.site-nav a');
  for (let i = 0; i < navLinks.length; i++) {
    if (navLinks[i].getBoundingClientRect().height + 0.5 < 44) return 'nav-short';
  }
  const card = document.querySelector('a.iq-card');
  if (card && card.getAttribute('href') !== 'https://12grades.gungwang.com/?from=math-home') return 'card-href';
  return 'ok';
})()`;
const IQ_HOME_EXPR = `(() => {
  const a = document.querySelector('a.iq-card');
  if (!a) return 'missing';
  const rel = (a.getAttribute('rel') || '').split(/\\s+/);
  const text = a.textContent || '';
  if (a.getAttribute('href') !== 'https://12grades.gungwang.com/?from=math-home') return 'href';
  if (a.target !== '_blank') return 'target';
  if (rel.indexOf('noopener') < 0) return 'rel';
  if (text.indexOf('IQ Test for Kids') < 0 || text.indexOf('Patterns · Complete the Picture · Spatial Reasoning') < 0 || text.indexOf('A fun assessment, separate from the math diagnostic') < 0) return 'text';
  if (/free|minutes?/i.test(text)) return 'promo';
  return 'ok';
})()`;
const IQ_RESULT_EXPR = `(() => {
  const line = document.getElementById('iq-line');
  const a = line && line.querySelector('a');
  if (!line || !a) return 'missing';
  const page = document.getElementById('root') && document.getElementById('root').lastElementChild;
  if (!page || page.lastElementChild !== line) return 'not-last';
  if (a.getAttribute('href') !== 'https://12grades.gungwang.com/?from=math-result') return 'href';
  if (a.target !== '_blank') return 'target';
  if ((a.getAttribute('rel') || '').split(/\\s+/).indexOf('noopener') < 0) return 'rel';
  const compact = (line.textContent || '').replace(/\\s+/g, '');
  if (compact !== 'Finishedthemathdiagnostic?TryanIQtestnext.→IQTestforKids') return 'text:' + compact;
  if (a.textContent !== 'IQ Test for Kids') return 'link-text';
  return 'ok';
})()`;
const DERIVE = TOPIC_ROWS.find((t) => t.id === 'cnm_h217' && t.grade === 13);
const GRAPH = E.buildGraph(readJson('topics.json'), readJson('dependencies.json'), readJson('questions.json'));
function seedFor(topicId, pred) {
  for (let i = 0; i < 60; i++) {
    const seed = 'smoke' + i;
    const it = E.nextItem(GRAPH, E.createSession(GRAPH, [topicId], { seed: seed, avoid: [] }));
    if (pred(it.question)) return { seed: seed, q: it.question };
  }
  throw new Error('No suitable seed found: ' + topicId);
}

function findChrome() {
  const cands = [process.env.CHROME,
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser'].filter(Boolean);
  const hit = cands.find((p) => fs.existsSync(p));
  if (!hit) throw new Error('Chrome/Chromium not found; set the CHROME environment variable');
  return hit;
}
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function pngInk(file, box) {
  const buf = fs.readFileSync(file);
  let off = 8, width = 0, height = 0, colorType = 0;
  const chunks = [];
  while (off + 8 <= buf.length) {
    const len = buf.readUInt32BE(off);
    const type = buf.toString('ascii', off + 4, off + 8);
    const data = buf.subarray(off + 8, off + 8 + len);
    if (type === 'IHDR') {
      width = data.readUInt32BE(0);
      height = data.readUInt32BE(4);
      colorType = data[9];
    } else if (type === 'IDAT') chunks.push(data);
    else if (type === 'IEND') break;
    off += 12 + len;
  }
  const bpp = colorType === 6 ? 4 : colorType === 2 ? 3 : 0;
  if (!bpp) throw new Error('Unable to parse screenshot color: ' + file);
  const raw = zlib.inflateSync(Buffer.concat(chunks));
  const stride = width * bpp;
  const x0 = box ? Math.max(0, box.x) : 0;
  const y0 = box ? Math.max(0, box.y) : 0;
  const x1 = box ? Math.min(width, box.x + box.w) : width;
  const y1 = box ? Math.min(height, box.y + box.h) : height;
  let pos = 0, orange = 0, blue = 0;
  let prev = Buffer.alloc(stride);
  for (let y = 0; y < height; y++) {
    const filter = raw[pos++];
    const row = Buffer.alloc(stride);
    for (let i = 0; i < stride; i++) {
      const x = raw[pos++];
      const a = i >= bpp ? row[i - bpp] : 0;
      const b = prev[i];
      const c = i >= bpp ? prev[i - bpp] : 0;
      let v = x;
      if (filter === 1) v = (x + a) & 255;
      else if (filter === 2) v = (x + b) & 255;
      else if (filter === 3) v = (x + ((a + b) >> 1)) & 255;
      else if (filter === 4) {
        const p = a + b - c;
        const pa = Math.abs(p - a), pb = Math.abs(p - b), pc = Math.abs(p - c);
        const pr = pa <= pb && pa <= pc ? a : pb <= pc ? b : c;
        v = (x + pr) & 255;
      }
      row[i] = v;
    }
    prev = row;
    if (y < y0 || y >= y1 || (y % 2)) continue;
    for (let x = x0; x < x1; x += 2) {
      const i = x * bpp;
      const r = row[i], g = row[i + 1], bch = row[i + 2];
      if (r > 180 && g > 60 && g < 190 && bch < 100) orange++;
      if (bch > 140 && bch > r + 40 && bch > g) blue++;
    }
  }
  return { width, height, orange, blue };
}

function pngDecode(file) {
  const buf = fs.readFileSync(file);
  if (buf.toString('ascii', 1, 4) !== 'PNG') throw new Error('Not a PNG: ' + file);
  let off = 8, width = 0, height = 0, bitDepth = 0, colorType = 0, interlace = 0;
  const idats = [];
  while (off + 8 <= buf.length) {
    const len = buf.readUInt32BE(off);
    const type = buf.toString('ascii', off + 4, off + 8);
    const data = buf.subarray(off + 8, off + 8 + len);
    if (type === 'IHDR') {
      width = data.readUInt32BE(0);
      height = data.readUInt32BE(4);
      bitDepth = data[8];
      colorType = data[9];
      interlace = data[12];
    } else if (type === 'IDAT') idats.push(data);
    else if (type === 'IEND') break;
    off += 12 + len;
  }
  if (bitDepth !== 8 || interlace !== 0 || (colorType !== 2 && colorType !== 6)) {
    throw new Error('Unable to decode PNG: ' + file + ' depth=' + bitDepth + ' color=' + colorType + ' interlace=' + interlace);
  }
  const bpp = colorType === 6 ? 4 : 3;
  const raw = zlib.inflateSync(Buffer.concat(idats));
  const stride = width * bpp;
  const rgba = new Uint8ClampedArray(width * height * 4);
  let pos = 0;
  let prev = Buffer.alloc(stride);
  for (let y = 0; y < height; y++) {
    const filter = raw[pos++];
    const row = Buffer.alloc(stride);
    for (let i = 0; i < stride; i++) {
      const x = raw[pos++];
      const a = i >= bpp ? row[i - bpp] : 0;
      const b = prev[i];
      const c = i >= bpp ? prev[i - bpp] : 0;
      let v = x;
      if (filter === 1) v = (x + a) & 255;
      else if (filter === 2) v = (x + b) & 255;
      else if (filter === 3) v = (x + ((a + b) >> 1)) & 255;
      else if (filter === 4) {
        const p = a + b - c;
        const pa = Math.abs(p - a), pb = Math.abs(p - b), pc = Math.abs(p - c);
        const pr = pa <= pb && pa <= pc ? a : pb <= pc ? b : c;
        v = (x + pr) & 255;
      }
      row[i] = v;
    }
    prev = row;
    for (let x = 0; x < width; x++) {
      const s = x * bpp;
      const d = (y * width + x) * 4;
      rgba[d] = row[s];
      rgba[d + 1] = row[s + 1];
      rgba[d + 2] = row[s + 2];
      rgba[d + 3] = bpp === 4 ? row[s + 3] : 255;
    }
  }
  return { width, height, data: rgba };
}
function pngRgba(file) { return pngDecode(file); }
function pngPixel(img, x, y) {
  const i = (y * img.width + x) * 4;
  return [img.data[i], img.data[i + 1], img.data[i + 2], img.data[i + 3]];
}
function cropRgba(img, box) {
  const x0 = Math.max(0, box.x), y0 = Math.max(0, box.y);
  const x1 = Math.min(img.width, box.x + box.w), y1 = Math.min(img.height, box.y + box.h);
  const w = x1 - x0, h = y1 - y0;
  const out = new Uint8ClampedArray(w * h * 4);
  for (let y = 0; y < h; y++) {
    const src = ((y0 + y) * img.width + x0) * 4;
    out.set(img.data.subarray(src, src + w * 4), y * w * 4);
  }
  return { width: w, height: h, data: out };
}
function decodeQr(img) {
  const boxes = [
    { x: 48, y: 1500, w: 400, h: 400 },
    { x: 0, y: img.height - 480, w: 560, h: 480 },
    { x: 0, y: 0, w: img.width, h: img.height }
  ];
  for (let i = 0; i < boxes.length; i++) {
    const crop = cropRgba(img, boxes[i]);
    const code = jsQR(crop.data, crop.width, crop.height, { inversionAttempts: 'dontInvert' });
    if (code && code.data) return code.data;
  }
  return null;
}

function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => { let b = ''; res.on('data', (c) => (b += c)); res.on('end', () => { try { resolve(JSON.parse(b)); } catch (e) { reject(e); } }); }).on('error', reject);
  });
}
async function waitFor(fn, what, ms) {
  const end = Date.now() + (ms || 15000);
  for (;;) {
    try { const v = await fn(); if (v) return v; } catch (e) { /* retry */ }
    if (Date.now() > end) throw new Error('Timed out waiting for: ' + what);
    await sleep(100);
  }
}

class CDP {
  constructor(ws) { this.ws = ws; this.id = 0; this.pending = new Map(); this.handlers = []; ws.addEventListener('message', (m) => this.onMessage(m.data)); }
  static async connect(url) {
    const ws = new WebSocket(url);
    await new Promise((res, rej) => { ws.addEventListener('open', res); ws.addEventListener('error', rej); });
    return new CDP(ws);
  }
  onMessage(data) {
    const msg = JSON.parse(data);
    if (msg.id && this.pending.has(msg.id)) {
      const { resolve, reject } = this.pending.get(msg.id);
      this.pending.delete(msg.id);
      if (msg.error) reject(new Error(msg.error.message)); else resolve(msg.result);
    } else if (msg.method) this.handlers.forEach((h) => h(msg));
  }
  send(method, params) {
    const id = ++this.id;
    this.ws.send(JSON.stringify({ id, method, params: params || {} }));
    return new Promise((resolve, reject) => this.pending.set(id, { resolve, reject }));
  }
  on(fn) { this.handlers.push(fn); }
}

async function main() {
  fs.mkdirSync(OUT, { recursive: true });
  const chromePath = findChrome();
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'cnm-chrome-'));
  const server = spawn(process.platform === 'win32' ? 'python' : 'python3', ['-m', 'http.server', String(PORT), '--bind', '127.0.0.1'], { cwd: ROOT, stdio: 'ignore' });
  const chrome = spawn(chromePath, [
    '--headless=new', '--remote-debugging-port=' + DEBUG_PORT, '--user-data-dir=' + profile,
    '--window-size=1280,900', '--hide-scrollbars', '--no-first-run', '--no-default-browser-check',
    '--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage',
    '--disable-background-networking', '--disable-sync', '--disable-default-apps', '--disable-extensions',
    '--disable-component-update', '--disable-domain-reliability', '--metrics-recording-only', '--no-pings',
    '--safebrowsing-disable-auto-update',
    '--disable-features=Translate,OptimizationHints,MediaRouter,DialMediaRouteProvider',
    'about:blank'
  ], { stdio: 'ignore' });
  const errors = [];
  const externalReqs = [];
  const checks = [];
  const check = (ok, msg) => { checks.push([ok, msg]); console.log((ok ? '  ok   ' : '  FAIL ') + msg); };
  let exitCode = 0;
  let dumpPage = null;
  try {
    await waitFor(() => getJson(BASE + '/diagnose/engine.js').then(() => true, () => fetchOk(BASE + '/diagnose/engine.js')), 'http.server');
    const targets = await waitFor(async () => { const l = await getJson('http://127.0.0.1:' + DEBUG_PORT + '/json/list'); return l.find((t) => t.type === 'page'); }, 'Chrome debugging port');
    const cdp = await CDP.connect(targets.webSocketDebuggerUrl);
    cdp.on((m) => {
      if (m.method === 'Runtime.exceptionThrown') errors.push('exception: ' + (m.params.exceptionDetails.exception && m.params.exceptionDetails.exception.description || m.params.exceptionDetails.text));
      if (m.method === 'Runtime.consoleAPICalled' && m.params.type === 'error') errors.push('console.error: ' + m.params.args.map((a) => a.value || a.description).join(' '));
      if (m.method === 'Log.entryAdded' && m.params.entry.level === 'error') errors.push('log: ' + m.params.entry.text + ' ' + (m.params.entry.url || ''));
      if (m.method === 'Network.responseReceived' && m.params.response.status >= 400) {
        const url = m.params.response.url;
        if (!/\/favicon\.ico(?:$|\?)/.test(url)) errors.push('http ' + m.params.response.status + ' ' + url);
      }
      if (m.method === 'Network.requestWillBeSent') noteExternal(m.params, externalReqs);
    });
    await Promise.all(['Runtime', 'Log', 'Page', 'Network'].map((d) => cdp.send(d + '.enable')));
    let viewW = 1280, viewH = 900;
    const setView = async (w, h) => {
      viewW = w; viewH = h;
      await cdp.send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: w < 700 });
      await sleep(80);
    };
    await setView(1280, 900);

    const evalJs = async (expr) => {
      const r = await cdp.send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true });
      if (r.exceptionDetails) throw new Error('Evaluation failed: ' + expr + ' → ' + JSON.stringify(r.exceptionDetails.exception && r.exceptionDetails.exception.description));
      return r.result.value;
    };
    const goto = async (url) => {
      await cdp.send('Page.navigate', { url });
      await waitFor(() => evalJs('document.readyState === "complete"'), 'load ' + url);
    };
    dumpPage = () => evalJs('document.body.innerText.slice(0, 1500)');
    const exists = (sel) => evalJs('!!document.querySelector(' + JSON.stringify(sel) + ')');
    const click = (sel) => evalJs('(() => { const e = document.querySelector(' + JSON.stringify(sel) + '); if (!e) throw new Error("no " + ' + JSON.stringify(sel) + '); e.click(); return true; })()');
    const shot = async (file, selector, clipH, opts) => {
      await sleep(300);
      // By default, capture the current viewport width starting at the page top; with a selector, start at that element's top (even beyond the viewport).
      // Large canvases render blank with captureBeyondViewport, so capture graphs inside the viewport from the viewport instead.
      const beyond = !opts || opts.beyond !== false;
      const y = selector ? await evalJs('Math.max(0, document.querySelector(' + JSON.stringify(selector) + ').getBoundingClientRect().top + window.scrollY - 12)') : 0;
      const r = await cdp.send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: beyond, clip: { x: 0, y: beyond ? y : 0, width: viewW, height: clipH || viewH, scale: 1 } });
      fs.writeFileSync(path.join(OUT, file), Buffer.from(r.data, 'base64'));
      console.log('  Screenshot screenshots/' + file);
    };
    const overflowOf = () => evalJs('(() => { const doc = document.documentElement; const sw = Math.max(doc.scrollWidth, document.body ? document.body.scrollWidth : 0); return { sw: sw, cw: doc.clientWidth, ok: sw <= doc.clientWidth + 1 }; })()');
    const assetsOf = () => evalJs(LOCAL_ASSET_EXPR);
    const checkPage = async (label) => {
      const ov = await overflowOf();
      check(ov.ok, label + ' has no horizontal overflow (scrollWidth ' + ov.sw + ' / clientWidth ' + ov.cw + ')');
      const bad = await assetsOf();
      check(bad.length === 0, label + ' has no external script/link/font/img requests' + (bad.length ? ': ' + bad.join('; ') : ''));
    };
    const checkBanner = async (label) => {
      const banner = await evalJs(TOP_BANNER_EXPR);
      check(banner === 'ok', label + ' top banner (' + banner + ')');
    };
    const NODE_METRICS_JS = `
      let tall = 0, spill = 0, uncut = 0, overlap = 0, primary = 0, junior = 0, senior = 0, grades = 0;
      const limit = window.matchMedia('(max-width: 700px)').matches ? 8 : 10;
      const boxes = [];
      cy.nodes().forEach(function (n) {
        if (n.hasClass('primary')) primary++;
        if (n.hasClass('junior')) junior++;
        if (n.hasClass('senior')) senior++;
        if (n.hasClass('grade')) grades++;
        if (n.height() > 40) tall++;
        const body = n.boundingBox({ includeLabels: false });
        const withL = n.boundingBox({ includeLabels: true });
        if (withL.w > body.w + 4 || withL.h > body.h + 4) spill++;
        const name = n.data('name') || '';
        const label = n.data('label') || '';
        if (Array.from(name).length > limit && !String(label).endsWith('…')) uncut++;
        if (Array.from(label).length > limit) uncut++;
        boxes.push(withL);
      });
      for (let i = 0; i < boxes.length; i++) {
        for (let j = i + 1; j < boxes.length; j++) {
          const a = boxes[i], b = boxes[j];
          if (a.x1 < b.x2 - 2 && a.x2 > b.x1 + 2 && a.y1 < b.y2 - 2 && a.y2 > b.y1 + 2) overlap++;
        }
      }
    `;
    const EXPLORE_GRAPH_EXPR = `(() => {
      const cy = window.__cy;
      const hard = cy.edges('.hard');
      const soft = cy.edges('.soft');
      ${NODE_METRICS_JS}
      return {
        nodes: cy.nodes().length, hash: location.hash,
        title: (document.querySelector('.detail-title') || {}).textContent || '',
        idCode: (document.querySelector('.id-code') || {}).textContent || '',
        meta: document.getElementById('graph-meta').textContent,
        diag: (document.querySelector('a.diag-btn') || {}).getAttribute ? document.querySelector('a.diag-btn').getAttribute('href') : '',
        alias: (document.querySelector('.alias-note') || {}).textContent || '',
        hard: hard.length ? hard[0].style('line-style') : '',
        soft: soft.length ? soft[0].style('line-style') : '',
        hardN: hard.length, softN: soft.length,
        current: cy.nodes('.current').length,
        primary, junior, senior, grades, tall, spill, uncut, overlap,
        wrap: cy.nodes().length ? cy.nodes()[0].style('text-wrap') : ''
      };
    })()`;
    const PATH_GRAPH_EXPR = `(() => {
      const cy = window.__pathCy;
      if (!cy) return null;
      ${NODE_METRICS_JS}
      const hard = cy.edges('.hard');
      const soft = cy.edges('.soft');
      const indirect = cy.edges('.indirect');
      return {
        nodes: cy.nodes().length, primary, junior, senior, grades, tall, spill, uncut, overlap,
        root: cy.nodes('.root').length,
        target: cy.nodes('.target').length,
        rootBorder: cy.nodes('.root').length ? cy.nodes('.root')[0].style('border-width') : '',
        hard: hard.length ? hard[0].style('line-style') : '',
        soft: soft.length ? soft[0].style('line-style') : '',
        indirect: indirect.length ? indirect[0].style('line-style') : '',
        hardN: hard.length, softN: soft.length, indirectN: indirect.length,
        pathItems: document.querySelectorAll('#path ol.path > li').length,
        svg: !!document.querySelector('svg.graph')
      };
    })()`;
    const checkPathGraph = async (label) => {
      await waitFor(() => evalJs('document.getElementById("path-cy") && document.getElementById("path-cy").dataset.ready === "1"'), label + ' path graph', 15000);
      const g = await evalJs(PATH_GRAPH_EXPR);
      check(!g.svg && g.nodes > 0 && g.pathItems > 0, label + ' has a Cytoscape path graph and a text path (' + g.nodes + ' nodes, ' + g.pathItems + ' steps)');
      check(g.primary + g.junior + g.senior === g.nodes, label + ' nodes are grouped by school level (elementary ' + g.primary + ', middle ' + g.junior + ', high ' + g.senior + ')');
      check(g.root >= 1 && parseFloat(g.rootBorder) >= 4, label + ' highlights weak root causes');
      check(g.target >= 1, label + ' marks the target');
      check(g.hardN === 0 || g.hard === 'solid', label + ' shows hard prerequisites as solid lines');
      check(g.softN === 0 || g.soft === 'dashed', label + ' shows soft prerequisites as dashed lines');
      check(g.indirectN === 0 || g.indirect === 'dotted', label + ' shows omitted edges as dotted lines');
      check(g.tall === 0 && g.spill === 0 && g.uncut === 0, label + ' truncates labels to one line (too tall ' + g.tall + ', overflow ' + g.spill + ', untruncated ' + g.uncut + ')');
      check(g.overlap === 0, label + ' has no overlapping nodes (' + g.overlap + ')');
      return g;
    };

    console.log('Smoke test');
    await goto(BASE + '/diagnose/');
    await evalJs('localStorage.clear()');
    await goto(BASE + '/diagnose/');
    await waitFor(() => exists('#target-list .topic-row'), 'start-page topic list');
    const rows = await evalJs('document.querySelectorAll("#target-list .topic-row").length');
    check(rows > 100, 'start page rendered the topic list (' + rows + ' rows)');
    check(await exists('.chap-head button.primary'), 'has a “Use entire chapter as target” button');
    check(await evalJs('document.querySelector("a.back").getAttribute("href")') === '../explore/', 'has a link back to the knowledge graph');
    await checkBanner('Diagnosis start page 1280');
    await checkPage('Diagnosis start page 1280');

    // Search for and select a target.
    await evalJs('(() => { const s = document.getElementById("search"); s.value = "Completing the Square"; s.dispatchEvent(new Event("input", {bubbles:true})); })()');
    const found = await evalJs('document.querySelectorAll("#target-list .topic-row").length');
    check(found >= 1 && found < 20, 'search for completing the square found ' + found + ' topics');
    await click('#target-list .topic-row button');
    await waitFor(() => exists('.q-text'), 'question page');
    check(true, 'can select a target and open the question page');
    check((await evalJs('document.querySelector(".q-title").textContent')).toLowerCase().includes('completing the square'), 'the first question is the target topic itself (completing the square)');

    // Question 1: click “Don't know” → show explanation and reference answer → next question; show question 2 for the same topic.
    check(await exists('.tag.diff-basic, .tag.diff-standard, .tag.diff-advanced'), 'question shows a difficulty tag');
    check(await exists('#btn-skip'), 'has a “Don’t know” button');
    await click('#btn-skip');
    await waitFor(() => exists('.refans'), 'reference answer after clicking “Don’t know”');
    check(await exists('#explain') && (await evalJs('document.querySelector("#explain").textContent')).includes('Explanation:'), 'shows the explanation and reference answer after “Don’t know”');
    await click('#btn-next');
    await waitFor(() => evalJs('document.querySelector(".q-text") && !document.querySelector(".refans")'), 'second question');
    const cardText2 = await evalJs('document.querySelector(".card").textContent');
    check(/Question 2 \//.test(cardText2) && cardText2.includes('Topic question 2 / 3') && (await evalJs('document.querySelector(".q-title").textContent')).toLowerCase().includes('completing the square'),
      'after missing question 1, question 2 is another question on the same topic');
    await click('#btn-skip');
    await click('#btn-next');
    await waitFor(() => evalJs('document.querySelector(".q-text") && !document.querySelector(".refans")'), 'prerequisite review');
    const cardText3 = await evalJs('document.querySelector(".card").textContent');
    check(/Question 3 \//.test(cardText3) && !(await evalJs('document.querySelector(".q-title").textContent')).toLowerCase().includes('completing the square') && cardText3.includes('Topic question 1 / 3'),
      'after missing both questions, the topic is marked weak and review returns to a prerequisite (question 3 covers another topic)');
    const saved = await evalJs('JSON.parse(localStorage.getItem("cnmDiagnose.session.v2")).answers.length');
    check(saved === 2, 'progress was saved to localStorage (answers=' + saved + ')');
    check(await evalJs('JSON.parse(localStorage.getItem("cnmDiagnose.seen.v1")).length') === 2, 'IDs of seen questions were saved to localStorage (2 questions)');

    // Continue after a refresh.
    await goto(BASE + '/diagnose/');
    await waitFor(() => exists('.banner button.primary'), 'resume-progress banner');
    await click('.banner button.primary');
    await waitFor(() => exists('.q-text'), 'question page after resuming');
    check(/Question 3 \//.test(await evalJs('document.querySelector(".card").textContent')), 'clicking “Continue” after refresh resumes at question 3');

    // Click “Don't know” through to the results page.
    for (let i = 0; i < 40; i++) {
      if (await exists('#summary')) break;
      if (await exists('#btn-skip')) await click('#btn-skip');
      await waitFor(() => exists('#btn-next'), 'next-question button');
      await click('#btn-next');
      await sleep(30);
    }
    await waitFor(() => exists('#summary'), 'results page');
    check(await exists('#roots') && await exists('#path') && await exists('#shaky') && await exists('ol.path'), 'results page includes root causes, unstable topics, and a text learning path');
    await checkPathGraph('results page');
    const asked = await evalJs('document.querySelectorAll("#log tbody tr").length');
    check(asked > 2 && asked <= 16, 'question count is within the limit of 16 (' + asked + ' asked)');
    check((await evalJs('document.querySelectorAll("#roots details.topic").length')) >= 1, 'at least one weak root cause can be expanded');
    check((await evalJs('document.querySelectorAll("#standards .std").length')) >= 1, 'related curriculum standards are listed with source text');
    await click('#btn-export');
    check(true, 'clicking “Export JSON” produced no error');
    const pdf = await cdp.send('Page.printToPDF', { printBackground: true });
    check(pdf.data.length > 1000, 'printed to PDF successfully (' + Math.round(pdf.data.length * 0.75 / 1024) + ' KB)');
    // Change an answer.
    await evalJs('(() => { const sel = document.querySelector("#log select"); sel.value = "correct"; sel.dispatchEvent(new Event("change", {bubbles:true})); })()');
    await sleep(200);
    check(await exists('#summary') || await exists('.q-text'), 'page recalculates normally after changing an answer');
    // Choice question: use a fixed seed, select an option, submit, and verify automatic grading and explanation.
    console.log('Choice / numeric questions');
    const ch = seedFor('cnm_221', (q) => q.type === 'choice');
    await goto(BASE + '/diagnose/');
    await evalJs('localStorage.clear()');
    await goto(BASE + '/diagnose/?target=cnm_221&seed=' + ch.seed);
    await waitFor(() => exists('#choices'), 'choice question page');
    check((await evalJs('document.querySelector("#q-text").textContent')) === ch.q.prompt, 'fixed seed produced the expected question (' + ch.q.id + ')');
    check((await evalJs('document.querySelectorAll("#choices .choice").length')) === ch.q.choices.length, 'rendered ' + ch.q.choices.length + ' choices');
    const wrongKey = ch.q.choices.find((c) => c.key !== ch.q.answer).key;
    await click('#choice-' + wrongKey);
    await click('#btn-submit');
    await waitFor(() => exists('.verdict'), 'choice grading');
    check((await evalJs('document.querySelector(".verdict").textContent')).includes('Incorrect'), 'an incorrect choice is marked incorrect');
    check((await evalJs('document.querySelector("#explain").textContent')).includes(ch.q.explanation), 'the explanation is shown after automatic grading');
    check((await evalJs('document.querySelector(".refans").textContent')).includes(ch.q.answer + '.'), 'the reference answer is shown, including its choice text');
    await click('#btn-flip');
    // By default, a topic requires 3 consecutive correct answers to be mastered; correcting the result should continue to the next question for that topic.
    await waitFor(() => evalJs('!!document.querySelector(".q-text") && !document.querySelector("#summary")'), 'continue to the next question for this topic after correcting the result');
    check((await evalJs('JSON.parse(localStorage.getItem("cnmDiagnose.session.v2")).answers[0].result')) === 'correct', 'the “I was marked wrong, but I actually got it right” action can change the result to correct');
    check((await evalJs('Array.from(document.querySelectorAll(".tag")).some(e => /Topic question 2 \\/ 3/.test(e.textContent))')), 'correcting the result advances to question 2 for the same topic');

    // Find a numeric question whose answer is a fraction or negative number, then answer using full-width digits.
    let nu = null, nuTopic = null;
    for (const t of GRAPH.topics) {
      if (t.external) continue;
      try { nu = seedFor(t.id, (q) => q.type === 'numeric' && /^-?\d+\/\d+$|^-\d+$/.test(q.answer)); nuTopic = t.id; break; } catch (e) { /* try another topic */ }
    }
    await goto(BASE + '/diagnose/');
    await evalJs('localStorage.clear()');
    await goto(BASE + '/diagnose/?target=' + nuTopic + '&seed=' + nu.seed);
    await waitFor(() => exists('#ans'), 'numeric question page');
    const typed = nu.q.answer;
    await evalJs('(() => { const i = document.getElementById("ans"); i.value = ' + JSON.stringify(typed.replace(/[0-9]/g, (d) => String.fromCharCode(d.charCodeAt(0) + 0xFEE0)).replace('-', '－').replace('/', '／')) + '; i.dispatchEvent(new Event("input", {bubbles:true})); })()');
    await click('#btn-submit');
    await waitFor(() => exists('.verdict'), 'automatic grading of numeric question');
    check((await evalJs('document.querySelector(".verdict").textContent')).includes('Correct'), 'automatic grading accepts the full-width form “' + typed + '” (' + nu.q.id + ')');
    await shot('05-explanation.png');

    // Screenshots (demo mode)
    console.log('Screenshots');
    await goto(BASE + '/diagnose/');
    await evalJs('localStorage.clear()');
    await goto(BASE + '/diagnose/');
    await waitFor(() => exists('#target-list .topic-row'), 'start page');
    await shot('01-start.png');
    await goto(BASE + '/diagnose/?target=cnm_221&demo=1&step=2');
    await waitFor(() => exists('.q-text'), 'demo question page');
    await shot('02-question.png');
    await goto(BASE + '/diagnose/?target=cnm_221&demo=1');
    await waitFor(() => exists('#summary'), 'demo results page');
    check(await exists('#roots details.topic'), 'demo mode reaches the results page with a root cause');
    const stat = (cls) => evalJs('parseInt(document.querySelector("#summary .stat.' + cls + ' b").textContent, 10)');
    check((await stat('ok')) > 0 && (await stat('shaky')) > 0 && (await stat('bad')) > 0,
      'demo mode shows all three states: mastered (' + await stat('ok') + '), unstable (' + await stat('shaky') + '), and weak (' + await stat('bad') + ')');
    check(await exists('#shaky details.topic') && await exists('#path .tag.shaky'), 'unstable topics are listed separately and included in the learning path');
    await shot('03-result.png');
    const iqResult = await evalJs(IQ_RESULT_EXPR);
    check(iqResult === 'ok', 'the results-page footer has a children’s IQ test entry (' + iqResult + ')');
    await shot('37-result-iq.png', '#iq-line', 160);
    await checkPathGraph('demo results page');
    // Save the path graph separately for easier inspection.
    await shot('04-graph.png', '#graph', 720);

    // Whole-chapter target (URL parameter chapter) and automatic grading of a numeric question.
    await goto(BASE + '/diagnose/?chapter=' + encodeURIComponent('七上 Chapter 1') + '&demo=1');
    await waitFor(() => exists('#summary'), 'whole-chapter demo results page');
    check((await evalJs('document.querySelector("#summary h2").textContent')).includes('entire chapter'), 'a whole chapter can be diagnosed as a target (?chapter=Grade 7, Semester 1 Chapter 1)');

    console.log('Home page / knowledge graph');
    await setView(1280, 900);
    await goto(BASE + '/');
    await waitFor(() => evalJs('document.getElementById("n-topics") && document.getElementById("n-topics").textContent !== "…" && document.querySelectorAll("a.grade-card").length === ' + N_GRADE_CARDS), 'home-page statistics');
    const stats = await evalJs('[document.getElementById("n-topics").textContent, document.getElementById("n-edges").textContent, document.getElementById("n-questions").textContent, document.getElementById("n-standards").textContent].join(",")');
    check(stats === [N_TOPICS, N_EDGES, N_QUESTIONS, N_STANDARDS].join(','), 'home-page statistics come from data files (' + stats + ')');
    check(!/not reviewed|teacher review/i.test(await evalJs('document.body.innerText')) && !/draft/i.test(await evalJs('document.title')), 'the footer has no draft disclaimer and the title contains no “draft” label');
    check((await evalJs('document.querySelector("a.grade-card").getAttribute("href")')) === 'explore/?grade=1', 'the Grade 1 card links to the knowledge graph');
    const iqHome = await evalJs(IQ_HOME_EXPR);
    check(iqHome === 'ok', 'home-page children’s IQ test card (' + iqHome + ')');
    await checkBanner('Home page 1280');
    await checkPage('Home page 1280');
    await shot('06-home.png', null, 1900);
    await shot('36-home-iq.png', 'a.iq-card', 280);
    await shot('41-top-banner.png', null, 280);

    const checkExplore = async (id, expect) => {
      await goto(BASE + '/explore/#' + encodeURIComponent(id));
      await waitFor(() => evalJs('document.getElementById("cy") && document.getElementById("cy").dataset.ready === "1"'), 'local graph ' + id, 20000);
      const info = await evalJs(EXPLORE_GRAPH_EXPR);
      check(info.ready !== 'err' && info.nodes > 1 && info.nodes < 80, id + ' rendered ' + info.nodes + ' nodes in its local graph (not the full graph of ' + N_TOPICS + ')');
      check(info.primary + info.junior + info.senior === info.nodes, id + ' colors nodes by school level (elementary ' + info.primary + ', middle ' + info.junior + ', high ' + info.senior + ')');
      check(info.meta.indexOf('Upstream: 2 levels') >= 0, id + ' graph note includes “up 2 levels” (' + info.meta + ')');
      check(info.hash === '#' + id, id + ' preserves its URL hash (' + info.hash + ')');
      check(info.title.indexOf(expect.title) >= 0 && info.idCode === expect.idCode, id + ' details show “' + info.title + '” (' + info.idCode + ')');
      check(info.diag.indexOf('target=' + encodeURIComponent(expect.diag)) >= 0, id + ' diagnosis button points to ' + expect.diag);
      check(info.current === 1, id + ' highlights the current node');
      if (expect.alias) check(info.alias.indexOf(expect.alias) >= 0 && info.alias.indexOf(id) >= 0, id + ' displays the old-ID note');
      if (info.hardN) check(info.hard === 'solid', id + ' draws hard prerequisites as solid lines');
      if (info.softN) check(info.soft === 'dashed', id + ' draws soft prerequisites as dashed lines (' + info.softN + ' edges)');
      check(info.wrap === 'ellipsis' && info.tall === 0 && info.spill === 0 && info.uncut === 0 && info.overlap === 0,
        id + ' truncates labels to one line without overlap (untruncated ' + info.uncut + ', overflow ' + info.spill + ', overlap ' + info.overlap + ', too tall ' + info.tall + ')');
      await checkPage('Graph ' + id + ' ' + viewW);
      return info;
    };

    await checkExplore('cnm_221', { title: 'Completing the Square', idCode: 'cnm_221', diag: 'cnm_221' });
    await checkBanner('Graph 1280');
    await shot('07-explore-221.png');
    await checkExplore('cnm_p001', { title: 'Understanding numbers 1 to 5', idCode: 'cnm_p001', diag: 'cnm_p001' });
    await shot('08-explore-p001.png');
    await checkExplore('cnm_ext_002', { title: 'Meaning of Fractions', idCode: 'cnm_p165', diag: 'cnm_p165', alias: 'Meaning of Fractions and Fraction Operations' });
    await shot('09-explore-ext002.png');

    await goto(BASE + '/#cnm_219');
    await waitFor(() => evalJs('location.pathname.indexOf("/explore/") >= 0 && location.hash === "#cnm_219" && document.getElementById("cy") && document.getElementById("cy").dataset.ready === "1"'), 'root path #cnm_219', 20000);
    check((await evalJs('(document.querySelector(".id-code") || {}).textContent')) === 'cnm_219', 'root path #cnm_219 still points to this topic');
    await checkPage('Root path #cnm_219');
    await shot('16-explore-219.png');

    console.log('All ancestors');
    await goto(BASE + '/explore/#cnm_234');
    await waitFor(() => evalJs('document.getElementById("cy") && document.getElementById("cy").dataset.ready === "1"'), 'cnm_234 local graph', 20000);
    await click('#depth-switch [data-depth="all"]');
    await waitFor(() => evalJs('document.getElementById("cy") && document.getElementById("cy").dataset.ready === "1" && document.getElementById("cy").dataset.mode === "grade"'), 'all ancestors collapsed', 20000);
    const folded = await evalJs(EXPLORE_GRAPH_EXPR);
    const foldTotal = await evalJs('document.getElementById("cy").dataset.total');
    const foldBtn = await evalJs('(document.getElementById("btn-expand-all") || {}).textContent || ""');
    check(Number(foldTotal) > 40 && folded.nodes <= 40 && folded.nodes > 1, 'all ancestors are collapsed by default (showing ' + folded.nodes + ' / ' + foldTotal + ')');
    check(folded.grades >= 2 && folded.primary > 0 && folded.junior > 0, 'collapsed graph is grouped by grade and includes elementary and middle school (grade nodes ' + folded.grades + ')');
    check(foldBtn === foldTotal + ' total · Expand all', 'collapsed-state expand prompt matches "' + foldBtn + '"');
    check(folded.wrap === 'ellipsis' && folded.overlap === 0 && folded.spill === 0, 'collapsed graph labels do not overlap');
    if (folded.hardN) check(folded.hard === 'solid', 'collapsed graph shows hard prerequisites as solid lines');
    if (folded.softN) check(folded.soft === 'dashed', 'collapsed graph shows soft prerequisites as dashed lines');
    await checkPage('All ancestors collapsed');
    await shot('17-explore-all.png');
    const expandStarted = Date.now();
    await click('#btn-expand-all');
    await waitFor(() => evalJs('document.getElementById("cy") && document.getElementById("cy").dataset.ready === "1" && document.getElementById("cy").dataset.mode === "full"'), 'all ancestors expanded', 20000);
    const expandMs = Date.now() - expandStarted;
    const opened = await evalJs(EXPLORE_GRAPH_EXPR);
    check(opened.nodes === Number(foldTotal) && opened.nodes > 40, 'expanded graph shows all ' + opened.nodes + ' topics');
    check(expandMs < 8000, 'expanded layout took ' + expandMs + ' ms');
    check(opened.overlap === 0 && opened.spill === 0 && opened.tall === 0, 'expanded nodes do not overlap and labels do not overflow');
    check((opened.meta || '').indexOf('Centered on the current topic') >= 0, 'the expanded graph note confirms it is centered on the current topic');
    const visible = await evalJs('(() => { const cy = window.__cy; const node = cy.getElementById("cnm_234"); const r = node.renderedBoundingBox(); const w = cy.width(), h = cy.height(); let colored = 0; document.querySelectorAll("#cy canvas").forEach(function (c) { const ctx = c.getContext("2d"); if (!ctx || !c.width || !c.height) return; const data = ctx.getImageData(0, 0, c.width, c.height).data; const step = 4; for (let y = 0; y < c.height; y += step) { for (let x = 0; x < c.width; x += step) { const i = (y * c.width + x) * 4; const R = data[i], G = data[i + 1], B = data[i + 2], A = data[i + 3]; if (A > 20 && (R < 240 || G < 240 || B < 240)) colored++; } } }); return { h: Math.round(r.h), w: Math.round(r.w), colored: colored, zoom: cy.zoom(), inside: r.x2 > 8 && r.x1 < w - 8 && r.y2 > 8 && r.y1 < h - 8 }; })()');
    check(visible.inside && visible.h >= 24 && visible.colored > 80, 'the current node is readable and the expanded canvas has content (height ' + visible.h + ', colored samples ' + visible.colored + ', zoom ' + visible.zoom.toFixed(2) + ')');
    const cyBox = await evalJs('(() => { const r = document.getElementById("cy").getBoundingClientRect(); return { x: Math.max(0, Math.floor(r.x)), y: Math.max(0, Math.floor(r.y)), w: Math.round(r.width), h: Math.round(r.height) }; })()');
    await shot('18-explore-all-open.png', null, null, { beyond: false });
    const ink = pngInk(path.join(OUT, '18-explore-all-open.png'), cyBox);
    check(ink.orange > 40 && ink.blue > 40, 'nodes are visible in the expanded screenshot (blue ' + ink.blue + ', orange ' + ink.orange + ', region ' + cyBox.x + ',' + cyBox.y + ' ' + cyBox.w + '×' + cyBox.h + ')');
    const zoomBefore = await evalJs('window.__cy.zoom()');
    await click('#btn-zoom-in');
    const zoomAfter = await evalJs('window.__cy.zoom()');
    check(zoomAfter > zoomBefore, 'the expanded graph remains zoomable (' + zoomBefore.toFixed(3) + ' → ' + zoomAfter.toFixed(3) + ')');
    await click('#btn-fit');
    const fitted = await evalJs('(() => { const cy = window.__cy; const r = cy.getElementById("cnm_234").renderedBoundingBox(); return { zoom: cy.zoom(), h: r.h }; })()');
    check(fitted.zoom >= 0.45 && fitted.h >= 12, 'the node does not shrink to a dot after fitting (' + fitted.zoom.toFixed(3) + ' zoom, height ' + Math.round(fitted.h) + ')');
    await evalJs('sessionStorage.setItem("cnmExplore.depth","2")');

    console.log('Narrow screen 375');
    await setView(375, 812);
    await goto(BASE + '/');
    await waitFor(() => evalJs('document.getElementById("n-topics") && document.getElementById("n-topics").textContent === ' + JSON.stringify(N_TOPICS)), 'Home page 375');
    check((await evalJs(IQ_HOME_EXPR)) === 'ok', 'children’s IQ test card on home page at 375 px');
    await checkBanner('Home page 375');
    await checkPage('Home page 375');
    await shot('10-home-375.png', null, 2900);
    await shot('42-top-banner-375.png', null, 420);
    await checkExplore('cnm_221', { title: 'Completing the Square', idCode: 'cnm_221', diag: 'cnm_221' });
    await checkBanner('Graph 375');
    await shot('11-explore-221-375.png', null, 1100);
    await checkExplore('cnm_p001', { title: 'Understanding numbers 1 to 5', idCode: 'cnm_p001', diag: 'cnm_p001' });
    await shot('12-explore-p001-375.png', null, 1100);
    await checkExplore('cnm_ext_002', { title: 'Meaning of Fractions', idCode: 'cnm_p165', diag: 'cnm_p165', alias: 'Meaning of Fractions and Fraction Operations' });
    await shot('13-explore-ext002-375.png', null, 1100);
    await evalJs('sessionStorage.setItem("cnmExplore.depth","2")');
    await goto(BASE + '/explore/#cnm_124');
    await waitFor(() => evalJs('document.getElementById("cy") && document.getElementById("cy").dataset.ready === "1" && document.querySelector(".id-code") && document.querySelector(".id-code").textContent === "cnm_124"'), 'long name 375', 20000);
    const longName = 'Triangle Congruence: Angle-Side-Angle (ASA) and Angle-Angle-Side (AAS)';
    const longInfo = await evalJs('(() => { const cy = window.__cy; const node = cy.getElementById("cnm_124"); node.emit("mouseover"); const tip = document.getElementById("node-tip"); const base = ' + EXPLORE_GRAPH_EXPR + '; return Object.assign(base, { tip: tip && !tip.hidden ? tip.textContent : "", label: node.data("label"), name: node.data("name"), hidden: !tip || tip.hidden }); })()');
    check(longInfo.name === longName && longInfo.tip === longName, 'full name appears on hover at 375 px (' + longInfo.tip + ')');
    check(Array.from(longInfo.label).length <= 8 && longInfo.label.endsWith('…'), 'long name is truncated at 375 px (' + longInfo.label + ')');
    check(longInfo.spill === 0 && longInfo.overlap === 0 && longInfo.tall === 0, 'long name does not wrap, overflow, or overlap at 375 px');
    await checkPage('Long name 375');
    await shot('19-longname-375.png', '.graph-pane', 760);
    await goto(BASE + '/diagnose/?target=cnm_221&demo=1');
    await waitFor(() => exists('#summary'), 'diagnosis results page 375');
    check((await evalJs(IQ_RESULT_EXPR)) === 'ok', 'diagnosis results page footer has a children’s IQ test entry at 375 px');
    await checkBanner('Diagnosis results 375');
    await checkPathGraph('375 results page');
    const choiceH = await evalJs('(() => { const b = document.querySelector("button"); return b ? b.getBoundingClientRect().height : 0; })()');
    check(choiceH >= 44, 'button touch target is at least 44 px high (' + Math.round(choiceH) + ')');
    await checkPage('Diagnosis results 375');
    await shot('14-diagnose-375.png', null, 1100);
    await shot('20-diagnose-graph-375.png', '#graph', 720);
    await goto(BASE + '/diagnose/');
    await evalJs('localStorage.clear()');
    await goto(BASE + '/diagnose/');
    await waitFor(() => exists('#search'), 'diagnosis start page 375');
    await checkPage('Diagnosis start page 375');
    await shot('15-start-375.png', null, 900);

    console.log('High school');
    await setView(1280, 900);
    const hsInfo = await checkExplore('cnm_h027', { title: 'Function Concepts', idCode: 'cnm_h027', diag: 'cnm_h027' });
    check(hsInfo.senior > 0 && hsInfo.junior > 0, 'the high-school “Function Concepts” local graph also includes middle-school nodes');
    check(await evalJs('!!document.querySelector(".legend .sw-h")'), 'knowledge graph legend includes high school');
    check((await evalJs('document.querySelector(".pill").textContent')) === 'High School', 'the detail panel labels the school level as high school');
    await shot('21-explore-h027.png');
    await goto(BASE + '/diagnose/?target=cnm_h027&demo=1');
    await waitFor(() => exists('#summary'), 'high-school function-concepts results');
    const hsPath = await checkPathGraph('high-school function concepts');
    check(hsPath.senior > 0 && hsPath.junior > 0, 'high-school diagnosis path includes high- and middle-school nodes');
    check(await evalJs('!!document.querySelector(".legend .sw-h")'), 'diagnosis legend includes high school');
    await shot('23-diagnose-h027.png', null, 1400);
    await shot('24-diagnose-h027-graph.png', '#graph', 720);
    await goto(BASE + '/diagnose/?grade=' + encodeURIComponent('高一') + '&demo=1&limit=12');
    await waitFor(() => exists('#chapters'), 'Grade 10 overall diagnosis', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).includes('High School Year 1'), 'Grade 10 (Required Course Book 1) overall diagnosis');
    check(await exists('#chapters .chap-sum'), 'Grade 10 overall diagnosis has chapter summaries');
    await checkPage('Grade 10 overall diagnosis 1280');
    await shot('25-diagnose-gaoyi.png', '#summary', 900);
    await setView(375, 812);
    await checkExplore('cnm_h027', { title: 'Function Concepts', idCode: 'cnm_h027', diag: 'cnm_h027' });
    await shot('22-explore-h027-375.png', null, 1100);
    await goto(BASE + '/diagnose/?target=cnm_h027&demo=1');
    await waitFor(() => exists('#summary'), 'high-school diagnosis results 375');
    await checkPathGraph('high-school function concepts 375');
    await checkPage('High-school diagnosis 375');
    await shot('26-diagnose-h027-375.png', null, 1100);
    await evalJs('localStorage.clear()');
    await goto(BASE + '/diagnose/');
    await waitFor(() => exists('#grade-card'), 'diagnosis start-page grade card');
    await evalJs('(() => { const b = Array.from(document.querySelectorAll("#grade-card .stage-tab")).find((x) => x.textContent === "High School Year 2"); if (!b) throw new Error("Grade 11 tab not found"); b.click(); })()');
    check((await evalJs('document.getElementById("grade-info").textContent')).indexOf('High School Year 2 · Required Volume 2') >= 0, 'Grade 11 card shows Required Course Book 2');
    check(await evalJs('!Array.from(document.querySelectorAll("#grade-card .stage-tab")).some((b) => b.textContent === "Semester 1" || b.textContent === "Semester 2")'), 'high-school overall diagnosis does not offer semester books');
    await checkPage('Grade 11 diagnosis start 375');
    await shot('27-diagnose-gaoer-375.png', '#grade-card', 520);

    console.log('Selective required courses');
    if (!DERIVE) throw new Error('Topic "Definition of a Derivative" not found');
    await setView(1280, 900);
    const derInfo = await checkExplore(DERIVE.id, { title: 'Definition of a Derivative', idCode: DERIVE.id, diag: DERIVE.id });
    check(derInfo.senior > 0, 'the “Derivative Concepts” local graph includes high-school nodes');
    check((await evalJs('document.body.innerText')).indexOf('Selective 2 · Selective Required Volume 2') >= 0, 'derivative page identifies Selective Required Course 2');
    await shot('28-explore-der.png');
    await goto(BASE + '/diagnose/?grade=' + encodeURIComponent('选必二') + '&demo=1&limit=12');
    await waitFor(() => exists('#chapters'), 'Selective Required Course 2 overall diagnosis', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).indexOf('Selective Required Volume 2') >= 0, 'Selective Required Course 2 overall diagnosis');
    check(await exists('#chapters .chap-sum'), 'Selective Required Course 2 overall diagnosis has chapter summaries');
    await checkPage('Selective Required Course 2 overall diagnosis 1280');
    await shot('30-diagnose-xuanbi2.png', '#summary', 900);
    await setView(375, 812);
    await checkExplore(DERIVE.id, { title: 'Definition of a Derivative', idCode: DERIVE.id, diag: DERIVE.id });
    check((await evalJs('document.body.innerText')).indexOf('Selective Required Volume 2') >= 0, '375 px derivative page still identifies Selective Required Course 2');
    await checkPage('Derivative concepts 375');
    await shot('29-explore-der-375.png', null, 1100);
    await goto(BASE + '/diagnose/?grade=' + encodeURIComponent('选必二') + '&demo=1&limit=12');
    await waitFor(() => exists('#chapters'), 'Selective Required Course 2 overall diagnosis 375', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).indexOf('Selective Required Volume 2') >= 0, 'Selective Required Course 2 overall diagnosis at 375 px');
    await checkPage('Selective Required Course 2 overall diagnosis 375');
    await shot('31-diagnose-xuanbi2-375.png', null, 1100);
    await evalJs('localStorage.clear()');
    await goto(BASE + '/diagnose/');
    await waitFor(() => exists('#grade-card'), 'diagnosis start page, Selective Required Course 2');
    await evalJs('(() => { const b = Array.from(document.querySelectorAll("#grade-card .stage-tab")).find((x) => x.textContent === "Selective 2"); if (!b) throw new Error("Selective Required Course 2 tab not found"); b.click(); })()');
    check((await evalJs('document.getElementById("grade-info").textContent')).indexOf('Selective Required Volume 2') >= 0, 'Selective Required Course 2 card shows its full course name');
    check(await evalJs('!Array.from(document.querySelectorAll("#grade-card .stage-tab")).some((b) => b.textContent === "Semester 1" || b.textContent === "Semester 2")'), 'Selective Required Course 2 overall diagnosis does not offer semester books');
    check(await evalJs('Array.from(document.querySelectorAll("#grade-card .stage-tab")).some((b) => b.textContent === "Full Volume")'), 'Selective Required Course 2 covers the full book');

    console.log('Elementary English');
    const ing = TOPIC_ROWS.find((t) => t.id === 'cne_p148');
    if (!ing) throw new Error('Topic "Present Continuous" not found');
    await setView(1280, 900);
    const ingInfo = await checkExplore(ing.id, { title: 'Present Continuous', idCode: ing.id, diag: ing.id });
    check(String(ing.id).startsWith('cne_p'), 'the present-continuous example remains an elementary-school topic');
    check(ingInfo.primary > 0 && ingInfo.junior >= 1 && ingInfo.senior === 0, 'the present-continuous local graph is mainly elementary and links to middle-school follow-up (' + ingInfo.primary + ' elementary, ' + ingInfo.junior + ' middle)');
    check((await evalJs('location.search')).indexOf('subject=english') >= 0, 'English topics automatically include subject=english');
    check((await evalJs('document.querySelector("a.diag-btn").getAttribute("href")')).indexOf('subject=english') >= 0, 'English diagnosis button includes the subject');
    await checkBanner('English graph 1280');
    const switchH = await evalJs('(() => { const a = document.querySelector(".subject-link"); return a ? a.getBoundingClientRect().height : 0; })()');
    check(switchH >= 44, 'subject-switch touch target is at least 44 px high (' + Math.round(switchH) + ')');
    await shot('32-explore-ing.png');
    await setView(375, 812);
    await checkExplore(ing.id, { title: 'Present Continuous', idCode: ing.id, diag: ing.id });
    await checkBanner('English graph 375');
    await checkPage('Present continuous 375');
    await shot('33-explore-ing-375.png', null, 1100);
    await setView(1280, 900);
    await goto(BASE + '/diagnose/?subject=english&grade=' + encodeURIComponent('四上') + '&demo=1&limit=12');
    await waitFor(() => exists('#chapters'), 'Grade 4, Book 1 English overall diagnosis', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).indexOf('Grade 4, Semester 1') >= 0, 'Grade 4, Book 1 English overall diagnosis title');
    check((await evalJs(IQ_RESULT_EXPR)) === 'ok', 'English diagnosis results page also has a children’s IQ test entry');
    await checkBanner('English diagnosis 1280');
    check(await exists('#chapters .chap-sum'), 'Grade 4, Book 1 English overall diagnosis has chapter summaries');
    check((await evalJs('document.body.innerText')).indexOf('Completing the Square') < 0, 'the full-book English diagnosis does not include math topics');
    await checkPage('Grade 4, Book 1 English 1280');
    await shot('34-diagnose-en-g4.png', '#summary', 900);
    await setView(375, 812);
    await goto(BASE + '/diagnose/?subject=english&grade=' + encodeURIComponent('四上') + '&demo=1&limit=12');
    await waitFor(() => exists('#chapters'), 'Grade 4, Book 1 English overall diagnosis 375', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).indexOf('Grade 4, Semester 1') >= 0, 'Grade 4, Book 1 English overall diagnosis at 375 px');
    await checkBanner('English diagnosis 375');
    await checkPage('Grade 4, Book 1 English 375');
    await shot('35-diagnose-en-g4-375.png', null, 1100);

    console.log('Middle-school English');
    const perfect = TOPIC_ROWS.find((t) => t.id === 'cne_j174');
    if (!perfect) throw new Error('Topic "Present Perfect" not found');
    await setView(1280, 900);
    const perfInfo = await checkExplore(perfect.id, { title: 'Present Perfect', idCode: perfect.id, diag: perfect.id });
    check(perfInfo.junior > 0, 'the present-perfect local graph includes middle-school nodes (middle ' + perfInfo.junior + ', high ' + perfInfo.senior + ')');
    const stageTabs = await evalJs('Array.from(document.querySelectorAll("#stage-tabs [data-stage]:not([hidden])")).map((b) => b.textContent).join(",")');
    check(stageTabs === 'All,Elementary,Middle School,High School', 'English graph school stages are all / elementary / middle / high (' + stageTabs + ')');
    const gradeOpts = await evalJs('Array.from(document.querySelectorAll("#fGrade option")).map((o) => o.textContent).join(",")');
    check(gradeOpts.indexOf('Grade 9') >= 0 && gradeOpts.indexOf('High School Year 1') < 0 && gradeOpts.indexOf('Grade 1') < 0 && gradeOpts.indexOf('Required Volume 1') >= 0 && gradeOpts.indexOf('Selective Required Volume 4') >= 0, 'English grade filters span Grade 3 through high school and use volume labels instead of school-year numbers (' + gradeOpts + ')');
    const legendH = await evalJs('(() => { const li = document.querySelector(".legend li:has(.sw-h)"); if (!li) return "missing"; return getComputedStyle(li).display; })()');
    const legendJ = await evalJs('(() => { const li = document.querySelector(".legend li:has(.sw-j)"); if (!li) return "missing"; return getComputedStyle(li).display; })()');
    check(legendH !== 'none' && legendH !== 'missing' && legendJ !== 'none', 'English graph legend includes both middle and high school (middle ' + legendJ + ', high ' + legendH + ')');
    await shot('43-explore-perfect.png');
    await setView(375, 812);
    await checkExplore(perfect.id, { title: 'Present Perfect', idCode: perfect.id, diag: perfect.id });
    await checkPage('Present perfect 375');
    await shot('44-explore-perfect-375.png', null, 1100);
    await setView(1280, 900);
    await goto(BASE + '/diagnose/?subject=english&grade=' + encodeURIComponent('八上') + '&demo=1&limit=12');
    await waitFor(() => exists('#chapters'), 'Grade 8, Book 1 English overall diagnosis', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).indexOf('Grade 8, Semester 1') >= 0, 'Grade 8, Book 1 English overall diagnosis title');
    check((await evalJs(IQ_RESULT_EXPR)) === 'ok', 'middle-school English results page also has a children’s IQ test entry');
    await checkBanner('Middle-school English diagnosis 1280');
    check(await exists('#chapters .chap-sum'), 'Grade 8, Book 1 English overall diagnosis has chapter summaries');
    check((await evalJs('document.body.innerText')).indexOf('Completing the Square') < 0, 'the full-book middle-school English diagnosis does not include math topics');
    check((await evalJs('document.body.innerText')).indexOf('Elementary, middle, and high school topics use different colors') >= 0, 'English results-page legend explains the colors for elementary, middle, and high school');
    await checkPage('Grade 8, Book 1 English 1280');
    await shot('45-diagnose-en-g8.png', '#summary', 900);
    await setView(375, 812);
    await goto(BASE + '/diagnose/?subject=english&grade=' + encodeURIComponent('八上') + '&demo=1&limit=12');
    await waitFor(() => exists('#chapters'), 'Grade 8, Book 1 English overall diagnosis 375', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).indexOf('Grade 8, Semester 1') >= 0, 'Grade 8, Book 1 English overall diagnosis at 375 px');
    await checkBanner('Middle-school English diagnosis 375');
    await checkPage('Grade 8, Book 1 English 375');
    await shot('46-diagnose-en-g8-375.png', null, 1100);

    console.log('High-school English');
    const subj = TOPIC_ROWS.find((t) => t.id === 'cne_h155');
    if (!subj) throw new Error('Topic "Subjunctive Mood" not found');
    await setView(1280, 900);
    const subInfo = await checkExplore(subj.id, { title: 'Subjunctive Mood', idCode: subj.id, diag: subj.id });
    check(subInfo.senior > 0 && subInfo.junior > 0, 'the subjunctive-mood local graph includes high- and middle-school nodes (high ' + subInfo.senior + ', middle ' + subInfo.junior + ')');
    check((await evalJs('document.body.innerText')).indexOf('High School Year 1') < 0, 'the subjunctive-mood page does not label the English book as Grade 10');
    check((await evalJs('document.body.innerText')).indexOf('Selective Required Volume 2') >= 0, 'the subjunctive-mood page identifies Selective Required Course 2');
    await checkPage('Subjunctive mood 1280');
    await shot('51-explore-subjunctive.png');
    await setView(375, 812);
    await checkExplore(subj.id, { title: 'Subjunctive Mood', idCode: subj.id, diag: subj.id });
    await checkPage('Subjunctive mood 375');
    await shot('52-explore-subjunctive-375.png', null, 1100);
    await setView(1280, 900);
    await goto(BASE + '/diagnose/?subject=english&grade=' + encodeURIComponent('选必一') + '&demo=1&limit=12');
    await waitFor(() => exists('#chapters'), 'Selective Required Course 1 English overall diagnosis', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).indexOf('Selective Required Volume 1') >= 0, 'Selective Required Course 1 English overall diagnosis title');
    check((await evalJs('document.body.innerText')).indexOf('Completing the Square') < 0, 'the full-book high-school English diagnosis does not include math topics');
    check((await evalJs('document.body.innerText')).indexOf('People of Achievement') >= 0, 'Selective Required Course 1 diagnosis is summarized by unit');
    check(await evalJs('!Array.from(document.querySelectorAll("#grade-card .stage-tab")).some((b) => b.textContent === "Semester 1" || b.textContent === "Semester 2")'), 'Selective Required Course 1 English does not offer semester books');
    await checkPage('Selective Required Course 1 English 1280');
    await shot('53-diagnose-en-xuanbi1.png', '#summary', 900);
    await setView(375, 812);
    await goto(BASE + '/diagnose/?subject=english&grade=' + encodeURIComponent('选必一') + '&demo=1&limit=12');
    await waitFor(() => exists('#chapters'), 'Selective Required Course 1 English overall diagnosis 375', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).indexOf('Selective Required Volume 1') >= 0, 'Selective Required Course 1 English overall diagnosis at 375 px');
    await checkPage('Selective Required Course 1 English 375');
    await shot('54-diagnose-en-xuanbi1-375.png', null, 1100);

    console.log('Share images');
    const shareUi = () => evalJs(`(() => {
      const img = document.getElementById('share-preview');
      const dl = document.getElementById('share-download');
      const hint = document.getElementById('share-hint');
      const visible = (el) => !!(el && el.getClientRects().length);
      return {
        tag: img ? img.tagName : '',
        src: img && img.src ? img.src.slice(0, 5) : '',
        w: img ? img.naturalWidth : 0,
        h: img ? img.naturalHeight : 0,
        download: visible(dl),
        downloadName: dl ? (dl.getAttribute('download') || '') : '',
        hint: visible(hint),
        hintText: hint ? (hint.textContent || '').trim() : ''
      };
    })()`);
    const saveShareImage = async (file) => {
      await waitFor(() => evalJs('(() => { const img = document.getElementById("share-preview"); return !!(img && img.complete && img.naturalWidth === 1080 && img.naturalHeight === 1920); })()'), 'share image dimensions ' + file, 10000);
      const b64 = await evalJs(`(async () => {
        const img = document.getElementById('share-preview');
        const blob = await (await fetch(img.src)).blob();
        const bytes = new Uint8Array(await blob.arrayBuffer());
        let binary = '';
        const chunk = 0x4000;
        for (let i = 0; i < bytes.length; i += chunk) {
          binary += String.fromCharCode.apply(null, bytes.subarray(i, Math.min(i + chunk, bytes.length)));
        }
        return btoa(binary);
      })()`);
      fs.writeFileSync(path.join(OUT, file), Buffer.from(b64, 'base64'));
      console.log('  Share image screenshots/' + file);
    };
    const assertSharePng = (file) => {
      const img = pngRgba(path.join(OUT, file));
      check(img.width === 1080 && img.height === 1920, file + ' is 1080×1920');
      const px = pngPixel(img, 80, 40);
      check(px[0] < 80 && px[1] > 80 && px[1] < 170 && px[2] > 70 && px[2] < 160, file + ' header uses the site teal color');
      const decoded = decodeQr(img);
      check(decoded === SHARE_URL, file + ' QR code contains the share URL (' + decoded + ')');
    };

    await setView(1280, 900);
    await goto(BASE + '/diagnose/?grade=' + encodeURIComponent('五上') + '&demo=1');
    await waitFor(() => exists('#btn-share'), 'math results-page share button', 20000);
    check((await evalJs('document.getElementById("btn-share").textContent')) === 'Create Share Image', 'button text is “Generate share image”');
    const qrSrc = await evalJs(`document.querySelector('script[src$="qrcode.js"]').getAttribute('src')`);
    check(qrSrc === '../assets/vendor/qrcode.js', 'QR-code script uses a local relative path (' + qrSrc + ')');
    await checkPage('Math share results page 1280');
    await click('#btn-share');
    await waitFor(() => exists('#share-preview'), 'math share modal', 10000);
    const mathUi = await shareUi();
    check(mathUi.tag === 'IMG', 'desktop preview is an img');
    check(mathUi.src === 'blob:' || mathUi.src === 'data:', 'desktop preview URL can be saved (' + mathUi.src + ')');
    check(mathUi.download && mathUi.downloadName === 'knowledge-graph-diagnostic-share.png', 'download image is shown at 1280 px');
    check(!mathUi.hint, 'no long-press hint is shown at 1280 px');
    const mathModel = await evalJs('window.__shareModel');
    check(mathModel && mathModel.siteName === '12Grades Knowledge Graph' && mathModel.subject === 'Math' && String(mathModel.scope).indexOf('Grade 5, Semester 1') >= 0 && mathModel.spotKind === 'chapter', 'math share scope is Grade 5, Book 1 (' + JSON.stringify(mathModel && { scope: mathModel.scope, subject: mathModel.subject, spotKind: mathModel.spotKind }) + ')');
    check(mathModel && mathModel.spots.length >= 1 && mathModel.spots.length <= 3, 'math share lists 1–3 chapters');
    check(mathModel && mathModel.roots.length >= 1 && mathModel.roots.length <= 2, 'math share includes 1–2 root causes');
    check(JSON.stringify(mathModel).indexOf('payment') < 0 && JSON.stringify(mathModel).indexOf('name') < 0, 'share content contains no payment or name information');
    await saveShareImage('38-share-math.png');
    assertSharePng('38-share-math.png');

    await setView(375, 812);
    await sleep(200);
    const phoneUi = await shareUi();
    check(phoneUi.tag === 'IMG' && (phoneUi.src === 'blob:' || phoneUi.src === 'data:'), '375 px preview remains a saveable img');
    check(!phoneUi.download, 'download image is hidden at 375 px');
    check(phoneUi.hint && phoneUi.hintText === 'Press and hold the image to save it.', '375 px shows a long-press-to-save hint (' + phoneUi.hintText + ')');
    await checkPage('Share modal 375');
    await shot('40-share-modal-375.png', null, 812, { beyond: false });

    await setView(1280, 900);
    await goto(BASE + '/diagnose/?subject=english&target=cne_p148&demo=1');
    await waitFor(() => exists('#btn-share'), 'English results-page share button', 20000);
    check((await evalJs('document.querySelector("#summary h2").textContent')).indexOf('Present Continuous') >= 0, 'English present-continuous results page');
    await checkPage('English share results page 1280');
    await click('#btn-share');
    await waitFor(() => exists('#share-preview'), 'English share modal', 10000);
    const enModel = await evalJs('window.__shareModel');
    check(enModel && enModel.subject === 'English' && String(enModel.scope).indexOf('Present Continuous') >= 0 && enModel.spotKind === 'topic', 'English share scope is present continuous (' + JSON.stringify(enModel && { scope: enModel.scope, subject: enModel.subject, spotKind: enModel.spotKind, spots: (enModel.spots || []).length, roots: (enModel.roots || []).length }) + ')');
    check(enModel && enModel.spots.length >= 1 && enModel.spots.length <= 3 && enModel.roots.length >= 1 && enModel.roots.length <= 2, 'English share includes 1–3 weak topics and 1–2 root causes');
    const enDesk = await shareUi();
    check(enDesk.download && !enDesk.hint, 'the English share modal is downloadable at 1280 px');
    await saveShareImage('39-share-en.png');
    assertSharePng('39-share-en.png');
    await setView(375, 812);
    await sleep(120);
    const enPhone = await shareUi();
    check(!enPhone.download && enPhone.hintText === 'Press and hold the image to save it.', 'the English share modal uses long-press saving at 375 px');
    await checkPage('English share modal 375');
    await setView(1280, 900);

    check(externalReqs.length === 0, 'the page made no external resource requests at runtime' + (externalReqs.length ? ':\n       ' + externalReqs.slice(0, 8).join('\n       ') : ''));
    check(errors.length === 0, 'no console or network errors' + (errors.length ? ':\n       ' + errors.join('\n       ') : ''));
    if (checks.some((c) => !c[0])) exitCode = 1;
    cdp.ws.close();
  } catch (e) {
    console.error('Smoke test exception: ' + (e && e.stack || e));
    if (dumpPage) { try { console.error('Current page text:\n' + await dumpPage()); } catch (e2) { /* ignore */ } }
    if (errors.length) console.error('Captured browser errors:\n' + errors.join('\n'));
    exitCode = 1;
  } finally {
    chrome.kill('SIGKILL');
    server.kill('SIGKILL');
    try { fs.rmSync(profile, { recursive: true, force: true }); } catch (e) { /* ignore */ }
  }
  console.log(exitCode ? '\nSmoke test failed' : '\nSmoke test passed (' + checks.length + ' checks)');
  process.exit(exitCode);
}

function fetchOk(url) { return fetch(url).then((r) => r.ok, () => false); }

function noteExternal(params, bucket) {
  const initiator = (params.initiator && params.initiator.type) || '';
  if (initiator !== 'parser' && initiator !== 'script') return;
  const url = params.request && params.request.url;
  if (!url || !/^https?:/i.test(url)) return;
  let host = '';
  try { host = new URL(url).hostname; } catch (e) { return; }
  if (host === '127.0.0.1' || host === 'localhost') return;
  const type = params.type || '';
  if (['Script', 'Stylesheet', 'Image', 'Font', 'XHR', 'Fetch', 'Document', 'Other'].indexOf(type) < 0) return;
  const line = type + ' ' + initiator + ' ' + url;
  if (bucket.indexOf(line) < 0) bucket.push(line);
}

const LOCAL_ASSET_EXPR = `(() => {
  const bad = [];
  const local = (raw) => {
    if (!raw || raw.indexOf('data:') === 0 || raw.indexOf('blob:') === 0 || raw.charAt(0) === '#') return true;
    try {
      const u = new URL(raw, location.href);
      return u.protocol === 'data:' || u.protocol === 'blob:' || u.hostname === '127.0.0.1' || u.hostname === 'localhost';
    } catch (e) { return false; }
  };
  document.querySelectorAll('script[src], link[href], img[src], iframe[src], video[src], audio[src], source[src]').forEach((el) => {
    const raw = el.getAttribute('src') || el.getAttribute('href') || '';
    if (!local(raw)) bad.push(el.tagName.toLowerCase() + ' ' + raw);
  });
  Array.from(document.styleSheets).forEach((sheet) => {
    let rules;
    try { rules = sheet.cssRules; } catch (e) { bad.push('stylesheet ' + (sheet.href || 'inline')); return; }
    const walk = (list) => {
      if (!list) return;
      for (const rule of list) {
        if (rule.style) {
          for (let i = 0; i < rule.style.length; i++) {
            const val = rule.style.getPropertyValue(rule.style[i]);
            const re = /url\\(([^)]+)\\)/g;
            let m;
            while ((m = re.exec(val))) {
              const raw = m[1].trim().replace(/^['"]|['"]$/g, '');
              if (!local(raw)) bad.push('css ' + raw);
            }
          }
        }
        if (rule.cssRules) walk(rule.cssRules);
      }
    };
    walk(rules);
  });
  return bad;
})()`;

main();
