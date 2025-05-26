PYTHON_CMD ?= python3
VENV_PYTHON ?= .venv/bin/python
VENV_PIP ?= .venv/bin/pip
ENV ?= dev

.PHONY: clean tests
.SILENT: dependencies

.venv: requirements.txt
	${PYTHON_CMD} -m venv .venv
	${VENV_PIP} install -r requirements.txt

# This is more of a helper to be used by test specific commands. The results are
# captured and only printed IF the command itself fails, effectively suppressing
# all the package installation.
dependencies: requirements-dev.txt
	results=`${VENV_PIP} install -r requirements-dev.txt` || echo ${results}

tests: .venv dependencies
	@${VENV_PYTHON} -m pytest tests/ -s

format: .venv dependencies
	@${VENV_PYTHON} -m black --check mimc tests

format-fix: .venv dependencies
	@${VENV_PYTHON} -m black mimc tests

clean:
	rm -rf .venv
	docker-compose down && docker volume rm mimc_dbdata || true
