#!/usr/bin/env python3
"""Strict check that each :::note bullet is grounded in the page body.

For every example page, extract the `:::note` block and compare each
bullet's keywords against tokens drawn from the rest of the page. A
bullet that has no overlap with any cell, prose paragraph, or program
fragment fails the build.

The intent is to catch notes that assert something the page never
demonstrates without forcing every bullet to mirror cell wording. Fix a
failure by adding a cell that grounds the claim, citing the term in
prose, or softening the note.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "src" / "example_sources"


NOTE_RE = re.compile(r":::note\n(.*?)\n:::", re.DOTALL)
WORD_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]{2,}")
STOPWORDS = {
    "the", "and", "but", "with", "from", "that", "this", "these", "those",
    "into", "onto", "over", "than", "then", "they", "them", "their",
    "when", "where", "what", "which", "while", "would", "could", "should",
    "have", "has", "had", "for", "use", "uses", "using", "used",
    "are", "was", "were", "been", "being", "not", "any", "all",
    "one", "two", "more", "most", "less", "least", "some",
    "yes", "instead", "without", "between", "among", "every",
    "page", "example", "cell", "code", "value", "values",
    "python", "object", "objects", "function", "functions",
    "method", "methods", "type", "types",
}


def tokens(text: str) -> set[str]:
    return {match.group(0).lower() for match in WORD_RE.finditer(text)} - STOPWORDS


def main() -> int:
    errors: list[str] = []
    for path in sorted(EXAMPLES_DIR.glob("*.md")):
        text = path.read_text()
        notes_match = NOTE_RE.search(text)
        if not notes_match:
            continue
        body_outside_notes = text[: notes_match.start()] + text[notes_match.end():]
        body_tokens = tokens(body_outside_notes)
        for raw_line in notes_match.group(1).splitlines():
            line = raw_line.strip()
            if not line.startswith("- "):
                continue
            bullet = line[2:]
            bullet_tokens = tokens(bullet)
            if not bullet_tokens:
                continue
            if not bullet_tokens & body_tokens:
                errors.append(
                    f"{path}: note bullet has no keyword overlap with the rest of the page: {bullet!r}"
                )
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Notes-supported check OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
