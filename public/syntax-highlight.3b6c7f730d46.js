import { codeToHtml } from 'https://esm.sh/shiki@1.29.2';

const blocks = document.querySelectorAll('pre code.language-python');

for (const block of blocks) {
  const source = block.textContent;
  try {
    const highlighted = await codeToHtml(source, {
      lang: 'python',
      theme: 'github-light',
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
