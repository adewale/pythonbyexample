import ast
import contextlib
import html as html_lib
import importlib
import io
import json
import re
import sys
import unittest
from pathlib import Path
from typing import ClassVar

from src.app import (
    build_dynamic_worker_code,
    get_example,
    list_examples,
    render_example_page,
    render_home,
    render_privacy,
    route,
)
from src.asset_manifest import ASSET_PATHS
from src.example_loader import EXAMPLES_DIR, load_manifest, verify_example_output
from src.example_sources_data import EXAMPLE_SOURCE_FILES
from src.security import CONTENT_SECURITY_POLICY

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

    # Environment-shaped examples carry hand-written expected_output
    # (their real output depends on subprocess/socket/thread timing), so
    # for them executing without error is the contract.
    ENVIRONMENT_SHAPED_SLUGS: ClassVar = {
        "networking",
        "subprocesses",
        "threads-and-processes",
        "virtual-environments",
    }

    def test_every_example_executes_and_matches_expected_output(self):
        for example in list_examples():
            with self.subTest(slug=example["slug"]):
                stdout = io.StringIO()
                with contextlib.redirect_stdout(stdout):
                    exec(example["code"], {"__name__": "__main__"})  # noqa: S102
                if example["slug"] in self.ENVIRONMENT_SHAPED_SLUGS:
                    continue
                self.assertEqual(stdout.getvalue(), example["expected_output"])

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
        self.assertNotIn('/journeys/workers', index.body)
        self.assertEqual(route("https://example.com/journeys/workers").status, 404)
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
        self.assertIn('rel="icon" href="/favicon.svg"', html)
        self.assertRegex(html, r'rel="stylesheet" href="/site\.[0-9a-f]{12}\.css"')
        self.assertRegex(html, r'type="module" src="/syntax-highlight\.[0-9a-f]{12}\.js"')
        self.assertRegex(html, r'type="module" src="/editor\.[0-9a-f]{12}\.js"')
        self.assertNotIn('href="/site.css"', html)
        self.assertNotIn('src="/syntax-highlight.js"', html)
        self.assertIn('class="language-python"', html)
        self.assertIn('print(&quot;hello world&quot;)', html)
        self.assertNotIn('class="tok-', html)
        self.assertIn("hello world", html)
        self.assertIn("Output", html)
        self.assertIn("Executed in 12.3 ms", render_example_page(get_example("hello-world"), output="hello world\n", execution_time_ms=12.3))
        self.assertIn("Execution time appears here after you run the example.", render_example_page(get_example("hello-world")))
        self.assertIn("Expected output", render_example_page(get_example("hello-world")))
        self.assertIn('rel="next" title="Next example (right arrow key)" href="/examples/values"', html)
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

    def test_home_cards_are_links_and_examples_use_the_shell(self):
        # Rendered styling (press states, touch targets, contrast, balanced
        # headings, antialiasing, transitions) is measured in a real browser by
        # scripts/check_browser_layout.mjs, not by matching site.css text.
        html = render_example_page(get_example("hello-world"), output="hello world\n")
        home = render_home()
        self.assertIn('class="hero"', home)
        self.assertIn('<a class="card" href="/examples/hello-world">', home)
        self.assertNotIn('<article class="card"', home)
        self.assertIn('class="example-shell"', html)

    def test_turnstile_widget_is_conditional_and_temporary(self):
        page = render_example_page(get_example("hello-world"))
        self.assertNotIn('class="turnstile-challenge"', page)
        self.assertNotIn('<script src="https://challenges.cloudflare.com/turnstile', page)

        protected = render_example_page(get_example("hello-world"), turnstile_site_key="site-key-123")
        self.assertIn('data-turnstile-sitekey="site-key-123"', protected)
        self.assertIn(ASSET_PATHS["RUNNER_JS"], protected)
        self.assertNotIn("<script nonce=", protected)
        self.assertNotIn("onclick=", protected)
        # The widget's Invisible execute mode and its removal after each
        # challenge are exercised in scripts/check_browser_layout.mjs.
        self.assertNotIn('class="cf-turnstile"', protected)

        challenged = render_example_page(
            get_example("hello-world"),
            turnstile_site_key="site-key-123",
            turnstile_required=True,
        )
        self.assertIn('data-turnstile-required="true"', challenged)

    def test_turnstile_verification_is_session_gated_in_worker(self):
        main_source = (ROOT / "src" / "main.py").read_text()
        self.assertIn("TURNSTILE_SECRET_KEY", main_source)
        self.assertIn("TURNSTILE_CHALLENGE_MODE", main_source)
        self.assertIn("TURNSTILE_CLEARANCE_COOKIE", main_source)
        self.assertIn("cf-turnstile-response", main_source)
        self.assertIn("/turnstile/v0/siteverify", main_source)
        self.assertIn("PBE_SMOKE_BYPASS_SECRET", main_source)
        self.assertIn("x-pythonbyexample-smoke-secret", main_source)
        self.assertIn("Content-Security-Policy", main_source)
        self.assertIn("Strict-Transport-Security", main_source)
        self.assertIn("script-src-attr 'none'", CONTENT_SECURITY_POLICY)
        self.assertNotIn("nonce-", CONTENT_SECURITY_POLICY)
        self.assertNotIn("script-src 'unsafe-inline'", CONTENT_SECURITY_POLICY)

    def test_playground_markup_is_server_rendered_and_escaped(self):
        # Runner behaviour (reset, stale-run ordering, 413 and network errors,
        # sharing, editor accessible name) and output wrapping are exercised in
        # scripts/check_browser_layout.mjs.
        html = render_example_page(get_example("hello-world"))
        self.assertNotIn("corner", html)
        self.assertNotIn('border-style: dashed', html)
        self.assertIn('class="playground-toolbar"', html)
        self.assertIn('type="submit">Run', html)
        self.assertIn('type="reset" data-reset', html)
        self.assertNotIn('data-copy', html)
        self.assertNotIn('data-share', html)
        self.assertIn('output-panel', html)
        self.assertIn('aria-live="polite"', html)
        self.assertIn('data-output-placeholder', html)
        self.assertIn('data-original-code="', html)
        self.assertIn(html_lib.escape(get_example("hello-world")["code"]), html)
        hostile_example = {**get_example("hello-world"), "code": 'print("</script><script>alert(1)</script>")\n'}
        hostile_html = render_example_page(hostile_example)
        self.assertIn('data-original-code="print(&quot;&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;&quot;)', hostile_html)
        self.assertNotIn("<script nonce=", hostile_html)
        self.assertIn(ASSET_PATHS["EDITOR_JS"], html)
        self.assertIn(ASSET_PATHS["RUNNER_JS"], html)
        self.assertNotIn("<script nonce=", html)
        self.assertIn('class="syntax-inline">print()</code>', html)
        self.assertNotIn("navigator.clipboard", html)
        # Server markup renders only the Run and Reset buttons; share and
        # copy affordances are injected by JavaScript.
        self.assertEqual(html.count("<button"), 2)

    def test_generated_drift_is_blocked_before_commit_and_merge(self):
        hook = (ROOT / ".githooks" / "pre-commit").read_text()
        installer = (ROOT / "scripts" / "install-git-hooks.sh").read_text()
        verify_workflow = (ROOT / ".github" / "workflows" / "verify.yml").read_text()
        self.assertIn("make check-generated", hook)
        self.assertIn(".githooks/pre-commit", installer)
        self.assertIn("make verify", verify_workflow)
        self.assertIn("uv sync --locked --all-groups", verify_workflow)
        self.assertIn("npm ci --ignore-scripts", verify_workflow)
        self.assertFalse((ROOT / ".github" / "workflows" / "preview.yml").exists())
        wrangler_config = (ROOT / "wrangler.jsonc").read_text()
        self.assertIn('"workers_dev": false', wrangler_config)
        self.assertIn('"preview_urls": false', wrangler_config)
        package = json.loads((ROOT / "package.json").read_text())
        lock = json.loads((ROOT / "package-lock.json").read_text())
        wrangler = package["devDependencies"]["wrangler"]
        self.assertRegex(wrangler, r"^\d+\.\d+\.\d+$")
        self.assertEqual(package["engines"]["node"], "22.x")
        self.assertEqual(lock["packages"][""]["devDependencies"]["wrangler"], wrangler)
        self.assertEqual(lock["packages"]["node_modules/wrangler"]["version"], wrangler)
        makefile = (ROOT / "Makefile").read_text()
        self.assertIn("check-node-version", makefile)
        self.assertIn("pywrangler sync --force", makefile)
        self.assertFalse((ROOT / ".github" / "workflows" / "regenerate-generated-files.yml").exists())

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
        self.assertIn("import observability", main_source)
        self.assertIn('app.add_middleware(observability.WideEventMiddleware)', main_source)
        self.assertIn('asgi_request = getattr(request, "js_object", request)', main_source)
        self.assertIn('state={"wide_event": event}', main_source)
        self.assertNotIn("extra_scope", main_source)
        self.assertNotIn('"worker_request": request', main_source)
        self.assertIn("observability.emit(event, env=self.env)", main_source)
        self.assertNotIn("_CURRENT_WORKER_REQUEST", main_source)
        self.assertIn("caches.default.match", main_source)
        self.assertIn("caches.default.put", main_source)
        self.assertIn("Cache-Control", main_source)
        self.assertIn("POST requests and are intentionally never cached", main_source)
        self.assertIn('def should_cache_get_url(url: str) -> bool:', main_source)
        self.assertIn('return not path.startswith("/layout-options/")', main_source)
        self.assertIn('response.headers.set("Cache-Control", "no-store")', main_source)
        self.assertNotIn("route(", main_source)

    def test_dynamic_worker_execution_uses_hash_keyed_get_cache(self):
        main_source = (ROOT / "src" / "main.py").read_text()
        self.assertIn("hashlib.sha256(code.encode", main_source)
        self.assertIn('worker_id = f"pythonbyexample:{PYTHON_VERSION}:{slug}:{code_hash}"', main_source)
        self.assertIn("env.LOADER.get(worker_id", main_source)
        self.assertIn("create_once_callable", main_source)
        self.assertIn("code_callback_used = True", main_source)
        self.assertIn('if code_callback is not None and not code_callback_used and hasattr(code_callback, "destroy")', main_source)
        self.assertIn('module_name = "runner.py"', main_source)
        self.assertIn("python_from_rpc", main_source)
        self.assertIn("dynamic_request = JsRequest.new(", main_source)
        self.assertIn('"headers": {"x-request-id": event.get("request_id", "")}', main_source)
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


