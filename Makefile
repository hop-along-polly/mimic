PYTHON_CMD ?= python3
VENV_PYTHON ?= .venv/bin/python
VENV_PIP ?= .venv/bin/pip
ENV ?= dev

.PHONY: clean tests

.venv: requirements.txt
	${PYTHON_CMD} -m venv .venv
	${VENV_PIP} install -r requirements.txt


# TODO Figure out a way that I don't always have to install dev dependencies?
devendencies: requirements-dev.txt
	${VENV_PIP} install -r requirements-dev.txt

tests: .venv devendencies
	${VENV_PYTHON} -m pytest tests/ -s

lint: .venv devendencies
	${VENV_PYTHON} -m black --check alwayson tests

lint-fix: .venv dependencies
	${VENV_PYTHON} -m black alwayson tests

clean:
	rm -rf .venv
	docker-compose down && docker volume rm always-on_dbdata || true
