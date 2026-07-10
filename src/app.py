from __future__ import annotations

import contextlib
import difflib
import html
import io
import json
import re
from pathlib import Path

try:
    from .asset_manifest import ASSET_PATHS
    from .editorial_registry import journeys as load_journeys, see_also_edge_labels as load_see_also_edge_labels
    from .examples import EXAMPLES, EXAMPLES_BY_SLUG, PYTHON_VERSION, REFERENCE_URL
    from .marginalia import render_banner, render_for_section
    from .textfmt import render_inline
except ImportError:  # Cloudflare Python Workers import sibling modules from main's directory.
    from asset_manifest import ASSET_PATHS
    from editorial_registry import journeys as load_journeys, see_also_edge_labels as load_see_also_edge_labels
    from examples import EXAMPLES, EXAMPLES_BY_SLUG, PYTHON_VERSION, REFERENCE_URL
    from marginalia import render_banner, render_for_section
    from textfmt import render_inline


class AppResponse:
    def __init__(self, body, status=200, headers=None):
        self.body = body
        self.status = status
        self.headers = headers


def list_examples():
    return EXAMPLES


def get_example(slug):
    return EXAMPLES_BY_SLUG.get(slug)


def _example_index(slug):
    for index, example in enumerate(EXAMPLES):
        if example["slug"] == slug:
            return index
    return -1


def _see_also_label(source_slug, target_slug):
    explicit = SEE_ALSO_EDGE_LABELS.get((source_slug, target_slug))
    if explicit:
        return explicit
    source = get_example(source_slug)
    target = get_example(target_slug)
    if source and target and source.get("section") == target.get("section"):
        return "related"
    source_index = _example_index(source_slug)
    target_index = _example_index(target_slug)
    if target_index >= 0 and source_index >= 0 and target_index < source_index:
        return "prerequisite"
    return "next depth"


def _recommended_examples(slug, limit=4):
    matches = difflib.get_close_matches(slug, [example["slug"] for example in EXAMPLES], n=limit, cutoff=0.2)
    recommendations = [get_example(match) for match in matches]
    if not recommendations:
        recommendations = EXAMPLES[:limit]
    return [example for example in recommendations if example is not None][:limit]


MAX_DYNAMIC_OUTPUT_BYTES = 64 * 1024
DYNAMIC_OUTPUT_LIMIT_MESSAGE = "Program output exceeded the 64 kB limit. Reduce output and try again."


def build_dynamic_worker_code(example_code: str) -> str:
    """Build a bounded Dynamic Worker module for a curated or edited example."""
    return f'''from workers import WorkerEntrypoint, Response
import contextlib
import io
import traceback

EXAMPLE_CODE = {example_code!r}
MAX_OUTPUT_BYTES = {MAX_DYNAMIC_OUTPUT_BYTES}
OUTPUT_LIMIT_MESSAGE = {DYNAMIC_OUTPUT_LIMIT_MESSAGE!r}


class OutputLimitExceeded(Exception):
    pass


class BoundedStdout(io.TextIOBase):
    def __init__(self):
        self.parts = []
        self.bytes_written = 0

    def writable(self):
        return True

    def write(self, value):
        # Every Unicode character is at least one UTF-8 byte. Reject an
        # obviously oversize chunk before encoding it, so a hostile exception
        # message cannot create another giant temporary byte string.
        if len(value) > MAX_OUTPUT_BYTES - self.bytes_written:
            raise OutputLimitExceeded
        encoded = value.encode("utf-8")
        if self.bytes_written + len(encoded) > MAX_OUTPUT_BYTES:
            raise OutputLimitExceeded
        self.parts.append(value)
        self.bytes_written += len(encoded)
        return len(value)

    def getvalue(self):
        return "".join(self.parts)


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        stdout = BoundedStdout()
        namespace = {{"__name__": "__main__"}}
        try:
            with contextlib.redirect_stdout(stdout):
                exec(EXAMPLE_CODE, namespace)
            return Response(stdout.getvalue(), headers={{"Content-Type": "text/plain; charset=utf-8"}})
        except OutputLimitExceeded:
            return Response(OUTPUT_LIMIT_MESSAGE, status=413, headers={{"Content-Type": "text/plain; charset=utf-8"}})
        except Exception:
            error_output = BoundedStdout()
            try:
                traceback.print_exc(file=error_output)
            except OutputLimitExceeded:
                return Response(OUTPUT_LIMIT_MESSAGE, status=413, headers={{"Content-Type": "text/plain; charset=utf-8"}})
            return Response(error_output.getvalue(), status=500, headers={{"Content-Type": "text/plain; charset=utf-8"}})
'''


