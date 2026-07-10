# All Python tooling runs through uv pinned to 3.13 so the suite works on any
# machine regardless of the system python3 (examples use 3.12+ `type` syntax).
PY := uv run --python 3.13
NODE_DEPS_STAMP := node_modules/.package-lock.json

.PHONY: node-deps test embed-examples embed-editorial-registry build-search-index build check-generated fingerprint prototypes browser-layout-test search-ranking-test social-cards check-social-cards seo-cache-lint verify-examples check-registry-integrity check-confusable-pairs check-broad-surface-tours check-footgun-coverage check-notes-supported check-program-covers-cells check-prose-duplication check-inline-links score-example-criteria check-quality-scores check-no-figure-rationales check-journey-outcomes audit-example-graph quality-checks rubric-audit format-examples verify-python-version verify smoke-deployment dev deploy lint

$(NODE_DEPS_STAMP): package.json package-lock.json
	npm ci --ignore-scripts

node-deps: $(NODE_DEPS_STAMP)

test:
	$(PY) python -m unittest discover -s tests -v

embed-examples:
	$(PY) scripts/embed_example_sources.py

embed-editorial-registry:
	$(PY) scripts/embed_editorial_registry.py

build-search-index: embed-examples
	$(PY) scripts/build_search_index.py

build: embed-examples embed-editorial-registry build-search-index fingerprint prototypes

check-generated: build check-social-cards
	git diff --exit-code src/example_sources_data.py src/editorial_registry_data.py src/asset_manifest.py public/_headers public/prototyping public/search-index.json
	# Tracked generated changes may be staged for commit; reject only untracked output here because git diff above already catches unstaged tracked drift.
	test -z "$$(git ls-files --others --exclude-standard -- public/prototyping public/*.css public/*.js public/*.json)"

fingerprint: embed-examples embed-editorial-registry build-search-index
	$(PY) scripts/fingerprint_assets.py

prototypes: embed-examples
	$(PY) scripts/build_prototypes.py
	$(PY) scripts/build_marginalia.py

browser-layout-test:
	scripts/check_browser_layout.mjs

search-ranking-test:
	scripts/check_search_ranking.mjs

social-cards:
	$(PY) scripts/build_social_cards.py
	scripts/build_social_cards.mjs

check-social-cards:
	$(PY) scripts/build_social_cards.py --check

seo-cache-lint:
	$(PY) scripts/lint_seo_cache.py

verify-examples: build
	$(PY) scripts/verify_examples.py

check-registry-integrity:
	$(PY) scripts/check_registry_integrity.py

check-confusable-pairs:
	$(PY) scripts/check_confusable_pairs.py

check-broad-surface-tours:
	$(PY) scripts/check_broad_surface_tours.py

check-footgun-coverage:
	$(PY) scripts/check_footgun_coverage.py

check-notes-supported:
	$(PY) scripts/check_notes_supported.py

check-program-covers-cells:
	$(PY) scripts/check_program_covers_cells.py

check-prose-duplication:
	$(PY) scripts/check_prose_duplication.py

check-inline-links:
	$(PY) scripts/check_inline_links.py

score-example-criteria:
	$(PY) scripts/score_example_criteria.py --limit 12

check-quality-scores:
	$(PY) scripts/check_quality_scores.py

check-no-figure-rationales:
	$(PY) scripts/check_no_figure_rationales.py

check-journey-outcomes:
	$(PY) scripts/check_journey_outcomes.py

audit-example-graph:
	$(PY) scripts/audit_example_graph.py --check

quality-checks: check-registry-integrity check-confusable-pairs check-broad-surface-tours check-footgun-coverage check-notes-supported check-program-covers-cells check-prose-duplication check-inline-links score-example-criteria check-quality-scores check-no-figure-rationales check-journey-outcomes audit-example-graph

rubric-audit:
	$(PY) scripts/audit_rubric_snapshot.py

format-examples:
	$(PY) scripts/format_examples.py

verify-python-version: build
	uv run --python $(VERSION) scripts/verify_examples.py --python-version $(VERSION)

lint:
	uv run ruff check src tests scripts

verify: build test seo-cache-lint verify-examples quality-checks browser-layout-test search-ranking-test lint check-generated

dev: node-deps
	uv run --group workers pywrangler dev --port 9696

smoke-deployment:
	$(PY) scripts/smoke_deployment.py $(URL)

deploy: node-deps check-generated
	uv run --group workers pywrangler sync
	uv run --group workers pywrangler deploy