class DarkModeAndAccessibilityTests(unittest.TestCase):
    def test_optional_highlighters_retain_readable_server_fallbacks(self):
        page = render_example_page(get_example("values"))
        self.assertIn('<pre><code class="language-python">', page)
        self.assertIn('aria-label="Editable Python example code"', page)
        self.assertIn('<script type="module" src="/syntax-highlight.', page)
        self.assertIn('<script type="module" src="/editor.', page)

    def test_every_page_offers_a_skip_link_to_main_content(self):
        for page in [render_home(), render_example_page(get_example("hello-world"))]:
            self.assertIn('<a class="skip-link" href="#main-content">Skip to main content</a>', page)
            self.assertIn('<main id="main-content">', page)


class DesignFoundationsTests(unittest.TestCase):
    # Type size, landing header, non-motion accessibility fallbacks, press
    # states, touch targets and terminal contrast are measured in a real
    # browser by scripts/check_browser_layout.mjs.
    def test_search_exposes_combobox_semantics(self):
        home = render_home()
        self.assertIn('role="combobox"', home)
        self.assertIn('aria-expanded="false"', home)
        self.assertIn('role="listbox"', home)


class BannerTests(unittest.TestCase):
    def test_mutability_renders_a_two_figure_small_multiple_banner(self):
        page = render_example_page(get_example("mutability"))
        self.assertIn('class="cell-banner cell-banner--2"', page)
        self.assertIn("Two names share one mutable list", page)
        self.assertIn("a tuple is frozen", page)
        self.assertEqual(page.count("<figcaption>"), 2)

    def test_render_banner_accepts_position_grammar_and_legacy_anchors(self):
        from src.marginalia import render_banner, render_for_anchor

        by_position = render_banner("mutability", "after-cell-0")
        self.assertIn("cell-banner--2", by_position)
        self.assertEqual(render_for_anchor("mutability", "cell-0"), by_position)
        self.assertEqual(render_banner("mutability", "before"), "")
        self.assertEqual(render_banner("mutability", "after-walkthrough"), "")

    def test_before_and_after_walkthrough_positions_render_around_cells(self):
        from unittest import mock

        from src import app as app_module

        def fake_banner(slug, position):
            if slug != "hello-world":
                return ""
            return {"before": '<div class="cell-banner cell-banner--1">BEFORE-BANNER</div>',
                    "after-walkthrough": '<div class="cell-banner cell-banner--1">AFTER-BANNER</div>'}.get(position, "")

        with mock.patch.object(app_module, "render_banner", fake_banner):
            page = app_module.render_example_page(get_example("hello-world"))
        first_cell = page.index("lesson-step lp-cell")
        self.assertLess(page.index("BEFORE-BANNER"), first_cell)
        self.assertGreater(page.index("AFTER-BANNER"), page.rindex("lesson-step lp-cell"))

    def test_curated_pair_banners_render_on_contrast_cells(self):
        positional = render_example_page(get_example("positional-only-parameters"))
        self.assertIn('cell-banner--2', positional)
        self.assertIn("positional-only", positional)
        self.assertIn("must be named at the call site", positional)

        metaclasses = render_example_page(get_example("metaclasses"))
        self.assertIn('cell-banner--2', metaclasses)
        self.assertIn("the same triangle one level down", metaclasses)

        tuples_page = render_example_page(get_example("tuples"))
        self.assertIn('cell-banner--2', tuples_page)
        self.assertEqual(tuples_page.count('class="cell-banner'), 1)

    def test_iterator_vs_iterable_gains_a_one_pass_figure(self):
        page = render_example_page(get_example("iterator-vs-iterable"))
        self.assertEqual(page.count('class="cell-banner'), 2)
        self.assertIn("drains it", page)

    def test_no_page_renders_an_empty_banner(self):
        for example in list_examples():
            with self.subTest(slug=example["slug"]):
                page = render_example_page(example)
                self.assertNotIn('<div class="cell-banner cell-banner--0"></div>', page)
                self.assertNotIn('cell-banner--0', page)


