#!/usr/bin/env make

include Makehelp.mk


###
# PYTHON TARGETS
###


## Format python code using black
fmt:
	. .venv/bin/activate && black --line-length 256 .


## Perform code format using black
check-fmt:
	. .venv/bin/activate && black --line-length 256 --check .
.PHONY: check-fmt


## Perform pylint check
check-lint:
	. .venv/bin/activate && pylint exercises tests
.PHONY: check-lint


## Perform mypy check
check-type:
	. .venv/bin/activate && mypy exercises tests
.PHONY: check-type


## Perform fmt, lint and type checks
check: check-fmt check-lint check-type
.PHONY: check


## Perform unit tests
test:
	. .venv/bin/activate && python -m pytest -v
.PHONY: test


## Create coverage report
coverage:
	. .venv/bin/activate
	coverage run -m pytest -v
	coverage xml -o reports/coverage.xml

	@echo
	coverage report
.PHONY: coverage
