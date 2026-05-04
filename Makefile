.PHONY: test dev deploy lint

test:
	python3 -m unittest discover -s tests -v

lint:
	uv run ruff check src tests

dev:
	uv run pywrangler dev --port 9696

deploy:
	uv run pywrangler deploy
