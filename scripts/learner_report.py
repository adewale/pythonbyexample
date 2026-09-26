#!/usr/bin/env python3
"""Aggregate exported Worker wide events into a learner-behavior report.

The Worker already emits one structured event per request (see
docs/observability-spec.md). This script turns an export of those events
into the numbers that should steer content work: which examples people
read, which they actually run, where edited code fails, and which
example URLs 404 (demand for pages that do not exist yet).

Input is newline-delimited JSON on stdin or from file arguments. Three
shapes are accepted per line and detected automatically:

- the raw wide-event payload (one JSON object per line)
- a `wrangler tail --format json` envelope (events inside logs[].message[])
- a Workers Logs / Logpush envelope (event inside $workers)

Usage:
    wrangler tail --format json | scripts/learner_report.py
    scripts/learner_report.py exported-logs.ndjson
    scripts/learner_report.py --json exported-logs.ndjson
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from collections.abc import Iterable, Iterator
from typing import TextIO

SERVICE = "pythonbyexample"

# Turnstile signals that mean the deployment is misconfigured rather than that
# a visitor failed: every challenged run fails until an operator fixes them.
TURNSTILE_CONFIG_ALERTS = {
    "reason:site_key_missing": "TURNSTILE_SITE_KEY is not configured, so challenges cannot render",
    "code:missing-input-secret": "Siteverify received no secret",
    "code:invalid-input-secret": "TURNSTILE_SECRET_KEY is wrong, rotated, or from another widget",
}


def _looks_like_wide_event(value) -> bool:
    return isinstance(value, dict) and value.get("service") == SERVICE and "path" in value


def _events_from_record(record) -> Iterator[dict]:
    if _looks_like_wide_event(record):
        yield record
        return
    if not isinstance(record, dict):
        return
    workers = record.get("$workers")
    if isinstance(workers, dict):
        event = workers.get("event", workers)
        if _looks_like_wide_event(event):
            yield event
            return
    for log in record.get("logs", []) or []:
        if not isinstance(log, dict):
            continue
        for message in log.get("message", []) or []:
            if _looks_like_wide_event(message):
                yield message


def iter_events(stream: TextIO) -> Iterator[dict]:
    for line in stream:
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except ValueError:
            continue
        yield from _events_from_record(record)


def _percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round(fraction * (len(ordered) - 1))))
    return ordered[index]


def aggregate_events(events: Iterable[dict]) -> dict:
    totals = Counter()
    page_views: Counter[str] = Counter()
    journey_views: Counter[str] = Counter()
    missing_example_paths: Counter[str] = Counter()
    turnstile_outcomes: Counter[str] = Counter()
    turnstile_failure_reasons: Counter[str] = Counter()
    turnstile_error_codes: Counter[str] = Counter()
    runs: dict[str, dict] = defaultdict(
        lambda: {"total": 0, "edited": 0, "errors": 0, "execution_ms": []}
    )

    for event in events:
        totals["events"] += 1
        method = str(event.get("method", "")).upper()
        path = str(event.get("path", ""))
        status = event.get("status_code", 0)

        if method == "GET":
            if path.startswith("/examples/") and status == 404:
                missing_example_paths[path] += 1
            elif status == 200:
                page_views[path] += 1
                if path.startswith("/journeys"):
                    journey_views[path] += 1

        example = event.get("example")
        if method == "POST" and isinstance(example, dict) and example.get("slug"):
            slug = str(example["slug"])
            entry = runs[slug]
            entry["total"] += 1
            if example.get("code_edited"):
                entry["edited"] += 1
            if event.get("outcome") == "error":
                entry["errors"] += 1
            execution_ms = event.get("execution_ms")
            if isinstance(execution_ms, (int, float)):
                entry["execution_ms"].append(float(execution_ms))

        turnstile = event.get("turnstile")
        if isinstance(turnstile, dict) and turnstile.get("outcome"):
            turnstile_outcomes[str(turnstile["outcome"])] += 1
            if turnstile.get("reason"):
                turnstile_failure_reasons[str(turnstile["reason"])] += 1
            error_codes = turnstile.get("error_codes")
            if isinstance(error_codes, list):
                turnstile_error_codes.update(str(code) for code in error_codes)

    run_summary = {}
    for slug, entry in runs.items():
        timings = entry.pop("execution_ms")
        summary = dict(entry)
        if timings:
            summary["execution_ms_p50"] = _percentile(timings, 0.5)
            summary["execution_ms_p95"] = _percentile(timings, 0.95)
            summary["execution_ms_max"] = max(timings)
        run_summary[slug] = summary

    return {
        "totals": dict(totals),
        "page_views": dict(page_views),
        "journey_views": dict(journey_views),
        "missing_example_paths": dict(missing_example_paths),
        "turnstile_outcomes": dict(turnstile_outcomes),
        "turnstile_failure_reasons": dict(turnstile_failure_reasons),
        "turnstile_error_codes": dict(turnstile_error_codes),
        "turnstile_config_alerts": _turnstile_config_alerts(turnstile_failure_reasons, turnstile_error_codes),
        "runs": run_summary,
    }


def _turnstile_config_alerts(reasons: Counter[str], error_codes: Counter[str]) -> dict[str, int]:
    signals = Counter({f"reason:{key}": count for key, count in reasons.items()})
    signals.update({f"code:{key}": count for key, count in error_codes.items()})
    return {signal: signals[signal] for signal in TURNSTILE_CONFIG_ALERTS if signals[signal]}


def _top(counter: dict, limit: int) -> list[tuple[str, int]]:
    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:limit]


def render_report(report: dict, limit: int = 15) -> str:
    lines = []
    lines.append(f"Learner report over {report['totals'].get('events', 0)} events")
    lines.append("")

    lines.append(f"Most-read pages (top {limit})")
    for path, count in _top(report["page_views"], limit):
        lines.append(f"  {count:>6}  {path}")
    lines.append("")

    lines.append(f"Most-run examples (top {limit})")
    ranked_runs = sorted(report["runs"].items(), key=lambda item: (-item[1]["total"], item[0]))[:limit]
    for slug, entry in ranked_runs:
        edited_share = entry["edited"] / entry["total"] if entry["total"] else 0.0
        error_share = entry["errors"] / entry["total"] if entry["total"] else 0.0
        timing = ""
        if "execution_ms_p50" in entry:
            timing = f"  p50 {entry['execution_ms_p50']:.0f}ms p95 {entry['execution_ms_p95']:.0f}ms"
        lines.append(
            f"  {entry['total']:>6}  {slug}  ({edited_share:.0%} edited, {error_share:.0%} errors){timing}"
        )
    lines.append("")

    if report["journey_views"]:
        lines.append("Journey traffic")
        for path, count in _top(report["journey_views"], limit):
            lines.append(f"  {count:>6}  {path}")
        lines.append("")

    lines.append("Missing-example requests (404s under /examples/ — demand for pages that do not exist)")
    missing = _top(report["missing_example_paths"], limit)
    if missing:
        for path, count in missing:
            lines.append(f"  {count:>6}  {path}")
    else:
        lines.append("  none")
    lines.append("")

    if report["turnstile_outcomes"]:
        lines.append("Turnstile outcomes")
        for outcome, count in _top(report["turnstile_outcomes"], limit):
            lines.append(f"  {count:>6}  {outcome}")
        lines.append("")

    if report["turnstile_failure_reasons"]:
        lines.append("Turnstile failure reasons")
        for reason, count in _top(report["turnstile_failure_reasons"], limit):
            lines.append(f"  {count:>6}  {reason}")
        lines.append("")

    if report["turnstile_error_codes"]:
        lines.append("Siteverify error codes")
        for code, count in _top(report["turnstile_error_codes"], limit):
            lines.append(f"  {count:>6}  {code}")
        lines.append("")

    if report["turnstile_config_alerts"]:
        lines.append("Turnstile configuration alerts (fix the deployment; these are not bot failures)")
        for signal, count in _top(report["turnstile_config_alerts"], limit):
            lines.append(f"  {count:>6}  {signal}: {TURNSTILE_CONFIG_ALERTS[signal]}")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", help="NDJSON log exports; reads stdin when omitted")
    parser.add_argument("--json", action="store_true", help="emit the aggregated report as JSON")
    parser.add_argument("--limit", type=int, default=15, help="rows per section in the text report")
    args = parser.parse_args()

    events: list[dict] = []
    if args.files:
        for name in args.files:
            with open(name, encoding="utf-8") as handle:
                events.extend(iter_events(handle))
    else:
        events.extend(iter_events(sys.stdin))

    report = aggregate_events(events)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_report(report, limit=args.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
