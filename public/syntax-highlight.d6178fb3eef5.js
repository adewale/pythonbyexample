// Copy affordance for read-only source blocks. The button attaches to
// the .cell-source wrapper (not the <pre>) so the Shiki replacement
// below leaves it in place, and it is injected client-side so no-JS
// pages render no dead buttons.
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
    } catch (error) {
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

// Shiki is imported dynamically so a CDN failure degrades to plain
// server-rendered code while the copy buttons above keep working.
let codeToHtml = null;
try {
  ({ codeToHtml } = await import('https://esm.sh/shiki@1.29.2'));
} catch (error) {
  codeToHtml = null;
}

const blocks = codeToHtml ? document.querySelectorAll('pre code.language-python') : [];

for (const block of blocks) {
  const source = block.textContent;
  try {
    const highlighted = await codeToHtml(source, {
      lang: 'python',
      themes: { light: 'github-light', dark: 'github-dark' },
      defaultColor: 'light',
    });
    const wrapper = document.createElement('div');
    wrapper.innerHTML = highlighted;
    const shikiPre = wrapper.firstElementChild;
    if (!shikiPre) continue;
    shikiPre.classList.add('shiki-block');
    const currentPre = block.closest('pre');
    currentPre.replaceWith(shikiPre);
  } catch (error) {
    block.dataset.highlightFailed = 'true';
  }
}
