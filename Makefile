.PHONY: test embed-examples build check-generated fingerprint browser-layout-test seo-cache-lint verify-examples check-registry-integrity check-confusable-pairs check-broad-surface-tours check-footgun-coverage check-notes-supported score-example-criteria check-quality-scores check-no-figure-rationales check-journey-outcomes quality-checks format-examples verify-python-version verify smoke-deployment dev deploy lint

test:
	python3 -m unittest discover -s tests -v

embed-examples:
	scripts/embed_example_sources.py

build: embed-examples fingerprint

check-generated: build
	git diff --exit-code src/example_sources_data.py src/asset_manifest.py public/_headers

fingerprint: embed-examples
	scripts/fingerprint_assets.py

browser-layout-test:
	scripts/check_browser_layout.mjs

seo-cache-lint:
	scripts/lint_seo_cache.py

verify-examples: build
	scripts/verify_examples.py

check-registry-integrity:
	scripts/check_registry_integrity.py

check-confusable-pairs:
	scripts/check_confusable_pairs.py

check-broad-surface-tours:
	scripts/check_broad_surface_tours.py

check-footgun-coverage:
	scripts/check_footgun_coverage.py

check-notes-supported:
	scripts/check_notes_supported.py

score-example-criteria:
	scripts/score_example_criteria.py --limit 12

check-quality-scores:
	scripts/check_quality_scores.py

check-no-figure-rationales:
	scripts/check_no_figure_rationales.py

check-journey-outcomes:
	scripts/check_journey_outcomes.py

quality-checks: check-registry-integrity check-confusable-pairs check-broad-surface-tours check-footgun-coverage check-notes-supported score-example-criteria check-quality-scores check-no-figure-rationales check-journey-outcomes

format-examples:
	scripts/format_examples.py

verify-python-version: build
	uv run --python $(VERSION) scripts/verify_examples.py --python-version $(VERSION)

lint:
	uv run ruff check src tests scripts

verify: build test seo-cache-lint verify-examples quality-checks browser-layout-test lint check-generated

dev:
	uv run pywrangler dev --port 9696

smoke-deployment:
	scripts/smoke_deployment.py $(URL)

deploy: build
	uv run pywrangler deploy
