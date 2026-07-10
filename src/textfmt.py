"""Inline prose rendering shared by page templates and figure captions.

Prose supports two inline forms:

- `code` spans, rendered as <code class="syntax-inline">;
- [text](/examples/slug) and [text](/journeys/slug) links, rendered as
  site-internal anchors. Any other link target stays literal text so a
  typo cannot ship as a broken anchor; scripts/check_inline_links.py
  rejects it at build time.
"""
from __future__ import annotations

import html
import re

_INTERNAL_LINK_RE = re.compile(r"\[([^\[\]]+)\]\((/(?:examples|journeys)/[a-z0-9-]+)\)")


def _render_text_segment(text: str) -> str:
    rendered: list[str] = []
    position = 0
    for match in _INTERNAL_LINK_RE.finditer(text):
        rendered.append(html.escape(text[position : match.start()]))
        label, href = match.group(1), match.group(2)
        rendered.append(f'<a class="text-link" href="{html.escape(href)}">{html.escape(label)}</a>')
        position = match.end()
    rendered.append(html.escape(text[position:]))
    return "".join(rendered)


def render_inline(text: str) -> str:
    parts = text.split("`")
    rendered = []
    for index, part in enumerate(parts):
        if index % 2:
            rendered.append(f'<code class="syntax-inline">{html.escape(part)}</code>')
        else:
            rendered.append(_render_text_segment(part))
    return "".join(rendered)