class SearchTests(unittest.TestCase):
    def test_search_index_covers_every_example(self):
        index = json.loads((ROOT / "public" / "search-index.json").read_text())
        slugs = {entry["slug"] for entry in index}
        self.assertEqual(slugs, {example["slug"] for example in list_examples()})
        for entry in index:
            for key in ("slug", "title", "section", "summary", "text"):
                self.assertIn(key, entry)
            self.assertEqual(entry["text"], entry["text"].lower())

    def test_home_page_offers_search_with_fingerprinted_assets(self):
        home = render_home()
        self.assertIn('id="site-search-input"', home)
        self.assertIn('type="search"', home)
        self.assertIn('id="site-search-results"', home)
        index_match = re.search(r'data-search-index="(/search-index\.[0-9a-f]{12}\.json)"', home)
        self.assertIsNotNone(index_match)
        self.assertTrue((ROOT / "public" / index_match.group(1).lstrip("/")).exists())
        script_match = re.search(r'<script type="module" src="(/search\.[0-9a-f]{12}\.js)"></script>', home)
        self.assertIsNotNone(script_match)
        self.assertTrue((ROOT / "public" / script_match.group(1).lstrip("/")).exists())

    def test_example_pages_do_not_load_search_assets(self):
        page = render_example_page(get_example("hello-world"))
        self.assertNotIn("search-index", page)
        self.assertNotIn("/search.", page)

    def test_search_assets_get_immutable_cache_headers(self):
        headers = (ROOT / "public" / "_headers").read_text()
        self.assertIn("/search.*.js", headers)
        self.assertIn("/search-index.*.json", headers)


