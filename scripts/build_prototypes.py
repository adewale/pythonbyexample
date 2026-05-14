#!/usr/bin/env python3
"""Generate exploratory prototypes under public/prototyping/.

The canonical layout is "figure between prose and code", with the cell
dropping to single-column when a figure is attached. These prototypes
demonstrate that layout on representative examples and journeys, plus
keep the marginalia-gestalt and operators-comparison review pages.
"""

from __future__ import annotations

import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from app import (  # noqa: E402  (sys.path set above)
    JOURNEYS_BY_SLUG,
    _walkthrough_cells,
    get_example,
    render_inline,
)
from marginalia import SECTION_FIGURES as JOURNEY_SECTION_FIGURES  # noqa: E402
from marginalia import _render_svg  # noqa: E402

OUT_DIR = ROOT / "public" / "prototyping"


# ─── Page scaffolding ──────────────────────────────────────────────────


def page(title: str, banner: str, style_extras: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(title)} · Prototype</title>
<link rel="stylesheet" href="/site.css">
<style>
  .prototype-banner {{
    margin: 0 0 var(--space-4);
    padding: var(--space-2) var(--space-3);
    background: var(--accent-soft);
    border: 1px dashed var(--hairline);
    border-radius: .5rem;
    color: var(--muted);
    font-size: .85rem;
  }}
  .prototype-banner strong {{ color: var(--text); font-weight: 600; }}
  .prototype-banner a {{ color: inherit; }}
{style_extras}
</style>
</head>
<body>
<div class="prototype-banner"><strong>Prototype</strong> · {banner} · <a href="/prototyping/">all prototypes</a></div>
{body}
</body>
</html>
"""


def render_cell(step: dict) -> str:
    """Render one literate cell — always prose | code in a 2-column grid.

    Figures live in banner rows between cells, never inside them.
    """
    prose_html = "".join(f"<p>{render_inline(p)}</p>" for p in step["prose"])
    code = html.escape(step["code"])
    output = html.escape(step["output"])
    code_stack = (
        '<div class="cell-code-stack">'
        f'<div class="cell-source"><p class="cell-label">Source</p><pre><code class="language-python">{code}</code></pre></div>'
        f'<div class="cell-output"><p class="cell-label">Output</p><pre><code>{output}</code></pre></div>'
        "</div>"
    )
    return f'<section class="lesson-step lp-cell"><div class="lp-prose">{prose_html}</div>{code_stack}</section>'


def render_article(example: dict, *, banners: dict[str, str] | None = None) -> str:
    """Render a full example article with optional banner rows between cells.

    banners keys: "before" | "after-cell-N" | "after-walkthrough".
    Each value is the HTML of one banner (use the banner() helper).
    """
    cells = _walkthrough_cells(example)
    banners = banners or {}
    parts: list[str] = []
    if "before" in banners:
        parts.append(banners["before"])
    for i, step in enumerate(cells):
        parts.append(render_cell(step))
        key = f"after-cell-{i}"
        if key in banners:
            parts.append(banners[key])
    if "after-walkthrough" in banners:
        parts.append(banners["after-walkthrough"])
    walkthrough = "".join(parts)
    notes = "".join(f"<li>{render_inline(n)}</li>" for n in example.get("notes", []))
    code = html.escape(example["code"])
    output = html.escape(example.get("expected_output", ""))
    return f"""
<article class="example-shell">
  <div class="example-top"><a class="text-link" href="/">↑ All examples</a><a class="text-link" href="{html.escape(example['doc_url'])}">Python docs reference</a></div>
  <section class="example-intro">
    <p class="eyebrow">{html.escape(example['section'])}</p>
    <h1>{html.escape(example['title'])}</h1>
    <p class="meta">{html.escape(example['summary'])}</p>
  </section>
  <section class="literate-program" aria-label="Annotated code walkthrough">{walkthrough}</section>
  <p class="eyebrow">Notes</p>
  <ul class="notes-list">{notes}</ul>
  <section class="playground" aria-label="Editable runnable example">
    <h2>Run the complete example</h2>
    <div class="runner-grid">
      <div class="runner-panel runner-editor">
        <h3>Example code</h3>
        <pre><code class="language-python">{code}</code></pre>
      </div>
      <section class="runner-panel output-panel"><h3>Expected output</h3><pre><code>{output}</code></pre></section>
    </div>
  </section>
