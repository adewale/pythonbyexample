"""Marginalia attachments and figure registry.

Authors of example markdown never touch this file. The project owner curates
named figures here and attaches them to cells via slug + anchor.

Anchors today:
    "cell-0", "cell-1", … each literate-program cell, zero-indexed.

(Reserved for future positions: `intro`, `notes`, `playground`. Banner
positions `before` / `after-cell-N` / `after-walkthrough` are documented
in the spec but currently exercised only by scripts/build_prototypes.py.)

The renderer in app.py emits each attached figure inline inside its cell
as `<figure class="cell-figure">`. The cell switches to single-column
stacking (prose, figure, code) via the `has-figure` class so the figure
sits between prose and code-stack without disturbing cells without
figures, which keep today's prose|code 2-column grid.

See docs/visual-explainer-spec.md for the full design and
docs/journey-visualisation-rubric.md for the figure-quality rubric.
"""

from __future__ import annotations

import html
from typing import Callable

try:
    from .marginalia_grammar import Canvas
except ImportError:  # Cloudflare Workers import siblings without the package prefix.
    from marginalia_grammar import Canvas


# ─── Named figures ─────────────────────────────────────────────────────


def aliasing_mutation(c: Canvas) -> None:
    """Two names binding to one mutable list, before and after a mutation."""
    c.tag(0, 12, "before")
    c.name_box(0, 18, "first")
    c.name_box(0, 48, "second")
    c.closed_arrow(60, 30, 86, 46, emphasis=False)
    c.closed_arrow(60, 60, 86, 46, emphasis=False)
    c.object_box(88, 32, "", '["python"]', w=88, h=28)

    c.tag(0, 100, "after append")
    c.name_box(0, 108, "first")
    c.name_box(0, 138, "second")
    c.closed_arrow(60, 120, 86, 136, emphasis=False)
    c.closed_arrow(60, 150, 86, 136, emphasis=False)
    c.object_box(88, 122, "", '["python","workers"]', w=130, h=28)


def tuple_no_mutation(c: Canvas) -> None:
    """The contrast: two names binding to one immutable tuple — no mutation possible."""
    c.tag(0, 12, "tuple — frozen")
    c.name_box(0, 18, "first")
    c.name_box(0, 48, "second")
    c.closed_arrow(60, 30, 86, 46, emphasis=False)
    c.closed_arrow(60, 60, 86, 46, emphasis=False)
    c.object_box(88, 32, "", '("python",)', w=110, h=28)

    c.tag(0, 100, "no .append")
    c.name_box(0, 108, "first")
    c.name_box(0, 138, "second")
    c.closed_arrow(60, 120, 86, 136, emphasis=False)
    c.closed_arrow(60, 150, 86, 136, emphasis=False)
    c.object_box(88, 122, "", '("python",)', w=110, h=28)
    c.label(150, 170, "tuples raise AttributeError", anchor="middle")


def iterator_unroll(c: Canvas) -> None:
    """Four passes of next() over a sequence, with a caret advancing each row."""
    items = list("abcd")
    for i in range(4):
        y = 8 + i * 30
        c.cells(20, y, items)
        c.caret(20 + i * 24 + 12, y)
        suffix = " — last" if i == 3 else ""
        c.label(124, y + 16, f"next(){suffix}")


def scope_rings(c: Canvas) -> None:
    """LEGB lookup: nested rings, lookup path traced from innermost outward."""
    c.frame(8, 6, 200, 100, label="B · built-in")
    c.frame(28, 22, 160, 76, label="G · global")
    c.frame(48, 38, 120, 52, label="E · enclosing")
    c.frame(68, 54, 80, 28, label="L · local")
    c.dot(108, 68, emphasis=True)
    c.dashed(108, 78, 108, 100)


def closure_cell(c: Canvas) -> None:
    """Inner function references a cell created by the outer call.

    Outer scope holds the `cell` (the captured `factor`); the inner function
    keeps a reference into it, so the call survives the outer return.
    """
    c.frame(0, 16, 240, 96, label="make_multiplier")
    c.tag(16, 32, "cell")
    c.cell(16, 38, "factor=2", w=84, h=22)
    c.frame(112, 38, 122, 60, label="multiply")
    c.label(173, 76, "uses cell", anchor="middle")
    c.closed_arrow(128, 76, 102, 56, emphasis=True)