_TEMPLATE_DIR = Path(__file__).with_name("templates")
_TEMPLATE_CACHE = {}
SITE_URL = "https://www.pythonbyexample.dev"

JOURNEYS = load_journeys()
JOURNEYS_BY_SLUG = {journey["slug"]: journey for journey in JOURNEYS}
SEE_ALSO_EDGE_LABELS = load_see_also_edge_labels()


FAVICON_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Python By Example">
  <rect width="64" height="64" rx="14" fill="#F5F1EB"/>
  <path d="M14 22l13 10-13 10" fill="none" stroke="#FF4801" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="31" y="40" fill="#521000" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="18" font-weight="800">py</text>
</svg>'''



def _template(name: str) -> str:
    if name not in _TEMPLATE_CACHE:
        _TEMPLATE_CACHE[name] = (_TEMPLATE_DIR / name).read_text()
    return _TEMPLATE_CACHE[name]


_PLACEHOLDER_RE = re.compile(r"__([A-Z][A-Z0-9_]*?)__")


def _replace(template: str, values: dict[str, str]) -> str:
    # Single pass over the template only: substituted values are never
    # rescanned, so user-submitted code containing a literal __TOKEN__
    # cannot pick up later substitutions, and the result cannot depend
    # on dict order. Unknown placeholders stay literal for the SEO lint
    # to catch.
    return _PLACEHOLDER_RE.sub(
        lambda match: values.get(match.group(1), match.group(0)), template
    )


def _meta_description(text: str) -> str:
    text = " ".join(text.split())
    if len(text) <= 175:
        return text
    return text[:172].rsplit(" ", 1)[0] + "…"


def _social_image_tags(image_url: str | None) -> str:
    if not image_url:
        return '<meta name="twitter:card" content="summary">'
    escaped = html.escape(image_url)
    return (
        f'<meta property="og:image" content="{escaped}">'
        '<meta property="og:image:width" content="1200">'
        '<meta property="og:image:height" content="630">'
        '<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:image" content="{escaped}">'
    )


def _structured_data_script(data: dict) -> str:
    # JSON-LD lives inside a <script> element, so escape the characters
    # that could terminate the element or open a new one mid-payload.
    payload = json.dumps(data, ensure_ascii=False)
    payload = payload.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return f'<script type="application/ld+json">{payload}</script>'


def _layout(title: str, content: str, description: str | None = None, path: str = "/", og_type: str = "website", include_editor: bool = False, include_search: bool = False, structured_data: dict | None = None, og_image: str | None = None) -> str:
    description = _meta_description(description or "Learn Python with concise, editable examples that run in isolated Cloudflare Dynamic Python Workers.")
    canonical_url = f"{SITE_URL}{path}"
    page_title = title if title == "Python By Example" else f"{title} · Python By Example"
    editor_scripts = (
        "".join(
            f'<script type="module" src="{html.escape(ASSET_PATHS[name])}"></script>'
            for name in ("EDITOR_JS", "RUNNER_JS")
        )
        if include_editor
        else ""
    )
    if include_search:
        editor_scripts += f'<script type="module" src="{html.escape(ASSET_PATHS["SEARCH_JS"])}"></script>'
    return _replace(
        _template("layout.html"),
        {
            "STRUCTURED_DATA": _structured_data_script(structured_data) if structured_data else "",
            "SOCIAL_IMAGE_TAGS": _social_image_tags(og_image),
            "PAGE_TITLE": html.escape(page_title),
            "TITLE": html.escape(title),
            "REFERENCE_URL": html.escape(REFERENCE_URL),
            "PYTHON_VERSION": html.escape(PYTHON_VERSION),
            "META_DESCRIPTION": html.escape(description),
            "CANONICAL_URL": html.escape(canonical_url),
            "OG_TYPE": html.escape(og_type),
            "SITE_CSS": html.escape(ASSET_PATHS["SITE_CSS"]),
            "SYNTAX_JS": html.escape(ASSET_PATHS["SYNTAX_JS"]),
            "EDITOR_SCRIPTS": editor_scripts,
            "CONTENT": content,
        },
    )


def render_home() -> str:
    # Group examples by section in the order each section first appears
    # in the manifest. Each section gets its own .home-section wrapper
    # holding an eyebrow (tight, ~12px above its cards) and the
    # section's grid; sections are spaced ~48px apart for clear
    # separation. The shared outer .grid is gone — using one grid
    # per section gives explicit control over the eyebrow's vertical
    # relationship to its own cards vs the previous section.
    by_section: dict[str, list[dict]] = {}
    for example in list_examples():
        by_section.setdefault(example["section"], []).append(example)
    sections_html = []
    for section, examples in by_section.items():
        card_markup = "".join(
            _replace(
                '<a class="card" href="/examples/__SLUG__"><h2>__TITLE__</h2><p class="meta">__SUMMARY__</p></a>',
                {
                    "SLUG": html.escape(example["slug"]),
                    "TITLE": html.escape(example["title"]),
                    "SUMMARY": html.escape(example["summary"]),
                },
            )
            for example in examples
        )
        sections_html.append(
            f'<section class="home-section">'
            f'<p class="eyebrow">{html.escape(section)}</p>'
            f'<div class="grid">{card_markup}</div>'
            f'</section>'
        )
    content = _replace(
        _template("home.html"),
        {
            "PYTHON_VERSION": html.escape(PYTHON_VERSION),
            "SEARCH_INDEX": html.escape(ASSET_PATHS["SEARCH_INDEX"]),
            "CARDS": "".join(sections_html),
        },
    )
    return _layout(
        "Python By Example",
        content,
        include_search=True,
        description="Learn Python 3.13 with concise, editable examples, expected output, official documentation links, and Cloudflare Dynamic Worker execution.",
        path="/",
        og_type="website",
        og_image=f"{SITE_URL}/og/home.jpg",
        structured_data={
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "Python By Example",
            "url": f"{SITE_URL}/",
            "description": f"Concise, editable Python {PYTHON_VERSION} examples with verified output and official documentation links.",
            "inLanguage": "en",
        },
    )


def render_journeys_index():
    description = "Curated Python By Example journeys that compose individual examples into larger mental maps with per-section learner outcomes."
    cards = []
    for journey in JOURNEYS:
        section_titles = "".join(f'<li>{html.escape(section["title"])}</li>' for section in journey["sections"])
        cards.append(
            f'''
