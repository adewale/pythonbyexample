// Read-only syntax highlighting, bundled into public/highlighter.js by
// scripts/build_browser_bundles.mjs. Only the Python grammar and the two
// themes the site uses are included, with Shiki's JavaScript regex engine,
// so no WebAssembly and no third-party request is needed at runtime.
import { createHighlighterCore } from 'shiki/core';
import { createJavaScriptRegexEngine } from 'shiki/engine/javascript';
import python from 'shiki/langs/python.mjs';
import githubDark from 'shiki/themes/github-dark.mjs';
import githubLight from 'shiki/themes/github-light.mjs';

let highlighter = null;

export async function codeToHtml(source, { theme }) {
  highlighter ??= createHighlighterCore({
    themes: [githubLight, githubDark],
    langs: [python],
    engine: createJavaScriptRegexEngine(),
  });
  return (await highlighter).codeToHtml(source, { lang: 'python', theme });
}
