install:
	@poetry install

test:
	poetry run coverage run -m pytest tests -vv

lint:
	poetry run flake8 gendiff

check: test lint

build: check
	@poetry build

.PHONY: install test check lint build
