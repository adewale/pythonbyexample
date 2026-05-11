import ast
import contextlib
import importlib
import io
import sys
import unittest
from pathlib import Path

from src.app import build_dynamic_worker_code, get_example, list_examples, render_example_page, render_home, route
from src.example_loader import EXAMPLES_DIR, load_manifest, verify_example_output
from src.example_sources_data import EXAMPLE_SOURCE_FILES

ROOT = Path(__file__).resolve().parents[1]


class AppTests(unittest.TestCase):
    def test_examples_are_versioned_and_lookupable(self):
        examples = list_examples()
        self.assertGreaterEqual(len(examples), 30)
        self.assertEqual(get_example("hello-world")["title"], "Hello World")
        self.assertIsNone(get_example("missing"))
        self.assertIn("docs.python.org/3.13", examples[0]["doc_url"])

    def test_every_example_has_go_by_example_style_explanation(self):
        for example in list_examples():
            with self.subTest(slug=example["slug"]):
                self.assertGreaterEqual(len(example.get("explanation", [])), 3)
                for paragraph in example["explanation"]:
                    self.assertGreaterEqual(len(paragraph), 40)
                    self.assertNotIn("sample code is deliberately small", paragraph.lower())
                    self.assertNotIn("use the linked python", paragraph.lower())
                    self.assertNotIn("full language rules", paragraph.lower())
                    self.assertNotIn("common shape you will write", paragraph.lower())
                self.assertNotIn(f"# {example['title']}\n", example["code"])
                self.assertGreaterEqual(len(example.get("walkthrough", [])), 1)
                self.assertIn("expected_output", example)
                self.assertIsInstance(example["expected_output"], str)

    def test_every_example_renders_literate_cells_with_output(self):
        for example in list_examples():
            with self.subTest(slug=example["slug"]):
                html = render_example_page(example)
                self.assertIn('lesson-step lp-cell', html)
                self.assertIn('class="cell-source"', html)
                self.assertIn('class="cell-output"', html)
                self.assertNotIn('<div class="cell-output"><p class="cell-label">Output</p><pre><code></code></pre></div>', html)

    def test_iterating_over_iterables_walkthrough_matches_code_fragments(self):
        example = get_example("iterating-over-iterables")
        pairs = [(step["prose"], step["code"]) for step in example["walkthrough"]]
        self.assertIn("ordinary list", pairs[0][0])
        self.assertIn('names = ["Ada", "Grace", "Guido"]', pairs[0][1])
        self.assertIn("only need the values", pairs[1][0])
        self.assertIn("for name in names", pairs[1][1])
        self.assertIn("enumerate()", pairs[2][0])
        self.assertIn("enumerate(names)", pairs[2][1])
        self.assertIn("dict.items()", pairs[3][0])
        self.assertIn("scores.items()", pairs[3][1])

    def test_every_example_executes_without_error(self):
        for example in list_examples():
            with self.subTest(slug=example["slug"]):
                stdout = io.StringIO()
                with contextlib.redirect_stdout(stdout):
                    exec(example["code"], {"__name__": "__main__"})
                self.assertIsInstance(stdout.getvalue(), str)

    def test_language_surface_has_good_initial_coverage(self):
        sections = {example["section"] for example in list_examples()}
        expected_sections = {
            "Basics",
            "Control Flow",
            "Functions",
            "Collections",
            "Classes",
            "Errors",
            "Modules",
            "Text",
            "Async",
            "Iteration",
            "Types",
            "Standard Library",
            "Data Model",
        }
        self.assertTrue(expected_sections.issubset(sections), sections)

        slugs = {example["slug"] for example in list_examples()}
        expected_slugs = {
            "conditionals",
            "assignment-expressions",
            "break-and-continue",
            "loop-else",
            "while-loops",
            "match-statements",
            "advanced-match-patterns",
            "tuples",
            "sets",
            "slices",
            "comprehension-patterns",
            "keyword-only-arguments",
            "positional-only-parameters",
            "lambdas",
            "generators",
            "yield-from",
            "generator-expressions",
            "iterators",
            "decorators",
            "scope-global-nonlocal",
            "context-managers",
            "delete-statements",
            "dataclasses",
            "inheritance-and-super",
            "metaclasses",
            "type-hints",
            "protocols",
            "enums",
            "json",
            "assertions",
            "exception-chaining",
            "exception-groups",
            "import-aliases",
            "datetime",
            "sorting",
            "itertools",
            "iterating-over-iterables",
            "truthiness",
            "equality-and-identity",
            "mutability",
            "unpacking",
            "args-and-kwargs",
            "properties",
            "special-methods",
            "regular-expressions",
            "constants",
            "numbers",
            "booleans",
            "none",
            "string-formatting",
            "multiple-return-values",
            "closures",
            "recursion",
            "number-parsing",
            "custom-exceptions",
            "operators",
            "literals",
            "async-iteration-and-context",
        }
        self.assertTrue(expected_slugs.issubset(slugs), slugs)

    def test_syntax_surface_has_explicit_examples(self):
        source = "\n".join(example["code"] for example in list_examples())
        tree = ast.parse(source)
        node_names = {type(node).__name__ for node in ast.walk(tree)}
        required_nodes = {
            "Assert",
            "AsyncFor",
            "AsyncWith",
            "Break",
            "Continue",
            "Delete",
            "Global",
            "NamedExpr",
            "Nonlocal",
            "TryStar",
            "YieldFrom",
        }
        self.assertTrue(required_nodes.issubset(node_names), required_nodes - node_names)
        required_snippets = [
            "for name in names:\n    if name ==",
            "class Event(metaclass=Tagged):",
            "def scale(value, /, factor=2, *, clamp=False):",
            "raise ConfigError(\"port must be a number\") from error",
            "except* ValueError as group:",
            "import statistics as stats",
            "from math import sqrt as square_root",
            "case [\"quit\" | \"exit\"]:",
            "case [\"echo\", *words]:",
            "case _:",
            "pattern = r\"\\d+\"",
            "data = b\"py\"",
            "number = 2 + 3j",
            "class Greeter(Protocol):",
            "print(Scale(2) @ Scale(3))",
            "print(...)",
        ]
        for snippet in required_snippets:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, source)

    def test_journey_pages_are_routable_but_not_linked_from_home(self):
        from src.app import JOURNEYS, route

        home = route("https://example.com/").body
        self.assertNotIn("/journeys/", home)
        index = route("https://example.com/journeys")
        self.assertEqual(index.status, 200)
        self.assertIn("Python learning journeys", index.body)
        self.assertGreaterEqual(len(JOURNEYS), 6)
        for journey in JOURNEYS:
            self.assertIn(f'/journeys/{journey["slug"]}', index.body)
        for journey in JOURNEYS:
            self.assertGreaterEqual(len(journey["sections"]), 3)
            page = route(f"https://example.com/journeys/{journey['slug']}")
            self.assertEqual(page.status, 200)
            self.assertIn("Journey", page.body)
            self.assertIn("journey-overview", page.body)
            self.assertIn("journey-section", page.body)
            self.assertNotIn("Gap ·", page.body)
            self.assertIn("/examples/", page.body)
            self.assertIn("Use this example to ", page.body)
            self.assertNotIn("This gap should ", page.body)
            self.assertNotIn("journey-step-number", page.body)

    def test_see_also_links_form_valid_example_graph(self):
        examples = list_examples()
        slugs = {example["slug"] for example in examples}
        linked = [example for example in examples if example.get("see_also")]
        self.assertGreaterEqual(len(linked), 12)
        for example in linked:
            with self.subTest(slug=example["slug"]):
                self.assertNotIn(example["slug"], example["see_also"])
                self.assertTrue(set(example["see_also"]).issubset(slugs), set(example["see_also"]) - slugs)
        html = render_example_page(get_example("break-and-continue"))
        self.assertIn("See also", html)
        self.assertIn("contrast", html)
        self.assertIn('/examples/loop-else', html)
        self.assertNotIn('class="see-also"', html)
        missing = route("https://example.com/examples/break-continue")
        self.assertEqual(missing.status, 404)
        self.assertIn("Recommended examples", missing.body)

    def test_examples_are_in_learning_order_and_link_supported_python_docs(self):
        examples = list_examples()
        self.assertEqual(
            [example["slug"] for example in examples[:9]],
            [
                "hello-world",
                "values",
                "literals",
                "numbers",
                "booleans",
                "operators",
                "none",
                "variables",
                "constants",
            ],
        )
        for example in examples:
            with self.subTest(slug=example["slug"]):
                self.assertTrue(example["doc_url"].startswith("https://docs.python.org/3.13/"))

    def test_example_page_contains_code_docs_and_run_form(self):
        html = render_example_page(get_example("hello-world"), output="hello world\n")
        self.assertIn("Hello World", html)
        self.assertIn("https://docs.python.org/", html)
        css = (ROOT / "public" / "site.css").read_text()
        self.assertIn('rel="icon" href="/favicon.svg"', html)
        self.assertRegex(html, r'rel="stylesheet" href="/site\.[0-9a-f]{12}\.css"')
        self.assertRegex(html, r'type="module" src="/syntax-highlight\.[0-9a-f]{12}\.js"')
        self.assertRegex(html, r'type="module" src="/editor\.[0-9a-f]{12}\.js"')
        self.assertNotIn('href="/site.css"', html)
        self.assertNotIn('src="/syntax-highlight.js"', html)
        self.assertIn('textarea { box-sizing: border-box; width: 100%; height: auto;', css)
        self.assertIn('class="language-python"', html)
        self.assertIn('print(&quot;hello world&quot;)', html)
        self.assertNotIn('class="tok-', html)
        self.assertIn("hello world", html)
        self.assertIn("Output", html)
        self.assertIn("Executed in 12.3 ms", render_example_page(get_example("hello-world"), output="hello world\n", execution_time_ms=12.3))
        self.assertIn("Execution time appears here after you run the example.", render_example_page(get_example("hello-world")))
        self.assertIn("Expected output", render_example_page(get_example("hello-world")))
        self.assertIn('rel="next" href="/examples/values"', html)
        self.assertIn('method="post"', html)
        self.assertIn('<textarea name="code"', html)
        self.assertNotIn('class="lesson-grid"', html)
        self.assertNotIn('class="lesson-copy"', html)
        self.assertIn('lesson-step lp-cell', html)
        self.assertIn('class="cell-output"', html)
        self.assertIn('class="literate-program"', html)
        self.assertIn('Annotated code walkthrough', html)
        self.assertIn('class="playground"', html)
        self.assertIn('class="runner-panel runner-editor"', html)
        self.assertIn('class="runner-panel output-panel"', html)
        self.assertIn('Run the complete example', html)

    def test_ui_polish_principles_are_applied(self):
        html = render_example_page(get_example("hello-world"), output="hello world\n")
        css = (ROOT / "public" / "site.css").read_text()
        self.assertIn("-webkit-font-smoothing: antialiased", css)
        self.assertIn("text-wrap: balance", css)
        self.assertIn("font-variant-numeric: tabular-nums", css)
        self.assertIn("transform: scale(0.96)", css)
        self.assertIn("nav a { color: inherit; text-decoration: underline", css)
        self.assertNotIn("nav a { min-height: 40px; display: inline-flex; align-items: center; border-radius", css)
        self.assertNotIn("transition: all", css)
        self.assertIn("min-height: 40px", css)
        self.assertIn("box-shadow:", css)
        self.assertIn("background: transparent", css)
        self.assertIn("border-left: 2px solid var(--accent)", css)
        self.assertIn("--space-6", css)
        self.assertIn("runner-grid", css)
        home = render_home()
        self.assertIn('class="hero"', home)
        self.assertIn('<a class="card" href="/examples/hello-world">', home)
        self.assertNotIn('<article class="card"', home)
        self.assertIn('class="example-shell"', html)

    def test_cf_workers_design_system_and_playground_lessons(self):
        html = render_example_page(get_example("hello-world"), output="hello world\n")
        css = (ROOT / "public" / "site.css").read_text()
        self.assertIn("#FF4801", css)
        self.assertIn("#F5F1EB", css)
        self.assertIn("#521000", css)
        self.assertIn("#EBD5C1", css)
        self.assertNotIn("corner", html)
        self.assertNotIn('border-style: dashed', html)
        self.assertIn('class="playground-toolbar"', html)
        self.assertIn('type="submit">Run', html)
        self.assertIn('type="button" data-reset', html)
        self.assertNotIn('data-copy', html)
        self.assertNotIn('data-share', html)
        self.assertIn('output-panel', html)
        self.assertIn(".runner-panel", css)
        self.assertIn(".runner-panel h3", css)
        self.assertIn("text-underline-offset", css)
        self.assertIn('aria-live="polite"', html)
        self.assertIn('min-height: 18rem', css)
        self.assertIn('white-space: pre-wrap', css)
        self.assertIn('overflow-wrap: anywhere', css)
        self.assertNotIn('max-height: 18rem', css)
        self.assertIn('data-output-placeholder', html)
        self.assertIn('.execution-time', css)
        self.assertIn('min-height: 1.5rem', css)
        self.assertIn('.cm-editor', css)
        self.assertIn("function resetCode", html)
        self.assertIn('class="syntax-inline">print()</code>', html)
        self.assertNotIn("navigator.clipboard", html)
        self.assertIn("fetch(form.action", html)
        self.assertIn("new URLSearchParams(new FormData(form))", html)
        self.assertIn("application/x-www-form-urlencoded", html)
        self.assertIn("Running in a Dynamic Python Worker", html)
        self.assertIn("catch (error)", html)

    def test_conditionals_are_substantive_not_bare_minimum(self):
        example = get_example("conditionals")
        self.assertGreaterEqual(len(example["walkthrough"]), 4)
        self.assertIn("elif", example["code"])
        self.assertIn("ternary", " ".join(example["explanation"]).lower())
        self.assertIn("nested", " ".join(example["explanation"]).lower())
        html = render_example_page(example)
        self.assertIn('class="syntax-inline">if</code>', html)
        self.assertIn('elif', html)
        self.assertNotIn("Conditions use truthiness", html)

    def test_datetime_covers_date_time_delta_formatting_and_parsing(self):
        example = get_example("datetime")
        code = example["code"]
        self.assertIn("date(", code)
        self.assertIn("time(", code)
        self.assertIn("timedelta", code)
        self.assertIn("strftime", code)
        self.assertIn("fromisoformat", code)
        self.assertGreaterEqual(len(example["walkthrough"]), 4)

    def test_routes(self):
        home = route("https://example.test/")
        self.assertEqual(home.status, 200)
        self.assertIn("Python By Example", home.body)

        page = route("https://example.test/examples/hello-world")
        self.assertEqual(page.status, 200)
        self.assertIn("Hello World", page.body)

        favicon = route("https://example.test/favicon.svg")
        self.assertEqual(favicon.status, 200)
        self.assertEqual(favicon.headers["Content-Type"], "image/svg+xml; charset=utf-8")
        self.assertIn("#FF4801", favicon.body)

        missing = route("https://example.test/examples/nope")
        self.assertEqual(missing.status, 404)

    def test_app_imports_when_worker_main_uses_src_as_import_root(self):
        src_path = str(Path(__file__).resolve().parents[1] / "src")
        sys.path.insert(0, src_path)
        try:
            module = importlib.import_module("app")
            self.assertEqual(module.get_example("hello-world")["title"], "Hello World")
        finally:
            sys.path.remove(src_path)
            sys.modules.pop("app", None)

    def test_worker_entrypoint_uses_fastapi_asgi_bridge(self):
        main_source = (ROOT / "src" / "main.py").read_text()
        self.assertIn("from fastapi import FastAPI, Request", main_source)
        self.assertIn("app = FastAPI", main_source)
        self.assertIn("import worker_asgi_bridge as asgi", main_source)
        self.assertIn("return await asgi.fetch(app, request.js_object, self.env)", main_source)
        self.assertIn("caches.default.match", main_source)
        self.assertIn("caches.default.put", main_source)
        self.assertIn("Cache-Control", main_source)
        self.assertIn("POST requests and are intentionally never cached", main_source)
        self.assertIn('def should_cache_get_url(url: str) -> bool:', main_source)
        self.assertIn('return not path.startswith("/layout-options/")', main_source)
        self.assertIn('response.headers.set("Cache-Control", "no-store")', main_source)

    def test_dynamic_worker_execution_uses_hash_keyed_get_cache(self):
        main_source = (ROOT / "src" / "main.py").read_text()
        self.assertIn("hashlib.sha256(code.encode", main_source)
        self.assertIn('worker_id = f"pythonbyexample:{PYTHON_VERSION}:{slug}:{code_hash}"', main_source)
        self.assertIn("env.LOADER.get(worker_id", main_source)
        self.assertIn("create_once_callable", main_source)
        self.assertIn('module_name = "runner.py"', main_source)
        self.assertIn("python_from_rpc", main_source)
        self.assertIn("JsRequest.new(str(request.url), _to_js_object", main_source)
        self.assertIn('"disable_python_external_sdk"', main_source)
        self.assertIn('"modules": {module_name: build_dynamic_worker_code(code)}', main_source)
        self.assertNotIn("env.LOADER.load(", main_source)
        self.assertNotIn('module_name = "src/runner.py"', main_source)
        self.assertNotIn('{"py": build_dynamic_worker_code(code)}', main_source)

    def test_runtime_dependencies_include_fastapi_stack(self):
        pyproject = (ROOT / "pyproject.toml").read_text()
        self.assertIn('"fastapi', pyproject)
        self.assertNotIn('"jinja2', pyproject)
        self.assertNotIn('"markupsafe', pyproject)
        self.assertIn('requires-python = ">=3.13,<3.14"', pyproject)
        wrangler = (ROOT / "wrangler.jsonc").read_text()
        self.assertIn('"assets"', wrangler)
        self.assertIn('"directory": "./public"', wrangler)
        self.assertTrue((ROOT / "public" / "favicon.svg").exists())

    def test_markdown_sources_drive_catalog_and_verifier(self):
        catalog = load_manifest()
        self.assertEqual(catalog.python_version, "3.13")
        self.assertEqual(catalog.docs_base_url, "https://docs.python.org/3.13")
        self.assertEqual(catalog.order[0], "hello-world")
        values_source = (EXAMPLES_DIR / "values.md").read_text()
        self.assertIn('doc_path = "/library/stdtypes.html"', values_source)
        self.assertIn(":::program", values_source)
        self.assertNotIn("docs.python.org/3.13", values_source)
        self.assertEqual(EXAMPLE_SOURCE_FILES["values.md"], values_source)
        self.assertEqual(verify_example_output(get_example("values")), [])

    def test_dynamic_worker_code_wraps_user_example(self):
        code = build_dynamic_worker_code('print("ok")\n')
        self.assertIn("class Default(WorkerEntrypoint)", code)
        self.assertIn("contextlib.redirect_stdout", code)
        self.assertIn('print("ok")', code)
        self.assertNotIn("globalOutbound", code)


if __name__ == "__main__":
    unittest.main()
