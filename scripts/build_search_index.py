#!/usr/bin/env python3
"""Build the client-side search index from the example catalog.

The index is a small JSON array served as a fingerprinted static asset.
`text` concatenates the note lines so searches can hit concepts the
title does not mention (for example "walrus" for assignment
expressions); it is lowercased at build time so the client never
normalizes entry content.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.app import list_examples  # noqa: E402

TARGET = ROOT / "public" / "search-index.json"


def build_entries() -> list[dict[str, str]]:
    entries = []
    for example in list_examples():
        text_parts = [example["slug"].replace("-", " ")]
        text_parts.extend(example.get("notes", []))
        entries.append(
            {
                "slug": example["slug"],
                "title": example["title"],
                "section": example["section"],
                "summary": example["summary"],
                "text": " ".join(text_parts).lower(),
            }
        )
    return entries


def main() -> None:
    entries = build_entries()
    TARGET.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"Search index written with {len(entries)} example entries.")


if __name__ == "__main__":
    main()
