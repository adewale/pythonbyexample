#!/usr/bin/env python3
"""Compose 1200x630 social-card HTML for every example page.

Each card reuses the example's curated marginalia figure so shared
links carry the same diagram the page teaches with. This script writes
self-contained HTML files; scripts/build_social_cards.mjs rasterizes
them to public/og/<slug>.png with headless Chrome. Run both via
`make social-cards`.

The PNGs are committed. They are intentionally NOT part of
check-generated: rasterized bytes vary across Chrome versions, so the
parity gate would flap. The SEO linter instead checks that a card file
exists for every page that references one.
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.app import PYTHON_VERSION, list_examples  # noqa: E402
from src.marginalia import render_first_figure  # noqa: E402

CARD_DIR = ROOT / "build" / "social-cards"
CARD_WIDTH = 1200
CARD_HEIGHT = 630

_CARD_CSS = """
  * { box-sizing: border-box; margin: 0; }
  body {
    width: 1200px; height: 630px; overflow: hidden;
    display: flex; align-items: stretch; gap: 48px;
    padding: 64px 72px;
    color: #521000;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "DejaVu Sans", sans-serif;
    background: radial-gradient(circle at top left, rgba(255, 72, 1, 0.12), transparent 40rem), #F5F1EB;
  }
  .copy { flex: 1.2; display: flex; flex-direction: column; min-width: 0; }
  .eyebrow { color: #FF4801; font-size: 26px; font-weight: 750; letter-spacing: .08em; text-transform: uppercase; }
  h1 { margin-top: 18px; font-size: 78px; line-height: 1.02; letter-spacing: -0.04em; }
  h1.long { font-size: 58px; }
  .summary { margin-top: 26px; color: rgba(82, 16, 0, 0.7); font-size: 30px; line-height: 1.4; max-width: 22ch; }
  .brand { margin-top: auto; font-size: 26px; }
  .brand strong { font-weight: 800; }
  .brand span { color: rgba(82, 16, 0, 0.7); }
  .figure { flex: 1; display: flex; align-items: center; justify-content: center; min-width: 0; }
  .figure-paper { display: flex; align-items: center; justify-content: center; padding: 28px; border: 1px solid #EBD5C1; border-radius: 20px; background: #FFFBF5; box-shadow: 0 2px 6px rgba(82, 16, 0, 0.05), 0 18px 48px rgba(82, 16, 0, 0.07); }
  .figure svg { display: block; max-width: 420px; max-height: 460px; width: auto; height: auto; }
  .motif { color: #FF4801; font-family: ui-monospace, "DejaVu Sans Mono", monospace; font-size: 150px; font-weight: 800; }
"""


def _card_shell(body: str) -> str:
    return (
        "<!doctype html>\n"
        '<html lang="en"><head><meta charset="utf-8">'
        f"<style>{_CARD_CSS}</style></head>"
        f"<body>{body}</body></html>\n"
    )


def render_social_card_html(example: dict) -> str:
    figure_svg = render_first_figure(example["slug"])
    figure = (
        f'<div class="figure"><div class="figure-paper">{figure_svg}</div></div>'
        if figure_svg
        else '<div class="figure"><div class="figure-paper"><span class="motif">&gt;py</span></div></div>'
    )
    title_class = ' class="long"' if len(example["title"]) > 18 else ""
    body = (
        '<div class="copy">'
        f'<p class="eyebrow">Python By Example · {html.escape(example["section"])}</p>'
        f"<h1{title_class}>{html.escape(example['title'])}</h1>"
        f'<p class="summary">{html.escape(example["summary"])}</p>'
        f'<p class="brand"><strong>pythonbyexample.dev</strong> <span>· editable examples · Python {html.escape(PYTHON_VERSION)}</span></p>'
        "</div>"
        f"{figure}"
    )
    return _card_shell(body)


def render_home_card_html() -> str:
    body = (
        '<div class="copy">'
        '<p class="eyebrow">Learn Python by running it</p>'
        "<h1>Python By Example</h1>"
        f'<p class="summary">{len(list_examples())} concise, editable Python {html.escape(PYTHON_VERSION)} examples with verified output.</p>'
        '<p class="brand"><strong>pythonbyexample.dev</strong> <span>· run every example in your browser</span></p>'
        "</div>"
        '<div class="figure"><div class="figure-paper"><span class="motif">&gt;py</span></div></div>'
    )
    return _card_shell(body)


def main() -> None:
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {"home": "home.html"}
    (CARD_DIR / "home.html").write_text(render_home_card_html())
    for example in list_examples():
        name = f"{example['slug']}.html"
        (CARD_DIR / name).write_text(render_social_card_html(example))
        manifest[example["slug"]] = name
    (CARD_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))
    print(f"Wrote {len(manifest)} social-card HTML files to {CARD_DIR.relative_to(ROOT)}/.")


if __name__ == "__main__":
    main()
