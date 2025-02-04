# Testerozza Contributors

- [Code of Conduct](#code-of-conduct)
- [Definition of Done](#definition-of-done)
- [Branching Strategy](#branching-strategy)
- [Versioning](#versioning)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Environment Setup](#environment-setup)
- [Tests](#tests)
- [Troubleshooting](#troubleshooting)


## Code of Conduct

1. Don't be an a**hole. (i.e. be open to hearing others thoughts and opinions and be respectful of them especially when you disagree)
2. Understand written communication is imperfect and a lot of tone and meaning can be lost in translation. Never assume malice when forgivable error will suffice.
3. Ensure you've met the [Definition of Done](#definition-of-done) for all pull requests,
4. Use Draft PRs when you want to share code that does not meet the [Definition of Done](#definition-of-done)


## Definition of Done

- I have only included commits that apply to the referenced Github Issue.
- I have performed a self-review of my code.
- I have taken the time to refactor the code to ensure testability and maintainability.
- I have made corresponding changes to the documentation.
- I have added tests that prove my fix/feature is working per requirements.
- I have provided sufficient code comments so any developer can support my code.


## Branching Strategy

Testerozza uses trunk based development. The trunk branch is `main` and all Pull Requests should be submitted back to `main`.

There are 4 types of changes any code base experiences. They are
 - `Bugfixes`: A non-breaking change that fixes an issue
 - `Features`: A non-breaking change that adds new functionality or improves existing functionality
 - `Chore`: A non-breaking change that adds no net new functionality (i.e. tests, docs, refactoring, etc.)
 - `Breaking Change`: A bugfix or feature that has to be added in a way that is not compatible with the previous version of the public API.

Depending on the type of work you are performing we recommend using one of the following branch naming conventions
 - Bugfixes: `bug/<issue-#>/<summary-of-work>` (i.e. `bug/iss-1/mongodb-connection`)
 - Features: `fea/<issue-#>/<summary>` (i.e. `fea/iss-2/add-manifests-svc`)
 - Chore/Dev Change: `dev/<issue-#>/<summary>` (i.e. `dev/iss-3/refactor-b4-onboarding-contributors`)
 - Breaking Change: `breaking/<issue-#>/<summary>` (i.e. `breaking/iss-4/support-manifest-file-uploads`)

## Versioning

Currently Testerozza is not being versioned. It's initial release will be `v0.1.0` and then we will follow semantic versioning.
While in development no LTS tags will be published.

## Getting Started

### Prerequisites

 - GNU Make: 3.81
 - Python: 3.11
 - PIP
 - venv
 - Docker Engine: 20.10.12 
 - Docker Compose: v2.2.3

### Environment Setup

0. Review the Terminology section of the README if you are not already familiar with the systems terminology.
1. Make a copy of the `.env.example` file. The values in the file will work
by default but you can customize them if you want.

**NOTE: When changing the `DB_USERNAME` and `DB_PASSWORD` you will need to upddate the `init-db.js` script file to use that same username and password.**
```bash
cp env.example .env
```

2. Spin up Docker services
```bash
docker-compose up
```

3. Verify the API and DB are healthy with the status endpoint
```bash
curl -XGET http://localhost:8000/v1/status
```
If everything is working the response should be
```json
{
  "api": "online",
  "db": "online"
}
```

4. Happy Coding!


## CI Checks

### Linting
We use `black` for our linter. You can check your code by running:
```sh
make lint
```
Don't worry though! `Black` can automatically fix a lot of your
errors by running:
```sh
make lint-fix
```

This runs as part of our Github CI-Checks.

### Tests

Testerozza's test-suite can be run with `make tests`. This will create a virtual environment, install dependencies and run the tests. If preferred the test-suite can be run with `python -m pytest tests/ -s` but dependencies will have to be installed manually.

## Troubleshooting
