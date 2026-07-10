#!/usr/bin/env node
// Rasterize build/social-cards/*.html to public/og/*.jpg through one
// headless Chrome session. Run scripts/build_social_cards.py first
// (or use `make social-cards`, which runs both).
import { spawn } from 'node:child_process';
import { mkdtemp, mkdir, readdir, readFile, rm, unlink, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cardDir = path.join(root, 'build', 'social-cards');
const outputDir = path.join(root, 'public', 'og');
const chromePath = process.env.CHROME_PATH || (process.platform === 'darwin'
  ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
  : '/usr/bin/google-chrome');
const width = 1200;
const height = 630;
const port = 9444 + Math.floor(Math.random() * 1000);
const profile = await mkdtemp(path.join(tmpdir(), 'pythonbyexample-og-chrome-'));

const manifest = JSON.parse(await readFile(path.join(cardDir, 'manifest.json'), 'utf8'));

const chrome = spawn(chromePath, [
  '--headless=new',
  '--disable-gpu',
  '--no-sandbox',
  '--disable-dev-shm-usage',
  '--no-first-run',
  '--no-default-browser-check',
  '--hide-scrollbars',
  `--user-data-dir=${profile}`,
  `--remote-debugging-port=${port}`,
  'about:blank',
], { stdio: ['ignore', 'pipe', 'pipe'] });

let stderr = '';
chrome.stderr.on('data', chunk => { stderr += chunk.toString(); });
function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }
async function jsonGet(endpoint) {
  const response = await fetch(`http://127.0.0.1:${port}${endpoint}`);
  if (!response.ok) throw new Error(`${endpoint} returned ${response.status}`);
  return response.json();
}
async function waitForChrome() {
  for (let i = 0; i < 80; i++) {
    try { return await jsonGet('/json/version'); } catch { await sleep(100); }
  }
  throw new Error(`Chrome did not start. stderr:\n${stderr}`);
}
let nextId = 1;
function connect(wsUrl) {
  const socket = new WebSocket(wsUrl);
  const pending = new Map();
  socket.addEventListener('message', event => {
    const message = JSON.parse(event.data);
    if (message.id && pending.has(message.id)) {
      const { resolve, reject } = pending.get(message.id);
      pending.delete(message.id);
      if (message.error) reject(new Error(JSON.stringify(message.error)));
      else resolve(message.result);
    }
  });
  const opened = new Promise((resolve, reject) => {
    socket.addEventListener('open', resolve, { once: true });
    socket.addEventListener('error', reject, { once: true });
  });
  return {
    opened,
    send(method, params = {}) {
      const id = nextId++;
      socket.send(JSON.stringify({ id, method, params }));
      return new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
    },
    close() { socket.close(); },
  };
}

try {
  await waitForChrome();
  const pages = await jsonGet('/json/list');
  const page = pages.find(item => item.type === 'page');
  const client = connect(page.webSocketDebuggerUrl);
  await client.opened;
  await client.send('Page.enable');
  await client.send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });

  await mkdir(outputDir, { recursive: true });
  const expected = new Set(Object.keys(manifest).map(name => `${name}.jpg`));
  for (const name of await readdir(outputDir)) {
    if (name.endsWith('.jpg') && !expected.has(name)) await unlink(path.join(outputDir, name));
  }
  let written = 0;
  for (const [name, file] of Object.entries(manifest)) {
    await client.send('Page.navigate', { url: `file://${path.join(cardDir, file)}` });
    for (let i = 0; i < 50; i++) {
      const ready = await client.send('Runtime.evaluate', {
        expression: "document.readyState === 'complete'",
        returnByValue: true,
      });
      if (ready.result.value) break;
      await sleep(50);
    }
    const shot = await client.send('Page.captureScreenshot', {
      format: 'jpeg', quality: 90,
      clip: { x: 0, y: 0, width, height, scale: 1 },
    });
    await writeFile(path.join(outputDir, `${name}.jpg`), Buffer.from(shot.data, 'base64'));
    written += 1;
  }
  client.close();
  console.log(`Rasterized ${written} social cards to public/og/.`);
} finally {
  chrome.kill('SIGTERM');
  await new Promise(resolve => chrome.once('exit', resolve));
  await rm(profile, { recursive: true, force: true });
}
