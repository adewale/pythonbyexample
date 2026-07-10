"""Marginalia attachments and figure registry.

Example prose and code live in Markdown; illustration definitions and their
slug/anchor attachments are curated here. Figure quality metadata lives in the
``[figures]`` table of ``docs/quality-registries.toml``.

Anchors today:
    "cell-0", "cell-1", … each literate-program cell, zero-indexed.
    The figure renders in a banner row AFTER the named cell.

The renderer in app.py interleaves cells and banners: every cell keeps
its prose|code 2-column grid intact, and a banner row spanning both
columns sits between cells (or after the only cell on single-cell
examples). Multiple figures attached to the same cell share one
banner as a small multiple. Cells without an attached figure render
exactly as before.

See docs/visual-explainer-spec.md for the full design and
docs/journey-visualisation-rubric.md for the figure-quality rubric.
"""

from __future__ import annotations

from typing import Callable

try:
    from .editorial_registry import (
        example_figure_scores as load_example_figure_scores,
        example_quality_scores as load_example_quality_scores,
        figure_attachments as load_figure_attachments,
        journey_section_figure_scores as load_journey_section_figure_scores,
        journey_section_figures as load_journey_section_figures,
    )
    from .marginalia_grammar import Canvas
    from .textfmt import render_inline
except ImportError:  # Cloudflare Workers import siblings without the package prefix.
    from editorial_registry import (  # type: ignore[no-redef]
        example_figure_scores as load_example_figure_scores,
        example_quality_scores as load_example_quality_scores,
        figure_attachments as load_figure_attachments,
        journey_section_figure_scores as load_journey_section_figure_scores,
        journey_section_figures as load_journey_section_figures,
    )
    from marginalia_grammar import Canvas
    from textfmt import render_inline


# ─── Named figures ─────────────────────────────────────────────────────


def aliasing_mutation(c: Canvas) -> None:
    """Two names binding to one mutable list, before and after a mutation."""
    c.two_names_one_object(0, 18, "before", "first", "second", '["python"]', object_w=88)
    c.two_names_one_object(0, 108, "after append", "first", "second",
                           '["python","workers"]', object_w=130)


def tuple_no_mutation(c: Canvas) -> None:
    """The contrast: two names binding to one immutable tuple — no mutation possible."""
    c.two_names_one_object(0, 18, "tuple — frozen", "first", "second",
                           '("python",)', object_w=110)
    c.two_names_one_object(0, 108, "no .append", "first", "second",
                           '("python",)', object_w=110)
    c.label(150, 170, "tuples raise AttributeError", anchor="middle")


def iterator_unroll(c: Canvas) -> None:
    """Four passes of next() over a sequence, with a caret advancing each row."""
    items = list("abcd")
    for i in range(4):
        y = 8 + i * 30
        c.cells(20, y, items)
        c.caret(20 + i * 24 + 12, y, emphasis=(i == 3))
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
    """Iteration journey · choose for, while, or sentinel by the stopping rule."""
    rows = [("for", "iterable exhausted"), ("while", "condition false"), ("sentinel", "marker returned")]
    for i, (loop, stop) in enumerate(rows):
        y = 8 + i * 30
        c.cell(0, y, loop, w=70, h=22)
        c.closed_arrow(70, y + 11, 104, y + 11, emphasis=(loop == "sentinel"))
        c.cell(106, y, stop, w=150, h=22, soft=(loop == "sentinel"))


def while_backedge(c: Canvas) -> None:
    """while-loops · the back-edge that returns control to the test each pass."""
    c.cell(64, 4, "while test:", w=104, h=22)
    c.closed_arrow(116, 26, 116, 46, emphasis=False)
    c.label(124, 40, "true")
    c.cell(64, 48, "body", w=104, h=22)
    c.stroke(168, 59, 204, 59)
    c.stroke(204, 59, 204, 15)
    c.closed_arrow(204, 15, 170, 15, emphasis=True)
    c.label(212, 40, "repeat")
    c.closed_arrow(64, 15, 30, 15, emphasis=False)
    c.label(0, 9, "false")


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
    c.label(93, 22, "dispatches", anchor="middle")
    c.cell(118, 30, "a.__add__(b)", w=140, h=28, soft=True)


def runtime_evidence_loop(c: Canvas) -> None:
    """Runtime journey · source and output form a runnable evidence loop."""
    c.frame(0, 10, 104, 76, label="page")
    c.cell(14, 26, "source", w=74, h=22)
    c.cell(14, 56, "output", w=74, h=22, soft=True)
    c.closed_arrow(104, 48, 142, 48, emphasis=True)
    c.node(160, 48, "run", r=16)
    c.closed_arrow(176, 48, 214, 48, emphasis=False)
    c.cell(216, 34, "evidence", w=88, h=28, soft=True)


def runtime_object_axes(c: Canvas) -> None:
    """Runtime journey · value, identity, and absence are separate questions."""
    c.cell(0, 36, "object", w=70, h=28, soft=True)
    c.closed_arrow(70, 50, 112, 18, emphasis=False)
    c.cell(114, 6, "== value", w=86, h=22)
    c.closed_arrow(70, 50, 112, 50, emphasis=True)
    c.cell(114, 38, "is identity", w=98, h=22, soft=True)
    c.closed_arrow(70, 50, 112, 82, emphasis=False)
    c.cell(114, 70, "None", w=86, h=22)


def runtime_expression_model(c: Canvas) -> None:
    """Runtime journey · expression syntax enters the data model, then returns a value."""
    c.cell(0, 34, "syntax", w=64, h=28)
    c.closed_arrow(64, 48, 102, 48, emphasis=True)
    c.frame(104, 12, 128, 72, label="data model")
    for i, method in enumerate(["__add__", "__len__", "__format__"]):
        c.cell(116, 24 + i * 18, method, w=104, h=16, soft=(i == 0))
    c.closed_arrow(232, 48, 270, 48, emphasis=False)
    c.cell(272, 34, "result", w=70, h=28, soft=True)


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
    """Interfaces journey · a named function is an input/body/return boundary."""
    c.cell(0, 30, "f(2, 3)", w=70, h=34)
    c.closed_arrow(70, 47, 104, 47, emphasis=False)
    c.frame(106, 20, 96, 54, label="def f")
    c.label(154, 50, "body", anchor="middle")
    c.closed_arrow(202, 47, 236, 47, emphasis=True)
    c.cell(238, 30, "return 5", w=70, h=34, soft=True)


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
    c.tag(0, 14, "x: int|str|None")
    c.cell(0, 22, "x", w=44, h=28)
    c.closed_arrow(44, 36, 90, 14, emphasis=False)
    c.closed_arrow(44, 36, 90, 36, emphasis=False)
    c.closed_arrow(44, 36, 90, 58, emphasis=False)
    c.cell(92, 4, "int", w=70, h=22, soft=True)
    c.cell(92, 26, "str", w=70, h=22, soft=True)
    c.cell(92, 48, "None", w=70, h=22, soft=True)


def generic_preservation(c: Canvas) -> None:
    """Types · Scale annotations: a generic preserves the input type through the call."""
    c.cell(0, 30, "T", w=36, h=28, soft=True)
    c.closed_arrow(36, 44, 72, 44, emphasis=False)
    c.frame(74, 26, 100, 36, label="fn[T]")
    c.closed_arrow(174, 44, 210, 44, emphasis=True)
    c.cell(212, 30, "T", w=36, h=28, soft=True)


def type_runtime_static_split(c: Canvas) -> None:
    """Types journey · runtime objects and static tool facts travel on separate tracks."""
    c.frame(0, 10, 210, 46, label="runtime")
    c.cell(16, 24, "value", w=60, h=22, soft=True)
    c.closed_arrow(76, 35, 120, 35, emphasis=True)
    c.cell(122, 24, "runs", w=58, h=22, soft=True)
    c.frame(0, 76, 220, 46, label="static tools")
    c.cell(16, 90, "x: int", w=70, h=22, ghost=True)
    c.closed_arrow(86, 101, 130, 101, emphasis=False)
    c.cell(132, 90, "checks", w=72, h=22, ghost=True)
    c.dashed(46, 56, 46, 76)


