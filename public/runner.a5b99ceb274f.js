function initializeRunner() {
  const textarea = document.getElementById('code-editor');
  const form = document.querySelector('form.runner-editor');
  if (!textarea || !form) return;

  const originalCode = textarea.dataset.originalCode ?? textarea.defaultValue;
  const setCode = (value) => {
    textarea.value = value;
    window.pythonByExampleEditor?.setValue(value);
  };

  const resetButton = form.querySelector('[data-reset]');
  if (resetButton) {
    resetButton.addEventListener('click', () => {
      setCode(originalCode);
      window.pythonByExampleEditor?.focus();
    });
  }

  const hash = new URL(window.location.href).hash;
  if (hash.startsWith('#code=')) {
    try {
      setCode(decodeURIComponent(escape(atob(hash.slice(6)))));
      if (textarea.value !== originalCode) {
        const panel = document.querySelector('.output-panel');
        const heading = panel && panel.querySelector('h3');
        const code = panel && panel.querySelector('code');
        if (heading) heading.textContent = 'Output';
        if (code) code.textContent = 'This link included edited code. Press Run to execute it.';
      }
    } catch (_) {
      // Ignore malformed share fragments and leave the authored example intact.
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
      script.onload = resolve;
      script.onerror = () => reject(new Error('Turnstile failed to load'));
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

  async function requestTurnstileToken() {
    if (!challengeBox) throw new Error('Turnstile challenge is not configured');
    await loadTurnstile();
    challengeBox.hidden = false;
    return new Promise((resolve, reject) => {
      challengeBox.innerHTML = '';
      turnstileWidgetId = turnstile.render(challengeBox, {
        sitekey: challengeBox.dataset.turnstileSitekey,
        execution: 'execute',
        callback: (token) => {
          removeTurnstile();
          resolve(token);
        },
        'error-callback': () => {
          removeTurnstile();
          reject(new Error('Turnstile challenge failed'));
        },
        'expired-callback': () => {
          removeTurnstile();
          reject(new Error('Turnstile challenge expired'));
        },
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

  async function submitRun(turnstileToken = '') {
    outputPanel.removeAttribute('data-output-placeholder');
    window.pythonByExampleEditor?.syncTextarea();
    outputPanel.querySelector('code').textContent = 'Running in a Dynamic Python Worker…';
    const formData = new FormData(form);
    if (turnstileToken) formData.set('cf-turnstile-response', turnstileToken);
    const response = await fetch(form.action, {
      method: 'POST',
      body: new URLSearchParams(formData),
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
    const html = await response.text();
    if (!response.ok) throw new Error(responseErrorMessage(response, html));
    const document = new DOMParser().parseFromString(html, 'text/html');
    const challengeRequired = document.querySelector('[data-turnstile-required]');
    if (challengeRequired) {
      outputPanel.querySelector('code').textContent = challengeRequired.textContent
        || 'Verification required before running edited code…';
      return submitRun(await requestTurnstileToken());
    }
    const nextOutput = document.querySelector('.output-panel');
    if (nextOutput) outputPanel.innerHTML = nextOutput.innerHTML;
  }

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    try {
      await submitRun();
    } catch (error) {
      removeTurnstile();
      outputPanel.querySelector('code').textContent = `Run failed: ${error.message}`;
    }
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeRunner, { once: true });
} else {
  initializeRunner();
}

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