def slice_ruler(c: Canvas) -> None:
    """Adjacent slices [:3] and [3:] split a sequence at index 3."""
    items = list("abcdef")
    for i, v in enumerate(items):
        c.cell(20 + i * 32, 30, v, w=32, h=24)
    c.hairline(20, 64, 20 + 6 * 32, 64)
    for i in range(7):
        c.tick(20 + i * 32, 64)
        c.label(20 + i * 32, 76, str(i), anchor="middle")
    # bracket above for [:3]
    c.dashed(20, 22, 20, 28)
    c.dashed(20 + 3 * 32, 22, 20 + 3 * 32, 28)
    c.dashed(20, 22, 20 + 3 * 32, 22)
    c.label(20 + 1.5 * 32, 18, "[:3]", anchor="middle")
    # bracket below for [3:]
    c.dashed(20 + 3 * 32, 92, 20 + 3 * 32, 86)
    c.dashed(20 + 6 * 32, 92, 20 + 6 * 32, 86)
    c.dashed(20 + 3 * 32, 92, 20 + 6 * 32, 92)
    c.label(20 + 4.5 * 32, 104, "[3:]", anchor="middle")


def branch_fork(c: Canvas) -> None:
    """Make decisions explicitly: a value flows through a predicate to one branch."""
    c.cell(0, 36, "value", w=52, h=22)
    c.closed_arrow(52, 47, 80, 47, emphasis=False)
    c.node(98, 47, "?", r=14)
    c.closed_arrow(110, 38, 158, 14, emphasis=False)
    c.closed_arrow(110, 56, 158, 80, emphasis=False)
    c.cell(160, 4, "case A", w=68, h=22)
    c.cell(160, 70, "case B", w=68, h=22)


def loop_repetition(c: Canvas) -> None:
    """The shape of a loop: walk the sequence, run the body, return."""
    c.cells(0, 28, ["a", "b", "c", "d"], w=28)
    c.caret(0 + 14, 28)
    c.closed_arrow(116, 40, 142, 40, emphasis=False)
    c.cell(144, 28, "body", w=56, h=24)
    c.dashed(172, 54, 172, 76)
    c.dashed(172, 76, 14, 76)
    c.dashed(14, 76, 14, 54)
    c.closed_arrow(14, 56, 14, 40, emphasis=True)


def iter_protocol(c: Canvas) -> None:
    """The hidden machinery behind for: iterable → iter() → next() … values."""
    c.object_box(0, 30, "iterable", "[a,b,c]", w=82, h=28)
    c.dashed(84, 44, 118, 44)
    c.label(101, 38, "iter()", anchor="middle")
    c.object_box(120, 30, "iterator", "", w=80, h=28)
    c.closed_arrow(200, 44, 232, 44, emphasis=True)
    c.label(216, 38, "next()", anchor="middle")
    c.cells(234, 32, ["a", "b", "c"], w=22)


# ─── Runtime journey ──────────────────────────────────────────────────


def program_output(c: Canvas) -> None:
    """Runtime · Start with executable evidence: a program produces visible output."""
    c.cell(0, 28, 'print("…")', w=92, h=28)
    c.closed_arrow(92, 42, 124, 42, emphasis=False)
    c.label(108, 36, "stdout", anchor="middle")
    c.cell(126, 28, "hello world", w=110, h=28, soft=True)


def identity_and_equality(c: Canvas) -> None:
    """Runtime · Separate value, identity, and absence: same object vs equal objects."""
    c.tag(0, 14, "is + ==")
    c.name_box(0, 22, "a")
    c.name_box(0, 50, "b")
    c.closed_arrow(60, 34, 100, 50, emphasis=False)
    c.closed_arrow(60, 62, 100, 50, emphasis=False)
    c.cell(102, 38, "[1,2]", w=46, h=24, soft=True)
    c.tag(170, 14, "== only")
    c.name_box(170, 22, "a")
    c.name_box(170, 50, "b")
    c.closed_arrow(230, 34, 252, 34, emphasis=False)
    c.closed_arrow(230, 62, 252, 62, emphasis=False)
    c.cell(254, 22, "[1,2]", w=44, h=22, soft=True)
    c.cell(254, 52, "[1,2]", w=44, h=22, soft=True)


def operator_dispatch(c: Canvas) -> None:
    """Runtime · Read expressions as object operations: syntax becomes a method call."""
    c.cell(0, 30, "a + b", w=70, h=28)
    c.closed_arrow(70, 44, 116, 44, emphasis=True)
    c.label(93, 36, "dispatches", anchor="middle")
    c.cell(118, 30, "a.__add__(b)", w=140, h=28, soft=True)