<a class="card journey-card" href="/journeys/{html.escape(journey["slug"])}">
  <p class="eyebrow">Journey</p>
  <h2>{html.escape(journey["title"])}</h2>
  <p class="meta">{html.escape(journey["summary"])}</p>
  <ul>{section_titles}</ul>
</a>'''
        )
    content = f'''
<section class="hero">
  <p class="eyebrow">Journeys</p>
  <h1>Python learning journeys</h1>
  <p>These paths compose individual examples into larger mental maps. They are inspired by the way <a class="text-link" href="https://www.oreilly.com/library/view/apprenticeship-patterns/9780596806842/">Apprenticeship Patterns</a> treats small patterns as material for longer learning journeys.</p>
</section>
<section class="grid journey-grid">{"".join(cards)}</section>
'''
    return _layout(
        "Python learning journeys",
        content,
        description=description,
        path="/journeys",
        og_image=f"{SITE_URL}/og/journeys.jpg",
        structured_data={
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Python learning journeys",
            "description": description,
            "url": f"{SITE_URL}/journeys",
            "inLanguage": "en",
            "isPartOf": {"@type": "WebSite", "name": "Python By Example", "url": f"{SITE_URL}/"},
        },
    )


def render_journey_page(journey):
    overview = "".join(f'<li>{html.escape(section["title"])}</li>' for section in journey["sections"])
    sections = []
    for section in journey["sections"]:
        rows = []
        for kind, value, description in section["items"]:
            if kind == "example":
                example = get_example(value)
                sentence = f"Use this example to {description}."
                if example is None:
                    label = html.escape(value)
                    target = f'<span class="journey-gap">Missing example: {label}</span>'
                else:
                    target = f'<a class="text-link journey-item-title" href="/examples/{html.escape(example["slug"])}">{html.escape(example["title"])}</a>'
                rows.append(f'<li>{target}<p class="meta">{html.escape(sentence)}</p></li>')
            else:
                sentence = f"This gap should {description}."
                rows.append(f'<li><p class="journey-gap-label">Gap · {html.escape(value)}</p><p class="meta">{html.escape(sentence)}</p></li>')
        figure_html = render_for_section(section["title"])
        sections.append(f'<section class="journey-section"><h2>{html.escape(section["title"])}</h2><p class="meta">{html.escape(section["summary"])}</p>{figure_html}<ul class="journey-list">{"".join(rows)}</ul></section>')
    content = f'''
