.PHONY: serve build test

serve:
	uv run mkdocs serve

build:
	uv run mkdocs build --strict

test:
	uv run pytest -q
