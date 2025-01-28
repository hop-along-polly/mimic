PYTHON_CMD ?= python3
VENV_PYTHON ?= .venv/bin/python
VENV_PIP ?= .venv/bin/pip
ENV ?= dev

.PHONY: clean tests
.SILENT: devendencies

.venv: requirements.txt
	${PYTHON_CMD} -m venv .venv
	${VENV_PIP} install -r requirements.txt

# This is more of a helper to be used by test specific commands. The results are
# captured and only printed IF the command itself fails, effectively suppressing
# all the package installation.
devendencies: requirements-dev.txt
	results=`${VENV_PIP} install -r requirements-dev.txt` || echo ${results}

tests: .venv devendencies
	@${VENV_PYTHON} -m pytest tests/ -s

format: .venv devendencies
	@${VENV_PYTHON} -m black --check alwayson tests

format-fix: .venv devendencies
	@${VENV_PYTHON} -m black alwayson tests

clean:
	rm -rf .venv
	docker-compose down && docker volume rm always-on_dbdata || true
