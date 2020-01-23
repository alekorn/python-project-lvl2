install:
	@poetry install

test:
	poetry run pytest diff tests

lint:
	poetry run flake8 diff

build: check
	@poetry build

.PHONY: install test lint build