# ─── Shapes journey ───────────────────────────────────────────────────


def container_questions(c: Canvas) -> None:
    """Shapes · Pick the container that matches the question — each answers a different one."""
    pairs = [
        ("list", "[a,b]", "ordered"),
        ("tuple", "(a,b)", "fixed"),
        ("dict", "{k:v}", "lookup"),
        ("set", "{a,b}", "unique"),
    ]
    for i, (tag, val, q) in enumerate(pairs):
        x = i * 70
        c.object_box(x, 26, tag, val, w=64, h=28)
        c.label(x + 32, 70, q, anchor="middle")


def reshape_pipeline(c: Canvas) -> None:
    """Shapes · Move between shapes deliberately: one input, one transform, one result."""
    c.cell(0, 30, "[3,1,4]", w=80, h=28)
    c.closed_arrow(80, 44, 120, 44, emphasis=True)
    c.label(100, 36, "sorted", anchor="middle")
    c.cell(122, 30, "[1,3,4]", w=80, h=28, soft=True)


def text_data_boundary(c: Canvas) -> None:
    """Shapes · Cross text and data boundaries: text in, structured value out."""
    c.cell(0, 30, '"42"', w=70, h=28)
    c.tag(0, 24, "text")
    c.closed_arrow(70, 44, 110, 44, emphasis=True)
    c.label(90, 36, "parse", anchor="middle")
    c.object_box(112, 30, "int", "42", w=58, h=28)


# ─── Interfaces journey ───────────────────────────────────────────────


def function_signature(c: Canvas) -> None:
    """Interfaces · Functions as named behavior: input → body → output."""
    c.closed_arrow(0, 44, 32, 44, emphasis=False)
    c.label(16, 36, "args", anchor="middle")
    c.frame(34, 26, 110, 36, label="def f(...)")
    c.closed_arrow(144, 44, 176, 44, emphasis=False)
    c.label(160, 36, "return", anchor="middle")


def function_as_value(c: Canvas) -> None:
    """Interfaces · Functions as values: name binds to a function object."""
    c.frame(0, 22, 80, 36, label="fn")
    c.mono(40, 44, "def f")
    c.closed_arrow(80, 40, 116, 40, emphasis=True)
    c.cell(118, 26, "g = fn", w=80, h=28, soft=True)


def class_with_state(c: Canvas) -> None:
    """Interfaces · Bundle behavior with state: a class groups fields and methods."""
    c.frame(0, 8, 150, 92, label="class Box")
    c.tag(12, 26, "state")
    c.cell(12, 32, "x · y", w=126, h=22)
    c.tag(12, 64, "methods")
    c.cell(12, 70, "move(...)", w=126, h=22)


# ─── Types journey ────────────────────────────────────────────────────


def annotation_ghost(c: Canvas) -> None:
    """Types · Keep runtime and static separate: annotations describe; runtime accepts any object."""
    c.mono(0, 36, "def f(x: int, y: str) -> bool: …", anchor="start")
    c.dashed(54, 28, 76, 28)
    c.dashed(102, 28, 124, 28)
    c.dashed(150, 28, 192, 28)


def union_types(c: Canvas) -> None:
    """Types · Describe realistic shapes: a slot accepting one of several types."""
    c.tag(0, 14, "x: int | str | None")
    c.cell(0, 22, "x", w=44, h=28)
    c.closed_arrow(44, 36, 80, 14, emphasis=False)
    c.closed_arrow(44, 36, 80, 36, emphasis=False)
    c.closed_arrow(44, 36, 80, 58, emphasis=False)
    c.cell(82, 4, "int", w=70, h=22, soft=True)
    c.cell(82, 26, "str", w=70, h=22, soft=True)
    c.cell(82, 48, "None", w=70, h=22, soft=True)


def generic_preservation(c: Canvas) -> None:
    """Types · Scale annotations: a generic preserves the input type through the call."""
    c.cell(0, 30, "T", w=36, h=28, soft=True)
    c.closed_arrow(36, 44, 72, 44, emphasis=True)
    c.frame(74, 26, 100, 36, label="fn[T]")
    c.closed_arrow(174, 44, 210, 44, emphasis=True)
    c.cell(212, 30, "T", w=36, h=28, soft=True)


