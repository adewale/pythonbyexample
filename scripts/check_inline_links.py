#!/usr/bin/env python3
"""Check inline links in example prose resolve to real pages.

`render_inline` (src/textfmt.py) renders [text](/examples/slug) and
[text](/journeys/slug) as anchors and leaves every other [text](target)
literal. This gate fails the build for:

- link syntax whose target is not an internal /examples or /journeys
  path (it would ship as literal bracket text);
- internal links pointing at a slug that does not exist;
- a page linking to itself.
"""
from __future__ import annotations

import re

from _common import EXAMPLES_DIR, ROOT, fail, load_catalog

LINK_RE = re.compile(r"\[([^\[\]]+)\]\(([^()\s]+)\)")
INTERNAL_RE = re.compile(r"^/(examples|journeys)/([a-z0-9-]+)$")


def journey_slugs() -> set[str]:
    import sys

    sys.path.insert(0, str(ROOT / "src"))
    from app import JOURNEYS_BY_SLUG

    return set(JOURNEYS_BY_SLUG)


def main() -> int:
    _, examples = load_catalog()
    example_slugs = {example["slug"] for example in examples}
    journeys = journey_slugs()
    errors: list[str] = []
    for example in examples:
        slug = example["slug"]
        path = EXAMPLES_DIR / f"{slug}.md"
        surfaces: list[tuple[int, str]] = [(1, paragraph) for paragraph in example["explanation"]]
        surfaces += [(1, note) for note in example.get("notes", [])]
        for cell in example["cells"]:
            surfaces += [(cell.get("line", 1), paragraph) for paragraph in cell.get("prose", [])]
        for line, text in surfaces:
            for match in LINK_RE.finditer(text):
                label, target = match.group(1), match.group(2)
                internal = INTERNAL_RE.match(target)
                if not internal:
                    errors.append(
                        f"{path}:{line}: link [{label}]({target}) is not an internal "
                        f"/examples or /journeys path and would render as literal text"
                    )
                    continue
                kind, target_slug = internal.group(1), internal.group(2)
                known = example_slugs if kind == "examples" else journeys
                if target_slug not in known:
                    errors.append(f"{path}:{line}: link [{label}]({target}) points at an unknown {kind} slug")
                if kind == "examples" and target_slug == slug:
                    errors.append(f"{path}:{line}: page links to itself: [{label}]({target})")
    return fail(errors, f"Inline-link check OK ({len(examples)} examples).")


if __name__ == "__main__":
    raise SystemExit(main())
