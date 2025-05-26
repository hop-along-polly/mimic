# Mimic

  Mimic is the API that always responds with the EXACT response you want.

**NOTE: As of right now Mimic only supports the HTTP protocol but eventually we would like it to support additional protocols such as gRPC, GraphQL etc.**


If you're looking to contribute to Mimic please read the [Contributing Guidelines](./CONTRIBUTING.md) which will help you oriented with the project, what
we expect from contributors and how to setup your development environment.

## Terminology

- `Request`: An Http request received by Mimic.
- `Response`: An Http response that Mimic has been configured to use as a
              response to a specific Request.
- `Mimic Endpoint`: A REST endpoint in Mimic that imitates another API. When a
                   Request is recieved Mimic will respond with the configured
                   Response for that specific Request.
- `System Endpoint`: API Endpoint used to configure, how Mimic server will behave
                     when imitating an API.
- `Manifest`: (Deprecated) A JSON object (not necessarily a file but it could be) thats maps
              a single Request to a single Response or series of Responses that
              Mimic returns when the Request is received by an echo endpoint.


## Introduction
 - What is Mimic
 - Why did I build Mimic
 - What problem(s) is Mimic solving


## Future Development
- [] Rename to Mimic
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
  - [x] GET
  - [ ] POST
  - [ ] PUT
  - [ ] PATCH
  - [ ] DELETE
- [ ] Deploy to AWS
  - [ ] Kubernetes or Lambda?
  - [ ] Point Domain at K8 cluster