# ─── Reliability journey ──────────────────────────────────────────────


def exception_lanes(c: Canvas) -> None:
    """Reliability · Make failure explicit: try/except/else/finally as parallel lanes."""
    ys = [(20, "try"), (40, "except"), (60, "else"), (80, "finally")]
    path = [(50, 20), (110, 20), (130, 60), (200, 60), (220, 80), (290, 80)]
    c.lanes(ys, x0=40, x1=300, path=path)


def context_bowtie(c: Canvas) -> None:
    """Reliability · Control resource boundaries: enter → body → exit, with raise routed through exit."""
    c.node(20, 48, "in", r=14)
    c.closed_arrow(34, 48, 76, 48, emphasis=False)
    c.cell(78, 36, "body", w=86, h=24)
    c.closed_arrow(164, 48, 206, 48, emphasis=False)
    c.node(220, 48, "out", r=14)
    c.dashed(122, 60, 210, 48)


def async_swimlane(c: Canvas) -> None:
    """Reliability · Operations that outlive one expression: loop and coroutine swap on await."""
    c.lane(28, x0=20, x1=270, label="loop")
    c.lane(64, x0=20, x1=270, label="coro")
    c.cell(40, 58, "", w=34, h=12)
    c.dashed(76, 64, 110, 28)
    c.cell(112, 22, "", w=58, h=12)
    c.dashed(172, 28, 206, 64)
    c.cell(208, 58, "", w=34, h=12)
    c.label(95, 16, "await", anchor="middle")
    c.label(190, 16, "resume", anchor="middle")


# ─── Control flow journey ─────────────────────────────────────────────


def naming_decisions(c: Canvas) -> None:
    """Control flow · Name and shape decisions: the walrus binds while comparing."""
    c.cell(0, 30, "len(xs)", w=80, h=28)
    c.closed_arrow(80, 44, 110, 44, emphasis=True)
    c.label(95, 36, ":=", anchor="middle")
    c.cell(112, 4, "n", w=40, h=22, soft=True)
    c.tag(112, 0, "name")
    c.cell(112, 50, "value", w=78, h=22, soft=True)
    c.dashed(152, 16, 196, 16)
    c.cell(198, 4, "n > 10", w=72, h=22)


def early_exit(c: Canvas) -> None:
    """Control flow · Stop as soon as the answer is known: the loop exits on first match."""
    c.cells(0, 28, ["a", "b", "c", "d", "e"], w=28)
    c.dot(70, 40, emphasis=True)
    c.closed_arrow(70, 56, 70, 78, emphasis=True)
    c.cell(40, 80, "found · break", w=80, h=24, soft=True)
    c.label(70, 14, "first match", anchor="middle")


# ─── Iteration journey ────────────────────────────────────────────────


# ─── Example figures (promoted from the gestalt) ──────────────────────


def variables_bind(c: Canvas) -> None:
    """Variables · names bind to objects: the canonical Python picture."""
    c.bind(0, 6, "x", "int", "42", object_w=70, gap=20)


def call_stack(c: Canvas) -> None:
    """Recursion · stacked frames of the same function with different arguments."""
    chain = [3, 2, 1, 0]
    for i, n in enumerate(chain):
        suffix = " ← base" if n == 0 else ""
        c.cell(0, i * 22, f"factorial({n}){suffix}", w=180, h=20)
    c.dashed(192, 90, 192, 18)
    c.closed_arrow(192, 30, 192, 18, emphasis=True)


def decorator_rebind(c: Canvas) -> None:
    """Decorators · before: name binds to function. After @dec: name binds to wrapper."""
    c.tag(0, 12, "before")
    c.bind(0, 18, "f", "fn", "f₀", object_w=50, gap=20)
    c.tag(0, 70, "after @dec")
    c.name_box(0, 78, "f")
    c.closed_arrow(60, 90, 96, 90, emphasis=True)
    c.cell(98, 76, "wrapper", w=80, h=28)
    c.object_box(186, 78, "", "f₀", w=44, h=24)
    c.dashed(178, 90, 186, 90)