class SocialCardTests(unittest.TestCase):
    def test_example_pages_reference_per_slug_social_cards(self):
        example = get_example("closures")
        page = render_example_page(example)
        self.assertIn('<meta property="og:image" content="https://www.pythonbyexample.dev/og/closures.jpg">', page)
        self.assertIn('<meta name="twitter:card" content="summary_large_image">', page)
        self.assertIn('<meta name="twitter:image" content="https://www.pythonbyexample.dev/og/closures.jpg">', page)
        self.assertIn('<meta property="og:image:width" content="1200">', page)

    def test_home_page_references_home_social_card(self):
        home = render_home()
        self.assertIn('<meta property="og:image" content="https://www.pythonbyexample.dev/og/home.jpg">', home)
        self.assertIn('<meta name="twitter:card" content="summary_large_image">', home)

    def test_journeys_index_references_social_card_and_collection_json_ld(self):
        from src.app import render_journeys_index

        page = render_journeys_index()
        self.assertIn('<meta property="og:image" content="https://www.pythonbyexample.dev/og/journeys.jpg">', page)
        self.assertIn('<meta name="twitter:card" content="summary_large_image">', page)
        data = json.loads(re.search(r'<script type="application/ld\+json">(.+?)</script>', page, re.DOTALL).group(1))
        self.assertEqual(data["@type"], "CollectionPage")
        self.assertEqual(data["name"], "Python learning journeys")
        self.assertEqual(data["url"], "https://www.pythonbyexample.dev/journeys")

    def test_journey_pages_reference_social_cards_and_collection_json_ld(self):
        from src.app import JOURNEYS, render_journey_page

        journey = JOURNEYS[0]
        page = render_journey_page(journey)
        self.assertIn(f'https://www.pythonbyexample.dev/og/journey-{journey["slug"]}.jpg', page)
        self.assertIn('<meta name="twitter:card" content="summary_large_image">', page)
        data = json.loads(re.search(r'<script type="application/ld\+json">(.+?)</script>', page, re.DOTALL).group(1))
        self.assertEqual(data["@type"], "CollectionPage")
        self.assertEqual(data["url"], f'https://www.pythonbyexample.dev/journeys/{journey["slug"]}')

    def test_social_card_image_exists_for_every_published_page(self):
        for example in list_examples():
            with self.subTest(slug=example["slug"]):
                self.assertTrue((ROOT / "public" / "og" / f"{example['slug']}.jpg").exists())
        from src.app import JOURNEYS
        for journey in JOURNEYS:
            with self.subTest(slug=journey["slug"]):
                self.assertTrue((ROOT / "public" / "og" / f"journey-{journey['slug']}.jpg").exists())
        self.assertTrue((ROOT / "public" / "og" / "home.jpg").exists())
        self.assertTrue((ROOT / "public" / "og" / "journeys.jpg").exists())

    def test_card_html_composes_title_section_and_figure(self):
        from scripts.build_social_cards import render_social_card_html

        card = render_social_card_html(get_example("closures"))
        self.assertIn("<svg", card)
        self.assertIn("Closures", card)
        self.assertIn("Functions", card)
        self.assertIn("pythonbyexample.dev", card)

    def test_card_html_includes_journeys_index(self):
        from scripts.build_social_cards import card_html

        cards = card_html()
        self.assertIn("journeys", cards)
        self.assertIn("Python learning journeys", cards["journeys"])
        self.assertIn("Python By Example · Journeys", cards["journeys"])

    def test_card_html_includes_about_and_privacy_pages(self):
        from scripts.build_social_cards import card_html

        cards = card_html()
        self.assertIn("about", cards)
        self.assertIn("How this site is made", cards["about"])
        self.assertIn("Python By Example · About", cards["about"])
        self.assertIn("privacy", cards)
        self.assertIn("Privacy and data use", cards["privacy"])
        self.assertIn("Python By Example · Privacy", cards["privacy"])

    def test_runtime_journeys_and_edge_labels_load_from_editorial_registry(self):
        from src import app as app_module
        from src.editorial_registry import journeys, see_also_edge_labels

        self.assertEqual(app_module.JOURNEYS, journeys())
        self.assertEqual(app_module.SEE_ALSO_EDGE_LABELS, see_also_edge_labels())


