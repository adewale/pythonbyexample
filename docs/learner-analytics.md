# Learner analytics

The Worker emits one structured wide event per request (see
`docs/observability-spec.md`). Those events carry the page path, the
example slug on POST runs, whether submitted code differed from the
example, the Dynamic Worker outcome, and execution time.

`scripts/learner_report.py` aggregates those events into an
**operational interaction scorecard**. It does not identify people,
deduplicate visits, measure comprehension, or prove that a content
change caused learning. Every row is a request count within the export's
time window:

- **Most-requested pages** — successful GET requests per path, including
  repeat requests and possible automated traffic.
- **Most-run examples** — accepted POST attempts per slug, with edited,
  error, and p50/p95 execution-time distributions. "Edited" means only
  that submitted code differed; it is not evidence of successful learning.
- **Journey requests** — GET request volume for curated-arc routes.
- **Missing-example requests** — 404s under `/examples/`. Recurring,
  human-validated paths may suggest content candidates, but typos, scanners,
  and bots are confounders.
- **Turnstile outcomes** — challenge and rejection counts used to monitor
  runner availability and abuse controls, not learner quality.

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

## Reading the scorecard

Use the report as a queue for investigation, not as a composite score or
a learning-outcome dashboard. Record the export interval and absolute
sample size, compare equivalent time windows, and inspect paths or code
patterns before changing content.

- A high **edited share** can justify reviewing an example for useful
  extension points. Pair it with error samples and direct learner feedback.
- A high **error share** can indicate unclear teaching, intentionally invalid
  experiments, abuse, or runtime trouble. Diagnose those alternatives first.
- Recurring **missing-example requests** are candidates only after filtering
  obvious automation and validating the intended topic.
- Do not rank authors or examples by one ratio, and do not claim learning
  improvement without a separate outcome measure and an appropriate study.
