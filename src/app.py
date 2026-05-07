from __future__ import annotations

import contextlib
import html
import io
import json
from pathlib import Path

try:
    from .asset_manifest import ASSET_PATHS
    from .examples import EXAMPLES, EXAMPLES_BY_SLUG, PYTHON_VERSION, REFERENCE_URL
except ImportError:  # Cloudflare Python Workers import sibling modules from main's directory.
    from asset_manifest import ASSET_PATHS
    from examples import EXAMPLES, EXAMPLES_BY_SLUG, PYTHON_VERSION, REFERENCE_URL


class AppResponse:
    def __init__(self, body, status=200, headers=None):
        self.body = body
        self.status = status
        self.headers = headers


def list_examples():
    return EXAMPLES


def get_example(slug):
    return EXAMPLES_BY_SLUG.get(slug)


def build_dynamic_worker_code(example_code: str) -> str:
    """Build a Python Dynamic Worker module that executes one example.

    The parent Worker supplies only curated example code from this repository. The
    dynamic Worker has no outbound network access when loaded by src.main.
    """
    return f'''from workers import WorkerEntrypoint, Response
import contextlib
import io
import traceback

EXAMPLE_CODE = {example_code!r}


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        stdout = io.StringIO()
        namespace = {{"__name__": "__main__"}}
        try:
            with contextlib.redirect_stdout(stdout):
                exec(EXAMPLE_CODE, namespace)
            return Response(stdout.getvalue(), headers={{"Content-Type": "text/plain; charset=utf-8"}})
        except Exception:
            return Response(traceback.format_exc(), status=500, headers={{"Content-Type": "text/plain; charset=utf-8"}})
'''


_TEMPLATE_DIR = Path(__file__).with_name("templates")
_TEMPLATE_CACHE = {}
SITE_URL = "https://www.pythonbyexample.dev"


FAVICON_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Python By Example">
  <rect width="64" height="64" rx="14" fill="#F5F1EB"/>
  <path d="M14 22l13 10-13 10" fill="none" stroke="#FF4801" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="31" y="40" fill="#521000" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="18" font-weight="800">py</text>
</svg>'''



def render_inline(text: str) -> str:
    parts = text.split("`")
    rendered = []
    for index, part in enumerate(parts):
        if index % 2:
            rendered.append(f'<code class="syntax-inline">{html.escape(part)}</code>')
        else:
            rendered.append(html.escape(part))
    return "".join(rendered)


def _template(name: str) -> str:
    if name not in _TEMPLATE_CACHE:
        _TEMPLATE_CACHE[name] = (_TEMPLATE_DIR / name).read_text()
    return _TEMPLATE_CACHE[name]


def _replace(template: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        template = template.replace(f"__{key}__", value)
    return template


def _meta_description(text: str) -> str:
    text = " ".join(text.split())
    if len(text) <= 175:
        return text
    return text[:172].rsplit(" ", 1)[0] + "…"


def _layout(title: str, content: str, description: str | None = None, path: str = "/", og_type: str = "website", include_editor: bool = False) -> str:
    description = _meta_description(description or "Learn Python with concise, editable examples that run in isolated Cloudflare Dynamic Python Workers.")
    canonical_url = f"{SITE_URL}{path}"
    page_title = title if title == "Python By Example" else f"{title} · Python By Example"
    editor_script = f'<script type="module" src="{html.escape(ASSET_PATHS["EDITOR_JS"])}"></script>' if include_editor else ""
    return _replace(
        _template("layout.html"),
        {
            "PAGE_TITLE": html.escape(page_title),
            "TITLE": html.escape(title),
            "REFERENCE_URL": html.escape(REFERENCE_URL),
            "PYTHON_VERSION": html.escape(PYTHON_VERSION),
            "META_DESCRIPTION": html.escape(description),
            "CANONICAL_URL": html.escape(canonical_url),
            "OG_TYPE": html.escape(og_type),
            "SITE_CSS": html.escape(ASSET_PATHS["SITE_CSS"]),
            "SYNTAX_JS": html.escape(ASSET_PATHS["SYNTAX_JS"]),
            "EDITOR_JS": html.escape(ASSET_PATHS["EDITOR_JS"]),
            "EDITOR_SCRIPT": editor_script,
            "CONTENT": content,
        },
    )


def render_home() -> str:
    cards = []
    for example in list_examples():
        cards.append(
            _replace(
                '<a class="card" href="/examples/__SLUG__"><p class="eyebrow">__SECTION__</p><h2>__TITLE__</h2><p class="meta">__SUMMARY__</p></a>',
                {
                    "SECTION": html.escape(example["section"]),
                    "SLUG": html.escape(example["slug"]),
                    "TITLE": html.escape(example["title"]),
                    "SUMMARY": html.escape(example["summary"]),
                },
            )
        )
    content = _replace(
        _template("home.html"),
        {"PYTHON_VERSION": html.escape(PYTHON_VERSION), "CARDS": "".join(cards)},
    )
    return _layout(
        "Python By Example",
        content,
        description="Learn Python 3.13 with concise, editable examples, expected output, official documentation links, and Cloudflare Dynamic Worker execution.",
        path="/",
        og_type="website",
    )


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
        <textarea name="code" id="code-editor" spellcheck="false" rows="{max(14, woven_source.count(chr(10)) + 2)}">{html.escape(woven_source)}</textarea>
        <div class="playground-toolbar"><button class="button" type="submit">Run all</button><button class="tool-button" type="button" data-reset onclick="resetCode()">Reset</button></div>
      </form>
    </details>
  </section>
  <section class="lp-cells" aria-label="Literate cells with output">{"".join(cells)}</section>
  <section class="notebook-notes"><h2>Notes</h2><ul>{notes}</ul></section>
</article>
<script>
const originalCode = {json.dumps(woven_source)};
function editor() {{ return document.getElementById('code-editor'); }}
function resizeEditor() {{ const field = editor(); if (!field) return; field.style.height = 'auto'; field.style.height = field.scrollHeight + 'px'; }}
function resetCode() {{ editor().value = originalCode; resizeEditor(); editor().focus(); }}
resizeEditor();
const field = editor(); if (field) field.addEventListener('input', resizeEditor);
</script>
'''
    return _layout(f'{example["title"]} literate cells option', content, description=f'Prototype layout for the {example["title"]} Python example.', path='/layout-options/cell-output-flow', include_editor=True)