def type_shape_catalog(c: Canvas) -> None:
    """Types journey · realistic data shapes pick field, variant, and absence contracts."""
    c.cell(0, 44, "data", w=62, h=24, soft=True)
    rows = [(8, "fields", "TypedDict"), (42, "variant", "Union"), (76, "absence", "Optional")]
    for y, question, shape in rows:
        c.closed_arrow(62, 56, 108, y + 11, emphasis=(shape == "Union"))
        c.cell(110, y, question, w=78, h=22)
        c.cell(198, y, shape, w=90, h=22, soft=(shape == "Union"))


def type_library_contract(c: Canvas) -> None:
    """Types journey · reusable APIs preserve caller contracts across the library boundary."""
    c.cell(0, 40, "caller", w=66, h=24)
    c.closed_arrow(66, 52, 106, 52, emphasis=False)
    c.frame(108, 18, 116, 72, label="library API")
    c.cell(120, 32, "T", w=36, h=20, soft=True)
    c.cell(166, 32, "P", w=36, h=20)
    c.cell(120, 62, "overloads", w=84, h=20)
    c.closed_arrow(224, 52, 264, 52, emphasis=True)
    c.cell(266, 40, "typed result", w=96, h=24, soft=True)


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
    # Land the dashed exit path on the circle's left-side tangent so it
    # doesn't terminate inside the "out" glyph. With body bottom-mid at
    # (122, 60) → circle (220, 48) of r=14, the tangent meets at ≈(206, 50).
    c.dashed(122, 60, 206, 50)


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


def reliability_signal_map(c: Canvas) -> None:
    """Reliability journey · choose an explicit signal for each failure shape."""
    c.cell(0, 52, "problem", w=70, h=24)
    rows = [(4, "assume", "assert"), (36, "recover", "except"), (68, "cause", "chain"), (100, "soft", "warn")]
    for y, kind, signal in rows:
        c.closed_arrow(70, 64, 112, y + 11, emphasis=(signal == "except"))
        c.cell(114, y, kind, w=70, h=22)
        c.cell(194, y, signal, w=72, h=22, soft=(signal == "except"))


def reliability_boundary_map(c: Canvas) -> None:
    """Reliability journey · resources, modules, and environments are explicit boundaries."""
    c.cell(0, 44, "code", w=58, h=24)
    c.closed_arrow(58, 56, 86, 56, emphasis=True)
    c.frame(88, 8, 194, 96, label="boundaries")
    rows = [(22, "resource", "cleanup"), (52, "module", "import"), (82, "env", "runtime")]
    for y, boundary, action in rows:
        c.cell(102, y, boundary, w=82, h=20, soft=(boundary == "resource"))
        c.closed_arrow(184, y + 10, 212, y + 10, emphasis=False)
        c.cell(214, y, action, w=58, h=20)


def reliability_operation_boundary(c: Canvas) -> None:
    """Reliability journey · long-lived operations cross a boundary before evidence returns."""
    c.cell(0, 44, "call", w=58, h=24)
    c.closed_arrow(58, 56, 96, 56, emphasis=True)
    c.frame(98, 18, 128, 76, label="operation")
    c.cell(110, 32, "await", w=46, h=18)
    c.cell(164, 32, "thread", w=52, h=18)
    c.cell(110, 62, "test", w=46, h=18)
    c.cell(164, 62, "log", w=52, h=18)
    c.closed_arrow(226, 56, 266, 56, emphasis=False)
    c.cell(268, 44, "evidence", w=82, h=24, soft=True)


# ─── Control flow journey ─────────────────────────────────────────────


def naming_decisions(c: Canvas) -> None:
    """Control flow journey · name a fact, then dispatch by shape when booleans are too small."""
    c.tag(0, 0, "name fact")
    c.cell(0, 12, "len(xs)", w=70, h=22)
    c.closed_arrow(70, 23, 100, 23, emphasis=False)
    c.label(85, 16, ":=", anchor="middle")
    c.cell(102, 12, "n", w=34, h=22, soft=True)
    c.closed_arrow(136, 23, 166, 23, emphasis=False)
    c.cell(168, 12, "n > 10", w=72, h=22)
    c.tag(0, 56, "dispatch shape")
    c.cell(0, 68, "value", w=70, h=22)
    for i, label in enumerate(["case int", "case [x,y]", "case _"]):
        x = 96 + i * 70
        c.closed_arrow(70 if i == 0 else x - 12, 79, x, 79, emphasis=(i == 1))
        c.cell(x, 68, label, w=62, h=22, soft=(i == 1))


def early_exit(c: Canvas) -> None:
    """Control flow · Stop as soon as the answer is known: the loop exits on first match."""
    c.cells(0, 28, ["a", "b", "c", "d", "e"], w=28)
    c.dot(70, 40)
    c.closed_arrow(70, 56, 70, 78, emphasis=True)
    c.cell(40, 80, "found · break", w=80, h=24, soft=True)
    c.label(70, 14, "first match", anchor="middle")


def control_decision_map(c: Canvas) -> None:
    """Control-flow journey · facts enter one decision point and choose one branch."""
    c.cell(0, 38, "facts", w=58, h=24)
    c.closed_arrow(58, 50, 92, 50, emphasis=False)
    c.node(110, 50, "?", r=15)
    branches = [(8, "if", False), (40, "elif", True), (72, "else", False)]
    for y, label, chosen in branches:
        c.closed_arrow(123, 50, 174, y + 11, emphasis=chosen)
        c.cell(176, y, label, w=64, h=22, soft=chosen)


def control_fact_shape(c: Canvas) -> None:
    """Control-flow journey · name facts or match shape before deciding."""
    c.cell(0, 38, "input", w=62, h=24)
    c.closed_arrow(62, 50, 98, 28, emphasis=False)
    c.cell(100, 16, "name fact", w=92, h=22, soft=True)
    c.closed_arrow(62, 50, 98, 72, emphasis=False)
    c.cell(100, 60, "match shape", w=104, h=22)
    c.closed_arrow(204, 27, 246, 50, emphasis=False)
    c.closed_arrow(204, 71, 246, 50, emphasis=True)
    c.node(264, 50, "?", r=15)


def control_stop_boundary(c: Canvas) -> None:
    """Control-flow journey · once the answer is found, the tail stays unread."""
    for i, item in enumerate(["a", "b", "c", "d", "e"]):
        c.cell(i * 28, 36, item, w=28, h=24, ghost=(i > 2))
    c.gate(84, 32, 64)
    c.label(70, 24, "first true", anchor="middle")
    # Start the arrow below the cell row so its diagonal does not strike
    # through the "d"/"e" labels on the way to the answer box.
    c.closed_arrow(84, 62, 130, 78, emphasis=False)
    c.cell(132, 66, "answer", w=74, h=24, soft=True)


# ─── Iteration journey ────────────────────────────────────────────────


def iteration_loop_selector(c: Canvas) -> None:
    """Iteration journey · choose the loop shape from the stopping rule."""
    c.cell(0, 40, "stop rule", w=86, h=24)
    choices = [(6, "for", "exhausted", False), (40, "while", "condition", False), (74, "sentinel", "marker", True)]
    for y, loop, rule, chosen in choices:
        c.closed_arrow(86, 52, 128, y + 11, emphasis=chosen)
        c.cell(130, y, loop, w=78, h=22, soft=chosen)
        c.label(218, y + 15, rule)


def iteration_protocol_map(c: Canvas) -> None:
    """Iteration journey · for is surface syntax over iter(), next(), and StopIteration."""
    c.cell(0, 8, "for", w=54, h=22)
    c.dashed(27, 30, 27, 52)
    c.object_box(0, 56, "iterable", "xs", w=70, h=28)
    c.dashed(72, 70, 106, 70)
    c.label(89, 64, "iter()", anchor="middle")
    c.object_box(108, 56, "iterator", "it", w=80, h=28)
    c.closed_arrow(188, 70, 230, 70, emphasis=True)
    c.label(209, 64, "next()", anchor="middle")
    c.cells(232, 58, ["a", "b", "…"], w=24)
    c.dashed(148, 86, 148, 104)
    c.cell(108, 106, "StopIteration", w=94, h=22, ghost=True)


def iteration_lazy_pull(c: Canvas) -> None:
    """Iteration journey · the consumer pulls one value through each lazy stage."""
    c.cell(0, 34, "source", w=68, h=22)
    c.closed_arrow(68, 45, 100, 45, emphasis=False)
    c.cell(102, 34, "filter", w=68, h=22)
    c.closed_arrow(170, 45, 202, 45, emphasis=False)
    c.cell(204, 34, "map", w=58, h=22)
    c.closed_arrow(262, 45, 294, 45, emphasis=False)
    c.cell(296, 34, "value", w=62, h=22, soft=True)
    c.cell(250, 4, "next()", w=68, h=20, soft=True)
    c.closed_arrow(284, 24, 232, 34, emphasis=True)
    c.dashed(136, 64, 136, 78)
    c.cell(86, 80, "no list", w=100, h=22, ghost=True)


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
    c.object_box(148, 32, "", "__init__(name, age, tags)", w=160, h=32)


