const MAX_SHARE_FRAGMENT_CHARS = 24000;
const TURNSTILE_ACTION = 'run-example';

function initializeRunner() {
  const textarea = document.getElementById('code-editor');
  const form = document.querySelector('form.runner-editor');
  if (!textarea || !form) return;

  const originalCode = textarea.dataset.originalCode ?? textarea.defaultValue;
  const resizeFallbackEditor = () => {
    // When the CDN-backed editor is unavailable, keep a shared multi-line
    // payload visible in the native textarea instead of leaving it at the
    // authored example's height.
    textarea.style.height = 'auto';
    textarea.style.height = `${Math.max(textarea.scrollHeight, 18 * 16)}px`;
  };
  const setCode = (value) => {
    textarea.value = value;
    resizeFallbackEditor();
    window.pythonByExampleEditor?.setValue(value);
  };

  let cancelActiveRun = () => {};
  const resetButton = form.querySelector('[data-reset]');
  if (resetButton) {
    resetButton.addEventListener('click', () => {
      cancelActiveRun();
      setCode(originalCode);
      window.pythonByExampleEditor?.focus();
    });
  }

  let sharedCodeLoaded = false;
  let sharedCodeRejected = false;
  const hash = new URL(window.location.href).hash;
  if (hash.startsWith('#code=')) {
    const encodedCode = hash.slice(6);
    if (encodedCode.length > MAX_SHARE_FRAGMENT_CHARS) {
      sharedCodeRejected = true;
    } else {
      try {
        setCode(decodeURIComponent(escape(atob(encodedCode))));
        sharedCodeLoaded = textarea.value !== originalCode;
      } catch (_) {
        sharedCodeRejected = true;
      }
    }
  }

  // Share the current editor code as the #code= fragment the loader
  // above has accepted since day one; unedited code shares the clean
  // page URL. The encoder mirrors the decoder exactly.
  async function copyTextToClipboard(text) {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }
    const holder = document.createElement('textarea');
    holder.value = text;
    holder.setAttribute('readonly', '');
    holder.style.position = 'fixed';
    holder.style.left = '-9999px';
    document.body.appendChild(holder);
    holder.select();
    const copied = document.execCommand('copy');
    holder.remove();
    if (!copied) throw new Error('execCommand copy failed');
  }

  const toolbar = form.querySelector('.playground-toolbar');
  if (toolbar) {
    const shareButton = document.createElement('button');
    shareButton.type = 'button';
    shareButton.className = 'tool-button share-button';
    shareButton.textContent = 'Copy link';
    shareButton.setAttribute('aria-live', 'polite');
    shareButton.setAttribute('aria-label', 'Copy a link to this example with the current code');
    let shareRestore = null;
    shareButton.addEventListener('click', async () => {
      window.pythonByExampleEditor?.syncTextarea();
      const code = textarea.value;
      const pageUrl = window.location.origin + window.location.pathname;
      const url = code === originalCode ? pageUrl : pageUrl + '#code=' + btoa(unescape(encodeURIComponent(code)));
      clearTimeout(shareRestore);
      let feedback = 'Link copied';
      if (url.length > 8000) {
        feedback = 'Code too long to link';
      } else {
        try { await copyTextToClipboard(url); } catch (_) { feedback = 'Copy failed'; }
      }
      shareButton.textContent = feedback;
      shareRestore = setTimeout(() => { shareButton.textContent = 'Copy link'; }, 1600);
    });
    toolbar.append(shareButton);
  }

  const outputPanel = document.querySelector('.output-panel');
  if (!outputPanel) return;
  if (sharedCodeLoaded || sharedCodeRejected) {
    outputPanel.querySelector('h3').textContent = 'Output';
    outputPanel.querySelector('code').textContent = sharedCodeLoaded
      ? 'This link included edited code. Press Run to execute it.'
      : 'The shared-code fragment was invalid or too large, so the authored example was kept.';
  }
  const challengeBox = document.querySelector('[data-turnstile-sitekey]');
  let turnstileWidgetId = null;
  let loadingTurnstile = null;

  function loadTurnstile() {
    if (window.turnstile) return Promise.resolve();
    if (loadingTurnstile) return loadingTurnstile;
    loadingTurnstile = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit';
      script.async = true;
      script.defer = true;
      script.onload = () => {
        if (window.turnstile) {
          resolve();
          return;
        }
        loadingTurnstile = null;
        script.remove();
        reject(new Error('Turnstile loaded without its browser API'));
      };
      script.onerror = () => {
        loadingTurnstile = null;
        script.remove();
        reject(new Error('Turnstile failed to load; press Run to retry'));
      };
      document.head.appendChild(script);
    });
    return loadingTurnstile;
  }

  function removeTurnstile() {
    if (!challengeBox) return;
    if (window.turnstile && turnstileWidgetId !== null) {
      try {
        turnstile.remove(turnstileWidgetId);
      } catch (_) {
        try {
          turnstile.reset(turnstileWidgetId);
        } catch (_) {
          // The widget is already gone.
        }
      }
    }
    turnstileWidgetId = null;
    challengeBox.hidden = true;
    challengeBox.innerHTML = '';
  }

  async function requestTurnstileToken(signal) {
    if (!challengeBox) throw new Error('Turnstile challenge is not configured');
    await loadTurnstile();
    if (signal.aborted) throw new DOMException('Run cancelled', 'AbortError');
    challengeBox.hidden = false;
    return new Promise((resolve, reject) => {
      let settled = false;
      const finish = (callback, value) => {
        if (settled) return;
        settled = true;
        signal.removeEventListener('abort', onAbort);
        removeTurnstile();
        callback(value);
      };
      const onAbort = () => finish(reject, new DOMException('Run cancelled', 'AbortError'));
      signal.addEventListener('abort', onAbort, { once: true });
      challengeBox.innerHTML = '';
      turnstileWidgetId = turnstile.render(challengeBox, {
        sitekey: challengeBox.dataset.turnstileSitekey,
        action: TURNSTILE_ACTION,
        execution: 'execute',
        callback: token => finish(resolve, token),
        'error-callback': () => finish(reject, new Error('Turnstile challenge failed')),
        'expired-callback': () => finish(reject, new Error('Turnstile challenge expired')),
      });
      turnstile.execute(turnstileWidgetId);
    });
  }

  function responseErrorMessage(response, body) {
    if (response.status === 413) {
      return 'Submitted code is too large (over 100 kB). Trim it and run again.';
    }
    const document = new DOMParser().parseFromString(body, 'text/html');
    return document.querySelector('.output-panel code')?.textContent?.trim()
      || body.trim()
      || `HTTP ${response.status}`;
  }

  let latestRunId = 0;
  let activeController = null;
  const runButton = form.querySelector('button[type="submit"]');

  async function submitRun(runId, signal, turnstileToken = '') {
    window.pythonByExampleEditor?.syncTextarea();
    const formData = new FormData(form);
    if (turnstileToken) formData.set('cf-turnstile-response', turnstileToken);
    const response = await fetch(form.action, {
      method: 'POST',
      body: new URLSearchParams(formData),
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      signal,
    });
    const html = await response.text();
    if (runId !== latestRunId) return;
    if (!response.ok) throw new Error(responseErrorMessage(response, html));
    const document = new DOMParser().parseFromString(html, 'text/html');
    const challengeRequired = document.querySelector('[data-turnstile-required]');
    if (challengeRequired) {
      outputPanel.querySelector('code').textContent = challengeRequired.textContent
        || 'Verification required before running edited code…';
      const token = await requestTurnstileToken(signal);
      if (runId !== latestRunId) return;
      return submitRun(runId, signal, token);
    }
    const nextOutput = document.querySelector('.output-panel');
    if (nextOutput) outputPanel.innerHTML = nextOutput.innerHTML;
  }

  cancelActiveRun = () => {
    latestRunId += 1;
    activeController?.abort();
    activeController = null;
    removeTurnstile();
    form.removeAttribute('aria-busy');
    if (runButton) runButton.disabled = false;
  };

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    activeController?.abort();
    const runId = ++latestRunId;
    const controller = new AbortController();
    activeController = controller;
    outputPanel.removeAttribute('data-output-placeholder');
    outputPanel.querySelector('code').textContent = 'Running in a Dynamic Python Worker…';
    form.setAttribute('aria-busy', 'true');
    if (runButton) runButton.disabled = true;
    try {
      await submitRun(runId, controller.signal);
    } catch (error) {
      if (runId === latestRunId && error.name !== 'AbortError') {
        removeTurnstile();
        outputPanel.querySelector('code').textContent = `Run failed: ${error.message}`;
      }
    } finally {
      if (runId === latestRunId) {
        activeController = null;
        form.removeAttribute('aria-busy');
        if (runButton) runButton.disabled = false;
      }
    }
  });
}

// layout.html emits this async module after the page content, so its targets
// are already parsed. Do not wait for DOMContentLoaded: the head's CDN-backed
// editor module can otherwise hold that event while Run/Reset/share remain dead.
initializeRunner();

// Left/right arrows page through the catalog via the existing
// rel=prev/next links. Modifier keys and any editable surface are
// ignored so the shortcut never interferes with editing.
document.addEventListener('keydown', (event) => {
  if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
  if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
  const target = event.target;
  if (target instanceof Element && target.closest('input, textarea, select, button, .cm-editor, [contenteditable="true"]')) return;
  const codeField = document.getElementById('code-editor');
  if (codeField && codeField.value !== (codeField.dataset.originalCode ?? codeField.defaultValue)) return;
  const link = document.querySelector(event.key === 'ArrowLeft' ? '.example-nav a[rel="prev"]' : '.example-nav a[rel="next"]');
  if (link) window.location.href = link.href;
});
