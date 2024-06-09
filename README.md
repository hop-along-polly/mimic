# AlwaysON

  AlwaysON is the API that always responds with the EXACT response you want.

**NOTE: As of right now AlwaysON only supports the HTTP protocol but eventually we would like it to support additional protocols such as gRPC, GraphQL etc.**


If you're looking to contribute to AlwaysON please read the [Contributing Guidelines](./CONTRIBUTING.md) which will help you oriented with the project, what
we expect from contributors and how to setup your development environment.

## Terminology

- `Request`: An Http request received by AlwaysON.
- `Response`: An Http response that AlwaysON has been configured to use as a
              response to a specific Request.
- `Echo Endpoint`: A REST endpoint in AlwaysON that imitates another API. When a
                   Request is recieved AlwaysON will respond with the configured
                   Response for that specific Request.
- `System Endpoint`: A REST Endpoint used to configure, and manage how AlwaysON
                     will behave when imitating an API.
- `Manifest`: A JSON object (not necessarily a file but it could be) thats maps
              a single Request to a single Response or series of Responses that
              AlwaysON returns when the Request is received by an echo endpoint.


## Introduction
 - What is AlwaysON
 - Why did I build AlwaysON
 - What problem(s) is AlwaysON solving


## Future Development
## Future Development
- [x] Dependency Injection
- [ ] CI/CD
  - [ ] Mypy - Typing
  - [ ] Linting
  - [ ] Code Coverage
  - [ ] Github Actions
- [ ] Logging
- [x] Dockerize
- [x] Select DB....I'm feeling Mongo
- [ ] Endpoints
  - [/] GET
  - [ ] POST
  - [ ] PUT
  - [ ] PATCH
  - [ ] DELETE
- [ ] Deploy to AWS
  - [ ] Kubernetes or Lambda?
  - [ ] Point Domain at K8 cluster
