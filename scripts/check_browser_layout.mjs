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

  // Exercise public browser contracts rather than asserting implementation
  // strings: run ordering/reset, sharing bounds, copy, resize, and arrow guards.
  await client.send('Page.navigate', { url: target });
  await waitFor("document.readyState === 'complete' && !!window.pythonByExampleEditor && !!document.querySelector('.copy-button') && !!document.querySelector('.share-button')", 'feature test page');
  const runnerAsset = await evaluateValue(`document.querySelector('script[src*="/runner."]')?.src`);
  const runnerOrdering = await evaluateValue(`(async () => {
    const form = document.querySelector('form.runner-editor');
    const output = document.querySelector('.output-panel code');
    const pending = [];
    const originalFetch = window.fetch;
    window.fetch = () => new Promise(resolve => pending.push(resolve));
    const response = text => ({
      ok: true,
      status: 200,
      text: async () => '<section class="output-panel"><h3>Output</h3><pre><code>' + text + '</code></pre></section>',
    });
    window.pythonByExampleEditor.setValue('print("first")');
    form.requestSubmit();
    await new Promise(resolve => setTimeout(resolve, 0));
    window.pythonByExampleEditor.setValue('print("second")');
    form.requestSubmit();
    await new Promise(resolve => setTimeout(resolve, 0));
    if (pending.length !== 2) {
      window.fetch = originalFetch;
      return { error: 'concurrent submissions did not create two requests', count: pending.length };
    }
    pending[1](response('second result'));
    await new Promise(resolve => setTimeout(resolve, 0));
    pending[0](response('stale first result'));
    await new Promise(resolve => setTimeout(resolve, 20));
    const finalOutput = document.querySelector('.output-panel code')?.textContent;
    const reset = form.querySelector('[data-reset]');
    reset.click();
    await new Promise(resolve => setTimeout(resolve, 0));
    const resetValue = document.getElementById('code-editor').value;
    window.fetch = originalFetch;
    return {
      finalOutput,
      resetType: reset.type,
      resetValue,
      originalCode: document.getElementById('code-editor').dataset.originalCode,
      busy: form.hasAttribute('aria-busy'),
    };
  })()`);
  const networkFailure = await evaluateValue(`(async () => {
    const form = document.querySelector('form.runner-editor');
    const originalFetch = window.fetch;
    window.fetch = () => Promise.reject(new TypeError('network down'));
    window.pythonByExampleEditor.setValue('print("offline")');
    form.requestSubmit();
    for (let i = 0; i < 100 && form.hasAttribute('aria-busy'); i++) {
      await new Promise(resolve => setTimeout(resolve, 10));
    }
    window.fetch = originalFetch;
    return {
      output: document.querySelector('.output-panel code')?.textContent,
      busy: form.hasAttribute('aria-busy'),
      runDisabled: form.querySelector('button[type="submit"]').disabled,
    };
  })()`);
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
    const url = writes.at(-1) || '';
    const editorHeight = document.querySelector('.cm-editor').getBoundingClientRect().height;
    const textarea = document.getElementById('code-editor');
    window.pythonByExampleEditor.setValue(textarea.dataset.originalCode ?? textarea.defaultValue);
    await new Promise(resolve => requestAnimationFrame(resolve));
    document.querySelector('.share-button').click();
    await new Promise(resolve => setTimeout(resolve, 50));
    return { code, url, editorHeight, uneditedUrl: writes.at(-1) || '', pageUrl: location.href.split('#')[0] };
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
    const icon = button.querySelector('.copy-icon');
    const statusNode = button.querySelector('.copy-status');
    const mask = () => getComputedStyle(icon).webkitMaskImage || getComputedStyle(icon).maskImage;
    const idleMask = mask();
    const sourceRect = source.getBoundingClientRect();
    const buttonRect = button.getBoundingClientRect();
    button.click();
    await new Promise(resolve => setTimeout(resolve, 50));
    const copiedState = {
      copied: writes.at(-1) || '',
      state: button.className,
      status: statusNode?.textContent,
      statusRight: statusNode?.getBoundingClientRect().right,
      liveRegion: button.getAttribute('aria-live'),
      copiedMask: mask(),
    };
    // Without the async Clipboard API the button must fall back to a selected
    // off-screen textarea and execCommand('copy').
    const fallbackWrites = [];
    try {
      Object.defineProperty(navigator, 'clipboard', { configurable: true, value: undefined });
    } catch (_) {}
    document.execCommand = command => {
      if (command !== 'copy') return false;
      fallbackWrites.push([...document.querySelectorAll('textarea[readonly]')].at(-1)?.value ?? '');
      return true;
    };
    button.click();
    await new Promise(resolve => setTimeout(resolve, 50));
    return {
      expected,
      ...copiedState,
      idleMask,
      iconPaint: [getComputedStyle(icon).backgroundColor, getComputedStyle(icon).color],
      // Anchored to its own cell's top-right corner, not to a distant ancestor.
      buttonAnchored: Math.abs(buttonRect.right - sourceRect.right) <= 1 && Math.abs(buttonRect.top - sourceRect.top) <= 16,
      fallbackCopied: fallbackWrites.at(-1) ?? '',
      fallbackState: button.className,
    };
  })()`);
  const arrow = await evaluateValue(`(async () => {
    const textarea = document.getElementById('code-editor');
    // Count navigation attempts with the Navigation API and cancel them, so a
    // guard that fails is seen even though the page has not unloaded yet.
    let attempts = 0;
    const cancel = event => { attempts += 1; event.preventDefault(); };
    navigation.addEventListener('navigate', cancel);
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    await new Promise(resolve => setTimeout(resolve, 50));
    const blockedModified = attempts === 0;
    const attemptsWhileEdited = attempts;
    window.pythonByExampleEditor.setValue(textarea.dataset.originalCode || textarea.defaultValue);
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', metaKey: true, bubbles: true }));
    document.querySelector('button[type="submit"]').dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    await new Promise(resolve => setTimeout(resolve, 50));
    navigation.removeEventListener('navigate', cancel);
    const blockedModifierAndButton = attempts === attemptsWhileEdited;
    const next = document.querySelector('.example-nav a[rel="next"]')?.href || '';
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    return { blockedModified, blockedModifierAndButton, next };
  })()`);
  await waitFor(`location.href === ${JSON.stringify(arrow.next)} && !!window.pythonByExampleEditor && !!document.querySelector('.cm-content')`, 'clean arrow navigation');
  const editableBlocked = await evaluateValue(`(async () => {
    const path = location.pathname;
    document.querySelector('.cm-content').dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    await new Promise(resolve => setTimeout(resolve, 50));
    return location.pathname === path;
  })()`);
  // ArrowLeft walks back: next -> the target page -> the first example, where
  // there is no previous link and the key must do nothing (and throw nothing).
  const arrowBack = [];
  for (let step = 0; step < 2; step++) {
    const expected = await evaluateValue(`document.querySelector('.example-nav a[rel="prev"]')?.href || ''`);
    await evaluateValue(`document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowLeft', bubbles: true }))`);
    await waitFor(`location.href === ${JSON.stringify(expected)} && document.readyState === 'complete' && !!document.querySelector('.example-nav')`, `ArrowLeft navigation ${step + 1}`);
    arrowBack.push(expected);
  }
  const catalogEdge = await evaluateValue(`(async () => {
    const errors = [];
    window.addEventListener('error', event => errors.push(event.message));
    const path = location.pathname;
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowLeft', bubbles: true }));
    await new Promise(resolve => setTimeout(resolve, 100));
    return { hasPrev: !!document.querySelector('.example-nav a[rel="prev"]'), stayed: location.pathname === path, errors };
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
  const searchFailure = await evaluateValue(`(async () => {
    const originalFetch = window.fetch;
    window.fetch = async () => ({ ok: false, status: 503, json: async () => ({}) });
    const input = document.getElementById('site-search-input');
    input.focus();
    input.value = 'decorator';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    await new Promise(resolve => setTimeout(resolve, 50));
    const state = {
      status: document.getElementById('site-search-status')?.textContent,
      outlineWidth: getComputedStyle(input).outlineWidth,
      shikiRequests: performance.getEntriesByType('resource').filter(entry => entry.name.includes('esm.sh/shiki')).length,
    };
    window.fetch = originalFetch;
    return state;
  })()`);
  await client.send('Page.navigate', { url: `${new URL(target).origin}/?browser_search_ok=${Date.now()}` });
  await waitFor("document.readyState === 'complete' && !!document.getElementById('site-search-input')", 'search success page');
  const searchSuccess = await evaluateValue(`(async () => {
    const input = document.getElementById('site-search-input');
    input.focus();
    input.value = 'decorator';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    for (let i = 0; i < 100 && input.getAttribute('aria-expanded') !== 'true'; i++) {
      await new Promise(resolve => setTimeout(resolve, 50));
    }
    const listbox = document.getElementById(input.getAttribute('aria-controls'));
    const options = [...(listbox?.querySelectorAll('[role="option"]') || [])];
    return {
      expanded: input.getAttribute('aria-expanded'),
      listboxRole: listbox?.getAttribute('role'),
      listboxHidden: listbox?.hidden,
      options: options.length,
      firstOption: options[0]?.textContent?.trim().slice(0, 60),
    };
  })()`);
  await client.send('Emulation.setDeviceMetricsOverride', { width: 390, height: 1800, deviceScaleFactor: 2, mobile: true });

  // Theme changes are a live OS preference, not a reload-only setting.
  await client.send('Emulation.setEmulatedMedia', {
    media: 'screen',
    features: [{ name: 'prefers-color-scheme', value: 'light' }],
  });
  await client.send('Page.navigate', { url: `${target}?browser_theme=light` });
  await waitFor("document.readyState === 'complete' && !!document.querySelector('.shiki-block') && !!document.querySelector('.cm-editor')", 'light theme page');
  // Colour helpers shared by the light and dark measurements.
  await evaluateValue(`window.__pbeColors = () => {
    const parse = color => color.match(/[\\d.]+/g).slice(0, 3).map(Number);
    const luminance = color => {
      const channels = parse(color).map(value => {
        const normalized = value / 255;
        return normalized <= .04045 ? normalized / 12.92 : ((normalized + .055) / 1.055) ** 2.4;
      });
      return .2126 * channels[0] + .7152 * channels[1] + .0722 * channels[2];
    };
    const contrast = (fg, bg) => {
      const a = luminance(fg);
      const b = luminance(bg);
      return (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
    };
    const body = getComputedStyle(document.body);
    const run = getComputedStyle(document.querySelector('button[type="submit"]'));
    const terminal = getComputedStyle(document.querySelector('.output-panel pre'));
    const figure = document.querySelector('.cell-banner figure svg');
    return {
      pageBackground: body.backgroundColor,
      pageLuminance: luminance(body.backgroundColor),
      textContrast: contrast(body.color, body.backgroundColor),
      runContrast: contrast(run.color, run.backgroundColor),
      terminalContrast: contrast(terminal.color, terminal.backgroundColor),
      figurePaperLuminance: figure ? luminance(getComputedStyle(figure).backgroundColor) : null,
      figurePaperAlpha: figure ? getComputedStyle(figure).backgroundColor : null,
    };
  }; true`);
  const lightTheme = await evaluateValue(`({
    shikiColor: getComputedStyle(document.querySelector('.shiki-block span')).color,
    editorColors: [...new Set([...document.querySelectorAll('.cm-line span')].map(node => getComputedStyle(node).color))].sort(),
    ...window.__pbeColors(),
  })`);
  await client.send('Emulation.setEmulatedMedia', {
    media: 'screen',
    features: [{ name: 'prefers-color-scheme', value: 'dark' }],
  });
  await waitFor(`getComputedStyle(document.querySelector('.shiki-block span')).color !== ${JSON.stringify(lightTheme.shikiColor)}`, 'live dark-theme Shiki rerender');
  const darkTheme = await evaluateValue(`(() => {
    const parse = color => color.match(/[\\d.]+/g).slice(0, 3).map(Number);
    const luminance = color => {
      const channels = parse(color).map(value => {
        const normalized = value / 255;
        return normalized <= .04045 ? normalized / 12.92 : ((normalized + .055) / 1.055) ** 2.4;
      });
      return .2126 * channels[0] + .7152 * channels[1] + .0722 * channels[2];
    };
    const button = document.querySelector('button[type="submit"]');
    const style = getComputedStyle(button);
    const a = luminance(style.color);
    const b = luminance(style.backgroundColor);
    document.querySelector('.cm-content').focus();
    const editorStyle = getComputedStyle(document.querySelector('.cm-editor'));
    return {
      shikiColor: getComputedStyle(document.querySelector('.shiki-block span')).color,
      editorColors: [...new Set([...document.querySelectorAll('.cm-line span')].map(node => getComputedStyle(node).color))].sort(),
      runContrast: (Math.max(a, b) + .05) / (Math.min(a, b) + .05),
      editorOutlineWidth: editorStyle.outlineWidth,
      ...window.__pbeColors(),
    };
  })()`);

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
  const offlineRunner = await evaluateValue(`(() => {
    const textarea = document.getElementById('code-editor');
    const panel = textarea.parentElement;
    const panelStyle = getComputedStyle(panel);
    const contentRight = panel.getBoundingClientRect().right - Number.parseFloat(panelStyle.paddingRight) - Number.parseFloat(panelStyle.borderRightWidth);
    return {
      editorLoaded: !!window.pythonByExampleEditor,
      fallbackHeight: textarea.getBoundingClientRect().height,
      fallbackOverflow: textarea.getBoundingClientRect().right - contentRight,
    };
  })()`);
  removePauseListener();
  await client.send('Fetch.disable');

  const oversizedUrl = new URL(target);
  oversizedUrl.searchParams.set('browser_oversized_fragment', Date.now());
  oversizedUrl.hash = `code=${'A'.repeat(24001)}`;
  await client.send('Page.navigate', { url: oversizedUrl.href });
  await waitFor("!!document.querySelector('.share-button')", 'oversized-fragment page');
  const fragmentBound = await evaluateValue(`({
    unchanged: document.getElementById('code-editor').value === document.getElementById('code-editor').dataset.originalCode,
    notice: document.querySelector('.output-panel code')?.textContent,
  })`);

  // Build a dependency-free runner fixture on a code-free page. The first
  // Turnstile script load fails; the second must create a fresh script,
  // execute with the fixed action, and submit the returned token.
  await client.send('Page.navigate', { url: `${new URL(target).origin}/?browser_turnstile_retry=${Date.now()}` });
  await waitFor("document.readyState === 'complete'", 'Turnstile retry fixture page');
  const turnstileRetry = await evaluateValue(`(async () => {
    document.body.innerHTML = \`
      <main>
        <form class="runner-editor" action="/examples/values">
          <textarea id="code-editor" name="code" data-original-code="print(1)">print(2)</textarea>
          <div data-turnstile-sitekey="test-key" hidden></div>
          <div class="playground-toolbar">
            <button type="submit">Run</button>
            <button type="reset" data-reset>Reset</button>
          </div>
        </form>
        <section class="output-panel"><h3>Output</h3><pre><code>Ready</code></pre></section>
      </main>\`;
    const nativeAppend = document.head.appendChild.bind(document.head);
    const nativeFetch = window.fetch;
    let scriptAttempts = 0;
    let renderAction = '';
    let widgetOptions = null;
    let removes = 0;
    document.head.appendChild = node => {
      if (node.tagName === 'SCRIPT' && node.src.includes('challenges.cloudflare.com/turnstile')) {
        scriptAttempts += 1;
        setTimeout(() => {
          if (scriptAttempts === 1) {
            node.onerror?.(new Event('error'));
            return;
          }
          window.turnstile = {
            render: (_box, options) => { widgetOptions = options; renderAction = options.action; return 7; },
            execute: () => queueMicrotask(() => widgetOptions.callback('retry-token')),
            remove: () => { removes += 1; },
            reset: () => {},
          };
          node.onload?.(new Event('load'));
        }, 0);
        return node;
      }
      return nativeAppend(node);
    };
    let fetchCount = 0;
    let submittedToken = '';
    window.fetch = async (_url, options) => {
      fetchCount += 1;
      submittedToken = options.body.get('cf-turnstile-response') || submittedToken;
      const html = fetchCount < 3
        ? '<div data-turnstile-required>Verification required</div>'
        : '<section class="output-panel"><h3>Output</h3><pre><code>retry succeeded</code></pre></section>';
      return { ok: true, status: 200, text: async () => html };
    };
    await import(${JSON.stringify(runnerAsset)} + '?retry=' + Date.now());
    const form = document.querySelector('form.runner-editor');
    const output = () => document.querySelector('.output-panel code')?.textContent || '';
    const waitUntil = async predicate => {
      for (let i = 0; i < 100; i++) {
        if (predicate()) return true;
        await new Promise(resolve => setTimeout(resolve, 10));
      }
      return false;
    };
    form.requestSubmit();
    await waitUntil(() => output().includes('press Run to retry'));
    const firstFailure = output();
    form.requestSubmit();
    await waitUntil(() => output().includes('retry succeeded'));
    const finalOutput = output();
    document.head.appendChild = nativeAppend;
    window.fetch = nativeFetch;
    return {
      scriptAttempts, fetchCount, renderAction, submittedToken, firstFailure, finalOutput,
      renderExecution: widgetOptions?.execution,
      renderHasSize: !!widgetOptions && 'size' in widgetOptions,
      removes,
      challengeHidden: document.querySelector('[data-turnstile-sitekey]').hidden,
    };
  })()`);

  // A server that keeps rejecting tokens (wrong secret, hostname, or action)
  // must cost one challenge per Run. The capped stub stops a regressed
  // challenge loop so this check reports it instead of hanging.
  await client.send('Page.navigate', { url: `${new URL(target).origin}/?browser_turnstile_rejected=${Date.now()}` });
  await waitFor("document.readyState === 'complete'", 'Turnstile rejection fixture page');
  const turnstileRejected = await evaluateValue(`(async () => {
    document.body.innerHTML = \`
      <main>
        <form class="runner-editor" action="/examples/values">
          <textarea id="code-editor" name="code" data-original-code="print(1)">print(2)</textarea>
          <div data-turnstile-sitekey="test-key" hidden></div>
          <div class="playground-toolbar">
            <button type="submit">Run</button>
            <button type="reset" data-reset>Reset</button>
          </div>
        </form>
        <section class="output-panel"><h3>Output</h3><pre><code>Ready</code></pre></section>
      </main>\`;
    const nativeFetch = window.fetch;
    let solves = 0;
    let widgetOptions = null;
    window.turnstile = {
      render: (_box, options) => { widgetOptions = options; return 9; },
      execute: () => queueMicrotask(() => widgetOptions.callback('rejected-token-' + (++solves))),
      remove: () => {},
      reset: () => {},
    };
    let fetchCount = 0;
    window.fetch = async () => {
      fetchCount += 1;
      const html = fetchCount < 20
        ? '<div data-turnstile-required>Verification required</div><section class="output-panel"><h3>Output</h3><pre><code>Turnstile verification failed. Press Run to try again.</code></pre></section>'
        : '<section class="output-panel"><h3>Output</h3><pre><code>loop cap reached</code></pre></section>';
      return { ok: true, status: 200, text: async () => html };
    };
    await import(${JSON.stringify(runnerAsset)} + '?rejected=' + Date.now());
    const form = document.querySelector('form.runner-editor');
    const output = () => document.querySelector('.output-panel code')?.textContent || '';
    const run = async () => {
      form.requestSubmit();
      for (let i = 0; i < 100 && form.hasAttribute('aria-busy'); i++) {
        await new Promise(resolve => setTimeout(resolve, 10));
      }
      return { fetchCount, solves, output: output(), busy: form.hasAttribute('aria-busy') };
    };
    const firstRun = await run();
    const secondRun = await run();
    window.fetch = nativeFetch;
    return { firstRun, secondRun };
  })()`);

  // Rendered-style contracts. Unit tests used to assert literal site.css text;
  // these measure what the browser computes for the same intentions instead.
  const origin = new URL(target).origin;
  await client.send('Emulation.setEmulatedMedia', { media: 'screen', features: [{ name: 'prefers-color-scheme', value: 'light' }] });
  await client.send('Emulation.setDeviceMetricsOverride', { width: 390, height: 1800, deviceScaleFactor: 2, mobile: true });
  await client.send('Page.navigate', { url: `${target}?browser_styles=${Date.now()}` });
  await waitFor("document.readyState === 'complete' && !!window.pythonByExampleEditor && !!document.querySelector('.copy-button') && !!document.querySelector('.share-button')", 'rendered-style page');
  // Headless pages are not focused by default, so :focus never matches.
  await client.send('Emulation.setFocusEmulationEnabled', { enabled: true });
  const rendered = await evaluateValue(`(async () => {
    const rect = element => element.getBoundingClientRect();
    const toolbar = rect(document.querySelector('.playground-toolbar'));
    const run = rect(document.querySelector('button[type="submit"]'));
    const reset = rect(document.querySelector('[data-reset]'));
    const share = rect(document.querySelector('.share-button'));
    const skip = document.querySelector('.skip-link');
    const skipBefore = rect(skip).right;
    skip.focus();
    const skipFocused = rect(skip);
    skip.blur();
    const allTransitions = [...document.querySelectorAll('*')].filter(element => {
      const style = getComputedStyle(element);
      return style.transitionProperty.split(',').some(value => value.trim() === 'all')
        && style.transitionDuration.split(',').some(value => Number.parseFloat(value) > 0);
    }).map(element => element.tagName.toLowerCase() + (element.className ? '.' + String(element.className).split(' ')[0] : ''));
    const output = document.querySelector('.output-panel code');
    const pre = document.querySelector('.output-panel pre');
    const panel = document.querySelector('.output-panel');
    const executionTime = document.querySelector('.execution-time');
    const panelRight = rect(panel).right;
    output.textContent = 'x'.repeat(600);
    const text = document.createRange();
    text.selectNodeContents(output);
    const wide = {
      textPastPanel: text.getBoundingClientRect().right - panelRight,
      pageOverflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
    };
    const oneLinePanelHeight = rect(panel).height;
    output.textContent = Array.from({ length: 60 }, (_, index) => 'line ' + index).join('\\n');
    const tall = { panelHeight: rect(panel).height, preClipped: pre.scrollHeight - pre.clientHeight };
    return {
      fontSmoothing: getComputedStyle(document.body).webkitFontSmoothing,
      headingWrap: getComputedStyle(document.querySelector('h1')).textWrapStyle || getComputedStyle(document.querySelector('h1')).textWrap,
      executionNumerals: executionTime ? getComputedStyle(executionTime).fontVariantNumeric : null,
      navUnderline: getComputedStyle(document.querySelector('nav a')).textDecorationLine,
      navTargetHeights: [...document.querySelectorAll('.nav-links a')].map(link => rect(link).height),
      buttonHeights: [run.height, reset.height, share.height],
      shareGap: share.left - reset.right,
      shareToToolbarEnd: Math.abs(toolbar.right - share.right),
      skipBefore,
      skipFocused: { left: skipFocused.left, top: skipFocused.top, width: skipFocused.width },
      allTransitions,
      wide,
      oneLinePanelHeight,
      tall,
    };
  })()`);

  // Pressed states: force :active through DevTools rather than trusting CSS text.
  await client.send('DOM.enable');
  await client.send('CSS.enable');
  async function forcedActiveTransform(selector) {
    const { root } = await client.send('DOM.getDocument', { depth: 0 });
    const { nodeId } = await client.send('DOM.querySelector', { nodeId: root.nodeId, selector });
    if (!nodeId) return `missing ${selector}`;
    await client.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active'] });
    await sleep(400); // let the 150ms transform transition finish
    const transform = await evaluateValue(`getComputedStyle(document.querySelector(${JSON.stringify(selector)})).transform`);
    await client.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] });
    return transform;
  }
  const scaleOf = transform => (/^matrix\(([-\d.]+)/.exec(transform || '') || [])[1];
  const pressed = {};
  for (const selector of ['button[type="submit"]', '.share-button', '.copy-button']) {
    pressed[selector] = await forcedActiveTransform(selector);
  }

  // Body text follows the reader's browser font size instead of a fixed 16px.
  await client.send('Page.setFontSizes', { fontSizes: { standard: 20, fixed: 16 } });
  await client.send('Page.navigate', { url: `${target}?browser_font_size=${Date.now()}` });
  await waitFor("document.readyState === 'complete'", 'font-size page');
  const userFontSize = await evaluateValue(`getComputedStyle(document.body).fontSize`);
  await client.send('Page.setFontSizes', { fontSizes: { standard: 16, fixed: 13 } });

  // Home page: the nav is visible on landing, cards press down, and the
  // translucent header has solid fallbacks for two non-motion preferences.
  await client.send('Page.navigate', { url: `${origin}/?browser_home_styles=${Date.now()}` });
  await waitFor("document.readyState === 'complete' && !!document.querySelector('.card')", 'home style page');
  const home = await evaluateValue(`(() => {
    const header = document.querySelector('header');
    const nav = document.querySelector('.nav-links');
    const navRect = nav.getBoundingClientRect();
    return {
      headerOpacity: getComputedStyle(header).opacity,
      navVisible: getComputedStyle(nav).visibility === 'visible' && getComputedStyle(nav).opacity === '1' && navRect.height > 0 && navRect.top >= 0,
      headerBackdrop: getComputedStyle(header).backdropFilter,
    };
  })()`);
  pressed['.card'] = await forcedActiveTransform('.card');
  const headerUnder = async (name, value) => {
    await client.send('Emulation.setEmulatedMedia', { media: 'screen', features: [{ name: 'prefers-color-scheme', value: 'light' }, { name, value }] });
    await sleep(400); // nav colours transition over 160ms
    return evaluateValue(`(() => {
      const header = getComputedStyle(document.querySelector('header'));
      return {
        matches: matchMedia(${JSON.stringify(`(${name}: ${value})`)}).matches,
        backdrop: header.backdropFilter,
        background: header.backgroundColor,
        navColor: getComputedStyle(document.querySelector('.nav-links a')).color,
        textColor: getComputedStyle(document.body).color,
      };
    })()`);
  };
  const reducedTransparency = await headerUnder('prefers-reduced-transparency', 'reduce');
  const moreContrast = await headerUnder('prefers-contrast', 'more');
  await client.send('Emulation.setEmulatedMedia', { media: 'screen', features: [{ name: 'prefers-color-scheme', value: 'light' }] });

  // The About page renders the design tokens live; every token it uses must exist.
  await client.send('Page.navigate', { url: `${origin}/about?browser_tokens=${Date.now()}` });
  await waitFor("document.readyState === 'complete' && !!document.querySelector('.token-grid')", 'about tokens page');
  const aboutTokens = await evaluateValue(`(() => {
    const html = document.documentElement.outerHTML;
    const used = [...new Set([...html.matchAll(/var\\((--[a-z0-9-]+)\\)/g)].map(match => match[1]))];
    const definedInline = new Set([...html.matchAll(/(--[a-z0-9-]+)\\s*:/g)].map(match => match[1]));
    const root = getComputedStyle(document.documentElement);
    const unresolved = used.filter(token => !definedInline.has(token) && !root.getPropertyValue(token).trim());
    return { used: used.length, unresolved };
  })()`);

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
  if (runnerOrdering.error) failures.push(runnerOrdering.error);
  if (runnerOrdering.finalOutput !== 'second result') failures.push(`Stale run overwrote the latest output (${runnerOrdering.finalOutput})`);
  if (runnerOrdering.resetType !== 'reset' || runnerOrdering.resetValue !== runnerOrdering.originalCode || runnerOrdering.busy) failures.push('Native Reset did not restore code and cancel runner state');
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
  if (!searchFailure.status?.includes('temporarily unavailable')) failures.push('Search fetch failure was not announced');
  if (Number.parseFloat(searchFailure.outlineWidth) < 3) failures.push('Search focus indicator is too weak');
  if (searchFailure.shikiRequests !== 0) failures.push('Code-free homepage unnecessarily loaded Shiki');
  if (lightTheme.shikiColor === darkTheme.shikiColor) failures.push('Shiki did not react to the OS theme change');
  if (JSON.stringify(lightTheme.editorColors) === JSON.stringify(darkTheme.editorColors)) failures.push('CodeMirror did not react to the OS theme change');
  if (darkTheme.runContrast < 4.5) failures.push(`Dark Run-button contrast is ${darkTheme.runContrast.toFixed(2)}:1`);
  if (Number.parseFloat(darkTheme.editorOutlineWidth) < 3) failures.push('CodeMirror focus indicator is too weak');
  if (heldCdnRequests === 0) failures.push('CDN-pending runner test did not hold an esm.sh request');
  if (offlineRunner.editorLoaded) failures.push('CDN-pending test unexpectedly loaded CodeMirror');
  if (offlineRunner.fallbackHeight < 1000) failures.push(`Shared fallback textarea did not resize (${offlineRunner.fallbackHeight}px)`);
  if (!fragmentBound.unchanged || !fragmentBound.notice?.includes('invalid or too large')) failures.push('Oversized shared-code fragment was decoded or not announced');
  if (turnstileRetry.scriptAttempts !== 2 || !turnstileRetry.firstFailure.includes('press Run to retry') || turnstileRetry.finalOutput !== 'retry succeeded') failures.push('Transient Turnstile CDN failure was cached instead of retried');
  if (turnstileRetry.renderAction !== 'run-example' || turnstileRetry.submittedToken !== 'retry-token') failures.push('Turnstile browser action/token contract failed');
  if (turnstileRetry.renderExecution !== 'execute' || turnstileRetry.renderHasSize) failures.push(`Turnstile widget is not rendered in Invisible execute mode (execution=${turnstileRetry.renderExecution}, size set=${turnstileRetry.renderHasSize})`);
  if (turnstileRetry.removes < 1 || !turnstileRetry.challengeHidden) failures.push('Turnstile widget was not removed and hidden after the challenge');
  if (networkFailure.output !== 'Run failed: network down' || networkFailure.busy || networkFailure.runDisabled) failures.push(`Network failure did not end the run with a message (${JSON.stringify(networkFailure)})`);
  if (!share.uneditedUrl || share.uneditedUrl.includes('#code=') || share.uneditedUrl !== share.pageUrl) failures.push(`Copy link for unedited code should be the plain page URL (${share.uneditedUrl})`);
  if (sourceCopy.fallbackCopied !== sourceCopy.expected || !sourceCopy.fallbackState.includes('copied')) failures.push('Source copy did not fall back to execCommand when the Clipboard API is unavailable');
  if (!sourceCopy.buttonAnchored) failures.push('Copy button is not anchored to its source cell');
  if (!(sourceCopy.statusRight <= 0) || sourceCopy.liveRegion !== 'polite') failures.push('Copy status is not an off-screen polite live announcement');
  if (sourceCopy.idleMask === 'none' || sourceCopy.copiedMask === sourceCopy.idleMask) failures.push('Copy icon is not a mask glyph that changes when copied');
  if (sourceCopy.iconPaint[0] !== sourceCopy.iconPaint[1]) failures.push('Copy icon glyph is not painted in currentColor');
  if (!arrow.blockedModifierAndButton) failures.push('Arrow navigation fired with a modifier key or from a focused button');
  if (arrowBack.length !== 2 || !arrowBack.every(Boolean)) failures.push('ArrowLeft did not walk back through previous examples');
  if (catalogEdge.hasPrev || !catalogEdge.stayed || catalogEdge.errors.length) failures.push(`ArrowLeft at the first example was not a no-op (${JSON.stringify(catalogEdge)})`);
  if (searchSuccess.expanded !== 'true' || searchSuccess.listboxRole !== 'listbox' || searchSuccess.listboxHidden || searchSuccess.options < 1) failures.push(`Search results do not expose combobox/listbox/option semantics (${JSON.stringify(searchSuccess)})`);
  if (Math.abs(darkTheme.pageLuminance - lightTheme.pageLuminance) < 0.5) failures.push('Page background did not switch between light and dark palettes');
  for (const [label, theme] of [['light', lightTheme], ['dark', darkTheme]]) {
    if (theme.textContrast < 4.5) failures.push(`${label} body text contrast is ${theme.textContrast.toFixed(2)}:1`);
    if (theme.terminalContrast < 7) failures.push(`${label} output terminal contrast is ${theme.terminalContrast.toFixed(2)}:1`);
  }
  if (lightTheme.runContrast < 4.5) failures.push(`Light Run-button contrast is ${lightTheme.runContrast.toFixed(2)}:1`);
  if (!(darkTheme.figurePaperLuminance > 0.7)) failures.push(`Dark mode does not keep marginalia figures on light paper (${darkTheme.figurePaperAlpha})`);
  if (offlineRunner.fallbackOverflow > 0.5) failures.push(`Fallback textarea overflows its panel by ${offlineRunner.fallbackOverflow.toFixed(1)}px`);
  if (rendered.fontSmoothing !== 'antialiased') failures.push('Body text is not antialiased');
  if (!String(rendered.headingWrap).includes('balance')) failures.push(`Headings do not balance their lines (${rendered.headingWrap})`);
  if (rendered.executionNumerals !== 'tabular-nums') failures.push('Execution time does not use tabular numerals');
  if (!rendered.navUnderline.includes('underline')) failures.push('Nav links are not underlined');
  if (!rendered.navTargetHeights.length || rendered.navTargetHeights.some(height => height < 40)) failures.push(`Nav link touch targets are under 40px (${rendered.navTargetHeights})`);
  if (rendered.buttonHeights.some(height => height < 40)) failures.push(`Runner buttons are under 40px tall (${rendered.buttonHeights})`);
  if (rendered.shareGap < 16 || rendered.shareToToolbarEnd > 1) failures.push(`Share button does not sit apart at the end of the toolbar (gap ${rendered.shareGap}px, ${rendered.shareToToolbarEnd}px from the end)`);
  if (rendered.skipBefore > 0) failures.push('Skip link is visible before it receives focus');
  if (rendered.skipFocused.left < 0 || rendered.skipFocused.top < 0 || rendered.skipFocused.width <= 0) failures.push('Skip link does not appear on screen when focused');
  if (rendered.allTransitions.length) failures.push(`Elements animate "transition: all" (${rendered.allTransitions.slice(0, 5)})`);
  if (rendered.wide.textPastPanel > 1 || rendered.wide.pageOverflow > 1) failures.push(`Long output overflows the output panel instead of wrapping (${JSON.stringify(rendered.wide)})`);
  if (rendered.tall.panelHeight <= rendered.oneLinePanelHeight || rendered.tall.preClipped > 1) failures.push(`Tall output is clipped instead of growing the panel (${JSON.stringify(rendered.tall)})`);
  for (const [selector, expected] of [['button[type="submit"]', '0.96'], ['.share-button', '0.96'], ['.copy-button', '0.96'], ['.card', '0.99']]) {
    if (scaleOf(pressed[selector]) !== expected) failures.push(`${selector} does not press down to scale(${expected}) when active (${pressed[selector]})`);
  }
  if (userFontSize !== '20px') failures.push(`Body text ignores the reader's browser font size (${userFontSize} at a 20px default)`);
  if (home.headerOpacity !== '1' || !home.navVisible) failures.push('Home header hides the nav on landing');
  for (const [label, state] of [['prefers-reduced-transparency', reducedTransparency], ['prefers-contrast: more', moreContrast]]) {
    if (!state.matches) failures.push(`${label} could not be emulated`);
    if (state.backdrop !== 'none' || !/^rgb\(/.test(state.background)) failures.push(`${label}: header stays translucent (${state.backdrop}, ${state.background})`);
  }
  if (moreContrast.navColor !== moreContrast.textColor) failures.push('prefers-contrast: more does not raise nav links to full text colour');
  if (aboutTokens.used < 21 || aboutTokens.unresolved.length) failures.push(`About page uses undefined design tokens (${aboutTokens.unresolved}; ${aboutTokens.used} used)`);
  const { firstRun: rejectedRun, secondRun: rejectedRetry } = turnstileRejected;
  if (rejectedRun.fetchCount !== 2 || rejectedRun.solves !== 1) failures.push(`Rejected Turnstile token re-challenged in a loop (${rejectedRun.fetchCount} POSTs, ${rejectedRun.solves} solves for one Run)`);
  if (!rejectedRun.output.includes('verification failed') || rejectedRun.busy) failures.push('Rejected Turnstile token did not end the run with the server message');
  if (rejectedRetry.fetchCount !== 4 || rejectedRetry.solves !== 2) failures.push('A new Run after a rejected token did not earn exactly one fresh challenge');

  console.log(JSON.stringify({
    runnerInteraction: interaction.result.value,
    runnerOrdering,
    share: { codeLength: share.code.length, urlLength: share.url.length, editorHeight: share.editorHeight },
    restored,
    sourceCopy: { copiedLength: sourceCopy.copied.length, state: sourceCopy.state, status: sourceCopy.status },
    arrow,
    searchWidths,
    searchFailure,
    lightTheme,
    darkTheme,
    offlineRunner,
    fragmentBound,
    turnstileRetry,
    turnstileRejected,
    heldCdnRequests,
    networkFailure,
    arrowBack,
    catalogEdge,
    searchSuccess,
    rendered,
    pressed,
    userFontSize,
    home,
    reducedTransparency,
    moreContrast,
    aboutTokens,
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