def class_triangle(c: Canvas) -> None:
    """Classes · instance → class → type — every Python value sits on this triangle."""
    c.type_triangle("type", "type")


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


# ─── Examples promoted from the gestalt: new paint code ──────────────


def number_lines(c: Canvas) -> None:
    """Numbers · int unbounded; float spacing widens at the extremes."""
    c.tag(0, 8, "int · unbounded")
    c.register(0, 22, 260, divisions=8)
    c.tag(0, 50, "float · representable spacing widens")
    c.register(0, 64, 260)
    for x in (10, 30, 60, 100, 130, 140, 148, 160, 188, 230, 260):
        c.tick(x, 64)
    c.dot(140, 64, emphasis=True)


def expression_tree(c: Canvas) -> None:
    """Operators and Literals · expression `(2+3)*4` parsed as a tree."""
    c.node(120, 12, "*", r=12)
    c.node(80, 50, "+", r=12)
    c.node(180, 50, "4", r=10)
    c.node(56, 80, "2", r=10)
    c.node(104, 80, "3", r=10)
    c.connect(120, 12, 12, 80, 50, 12)
    c.connect(120, 12, 12, 180, 50, 10)
    c.connect(80, 50, 12, 56, 80, 10)
    c.connect(80, 50, 12, 104, 80, 10)


def none_singleton(c: Canvas) -> None:
    """None · three names converging on the single None object."""
    for i, n in enumerate("abc"):
        c.name_box(0, i * 28, n)
    for y in (12, 40, 68):
        c.closed_arrow(60, y, 158, 40, emphasis=False)
    c.object_box(160, 24, "NoneType", "None", w=80)


def codepoints_bytes(c: Canvas) -> None:
    """Strings · text is unicode; bytes are a separate encoding layer."""
    c.tag(0, 8, "codepoints")
    for i, ch in enumerate("café"):
        c.cell(i * 40, 16, ch, w=40, h=28)
    c.tag(0, 60, "utf-8 bytes")
    widths = [40, 40, 40, 20, 20]
    bytes_ = ["63", "61", "66", "c3", "a9"]
    x = 0
    for w, b in zip(widths, bytes_):
        c.cell(x, 68, b, w=w, h=14)
        x += w


def sort_stability(c: Canvas) -> None:
    """Sorting · stable sort preserves equal keys' original order."""
    c.tag(0, 4, "input")
    c.tag(180, 4, "stable sort by key")
    inputs = ["2 · Ada", "1 · Bo", "2 · Eve", "1 · Cy"]
    outputs = ["1 · Bo", "1 · Cy", "2 · Ada", "2 · Eve"]
    for i, (a, b) in enumerate(zip(inputs, outputs)):
        c.cell(0, 12 + i * 22, a, w=80, h=20)
        c.cell(180, 12 + i * 22, b, w=80, h=20)
    c.dashed(80, 44, 180, 22)
    c.dashed(80, 88, 180, 44)
    c.dashed(80, 22, 180, 66)
    c.dashed(80, 66, 180, 88)


def kw_only_separator(c: Canvas) -> None:
    """Keyword-only arguments · `*` divides positional from keyword-only."""
    c.mono(0, 18, "def f(a, b, *, c, d): …", anchor="start")
    c.mono_divider(0, 12, 22, 38)  # the '*' sits at index 12
    c.label(33, 50, "positional or kw", anchor="middle")
    c.label(120, 50, "keyword only", anchor="middle")


def positional_only_separator(c: Canvas) -> None:
    """Positional-only parameters · `/` divides positional-only from positional-or-kw."""
    c.mono(0, 18, "def f(a, b, /, c, d): …", anchor="start")
    c.mono_divider(0, 12, 22, 38)  # the '/' sits at index 12
    c.label(33, 50, "positional only", anchor="middle")
    c.label(120, 50, "positional or kw", anchor="middle")


def generator_ribbon(c: Canvas) -> None:
    """Generators · execution paused between yields, resumed by next()."""
    c.tag(0, 8, "paused between yields · resumed by next()")
    c.ribbon(0, 16, 260, h=30, gates=[64, 136, 208], soft_segments=[(0, 64), (136, 208)])
    c.mono(32, 36, "…")
    c.mono(100, 36, "yield")
    c.mono(172, 36, "…")
    c.mono(244, 36, "yield")


def truth_and_size(c: Canvas) -> None:
    """Truth and size · bool(x) checks __bool__, then __len__, else True."""
    c.cell(0, 22, "x", w=40, h=24)
    c.closed_arrow(40, 34, 70, 34, emphasis=True)
    c.cell(72, 0, "__bool__()", w=160, h=22)
    c.cell(72, 22, "__len__() != 0", w=160, h=22, ghost=True)
    c.cell(72, 44, "default: True", w=160, h=22, ghost=True)


def descriptor_protocol(c: Canvas) -> None:
    """Descriptors · attribute access routes to __get__/__set__/__delete__."""
    c.cell(0, 22, "obj.attr", w=80, h=24)
    c.closed_arrow(80, 34, 110, 34, emphasis=True)
    c.frame(112, 0, 110, 70, label="descriptor")
    c.mono(167, 22, "__get__")
    c.mono(167, 38, "__set__")
    c.mono(167, 54, "__delete__")


def bound_unbound(c: Canvas) -> None:
    """Bound vs unbound methods · instance.method binds self; Class.method does not."""
    c.cell(0, 0, "obj.method", w=110, h=22)
    c.closed_arrow(110, 11, 140, 11, emphasis=True)
    c.cell(142, 0, "bound · self filled", w=152, h=22, soft=True)
    c.cell(0, 32, "Class.method", w=110, h=22)
    c.closed_arrow(110, 43, 140, 43, emphasis=False)
    c.cell(142, 32, "function · self required", w=152, h=22)


def method_kinds(c: Canvas) -> None:
    """Method kinds · classmethod, staticmethod, instance — first-arg differs."""
    rows = [
        ("@classmethod", "Cls"),
        ("@staticmethod", "(none)"),
        ("instance", "self"),
    ]
    for i, (decorator, first_arg) in enumerate(rows):
        y = i * 24
        c.cell(0, y, decorator, w=110, h=22)
        c.closed_arrow(110, y + 11, 140, y + 11, emphasis=False)
        c.cell(142, y, f"first arg · {first_arg}", w=130, h=22, soft=True)


def callable_objects(c: Canvas) -> None:
    """Callable objects · `__call__` makes any object look like a function."""
    c.frame(0, 4, 100, 36, label="object")
    c.mono(50, 26, "__call__")
    c.closed_arrow(100, 22, 138, 22, emphasis=True)
    c.cell(140, 10, "obj(...)", w=80, h=24, soft=True)


def attribute_lookup(c: Canvas) -> None:
    """Attribute access · instance dict, then class dict, then __getattr__; first hit wins."""
    c.cell(0, 22, "obj.x", w=70, h=24)
    c.closed_arrow(70, 34, 100, 34, emphasis=True)
    c.cell(102, 0, "instance __dict__", w=140, h=22)
    c.cell(102, 22, "class __dict__", w=140, h=22)
    c.cell(102, 44, "__getattr__", w=140, h=22, ghost=True)


def guard_clauses(c: Canvas) -> None:
    """Guard clauses · early returns first; main work runs only when guards fall through."""
    c.cell(0, 0, "if not valid: return", w=180, h=22, soft=True)
    c.cell(0, 24, "if missing: return None", w=180, h=22, soft=True)
    c.cell(0, 48, "if special_case: return X", w=180, h=22, soft=True)
    c.cell(0, 78, "main work …", w=180, h=22)
    c.closed_arrow(190, 11, 220, 11, emphasis=False)
    c.closed_arrow(190, 35, 220, 35, emphasis=False)
    c.closed_arrow(190, 59, 220, 59, emphasis=False)
    c.label(222, 38, "exit", anchor="start")


