from __future__ import annotations

import builtins
import html
import io
import json
import keyword
import token
import tokenize

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


def _layout(title: str, content: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} · Python By Example</title>
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <style>
    :root {{ color-scheme: light; --accent: #FF4801; --accent-hover: #FF7038; --accent-soft: rgba(255, 72, 1, 0.08); --text: #521000; --muted: rgba(82, 16, 0, 0.7); --subtle: rgba(82, 16, 0, 0.4); --page: #F5F1EB; --surface: #FFFBF5; --surface-2: #FFFDFB; --surface-3: #FEF7ED; --hairline: #EBD5C1; --hairline-soft: rgba(235, 213, 193, 0.5); --space-1: .5rem; --space-2: .75rem; --space-3: 1rem; --space-4: 1.5rem; --space-5: 2rem; --space-6: 3rem; }}
    * {{ box-sizing: border-box; }}
    html {{ -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }}
    body {{ max-width: 1040px; margin: 0 auto; padding: var(--space-4); color: var(--text); font: 16px/1.6 FT Kunst Grotesk, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif; background: radial-gradient(circle at top left, rgba(255, 72, 1, 0.10), transparent 34rem), var(--page); }}
    header {{ position: sticky; top: 0; z-index: 2; margin: 0 calc(-1 * var(--space-4)) var(--space-5); padding: var(--space-2) var(--space-4); backdrop-filter: blur(16px); background: rgba(245, 241, 235, 0.82); }}
    nav {{ display: flex; align-items: center; justify-content: space-between; gap: 1rem; }}
    nav a {{ color: inherit; text-decoration: underline; text-decoration-color: var(--hairline); text-underline-offset: .22em; transition-property: color, text-decoration-color; transition-duration: 160ms; transition-timing-function: cubic-bezier(0.2, 0, 0, 1); }}
    nav a:hover {{ color: var(--accent); text-decoration-color: var(--accent); }}
    .button:active {{ transform: scale(0.96); }}
    h1, h2 {{ letter-spacing: -0.04em; line-height: 1.05; text-wrap: balance; }}
    h1 {{ font-size: clamp(2.4rem, 7vw, 5.75rem); margin: 0 0 1rem; }}
    h2 {{ margin-top: 0; }}
    p, li {{ text-wrap: pretty; }}
    pre {{ overflow: auto; padding: 1rem; border-radius: 1rem; background: #0b1020; color: #f9fafb; box-shadow: 0 1px 1px rgba(0,0,0,.12), 0 12px 42px rgba(0,0,0,.18); }}
    textarea {{ box-sizing: border-box; width: 100%; height: auto; min-height: 18rem; padding: 1rem; overflow: hidden; resize: vertical; border: 1px dashed var(--hairline); border-radius: .875rem; outline: 0; background: var(--surface-2); color: var(--text); box-shadow: inset 0 1px 0 rgba(255,255,255,.55); font: 14px/1.5 Apercu Mono Pro, SF Mono, Fira Code, Consolas, monospace; tab-size: 4; transition-property: border-color, box-shadow; transition-duration: 150ms; transition-timing-function: cubic-bezier(0, 0, 0.2, 1); }}
    textarea:focus {{ border-color: var(--accent); box-shadow: 0 0 0 3px rgba(255, 72, 1, 0.2), inset 0 1px 0 rgba(255,255,255,.55); }}
    code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-variant-numeric: tabular-nums; }}
    .syntax-inline {{ padding: .08rem .25rem; border-radius: .25rem; background: var(--accent-soft); color: var(--text); font-size: .94em; }}
    .tok-keyword {{ color: #9D2B00; font-weight: 700; }}
    .tok-builtin {{ color: #6A3A00; }}
    .tok-string {{ color: #8A4B00; }}
    .tok-number {{ color: #7C2D12; }}
    .tok-comment {{ color: var(--muted); font-style: italic; }}
    .tok-operator {{ color: var(--accent); }}
    .brand {{ font-weight: 800; }}
    .nav-links {{ display: flex; gap: .35rem; }}
    .nav-links a {{ padding: 0 .9rem; color: var(--muted); }}
    .hero {{ overflow: hidden; border: 1px solid var(--hairline); border-radius: 1rem; padding: clamp(1.5rem, 5vw, 4rem); margin-bottom: 1.25rem; background: linear-gradient(135deg, var(--surface), var(--surface-3)); box-shadow: 0 1px 3px rgba(82, 16, 0, 0.04), 0 4px 12px rgba(82, 16, 0, 0.02); }}
    .hero p {{ max-width: 66ch; color: var(--muted); font-size: 1.08rem; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: var(--space-3); }}
    .card {{ min-height: 10rem; border: 1px solid var(--hairline); border-radius: .75rem; padding: var(--space-3); background: var(--surface-2); box-shadow: 0 1px 3px rgba(82, 16, 0, 0.04), 0 4px 12px rgba(82, 16, 0, 0.02); transition-property: transform, background-color, border-color; transition-duration: 200ms; transition-timing-function: cubic-bezier(0, 0, 0.2, 1); }}
    .card:hover {{ transform: translateY(-2px); background: var(--surface-3); border-color: var(--accent); }}
    .card a {{ color: inherit; text-decoration: underline; text-decoration-color: var(--hairline); text-underline-offset: .18em; }}
    .card a:hover {{ text-decoration-color: var(--accent); }}
    .button {{ min-height: 40px; border: 1px solid var(--accent); border-radius: 9999px; padding: .72rem 1rem; background: var(--accent); color: white; cursor: pointer; font-weight: 650; box-shadow: 0 1px 3px rgba(82, 16, 0, 0.04), 0 4px 12px rgba(82, 16, 0, 0.02); transition-property: transform, opacity, border-style; transition-duration: 150ms; transition-timing-function: cubic-bezier(0.25, 0.46, 0.45, 0.94); }}
    .button:hover {{ opacity: .95; border-color: var(--accent-hover); }}
    .meta {{ color: var(--muted); font-variant-numeric: tabular-nums; }}
    .eyebrow {{ margin: 0 0 var(--space-2); color: var(--accent); font-size: .78rem; font-weight: 750; letter-spacing: .08em; text-transform: uppercase; }}
    .text-link {{ color: var(--text); text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: .22em; }}
    .text-link:hover {{ color: var(--accent); }}
    .example-shell {{ padding: clamp(var(--space-3), 3vw, var(--space-5)) 0; }}
    .example-intro {{ max-width: 68ch; margin-bottom: var(--space-5); }}
    .literate-program {{ margin: var(--space-5) 0; border-block: 1px solid var(--hairline); }}
    .lesson-step {{ display: grid; grid-template-columns: minmax(18rem, .9fr) minmax(0, 1.35fr); gap: clamp(var(--space-4), 4vw, var(--space-6)); align-items: start; padding: var(--space-4) 0; border-top: 1px dashed var(--hairline-soft); }}
    .lesson-step:first-child {{ border-top: 0; }}
    .lesson-step p {{ margin: 0; color: var(--muted); max-width: 38ch; }}
    .lesson-step pre {{ margin: 0; padding: 0 0 0 var(--space-3); border-left: 2px solid var(--accent); border-radius: 0; background: transparent; color: var(--text); box-shadow: none; }}
    .lesson-step code {{ white-space: pre-wrap; }}
    .playground {{ margin-top: var(--space-6); padding-top: var(--space-4); border-top: 1px solid var(--hairline); }}
    .runner-grid {{ display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(18rem, .75fr); gap: var(--space-4); align-items: stretch; }}
    .playground-toolbar {{ display: flex; gap: .5rem; flex-wrap: wrap; align-items: center; margin: .8rem 0 1rem; }}
    .tool-button {{ min-height: 40px; border: 1px solid var(--hairline); border-radius: 9999px; padding: .62rem .9rem; background: var(--surface-2); color: var(--text); cursor: pointer; transition-property: transform, background-color, border-style; transition-duration: 150ms; }}
    .tool-button:hover {{ background: var(--surface-3); border-color: var(--accent); }}
    .tool-button:active {{ transform: scale(0.96); }}
    .output-panel {{ min-height: 18rem; display: flex; flex-direction: column; border: 1px dashed var(--hairline); border-radius: .75rem; padding: 1rem; background: var(--surface); }}
    .output-panel pre {{ flex: 1; min-height: 0; overflow: visible; white-space: pre-wrap; overflow-wrap: anywhere; margin-bottom: 0; }}
    .example-top, .example-nav {{ display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin-bottom: 1rem; flex-wrap: wrap; }}
    .example-nav {{ margin-top: var(--space-5); padding-top: var(--space-3); border-top: 1px solid var(--hairline); }}
    footer {{ margin-block: 2rem; color: var(--muted); }}
    @media (max-width: 860px) {{ .lesson-step, .runner-grid {{ grid-template-columns: 1fr; }} body {{ padding: .875rem; }} header {{ margin-inline: -.875rem; padding-inline: .875rem; }} }}
    @media (prefers-reduced-motion: reduce) {{ *, *::before, *::after {{ transition-duration: 1ms !important; }} }}
  </style>
</head>
<body>
  <header>
    <nav><a class="brand" href="/">Python By Example</a><span class="nav-links"><a href="{REFERENCE_URL}">Python {PYTHON_VERSION} docs</a><a href="/examples/hello-world">Start</a></span></nav>
  </header>
  <main>{content}</main>
  <footer class="meta">Inspired by Go by Example. Examples execute in Cloudflare Dynamic Python Workers.</footer>
</body>
</html>"""


def render_home() -> str:
    cards = []
    for example in list_examples():
        cards.append(
            f'''<article class="card">
  <p class="eyebrow">{html.escape(example["section"])}</p>
  <h2><a href="/examples/{html.escape(example["slug"])}">{html.escape(example["title"])}</a></h2>
  <p class="meta">{html.escape(example["summary"])}</p>
</article>'''
        )
    return _layout(
        "Python By Example",
        f'''<section class="hero">
  <p class="eyebrow">Python {PYTHON_VERSION} · Cloudflare Dynamic Workers</p>
  <h1>Python By Example</h1>
  <p>Learn Python with small, editable examples backed by the official Python {PYTHON_VERSION} docs. Run each snippet in an isolated Dynamic Python Worker using the newest Python version currently supported by Cloudflare Workers/Pyodide.</p>
</section>
<section class="grid">{"".join(cards)}</section>''',
    )


def _example_neighbors(slug):
    slugs = [item["slug"] for item in list_examples()]
    index = slugs.index(slug)
    previous_example = get_example(slugs[index - 1]) if index > 0 else None
    next_example = get_example(slugs[index + 1]) if index + 1 < len(slugs) else None
    return previous_example, next_example


def render_example_page(example, output=None, code=None):
    notes = "".join(f"<li>{render_inline(note)}</li>" for note in example.get("notes", []))
    walkthrough = "".join(
        f'''<div class="lesson-step"><p>{render_inline(step["prose"])}</p><pre><code>{highlight_python(step["code"])}</code></pre></div>'''
        for step in example.get("walkthrough", [])
    )
    shown_output = output if output is not None else example.get("expected_output", "Run this example to see output here.")
    placeholder_attr = "" if output is not None else " data-output-placeholder"
    output_heading = "Output" if output is not None else "Expected output"
    output_html = f"<section class=\"output-panel\" aria-live=\"polite\"{placeholder_attr}><h2>{output_heading}</h2><pre><code>{html.escape(shown_output)}</code></pre></section>"
    editable_code = example["code"] if code is None else code
    original_code_json = json.dumps(example["code"])
    previous_example, next_example = _example_neighbors(example["slug"])
    previous_link = f'<a class="text-link" rel="prev" href="/examples/{html.escape(previous_example["slug"])}">← {html.escape(previous_example["title"])}</a>' if previous_example else '<span></span>'
    next_link = f'<a class="text-link" rel="next" href="/examples/{html.escape(next_example["slug"])}">{html.escape(next_example["title"])} →</a>' if next_example else '<span></span>'
    content = f'''<article class="example-shell">
  <div class="example-top"><a class="text-link" href="/">← All examples</a><a class="text-link" href="{html.escape(example["doc_url"])}">Python docs reference</a></div>
  <section class="example-intro">
    <p class="eyebrow">{html.escape(example["section"])}</p>
    <h1>{html.escape(example["title"])}</h1>
    <p class="meta">{html.escape(example["summary"])}</p>
  </section>
  <section class="literate-program" aria-label="Annotated code walkthrough">{walkthrough}</section>
  <h2>Notes</h2>
  <ul>{notes}</ul>
  <nav class="example-nav" aria-label="Example navigation">{previous_link}{next_link}</nav>
  <section class="playground" aria-label="Editable runnable example">
    <h2>Run the complete example</h2>
    <div class="runner-grid">
      <form method="post" action="/examples/{html.escape(example["slug"])}">
        <textarea name="code" id="code-editor" spellcheck="false" rows="{max(18, editable_code.count(chr(10)) + 2)}">{html.escape(editable_code)}</textarea>
        <div class="playground-toolbar">
          <button class="button" type="submit">Run</button>
          <button class="tool-button" type="button" data-reset onclick="resetCode()">Reset</button>
        </div>
      </form>
      {output_html}
    </div>
  </section>
</article>
<script>
const originalCode = {original_code_json};
function editor() {{ return document.getElementById('code-editor'); }}
function resizeEditor() {{ const field = editor(); field.style.height = 'auto'; field.style.height = field.scrollHeight + 'px'; }}
function resetCode() {{ editor().value = originalCode; resizeEditor(); editor().focus(); }}
resizeEditor();
editor().addEventListener('input', resizeEditor);
const form = document.querySelector('form');
const outputPanel = document.querySelector('.output-panel');
form.addEventListener('submit', async (event) => {{
  event.preventDefault();
  outputPanel.removeAttribute('data-output-placeholder');
  outputPanel.querySelector('code').textContent = 'Running in a Dynamic Python Worker…';
  try {{
    const response = await fetch(form.action, {{
      method: 'POST',
      body: new URLSearchParams(new FormData(form)),
      headers: {{ 'Content-Type': 'application/x-www-form-urlencoded' }}
    }});
    if (!response.ok) throw new Error('HTTP ' + response.status);
    const html = await response.text();
    const doc = new DOMParser().parseFromString(html, 'text/html');
    const nextOutput = doc.querySelector('.output-panel');
    if (nextOutput) outputPanel.innerHTML = nextOutput.innerHTML;
  }} catch (error) {{
    outputPanel.querySelector('code').textContent = 'Run failed: ' + error.message;
  }}
}});
const hash = new URL(window.location.href).hash;
if (hash.startsWith('#code=')) {{
  try {{ editor().value = decodeURIComponent(escape(atob(hash.slice(6)))); }} catch (error) {{}}
}}
</script>'''
    return _layout(example["title"], content)


FAVICON_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#F5F1EB"/>
  <path d="M13 38c0-13 10-23 23-23h8v10h-8c-7 0-12 5-12 13v2h20v10H13V38Z" fill="#FF4801"/>
  <circle cx="43" cy="20" r="4" fill="#521000"/>
</svg>'''


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
        return AppResponse(render_example_page(example), headers={"Content-Type": "text/html; charset=utf-8"})
    return AppResponse(_layout("Not Found", "<h1>Not found</h1>"), status=404)