</article>
"""


def banner(*items: tuple[str, str | None]) -> str:
    """A banner row holding 1+ figures spanning the full cell width.

    items: tuples of (figure_name, caption_or_None). The banner uses an
    auto-fit grid so a single figure centers, two pair as small multiples,
    three or more wrap as the cell allows.
    """
    figures_html = "".join(
        f'<figure>{_render_svg(name)}'
        f'{("<figcaption>" + html.escape(cap) + "</figcaption>") if cap else ""}'
        "</figure>"
        for name, cap in items
    )
    count_class = f" cell-banner--{len(items)}"
    return f'<div class="cell-banner{count_class}">{figures_html}</div>'


# ─── Index ─────────────────────────────────────────────────────────────


PROTOTYPES = [
    ("marginalia-gestalt.html", "Marginalia gestalt",
     "Every journey and example as a card, drawn from the shared grammar. Pure design review."),
    ("journey-figures-gestalt.html", "Journey-figures gestalt",
     "All journey section figures on one page, grouped by journey, for uniform rubric review."),
    ("production-figures-gestalt.html", "Production figures gestalt",
     "Every figure currently registered in src/marginalia.py FIGURES, with a tag showing where it renders (example attachment, journey section, or unattached)."),
    ("layout-banner-single.html", "Layout · banner between cells",
     "The grammar: cells stay 2-column always; figures live in banner rows BETWEEN cells. Holds one figure here. The intended union of Tufte/Knuth/algebrica."),
    ("layout-banner-pair.html", "Layout · banner with small-multiples pair",
     "Same grammar with two figures in the banner — a Tufte small-multiple. The mutable list and the immutable tuple side by side, captioned, between the same pair of cells."),
    ("layout-banner-trio.html", "Layout · multiple banners across the walkthrough",
     "The grammar at scale: a single-figure banner before the walkthrough, a pair-banner between two cells, a single-figure summary after the last cell. Multiple diagrams; cells never displaced."),
]


def build_index() -> None:
    items = "".join(
        f'<li><a class="text-link" href="/prototyping/{html.escape(slug)}"><strong>{html.escape(title)}</strong></a><p class="meta">{html.escape(desc)}</p></li>'
        for (slug, title, desc) in PROTOTYPES
    )
    body = f"""
<article class="example-shell">
  <section class="example-intro">
    <p class="eyebrow">Prototypes · cache: no-cache, must-revalidate</p>
    <h1>Visual explainer prototypes</h1>
    <p class="meta">Real example pages with their attached figures, plus the design-review pages. The example pages all use the production layout: a cell with an attached figure stacks prose, figure, and code vertically; cells without figures keep today's prose|code grid.</p>
  </section>
  <ul class="prototype-list">{items}</ul>
</article>
"""
    style = """
  .prototype-list { list-style: none; padding: 0; margin: var(--space-4) 0 0; }
  .prototype-list li { padding: var(--space-3) 0; border-bottom: 1px dashed var(--hairline-soft); }
  .prototype-list li:first-child { border-top: 1px dashed var(--hairline-soft); }
  .prototype-list strong { font-weight: 600; font-size: 1.05rem; }
  .prototype-list .meta { margin: .25rem 0 0; max-width: 60ch; }
"""
    (OUT_DIR / "index.html").write_text(
        page("Visual explainer prototypes", "All prototypes", style, body)
    )


# ─── Banner CSS (lives between cells, never inside) ───────────────────


BANNER_CSS = """
  /* Banner rows live BETWEEN cells, never inside them. The cell keeps
     its prose|code 2-column grid intact; the banner spans the full
     content width and holds 1+ figures via an auto-fit grid. Generous
     vertical rhythm marks each banner as a teaching pause between
     cells (Tufte's small-multiples, Knuth's interleaved literate
     prose, algebrica's quiet figure+caption pairing). */
  .cell-banner {
    margin: var(--space-5) 0;
    padding: var(--space-4) 0;
    border-block: 1px dashed var(--hairline-soft);
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: var(--space-4);
    justify-items: center;
  }
  .cell-banner figure { margin: 0; padding: 0; max-width: 360px; }
  .cell-banner svg { max-width: 100%; height: auto; display: block; }
  .cell-banner figcaption {
    margin-top: var(--space-2);
    color: var(--muted);
    font-size: .92rem;
    font-style: italic;
    max-width: 44ch;
  }
  /* Single figure: centered, generous breathing room. */
  .cell-banner--1 figure { max-width: 440px; }