def bytes_vs_bytearray(c: Canvas) -> None:
    """Bytes vs bytearray · frozen sequence of integers vs mutable counterpart."""
    c.tag(0, 4, "bytes — frozen")
    c.cell(0, 12, "b'\\\\x63\\\\x61\\\\x66'", w=160, h=24)
    c.tag(0, 50, "bytearray — mutable")
    c.cell(0, 58, "bytearray(b'\\\\x63\\\\x61')", w=180, h=24)
    c.closed_arrow(180, 70, 218, 70, emphasis=True)
    c.label(222, 67, ".append(0x66)", anchor="start")


def sentinel_iteration(c: Canvas) -> None:
    """Sentinel iteration · `iter(callable, sentinel)` calls until the sentinel returns."""
    c.cell(0, 22, "iter(read, '')", w=120, h=24)
    c.closed_arrow(120, 34, 152, 34, emphasis=True)
    c.cell(154, 0, "value", w=70, h=20)
    c.cell(154, 22, "value", w=70, h=20)
    c.cell(154, 44, "value", w=70, h=20)
    c.cell(154, 66, "''", w=70, h=20, ghost=True)
    c.label(228, 80, "sentinel · stop", anchor="start")


def partial_functions(c: Canvas) -> None:
    """Partial functions · `partial(f, 1)` pre-fills arguments, returning a thinner callable."""
    c.cell(0, 12, "f(a, b, c)", w=100, h=24)
    c.closed_arrow(100, 24, 130, 24, emphasis=True)
    c.cell(132, 0, "partial(f, 1)", w=100, h=24)
    c.closed_arrow(232, 24, 262, 24, emphasis=False)
    c.cell(264, 12, "g(b, c)", w=70, h=24, soft=True)


# ─── More example figures (third coverage push) ───────────────────────


def args_kwargs(c: Canvas) -> None:
    """Args and kwargs · *args gathers extra positionals; **kwargs gathers extra keywords."""
    c.mono(20, 22, "def f(*args, **kwargs): …", anchor="start")
    # *args spans signature indices 6-10 (center char 8); **kwargs spans
    # 13-20 (center falls on the 16/17 boundary, index 16.5).
    args_x = c.mono_divider(20, 8, 26, 44)
    kwargs_x = c.mono_divider(20, 16.5, 26, 44)
    c.label(args_x, 56, "→ tuple", anchor="middle")
    c.label(kwargs_x, 56, "→ dict", anchor="middle")


def multiple_return(c: Canvas) -> None:
    """Multiple return values · the function returns a tuple; the caller unpacks it."""
    c.cell(0, 0, "def f(): return a, b", w=180, h=24)
    c.closed_arrow(90, 26, 90, 44, emphasis=True)
    c.cell(58, 44, "(a, b)", w=64, h=22, soft=True)
    c.closed_arrow(90, 68, 90, 86, emphasis=False)
    c.cell(50, 86, "x, y", w=80, h=22)


def lambda_expression(c: Canvas) -> None:
    """Lambdas · a function as a value: parameters on the left, expression on the right."""
    c.cell(0, 0, "lambda x: x + 1", w=170, h=28, soft=True)
    c.dashed(40, 28, 40, 50)
    c.dashed(120, 28, 120, 50)
    c.label(40, 62, "params", anchor="middle")
    c.label(120, 62, "expression", anchor="middle")


def property_fork(c: Canvas) -> None:
    """Properties · obj.x routes through fget/fset instead of touching __dict__."""
    c.cell(0, 22, "obj.x", w=70, h=24)
    c.closed_arrow(70, 22, 110, 4, emphasis=True)
    c.cell(112, 0, "fget / fset", w=120, h=22, soft=True)
    c.closed_arrow(70, 46, 110, 56, emphasis=False)
    c.cell(112, 50, "__dict__", w=120, h=22, ghost=True)


def metaclass_triangle(c: Canvas) -> None:
    """Metaclasses · instance → class → metaclass; the metaclass is the type of the class."""
    c.type_triangle("metaclass", "type", third_w=80)


def sys_path_resolution(c: Canvas) -> None:
    """Modules · imports walk sys.path; the first hit wins."""
    c.tag(0, 4, "sys.path")
    paths = ["cwd", "site-packages", "stdlib", "…"]
    for i, p in enumerate(paths):
        c.cell(0, 14 + i * 20, p, w=120, h=20)
    c.closed_arrow(120, 46, 156, 46, emphasis=True)
    c.label(145, 30, "first hit", anchor="middle")
    c.cell(158, 34, "mymod.py", w=100, h=24, soft=True)


def import_alias(c: Canvas) -> None:
    """Import aliases · `import x as y` makes y point at the same module object as x."""
    c.mono(0, 8, "import numpy as np", anchor="start")
    c.cell(0, 24, "np", w=40, h=22)
    c.closed_arrow(40, 35, 80, 35, emphasis=True)
    c.cell(82, 24, "numpy module", w=130, h=22, soft=True)


def protocol_check(c: Canvas) -> None:
    """Protocols · structural check; an object satisfies a protocol if it has the required methods."""
    c.frame(0, 4, 100, 70, label="object")
    c.mono(50, 20, "read()")
    c.mono(50, 36, "write()")
    c.mono(50, 52, "close()")
    c.closed_arrow(100, 38, 138, 38, emphasis=True)
    c.label(119, 0, "structural", anchor="middle")
    c.frame(140, 4, 80, 70, label="protocol", ghost=True)
    c.mono(180, 28, "read()")
    c.mono(180, 46, "close()")


def enum_members(c: Canvas) -> None:
    """Enums · a fixed set of named symbolic values; no new members appear at runtime."""
    c.frame(0, 0, 280, 60, label="Color · closed set", ghost=True)
    members = ["RED", "GREEN", "BLUE", "no more"]
    for i, m in enumerate(members):
        c.cell(20 + i * 60, 16, m, w=50, h=28)


def datetime_instant(c: Canvas) -> None:
    """Datetime · one instant; the offset names which clock face you're reading."""
    c.register(10, 40, 260, divisions=8)
    c.dashed(150, 30, 150, 50)
    c.label(150, 24, "one instant", anchor="middle")
    c.node(90, 70, "−5h", r=12)
    c.dashed(90, 58, 150, 50)
    c.node(210, 70, "+0h", r=12)
    c.dashed(210, 58, 150, 50)


def json_python_mapping(c: Canvas) -> None:
    """JSON ↔ Python · six type pairs map across the text boundary."""
    c.hairline(120, 0, 120, 110)
    c.tag(60, 4, "json", anchor="middle")
    c.tag(180, 4, "python", anchor="middle")
    rows = [
        ("object", "dict"),
        ("array", "list"),
        ("string", "str"),
        ("number", "int / float"),
        ("true / false", "True / False"),
        ("null", "None"),
    ]
    for i, (a, b) in enumerate(rows):
        y = 24 + i * 14
        c.mono(0, y, a, anchor="start", size=10)
        c.mono(132, y, b, anchor="start", size=10)


def regex_anchors(c: Canvas) -> None:
    """Regular expressions · anchors and quantifiers shape what the pattern matches."""
    c.tag(0, 4, "pattern")
    c.mono(0, 24, "^\\d{2}-\\d{2}$", anchor="start")
    c.tag(0, 56, "input")
    c.cell(0, 64, "", w=200, h=20)
    c.cell(40, 64, "12-34", w=120, h=20, soft=True)


def number_parse(c: Canvas) -> None:
    """Number parsing · text → typed number, raising on bad input."""
    c.cell(0, 22, '"42"', w=70, h=24)
    c.closed_arrow(70, 34, 102, 34, emphasis=True)
    c.label(86, 26, "int()", anchor="middle")
    c.cell(104, 10, "42", w=60, h=22, soft=True)
    c.cell(104, 36, "ValueError", w=100, h=22, ghost=True)


def format_spec(c: Canvas) -> None:
    """String formatting · the format spec is a railroad of named optional fields."""
    c.tag(0, 4, "format spec")
    stations = [("align", 36), ("sign", 30), ("width", 40), (",", 22), (".prec", 44), ("type", 32)]
    x = 0
    for label_text, w in stations:
        c.cell(x, 16, label_text, w=w, h=18)
        x += w + 2
    c.label(0, 54, "{:>6,.2f}")