def render_example_page(example, output=None, code=None, execution_time_ms=None):
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
    walkthrough_html = "".join(
        f'<section class="lesson-step lp-cell"><div class="lp-prose">{"".join(f"<p>{render_inline(prose)}</p>" for prose in step["prose"])}</div><div class="cell-source"><p class="cell-label">Source</p><pre><code class="language-python">{html.escape(step["code"])}</code></pre></div><div class="cell-output"><p class="cell-label">Output</p><pre><code>{html.escape(step["output"])}</code></pre></div></section>'
        for index, step in enumerate(walkthrough, 1)
    )
    notes_html = "".join(f"<li>{note}</li>" for note in notes)
    see_also_examples = [get_example(slug) for slug in example.get("see_also", [])]
    see_also_links = "".join(
        f'<li><a class="text-link" href="/examples/{html.escape(item["slug"])}">{html.escape(item["title"])}</a></li>'
        for item in see_also_examples
        if item is not None
    )
    see_also_html = f'<section class="see-also"><h2>See also</h2><ul>{see_also_links}</ul></section>' if see_also_links else ""
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
            "OUTPUT_PLACEHOLDER": " data-output-placeholder" if output is None else "",
            "OUTPUT_HEADING": html.escape(output_heading),
            "SHOWN_OUTPUT": html.escape(shown_output),
            "EXECUTION_TIME": html.escape(execution_time),
            "ORIGINAL_CODE_JSON": json.dumps(example["code"]),
        },
    )
    return _layout(
        example["title"],
        content,
        description=f'{example["summary"]} Includes editable Python {PYTHON_VERSION} code, expected output, and links to the official Python documentation.',
        path=f'/examples/{example["slug"]}',
        og_type="article",
        include_editor=True,
    )


def route(url: str, method: str = "GET") -> AppResponse:
    without_scheme = url.split("://", 1)[-1]
    path_part = without_scheme.split("/", 1)[1] if "/" in without_scheme else ""
    path = ("/" + path_part.split("?", 1)[0]).rstrip("/") or "/"
    if method == "GET" and path == "/favicon.svg":
        return AppResponse(FAVICON_SVG, headers={"Content-Type": "image/svg+xml; charset=utf-8"})
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
    if path.startswith("/examples/"):
        slug = path.split("/", 2)[2]
        example = get_example(slug)
        if example is None:
            return AppResponse(_layout("Not Found", "<h1>Example not found</h1>"), status=404)
        return AppResponse(
            render_example_page(example), headers={"Content-Type": "text/html; charset=utf-8"}
        )
    return AppResponse(_layout("Not Found", "<h1>Not found</h1>"), status=404)
