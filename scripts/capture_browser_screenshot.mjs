#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { mkdtemp, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

const args = new Set(process.argv.slice(2));
const chromePath = process.env.CHROME_PATH || (process.platform === 'darwin'
  ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
  : '/usr/bin/google-chrome');
const target = process.env.TARGET_URL || 'http://127.0.0.1:9696/layout-options/mobile-run-first';
const output = process.env.OUTPUT || (args.has('--inject-shiki') ? '/tmp/pythonbyexample-shots/desktop-literate-shiki.png' : '/tmp/pythonbyexample-shots/desktop-literate-plain.png');
const url = `${target}${target.includes('?') ? '&' : '?'}screenshot_test=${Date.now()}`;
const width = Number(process.env.WIDTH || 2040);
const height = Number(process.env.HEIGHT || 626);
const port = 9444 + Math.floor(Math.random() * 1000);
const profile = await mkdtemp(path.join(tmpdir(), 'pythonbyexample-shot-chrome-'));

const chrome = spawn(chromePath, [
  '--headless=new',
  '--disable-gpu',
  '--disable-dev-shm-usage',
  '--no-first-run',
  '--no-default-browser-check',
  '--disable-application-cache',
  '--disk-cache-size=1',
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
  await client.send('Network.enable');
  await client.send('Network.setCacheDisabled', { cacheDisabled: true });
  await client.send('Page.enable');
  await client.send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });
  await client.send('Page.navigate', { url });

  for (let i = 0; i < 100; i++) {
    const ready = await client.send('Runtime.evaluate', {
      expression: "document.readyState === 'complete' && !!document.querySelector('.literate-program')",
      returnByValue: true,
    });
    if (ready.result.value) break;
    await sleep(100);
  }

  if (args.has('--legacy-shiki')) {
    await client.send('Runtime.evaluate', {
      awaitPromise: true,
      expression: `(async () => {
        const { codeToHtml } = await import('https://esm.sh/shiki@1.29.2');
        for (const block of document.querySelectorAll('pre code.language-python')) {
          const highlighted = await codeToHtml(block.textContent, { lang: 'python', theme: 'github-light' });
          const wrapper = document.createElement('div');
          wrapper.innerHTML = highlighted;
          const shikiPre = wrapper.firstElementChild;
          shikiPre.classList.add('shiki-block');
          block.closest('pre').replaceWith(shikiPre);
        }
      })()`,
    });
    await sleep(1000);
  } else if (args.has('--inject-shiki')) {
    await client.send('Runtime.evaluate', {
      awaitPromise: true,
      expression: `import(document.querySelector('script[type="module"][src*="syntax-highlight"]').src + '?forced=' + Date.now())`,
    });
    await sleep(1000);
  }

  const data = await client.send('Runtime.evaluate', {
    returnByValue: true,
    expression: `(() => {
      const program = document.querySelector('.literate-program');
      const rect = program.getBoundingClientRect();
      const steps = [...document.querySelectorAll('.lesson-step')].map((step, index) => {
        const pre = step.querySelector('pre');
        const code = step.querySelector('code');
        const r = pre.getBoundingClientRect();
        const cs = getComputedStyle(code);
        return { index, text: code.textContent, top: r.top, height: r.height, lineHeight: cs.lineHeight, html: pre.outerHTML.slice(0, 240) };
      });
      return { scrollX, scrollY, rect: { x: rect.x, y: rect.y, width: rect.width, height: rect.height }, steps };
    })()`,
  });
  const info = data.result.value;
  console.log(JSON.stringify(info.steps, null, 2));

  const clip = {
    x: Math.max(0, info.rect.x - 20 + info.scrollX),
    y: Math.max(0, info.rect.y - 20 + info.scrollY),
    width: Math.min(width, info.rect.width + 40),
    height: Math.min(height, info.rect.height + 40),
    scale: 1,
  };
  const screenshot = await client.send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip });
  await writeFile(output, Buffer.from(screenshot.data, 'base64'));
  console.log(`wrote ${output}`);
  client.close();
} finally {
  chrome.kill('SIGTERM');
  await new Promise(resolve => chrome.once('exit', resolve));
  await rm(profile, { recursive: true, force: true, maxRetries: 5, retryDelay: 100 });
}
