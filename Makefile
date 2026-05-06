.PHONY: test embed-examples fingerprint browser-layout-test seo-cache-lint verify-examples verify-python-version verify dev deploy lint

test:
	python3 -m unittest discover -s tests -v

embed-examples:
	scripts/embed_example_sources.py

fingerprint: embed-examples
	scripts/fingerprint_assets.py

browser-layout-test:
	scripts/check_browser_layout.mjs

seo-cache-lint:
	scripts/lint_seo_cache.py

verify-examples: embed-examples
	scripts/verify_examples.py

verify-python-version: embed-examples
	scripts/verify_examples.py --python-version $(VERSION)

lint:
	uv run ruff check src tests scripts

verify: fingerprint test seo-cache-lint verify-examples browser-layout-test lint

dev:
	uv run pywrangler dev --port 9696

deploy: fingerprint
	uv run pywrangler deploy
