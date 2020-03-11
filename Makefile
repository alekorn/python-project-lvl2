install:
	@poetry install

test:
	poetry run python -m pytest --cov=page_loader tests/ --cov-report=xml

lint:
	poetry run flake8 gendiff

check: test lint

build: check
	@poetry build

.PHONY: install test check lint build
