#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

const chromePath = process.env.CHROME_PATH || (process.platform === 'darwin'
  ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
  : '/usr/bin/google-chrome');
const target = process.argv[2] || 'http://127.0.0.1:9696/layout-options/mobile-run-first';
const url = `${target}${target.includes('?') ? '&' : '?'}browser_layout_check=${Date.now()}`;
const port = 9333 + Math.floor(Math.random() * 1000);
const profile = await mkdtemp(path.join(tmpdir(), 'pythonbyexample-chrome-'));

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
  for (let i = 0; i < 300; i++) {
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
  await client.send('Emulation.setDeviceMetricsOverride', {
    width: 390,
    height: 1800,
    deviceScaleFactor: 2,
    mobile: true,
  });
  await client.send('Page.enable');
  await client.send('Page.navigate', { url });

  let pageReady = false;
  for (let i = 0; i < 300; i++) {
    const ready = await client.send('Runtime.evaluate', {
      expression: `location.href === ${JSON.stringify(url)} && document.readyState === 'complete' && !!document.querySelector('.lesson-step code') && !!window.pythonByExampleEditor && !!document.querySelector('.cm-content')`,
      returnByValue: true,
    });
    if (ready.result.value) {
      pageReady = true;
      break;
    }
    await sleep(100);
  }
  if (!pageReady) {
    const debug = await client.send('Runtime.evaluate', {
      expression: `({ href: location.href, readyState: document.readyState, title: document.title, text: document.body?.innerText?.slice(0, 500) })`,
      returnByValue: true,
    });
    throw new Error(`Browser layout page did not become ready: ${JSON.stringify(debug.result.value)}`);
  }

  const result = await client.send('Runtime.evaluate', {
    returnByValue: true,
    expression: `(() => {
      const loadedShiki = performance.getEntriesByType('resource').some(entry => /syntax-highlight\.[0-9a-f]{12}\.js/.test(entry.name));
      const blocks = [...document.querySelectorAll('.lesson-step pre')].map((pre, index) => {
        const code = pre.querySelector('code');
        const text = code.textContent.replace(/\\n$/, '');
        const lines = text.split('\\n').length;
        const style = getComputedStyle(code);
        const lineHeight = Number.parseFloat(style.lineHeight);
        const codeHeight = code.getBoundingClientRect().height;
        const preHeight = pre.getBoundingClientRect().height;
        const expected = lineHeight * lines;
        const ratio = codeHeight / expected;
        return { index, text, lines, lineHeight, codeHeight, preHeight, expected, ratio, font: style.font };
      });
      return { loadedShiki, blocks };
    })()`,
  });

  const metrics = result.result.value;
  console.log(JSON.stringify(metrics, null, 2));

  const interaction = await client.send('Runtime.evaluate', {
    expression: `(() => new Promise((resolve) => {
      const editor = document.querySelector('.cm-content');
      const output = document.querySelector('.output-panel code');
      const form = document.querySelector('form.runner-editor');
      if (!editor || !output || !form || !window.pythonByExampleEditor) {
        resolve({ error: 'runner controls did not initialize' });
        return;
      }
      window.pythonByExampleEditor.setValue('x'.repeat(100001));
      form.requestSubmit();
      let attempts = 0;
      const waitFor413 = () => {
        const text = output.textContent;
        if (text.includes('Submitted code is too large')) {
          resolve({ ariaLabel: editor.getAttribute('aria-label'), text });
          return;
        }
        if (++attempts === 100) {
          resolve({ ariaLabel: editor.getAttribute('aria-label'), text, error: '413 message did not render' });
          return;
        }
        setTimeout(waitFor413, 100);
      };
      waitFor413();
    }))()`,
    awaitPromise: true,
    returnByValue: true,
  });

  const failures = [];
  if (interaction.result.value?.ariaLabel !== 'Editable Python example code') {
    failures.push('CodeMirror editor is missing its accessible name');
  }
  if (interaction.result.value?.error) {
    failures.push(interaction.result.value.error);
  }
  for (const block of metrics.blocks) {
    if (block.ratio > 1.25) failures.push(`block ${block.index} visual line height ratio ${block.ratio.toFixed(2)} > 1.25`);
  }
  if (!metrics.loadedShiki) failures.push('Shiki did not load');

  console.log(JSON.stringify({ runnerInteraction: interaction.result.value }, null, 2));
  client.close();
  if (failures.length) {
    console.error(`Browser layout check failed: ${failures.join('; ')}`);
    process.exitCode = 1;
  }
} finally {
  chrome.kill('SIGTERM');
  await new Promise(resolve => chrome.once('exit', resolve));
  await rm(profile, { recursive: true, force: true, maxRetries: 5, retryDelay: 100 });
}
