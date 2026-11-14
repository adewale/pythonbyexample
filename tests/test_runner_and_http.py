"""Behaviour a learner or a crawler can observe at the runner and HTTP edges."""
import asyncio
import json
import sys
import time
import types
import unittest
from pathlib import Path
from types import SimpleNamespace

from src.app import (
    INPUT_UNAVAILABLE_MESSAGE,
    JOURNEYS,
    build_dynamic_worker_code,
    example_markdown,
    get_example,
    list_examples,
    render_example_page,
    render_journey_page,
    render_llms_txt,
    sandbox_limit_note,
)
from src.marginalia import render_banner
from tests.test_main_observability import MainModuleHarness, _Headers
from tests.test_main_turnstile import main as real_main
from tests.test_main_turnstile import make_request, session_env

ROOT = Path(__file__).resolve().parents[1]


def run_in_harness(code: str):
    """Execute the generated Dynamic Worker module the way the sandbox does."""
    saved = sys.modules.get("workers")
    fake = types.ModuleType("workers")

    class Response:
        def __init__(self, body, status=200, headers=None):
            self.body, self.status, self.headers = body, status, headers or {}

    fake.Response = Response
    fake.WorkerEntrypoint = object
    sys.modules["workers"] = fake
    try:
        namespace = {}
        exec(compile(build_dynamic_worker_code(code), "/session/runner.py", "exec"), namespace)  # noqa: S102
        return asyncio.run(namespace["Default"]().fetch(None))
    finally:
        if saved is None:
            sys.modules.pop("workers", None)
        else:
            sys.modules["workers"] = saved


class LearnerRunOutputTests(unittest.TestCase):
    def test_traceback_shows_only_the_learners_frames_with_source_lines(self):
        response = run_in_harness('print("before")\ndef divide(x):\n    return 1 / x\ndivide(0)\n')
        self.assertEqual(response.status, 500)
        self.assertTrue(response.body.startswith("before\nTraceback (most recent call last):\n"))
        self.assertIn('File "example.py", line 4, in <module>\n    divide(0)', response.body)
        self.assertIn('File "example.py", line 3, in divide\n    return 1 / x', response.body)
        self.assertTrue(response.body.rstrip().endswith("ZeroDivisionError: division by zero"))
        self.assertNotIn("runner.py", response.body)
        self.assertNotIn("exec(", response.body)

    def test_chained_exceptions_hide_harness_frames_too(self):
        response = run_in_harness(
            "try:\n    1 / 0\nexcept ZeroDivisionError as error:\n    raise ValueError('bad') from error\n"
        )
        self.assertIn("direct cause", response.body)
        self.assertNotIn("runner.py", response.body)

    def test_syntax_error_points_at_the_learners_line(self):
        response = run_in_harness("def broken(:\n    pass\n")
        self.assertEqual(response.status, 500)
        self.assertIn('File "example.py", line 1', response.body)
        self.assertIn("SyntaxError", response.body)
        self.assertNotIn("runner.py", response.body)

    def test_exit_ends_the_program_instead_of_failing_the_request(self):
        for code, expected in (
            ('print("done")\nexit()', "done\n"),
            ('import sys\nprint("done")\nsys.exit(0)', "done\n"),
            ("exit(3)", "[exited with status 3]\n"),
            ('import sys\nsys.exit("stopping early")', "stopping early\n"),
        ):
            with self.subTest(code=code):
                response = run_in_harness(code)
                self.assertEqual(response.status, 200)
                self.assertEqual(response.body, expected)

    def test_stderr_is_shown_in_program_order(self):
        response = run_in_harness('import sys\nprint("one")\nprint("two", file=sys.stderr)\nprint("three")\n')
        self.assertEqual((response.status, response.body), (200, "one\ntwo\nthree\n"))

    def test_input_explains_that_there_is_no_terminal(self):
        response = run_in_harness('name = input("Name? ")\n')
        self.assertEqual(response.status, 500)
        self.assertIn(f"EOFError: {INPUT_UNAVAILABLE_MESSAGE}", response.body)
        self.assertNotIn("_no_input", response.body)

    def test_sandbox_limited_pages_explain_the_limit(self):
        note = sandbox_limit_note(get_example("networking"))
        self.assertIn("sockets", note)
        self.assertIn("sandbox", note)
        self.assertEqual(sandbox_limit_note(get_example("values")), "")
        limited = {example["slug"] for example in list_examples() if example.get("sandbox_limit")}
        self.assertEqual(limited, {"virtual-environments", "subprocesses", "threads-and-processes", "networking"})


class RenderedProseTests(unittest.TestCase):
    def test_every_intro_paragraph_reaches_the_page(self):
        for example in list_examples():
            page = render_example_page(example)
            self.assertIn('<div class="example-explanation">', page, example["slug"])
            self.assertEqual(
                page.count("<p>", page.index('<div class="example-explanation">'), page.index("</section>", page.index('<div class="example-explanation">'))),
                len(example["explanation"]),
                example["slug"],
            )
        closures = render_example_page(get_example("closures"))
        self.assertIn("A closure is a function that remembers names from the scope where it was created.", closures)

    def test_journey_pages_render_inline_code_instead_of_backticks(self):
        for journey in JOURNEYS:
            page = render_journey_page(journey)
            self.assertNotIn("`", page.split("<main", 1)[1].split("</main>", 1)[0], journey["slug"])

    def test_figures_carry_their_intrinsic_width_for_the_phone_layout(self):
        banner = render_banner("values", "after-cell-0") or render_banner("values", "before")
        self.assertRegex(banner, r'<svg [^>]*width="(\d+)" [^>]*style="--fig-w: \1px"')
        css = (ROOT / "public" / "site.css").read_text()
        self.assertIn("var(--fig-w", css)


