from __future__ import annotations

import contextlib
import difflib
import html
import io
import json
from pathlib import Path

try:
    from .asset_manifest import ASSET_PATHS
    from .examples import EXAMPLES, EXAMPLES_BY_SLUG, PYTHON_VERSION, REFERENCE_URL
    from .marginalia import render_for_anchor, render_for_section
except ImportError:  # Cloudflare Python Workers import sibling modules from main's directory.
    from asset_manifest import ASSET_PATHS
    from examples import EXAMPLES, EXAMPLES_BY_SLUG, PYTHON_VERSION, REFERENCE_URL
    from marginalia import render_for_anchor, render_for_section


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

JOURNEYS = [
    {
        "slug": "runtime",
        "title": "Runtime",
        "summary": "This journey builds the smallest coherent model of Python at runtime: programs run statements, names refer to objects, objects have types, and operations ask those objects to do work.",
        "sections": [
            {
                "title": "Start with executable evidence.",
                "summary": "Learners first need to see that every page is a runnable program with visible output.",
                "items": [
                    ("example", "hello-world", "start with a complete program and its output"),
                    ("example", "values", "see that Python programs manipulate runtime objects"),
                    ("example", "literals", "write small values directly in source code"),
                    ("example", "variables", "understand that names bind to objects rather than storing values themselves"),
                    ("example", "constants", "learn the convention Python uses for values that should not change"),
                ],
            },
            {
                "title": "Separate value, identity, and absence.",
                "summary": "This section prevents early confusion about equality, object identity, missing values, and truth tests.",
                "items": [
                    ("example", "none", "represent expected absence with a singleton object"),
                    ("example", "booleans", "combine facts with boolean operators"),
                    ("example", "truthiness", "predict how objects behave in boolean contexts"),
                    ("example", "equality-and-identity", "distinguish value equality from object identity"),
                    ("example", "mutability", "predict when operations change an object in place"),
                    ("example", "object-lifecycle", "explain references, garbage collection, and why identity can outlive a single name"),
                ],
            },
            {
                "title": "Read expressions as object operations.",
                "summary": "This section connects operators, text, and formatting to Python's data model.",
                "items": [
                    ("example", "numbers", "use numeric objects and arithmetic operators"),
                    ("example", "operators", "combine, compare, and test values with expression syntax"),
                    ("example", "strings", "treat text as Unicode rather than raw bytes"),
                    ("example", "string-formatting", "turn objects into readable text at output boundaries"),
                    ("example", "bytes-and-bytearray", "contrast text with binary data and explicit decoding"),
                ],
            },
        ],
    },
    {
        "slug": "control-flow",
        "title": "Control Flow",
        "summary": "This journey follows how a Python program chooses which path runs, names facts at decision points, and exits early when the remaining work no longer applies.",
        "sections": [
            {
                "title": "Choose between paths.",
                "summary": "Start with ordinary branching and boolean predicates before reaching for more compact forms.",
                "items": [
                    ("example", "booleans", "combine facts into readable conditions"),
                    ("example", "truthiness", "use object truth values without hiding intent"),
                    ("example", "operators", "build comparisons and boolean expressions for conditions"),
                    ("example", "conditionals", "choose between branches with clear predicates"),
                ],
            },
            {
                "title": "Name and shape decisions.",
                "summary": "Some branches become clearer when the code names an intermediate value or dispatches on data shape.",
                "items": [
                    ("example", "assignment-expressions", "name an intermediate value inside a condition when it improves clarity"),
                    ("example", "match-statements", "dispatch on the shape of data rather than only on boolean tests"),
                    ("example", "advanced-match-patterns", "combine destructuring, alternatives, and guards in pattern matching"),
                ],
            },
            {
                "title": "Stop as soon as the answer is known.",
                "summary": "Early exits make the successful path easier to read by moving exceptional or completed cases out of the way.",
                "items": [
                    ("example", "guard-clauses", "show how early returns reduce nested conditional code"),
                    ("example", "assertions", "state assumptions that should fail loudly while developing"),
                    ("example", "exceptions", "leave the current path when ordinary return values are not enough"),
                ],
            },
        ],
    },
    {
        "slug": "iteration",
        "title": "Iteration",
        "summary": "This journey follows repeated work from ordinary loops to the iterator protocol: consume values, stop deliberately, and produce lazy streams only when they help.",
        "sections": [
            {
                "title": "Choose the right loop shape.",
                "summary": "Loops differ by what they consume, when they stop, and whether completion itself carries meaning.",
                "items": [
                    ("example", "for-loops", "consume values from an iterable"),
                    ("example", "while-loops", "repeat while a condition must be rechecked"),
                    ("example", "break-and-continue", "interrupt or skip loop work intentionally"),
                    ("example", "loop-else", "attach completion logic to loops that did not break"),
                    ("example", "sentinel-iteration", "show `iter(callable, sentinel)` for repeated reads until a marker appears"),
                ],
            },
            {
                "title": "See the protocol behind `for`.",
                "summary": "The important mental shift is that loops consume producers through a protocol rather than special-casing lists.",
                "items": [
                    ("example", "iterating-over-iterables", "separate value producers from value consumers"),
                    ("example", "iterators", "use `iter()` and `next()` to expose the protocol behind `for`"),
                    ("example", "generators", "write functions that produce values lazily"),
                ],
            },
            {
                "title": "Compose lazy value streams.",
                "summary": "Iterator pipelines are useful when code can transform values one at a time instead of materializing every intermediate result.",
                "items": [
                    ("example", "generator-expressions", "create lazy one-pass streams with expression syntax"),
                    ("example", "itertools", "compose iterator streams without materializing every value"),
                    ("example", "yield-from", "delegate part of a generator to another iterable"),
                ],
            },
        ],
    },
    {
        "slug": "shapes",
        "title": "Shapes",
        "summary": "This journey teaches the core Python habit of choosing a data shape, transforming it directly, and making the result visible.",
        "sections": [
            {
                "title": "Pick the container that matches the question.",
                "summary": "Lists, tuples, dictionaries, and sets answer different questions about order, position, lookup, and uniqueness.",
                "items": [
                    ("example", "lists", "store ordered mutable data"),
                    ("example", "tuples", "group fixed-position values"),
                    ("example", "dicts", "look up values by key"),
                    ("example", "sets", "model uniqueness and membership"),
                    ("example", "collections-module", "show `deque`, `Counter`, `defaultdict`, and `namedtuple` as specialized shapes"),
                ],
            },
            {
                "title": "Move between shapes deliberately.",
                "summary": "Most everyday Python code is data reshaping, so learners need the idioms for selecting, unpacking, and rebuilding values.",
                "items": [
                    ("example", "unpacking", "bind names from structured values"),
                    ("example", "slices", "select ranges from sequences"),
                    ("example", "comprehensions", "build concrete collections from compact loops"),
                    ("example", "comprehension-patterns", "compose filters and nested transformations"),
                    ("example", "sorting", "order records with key functions"),
                    ("example", "copying-collections", "contrast shallow copies, deep copies, and shared nested data"),
                ],
            },
            {
                "title": "Cross text and data boundaries.",
                "summary": "Programs often receive text and produce structured data, so parsing and serialization belong in the data journey.",
                "items": [
                    ("example", "number-parsing", "turn text into numbers safely"),
                    ("example", "json", "move structured data across a text boundary"),
                    ("example", "regular-expressions", "extract structure from text patterns"),
                    ("example", "datetime", "represent dates, times, and durations as typed values"),
                    ("example", "csv-data", "show row-shaped text data and dictionary records"),
                ],
            },
        ],
    },
    {
        "slug": "interfaces",
        "title": "Interfaces",
        "summary": "This journey shows how Python grows from simple functions to callable APIs, object interfaces, protocols, and metaclasses.",
        "sections": [
            {
                "title": "Start with functions as named behavior.",
                "summary": "Functions are the first abstraction boundary because they name behavior and control how callers provide information.",
                "items": [
                    ("example", "functions", "package behavior behind a name"),
                    ("example", "keyword-only-arguments", "make important call-site choices explicit"),
                    ("example", "positional-only-parameters", "hide parameter names that should remain implementation details"),
                    ("example", "args-and-kwargs", "accept flexible call shapes when forwarding or adapting APIs"),
                    ("example", "multiple-return-values", "return multiple related values as a tuple"),
                ],
            },
            {
                "title": "Use functions as values.",
                "summary": "Python functions can capture state, be passed around, and wrap other functions.",
                "items": [
                    ("example", "scope-global-nonlocal", "control where assignment happens"),
                    ("example", "closures", "capture state in nested functions"),
                    ("example", "recursion", "solve self-similar problems with a base case"),
                    ("example", "lambdas", "write small unnamed functions for expression positions"),
                    ("example", "decorators", "wrap behavior without changing call sites"),
                    ("example", "partial-functions", "show how to pre-fill arguments with `functools.partial`"),
                ],
            },
            {
                "title": "Bundle behavior with state.",
                "summary": "Classes become useful when data and behavior need to move together behind a stable interface.",
                "items": [
                    ("example", "classes", "bundle state and behavior into a new object type"),
                    ("example", "inheritance-and-super", "reuse and extend behavior through parent classes"),
                    ("example", "dataclasses", "generate common methods for data containers"),
                    ("example", "properties", "keep attribute syntax while adding computation or validation"),
                    ("example", "special-methods", "connect objects to Python syntax and built-ins"),
                    ("example", "truth-and-size", "make objects work with truth tests and `len()`"),
                    ("example", "container-protocols", "support membership, lookup, and assignment syntax"),
                    ("example", "callable-objects", "make stateful instances callable like functions"),
                    ("example", "operator-overloading", "define operators only when the operation is unsurprising"),
                    ("example", "attribute-access", "customize fallback lookup and assignment carefully"),
                    ("example", "descriptors", "explain the protocol behind methods, properties, and managed attributes"),
                    ("example", "metaclasses", "customize class creation when ordinary class tools are not enough"),
                ],
            },
        ],
    },
    {
        "slug": "types",
        "title": "Types",
        "summary": "This journey maps Python's runtime object model to optional static annotations so learners know what types can and cannot promise.",
        "sections": [
            {
                "title": "Keep runtime and static analysis separate.",
                "summary": "The first lesson is that annotations describe expectations for tools while ordinary Python objects still run the program.",
                "items": [
                    ("example", "type-hints", "document expected types and feed type checkers"),
                    ("example", "protocols", "describe required behavior by structural shape"),
                    ("example", "enums", "name a fixed set of symbolic values"),
                    ("example", "runtime-type-checks", "show `type()`, `isinstance()`, and `issubclass()` without turning Python into Java"),
                ],
            },
            {
                "title": "Describe realistic data shapes.",
                "summary": "Typed Python becomes useful when annotations explain optional values, unions, callables, and JSON-like records.",
                "items": [
                    ("example", "union-and-optional-types", "show `X | Y` and `None`-aware APIs"),
                    ("example", "type-aliases", "name complex types with `type` statements or aliases"),
                    ("example", "typed-dicts", "type dictionary records that come from JSON"),
                    ("example", "literal-and-final", "express constrained values and names that should not be rebound"),
                    ("example", "callable-types", "type functions that are passed as arguments"),
                ],
            },
            {
                "title": "Scale annotations for reusable libraries.",
                "summary": "Advanced typing exists to preserve information across reusable functions, containers, and decorators.",
                "items": [
                    ("example", "generics-and-typevar", "write reusable typed containers and functions"),
                    ("example", "paramspec", "preserve callable signatures through decorators"),
                    ("example", "overloads", "describe APIs whose return type depends on the input shape"),
                    ("example", "casts-and-any", "show escape hatches and their tradeoffs"),
                    ("example", "newtype", "create distinct static identities for runtime-compatible values"),
                ],
            },
        ],
    },
    {
        "slug": "reliability",
        "title": "Reliability",
        "summary": "This journey follows the boundaries where programs fail, clean up, split into modules, communicate with the outside world, and run concurrent work.",
        "sections": [
            {
                "title": "Make failure explicit.",
                "summary": "Robust Python code distinguishes expected absence, broken assumptions, recoverable errors, and domain-specific failures.",
                "items": [
                    ("example", "exceptions", "signal and recover from errors"),
                    ("example", "assertions", "state internal assumptions"),
                    ("example", "exception-chaining", "preserve the cause while translating an error"),
                    ("example", "exception-groups", "handle multiple failures together"),
                    ("example", "custom-exceptions", "name failures in the language of the problem domain"),
                    ("example", "warnings", "signal soft problems and deprecations"),
                ],
            },
            {
                "title": "Control resource and module boundaries.",
                "summary": "Cleanup, deletion, imports, and modules define where responsibilities begin and end.",
                "items": [
                    ("example", "context-managers", "pair setup with reliable cleanup"),
                    ("example", "delete-statements", "remove names, attributes, and items intentionally"),
                    ("example", "modules", "split code into importable files"),
                    ("example", "import-aliases", "make imported names clear at use sites"),
                    ("example", "packages", "show package directories, `__init__.py`, and public module boundaries"),
                    ("example", "virtual-environments", "isolate dependencies for a project"),
                ],
            },
            {
                "title": "Handle operations that outlive one expression.",
                "summary": "I/O, testing, logging, subprocesses, and concurrency require different control boundaries from ordinary expressions.",
                "items": [
                    ("example", "async-await", "await concurrent I/O-shaped work"),
                    ("example", "async-iteration-and-context", "consume async streams and cleanup protocols"),
                    ("example", "logging", "record operational events without using `print()`"),
                    ("example", "testing", "write deterministic tests with `unittest` or `pytest`"),
                    ("example", "subprocesses", "run external commands safely"),
                    ("example", "threads-and-processes", "contrast concurrency choices beyond `asyncio`"),
                    ("example", "networking", "make HTTP or socket boundaries explicit"),
                ],
            },
        ],
    },
    {
        "slug": "workers",
        "title": "Workers",
        "summary": "This journey explains the examples that were adapted so they can teach operating-system boundaries while still running inside Cloudflare Dynamic Workers.",
        "sections": [
            {
                "title": "Replace unavailable process boundaries with portable evidence.",
                "summary": "Dynamic Workers run Python in a constrained runtime, so examples cannot assume child processes, shell commands, or project-local virtual environments are available.",
                "items": [
                    ("example", "virtual-environments", "report stable environment facts instead of creating or depending on a local virtual environment"),
                    ("example", "subprocesses", "show the command and `CompletedProcess` result shape"),
                    ("example", "threads-and-processes", "compare thread and process executor boundaries"),
                ],
            },
            {
                "title": "Keep network lessons local to the protocol boundary.",
                "summary": "Workers should not open arbitrary low-level sockets, so the networking example teaches addresses, protocol constants, and bytes without making an outbound connection.",
                "items": [
                    ("example", "bytes-and-bytearray", "show the text-to-bytes boundary that networking and subprocess APIs usually require"),
                    ("example", "networking", "make endpoint and byte-encoding boundaries visible without opening a socket"),
                    ("example", "async-await", "show the supported coroutine model for I/O-shaped work in this environment"),
                ],
            },
            {
                "title": "Preserve the lesson while respecting the runtime.",
                "summary": "The changed examples favor deterministic, editable evidence over fake demonstrations of unavailable operating-system features.",
                "items": [
                    ("example", "logging", "show operational output through a configurable Python API rather than shell output"),
                    ("example", "testing", "capture test-runner output so the page remains deterministic"),
                    ("example", "context-managers", "show cleanup boundaries that still apply when resources are represented abstractly"),
                ],
            },
        ],
    },
]

