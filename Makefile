install:
	uv sync

lint:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml


.PHONY: install update test lint selfcheck check build
