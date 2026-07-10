#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

const chromePath = process.env.CHROME_PATH || (process.platform === 'darwin'
  ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
  : '/usr/bin/google-chrome');
const target = process.argv[2] || 'http://127.0.0.1:9696/examples/values';
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
  const listeners = new Map();
  socket.addEventListener('message', event => {
    const message = JSON.parse(event.data);
    if (message.id && pending.has(message.id)) {
      const { resolve, reject } = pending.get(message.id);
      pending.delete(message.id);
      if (message.error) reject(new Error(JSON.stringify(message.error)));
      else resolve(message.result);
      return;
    }
    for (const listener of listeners.get(message.method) || []) listener(message.params);
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
    on(method, listener) {
      const handlers = listeners.get(method) || new Set();
      handlers.add(listener);
      listeners.set(method, handlers);
      return () => handlers.delete(listener);
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
      expression: `location.href === ${JSON.stringify(url)} && document.readyState === 'complete' && !!document.querySelector('.lesson-step code') && !!window.pythonByExampleEditor && !!document.querySelector('.cm-content') && !!document.querySelector('.copy-button') && !!document.querySelector('.share-button')`,
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

  async function evaluateValue(expression) {
    const result = await client.send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
    if (result.exceptionDetails) throw new Error(`Browser evaluation failed: ${result.exceptionDetails.text}`);
    return result.result.value;
  }

  async function waitFor(expression, label, attempts = 300) {
    for (let i = 0; i < attempts; i++) {
      if (await evaluateValue(expression)) return;
      await sleep(100);
    }
    throw new Error(`Timed out waiting for ${label}`);
  }

  // Exercise the public browser contracts rather than merely asserting source
  // strings: copy text, fragment sharing/restoration, resize, and arrow guards.
  await client.send('Page.navigate', { url: target });
  await waitFor("document.readyState === 'complete' && !!window.pythonByExampleEditor && !!document.querySelector('.copy-button') && !!document.querySelector('.share-button')", 'feature test page');
  const share = await evaluateValue(`(async () => {
    const writes = [];
    window.__pbeClipboardWrites = writes;
    try {
      Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async text => writes.push(text) } });
    } catch (_) {}
    document.execCommand = command => {
      if (command !== 'copy') return false;
      writes.push(document.activeElement?.value || '');
      return true;
    };
    const code = Array.from({ length: 80 }, (_, index) => 'print("π ' + index + '")').join('\\n');
    window.pythonByExampleEditor.setValue(code);
    await new Promise(resolve => requestAnimationFrame(resolve));
    document.querySelector('.share-button').click();
    await new Promise(resolve => setTimeout(resolve, 50));
    return { code, url: writes.at(-1) || '', editorHeight: document.querySelector('.cm-editor').getBoundingClientRect().height };
  })()`);

  const sharedReloadUrl = new URL(share.url);
  sharedReloadUrl.searchParams.set('browser_share_test', Date.now());
  await client.send('Page.navigate', { url: sharedReloadUrl.href });
  await waitFor(`document.readyState === 'complete' && !!window.pythonByExampleEditor && document.getElementById('code-editor')?.value === ${JSON.stringify(share.code)}`, 'shared-code restoration');
  const restored = await evaluateValue(`({
    editorHeight: document.querySelector('.cm-editor').getBoundingClientRect().height,
    notice: document.querySelector('.output-panel code')?.textContent,
  })`);
  const sourceCopy = await evaluateValue(`(async () => {
    const writes = window.__pbeClipboardWrites = [];
    try {
      Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async text => writes.push(text) } });
    } catch (_) {}
    document.execCommand = command => {
      if (command !== 'copy') return false;
      writes.push(document.activeElement?.value || '');
      return true;
    };
    const source = document.querySelector('.cell-source');
    const expected = source.querySelector('pre').textContent;
    const button = source.querySelector('.copy-button');
    button.click();
    await new Promise(resolve => setTimeout(resolve, 50));
    return { expected, copied: writes.at(-1) || '', state: button.className, status: button.querySelector('.copy-status')?.textContent };
  })()`);
  const arrow = await evaluateValue(`(async () => {
    const textarea = document.getElementById('code-editor');
    const modifiedPath = location.pathname;
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    await new Promise(resolve => setTimeout(resolve, 50));
    const blockedModified = location.pathname === modifiedPath;
    window.pythonByExampleEditor.setValue(textarea.dataset.originalCode || textarea.defaultValue);
    const next = document.querySelector('.example-nav a[rel="next"]')?.href || '';
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    return { blockedModified, next };
  })()`);
  await waitFor(`location.href === ${JSON.stringify(arrow.next)} && !!window.pythonByExampleEditor && !!document.querySelector('.cm-content')`, 'clean arrow navigation');
  const editableBlocked = await evaluateValue(`(async () => {
    const path = location.pathname;
    document.querySelector('.cm-content').dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    await new Promise(resolve => setTimeout(resolve, 50));
    return location.pathname === path;
  })()`);

  async function searchWidthAt(label, width, height, mobile) {
    await client.send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile });
    await client.send('Page.navigate', { url: `${new URL(target).origin}/?browser_search_width=${label}` });
    await waitFor("document.readyState === 'complete' && !!document.querySelector('.site-search')", `${label} search page`);
    return evaluateValue(`(() => {
      const search = document.querySelector('.site-search').getBoundingClientRect();
      const main = document.querySelector('main').getBoundingClientRect();
      const input = document.querySelector('.site-search input').getBoundingClientRect();
      return { label: ${JSON.stringify(label)}, searchWidth: search.width, mainWidth: main.width, inputWidth: input.width };
    })()`);
  }

  const searchWidths = [];
  searchWidths.push(await searchWidthAt('desktop', 1200, 900, false));
  searchWidths.push(await searchWidthAt('mobile-portrait', 390, 844, true));
  searchWidths.push(await searchWidthAt('mobile-landscape', 844, 390, true));
  await client.send('Emulation.setDeviceMetricsOverride', { width: 390, height: 1800, deviceScaleFactor: 2, mobile: true });

  // Keep esm.sh import requests pending. The runner has no imports and is
  // emitted after its markup, so its controls must attach before the editor's
  // CDN graph can let DOMContentLoaded fire.
  let heldCdnRequests = 0;
  const removePauseListener = client.on('Fetch.requestPaused', () => { heldCdnRequests += 1; });
  await client.send('Fetch.enable', { patterns: [{ urlPattern: 'https://esm.sh/*' }] });
  const offlineCode = Array.from({ length: 80 }, (_, index) => `print(${index})`).join('\n');
  const offlineUrl = `${target}#code=${Buffer.from(offlineCode, 'utf8').toString('base64')}`;
  await client.send('Page.navigate', { url: offlineUrl });
  await waitFor(`!!document.querySelector('.share-button') && !!document.querySelector('.copy-button') && document.getElementById('code-editor')?.value === ${JSON.stringify(offlineCode)}`, 'runner controls while CDN is pending');
  const offlineRunner = await evaluateValue(`({
    editorLoaded: !!window.pythonByExampleEditor,
    fallbackHeight: document.getElementById('code-editor').getBoundingClientRect().height,
  })`);
  removePauseListener();
  await client.send('Fetch.disable');

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
  if (!share.url.includes('#code=')) failures.push('Copy link did not copy a shared-code fragment');
  if (restored.notice !== 'This link included edited code. Press Run to execute it.') failures.push('Shared-code recipient notice did not render');
  if (restored.editorHeight < 1000) failures.push(`Shared CodeMirror payload did not resize the editor (${restored.editorHeight}px)`);
  if (sourceCopy.copied !== sourceCopy.expected || !sourceCopy.state.includes('copied') || sourceCopy.status !== 'Copied') {
    failures.push('Source copy button did not copy its exact source or report success');
  }
  if (!arrow.blockedModified) failures.push('Arrow navigation discarded edited code');
  if (!arrow.next) failures.push('Clean example has no next navigation target');
  if (!editableBlocked) failures.push('Arrow navigation fired from the editable CodeMirror surface');
  for (const measurement of searchWidths) {
    if (Math.abs(measurement.searchWidth - measurement.mainWidth) > 1 || Math.abs(measurement.inputWidth - measurement.searchWidth) > 1) {
      failures.push(`${measurement.label} search is not full width (${measurement.searchWidth}px search, ${measurement.mainWidth}px main, ${measurement.inputWidth}px input)`);
    }
  }
  if (heldCdnRequests === 0) failures.push('CDN-pending runner test did not hold an esm.sh request');
  if (offlineRunner.editorLoaded) failures.push('CDN-pending test unexpectedly loaded CodeMirror');
  if (offlineRunner.fallbackHeight < 1000) failures.push(`Shared fallback textarea did not resize (${offlineRunner.fallbackHeight}px)`);

  console.log(JSON.stringify({
    runnerInteraction: interaction.result.value,
    share: { codeLength: share.code.length, urlLength: share.url.length, editorHeight: share.editorHeight },
    restored,
    sourceCopy: { copiedLength: sourceCopy.copied.length, state: sourceCopy.state, status: sourceCopy.status },
    arrow,
    searchWidths,
    offlineRunner,
    heldCdnRequests,
  }, null, 2));
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
