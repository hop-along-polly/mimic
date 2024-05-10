# AlwaysON Contributors

 - [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Environment Setup](#dev-env-setup)
 - [Tests](#tests)
 - [Troubleshooting](#troubleshooting)


## Getting Started

### Prerequisites

 - GNU Make: 3.81
 - Python: 3.11
 - Docker Engine: 20.10.12 
 - Docker Compose: v2.2.3


## Dev Env Setup

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

## Tests

AlwaysOn's test-suite can be run with `make tests`. This will create a virtual environment, install dependencies and run the tests. If preferred the test-suite can be run with `python -m pytest tests/ -s` but dependencies will have to be installed manually.

## Troubleshooting