class DiscoverabilityTests(unittest.TestCase):
    def test_sitemap_lists_every_page_with_canonical_urls(self):
        response = route("https://example.test/sitemap.xml")
        self.assertEqual(response.status, 200)
        self.assertEqual(response.headers["Content-Type"], "application/xml; charset=utf-8")
        self.assertIn('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', response.body)
        self.assertIn("<loc>https://www.pythonbyexample.dev/</loc>", response.body)
        self.assertIn("<loc>https://www.pythonbyexample.dev/about</loc>", response.body)
        self.assertIn("<loc>https://www.pythonbyexample.dev/privacy</loc>", response.body)
        self.assertIn("<loc>https://www.pythonbyexample.dev/journeys</loc>", response.body)
        from src.app import JOURNEYS

        for journey in JOURNEYS:
            self.assertIn(f"<loc>https://www.pythonbyexample.dev/journeys/{journey['slug']}</loc>", response.body)
        for example in list_examples():
            self.assertIn(f"<loc>https://www.pythonbyexample.dev/examples/{example['slug']}</loc>", response.body)
        self.assertEqual(
            response.body.count("<loc>"),
            4 + len(JOURNEYS) + len(list_examples()),
        )

    def test_example_pages_carry_learning_resource_json_ld(self):
        example = get_example("closures")
        page = render_example_page(example)
        match = re.search(r'<script type="application/ld\+json">(.+?)</script>', page, re.DOTALL)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(data["@context"], "https://schema.org")
        self.assertEqual(data["@type"], ["TechArticle", "LearningResource"])
        self.assertEqual(data["name"], example["title"])
        self.assertEqual(data["url"], "https://www.pythonbyexample.dev/examples/closures")
        self.assertEqual(data["programmingLanguage"], "Python")
        self.assertEqual(data["learningResourceType"], "Example")
        self.assertEqual(data["isPartOf"]["@type"], "WebSite")

    def test_home_page_carries_website_json_ld(self):
        page = render_home()
        match = re.search(r'<script type="application/ld\+json">(.+?)</script>', page, re.DOTALL)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(data["@type"], "WebSite")
        self.assertEqual(data["url"], "https://www.pythonbyexample.dev/")

    def test_json_ld_escapes_script_closing_sequences(self):
        from src.app import _structured_data_script

        script = _structured_data_script({"name": "</script><script>alert(1)"})
        self.assertNotIn("</script><script>", script.removesuffix("</script>"))

    def test_404_pages_omit_canonical_and_og_url_metadata(self):
        for response in (
            route("https://example.test/no-such-page"),
            route("https://example.test/examples/no-such-example"),
            route("https://example.test/journeys/no-such-journey"),
        ):
            with self.subTest(body=response.body[:80]):
                self.assertEqual(response.status, 404)
                self.assertNotIn('rel="canonical"', response.body)
                self.assertNotIn('property="og:url"', response.body)
                self.assertIn('<meta name="robots" content="noindex">', response.body)

    def test_robots_txt_references_sitemap(self):
        robots = (ROOT / "public" / "robots.txt").read_text()
        self.assertIn("Sitemap: https://www.pythonbyexample.dev/sitemap.xml", robots)
        self.assertIn("User-agent: *", robots)


