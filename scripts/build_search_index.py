#!/usr/bin/env python3
"""Build the client-side search index from the example catalog.

The index is a small JSON array served as a fingerprinted static asset.
Each entry carries:

- `keywords`: words a learner might type that the title does not contain
  ("dictionary" for Dicts, "mutable" for Mutability), ranked just below a
  title match;
- `text`: every distinct word of the page's prose, notes and code, so a
  search can hit a name the page uses (`zip`, `join`, `docstring`) even
  when no heading mentions it.

Both are lowercased at build time so the client never normalizes entry
content.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.app import list_examples

TARGET = ROOT / "public" / "search-index.json"

# Everyday names for a page's subject. Add a line when a query that should
# find a page does not; scripts/check_search_ranking.mjs pins the important
# ones.
KEYWORDS = {
    "dicts": "dictionary dictionaries mapping map hash key value lookup",
    "lists": "array arrays sequence append",
    "tuples": "immutable sequence record",
    "sets": "unique membership union intersection",
    "strings": "str text unicode join split",
    "string-formatting": "f-string fstring format interpolation",
    "mutability": "mutable immutable in-place alias aliasing",
    "equality-and-identity": "is == equal same object",
    "assignment-expressions": "walrus :=",
    "for-loops": "loop iterate iteration range enumerate zip",
    "while-loops": "loop repeat",
    "conditionals": "if elif else branch",
    "functions": "def return parameter argument docstring",
    "lambdas": "anonymous function",
    "comprehensions": "list comprehension dict comprehension",
    "iterating-over-iterables": "enumerate zip reversed",
    "itertools": "chain islice product permutations combinations",
    "collections-module": "counter defaultdict deque namedtuple",
    "exceptions": "try except finally raise error",
    "context-managers": "with statement",
    "modules": "import random math standard library",
    "classes": "object oriented oop instance self init method",
    "inheritance-and-super": "subclass parent base class",
    "special-methods": "dunder magic methods",
    "none": "null nil missing",
    "numbers": "int float integer decimal arithmetic math",
    "booleans": "true false bool",
    "slices": "slicing index range substring",
    "sorting": "sort sorted key reverse order",
    "regular-expressions": "regex re pattern match",
    "json": "serialize deserialize parse dump load",
    "datetime": "date time timezone timedelta",
    "csv-data": "csv spreadsheet rows",
    "testing": "unittest test assert pytest",
    "type-hints": "typing annotations annotation",
    "generators": "yield lazy",
    "decorators": "wrapper wraps",
    "async-await": "asyncio coroutine concurrency",
    "match-statements": "switch case pattern matching",
    "unpacking": "destructuring star splat",
    "args-and-kwargs": "variadic star arguments",
    "dataclasses": "record struct",
    "enums": "enumeration constants",
    "logging": "log logger debug",
    "virtual-environments": "venv pip install packages",
}

_WORD_RE = re.compile(r"[a-z_][a-z0-9_]{1,}")


def _word_bag(example: dict) -> str:
    """Distinct lowercase words from everything a reader sees on the page."""
    parts = [example["slug"].replace("-", " ")]
    parts.extend(example.get("notes", []))
    parts.extend(example.get("explanation", []))
    for cell in example.get("cells", []):
        parts.extend(cell["prose"])
        parts.append(cell["code"])
    parts.append(example["code"])
    seen: dict[str, None] = {}
    for word in _WORD_RE.findall(" ".join(parts).lower()):
        seen.setdefault(word)
    return " ".join(seen)


def build_entries() -> list[dict[str, str]]:
    known = {example["slug"] for example in list_examples()}
    unknown = sorted(set(KEYWORDS) - known)
    if unknown:
        raise SystemExit(f"KEYWORDS names slugs that are not in the catalog: {unknown}")
    entries = []
    for example in list_examples():
        entries.append(
            {
                "slug": example["slug"],
                "title": example["title"],
                "section": example["section"],
                "summary": example["summary"],
                "keywords": KEYWORDS.get(example["slug"], ""),
                "text": _word_bag(example),
            }
        )
    return entries


def main() -> None:
    entries = build_entries()
    TARGET.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"Search index written with {len(entries)} example entries.")


if __name__ == "__main__":
    main()
