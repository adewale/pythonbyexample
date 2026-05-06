.PHONY: test fingerprint browser-layout-test seo-cache-lint verify dev deploy lint

test:
	python3 -m unittest discover -s tests -v

fingerprint:
	scripts/fingerprint_assets.py

browser-layout-test:
	scripts/check_browser_layout.mjs

seo-cache-lint:
	scripts/lint_seo_cache.py

lint:
	uv run ruff check src tests scripts

verify: fingerprint test seo-cache-lint browser-layout-test lint

dev:
	uv run pywrangler dev --port 9696

deploy: fingerprint
	uv run pywrangler deploy