def truthy_check(c: Canvas) -> None:
    """Truthiness · bool(x) is True except for a small fixed set of falsy values."""
    c.cell(0, 0, "x", w=40, h=24)
    c.closed_arrow(40, 12, 70, 12, emphasis=True)
    c.label(55, 6, "bool", anchor="middle")
    c.cell(72, 0, "True or False", w=130, h=24)
    c.tag(0, 38, "falsy values")
    falsy = [("0", 22), ("0.0", 30), ('""', 26), ("[]", 22), ("{}", 22), ("None", 40), ("False", 40)]
    x = 0
    for label_text, w in falsy:
        c.cell(x, 46, label_text, w=w, h=20)
        x += w + 2


def boolean_truth_table(c: Canvas) -> None:
    """Booleans · `a and b` is True only when both are True; otherwise False."""
    c.tag(64, 0, "a and b", anchor="middle")
    c.label(80, 16, "T", anchor="middle")
    c.label(112, 16, "F", anchor="middle")
    c.label(58, 36, "T", anchor="end")
    c.label(58, 56, "F", anchor="end")
    c.cell(64, 22, "T", w=32, h=20, soft=True)
    c.cell(96, 22, "F", w=32, h=20)
    c.cell(64, 42, "F", w=32, h=20)
    c.cell(96, 42, "F", w=32, h=20)


def set_buckets(c: Canvas) -> None:
    """Sets · hash buckets with no values; membership is O(1)."""
    c.tag(0, 4, "keys only")
    for i, k in enumerate("abc"):
        c.cell(0, 14 + i * 22, k, w=50, h=20)
    c.closed_arrow(50, 36, 90, 36, emphasis=True)
    c.label(70, 28, "x in s", anchor="middle")
    c.cell(92, 24, "O(1)", w=60, h=22, soft=True)


def tuple_frozen(c: Canvas) -> None:
    """Tuples · ordered, immutable sequence; .append doesn't exist."""
    c.tag(0, 0, "frozen sequence")
    c.cell(0, 12, "(3, 1, 4, 1)", w=180, h=26)
    c.dashed(45, 8, 45, 42)
    c.dashed(90, 8, 90, 42)
    c.dashed(135, 8, 135, 42)
    c.cell(190, 12, ".append", w=80, h=26, ghost=True)
    c.dashed(190, 24, 270, 24)


def value_types(c: Canvas) -> None:
    """Values · every literal is a typed object: int, str, list, dict each carry their behaviour."""
    rows = [("int", "42"), ("str", '"hi"'), ("list", "[1,2,3]"), ("dict", "{k:v}")]
    for i, (t, v) in enumerate(rows):
        y = i * 30
        c.object_box(0, y, t, v, w=160, h=26, tag_position="inside")


def literal_forms(c: Canvas) -> None:
    """Literals · each type has its own literal spellings; the source spelling determines the value type."""
    rows = [
        ("int", "42  ·  0x2a  ·  0b101"),
        ("float", "3.14  ·  1e-3"),
        ("str", '"hi"  ·  \'hi\''),
        ("list", "[1, 2, 3]"),
        ("dict", "{k: v}"),
        ("set", "{1, 2, 3}"),
    ]
    for i, (t, spellings) in enumerate(rows):
        y = i * 22
        c.cell(0, y, t, w=50, h=20, soft=True)
        c.cell(52, y, spellings, w=200, h=20)


def function_with_body(c: Canvas) -> None:
    """Functions · `def greet(name): return "Hello, " + name` takes input, computes, returns output."""
    c.closed_arrow(0, 36, 30, 36, emphasis=False)
    c.label(15, 28, "name", anchor="middle")
    c.frame(32, 18, 150, 44, label="def greet(name):")
    c.mono(107, 44, '"Hello, " + name')
    c.closed_arrow(182, 36, 212, 36, emphasis=True)
    c.cell(214, 24, '"Hello, Ada"', w=120, h=24, soft=True)


def yield_delegation(c: Canvas) -> None:
    """Yield from · delegate iteration to an inner generator; its yields surface here."""
    c.tag(0, 4, "outer")
    c.ribbon(0, 14, 240, h=20, gates=[100, 180])
    c.mono(140, 28, "yield from inner")
    c.tag(100, 46, "inner")
    c.ribbon(100, 56, 80, h=24, gates=[124, 152])
    c.dashed(140, 56, 140, 34)


def itertools_chain(c: Canvas) -> None:
    """Itertools · chain joins two iterables into one stream without materialising either."""
    c.object_box(0, 14, "iter A", "1 · 2", w=70, h=24)
    c.object_box(0, 52, "iter B", "3 · 4", w=70, h=24)
    c.closed_arrow(70, 26, 100, 36, emphasis=False)
    c.closed_arrow(70, 64, 100, 54, emphasis=False)
    c.object_box(102, 30, "chain", "1 · 2 · 3 · 4", w=140, h=28)


def assertion_check(c: Canvas) -> None:
    """Assertions · assert tests a condition; True passes, False raises AssertionError."""
    c.cell(0, 22, "assert cond", w=110, h=24)
    c.closed_arrow(110, 22, 140, 0, emphasis=True)
    c.cell(142, 0, "True · pass", w=120, h=20, soft=True)
    c.closed_arrow(110, 46, 140, 56, emphasis=False)
    c.cell(142, 50, "False · AssertionError", w=160, h=20)


def custom_exception_chain(c: Canvas) -> None:
    """Custom exceptions · subclass an existing exception; gain a domain name without changing semantics."""
    chain = ["BaseException", "Exception", "ValueError", "MyDomainError"]
    for i, name in enumerate(chain):
        emph = i == len(chain) - 1
        c.cell(0, i * 24, name, w=220, h=22, soft=emph)


def exception_group_peel(c: Canvas) -> None:
    """Exception groups · except* peels matching leaves; survivors regroup."""
    c.tag(0, 0, "before")
    c.dot(40, 14)
    for x in (20, 36, 52, 68):
        c.ghost(40, 14, x, 44)
    c.dot(20, 44)
    c.dot(36, 44)
    c.dot(52, 44)
    c.dot(68, 44)
    c.closed_arrow(90, 30, 140, 30, emphasis=True)
    c.label(115, 22, "except*", anchor="middle")
    c.tag(160, 0, "after")
    c.dot(200, 14)
    c.ghost(200, 14, 180, 44)
    c.ghost(200, 14, 220, 44)
    c.dot(180, 44)
    c.dot(220, 44)


def delete_name_erased(c: Canvas) -> None:
    """Delete statements · `del x` removes the name; the object survives if any other name holds it."""
    c.tag(0, 0, "before")
    c.name_box(0, 12, "x")
    c.closed_arrow(60, 23, 100, 23, emphasis=False)
    c.cell(102, 12, "[1, 2, 3]", w=90, h=22, soft=True)
    c.tag(0, 52, "after del x")
    c.name_box(0, 60, "x")
    c.dashed(0, 70, 60, 70)
    c.dashed(60, 60, 0, 80)
    c.cell(102, 60, "[1, 2, 3]", w=90, h=22, soft=True)


# ─── Fourth coverage push: constraint-shaped examples ─────────────────


def package_tree(c: Canvas) -> None:
    """Packages · a directory with __init__.py becomes an importable package; submodules nest."""
    c.frame(70, 0, 100, 22, label="mypackage")
    c.mono(120, 14, "__init__.py")
    c.stroke(120, 22, 40, 50)
    c.stroke(120, 22, 120, 50)
    c.stroke(120, 22, 200, 50)
    c.cell(10, 50, "a.py", w=60, h=22)
    c.cell(90, 50, "b.py", w=60, h=22)
    c.cell(170, 50, "sub/", w=60, h=22, soft=True)


def venv_boundary(c: Canvas) -> None:
    """Virtual environments · a venv isolates a project's interpreter and packages from the system."""
    c.frame(0, 0, 110, 70, label="project")
    c.cell(12, 18, "code", w=84, h=20)
    c.cell(12, 42, "requirements", w=84, h=20)
    c.closed_arrow(110, 35, 142, 35, emphasis=True)
    c.frame(144, 0, 130, 70, label="venv")
    c.mono(209, 22, "python")
    c.mono(209, 42, "site-packages")


def subprocess_spawn(c: Canvas) -> None:
    """Subprocesses · spawn a child process; capture stdout, stderr, and exit code as portable evidence."""
    c.cell(0, 22, "parent", w=70, h=24)
    c.closed_arrow(70, 34, 110, 34, emphasis=True)
    c.label(90, 26, "spawn", anchor="middle")
    c.cell(112, 22, "child process", w=110, h=24, soft=True)
    c.closed_arrow(222, 34, 252, 34, emphasis=False)
    c.cell(254, 22, "output", w=70, h=24)


