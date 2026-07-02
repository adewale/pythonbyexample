import io
import json
import unittest

from scripts.learner_report import aggregate_events, iter_events, render_report


def raw(event):
    return json.dumps(event)


def tail_envelope(event):
    return json.dumps({"outcome": "ok", "logs": [{"message": [event], "level": "log"}]})


def workers_logs_envelope(event):
    return json.dumps({"$workers": {"event": event}, "$metadata": {"id": "abc"}})


def page_view(path, status=200, cache="hit"):
    return {
        "service": "pythonbyexample",
        "method": "GET",
        "path": path,
        "cache": cache,
        "status_code": status,
        "outcome": "success" if status < 400 else ("client_error" if status < 500 else "error"),
        "duration_ms": 12.0,
    }


def example_run(slug, edited=False, execution_ms=250.0, outcome="success"):
    return {
        "service": "pythonbyexample",
        "method": "POST",
        "path": f"/examples/{slug}",
        "cache": "bypass",
        "status_code": 200 if outcome == "success" else 500,
        "outcome": outcome,
        "execution_ms": execution_ms,
        "example": {"slug": slug, "code_edited": edited, "code_hash": "abc", "code_bytes": 100},
        "turnstile": {"outcome": "not_required"},
    }


class IterEventsTests(unittest.TestCase):
    def test_reads_raw_tail_and_workers_logs_lines(self):
        lines = [
            raw(page_view("/examples/closures")),
            tail_envelope(example_run("closures")),
            workers_logs_envelope(page_view("/journeys/iteration")),
            "not json at all",
            json.dumps({"unrelated": True}),
        ]
        events = list(iter_events(io.StringIO("\n".join(lines))))
        self.assertEqual(len(events), 3)
        self.assertEqual(events[0]["path"], "/examples/closures")
        self.assertEqual(events[1]["example"]["slug"], "closures")
        self.assertEqual(events[2]["path"], "/journeys/iteration")


class AggregateTests(unittest.TestCase):
    def build_report(self):
        events = [
            page_view("/"),
            page_view("/examples/closures"),
            page_view("/examples/closures", cache="miss"),
            page_view("/examples/decorators"),
            page_view("/examples/not-a-real-example", status=404),
            page_view("/journeys/iteration"),
            example_run("closures", edited=False, execution_ms=100.0),
            example_run("closures", edited=True, execution_ms=300.0),
            example_run("closures", edited=True, execution_ms=500.0, outcome="error"),
            example_run("decorators", edited=False, execution_ms=200.0),
        ]
        return aggregate_events(events)

    def test_aggregates_page_views_runs_and_gaps(self):
        report = self.build_report()
        self.assertEqual(report["totals"]["events"], 10)
        self.assertEqual(report["page_views"]["/examples/closures"], 2)
        self.assertEqual(report["runs"]["closures"]["total"], 3)
        self.assertEqual(report["runs"]["closures"]["edited"], 2)
        self.assertEqual(report["runs"]["closures"]["errors"], 1)
        self.assertEqual(report["runs"]["decorators"]["total"], 1)
        self.assertEqual(report["journey_views"]["/journeys/iteration"], 1)
        self.assertEqual(report["missing_example_paths"]["/examples/not-a-real-example"], 1)

    def test_execution_percentiles_per_slug(self):
        report = self.build_report()
        closures = report["runs"]["closures"]
        self.assertEqual(closures["execution_ms_p50"], 300.0)
        self.assertEqual(closures["execution_ms_max"], 500.0)

    def test_render_report_is_readable(self):
        text = render_report(self.build_report())
        self.assertIn("Most-run examples", text)
        self.assertIn("closures", text)
        self.assertIn("Missing-example requests", text)
        self.assertIn("/examples/not-a-real-example", text)


if __name__ == "__main__":
    unittest.main()
