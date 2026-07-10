// Copy affordance for read-only source blocks. The button attaches to
// the .cell-source wrapper (not the <pre>) so Shiki replacement leaves it
// in place, and it is injected client-side so no-JS pages render no dead
// controls.
async function copyText(text) {
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

for (const source of document.querySelectorAll('.cell-source')) {
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'copy-button';
  button.title = 'Copy';
  button.setAttribute('aria-label', 'Copy this source fragment');
  button.setAttribute('aria-live', 'polite');
  const icon = document.createElement('span');
  icon.className = 'copy-icon';
  icon.setAttribute('aria-hidden', 'true');
  const status = document.createElement('span');
  status.className = 'copy-status';
  button.append(icon, status);
  let restore = null;
  button.addEventListener('click', async () => {
    const code = source.querySelector('pre code') || source.querySelector('pre');
    if (!code) return;
    clearTimeout(restore);
    button.classList.remove('copied', 'failed');
    try {
      await copyText(code.textContent);
      button.classList.add('copied');
      status.textContent = 'Copied';
    } catch (_) {
      button.classList.add('failed');
      status.textContent = 'Copy failed';
    }
    restore = setTimeout(() => {
      button.classList.remove('copied', 'failed');
      status.textContent = '';
    }, 1600);
  });
  source.append(button);
}

// Read-only Python cells are the only pages that need Shiki. Avoid even
// requesting the CDN module on the home, About, and other code-free pages.
const sourceBlocks = [...document.querySelectorAll('pre code.language-python')].map((code) => ({
  source: code.textContent,
  pre: code.closest('pre'),
}));

if (sourceBlocks.length) {
  let codeToHtml = null;
  try {
    ({ codeToHtml } = await import('https://esm.sh/shiki@1.29.2'));
  } catch (_) {
    // Plain server-rendered code remains readable when the optional CDN fails.
  }

  if (codeToHtml) {
    const themePreference = window.matchMedia('(prefers-color-scheme: dark)');
    const highlight = async () => {
      const theme = themePreference.matches ? 'github-dark' : 'github-light';
      for (const block of sourceBlocks) {
        try {
          const highlighted = await codeToHtml(block.source, { lang: 'python', theme });
          const wrapper = document.createElement('div');
          wrapper.innerHTML = highlighted;
          const shikiPre = wrapper.firstElementChild;
          if (!shikiPre || !block.pre?.isConnected) continue;
          shikiPre.classList.add('shiki-block');
          block.pre.replaceWith(shikiPre);
          block.pre = shikiPre;
        } catch (_) {
          block.pre?.setAttribute('data-highlight-failed', 'true');
        }
      }
    };

    await highlight();
    themePreference.addEventListener?.('change', highlight);
  }
}