def logging_levels(c: Canvas) -> None:
    """Logging · five levels; messages below the configured threshold are dropped."""
    levels = [("CRITICAL", "50"), ("ERROR", "40"), ("WARNING", "30"), ("INFO", "20"), ("DEBUG", "10")]
    for i, (name, num) in enumerate(levels):
        c.cell(0, i * 22, name, w=120, h=20)
        c.cell(122, i * 22, num, w=40, h=20, soft=True)


def aaa_pattern(c: Canvas) -> None:
    """Testing · arrange-act-assert: set up, run the behavior, compare the result."""
    rows = [("arrange", "set up state"), ("act", "perform behavior"), ("assert", "compare result")]
    for i, (label_text, body) in enumerate(rows):
        c.cell(0, i * 24, label_text, w=80, h=22, soft=(i == 2))
        c.closed_arrow(80, i * 24 + 11, 108, i * 24 + 11, emphasis=False)
        c.cell(110, i * 24, body, w=140, h=22)


def socket_byte_boundary(c: Canvas) -> None:
    """Networking · sockets carry bytes; encode marks the python → wire boundary, decode the wire → python boundary."""
    c.object_box(0, 18, "str", '"ping"', w=64, h=22)
    c.closed_arrow(64, 29, 96, 29, emphasis=False)
    c.label(80, 23, "encode", anchor="middle")
    c.object_box(98, 18, "bytes", "b'ping'", w=70, h=22, soft=True)
    c.dashed(168, 29, 192, 29)
    c.tag(180, 8, "socket", anchor="middle")
    c.object_box(194, 18, "bytes", "b'ping'", w=70, h=22, soft=True)
    c.closed_arrow(264, 29, 296, 29, emphasis=False)
    c.label(280, 23, "decode", anchor="middle")
    c.object_box(298, 18, "str", '"ping"', w=64, h=22)


def gil_lanes(c: Canvas) -> None:
    """Threads and processes · threads share one interpreter lane; processes isolate interpreters."""
    c.tag(0, 0, "threads: shared interpreter")
    c.lane(26, x0=84, x1=292, label="GIL")
    c.lane(50, x0=84, x1=292, label="thread A")
    c.lane(74, x0=84, x1=292, label="thread B")
    for x, y in [(94, 44), (142, 68), (190, 44), (238, 68)]:
        c.cell(x, y, "", w=26, h=10)
    c.tag(0, 98, "processes: isolated")
    c.cell(84, 110, "proc A", w=76, h=20)
    c.cell(184, 110, "proc B", w=76, h=20)
    c.dashed(172, 104, 172, 134)


def cast_escape(c: Canvas) -> None:
    """Casts and any · cast(T, x) tells the type checker to treat x as T; runtime is unaffected."""
    c.cell(0, 22, "Any", w=70, h=24, ghost=True)
    c.closed_arrow(70, 34, 110, 34, emphasis=True)
    c.label(90, 12, "cast(T, x)", anchor="middle")
    c.cell(112, 22, "T", w=70, h=24, soft=True)


def newtype_phantom(c: Canvas) -> None:
    """NewType · two static identities backed by the same runtime type."""
    c.tag(0, 0, "runtime: int")
    c.cell(0, 12, "42", w=60, h=24)
    c.tag(0, 50, "static: UserId")
    c.cell(0, 62, "UserId(42)", w=90, h=24, soft=True)


def overload_signatures(c: Canvas) -> None:
    """Overloads · static call signatures narrow to one runtime implementation."""
    c.tag(0, 0, "static signatures")
    c.cell(0, 12, "double(int) -> int", w=150, h=20)
    c.cell(0, 36, "double(str) -> str", w=150, h=20)
    c.closed_arrow(150, 32, 190, 32, emphasis=True)
    c.tag(198, 0, "runtime")
    c.cell(192, 22, "one double() body", w=112, h=22, soft=True)


def paramspec_preserve(c: Canvas) -> None:
    """ParamSpec · the decorator preserves the wrapped function's full signature, parameter for parameter."""
    c.cell(0, 22, "f(P)", w=50, h=24)
    c.closed_arrow(50, 34, 80, 34, emphasis=False)
    c.frame(82, 12, 100, 44, label="@dec")
    c.mono(132, 36, "P preserved")
    c.closed_arrow(182, 34, 212, 34, emphasis=True)
    c.cell(214, 22, "wrapper(P)", w=80, h=24, soft=True)


def literal_constrained(c: Canvas) -> None:
    """Literal · the type narrows the slot to a fixed set of constant values."""
    c.tag(0, 0, "Literal[…]")
    c.cell(0, 12, "x", w=40, h=24)
    c.closed_arrow(40, 24, 70, 4, emphasis=False)
    c.closed_arrow(40, 24, 70, 24, emphasis=False)
    c.closed_arrow(40, 24, 70, 44, emphasis=False)
    c.cell(72, 0, "'red'", w=70, h=20, soft=True)
    c.cell(72, 22, "'green'", w=70, h=20, soft=True)
    c.cell(72, 44, "'blue'", w=70, h=20, soft=True)


def callable_type(c: Canvas) -> None:
    """Callable types · a callback slot requires a specific argument list and return type."""
    c.tag(0, 0, "callback slot")
    c.cell(0, 12, "Callable[[int, str], bool]", w=170, h=22)
    c.closed_arrow(170, 23, 202, 23, emphasis=True)
    c.cell(204, 2, "int,str", w=58, h=34)
    c.closed_arrow(262, 19, 290, 19, emphasis=False)
    c.cell(292, 2, "bool", w=58, h=34, soft=True)


def isinstance_check(c: Canvas) -> None:
    """Runtime type checks · isinstance asks the runtime; the answer is a bool, not a refinement."""
    c.cell(0, 22, "isinstance(x, T)", w=140, h=24)
    c.closed_arrow(140, 22, 170, 4, emphasis=True)
    c.cell(172, 0, "True", w=60, h=20, soft=True)
    c.closed_arrow(140, 46, 170, 56, emphasis=False)
    c.cell(172, 50, "False", w=60, h=20)


def collections_containers(c: Canvas) -> None:
    """Collections module · four specialised containers for shapes the built-in types don't cover well."""
    rows = [("deque", "fast appends both ends"), ("Counter", "key → count"), ("defaultdict", "missing key default"), ("namedtuple", "tuple with names")]
    for i, (name, role) in enumerate(rows):
        c.cell(0, i * 22, name, w=110, h=20)
        c.cell(112, i * 22, role, w=170, h=20, soft=True)


def typed_dict_shape(c: Canvas) -> None:
    """Structured data shapes · TypedDict names each key's value type; the dict obeys the declared shape."""
    c.frame(0, 0, 200, 86, label="User TypedDict")
    rows = [("id", "int"), ("name", "str"), ("active", "bool")]
    for i, (k, v) in enumerate(rows):
        c.cell(14, 18 + i * 20, f"{k}: {v}", w=172, h=18)


def csv_records(c: Canvas) -> None:
    """CSV data · rows of records; each line has the same columns in the same order."""
    c.tag(0, 0, "rows · records")
    headers = ["id", "name", "score"]
    rows = [["1", "Ada", "97"], ["2", "Bo", "88"], ["3", "Cy", "76"]]
    for j, h in enumerate(headers):
        c.cell(j * 70, 12, h, w=70, h=20, soft=True)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            c.cell(j * 70, 32 + i * 20, v, w=70, h=18)


def warning_signal(c: Canvas) -> None:
    """Warnings · a soft signal: the warning is reported, execution continues."""
    c.cell(0, 22, "code path", w=90, h=24)
    c.closed_arrow(90, 22, 120, 4, emphasis=False)
    c.cell(122, 0, "DeprecationWarning", w=170, h=22, soft=True)
    c.closed_arrow(90, 46, 120, 56, emphasis=True)
    c.cell(122, 50, "execution continues", w=170, h=22)


def object_lifecycle(c: Canvas) -> None:
    """Object lifecycle · names keep an object reachable until the last reference disappears."""
    c.name_box(0, 14, "box")
    c.name_box(0, 48, "alias")
    c.closed_arrow(54, 26, 118, 44, emphasis=False)
    c.closed_arrow(54, 60, 118, 44, emphasis=False)
    c.object_box(120, 28, "Box", "label='draft'", w=112, h=32, soft=True)
    c.closed_arrow(232, 44, 276, 44, emphasis=True)
    c.cell(278, 32, "last ref?", w=88, h=34)


