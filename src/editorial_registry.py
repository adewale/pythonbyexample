"""Runtime loaders for editorial TOML registries.

The site keeps mutable editorial metadata — journey order, edge labels,
figure attachments, captions, and curated scores — in
``docs/quality-registries.toml``. Python modules keep only executable
behavior such as renderers and figure paint functions.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any
import tomllib

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"


def _registry_toml() -> str:
    if REGISTRY_PATH.exists():
        return REGISTRY_PATH.read_text()
    try:
        from .editorial_registry_data import REGISTRY_TOML
    except ImportError:  # Cloudflare Workers import sibling modules without package prefix.
        from editorial_registry_data import REGISTRY_TOML
    return REGISTRY_TOML


@lru_cache(maxsize=1)
def load_registry() -> dict[str, Any]:
    return tomllib.loads(_registry_toml())


def _required_table(name: str) -> list[dict[str, Any]]:
    rows = load_registry().get(name)
    if not isinstance(rows, list):
        raise KeyError(f"{REGISTRY_PATH}: missing [[{name}]] registry")
    return rows


def journeys() -> list[dict[str, Any]]:
    parsed: list[dict[str, Any]] = []
    for journey in _required_table("journeys"):
        sections: list[dict[str, Any]] = []
        for section in journey.get("sections", []):
            items = [
                (item["kind"], item["value"], item["description"])
                for item in section.get("items", [])
            ]
            sections.append(
                {
                    "title": section["title"],
                    "summary": section["summary"],
                    "items": items,
                }
            )
        parsed.append(
            {
                "slug": journey["slug"],
                "title": journey["title"],
                "summary": journey["summary"],
                "sections": sections,
            }
        )
    return parsed


def see_also_edge_labels() -> dict[tuple[str, str], str]:
    return {
        (row["source"], row["target"]): row["label"]
        for row in _required_table("see_also_edge_labels")
    }


def figure_attachments() -> dict[str, list[tuple[str, str, str | None]]]:
    attachments: dict[str, list[tuple[str, str, str | None]]] = {}
    for row in _required_table("figure_attachments"):
        attachments.setdefault(row["slug"], []).append(
            (row["anchor"], row["figure"], row.get("caption"))
        )
    return attachments


def journey_section_figures() -> dict[str, tuple[str, str]]:
    return {
        row["section"]: (row["figure"], row["caption"])
        for row in _required_table("journey_section_figures")
    }


def example_figure_scores() -> dict[str, tuple[float, str]]:
    return {
        row["slug"]: (float(row["score"]), row["comment"])
        for row in _required_table("example_figure_scores")
    }


def journey_section_figure_scores() -> dict[str, tuple[float, str]]:
    return {
        row["section"]: (float(row["score"]), row["comment"])
        for row in _required_table("journey_section_figure_scores")
    }


def example_quality_scores() -> dict[str, tuple[float, str]]:
    return {
        row["slug"]: (float(row["score"]), row["comment"])
        for row in _required_table("example_quality_scores")
    }