<article class="example-shell journey-page">
  <div class="example-top"><a class="text-link" href="/">↑ All examples</a><a class="text-link" href="{html.escape(REFERENCE_URL)}">Python docs reference</a></div>
  <section class="example-intro">
    <p class="eyebrow">Journey</p>
    <h1>{html.escape(journey["title"])}</h1>
    <p class="meta">{html.escape(journey["summary"])}</p>
    <div class="journey-overview"><p class="cell-label">In this journey</p><ul>{overview}</ul></div>
  </section>
  {"".join(sections)}
</article>
'''
    return _layout(
        journey["title"],
        content,
        description=f'{journey["summary"]} A curated Python By Example journey with per-section learner outcomes.',
        path=f'/journeys/{journey["slug"]}',
        og_image=f'{SITE_URL}/og/journey-{journey["slug"]}.jpg',
        structured_data={
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": journey["title"],
            "description": journey["summary"],
            "url": f'{SITE_URL}/journeys/{journey["slug"]}',
            "inLanguage": "en",
            "isPartOf": {"@type": "WebSite", "name": "Python By Example", "url": f"{SITE_URL}/"},
        },
    )


def render_sitemap() -> str:
    paths = ["/", "/journeys"]
    paths.extend(f'/journeys/{journey["slug"]}' for journey in JOURNEYS)
    paths.extend(f'/examples/{example["slug"]}' for example in list_examples())
    entries = "".join(f"<url><loc>{html.escape(SITE_URL + path)}</loc></url>" for path in paths)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{entries}"
        "</urlset>\n"
    )


def render_example_not_found(slug: str) -> str:
    recommendations = "".join(
        f'<li><a class="text-link" href="/examples/{html.escape(item["slug"])}">{html.escape(item["title"])}</a></li>'
        for item in _recommended_examples(slug)
    )
    content = (
        "<h1>Example not found</h1>"
        '<p class="meta">Try one of these nearby examples.</p>'
        f"<h2>Recommended examples</h2><ul>{recommendations}</ul>"
    )
    return _layout("Not Found", content)


def render_journey_not_found() -> str:
    return _layout("Not Found", "<h1>Journey not found</h1>")


def render_not_found() -> str:
    return _layout("Not Found", "<h1>Not found</h1>")


def _example_neighbors(slug):
    slugs = [item["slug"] for item in list_examples()]
    index = slugs.index(slug)
    previous_example = get_example(slugs[index - 1]) if index > 0 else None
    next_example = get_example(slugs[index + 1]) if index + 1 < len(slugs) else None
    return previous_example, next_example


def render_mobile_run_first_option(example):
    page = render_example_page(example)
    page = page.replace(
        '<article class="example-shell">',
        '<article class="example-shell mobile-run-first">',
        1,
    )
    page = page.replace(
        '<div class="example-top">',
        '<div class="example-top"><a class="text-link" href="/examples/values">← Current layout</a>',
        1,
    )
    page = page.replace(
        '<p class="eyebrow">Basics</p>',
        '<p class="eyebrow">Layout option · mobile run-first</p>',
        1,
    )
    return page


def _walkthrough_cells(example):
    if "cells" in example:
        return example["cells"]
    stdout = io.StringIO()
    namespace = {"__name__": "__main__"}
    cells = []
    pending_steps = []
    last_output_length = 0
    steps = example.get("walkthrough", [])
    for index, step in enumerate(steps, 1):
        pending_steps.append(step)
        delta = ""
        try:
            with contextlib.redirect_stdout(stdout):
                exec(compile(step["code"], "<walkthrough>", "exec", dont_inherit=True), namespace)
            current_output = stdout.getvalue()
            delta = current_output[last_output_length:]
            last_output_length = len(current_output)
        except Exception as error:
            delta = f"Execution reaches this point in the complete example. ({error.__class__.__name__})\n"
        if delta or index == len(steps):
            cells.append(
                {
                    "name": f"fragment-{len(cells) + 1}",
                    "prose": [item["prose"] for item in pending_steps],
                    "code": "\n\n".join(item["code"] for item in pending_steps),
                    "output": delta.rstrip("\n") or "This fragment prepares state for the complete example.",
                }
            )
            pending_steps = []
    return cells


def render_cell_output_flow_option(example):
    notes = "".join(f"<li>{render_inline(note)}</li>" for note in example.get("notes", []))
    fragments = [
        {
            "name": "make-values",
            "prose": "Start by making visible values. The first fragment binds names, then prints the objects so the rest of the program has evidence to build on.",
            "code": 'text = "python"\ncount = 3\nratio = 2.5\nready = True\nmissing = None\n\nprint(text)\nprint(count)\nprint(ratio)',
            "output": ["python", "3", "2.5"],
        },
        {
            "name": "transform-values",
            "prose": "Methods and operators evaluate to new values. The original bindings remain ordinary objects you can reuse.",
            "code": 'print(text.upper())\nprint(count + 4)\nprint(ratio * 2)',
            "output": ["PYTHON", "7", "5.0"],
        },
        {
            "name": "check-booleans",
            "prose": "Boolean expressions combine facts, and `None` is checked by identity because it is a singleton absence marker.",
            "code": 'print(ready and count > 0)\nprint(missing is None)',
            "output": ["True", "True"],
        },
    ]
    woven_source = "\n\n".join(fragment["code"] for fragment in fragments)
    cells = []
    for index, fragment in enumerate(fragments, 1):
        cells.append(
            f'''