JOURNEYS_BY_SLUG = {journey["slug"]: journey for journey in JOURNEYS}


SEE_ALSO_EDGE_LABELS = {
    ("break-and-continue", "loop-else"): "contrast",
    ("assignment-expressions", "conditionals"): "contrast",
    ("yield-from", "generators"): "prerequisite",
    ("async-iteration-and-context", "async-await"): "prerequisite",
    ("delete-statements", "mutability"): "shared mechanism",
    ("positional-only-parameters", "keyword-only-arguments"): "contrast",
    ("assertions", "exceptions"): "alternative",
    ("exception-chaining", "exceptions"): "builds on",
    ("exception-groups", "exceptions"): "alternative",
    ("operators", "numbers"): "related syntax",
    ("operators", "booleans"): "condition building",
    ("operators", "assignment-expressions"): "specialized expression",
    ("literals", "values"): "value surface",
    ("literals", "strings"): "text literal",
    ("literals", "sets"): "container literal",
}


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
        {"PYTHON_VERSION": html.escape(PYTHON_VERSION), "CARDS": "".join(sections_html)},
    )
    return _layout(
        "Python By Example",
        content,
        description="Learn Python 3.13 with concise, editable examples, expected output, official documentation links, and Cloudflare Dynamic Worker execution.",
        path="/",
        og_type="website",
    )


