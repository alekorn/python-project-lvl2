install:
	@poetry install

test:
	coverage run -m pytest tests

lint:
	poetry run flake8 gendiff

check: test lint

build: check
	@poetry build

.PHONY: install test lint build