class MachineReadableSurfaceTests(unittest.TestCase):
    def test_llms_txt_links_every_example_as_markdown(self):
        text = render_llms_txt()
        for example in list_examples():
            self.assertIn(f"/examples/{example['slug']}.md): {example['summary']}", text)
        for journey in JOURNEYS:
            self.assertIn(f"/journeys/{journey['slug']})", text)

    def test_markdown_endpoint_serves_the_authored_source(self):
        self.assertEqual(
            example_markdown("closures"), (ROOT / "src" / "example_sources" / "closures.md").read_text()
        )
        self.assertIsNone(example_markdown("no-such-example"))
        self.assertIsNone(example_markdown("manifest"))
        response = asyncio.run(real_main.example_page("closures.md", make_request()))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.headers["content-type"].startswith("text/markdown"))
        self.assertEqual(asyncio.run(real_main.example_page("nope.md", make_request())).status_code, 404)

    def test_search_index_covers_prose_code_and_everyday_words(self):
        entries = {entry["slug"]: entry for entry in json.loads((ROOT / "public" / "search-index.json").read_text())}
        self.assertEqual(set(entries), {example["slug"] for example in list_examples()})
        self.assertIn("dictionary", entries["dicts"]["keywords"].split())
        self.assertIn("mutable", entries["mutability"]["keywords"].split())
        self.assertIn("remembers", entries["closures"]["text"].split())  # intro prose
        self.assertIn("make_multiplier", entries["closures"]["text"].split())  # code


class TrailingSlashTests(unittest.TestCase):
    def test_trailing_slash_redirects_to_the_canonical_path_and_keeps_the_query(self):
        request = SimpleNamespace(url=SimpleNamespace(query="ref=feed"))
        response = asyncio.run(real_main.not_found("examples/values/", request))
        self.assertEqual(response.status_code, 308)
        self.assertEqual(response.headers["location"], "/examples/values?ref=feed")
        bare = asyncio.run(real_main.not_found("journeys/", SimpleNamespace(url=SimpleNamespace(query=""))))
        self.assertEqual(bare.headers["location"], "/journeys")


class ClearanceBindingTests(unittest.TestCase):
    def test_clearance_is_only_accepted_from_the_address_that_earned_it(self):
        env = session_env()
        expires = int(time.time()) + 600
        cookie = real_main._sign_clearance("clearance-secret", expires, "203.0.113.7")
        same = make_request(cookie=cookie, headers={"CF-Connecting-IP": "203.0.113.7"}, env=env)
        other = make_request(cookie=cookie, headers={"CF-Connecting-IP": "198.51.100.9"}, env=env)
        self.assertTrue(real_main._clearance_valid(same))
        self.assertFalse(real_main._clearance_valid(other))
        self.assertFalse(real_main._clearance_valid(make_request(cookie=cookie, env=env)))


class HeadAndCacheTests(MainModuleHarness):
    def _worker(self, main, response):
        seen = []

        async def asgi_fetch(app, request, *args, **kwargs):
            seen.append(request)
            return response

        main.asgi.fetch = asgi_fetch
        main.observability.event_from_worker_request = lambda *args, **kwargs: {"cache": "bypass"}
        main.observability.emit = lambda value, env=None: None
        main.JsRequest = SimpleNamespace(new=lambda source, init=None: SimpleNamespace(source=source, **(init or {})))
        main.JsResponse = SimpleNamespace(
            new=lambda body, init: SimpleNamespace(
                body=body,
                status=init["status"] if isinstance(init, dict) else init.status,
                headers=_Headers(init["headers"] if isinstance(init, dict) else init.headers),
            )
        )
        main.jsnull = None
        worker = main.Default()
        worker.env = SimpleNamespace()
        return worker, seen

    def test_head_is_answered_from_the_get_representation_without_a_body(self):
        main = self.import_main()
        main.caches = None
        response = SimpleNamespace(status=200, headers=_Headers({"Content-Type": "text/html; charset=utf-8"}), body="<html>")
        worker, seen = self._worker(main, response)
        request = SimpleNamespace(method="HEAD", url="https://www.pythonbyexample.dev/examples/values", js_object=SimpleNamespace())
        returned = asyncio.run(worker.fetch(request))
        self.assertEqual(seen[0].method, "GET")
        self.assertEqual(returned.status, 200)
        self.assertIsNone(returned.body)
        self.assertEqual(returned.headers["Content-Type"], "text/html; charset=utf-8")

    def test_cache_hits_leave_with_the_intended_browser_lifetime(self):
        main = self.import_main()
        cached = SimpleNamespace(status=200, headers=_Headers({"Cache-Control": "public, max-age=14400"}), body="<html>")

        async def match(key):
            return cached

        main.caches = SimpleNamespace(default=SimpleNamespace(match=match))
        worker, seen = self._worker(main, None)
        request = SimpleNamespace(method="GET", url="https://www.pythonbyexample.dev/examples/values", js_object=SimpleNamespace())
        returned = asyncio.run(worker.fetch(request))
        self.assertEqual(seen, [])
        self.assertEqual(returned.headers["Cache-Control"], main.HTML_CACHE_CONTROL)
        self.assertEqual(cached.headers["Cache-Control"], "public, max-age=14400")


if __name__ == "__main__":
    unittest.main()
