#!/usr/bin/env python3
"""Build reviewable social-card inputs and provenance for committed JPEG cards.

Chrome JPEG bytes vary by platform, so freshness is checked from the deterministic
HTML inputs rather than a byte-for-byte raster comparison. ``make social-cards``
updates the HTML, JPEGs, and committed provenance manifest; ``--check`` verifies
that the committed JPEG set and provenance still match the current site data.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.app import JOURNEYS, PYTHON_VERSION, list_examples  # noqa: E402
from src.marginalia import render_first_figure  # noqa: E402

CARD_DIR = ROOT / "build" / "social-cards"
OUTPUT_DIR = ROOT / "public" / "og"
PROVENANCE_PATH = OUTPUT_DIR / "manifest.json"
CARD_WIDTH = 1200
CARD_HEIGHT = 630
PROVENANCE_VERSION = 1

_CARD_CSS = """
  * { box-sizing: border-box; margin: 0; }
  body { width: 1200px; height: 630px; overflow: hidden; display: flex; align-items: stretch; gap: 48px; padding: 64px 72px; color: #521000; font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", \"DejaVu Sans\", sans-serif; background: radial-gradient(circle at top left, rgba(255, 72, 1, 0.12), transparent 40rem), #F5F1EB; }
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
  .motif { color: #FF4801; font-family: ui-monospace, \"DejaVu Sans Mono\", monospace; font-size: 150px; font-weight: 800; }
"""


def _card_shell(body: str) -> str:
    return "<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">" f"<style>{_CARD_CSS}</style></head><body>{body}</body></html>\n"


def _card_body(*, eyebrow: str, title: str, summary: str, figure_svg: str = "") -> str:
    figure = f'<div class="figure"><div class="figure-paper">{figure_svg}</div></div>' if figure_svg else '<div class="figure"><div class="figure-paper"><span class="motif">&gt;py</span></div></div>'
    title_class = ' class="long"' if len(title) > 18 else ""
    return (
        '<div class="copy">'
        f'<p class="eyebrow">{html.escape(eyebrow)}</p>'
        f"<h1{title_class}>{html.escape(title)}</h1>"
        f'<p class="summary">{html.escape(summary)}</p>'
        f'<p class="brand"><strong>pythonbyexample.dev</strong> <span>· editable examples · Python {html.escape(PYTHON_VERSION)}</span></p>'
        "</div>" + figure
    )


def render_social_card_html(example: dict) -> str:
    return _card_shell(_card_body(eyebrow=f"Python By Example · {example['section']}", title=example["title"], summary=example["summary"], figure_svg=render_first_figure(example["slug"])))


def render_journey_social_card_html(journey: dict) -> str:
    return _card_shell(_card_body(eyebrow="Python By Example · Journey", title=journey["title"], summary=journey["summary"]))


def render_home_card_html() -> str:
    return _card_shell(_card_body(eyebrow="Learn Python by running it", title="Python By Example", summary=f"{len(list_examples())} concise, editable Python {PYTHON_VERSION} examples with verified output."))


def card_html() -> dict[str, str]:
    cards = {"home": render_home_card_html()}
    cards.update({example["slug"]: render_social_card_html(example) for example in list_examples()})
    cards.update({f"journey-{journey['slug']}": render_journey_social_card_html(journey) for journey in JOURNEYS})
    return cards


def provenance(cards: dict[str, str]) -> dict[str, object]:
    return {"version": PROVENANCE_VERSION, "inputs": {f"{name}.jpg": hashlib.sha256(source.encode()).hexdigest() for name, source in sorted(cards.items())}}


def check_current(cards: dict[str, str]) -> list[str]:
    failures: list[str] = []
    expected = provenance(cards)
    try:
        actual = json.loads(PROVENANCE_PATH.read_text())
    except (OSError, ValueError):
        actual = None
    if actual != expected:
        failures.append("social-card provenance is stale or missing; run make social-cards")
    expected_files = set(expected["inputs"])
    actual_files = {path.name for path in OUTPUT_DIR.glob("*.jpg")}
    for name in sorted(expected_files - actual_files):
        failures.append(f"missing social card {name}; run make social-cards")
    for name in sorted(actual_files - expected_files):
        failures.append(f"unexpected stale social card {name}; run make social-cards")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify committed JPEG provenance without writing files")
    args = parser.parse_args()
    cards = card_html()
    if args.check:
        failures = check_current(cards)
        if failures:
            print("\n".join(f"FAIL: {failure}" for failure in failures), file=sys.stderr)
            return 1
        print(f"Social-card provenance OK ({len(cards)} cards).")
        return 0
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {name: f"{name}.html" for name in sorted(cards)}
    for name, source in cards.items():
        (CARD_DIR / manifest[name]).write_text(source)
    (CARD_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PROVENANCE_PATH.write_text(json.dumps(provenance(cards), indent=2, sort_keys=True) + "\n")
    print(f"Wrote {len(cards)} social-card HTML files and provenance manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