"""



# ─── Journey-figures gestalt (all journey section figures on one page) ─


JOURNEY_FIGURES_GESTALT_STYLE = """
  .journey-block { margin-block: var(--space-6); padding-top: var(--space-4); border-top: 1px solid var(--hairline); }
  .journey-block:first-of-type { border-top: 0; padding-top: 0; }
  .journey-block h2 { margin: 0 0 var(--space-2); }
  .journey-block .meta { max-width: 64ch; color: var(--muted); margin: 0 0 var(--space-4); }
  .section-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--space-4) var(--space-4);
  }
  .section-grid figure { margin: 0; padding: 0; }
  .section-grid h3 {
    font-size: 1rem; font-weight: 600; letter-spacing: -0.005em;
    margin: 0 0 var(--space-2); color: var(--text);
  }
  .section-grid svg { max-width: min(100%, 320px); height: auto; display: block; }
  .section-grid figcaption {
    margin-top: var(--space-2); color: var(--muted);
    font-size: .9rem; font-style: italic; max-width: 44ch;
  }
  .section-grid figure .score-line {
    margin: var(--space-1) 0 0; color: var(--muted);
    font-size: .82rem; font-family: -apple-system, 'Source Sans Pro', sans-serif;
  }
"""


def build_journey_figures_gestalt() -> None:
    """One page showing every journey section's figure, grouped by journey.

    Reviewers can see all section figures at once to spot drift and
    apply the rubric uniformly (see docs/journey-visualisation-rubric.md).
    """
    blocks: list[str] = []
    total_figures = 0
    for slug in (
        "runtime",
        "control-flow",
        "iteration",
        "shapes",
        "interfaces",
        "types",
        "reliability",
    ):
        journey = JOURNEYS_BY_SLUG[slug]
        cards: list[str] = []
        for section in journey["sections"]:
            entry = JOURNEY_SECTION_FIGURES.get(section["title"])
            if entry is None:
                continue
            fig_name, caption = entry
            cards.append(
                f"<figure>"
                f'<h3>{html.escape(section["title"])}</h3>'
                f"{_render_svg(fig_name)}"
                f"<figcaption>{html.escape(caption)}</figcaption>"
                f"</figure>"
            )
            total_figures += 1
        blocks.append(
            f'<section class="journey-block">'
            f'<h2>{html.escape(journey["title"])}</h2>'
            f'<p class="meta">{html.escape(journey["summary"])}</p>'
            f'<div class="section-grid">{"".join(cards)}</div>'
            f"</section>"
        )
    body = f"""
<article class="example-shell">
  <section class="example-intro">
    <p class="eyebrow">Journeys · {total_figures} section figures</p>
    <h1>Journey-figures gestalt</h1>
    <p class="meta">Every journey section's figure on one page so the set can be reasoned about as a whole. Score against <a class="text-link" href="https://github.com/adewale/pythonbyexample/blob/main/docs/journey-visualisation-rubric.md">the rubric</a>; redesign anything below the 8.5 gate before shipping to /journeys/&lt;slug&gt;.</p>
  </section>
  {''.join(blocks)}
</article>
"""
    (OUT_DIR / "journey-figures-gestalt.html").write_text(
        page(
            "Journey-figures gestalt",
            f"All {total_figures} journey section figures grouped by journey, for uniform rubric review.",
            JOURNEY_FIGURES_GESTALT_STYLE,
            body,
        )
    )


def build_production_figures_gestalt() -> None:
    """One page showing exactly what is registered in src/marginalia.py FIGURES.

    Distinct from marginalia-gestalt (which renders the design-only catalogue
    in scripts/build_marginalia.py) and journey-figures-gestalt (which only
    renders figures attached to journey sections). This page makes the
    ship-vs-design gap visible: any figure shown here is wired through to
    production attachments OR available for attachment.
    """
    from marginalia import ATTACHMENTS, FIGURES, SCORES  # noqa: PLC0415

    # Build a slug→figure_names index of attached figures so we can mark
    # figures that already render somewhere on a real page.
    attached_to_slug: dict[str, list[str]] = {}
    for slug, attachments in ATTACHMENTS.items():
        for _, fig_name, _ in attachments:
            attached_to_slug.setdefault(fig_name, []).append(slug)
    journey_section_figs = {n for n, _ in JOURNEY_SECTION_FIGURES.values()}

    def score_summary(slugs: list[str]) -> str:
        scores = [SCORES.get(s) for s in slugs]
        present = [(s, sc) for s, sc in zip(slugs, scores) if sc is not None]
        if not present:
            return ""
        pieces = [f"{s} {score:.1f}" for s, (score, _note) in present]
        return " · ".join(pieces)

    cards: list[str] = []
    for name, (_, w, h) in FIGURES.items():
        kind: list[str] = []
        if name in attached_to_slug:
            slugs = ", ".join(attached_to_slug[name])
            kind.append(f"attached to /examples/{slugs}")
        if name in journey_section_figs:
            kind.append("attached to a journey section")
        if not kind:
            kind.append("registered, not yet attached")
        kind_html = " · ".join(html.escape(k) for k in kind)
        score_html = ""
        if name in attached_to_slug:
            summary = score_summary(attached_to_slug[name])
            if summary:
                score_html = f'<p class="score-line">v2 scores: {html.escape(summary)}</p>'
        cards.append(
            f"<figure>"
            f'<h3>{html.escape(name)}</h3>'
            f"{_render_svg(name)}"
            f'<figcaption>{kind_html} · viewBox {w}×{h}</figcaption>'
            f"{score_html}"
            f"</figure>"
        )
    body = f"""
