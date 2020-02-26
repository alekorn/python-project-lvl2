install:
	@poetry install

test:
	poetry run pytest gendiff tests

lint:
	poetry run flake8 gendiff

check: test lint

build: check
	@poetry build

.PHONY: install test lint build