def mro_chain(c: Canvas) -> None:
    """Inheritance · diamond becomes a linear MRO via C3 linearization."""
    # Diamond ghost above
    c.frame(80, 0, 40, 22, ghost=True)
    c.mono(100, 16, "A")
    c.ghost(98, 22, 58, 42)
    c.ghost(102, 22, 142, 42)
    c.frame(40, 42, 40, 22, ghost=True)
    c.mono(60, 58, "B")
    c.frame(120, 42, 40, 22, ghost=True)
    c.mono(140, 58, "C")
    c.ghost(60, 64, 96, 80)
    c.ghost(140, 64, 104, 80)
    c.frame(80, 80, 40, 22, ghost=True)
    c.mono(100, 96, "D")
    # MRO chain below
    c.tag(0, 118, "mro")
    chain = [("D", 36), ("B", 36), ("C", 36), ("A", 36), ("object", 56)]
    x = 0
    for v, w in chain:
        c.cell(x, 124, v, w=w, h=22)
        x += w


def dataclass_fields(c: Canvas) -> None:
    """Dataclasses · fields declared once become __init__ parameters."""
    c.tag(0, 12, "declaration")
    fields = [("name", "str"), ("age", "int"), ("tags", "list")]
    for i, (n, t) in enumerate(fields):
        c.cell(0, 18 + i * 20, f"{n} : {t}", w=110, h=20)
    c.closed_arrow(110, 48, 146, 48, emphasis=True)
    c.object_box(148, 32, "", "__init__(name, age, tags)", w=128, h=32)


def class_triangle(c: Canvas) -> None:
    """Classes · instance → class → type — every Python value sits on this triangle."""
    c.dot(20, 28)
    c.label(20, 54, "instance", anchor="middle")
    c.closed_arrow(26, 28, 86, 28, emphasis=False)
    c.frame(88, 10, 60, 36, label="class")
    c.mono(118, 32, "Class")
    c.closed_arrow(148, 28, 208, 28, emphasis=False)
    c.frame(210, 10, 60, 36, label="type")
    c.mono(240, 32, "type")


def exception_cause_context(c: Canvas) -> None:
    """Exception chaining · explicit `__cause__` (raise from) vs implicit `__context__`."""
    c.cell(0, 20, "ValueError", w=100, h=32)
    c.closed_arrow(100, 28, 180, 28, emphasis=True)
    c.label(140, 20, "__cause__", anchor="middle")
    c.dashed(100, 44, 180, 44)
    c.label(140, 62, "__context__", anchor="middle")
    c.cell(182, 20, "RuntimeError", w=100, h=32)


def unpacking_bind(c: Canvas) -> None:
    """Unpacking · left-side names bind to right-side positions; *rest gathers the middle."""
    items = ["1", "2", "3", "4", "5"]
    for i, v in enumerate(items):
        c.cell(i * 30, 0, v, w=30, h=22)
    c.cell(0, 58, "a", w=30, h=22)
    c.cell(30, 58, "*rest", w=90, h=22, ghost=True)
    c.cell(120, 58, "b", w=30, h=22)
    c.dashed(15, 22, 15, 58)
    c.dashed(45, 22, 75, 58)
    c.dashed(75, 22, 75, 58)
    c.dashed(105, 22, 75, 58)
    c.dashed(135, 22, 135, 58)


def comprehension_equivalence(c: Canvas) -> None:
    """Comprehensions · the comprehension above and the equivalent for-loop below."""
    c.cell(0, 0, "[x*2 for x in xs if x > 0]", w=280, h=22, soft=True)
    c.cell(0, 30, "out = []", w=280, h=14, ghost=True)
    c.cell(0, 44, "for x in xs:", w=280, h=14, ghost=True)
    c.cell(0, 58, "    if x > 0: out.append(x*2)", w=280, h=14, ghost=True)


def list_append(c: Canvas) -> None:
    """Lists · mutable sequence; `.append` extends the same list object."""
    c.cells(0, 8, ["3", "1", "4"], w=24)
    c.cell(72, 8, "+1", ghost=True)
    c.closed_arrow(98, 20, 132, 20, emphasis=True)
    c.label(136, 18, ".append", anchor="start")


def dict_buckets(c: Canvas) -> None:
    """Dictionaries · hashed buckets; collisions chain into a neighbouring slot."""
    c.tag(0, 12, "hash → bucket")
    rows = [("0", '"a" → 1'), ("1", '"b" → 2'), ("2", '"c" → 3')]
    for i, (idx, body) in enumerate(rows):
        y = 18 + i * 24
        c.label(0, y + 16, idx, anchor="start")
        c.cell(14, y, body, w=80, h=24)
    c.closed_arrow(96, 54, 132, 54, emphasis=True)
    c.cell(134, 42, '"d" → 4', w=80, h=24, soft=True)
    c.label(218, 58, "collision", anchor="start")