<article class="example-shell">
  <section class="example-intro">
    <p class="eyebrow">Production figure registry · {len(FIGURES)} figures</p>
    <h1>Production figures gestalt</h1>
    <p class="meta">Every figure currently registered in <code>src/marginalia.py</code> <code>FIGURES</code>. Each card names the figure, where it renders today (an example attachment, a journey section, or "not yet attached"), and the intrinsic viewBox dimensions. Use this page beside the example-figure rubric to triage which figures are shipping, which are journey-only, and which are sitting in the registry waiting for an example attachment.</p>
  </section>
  <div class="section-grid">{"".join(cards)}</div>
</article>
"""
    (OUT_DIR / "production-figures-gestalt.html").write_text(
        page(
            "Production figures gestalt",
            f"All {len(FIGURES)} figures currently registered in src/marginalia.py FIGURES; each card names where it renders.",
            JOURNEY_FIGURES_GESTALT_STYLE,
            body,
        )
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_index()
    # ─── Banner-between grammar ─────────────────────────────────────
    # Cells stay 2-column; banners between cells hold 1+ figures.
    aliasing_caption = (
        "Two names share one mutable list — appending through one name "
        "changes the object visible through both."
    )
    tuple_caption = (
        "By contrast, a tuple is frozen — its contents cannot change in "
        "place, so aliasing carries no mutation hazard."
    )
    ex_mut = get_example("mutability")

    # 1) one banner, one figure between cells 0 and 1
    body = render_article(
        ex_mut,
        banners={"after-cell-0": banner(("aliasing-mutation", aliasing_caption))},
    )
    (OUT_DIR / "layout-banner-single.html").write_text(
        page(
            "Mutability · banner between cells (single figure)",
            "Cells keep their prose|code grid; one figure sits in a banner row between cell 0 and cell 1.",
            BANNER_CSS,
            body,
        )
    )

    # 2) one banner, two figures (small multiples) between cells 0 and 1
    body = render_article(
        ex_mut,
        banners={
            "after-cell-0": banner(
                ("aliasing-mutation", aliasing_caption),
                ("tuple-no-mutation", tuple_caption),
            )
        },
    )
    (OUT_DIR / "layout-banner-pair.html").write_text(
        page(
            "Mutability · banner with paired small-multiples",
            "One banner with two figures — list mutates, tuple does not. Same grammar, just more figures in the slot.",
            BANNER_CSS,
            body,
        )
    )

    # 3) multiple banners across the walkthrough
    body = render_article(
        ex_mut,
        banners={
            "before": banner(
                ("aliasing-mutation", aliasing_caption),
            ),
            "after-cell-1": banner(
                ("aliasing-mutation", "Mutable: change visible through any alias."),
                ("tuple-no-mutation", "Immutable: aliases share a frozen value."),
            ),
            "after-walkthrough": banner(
                ("tuple-no-mutation", "When in doubt, reach for the immutable shape."),
            ),
        },
    )
    (OUT_DIR / "layout-banner-trio.html").write_text(
        page(
            "Mutability · banners across the whole walkthrough",
            "Demonstrates that the grammar accepts multiple banners at any position: lead-in figure, mid-walkthrough small-multiple pair, summary figure. Cells never reflow.",
            BANNER_CSS,
            body,
        )
    )

    build_journey_figures_gestalt()
    build_production_figures_gestalt()
    written = sorted(p.name for p in OUT_DIR.iterdir() if p.is_file() and p.suffix == ".html")
    print(f"wrote {len(written)} files to {OUT_DIR.relative_to(ROOT)}/:")
    for name in written:
        print(f"  {name}")


if __name__ == "__main__":
    main()
