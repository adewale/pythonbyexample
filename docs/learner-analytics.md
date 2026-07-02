# Learner analytics

The Worker emits one structured wide event per request (see
`docs/observability-spec.md`). Those events already carry the fields
that matter for content decisions: the page path, the example slug on
POST runs, whether the submitted code was edited, the Dynamic Worker
outcome, and the execution time.

`scripts/learner_report.py` turns an export of those events into a
learner-behavior report so content work is steered by external signal
rather than internal quality scores:

- **Most-read pages** — GET traffic per path.
- **Most-run examples** — POST runs per slug, with the edited share
  (are people experimenting or just pressing Run?), the error share
  (where edited code fails), and p50/p95 execution times.
- **Journey traffic** — which curated arcs get used.
- **Missing-example requests** — 404s under `/examples/`, i.e. demand
  for pages that do not exist yet. These are content candidates.
- **Turnstile outcomes** — how often runs are challenged or blocked.

## Getting events

Live tail (short windows; see the `wrangler tail` caveats in
`docs/lessons-learned.md`):

```bash
uv run --group workers pywrangler tail --format json > events.ndjson
scripts/learner_report.py events.ndjson
```

Or export from the Cloudflare dashboard (Workers Logs) / a Logpush job
and feed the NDJSON file in the same way. The script auto-detects the
raw payload, the `wrangler tail` envelope, and the Workers Logs
envelope, so exports from any of the three sources work unmodified.

`--json` emits the aggregated report as JSON for further processing;
`--limit N` controls rows per section.

## Reading the report

- A high **edited share** with a low error share means the example
  invites successful experimentation — the ideal.
- A high **error share** on edited runs marks pages where learners try
  something the example did not prepare them for; consider extending
  the walkthrough or notes there.
- **Missing-example requests** that recur are the strongest possible
  signal for what to write next.
