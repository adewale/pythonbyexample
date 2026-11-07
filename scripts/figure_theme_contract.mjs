// Rendered contract for the marginalia figure tokens.
//
// Figures paint with var(--fig-ink) and friends instead of literal colours,
// so one paint function renders in both colour schemes. That holds only if
// the page defines every token in light and dark, with the colours
// src/marginalia_grammar.py documents (the social cards and gestalt pages
// embed the same values). check_browser_layout.mjs measures each scheme on
// the rendered page with figureThemeExpression() and reports
// figureThemeFailures(); nothing here reads CSS text.
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

// The grammar's FIGURE_TOKENS_LIGHT and FIGURE_TOKENS_DARK, imported from Python.
export function documentedFigureTokens() {
  const program = 'import json; from src.marginalia_grammar import FIGURE_TOKENS_DARK, FIGURE_TOKENS_LIGHT; '
    + 'print(json.dumps({"light": FIGURE_TOKENS_LIGHT, "dark": FIGURE_TOKENS_DARK}))';
  const output = execFileSync('uv', ['run', '--python', '3.13', 'python', '-c', program], {
    cwd: root,
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  return JSON.parse(output);
}

// Runs in the page under the current colour scheme. `documented` maps each
// token to the colour the grammar gives it in that scheme.
function measureFigures(documented) {
  // Compare colours as the browser resolves them, not as they are spelled.
  const resolve = value => {
    const probe = document.createElement('span');
    probe.style.color = value;
    if (!probe.style.color) return null;
    document.body.append(probe);
    const colour = getComputedStyle(probe).color;
    probe.remove();
    return colour;
  };
  const luminance = colour => {
    const [r, g, b] = colour.match(/[\d.]+/g).slice(0, 3).map(value => {
      const channel = Number(value) / 255;
      return channel <= .04045 ? channel / 12.92 : ((channel + .055) / 1.055) ** 2.4;
    });
    return .2126 * r + .7152 * g + .0722 * b;
  };
  const contrast = (a, b) => {
    const [high, low] = [luminance(a), luminance(b)].sort((x, y) => y - x);
    return (high + .05) / (low + .05);
  };
  const pageBackground = getComputedStyle(document.body).backgroundColor;
  const svgs = [...document.querySelectorAll('.cell-banner figure svg')];
  const inherited = svgs[0] ? getComputedStyle(svgs[0]) : null;
  const tokens = {};
  for (const [name, value] of Object.entries(documented)) {
    tokens[name] = { value: inherited ? resolve(inherited.getPropertyValue(name).trim()) : null, documented: resolve(value) };
  }
  // Every stroke and fill a figure paints through a token, in document order.
  const paints = [];
  for (const node of svgs.flatMap(svg => [...svg.querySelectorAll('*')])) {
    for (const attr of ['stroke', 'fill']) {
      const token = /^var\((--fig-[a-z-]+)\)$/.exec(node.getAttribute(attr) || '')?.[1];
      if (!token) continue;
      const style = getComputedStyle(node);
      paints.push({ token, attr, painted: style[attr], tokenColour: resolve(style.getPropertyValue(token).trim()) });
    }
  }
  const ink = paints.find(paint => paint.token === '--fig-ink' && paint.attr === 'stroke')?.painted ?? null;
  return {
    figures: svgs.length,
    pageBackground,
    chips: svgs.map(svg => getComputedStyle(svg).backgroundColor),
    tokens,
    paints,
    ink,
    inkContrast: ink?.startsWith('rgb') ? contrast(ink, pageBackground) : null,
  };
}

export function figureThemeExpression(documented) {
  return `(${measureFigures.toString()})(${JSON.stringify(documented)})`;
}

export function figureThemeFailures({ light, dark }) {
  const failures = [];
  for (const [scheme, theme] of [['light', light], ['dark', dark]]) {
    if (!theme.figures) {
      failures.push(`${scheme}: no marginalia figure on the page to measure`);
      continue;
    }
    if (!(theme.inkContrast >= 4.5)) failures.push(`${scheme} marginalia figure ink contrast is ${theme.inkContrast?.toFixed(2)}:1 (ink ${theme.ink} on ${theme.pageBackground})`);
    // No light "paper chip" behind figures: the tokens do the work.
    const chips = [...new Set(theme.chips)].filter(chip => chip !== 'rgba(0, 0, 0, 0)');
    if (chips.length) failures.push(`${scheme} marginalia figures sit on a painted chip (${chips.join(', ')})`);
    for (const [name, token] of Object.entries(theme.tokens)) {
      if (!token.value) failures.push(`${scheme} figure token ${name} does not resolve to a colour`);
      else if (token.value !== token.documented) failures.push(`${scheme} figure token ${name} is ${token.value}, not the ${token.documented} src/marginalia_grammar.py documents`);
    }
    const offToken = theme.paints.filter(paint => !paint.tokenColour || paint.painted !== paint.tokenColour);
    if (offToken.length) failures.push(`${scheme}: ${offToken.length} figure strokes/fills do not paint their token's colour (${offToken.slice(0, 3).map(paint => `${paint.attr}=var(${paint.token}) painted ${paint.painted}`).join('; ')})`);
  }
  // Dark mode recolours figures through the tokens, not with a second palette.
  const kept = light.paints.filter((paint, index) => paint.painted === dark.paints[index]?.painted);
  if (!light.paints.length || light.paints.length !== dark.paints.length || kept.length) {
    failures.push(`Marginalia figures did not recolour with the dark palette (${kept.length} of ${light.paints.length} strokes/fills kept their light colour: ${[...new Set(kept.map(paint => paint.token))].join(', ')})`);
  }
  return failures;
}
