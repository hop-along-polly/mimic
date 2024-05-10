PYTHON_CMD ?= python3
VENV_PYTHON ?= .venv/bin/python
VENV_PIP ?= .venv/bin/pip
ENV ?= dev

.PHONY: clean tests

.venv: requirements.txt
	${PYTHON_CMD} -m venv .venv
	${VENV_PIP} install -r requirements.txt


# TODO Figure out a way that I don't always have to install dev dependencies?
tests: .venv requirements-dev.txt
	${VENV_PIP} install -r requirements-dev.txt
	${VENV_PYTHON} -m pytest tests/ -s

clean:
	rm -rf .venv
	docker-compose down && docker volume rm always-on_dbdata || true
 