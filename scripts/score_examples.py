#!/usr/bin/env python3
"""Score Python By Example and sampled Go/Rust By Example pages against the rubric."""
from __future__ import annotations

import ast
import contextlib
import html
import io
import re
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.examples import EXAMPLES  # noqa: E402

APP_SOURCE = (ROOT / "src" / "app.py").read_text()
STYLE_SOURCE = (ROOT / "public" / "site.css").read_text()
PROJECT_SURFACE = APP_SOURCE + "\n" + STYLE_SOURCE

GOBYEXAMPLE_SAMPLE = ["hello-world", "values", "variables", "for", "if-else", "slices", "maps", "functions", "methods", "interfaces", "regular-expressions"]
RUST_BY_EXAMPLE_SAMPLE = ["hello.html", "primitives.html", "variable_bindings.html", "flow_control.html", "fn.html", "mod.html"]


@dataclass
class Score:
    name: str
    total: float
    payoff: float
    deterministic: float
    idiom: float
    literate: float
    output: float
    navigation: float
    layout: float


def _runs(code: str) -> bool:
    try:
        ast.parse(code)
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(code, "<example>", "exec"), {"__name__": "__main__"})
        return True
    except Exception:
        return False


def _fetch_text(url: str) -> str:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        raw = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
    except Exception:
        return ""
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return html.unescape(re.sub(r"\s+", " ", text))


def score_python_example(example: dict) -> Score:
    code = example["code"]
    explanation = "\n".join(example.get("explanation", []))
    notes = "\n".join(example.get("notes", []))
    walkthrough = example.get("walkthrough", [])
    words = re.findall(r"[a-z]+", (example["summary"] + " " + explanation + " " + notes).lower())
    concept_words = {"why", "when", "use", "because", "idiomatic", "mutable", "iterable", "protocol", "explicit", "lazy", "mapping", "cleanup", "recover"}
    executable_lines = [line for line in code.splitlines() if line.strip() and not line.strip().startswith("#")]

    payoff = 1.2 + min(0.8, 0.12 * len(set(words) & concept_words) + 0.1 * min(4, len(walkthrough)))
    deterministic = 1.25 if _runs(code) and not re.search(r"random|datetime\.now|time\.time|requests|urllib", code) else 0.7
    idiom = 1.75
    if re.search(r"range\(len\(|except Exception|from .* import \*", code):
        idiom -= 0.4
    if len(executable_lines) > 35:
        idiom -= 0.2

    matched_steps = sum(1 for step in walkthrough if step.get("prose") and step.get("code") and step["code"].strip() in code)
    literate = 0.8 + min(0.9, 0.9 * matched_steps / max(1, len(walkthrough)))
    if any(phrase in explanation.lower() for phrase in ["use the linked python", "full language rules", "sample code is deliberately"]):
        literate -= 0.5
    if re.search(rf"^# {re.escape(example['title'])}\s*$", code, re.M):
        literate -= 0.3
    literate = max(0, min(2, literate))

    output = 1.0 if example.get("expected_output") is not None and "white-space: pre-wrap" in PROJECT_SURFACE and "overflow-wrap: anywhere" in PROJECT_SURFACE else 0.4
    navigation = 1.0 if "rel=\"prev\"" in PROJECT_SURFACE and "rel=\"next\"" in PROJECT_SURFACE and "docs.python.org/3.13/" in example.get("doc_url", "") else 0.5
    layout = 1.0
    if "class=\"pill\"" in PROJECT_SURFACE or "corner" in PROJECT_SURFACE or "border-radius: 999px; color: inherit" in PROJECT_SURFACE:
        layout -= 0.4
    if "nav a { color: inherit; text-decoration: underline" not in PROJECT_SURFACE:
        layout -= 0.2
    total = round(max(0, payoff + deterministic + idiom + literate + output + navigation + layout), 2)
    return Score(example["slug"], total, payoff, deterministic, idiom, literate, output, navigation, max(0, layout))


def score_external_literate_page(name: str, url: str, language_markers: tuple[str, ...], reference_label: str) -> Score:
    text = _fetch_text(url)
    if not text:
        return Score(name, 0, 0, 0, 0, 0, 0, 0, 0)
    words = text.split()
    payoff = 1.8 if len(words) > 220 else 1.5
    deterministic = 1.1 if any(marker in text for marker in ["Run", "Playground", "$ go run", "go run"]) else 0.8
    idiom = 1.75 if any(marker in text for marker in language_markers) else 1.3
    cues = len(re.findall(r"\bHere('|’)s|\bThis |\bNow |\bFor |\bNext |\bTo |\bLet's|\bThe ", text))
    literate = 2.0 if cues >= 6 else 1.6 if cues >= 3 else 1.2
    output = 0.8 if any(marker in text for marker in ["Output", "$ ", "Run"]) else 0.4
    navigation = 0.8 if any(marker in text for marker in ["Next", "Previous", "Rust By Example", "Go by Example"]) else 0.4
    layout = 1.0
    total = round(payoff + deterministic + idiom + literate + output + navigation + layout, 2)
    return Score(name, total, payoff, deterministic, idiom, literate, output, navigation, layout)


def score_gobyexample_page(slug: str) -> Score:
    return score_external_literate_page(slug, f"https://gobyexample.com/{slug}", ("package main", "func", "fmt"), "Go by Example")


def score_rust_by_example_page(slug: str) -> Score:
    return score_external_literate_page(slug.removesuffix(".html"), f"https://doc.rust-lang.org/rust-by-example/{slug}", ("fn main", "let ", "println!", "use "), "Rust By Example")


def print_table(title: str, scores: list[Score]) -> None:
    print(f"\n{title}")
    print("name,total,payoff,deterministic,idiom,literate,output,navigation,layout")
    for s in scores:
        print(f"{s.name},{s.total:.2f},{s.payoff:.1f},{s.deterministic:.1f},{s.idiom:.1f},{s.literate:.1f},{s.output:.1f},{s.navigation:.1f},{s.layout:.1f}")
    print(f"average,{mean(s.total for s in scores):.2f}")


def main() -> int:
    py_scores = [score_python_example(example) for example in EXAMPLES]
    go_scores = [score_gobyexample_page(slug) for slug in GOBYEXAMPLE_SAMPLE]
    rust_scores = [score_rust_by_example_page(slug) for slug in RUST_BY_EXAMPLE_SAMPLE]
    print_table("Python By Example", py_scores)
    print_table("Go By Example sample", go_scores)
    print_table("Rust By Example sample", rust_scores)
    failing = [s for s in py_scores if s.total < 8.5]
    if failing:
        print("\nBelow gate:", ", ".join(f"{s.name}={s.total:.2f}" for s in failing))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
