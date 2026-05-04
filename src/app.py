from __future__ import annotations

import builtins
import html
import io
import json
import keyword
import token
import tokenize
from pathlib import Path

try:
    from .examples import EXAMPLES, EXAMPLES_BY_SLUG, PYTHON_VERSION, REFERENCE_URL
except ImportError:  # Cloudflare Python Workers import sibling modules from main's directory.
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


_BUILTIN_NAMES = set(dir(builtins))
_TEMPLATE_DIR = Path(__file__).with_name("templates")
_TEMPLATE_CACHE = {}


FAVICON_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Python By Example">
  <rect width="64" height="64" rx="14" fill="#F5F1EB"/>
  <path d="M14 22l13 10-13 10" fill="none" stroke="#FF4801" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="31" y="40" fill="#521000" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="18" font-weight="800">py</text>
</svg>'''


def _span(class_name: str, value: str) -> str:
    return f'<span class="{class_name}">{html.escape(value)}</span>'


def highlight_python(code: str) -> str:
    """Tiny Python syntax highlighter for read-only example fragments."""
    result = []
    last_line, last_col = 1, 0
    try:
        tokens = tokenize.generate_tokens(io.StringIO(code).readline)
        for tok in tokens:
            tok_type, tok_text, start, end, _line = tok
            if tok_type in {tokenize.ENCODING, token.ENDMARKER}:
                continue
            start_line, start_col = start
            end_line, end_col = end
            if start_line > last_line:
                result.append("\n" * (start_line - last_line))
                last_col = 0
            if start_col > last_col:
                result.append(" " * (start_col - last_col))
            if tok_type == token.NAME and keyword.iskeyword(tok_text):
                result.append(_span("tok-keyword", tok_text))
            elif tok_type == token.NAME and tok_text in _BUILTIN_NAMES:
                result.append(_span("tok-builtin", tok_text))
            elif tok_type == token.STRING:
                result.append(_span("tok-string", tok_text))
            elif tok_type == token.NUMBER:
                result.append(_span("tok-number", tok_text))
            elif tok_type == tokenize.COMMENT:
                result.append(_span("tok-comment", tok_text))
            elif tok_type == token.OP:
                result.append(_span("tok-operator", tok_text))
            else:
                result.append(html.escape(tok_text))
            last_line, last_col = end_line, end_col
    except tokenize.TokenError:
        return html.escape(code)
    return "".join(result)


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


def _layout(title: str, content: str) -> str:
    return _replace(
        _template("layout.html"),
        {
            "TITLE": html.escape(title),
            "REFERENCE_URL": html.escape(REFERENCE_URL),
            "PYTHON_VERSION": html.escape(PYTHON_VERSION),
            "CONTENT": content,
        },
    )


def render_home() -> str:
    cards = []
    for example in list_examples():
        cards.append(
            _replace(
                '<article class="card"><p class="eyebrow">__SECTION__</p><h2><a href="/examples/__SLUG__">__TITLE__</a></h2><p class="meta">__SUMMARY__</p></article>',
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
    return _layout("Python By Example", content)


def _example_neighbors(slug):
    slugs = [item["slug"] for item in list_examples()]
    index = slugs.index(slug)
    previous_example = get_example(slugs[index - 1]) if index > 0 else None
    next_example = get_example(slugs[index + 1]) if index + 1 < len(slugs) else None
    return previous_example, next_example


def render_example_page(example, output=None, code=None):
    notes = [render_inline(note) for note in example.get("notes", [])]
    walkthrough = [
        {"prose": render_inline(step["prose"]), "code": highlight_python(step["code"])}
        for step in example.get("walkthrough", [])
    ]
    shown_output = output if output is not None else example.get("expected_output", "Run this example to see output here.")
    output_heading = "Output" if output is not None else "Expected output"
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
        f'<div class="lesson-step"><p>{step["prose"]}</p><pre><code>{step["code"]}</code></pre></div>'
        for step in walkthrough
    )
    notes_html = "".join(f"<li>{note}</li>" for note in notes)
    content = _replace(
        _template("example.html"),
        {
            "DOC_URL": html.escape(example["doc_url"]),
            "SECTION": html.escape(example["section"]),
            "TITLE": html.escape(example["title"]),
            "SUMMARY": html.escape(example["summary"]),
            "WALKTHROUGH": walkthrough_html,
            "NOTES": notes_html,
            "PREVIOUS_LINK": previous_link,
            "NEXT_LINK": next_link,
            "SLUG": html.escape(example["slug"]),
            "EDITOR_ROWS": str(max(18, editable_code.count("\n") + 2)),
            "EDITABLE_CODE": html.escape(editable_code),
            "OUTPUT_PLACEHOLDER": " data-output-placeholder" if output is None else "",
            "OUTPUT_HEADING": html.escape(output_heading),
            "SHOWN_OUTPUT": html.escape(shown_output),
            "ORIGINAL_CODE_JSON": json.dumps(example["code"]),
        },
    )
    return _layout(example["title"], content)


def route(url: str, method: str = "GET") -> AppResponse:
    without_scheme = url.split("://", 1)[-1]
    path_part = without_scheme.split("/", 1)[1] if "/" in without_scheme else ""
    path = ("/" + path_part.split("?", 1)[0]).rstrip("/") or "/"
    if method == "GET" and path == "/favicon.svg":
        return AppResponse(FAVICON_SVG, headers={"Content-Type": "image/svg+xml; charset=utf-8"})
    if method == "GET" and path == "/":
        return AppResponse(render_home(), headers={"Content-Type": "text/html; charset=utf-8"})
    if path.startswith("/examples/"):
        slug = path.split("/", 2)[2]
        example = get_example(slug)
        if example is None:
            return AppResponse(_layout("Not Found", "<h1>Example not found</h1>"), status=404)
        return AppResponse(
            render_example_page(example), headers={"Content-Type": "text/html; charset=utf-8"}
        )
    return AppResponse(_layout("Not Found", "<h1>Not found</h1>"), status=404)
