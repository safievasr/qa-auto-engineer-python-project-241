install:
	uv sync --all-groups

check:
	uv run ruff check gendiff tests
	uv run pytest

lint:
	uv run ruff check gendiff tests

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

.PHONY: install update test lint selfcheck check build
