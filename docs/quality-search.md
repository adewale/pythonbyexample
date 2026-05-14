# Rubric-driven quality search

Python By Example now has two complementary scoring loops:

1. `scripts/check_quality_scores.py` is the editorial gate. It enforces the curated score registry, hard-minimum waivers, stale backlog cleanup, weak journey-section tracking, and the 10-point rubric weight model.
2. `scripts/score_example_criteria.py` is the search aid. It breaks each page into rubric criteria so rewrite work can target the weakest axis instead of treating the score as one opaque number.

The criterion report is deliberately heuristic. It should suggest candidates, not replace editorial review.

## Hill-climbing move types

Use these moves when a page is already close and the weakest criterion is clear:

- **Decompose one compressed cell** into setup, boundary, and payoff cells.
- **Add a before/after contrast** when the feature exists to remove boilerplate or clarify a shape.
- **Add a runtime/static boundary cell** for typing pages where runtime behavior differs from type-checker behavior.
- **Add a failure/recovery cell** for parsing, exceptions, warnings, and validation examples.
- **Add a standard-Python/runner-boundary unsupported cell** for runtime features constrained by this site's live example runner.
- **Strengthen graph edges** with prerequisite, neighboring, and next-depth `see_also` links.
- **Replace generic prose** with a concrete domain pressure: user input, package setup, protocol bytes, record shape, service logging, or state transition.

## Escaping local maxima with simulated annealing

Greedy hill-climbing tends to overfit the current page shape: it adds one more note or one more small cell even when the page needs a different structure. For pages stuck around 8.2-8.8, use a simulated-annealing review loop:

1. **State**: the page markdown plus metadata, figure rationale, and graph edges.
2. **Energy**: `10 - curated_score`, with penalties for weak criterion scores, unsupported runtime ambiguity, graph isolation, empty output evidence, and overlong code runs.
3. **Neighbor moves**:
   - split a cell;
   - merge two repetitive cells;
   - swap the first example domain;
   - introduce a contrasting failure case;
   - move from toy data to realistic data;
   - convert a figure requirement into a no-figure rationale when the page is constraint-shaped;
   - add/remove a `see_also` edge;
   - rewrite the intro around “when to use this”.
4. **Temperature**: start high enough to accept occasional worse rewrites, especially when they introduce a new structure. Cool after tests, verification, and rubric review pass.
5. **Acceptance rule**: accept improvements always; accept a worse intermediate with probability based on score loss and temperature only if executable correctness and docs links remain valid.
6. **Refinement**: after cooling, run `make verify`, the criterion report, and a manual rubric pass before updating the curated score.

This gives the project permission to try non-local changes — different domains, different cell order, or a no-figure rationale — without normalizing failed experiments into production.

## Techniques learned from the bottom-28 pass

The low-score pages mostly needed the same repair pattern rather than more prose:

- **Name the boundary in the page graph.** Pages that were otherwise good still looked weak when they had no prerequisite/neighbor/next-depth `see_also` edges. Adding edges made the intended learning path inspectable.
- **Use a three-cell spine.** Strong pages usually have setup, contrast/boundary, and payoff evidence. One compressed cell hides too many teaching jobs.
- **Show the neighboring tool.** `for` vs `while`, `lambda` vs `def`, `list` vs `set`, `None` vs exception/default, and eager vs lazy examples score better because learners see when not to use the feature.
- **Keep runtime/static distinctions explicit.** Typing pages improved when a cell showed the runtime caveat instead of leaving the type-checker promise implicit.
- **Let criterion scoring detect stale editorial labels.** Several pages had already gained cells, notes, and graph edges, but the curated comment still said `isolated`. The criterion report is useful for finding those stale labels.

## Wider-system unlocks

Future improvements that create new quality headroom:

- Store criterion-level editorial subscores in TOML once the heuristic report stabilizes.
- Add an authoring command that proposes the top three rewrite moves for a slug from the criterion deficits.
- Add browser snapshots for representative low-score shapes, not only layout smoke.
- Track page archetypes (`foundational`, `protocol-boundary`, `static-typing`, `aggregator`, `runtime-constrained`) so rubrics can apply the right expectations.
- TODO: Design a future learner-facing journey about the limitations and adaptation choices in this site's editable examples, without framing those constraints as Cloudflare Workers platform limitations.
- Add a no-figure review path to avoid weak diagrams for constraint-shaped pages.
- Let CI post a quality delta comment for PRs: scores changed, graph edges changed, weak criteria changed.