# ─── Fifth pass: tightened figures for slugs that were on reuse-floors ─


def type_alias_name(c: Canvas) -> None:
    """Type aliases · complex annotation collapses to a single readable name."""
    c.cell(0, 30, "dict[str, list[tuple[int, str]]]", w=240, h=24, ghost=True)
    c.closed_arrow(120, 54, 120, 70, emphasis=True)
    c.label(96, 66, "type Index = …", anchor="middle")
    c.cell(80, 76, "Index", w=80, h=24, soft=True)


def match_dispatch_ladder(c: Canvas) -> None:
    """Match statements · the value flows down the patterns; the first match wins."""
    c.cell(0, 0, "match value", w=170, h=22)
    cases = ["case 0:", "case [x, y]:", "case Point(0, _):", "case _:"]
    for i, txt in enumerate(cases):
        c.cell(0, 30 + i * 22, txt, w=170, h=20)
    c.dashed(186, 32, 186, 122)
    c.dot(186, 74)
    c.closed_arrow(186, 110, 186, 124, emphasis=True)
    c.label(196, 76, "first match", anchor="start")


def match_pattern_variants(c: Canvas) -> None:
    """Advanced match patterns · capture, alternative, guard, class — four pattern shapes."""
    rows = [("capture", "[x, y]"), ("alternative", "P() | Q()"), ("guard", "[x] if x > 0"), ("class", "Point(x=0, y=_)")]
    for i, (kind, shape) in enumerate(rows):
        y = i * 22
        c.cell(0, y, kind, w=90, h=20)
        c.cell(92, y, shape, w=180, h=20, soft=(kind == "class"))


def loop_else_gate(c: Canvas) -> None:
    """Loop else · runs when the loop falls through naturally; break skips it."""
    c.cell(0, 20, "loop body", w=110, h=24)
    c.closed_arrow(110, 20, 150, 0, emphasis=True)
    c.cell(152, 0, "fell through · else runs", w=160, h=20, soft=True)
    c.closed_arrow(110, 44, 150, 56, emphasis=False)
    c.cell(152, 50, "broke · else skipped", w=160, h=20)


def lazy_stream(c: Canvas) -> None:
    """Iteration · Compose lazy value streams: filter and map flow values without materialising."""
    c.object_box(0, 26, "source", "[a,b,c]", w=78, h=24)
    c.dashed(78, 38, 102, 38)
    c.object_box(104, 26, "filter", "x>0", w=68, h=24)
    c.dashed(172, 38, 196, 38)
    c.object_box(198, 26, "map", "x*2", w=64, h=24)
    c.closed_arrow(262, 38, 294, 38, emphasis=True)
    c.label(278, 30, "next()", anchor="middle")




def container_methods(c: Canvas) -> None:
    """Container protocols · syntax routes to __setitem__, __contains__, and __getitem__."""
    rows = [("scores[k] = v", "__setitem__"), ("k in scores", "__contains__"), ("scores[k]", "__getitem__")]
    for i, (syntax, method) in enumerate(rows):
        y = i * 28
        c.cell(0, y, syntax, w=120, h=22)
        c.closed_arrow(120, y + 11, 158, y + 11, emphasis=(i == 1))
        c.cell(160, y, method, w=110, h=22, soft=(i == 1))


def structured_shapes(c: Canvas) -> None:
    """Structured data shapes · same record, three runtime trade-offs."""
    rows = [("dataclass", "mutable attrs"), ("NamedTuple", "tuple + names"), ("TypedDict", "dict at runtime")]
    for i, (shape, tradeoff) in enumerate(rows):
        y = i * 28
        c.cell(0, y, shape, w=100, h=22)
        c.closed_arrow(100, y + 11, 132, y + 11, emphasis=(i == 2))
        c.cell(134, y, tradeoff, w=130, h=22, soft=(i == 2))

# Registry: figure_name -> (paint_fn, viewbox_w, viewbox_h)
FIGURES: dict[str, tuple[Callable[[Canvas], None], int, int]] = {
    "aliasing-mutation": (aliasing_mutation, 220, 175),
    "tuple-no-mutation": (tuple_no_mutation, 220, 185),
    "iterator-unroll": (iterator_unroll, 220, 130),
    "scope-rings": (scope_rings, 216, 116),
    "closure-cell": (closure_cell, 240, 120),
    "slice-ruler": (slice_ruler, 232, 120),
    "branch-fork": (branch_fork, 232, 100),
    "loop-repetition": (loop_repetition, 260, 100),
    "while-backedge": (while_backedge, 252, 80),
    "iter-protocol": (iter_protocol, 304, 70),
    # Runtime
    "program-output": (program_output, 240, 80),
    "identity-and-equality": (identity_and_equality, 304, 96),
    "operator-dispatch": (operator_dispatch, 260, 70),
    "runtime-evidence-loop": (runtime_evidence_loop, 306, 96),
    "runtime-object-axes": (runtime_object_axes, 214, 104),
    "runtime-expression-model": (runtime_expression_model, 344, 96),
    # Shapes
    "container-questions": (container_questions, 280, 88),
    "reshape-pipeline": (reshape_pipeline, 204, 80),
    "text-data-boundary": (text_data_boundary, 172, 70),
    # Interfaces
    "function-signature": (function_signature, 310, 82),
    "function-as-value": (function_as_value, 200, 66),
    "class-with-state": (class_with_state, 152, 108),
    # Types
    "annotation-ghost": (annotation_ghost, 220, 52),
    "union-types": (union_types, 166, 80),
    "generic-preservation": (generic_preservation, 250, 70),
    "type-runtime-static-split": (type_runtime_static_split, 224, 126),
    "type-shape-catalog": (type_shape_catalog, 290, 108),
    "type-library-contract": (type_library_contract, 364, 104),
    # Reliability
    "exception-lanes": (exception_lanes, 320, 100),
    "context-bowtie": (context_bowtie, 244, 76),
    "async-swimlane": (async_swimlane, 280, 84),
    "reliability-signal-map": (reliability_signal_map, 270, 128),
    "reliability-boundary-map": (reliability_boundary_map, 286, 110),
    "reliability-operation-boundary": (reliability_operation_boundary, 354, 104),
    # Control flow + Iteration coverage gap (see audit)
    "naming-decisions": (naming_decisions, 310, 98),
    "early-exit": (early_exit, 144, 116),
    "lazy-stream": (lazy_stream, 300, 56),
    "control-decision-map": (control_decision_map, 244, 104),
    "control-fact-shape": (control_fact_shape, 286, 104),
    "control-stop-boundary": (control_stop_boundary, 210, 104),
    "iteration-loop-selector": (iteration_loop_selector, 276, 104),
    "iteration-protocol-map": (iteration_protocol_map, 306, 132),
    "iteration-lazy-pull": (iteration_lazy_pull, 360, 112),
    # Promoted from the gestalt — wired to example pages via ATTACHMENTS
    "variables-bind": (variables_bind, 180, 44),
    "call-stack": (call_stack, 200, 100),
    "decorator-rebind": (decorator_rebind, 232, 110),
    "mro-chain": (mro_chain, 200, 152),
    "dataclass-fields": (dataclass_fields, 312, 76),
    "class-triangle": (class_triangle, 274, 60),
    "exception-cause-context": (exception_cause_context, 282, 70),
    "unpacking-bind": (unpacking_bind, 152, 80),
    "comprehension-equivalence": (comprehension_equivalence, 280, 76),
    "list-append": (list_append, 220, 36),
    "dict-buckets": (dict_buckets, 270, 88),
    # Newly designed paint code for examples that lacked a figure
    "number-lines": (number_lines, 260, 78),
    "expression-tree": (expression_tree, 220, 92),
    "none-singleton": (none_singleton, 240, 84),
    "codepoints-bytes": (codepoints_bytes, 200, 84),
    "sort-stability": (sort_stability, 270, 100),
    "kw-only-separator": (kw_only_separator, 200, 56),
    "positional-only-separator": (positional_only_separator, 200, 56),
    "generator-ribbon": (generator_ribbon, 260, 50),
    "truth-and-size": (truth_and_size, 232, 70),
    "descriptor-protocol": (descriptor_protocol, 222, 76),
    "bound-unbound": (bound_unbound, 296, 56),
    "method-kinds": (method_kinds, 272, 70),
    "callable-objects": (callable_objects, 220, 44),
    "attribute-lookup": (attribute_lookup, 242, 70),
    "guard-clauses": (guard_clauses, 264, 104),
    "bytes-vs-bytearray": (bytes_vs_bytearray, 308, 86),
    "sentinel-iteration": (sentinel_iteration, 320, 92),
    "partial-functions": (partial_functions, 334, 36),
    # Third coverage push: 24 more figures
    "args-kwargs": (args_kwargs, 280, 68),
    "multiple-return": (multiple_return, 180, 110),
    "lambda-expression": (lambda_expression, 170, 76),
    "property-fork": (property_fork, 232, 72),
    "metaclass-triangle": (metaclass_triangle, 300, 60),
    "sys-path-resolution": (sys_path_resolution, 258, 100),
    "import-alias": (import_alias, 212, 56),
    "protocol-check": (protocol_check, 220, 78),
    "enum-members": (enum_members, 280, 60),
    "datetime-instant": (datetime_instant, 280, 88),
    "json-python-mapping": (json_python_mapping, 220, 116),
    "regex-anchors": (regex_anchors, 200, 92),
    "number-parse": (number_parse, 204, 64),
    "format-spec": (format_spec, 220, 64),
    "truthy-check": (truthy_check, 240, 70),
    "boolean-truth-table": (boolean_truth_table, 132, 64),
    "set-buckets": (set_buckets, 156, 90),
    "tuple-frozen": (tuple_frozen, 280, 48),
    "value-types": (value_types, 160, 116),
    "yield-delegation": (yield_delegation, 240, 84),
    "itertools-chain": (itertools_chain, 246, 82),
    "assertion-check": (assertion_check, 304, 76),
    "custom-exception-chain": (custom_exception_chain, 220, 90),
    "exception-group-peel": (exception_group_peel, 240, 50),
    "delete-name-erased": (delete_name_erased, 200, 84),
    # Fourth coverage push: 19 figures for constraint-shaped examples
    "package-tree": (package_tree, 240, 76),
    "venv-boundary": (venv_boundary, 274, 76),
    "subprocess-spawn": (subprocess_spawn, 324, 60),
    "logging-levels": (logging_levels, 164, 124),
    "aaa-pattern": (aaa_pattern, 250, 80),
    "socket-byte-boundary": (socket_byte_boundary, 364, 46),
    "gil-lanes": (gil_lanes, 300, 138),
    "cast-escape": (cast_escape, 184, 56),
    "newtype-phantom": (newtype_phantom, 96, 92),
    "overload-signatures": (overload_signatures, 304, 64),
    "paramspec-preserve": (paramspec_preserve, 294, 60),
    "literal-constrained": (literal_constrained, 144, 76),
    "callable-type": (callable_type, 352, 42),
    "isinstance-check": (isinstance_check, 232, 76),
    "collections-containers": (collections_containers, 284, 92),
    "container-methods": (container_methods, 272, 82),
    "typed-dict-shape": (typed_dict_shape, 200, 92),
    "structured-shapes": (structured_shapes, 266, 82),
    "csv-records": (csv_records, 212, 96),
    "warning-signal": (warning_signal, 292, 80),
    "object-lifecycle": (object_lifecycle, 366, 80),
    # Fifth pass: slug-specific figures lifting attached scores off the 8.0 floor
    "type-alias-name": (type_alias_name, 240, 104),
    "match-dispatch-ladder": (match_dispatch_ladder, 260, 130),
    "match-pattern-variants": (match_pattern_variants, 272, 96),
    "loop-else-gate": (loop_else_gate, 312, 76),
    # Sixth pass: lift the lingering 8.0-band figures with slug-specific paint
    "literal-forms": (literal_forms, 252, 132),
    "function-with-body": (function_with_body, 334, 68),
}


