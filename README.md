# AlwaysON

  AlwaysON is the REST API that always responds with the EXACT response you want.

## Introduction
 - What is AlwaysON
 - Why did I build AlwaysON
 - What problem(s) is AlwaysON solving


## Future Development
 - [] Dependency Injection
 - [] CI/CD
  - [] Mypy - Typing
  - [] Linting
  - [] Code Coverage
  - [] Github Actions
 - [] Logging
 - [x] Dockerize
 - [] Select DB....I'm feeling Mongo
 - [] Endpoints
  - [x] GET
  - [] POST
  - [] PUT
  - [] PATCH
  - [] DELETE
 - [] Deploy to AWS
  - [] Kubernetes or Lambda?
  - [] Point Domain at K8 cluster


## .alwayson File
```json
{
  "http_method": {
    "pathname": [
      {
        "status_code": "",
        "body": <JSON | XML | plaintext | blob | YML>
      },...
    ]
  }
}
```