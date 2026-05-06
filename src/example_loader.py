"""Load Python By Example source files from Markdown."""
from __future__ import annotations

import ast
import contextlib
import io
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = Path(__file__).with_name("example_sources")

try:
    from .example_sources_data import EXAMPLE_SOURCE_FILES
except ImportError:  # pragma: no cover - Worker imports src as root.
    try:
        from example_sources_data import EXAMPLE_SOURCE_FILES
    except ImportError:  # pragma: no cover - only before first build.
        EXAMPLE_SOURCE_FILES = {}


@dataclass(frozen=True)
class SourceLocation:
    path: str
    line: int


@dataclass(frozen=True)
class Cell:
    prose: list[str]
    source: str
    output: str
    line: int


@dataclass(frozen=True)
class ExampleCatalog:
    python_version: str
    docs_base_url: str
    order: list[str]


def _source_text(filename: str) -> str:
    path = EXAMPLES_DIR / filename
    if path.exists():
        return path.read_text()
    return EXAMPLE_SOURCE_FILES[filename]


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def load_manifest() -> ExampleCatalog:
    data = tomllib.loads(_source_text("manifest.toml"))
    return ExampleCatalog(str(data["python_version"]), str(data["docs_base_url"]).rstrip("/"), list(data["order"]))


def _split_frontmatter(text: str, filename: str) -> tuple[dict[str, Any], str, int]:
    if not text.startswith("+++\n"):
        raise ValueError(f"{filename}:1: expected TOML frontmatter delimited by +++")
    marker = "\n+++\n"
    end = text.find(marker, 4)
    if end < 0:
        raise ValueError(f"{filename}:1: missing closing +++ frontmatter delimiter")
    frontmatter = tomllib.loads(text[4:end])
    body_start = end + len(marker)
    return frontmatter, text[body_start:], _line_for_offset(text, body_start)


def _paragraphs(markdown_text: str) -> list[str]:
    paragraphs: list[str] = []
    for paragraph in re.split(r"\n\s*\n", markdown_text.strip()):
        cleaned = " ".join(line.strip() for line in paragraph.splitlines()).strip()
        if cleaned:
            paragraphs.append(cleaned)
    return paragraphs


def _single_fence(cell_text: str, language: str, filename: str, line: int) -> str:
    matches = re.findall(rf"```{re.escape(language)}\n(.*?)\n```", cell_text, flags=re.S)
    if len(matches) != 1:
        raise ValueError(f"{filename}:{line}: expected exactly one {language} fence in cell")
    return matches[0].rstrip("\n")


def _parse_cells_and_notes(body: str, filename: str, body_line: int) -> tuple[list[str], list[Cell], list[str]]:
    notes: list[str] = []
    note_pattern = re.compile(r":::note\n(.*?)\n:::", re.S)

    def note_repl(match: re.Match[str]) -> str:
        for line in match.group(1).splitlines():
            stripped = line.strip()
            if stripped.startswith("- "):
                notes.append(stripped[2:].strip())
            elif stripped:
                notes.append(stripped)
        return "\n"

    body_no_notes = note_pattern.sub(note_repl, body)
    cell_pattern = re.compile(r":::cell\n(.*?)\n:::", re.S)
    matches = list(cell_pattern.finditer(body_no_notes))
    if not matches:
        raise ValueError(f"{filename}:{body_line}: expected at least one :::cell block")
    intro = _paragraphs(body_no_notes[: matches[0].start()])
    cells: list[Cell] = []
    for match in matches:
        line = body_line + _line_for_offset(body_no_notes, match.start()) - 1
        text = match.group(1).strip()
        source = _single_fence(text, "python", filename, line)
        output = _single_fence(text, "output", filename, line)
        prose_text = re.sub(r"```python\n.*?\n```", "", text, flags=re.S)
        prose_text = re.sub(r"```output\n.*?\n```", "", prose_text, flags=re.S)
        prose = _paragraphs(prose_text)
        if not prose:
            raise ValueError(f"{filename}:{line}: cell prose is required")
        cells.append(Cell(prose, source, output.rstrip("\n"), line))
    return intro, cells, notes


def _run(code: str, namespace: dict[str, Any] | None = None) -> str:
    stdout = io.StringIO()
    if namespace is None:
        namespace = {"__name__": "__main__"}
    with contextlib.redirect_stdout(stdout):
        exec(compile(code, "<example>", "exec", dont_inherit=True), namespace)
    return stdout.getvalue()


def example_to_dict(filename: str, catalog: ExampleCatalog) -> dict[str, Any]:
    raw = _source_text(filename)
    frontmatter, body, body_line = _split_frontmatter(raw, filename)
    intro, cells, notes = _parse_cells_and_notes(body, filename, body_line)
    slug = str(frontmatter["slug"])
    doc_path = str(frontmatter["doc_path"])
    code = "\n\n".join(cell.source for cell in cells).rstrip() + "\n"
    expected_output = "\n".join(cell.output for cell in cells).rstrip() + "\n"
    return {
        "slug": slug,
        "title": str(frontmatter["title"]),
        "section": str(frontmatter["section"]),
        "summary": str(frontmatter["summary"]),
        "doc_path": doc_path,
        "doc_url": f"{catalog.docs_base_url}{doc_path}",
        "explanation": intro,
        "notes": notes,
        "walkthrough": [{"prose": prose, "code": cell.source} for cell in cells for prose in cell.prose],
        "cells": [{"prose": cell.prose, "code": cell.source, "output": cell.output, "line": cell.line} for cell in cells],
        "code": code,
        "expected_output": expected_output,
        "min_python": frontmatter.get("min_python"),
        "version_sensitive": bool(frontmatter.get("version_sensitive", False)),
        "version_notes": frontmatter.get("version_notes"),
    }


def load_examples() -> tuple[ExampleCatalog, list[dict[str, Any]]]:
    catalog = load_manifest()
    return catalog, [example_to_dict(f"{slug}.md", catalog) for slug in catalog.order]


def verify_example_output(example: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    namespace: dict[str, Any] = {"__name__": "__main__"}
    for index, cell in enumerate(example["cells"], 1):
        line = cell.get("line", 1)
        try:
            ast.parse(cell["code"])
            actual = _run(cell["code"], namespace).rstrip("\n")
        except Exception as error:  # noqa: BLE001 - verifier reports context.
            errors.append(f"{example['slug']}.md:{line}: cell {index} execution failed: {error.__class__.__name__}: {error}")
            continue
        if actual != cell["output"]:
            errors.append(f"{example['slug']}.md:{line}: cell {index} output mismatch: expected {cell['output']!r}, got {actual!r}")
    try:
        ast.parse(example["code"])
        full = _run(example["code"]).rstrip("\n") + "\n"
    except Exception as error:  # noqa: BLE001
        errors.append(f"{example['slug']}.md:1: full code execution failed: {error.__class__.__name__}: {error}")
    else:
        if full != example["expected_output"]:
            errors.append(f"{example['slug']}.md:1: full code output mismatch")
    return errors
