#!/usr/bin/env python3
"""Check for copy-paste prose residue in example pages.

Three patterns indicate an unfinished edit rather than a writing choice,
and all three shipped at least once:

- the same paragraph twice in a row inside one prose block;
- cell prose that is a verbatim copy of an intro paragraph (the cell
  should describe its specific code, not repeat the page opening);
- the same note bullet stated twice in one page.

Comparison is exact after whitespace normalization; paraphrases are an
editorial judgement this gate deliberately stays out of.
"""
from __future__ import annotations

from _common import EXAMPLES_DIR, fail, load_catalog


def main() -> int:
    _, examples = load_catalog()
    errors: list[str] = []
    for example in examples:
        slug = example["slug"]
        path = EXAMPLES_DIR / f"{slug}.md"
        intro = example.get("explanation", [])
        for first, second in zip(intro, intro[1:]):
            if first == second:
                errors.append(f"{path}:1: intro repeats a paragraph verbatim: {first[:70]!r}")
        intro_set = set(intro)
        for index, cell in enumerate(example["cells"], 1):
            prose = cell.get("prose", [])
            line = cell.get("line", 1)
            for first, second in zip(prose, prose[1:]):
                if first == second:
                    errors.append(
                        f"{path}:{line}: cell {index} repeats a paragraph verbatim: {first[:70]!r}"
                    )
            for paragraph in prose:
                if paragraph in intro_set:
                    errors.append(
                        f"{path}:{line}: cell {index} prose duplicates an intro paragraph: "
                        f"{paragraph[:70]!r}"
                    )
        seen: set[str] = set()
        for note in example.get("notes", []):
            if note in seen:
                errors.append(f"{path}:1: duplicate note bullet: {note[:70]!r}")
            seen.add(note)
    return fail(errors, f"Prose-duplication check OK ({len(examples)} examples).")


if __name__ == "__main__":
    raise SystemExit(main())