# ─── Attachments ───────────────────────────────────────────────────────

# Loaded from docs/quality-registries.toml: slug -> [(anchor, figure_name, caption_or_None), …]
ATTACHMENTS: dict[str, list[tuple[str, str, str | None]]] = load_figure_attachments()


# ─── Render helpers ────────────────────────────────────────────────────


def _render_svg(figure_name: str) -> str:
    paint, w, h = FIGURES[figure_name]
    canvas = Canvas(w=w, h=h)
    paint(canvas)
    return canvas.to_svg()


def render_first_figure(slug: str) -> str:
    """SVG for the example's first attached figure. Empty if none.

    Used by scripts/build_social_cards.py to reuse the curated figure
    set for social-card images.
    """
    for _anchor, name, _caption in ATTACHMENTS.get(slug, []):
        return _render_svg(name)
    return ""


def _normalize_position(anchor: str) -> str:
    """Map an attachment anchor to a banner position.

    The position grammar (docs/visual-explainer-spec.md) is `before`,
    `after-cell-N`, and `after-walkthrough`. The legacy anchor `cell-N`
    means the banner after cell N, so both spellings resolve to the
    same position.
    """
    if anchor.startswith("cell-"):
        return f"after-{anchor}"
    return anchor


def render_banner(slug: str, position: str) -> str:
    """HTML for the banner row at a position. Empty if nothing attaches.

    Cells always keep their prose|code 2-column grid. Figures live in
    banner rows that span both columns: before the first cell, between
    cells, or after the walkthrough. Multiple figures attached to the
    same position share one banner as a small multiple.
    """
    attachments = ATTACHMENTS.get(slug, [])
    matched = [
        (name, caption)
        for (anchor, name, caption) in attachments
        if _normalize_position(anchor) == position
    ]
    if not matched:
        return ""
    figures: list[str] = []
    for name, caption in matched:
        cap = f"<figcaption>{render_inline(caption)}</figcaption>" if caption else ""
        figures.append(f"<figure>{_render_svg(name)}{cap}</figure>")
    count_class = f" cell-banner--{len(matched)}"
    return f'<div class="cell-banner{count_class}">{"".join(figures)}</div>'


def render_for_anchor(slug: str, anchor: str) -> str:
    """Anchor-spelling compatibility wrapper around render_banner."""
    return render_banner(slug, _normalize_position(anchor))


# ─── Journey-section figures ──────────────────────────────────────────
# One figure per journey section, keyed by section title. The figure
# depicts the conceptual shift the section's examples share — the
# journey-section rubric (docs/journey-visualisation-rubric.md) scores
# these. Rendered inline on /journeys/<slug> between the section
# heading and the example list. Reviewed all together on
# /prototyping/journey-figures-gestalt.

SECTION_FIGURES: dict[str, tuple[str, str]] = load_journey_section_figures()


def render_for_section(section_title: str) -> str:
    """HTML for a section figure on a journey page. Empty if no
    figure is registered for this section title.
    """
    entry = SECTION_FIGURES.get(section_title)
    if not entry:
        return ""
    name, caption = entry
    cap = f"<figcaption>{render_inline(caption)}</figcaption>" if caption else ""
    return f'<figure class="journey-section-figure">{_render_svg(name)}{cap}</figure>'


# ─── Section-figure scores ────────────────────────────────────────────
# Score every journey-section figure against
# docs/journey-visualisation-rubric.md (10-point scale).
# Keyed by section title to match SECTION_FIGURES.
SECTION_FIGURE_SCORES: dict[str, tuple[float, str]] = load_journey_section_figure_scores()


# ─── Scores (v2 rubric — see docs/example-figure-rubric.md) ────────────
# Score every attached example figure against the v2 rubric. The dict is
# loaded from the TOML source of truth used by both the gestalt review pages
# (scripts/build_marginalia.py, scripts/build_prototypes.py) and any
# future per-example scoring surface.

SCORES: dict[str, tuple[float, str]] = load_example_figure_scores()


def figure_score(slug: str) -> tuple[float, str] | None:
    """Return the v2 score and rationale for an attached example slug, if any."""
    return SCORES.get(slug)


# ─── Example quality scores ──────────────────────────────────────────
# Score every example PAGE against docs/example-quality-rubric.md.
# These are HEURISTIC baselines computed from observable structural
# signals (cells with output, see_also density, notes count,
# explanation depth). Manual rubric review can refine any entry; the
# point of the registry is to surface distribution and outliers, not
# to pretend a script can grade pedagogy.

EXAMPLE_QUALITY_SCORES: dict[str, tuple[float, str]] = load_example_quality_scores()