def render_journeys_index():
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
        description="Curated Python By Example journeys that compose individual examples into larger mental maps, with explicit placeholders for missing topics.",
        path="/journeys",
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
        description=f'{journey["summary"]} A curated Python By Example journey with explicit placeholders for missing examples.',
        path=f'/journeys/{journey["slug"]}',
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


def _render_cell(step):
    prose_html = "".join(f"<p>{render_inline(prose)}</p>" for prose in step["prose"])
    source = html.escape(step["code"])
    if step.get("kind") == "unsupported":
        return f'<section class="lesson-step lp-cell unsupported-cell"><div class="lp-prose">{prose_html}</div><div class="cell-code-stack"><div class="cell-source"><p class="cell-label">Standard Python</p><pre><code class="language-python">{source}</code></pre></div></div></section>'
    return f'<section class="lesson-step lp-cell"><div class="lp-prose">{prose_html}</div><div class="cell-code-stack"><div class="cell-source"><p class="cell-label">Source</p><pre><code class="language-python">{source}</code></pre></div><div class="cell-output"><p class="cell-label">Output</p><pre><code>{html.escape(step["output"])}</code></pre></div></div></section>'


def _turnstile_widget(site_key: str | None) -> str:
    if not site_key:
        return ""
    escaped = html.escape(site_key)
    return (
        '<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>'
        f'<div class="cf-turnstile" data-sitekey="{escaped}"></div>'
    )


def render_example_page(example, output=None, code=None, execution_time_ms=None, turnstile_site_key=None):
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
    walkthrough_parts: list[str] = []
    for i, step in enumerate(walkthrough):
        walkthrough_parts.append(_render_cell(step))
        banner_html = render_for_anchor(example["slug"], f"cell-{i}")
        if banner_html:
            walkthrough_parts.append(banner_html)
    walkthrough_html = "".join(walkthrough_parts)
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
            "TURNSTILE_WIDGET": _turnstile_widget(turnstile_site_key),
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


def route(url: str, method: str = "GET", turnstile_site_key: str | None = None) -> AppResponse:
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
