.PHONY: test embed-examples build check-generated fingerprint browser-layout-test seo-cache-lint verify-examples format-examples verify-python-version verify dev deploy lint

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

format-examples:
	scripts/format_examples.py

verify-python-version: build
	uv run --python $(VERSION) scripts/verify_examples.py --python-version $(VERSION)

lint:
	uv run ruff check src tests scripts

verify: build test seo-cache-lint verify-examples browser-layout-test lint check-generated

dev:
	uv run pywrangler dev --port 9696

deploy: build
	uv run pywrangler deploy