# ─── Workers journey (abstract sections; designs tentative) ──────────


def workers_portable_evidence(c: Canvas) -> None:
    """Workers · process boundaries unavailable; portable evidence (a value) crosses instead."""
    c.frame(0, 8, 70, 30, ghost=True, label="process A")
    c.frame(110, 8, 70, 30, ghost=True, label="process B")
    c.dashed(74, 8, 106, 38)
    c.dashed(74, 38, 106, 8)
    c.tag(0, 60, "instead")
    c.cell(0, 66, "value", w=60, h=22, soft=True)
    c.closed_arrow(60, 77, 116, 77, emphasis=True)
    c.cell(118, 66, "captured", w=62, h=22)


def workers_protocol_local(c: Canvas) -> None:
    """Workers · protocol shape, not real network: assert on the shape, not the socket."""
    c.tag(0, 12, "request shape")
    c.cell(0, 18, "GET /resource", w=140, h=22, soft=True)
    c.closed_arrow(70, 44, 70, 60, emphasis=True)
    c.tag(0, 80, "response shape")
    c.cell(0, 86, "200 · { … }", w=140, h=22, soft=True)


def workers_lesson_runtime(c: Canvas) -> None:
    """Workers · lesson shape preserved while runtime constraints are respected."""
    c.frame(0, 6, 70, 32, label="lesson")
    c.mono(34, 26, "evidence")
    c.frame(110, 6, 70, 32, label="runtime")
    c.mono(144, 26, "respected")
    c.closed_arrow(70, 22, 110, 22, emphasis=True)


def lazy_stream(c: Canvas) -> None:
    """Iteration · Compose lazy value streams: filter and map flow values without materialising."""
    c.object_box(0, 26, "source", "[a,b,c]", w=78, h=24)
    c.dashed(78, 38, 102, 38)
    c.object_box(104, 26, "filter", "x>0", w=68, h=24)
    c.dashed(172, 38, 196, 38)
    c.object_box(198, 26, "map", "x*2", w=64, h=24)
    c.closed_arrow(262, 38, 294, 38, emphasis=True)
    c.label(278, 30, "next()", anchor="middle")


# Registry: figure_name -> (paint_fn, viewbox_w, viewbox_h)
FIGURES: dict[str, tuple[Callable[[Canvas], None], int, int]] = {
    "aliasing-mutation": (aliasing_mutation, 220, 175),
    "tuple-no-mutation": (tuple_no_mutation, 220, 185),
    "iterator-unroll": (iterator_unroll, 220, 130),
    "scope-rings": (scope_rings, 216, 116),
    "closure-cell": (closure_cell, 240, 120),
    "slice-ruler": (slice_ruler, 232, 120),
    "branch-fork": (branch_fork, 232, 100),
    "loop-repetition": (loop_repetition, 204, 90),
    "iter-protocol": (iter_protocol, 304, 70),
    # Runtime
    "program-output": (program_output, 240, 80),
    "identity-and-equality": (identity_and_equality, 304, 96),
    "operator-dispatch": (operator_dispatch, 260, 70),
    # Shapes
    "container-questions": (container_questions, 280, 88),
    "reshape-pipeline": (reshape_pipeline, 204, 80),
    "text-data-boundary": (text_data_boundary, 172, 70),
    # Interfaces
    "function-signature": (function_signature, 188, 80),
    "function-as-value": (function_as_value, 200, 66),
    "class-with-state": (class_with_state, 152, 108),
    # Types
    "annotation-ghost": (annotation_ghost, 220, 52),
    "union-types": (union_types, 156, 80),
    "generic-preservation": (generic_preservation, 250, 70),
    # Reliability
    "exception-lanes": (exception_lanes, 320, 100),
    "context-bowtie": (context_bowtie, 244, 76),
    "async-swimlane": (async_swimlane, 280, 84),
    # Control flow + Iteration coverage gap (see audit)
    "naming-decisions": (naming_decisions, 274, 80),
    "early-exit": (early_exit, 144, 116),
    "lazy-stream": (lazy_stream, 300, 56),
    # Promoted from the gestalt — wired to example pages via ATTACHMENTS
    "variables-bind": (variables_bind, 180, 44),
    "call-stack": (call_stack, 200, 100),
    "decorator-rebind": (decorator_rebind, 232, 110),
    "mro-chain": (mro_chain, 200, 152),
    "dataclass-fields": (dataclass_fields, 280, 76),
    "class-triangle": (class_triangle, 274, 60),
    "exception-cause-context": (exception_cause_context, 282, 70),
    "unpacking-bind": (unpacking_bind, 152, 80),
    "comprehension-equivalence": (comprehension_equivalence, 280, 76),
    "list-append": (list_append, 220, 36),
    "dict-buckets": (dict_buckets, 270, 88),
    # Workers journey (constraint-shaped sections; designs tentative)
    "workers-portable-evidence": (workers_portable_evidence, 200, 96),
    "workers-protocol-local": (workers_protocol_local, 144, 116),
    "workers-lesson-runtime": (workers_lesson_runtime, 188, 50),
}