class AboutPageTests(unittest.TestCase):
    def test_about_page_is_routable_with_canonical_metadata(self):
        response = route("https://example.test/about")
        self.assertEqual(response.status, 200)
        page = response.body
        self.assertIn("<title>About · Python By Example</title>", page)
        self.assertIn('<link rel="canonical" href="https://www.pythonbyexample.dev/about">', page)
        self.assertIn('<meta property="og:url" content="https://www.pythonbyexample.dev/about">', page)
        self.assertIn('<meta property="og:image" content="https://www.pythonbyexample.dev/og/about.jpg">', page)
        self.assertIn('<meta name="twitter:image" content="https://www.pythonbyexample.dev/og/about.jpg">', page)
        self.assertTrue((ROOT / "public" / "og" / "about.jpg").exists())
        match = re.search(r'<script type="application/ld\+json">(.+?)</script>', page, re.DOTALL)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(data["@type"], "AboutPage")
        self.assertEqual(data["url"], "https://www.pythonbyexample.dev/about")

    def test_about_page_derives_counts_instead_of_hardcoding_them(self):
        from src.app import JOURNEYS, render_about

        page = render_about()
        self.assertNotIn("__EXAMPLE_COUNT__", page)
        self.assertNotIn("__JOURNEY_COUNT__", page)
        self.assertIn(f"{len(list_examples())} examples and {len(JOURNEYS)} journeys", page)

    def test_about_page_renders_the_design_language_from_live_tokens(self):
        from src.app import render_about

        page = render_about()
        self.assertIn('class="token-grid"', page)
        self.assertIn("--swatch: var(--accent)", page)
        self.assertIn("width: var(--space-6)", page)
        self.assertIn('class="cell-code-stack"', page)

    def test_every_page_links_about_in_the_nav(self):
        for page in [render_home(), render_example_page(get_example("hello-world"))]:
            self.assertIn('<a href="/about">About</a>', page)

    def test_about_page_loads_no_editor_or_search_assets(self):
        page = route("https://example.test/about").body
        self.assertNotIn("/editor.", page)
        self.assertNotIn("search-index", page)

    def test_about_page_meets_the_seo_linter_bar(self):
        page = route("https://example.test/about").body
        self.assertIsNone(re.search(r"__[A-Z][A-Z0-9_]+__", page))
        description = re.search(r'<meta name="description" content="([^"]*)">', page)
        self.assertIsNotNone(description)
        self.assertTrue(80 <= len(description.group(1)) <= 180, len(description.group(1)))
        self.assertRegex(page, r'href="/site\.[0-9a-f]{12}\.css"')
        self.assertRegex(page, r'src="/syntax-highlight\.[0-9a-f]{12}\.js"')


