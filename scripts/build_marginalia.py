#!/usr/bin/env python3
"""Generate public/prototyping/marginalia-gestalt.html — every attached
production figure rendered as a small card so the whole library can be
reviewed at a glance.

The gestalt is a thin view over `src/marginalia.py`: every card pulls
its paint function, dimensions, score, and commentary directly from
the production registries (FIGURES, ATTACHMENTS, SCORES). No bespoke
paint code lives here — drift between "what readers see on
/examples/X" and "what reviewers see on the gestalt page" is
structurally impossible.

(Journey overview thumbnails are not rendered on this page; the
per-section journey figures are reviewed on
journey-figures-gestalt.html instead.)
"""

from __future__ import annotations

from _common import ROOT, load_catalog
from src.marginalia import ATTACHMENTS, FIGURES, SCORES
from src.marginalia_grammar import Card

OUT = ROOT / "public" / "prototyping" / "marginalia-gestalt.html"


def _example_cards() -> list[Card]:
    """One Card per attached production figure, in example order.

    The paint function, dimensions, and the exact production figcaption
    all come from FIGURES/ATTACHMENTS, so reviewers judge the same
    figure+caption pairing readers see — a caption asserting something
    the figure does not draw is visible here at a glance.
    """
    _, examples = load_catalog()
    cards: list[Card] = []
    for i, ex in enumerate(examples, start=1):
        slug = ex["slug"]
        attachments = ATTACHMENTS.get(slug)
        if not attachments:
            continue
        for _, figure_name, caption in attachments:
            paint, w, h = FIGURES[figure_name]
            card = Card(
                slug=slug,
                title=ex["title"],
                section=ex["section"],
                order=i,
                figure=paint,
                caption=caption,
                width=w,
                height=h,
            )
            score = SCORES.get(slug)
            if score is not None:
                card.score, card.score_note = score
            cards.append(card)
    return cards


EXAMPLES: list[Card] = _example_cards()


# ─── Page scaffold ─────────────────────────────────────────────────────


HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Marginalia gestalt — Python By Example</title>
<style>
  :root {
    /* Aligned with public/site.css tokens. */
    --paper: #F5F1EB;
    --ink: #521000;
    --ink-soft: rgba(82, 16, 0, 0.7);
    --rule: #EBD5C1;
  }
  *, *::before, *::after { box-sizing: border-box; }
  html, body { background: var(--paper); color: var(--ink); margin: 0; }
  body {
    font-family: 'Iowan Old Style', 'Charter', Georgia, serif;
    font-size: 14px; line-height: 1.5;
    padding: 48px 56px 96px;
    max-width: 1240px; margin: 0 auto;
  }
  header { margin-bottom: 48px; }
  h1 { font-weight: 500; font-size: 28px; margin: 0 0 8px; letter-spacing: -0.01em; }
  header p { color: var(--ink-soft); max-width: 680px; margin: 0 0 4px; }
  header p.note { font-size: 12px; }
  h2.section {
    font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase;
    color: var(--ink-soft); font-weight: 500;
    border-bottom: 1px solid var(--rule);
    padding-bottom: 8px; margin: 56px 0 24px;
  }
  .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 36px 28px; }
  .card { display: flex; flex-direction: column; gap: 4px; }
  .card .eyebrow {
    font-family: -apple-system, BlinkMacSystemFont, 'Source Sans Pro', sans-serif;
    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--ink-soft); margin: 0;
  }
  .card h3 { font-size: 15px; font-weight: 500; margin: 0; letter-spacing: -0.005em; }
  .card svg { margin-top: 8px; max-width: 100%; height: auto; overflow: visible; }
  .card .caption {
    margin: 6px 0 0; font-size: 12px; color: var(--ink);
    max-width: 44ch;
  }
  .card .note {
    margin: 6px 0 0; font-style: italic; font-size: 12px; color: var(--ink-soft);
    max-width: 38ch;
  }
  .card .score {
    margin: 6px 0 0; font-size: 11px; color: var(--ink-soft);
    font-family: -apple-system, 'Source Sans Pro', sans-serif;
  }
  .card .score::before { content: "▍ "; opacity: 0.4; }
  .card .score-high { color: var(--ink); }
  .card .score-low::before { content: "▍ "; opacity: 0.6; color: #a2604c; }
</style>
</head>
<body>
<header>
  <h1>Marginalia gestalt</h1>
  <p>Every example figure rendered from the same paint code that ships on /examples/&lt;slug&gt;.</p>
  <p class="note">Locked metrics, locked palette, locked typography. Cards compose words; words compose tokens; nothing is bespoke.</p>
</header>
"""


def render() -> str:
    out = [HEAD]
    out.append('<h2 class="section">Examples</h2>\n<div class="grid">')
    for card in EXAMPLES:
        out.append(card.render_html())
    out.append("</div>\n</body>\n</html>\n")
    return "\n".join(out)


def main() -> None:
    OUT.write_text(render())
    print(f"wrote {OUT.relative_to(ROOT)} — {len(EXAMPLES)} figure cards (from production FIGURES)")


if __name__ == "__main__":
    main()