# ─── Attachments ───────────────────────────────────────────────────────

# slug -> [(anchor, figure_name, caption_or_None), …]
ATTACHMENTS: dict[str, list[tuple[str, str, str | None]]] = {
    "mutability": [
        (
            "cell-0",
            "aliasing-mutation",
            "Two names share one mutable list — appending through one name changes the object visible through both.",
        ),
    ],
    "variables": [
        (
            "cell-0",
            "variables-bind",
            "A name is a label that points at an object. Assignment binds the label; the object exists independently.",
        ),
    ],
    "lists": [
        (
            "cell-0",
            "list-append",
            "Lists are mutable sequences. `.append` extends the same list object — no new list is created.",
        ),
    ],
    "dicts": [
        (
            "cell-0",
            "dict-buckets",
            "Each key is hashed to a bucket; collisions chain into the next slot. Lookup is constant-time on average.",
        ),
    ],
    "unpacking": [
        (
            "cell-0",
            "unpacking-bind",
            "Left-side names bind to right-side positions; `*rest` gathers the middle into a list.",
        ),
    ],
    "comprehensions": [
        (
            "cell-0",
            "comprehension-equivalence",
            "A comprehension is a compact spelling of the equivalent for-loop with append, made into one expression.",
        ),
    ],
    "classes": [
        (
            "cell-0",
            "class-triangle",
            "Every Python value sits on the instance → class → type triangle; the metaclass is the type of the class.",
        ),
    ],
    "inheritance-and-super": [
        (
            "cell-0",
            "mro-chain",
            "Multiple inheritance forms a graph; C3 linearisation flattens it into the MRO Python uses for attribute lookup.",
        ),
    ],
    "dataclasses": [
        (
            "cell-0",
            "dataclass-fields",
            "Field declarations become the generated __init__ signature: declaration is the constructor.",
        ),
    ],
    "special-methods": [
        (
            "cell-0",
            "operator-dispatch",
            "Operators are method calls. `a + b` dispatches to `a.__add__(b)`; the data model exposes the syntax.",
        ),
    ],
    "decorators": [
        (
            "cell-0",
            "decorator-rebind",
            "@dec rebinds the name to wrapper(f₀); the original function survives only in the wrapper's closure cell.",
        ),
    ],
    "recursion": [
        (
            "cell-1",
            "call-stack",
            "Each call pushes a new frame with the same name and a smaller argument; the base case unwinds back up the stack.",
        ),
    ],
    "exception-chaining": [
        (
            "cell-0",
            "exception-cause-context",
            "`raise X from Y` sets `__cause__` (explicit); raising during except sets `__context__` (implicit).",
        ),
    ],
}


# ─── Render helpers ────────────────────────────────────────────────────


def _render_svg(figure_name: str) -> str:
    paint, w, h = FIGURES[figure_name]
    canvas = Canvas(w=w, h=h)
    paint(canvas)
    return canvas.to_svg()


def render_for_anchor(slug: str, anchor: str) -> str:
    """HTML for inline figures inside an anchor block. Empty if none.

    Returns one or more `<figure class="cell-figure">` elements. The cell
    that hosts the figure switches to single-column layout via the
    has-figure class added by the renderer, so prose, figure, and code
    stack vertically.
    """
    attachments = ATTACHMENTS.get(slug, [])
    matched = [(name, caption) for (a, name, caption) in attachments if a == anchor]
    if not matched:
        return ""
    parts = []
    for name, caption in matched:
        cap = f"<figcaption>{html.escape(caption)}</figcaption>" if caption else ""
        parts.append(f'<figure class="cell-figure">{_render_svg(name)}{cap}</figure>')
    return "".join(parts)
