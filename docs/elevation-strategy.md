# Website elevation strategy

Drafted 2026-07-10. Status: proposal.

This document answers one question: how do we make Python By Example
more successful without disrupting its essence? It builds on
`docs/rubric-saturation.md` (internal quality has plateaued at a high
level), `docs/learner-analytics.md` (the external signal we can already
measure), and `docs/research-similar-sites.md` (the competitive
landscape).

## The essence (what must not change)

Everything below is the product. Elevation work that erodes any of it
is a regression, whatever it does for traffic.

- **One concept per page.** Compact literate walkthroughs: prose beside
  the source it explains, output evidence beside the source that
  produced it.
- **Everything runs.** The complete program is editable and executes in
  an isolated Dynamic Worker. Expected output is verified, not claimed.
- **Anchored to authority.** Every page links the official Python docs
  for the current Cloudflare-supported Python version.
- **Low chrome, article-like.** Not a notebook, not a course, not a
  reference dump. Reading order and quiet layout are features.
- **Curated craft.** The locked figure grammar, quality rubrics,
  registries, and contract tests are the moat. Nothing ships below the
  gates.
- **Respectful by default.** No accounts, no ads, privacy-safe wide
  events only.

## Where the project stands

The last two improvement rounds made the inside excellent: 109
examples all above the quality gate, 100% figure coverage with a mean
rubric score ≈ 8.7 and nothing below 8.0, journeys with outcome
contracts, zero orphaned examples, and a green steady state that
`docs/lessons-learned.md` explicitly warns against inflating further.
SEO metadata, structured data, sitemap, social cards, dark mode, search,
and learner analytics all landed in the previous elevation pass.

The constraint has therefore moved. Page quality is no longer what
limits success; **reach, engagement depth, and coverage of what
learners actually look for** are. `docs/lessons-learned.md` already
points the way: steer content work by external signal rather than
internal quality scores.

## What "more successful" means

A shared scorecard, so "success" is not vibes. Everything below is
measurable with the existing wide events plus `scripts/learner_report.py`
and a search-console account.

1. **Reach** — unique learners per week on example pages; search
   impressions and clicks.
2. **Engagement** — POST runs per week; edited-run share (the ideal
   documented in `docs/learner-analytics.md`: high edited share, low
   error share); journey traffic.
3. **Return** — repeat visits per week (approximate is fine; no
   accounts).
4. **Authority** — inbound links, listings in "learn Python"
   collections, and citations by AI assistants.
5. **Demand conversion** — recurring `/examples/` 404s turned into
   shipped pages.

## Thrust 1 — Close the demand loop

The instrumentation exists; the ritual does not. The wide events
already record which pages are read, which examples are run and
edited, where edited code errors, and which nonexistent example URLs
are requested. Make consuming that signal a habit:

- Schedule a Workers Logs export (Logpush or a periodic dashboard
  export) and run `scripts/learner_report.py` on a weekly cadence.
- Treat recurring missing-example 404s as the top of the content
  backlog — the docs already call this "the strongest possible signal
  for what to write next."
- Treat high error-share pages as walkthrough gaps: learners tried
  something the page did not prepare them for. Extend the cells or
  notes there.
- Register the sitemap with Google Search Console and Bing Webmaster
  Tools (if not already done) and fold query/impression data into the
  same weekly look. Queries that show impressions without clicks are
  title/summary problems; queries with no impressions are coverage
  problems.

## Thrust 2 — Cover what learners actually search for, without sprawl

The catalog is deep on language semantics (Types 14, Data Model 12,
Basics 12, Functions 11, Collections 11) and comparatively light on the
task-shaped standard-library surfaces that dominate real Python search
demand (Standard Library 9, Text 3, Async 2). Go By Example's
most-linked pages are exactly the task-shaped ones: reading and
writing files, command-line arguments, environment variables. We have
no file-I/O or pathlib page today.

Candidate additions — each still one mechanism per page, each through
the same rubric gates:

- **Files and paths**: reading/writing text files, `pathlib`. Pyodide's
  in-memory filesystem makes these genuinely runnable in the Dynamic
  Worker — a live advantage over static competitors.
