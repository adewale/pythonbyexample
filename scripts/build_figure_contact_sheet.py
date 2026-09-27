#!/usr/bin/env python3
"""Render a before/after contact sheet of every figure a branch changed.

Reviewer tooling for figure pull requests. The script extracts the base
revision's ``src/`` and registry with ``git archive``, renders every
attached example figure and journey-section figure from both trees,
and keeps the ones whose drawing differs once colour, font and
text-length attributes are ignored (those change for every figure when
the palette moves, and are not what a reviewer needs to compare). Each
row shows the base drawing beside the head drawing with its caption and
element count, so "is the new figure busier?" is answered by a number
as well as a picture.

    uv run --python 3.13 scripts/build_figure_contact_sheet.py --base main \\
        --output docs/pr-evidence/diagram-upgrade-contact-sheet

writes a light and a dark PNG captured from a ``build/`` HTML page through
``scripts/capture_browser_screenshot.mjs``. In dark mode the base column
sits on the light paper chip the site used to draw, so both columns show
what a reader actually saw.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

DUMP = r"""
import json, sys
sys.path.insert(0, sys.argv[1])
from src.marginalia import ATTACHMENTS, FIGURES, SECTION_FIGURES, _render_svg
rows = {}
for slug, items in ATTACHMENTS.items():
    rows[f"example · {slug}"] = [
        {"figure": name, "caption": caption or "", "svg": _render_svg(name)} for _anchor, name, caption in items
    ]
for section, (name, caption) in SECTION_FIGURES.items():
    rows[f"journey section · {section}"] = [{"figure": name, "caption": caption, "svg": _render_svg(name)}]
