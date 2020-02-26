install:
	@poetry install

test:
	poetry run pytest gendiff tests

lint:
	poetry run flake8 gendiff

build: check
	@poetry build

.PHONY: install test lint build