- **Process environment**: environment variables; command-line
  arguments (`argparse`'s smallest loop). Both fit the proven
  runtime-boundary framing already used by `networking` and
  `subprocesses`: teach normal Python first, state the sandbox
  constraint once.
- **Everyday stdlib**: `random`, `time`/`perf_counter`, `math` and
  `statistics`, `hashlib`, `tempfile`, `functools` beyond
  `partial` (`lru_cache`, `reduce`), `textwrap`.

Filter and order this list by the 404 demand from Thrust 1 rather than
shipping it wholesale; cap the pace at what can clear the 9.0 gate.
The scope boundary should be stated once and kept: **language plus
standard library**. Third-party frameworks (pandas, Django, FastAPI)
are off-essence.

Separately, sharpen how the existing contrast work meets search
intent. The confusable-pair contrasts already reach visitors: every
owner page is a public example, all of them appear in journey
sections, roughly half the pairs are stated in visitor-facing journey
text (e.g. "distinguish value equality from object identity"), and
iterator vs iterable has a dedicated page. What does not exist is a
surface shaped like the search query: no page enumerates the pairs,
and the registry itself is read only at build time. A small "X vs Y"
contrasts index — generated from the registry, linking to the owning
pages — would target those high-intent queries directly instead of
leaving each contrast mid-page where only an on-page reader finds it.

## Thrust 3 — Deepen the on-page loop

Small affordances, all quiet enough to preserve the low-chrome feel,
all aimed at the scorecard's engagement and return lines:

- **Share this code.** `example.html` already restores code from a
  `#code=` base64 fragment on load, but nothing ever writes one. Add a
  "copy link to this code" affordance near the runner so every
  experiment becomes a shareable artifact. Half the mechanism is
  already built; the missing half is a distribution channel.
- **Copy buttons on code blocks.** Learners copy code constantly;
  making them select text by hand is friction with no editorial value.
- **"Try it" nudges.** A one-line micro-challenge near the runner
  ("change X to Y — predict the output before running") directly
  targets the edited-share-up, error-share-down ideal. Start as a
  notes convention or an optional block on the ten most-run pages and
  measure whether edited share moves.
- **Example → journey orientation.** Journey pages link examples, but
  example pages never mention the journeys they belong to. A one-line
  "Part of the Iteration journey" link closes that edge of the graph
  and gives a learner who landed from search a curated next step
  beyond prev/next.
- **Keyboard prev/next** (`←`/`→`) to reinforce the tour feel.
- **Local progress marks.** A localStorage-only check on examples a
  learner has read or run, rendered as a quiet dot on home cards and
  journey lists. No accounts, no server state — but journeys gain a
  sense of completion, which is the cheapest honest return-visit
  mechanic available.

## Thrust 4 — Earn distribution

- **Publish the method.** An `/about` (or colophon) page telling the
  editorial story: literate cells with verified output, the locked
  figure grammar, geometry contract tests, quality gates. The `docs/`
  folder is already public-grade; no competitor has this story, and it
  is exactly the trust signal search engines and human referrers
  reward.
- **Be citable by machines.** Publish `/llms.txt` and per-example
  Markdown endpoints (`/examples/<slug>.md`). The sources are already
  Markdown, and `docs/lessons-learned.md` already requires teaching
  artifacts to be clean enough to serve as public material. AI
  assistants are now a first-class referrer of learners; being the
  cleanest citable source for "Python by example" queries is cheap and
  fully on-essence.
- **Feeds.** An Atom feed of new and substantially revised examples so
  newsletters and aggregators can pick up changes without watching the
  repo.
- **Edit this page on GitHub.** A per-example source link converts
  readers into contributors (CONTRIBUTING and issue templates already
  exist) and is a further trust signal.
- **Launch moments.** The site has never had one. Milestone-shaped
  posts — Show HN, r/Python, Python Weekly, an awesome-python listing
  PR — with the runnable-literate angle as the hook. Sequence these
  *after* the quick loop-deepening wins so spike traffic lands on the
  sharpest version of the page.
- **Stay current as an event.** When Cloudflare's Python Workers
  runtime moves past 3.13, migrate fast (the tooling exists:
  `make verify-python-version`) and ship a small "new in this Python,
  by example" set. Version currency is a recurring, newsworthy proof
  that the site is alive — most competitor catalogs visibly rot.

## Guardrails — what we will not do

- No accounts, no ads, no comments, no gamification beyond quiet local
  progress marks.
- No third-party framework or library tutorials; the boundary is the
  language and its standard library.
- No course-ification; journeys remain curated arcs over the same
  example pages.
- No content that bypasses the gates: every new page passes the same
  rubric, formatter, parity, and verified-output checks regardless of
  how fast we want to grow.
- No chrome creep: share, copy, progress, and breadcrumb affordances
  must stay visually quiet. The reading experience is the product.

## Sequencing

**Now (days; mostly small, single-surface changes)**

1. Share-this-code link + copy buttons on code blocks.
   *(Both shipped 2026-07-10.)*
2. `/about` page + edit-on-GitHub links.
   *(`/about` shipped 2026-07-10; edit-on-GitHub links are still open.)*
3. `/llms.txt`, per-example Markdown endpoints, Atom feed.
4. Search-console registration + the first weekly learner-report
   ritual. *(Google Search Console ownership verified 2026-07-10;
   sitemap submission waits on the next deploy.)*

**Next (weeks)**

5. First demand-driven stdlib tranche: files/pathlib, environment
   variables, command-line arguments, `random`, `time` — ordered by
   observed 404s, gated by the rubric.
6. Example → journey breadcrumbs; keyboard prev/next.
   *(Keyboard prev/next shipped 2026-07-10; breadcrumbs are still
   open.)*
7. "X vs Y" contrasts index from the confusable-pair registry.
8. "Try it" nudges on the ten most-run pages; measure edited share.
9. First launch moment, once 1–3 are live.

**Horizon (quarter-plus)**

10. Local journey progress marks.
11. Python version migration moment (runtime-dependent) plus a
    what's-new example set.
12. Translations — only with a sustainable community model, never
    machine-dumped.
13. Embeddable example widget for blogs — only if inbound demand
    appears.

## Risks

- **Distribution before sharpening wastes the spike.** A Show HN that
  lands on pages without share/copy affordances converts one visit
  into zero artifacts. Sequence quick wins first.
- **Stdlib expansion drifts into reference sprawl.** The 404-demand
  filter, the one-mechanism-per-page rule, and the broad-surface-title
  lesson in `docs/lessons-learned.md` are the existing defenses; keep
  them binding.
- **The analytics ritual decays.** Keep it one command and one short
  dated summary; if it takes an hour it will stop happening.
- **Runner cost or abuse under spike traffic.** Turnstile protection
  and the smoke bypass already exist; watch turnstile outcomes in the
  weekly report during launch weeks.