<section class="lp-cell">
  <p class="cell-label">Cell {index} · &lt;&lt;{html.escape(fragment["name"])}&gt;&gt;</p>
  <div class="lp-prose"><p>{render_inline(fragment["prose"])}</p></div>
  <div class="cell-source"><p class="cell-label">Source fragment</p><pre><code class="language-python">{html.escape(fragment["code"])}</code></pre></div>
  <div class="cell-output"><p class="cell-label">Output</p><pre><code>{html.escape(chr(10).join(fragment["output"]))}</code></pre></div>
</section>'''
        )
    content = f'''
<article class="cell-flow-prototype">
  <div class="example-top"><a class="text-link" href="/examples/{html.escape(example["slug"])}">← Current layout</a><a class="text-link" href="{html.escape(example["doc_url"])}">Python docs reference</a></div>
  <section class="notebook-hero">
    <p class="eyebrow">Layout option · literate cells</p>
    <h1>{html.escape(example["title"])}</h1>
    <p class="meta">{html.escape(example["summary"])}</p>
  </section>
  <section class="cell-run-summary">
    <h2>Run the woven program</h2>
    <p>The explanation is organized as named fragments. Each fragment has source and output; the complete program is woven from those fragments in order.</p>
    <details>
      <summary>Show complete editable source</summary>
      <form class="runner-panel runner-editor" method="post" action="/examples/{html.escape(example["slug"])}">
        <h2>Complete woven source</h2>
        <textarea name="code" id="code-editor" data-original-code="{html.escape(woven_source)}" aria-label="Editable Python example code" spellcheck="false" rows="{max(14, woven_source.count(chr(10)) + 2)}">{html.escape(woven_source)}</textarea>
        <div class="playground-toolbar"><button class="button" type="submit">Run all</button><button class="tool-button" type="button" data-reset>Reset</button></div>
      </form>
    </details>
  </section>
  <section class="lp-cells" aria-label="Literate cells with output">{"".join(cells)}</section>
  <section class="notebook-notes"><h2>Notes</h2><ul>{notes}</ul></section>
