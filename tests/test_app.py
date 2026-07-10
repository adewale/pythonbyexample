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

from src.app import build_dynamic_worker_code, get_example, list_examples, render_example_page, render_home, route
from src.example_loader import EXAMPLES_DIR, load_manifest, verify_example_output
from src.asset_manifest import ASSET_PATHS
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
    ENVIRONMENT_SHAPED_SLUGS = {
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
                    exec(example["code"], {"__name__": "__main__"})
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
        self.assertIn("--accent-action: #C83800", css)
        self.assertIn("background: var(--accent-action)", css)
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

    def test_turnstile_widget_is_conditional_and_temporary(self):
        page = render_example_page(get_example("hello-world"))
        self.assertNotIn('class="turnstile-challenge"', page)
        self.assertNotIn('<script src="https://challenges.cloudflare.com/turnstile', page)

        protected = render_example_page(get_example("hello-world"), turnstile_site_key="site-key-123")
        runner = (ROOT / "public" / "runner.js").read_text()
        self.assertIn('data-turnstile-sitekey="site-key-123"', protected)
        self.assertIn(ASSET_PATHS["RUNNER_JS"], protected)
        self.assertNotIn("<script nonce=", protected)
        self.assertNotIn("onclick=", protected)
        self.assertIn("turnstile.render", runner)
        self.assertIn("execution: 'execute'", runner)
        self.assertNotIn("size: 'invisible'", runner)
        self.assertIn("turnstile.remove", runner)
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

    def test_cf_workers_design_system_and_playground_lessons(self):
        html = render_example_page(get_example("hello-world"))
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

        editor = (ROOT / "public" / "editor.js").read_text()
        runner = (ROOT / "public" / "runner.js").read_text()
        self.assertIn("EditorView.contentAttributes.of", editor)
        self.assertIn("'aria-label': textarea.getAttribute('aria-label')", editor)
        self.assertIn("textarea.dataset.originalCode", runner)
        self.assertIn("window.pythonByExampleEditor?.setValue(value)", runner)
        self.assertIn("fetch(form.action", runner)
        self.assertIn("new URLSearchParams(formData)", runner)
        self.assertIn("application/x-www-form-urlencoded", runner)
        self.assertIn("response.status === 413", runner)
        self.assertIn("Submitted code is too large", runner)
        self.assertIn("catch (error)", runner)

    def test_generated_drift_is_blocked_before_commit_and_merge(self):
        hook = (ROOT / ".githooks" / "pre-commit").read_text()
        installer = (ROOT / "scripts" / "install-git-hooks.sh").read_text()
        verify_workflow = (ROOT / ".github" / "workflows" / "verify.yml").read_text()
        self.assertIn("make check-generated", hook)
        self.assertIn(".githooks/pre-commit", installer)
        self.assertIn("make verify", verify_workflow)
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
    def test_css_defines_a_dark_palette(self):
        css = (ROOT / "public" / "site.css").read_text()
        self.assertIn("@media (prefers-color-scheme: dark)", css)
        self.assertIn("color-scheme: dark", css)
        dark_block = css.split("@media (prefers-color-scheme: dark)", 1)[1]
        for token in ["--text:", "--muted:", "--page:", "--surface:", "--hairline:"]:
            self.assertIn(token, dark_block)

    def test_dark_mode_keeps_marginalia_figures_on_light_paper(self):
        css = (ROOT / "public" / "site.css").read_text()
        dark_block = css.split("@media (prefers-color-scheme: dark)", 1)[1]
        self.assertIn("--figure-paper", css)
        self.assertIn(".cell-banner figure svg", dark_block)
        self.assertIn(".journey-section-figure svg", dark_block)

    def test_shiki_highlights_with_dual_light_dark_themes(self):
        js = (ROOT / "public" / "syntax-highlight.js").read_text()
        self.assertIn("github-light", js)
        self.assertIn("github-dark", js)
        self.assertIn("themes:", js)
        css = (ROOT / "public" / "site.css").read_text()
        self.assertIn("--shiki-dark", css)

    def test_editor_picks_a_dark_highlight_style_in_dark_mode(self):
        js = (ROOT / "public" / "editor.js").read_text()
        self.assertIn("prefers-color-scheme: dark", js)
        self.assertIn("oneDarkHighlightStyle", js)

    def test_every_page_offers_a_skip_link_to_main_content(self):
        for page in [render_home(), render_example_page(get_example("hello-world"))]:
            self.assertIn('<a class="skip-link" href="#main-content">Skip to main content</a>', page)
            self.assertIn('<main id="main-content">', page)
        css = (ROOT / "public" / "site.css").read_text()
        self.assertIn(".skip-link", css)
        self.assertIn(".skip-link:focus", css)


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

    def test_search_css_styles_light_and_dark(self):
        css = (ROOT / "public" / "site.css").read_text()
        self.assertIn(".site-search", css)
        self.assertIn(".search-results", css)


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

    def test_journey_pages_reference_social_cards_and_collection_json_ld(self):
        from src.app import JOURNEYS, render_journey_page

        journey = JOURNEYS[0]
        page = render_journey_page(journey)
        self.assertIn(f'https://www.pythonbyexample.dev/og/journey-{journey["slug"]}.jpg', page)
        self.assertIn('<meta name="twitter:card" content="summary_large_image">', page)
        data = json.loads(re.search(r'<script type="application/ld\+json">(.+?)</script>', page, re.S).group(1))
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

    def test_card_html_composes_title_section_and_figure(self):
        from scripts.build_social_cards import render_social_card_html

        card = render_social_card_html(get_example("closures"))
        self.assertIn("<svg", card)
        self.assertIn("Closures", card)
        self.assertIn("Functions", card)
        self.assertIn("pythonbyexample.dev", card)

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
        self.assertIn("<loc>https://www.pythonbyexample.dev/journeys</loc>", response.body)
        from src.app import JOURNEYS

        for journey in JOURNEYS:
            self.assertIn(f"<loc>https://www.pythonbyexample.dev/journeys/{journey['slug']}</loc>", response.body)
        for example in list_examples():
            self.assertIn(f"<loc>https://www.pythonbyexample.dev/examples/{example['slug']}</loc>", response.body)
        self.assertEqual(
            response.body.count("<loc>"),
            2 + len(JOURNEYS) + len(list_examples()),
        )

    def test_example_pages_carry_learning_resource_json_ld(self):
        example = get_example("closures")
        page = render_example_page(example)
        match = re.search(r'<script type="application/ld\+json">(.+?)</script>', page, re.S)
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
        match = re.search(r'<script type="application/ld\+json">(.+?)</script>', page, re.S)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(data["@type"], "WebSite")
        self.assertEqual(data["url"], "https://www.pythonbyexample.dev/")

    def test_json_ld_escapes_script_closing_sequences(self):
        from src.app import _structured_data_script

        script = _structured_data_script({"name": "</script><script>alert(1)"})
        self.assertNotIn("</script><script>", script.removesuffix("</script>"))

    def test_robots_txt_references_sitemap(self):
        robots = (ROOT / "public" / "robots.txt").read_text()
        self.assertIn("Sitemap: https://www.pythonbyexample.dev/sitemap.xml", robots)
        self.assertIn("User-agent: *", robots)


if __name__ == "__main__":
    unittest.main()