print(json.dumps(rows))
"""

STRIP = re.compile(r'\s(?:fill|stroke|font-family|textLength|lengthAdjust)="[^"]*"')
ELEMENT = re.compile(r"<(?:rect|text|line|circle|path|polygon)\b")


def dump(tree: Path) -> dict[str, list[dict[str, str]]]:
    out = subprocess.run(
        [sys.executable, "-c", DUMP, str(tree)], capture_output=True, text=True, check=True, cwd=tree
    )
    return json.loads(out.stdout)


def extract(base: str) -> Path:
    tree = Path(tempfile.mkdtemp(prefix="figure-sheet-base-"))
    archive = subprocess.run(["git", "archive", base, "src", "docs/quality-registries.toml"], cwd=ROOT, capture_output=True, check=True)
    subprocess.run(["tar", "-x", "-C", str(tree)], input=archive.stdout, check=True)
    return tree


def normalised(figures: list[dict[str, str]]) -> str:
    return "|".join(STRIP.sub("", f["svg"]).replace(" ", "") for f in figures)


def elements(figures: list[dict[str, str]]) -> int:
    return sum(len(ELEMENT.findall(f["svg"])) for f in figures)


def cell(figures: list[dict[str, str]], rationale: str | None) -> str:
    if not figures:
        note = f"<p class='caption'>{html.escape(rationale)}</p>" if rationale else ""
        return f"<td class='none'><p class='eyebrow'>no figure</p>{note}</td>"
    parts = []
    for f in figures:
        parts.append(
            f"<figure>{f['svg']}<figcaption>{html.escape(f['caption'])}</figcaption></figure>"
        )
    names = " + ".join(html.escape(f["figure"]) for f in figures)
    return f"<td><p class='eyebrow'>{names} · {elements(figures)} elements</p>{''.join(parts)}</td>"


def render(base: str, before: dict, after: dict, rationales: dict[str, str]) -> str:
    from src.marginalia_grammar import FIGURE_TOKENS_DARK, FIGURE_TOKENS_LIGHT, figure_token_css

    rows = []
    for key in list(before) + [k for k in after if k not in before]:
        b, a = before.get(key, []), after.get(key, [])
        if normalised(b) == normalised(a):
            continue
        slug = key.split(" · ", 1)[1]
        rows.append(f"<tr><th>{html.escape(key)}</th>{cell(b, None)}{cell(a, rationales.get(slug))}</tr>")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Figure contact sheet</title>
<style>
  :root {{ color-scheme: light dark; --paper: #F5F1EB; --ink: #521000; --muted: rgba(82,16,0,.7); --rule: #EBD5C1; --chip: transparent; {figure_token_css(FIGURE_TOKENS_LIGHT)} }}
  @media (prefers-color-scheme: dark) {{ :root {{ --paper: #1B120B; --ink: #F3E7DC; --muted: rgba(243,231,220,.72); --rule: #43301F; --chip: #F5F1EB; {figure_token_css(FIGURE_TOKENS_DARK)} }} }}
  body {{ margin: 0; background: var(--paper); color: var(--ink); font: 14px/1.5 system-ui, -apple-system, 'Segoe UI', sans-serif; }}
  .sheet {{ width: 1460px; padding: 28px 32px 40px; box-sizing: border-box; }}
  h1 {{ font-size: 22px; margin: 0 0 4px; }}
  p.meta {{ margin: 0 0 20px; color: var(--muted); }}
  table {{ border-collapse: collapse; width: 100%; table-layout: fixed; }}
  th, td {{ vertical-align: top; text-align: left; padding: 16px 14px; border-top: 1px solid var(--rule); }}
  thead th {{ border-top: 0; font-size: 12px; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); }}
  tbody th {{ width: 200px; font-weight: 600; font-size: 13px; }}
  td.none {{ color: var(--muted); }}
  .eyebrow {{ margin: 0 0 8px; font-size: 11px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }}
  figure {{ margin: 0 0 10px; }}
  svg {{ display: block; max-width: 100%; height: auto; }}
  td:nth-child(2) svg {{ background: var(--chip); padding: 8px; border-radius: 6px; }}
  figcaption, .caption {{ margin-top: 8px; font-style: italic; font-size: 13px; color: var(--muted); max-width: 52ch; }}
</style></head><body><div class="sheet">
<h1>Figures changed since <code>{html.escape(base)}</code></h1>
<p class="meta">Left: the figure as rendered on <code>{html.escape(base)}</code> (in dark mode, on the light chip the site used to draw). Right: this branch. Element counts are drawable SVG elements; captions are the shipped figcaptions.</p>
<table><thead><tr><th>page</th><th>before</th><th>after</th></tr></thead><tbody>
{''.join(rows)}
</tbody></table></div></body></html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base", default="main")
    parser.add_argument("--output", required=True, help="PNG path stem; writes <stem>-light.png and <stem>-dark.png")
    args = parser.parse_args()

    before = dump(extract(args.base))
    after = dump(ROOT)
    from src.editorial_registry import load_registry

    rationales = {slug: entry["reason"] for slug, entry in load_registry().get("no_figure_rationales", {}).items()}
    stem = Path(args.output).resolve()
    stem.parent.mkdir(parents=True, exist_ok=True)
    page = ROOT / "build" / "figure-contact-sheet" / f"{stem.name}.html"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(render(args.base, before, after, rationales))
    changed = sum(1 for k in set(before) | set(after) if normalised(before.get(k, [])) != normalised(after.get(k, [])))
    print(f"wrote {page.relative_to(ROOT)} — {changed} changed figure rows")
    for scheme in ("light", "dark"):
        output = stem.parent / f"{stem.name}-{scheme}.png"
        env = {
            **os.environ,
            "TARGET_URL": page.resolve().as_uri(),
            "CAPTURE_SELECTOR": ".sheet",
            "WIDTH": "1500",
            "HEIGHT": "12000",
            "COLOR_SCHEME": scheme,
            "OUTPUT": str(output),
        }
        subprocess.run(["node", str(ROOT / "scripts" / "capture_browser_screenshot.mjs")], env=env, check=True, capture_output=True)
        print(f"wrote {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
