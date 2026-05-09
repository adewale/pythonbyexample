.PHONY: test embed-examples build check-generated fingerprint browser-layout-test seo-cache-lint verify-examples check-confusable-pairs check-broad-surface-tours check-footgun-coverage check-notes-supported quality-checks format-examples verify-python-version verify dev deploy lint

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

check-confusable-pairs:
	scripts/check_confusable_pairs.py

check-broad-surface-tours:
	scripts/check_broad_surface_tours.py

check-footgun-coverage:
	scripts/check_footgun_coverage.py

check-notes-supported:
	scripts/check_notes_supported.py

quality-checks: check-confusable-pairs check-broad-surface-tours check-footgun-coverage check-notes-supported

format-examples:
	scripts/format_examples.py

verify-python-version: build
	uv run --python $(VERSION) scripts/verify_examples.py --python-version $(VERSION)

lint:
	uv run ruff check src tests scripts

verify: build test seo-cache-lint verify-examples quality-checks browser-layout-test lint check-generated

dev:
	uv run pywrangler dev --port 9696

deploy: build
	uv run pywrangler deploy