</article>
'''
    return _layout(f'{example["title"]} literate cells option', content, description=f'Prototype layout for the {example["title"]} Python example.', path='/layout-options/cell-output-flow', include_editor=True)


def _render_cell(step):
    prose_html = "".join(f"<p>{render_inline(prose)}</p>" for prose in step["prose"])
    source = html.escape(step["code"])
    if step.get("kind") == "unsupported":
        return f'<section class="lesson-step lp-cell unsupported-cell"><div class="lp-prose">{prose_html}</div><div class="cell-code-stack"><div class="cell-source"><p class="cell-label">Standard Python</p><pre><code class="language-python">{source}</code></pre></div></div></section>'
    return f'<section class="lesson-step lp-cell"><div class="lp-prose">{prose_html}</div><div class="cell-code-stack"><div class="cell-source"><p class="cell-label">Source</p><pre><code class="language-python">{source}</code></pre></div><div class="cell-output"><p class="cell-label">Output</p><pre><code>{html.escape(step["output"])}</code></pre></div></div></section>'


def _render_walkthrough(slug: str, walkthrough: list[dict]) -> str:
    """Interleave cells with their figure banners.

    Banners slot into the positions from docs/visual-explainer-spec.md:
    `before` the first cell, `after-cell-N`, and `after-walkthrough`.
    A page with no attached figures renders cells only.
    """
    parts: list[str] = []
    before = render_banner(slug, "before")
    if before:
        parts.append(before)
    for i, step in enumerate(walkthrough):
        parts.append(_render_cell(step))
        banner_html = render_banner(slug, f"after-cell-{i}")
        if banner_html:
            parts.append(banner_html)
    after = render_banner(slug, "after-walkthrough")
    if after:
        parts.append(after)
    return "".join(parts)


def _turnstile_challenge_container(site_key: str | None) -> str:
    if not site_key:
        return ""
    escaped = html.escape(site_key)
    return f'<div class="turnstile-challenge" data-turnstile-sitekey="{escaped}" hidden></div>'


def _turnstile_required_marker(required: bool) -> str:
    if not required:
        return ""
    return '<div data-turnstile-required="true" hidden>Verification required before running edited code…</div>'


def render_example_page(
    example,
    output=None,
    code=None,
    execution_time_ms=None,
    turnstile_site_key=None,
    turnstile_required=False,
):
    notes = [render_inline(note) for note in example.get("notes", [])]
    walkthrough = _walkthrough_cells(example)
    shown_output = output if output is not None else example.get("expected_output", "Run this example to see output here.")
    output_heading = "Output" if output is not None else "Expected output"
    execution_time = f"Executed in {execution_time_ms:.1f} ms" if execution_time_ms is not None else "Execution time appears here after you run the example."
    editable_code = example["code"] if code is None else code
    previous_example, next_example = _example_neighbors(example["slug"])
    previous_link = (
        f'<a class="text-link" rel="prev" href="/examples/{html.escape(previous_example["slug"])}">← {html.escape(previous_example["title"])}</a>'
        if previous_example
        else "<span></span>"
    )
    next_link = (
        f'<a class="text-link" rel="next" href="/examples/{html.escape(next_example["slug"])}">{html.escape(next_example["title"])} →</a>'
        if next_example
        else "<span></span>"
    )
    walkthrough_html = _render_walkthrough(example["slug"], walkthrough)
    notes_html = "".join(f"<li>{note}</li>" for note in notes)
    see_also_examples = [get_example(slug) for slug in example.get("see_also", [])]
    see_also_links = "".join(
        f'<li>{html.escape(_see_also_label(example["slug"], item["slug"]))}: <a class="text-link" href="/examples/{html.escape(item["slug"])}">{html.escape(item["title"])}</a></li>'
        for item in see_also_examples
        if item is not None
    )
    see_also_html = f'<h2>See also</h2><ul>{see_also_links}</ul>' if see_also_links else ""
    content = _replace(
        _template("example.html"),
        {
            "DOC_URL": html.escape(example["doc_url"]),
            "SECTION": html.escape(example["section"]),
            "TITLE": html.escape(example["title"]),
            "SUMMARY": html.escape(example["summary"]),
            "WALKTHROUGH": walkthrough_html,
            "NOTES": notes_html,
            "SEE_ALSO": see_also_html,
            "PREVIOUS_LINK": previous_link,
            "NEXT_LINK": next_link,
            "SLUG": html.escape(example["slug"]),
            "EDITOR_ROWS": str(max(18, editable_code.count("\n") + 2)),
            "EDITABLE_CODE": html.escape(editable_code),
            "TURNSTILE_CHALLENGE": _turnstile_challenge_container(turnstile_site_key) + _turnstile_required_marker(turnstile_required),
            "OUTPUT_PLACEHOLDER": " data-output-placeholder" if output is None else "",
            "OUTPUT_HEADING": html.escape(output_heading),
            "SHOWN_OUTPUT": html.escape(shown_output),
            "EXECUTION_TIME": html.escape(execution_time),
            # This value feeds the external runner's Reset action, not an
            # executable script. Attribute escaping keeps authored code inert.
            "ORIGINAL_CODE": html.escape(example["code"]),
        },
    )
    return _layout(
        example["title"],
        content,
        description=f'{example["summary"]} Includes editable Python {PYTHON_VERSION} code, expected output, and links to the official Python documentation.',
        path=f'/examples/{example["slug"]}',
        og_type="article",
        include_editor=True,
        og_image=f'{SITE_URL}/og/{example["slug"]}.jpg',
        structured_data={
            "@context": "https://schema.org",
            "@type": ["TechArticle", "LearningResource"],
            "name": example["title"],
            "headline": example["title"],
            "description": example["summary"],
            "url": f'{SITE_URL}/examples/{example["slug"]}',
            "inLanguage": "en",
            "programmingLanguage": "Python",
            "learningResourceType": "Example",
            "teaches": example["summary"],
            "articleSection": example["section"],
            "isAccessibleForFree": True,
            "isPartOf": {
                "@type": "WebSite",
                "name": "Python By Example",
                "url": f"{SITE_URL}/",
            },
        },
    )


def route(url: str, method: str = "GET", turnstile_site_key: str | None = None) -> AppResponse:
    without_scheme = url.split("://", 1)[-1]
    path_part = without_scheme.split("/", 1)[1] if "/" in without_scheme else ""
    path = ("/" + path_part.split("?", 1)[0]).rstrip("/") or "/"
    if method == "GET" and path == "/favicon.svg":
        return AppResponse(FAVICON_SVG, headers={"Content-Type": "image/svg+xml; charset=utf-8"})
    if method == "GET" and path == "/sitemap.xml":
        return AppResponse(render_sitemap(), headers={"Content-Type": "application/xml; charset=utf-8"})
    if method == "GET" and path == "/":
        return AppResponse(render_home(), headers={"Content-Type": "text/html; charset=utf-8"})
    if method == "GET" and path == "/layout-options/mobile-run-first":
        return AppResponse(
            render_mobile_run_first_option(get_example("values")),
            headers={"Content-Type": "text/html; charset=utf-8"},
        )
    if method == "GET" and path == "/layout-options/cell-output-flow":
        return AppResponse(
            render_cell_output_flow_option(get_example("values")),
            headers={"Content-Type": "text/html; charset=utf-8"},
        )
    if method == "GET" and path == "/journeys":
        return AppResponse(render_journeys_index(), headers={"Content-Type": "text/html; charset=utf-8"})
    if method == "GET" and path.startswith("/journeys/"):
        slug = path.split("/", 2)[2]
        journey = JOURNEYS_BY_SLUG.get(slug)
        if journey is None:
            return AppResponse(_layout("Not Found", "<h1>Journey not found</h1>"), status=404)
        return AppResponse(render_journey_page(journey), headers={"Content-Type": "text/html; charset=utf-8"})
    if path.startswith("/examples/"):
        slug = path.split("/", 2)[2]
        example = get_example(slug)
        if example is None:
            recommendations = "".join(
                f'<li><a class="text-link" href="/examples/{html.escape(item["slug"])}">{html.escape(item["title"])}</a></li>'
                for item in _recommended_examples(slug)
            )
            body = f'<h1>Example not found</h1><p class="meta">Try one of these nearby examples.</p><h2>Recommended examples</h2><ul>{recommendations}</ul>'
            return AppResponse(_layout("Not Found", body), status=404)
        return AppResponse(
            render_example_page(example, turnstile_site_key=turnstile_site_key),
            headers={"Content-Type": "text/html; charset=utf-8"},
        )
    return AppResponse(_layout("Not Found", "<h1>Not found</h1>"), status=404)