class PrivacyPageTests(unittest.TestCase):
    def test_privacy_page_is_routable_and_globally_linked(self):
        response = route("https://example.test/privacy")
        self.assertEqual(response.status, 200)
        page = response.body
        self.assertIn("<title>Privacy · Python By Example</title>", page)
        self.assertIn('<link rel="canonical" href="https://www.pythonbyexample.dev/privacy">', page)
        self.assertIn('<meta property="og:image" content="https://www.pythonbyexample.dev/og/privacy.jpg">', page)
        self.assertTrue((ROOT / "public" / "og" / "privacy.jpg").exists())
        for rendered in (render_home(), render_example_page(get_example("hello-world")), page):
            self.assertIn('<a class="text-link" href="/privacy">Privacy</a>', rendered)

    def test_privacy_notice_discloses_runner_turnstile_logs_cdn_and_cookie(self):
        page = render_privacy()
        for required in (
            "Cloudflare Turnstile Privacy Addendum",
            "https://www.cloudflare.com/privacypolicy/",
            "pbe_turnstile_clearance",
            "eight hours",
            "submitted Python source",
            "esm.sh",
            "IP address",
            "raw submitted code",
        ):
            with self.subTest(required=required):
                self.assertIn(required, page)
        self.assertIn("do not sell", page)

    def test_privacy_page_has_webpage_structured_data_without_editor_assets(self):
        page = render_privacy()
        match = re.search(r'<script type="application/ld\+json">(.+?)</script>', page, re.DOTALL)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(data["@type"], "WebPage")
        self.assertEqual(data["url"], "https://www.pythonbyexample.dev/privacy")
        self.assertNotIn("/editor.", page)
        self.assertNotIn("search-index", page)


class KeyboardNavTests(unittest.TestCase):
    # Arrow navigation, its guards (edited code, modifier keys, editable and
    # button targets, catalog edges), sharing and the copy button are
    # exercised in scripts/check_browser_layout.mjs.
    def test_nav_links_advertise_the_keyboard_shortcut(self):
        page = render_example_page(get_example("values"))
        self.assertIn('title="Previous example (left arrow key)"', page)
        self.assertIn('title="Next example (right arrow key)"', page)

    def test_runner_module_loads_async_ahead_of_cdn_modules(self):
        page = render_example_page(get_example("values"))
        self.assertRegex(page, r'<script type="module" async src="/runner\.[0-9a-f]{12}\.js"></script>')

    def test_arrow_navigation_guards_missing_neighbors_at_catalog_edges(self):
        examples = list_examples()
        first_page = render_example_page(get_example(examples[0]["slug"]))
        last_page = render_example_page(get_example(examples[-1]["slug"]))
        self.assertNotIn('<a class="text-link" rel="prev"', first_page)
        self.assertIn('<a class="text-link" rel="next"', first_page)
        self.assertIn('<a class="text-link" rel="prev"', last_page)
        self.assertNotIn('<a class="text-link" rel="next"', last_page)


if __name__ == "__main__":
    unittest.main()
