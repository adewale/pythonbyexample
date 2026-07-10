"""Shared plumbing for the check scripts.

Every script needs the repo root on sys.path, the canonical example
catalog, and often the quality registry or a page's frontmatter. Keeping
those in one module stops the three frontmatter parsers and a dozen
copies of the sys.path dance from drifting apart.
"""
from __future__ import annotations

import sys
import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "src" / "example_sources"
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def load_catalog():
    """Return (catalog, examples) through the canonical website loader."""
    from src.example_loader import load_examples

    return load_examples()


def load_registry() -> dict[str, Any]:
    return tomllib.loads(REGISTRY_PATH.read_text())


def frontmatter(path: Path) -> dict[str, Any]:
    """Parse a page's TOML frontmatter with the canonical loader's splitter."""
    from src.example_loader import _split_frontmatter

    data, _, _ = _split_frontmatter(path.read_text(), path.name)
    return data


def fail(errors: list[str], ok_message: str) -> int:
    """Standard exit protocol: errors to stderr and 1, or ok line and 0."""
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(ok_message)
    return 0
