# ThreatCode Schemas

This repository contains the published schema assets used across ThreatCode projects, including configuration schemas and API contract definitions.

## Packages

- `schemas/proxy` – published GraphQL and OpenAPI schema files for the Proxy API
- `schemas/cloud` – cloud configuration schema definitions

## Publishing

The proxy schema package is published to npm and PyPI through the GitHub Actions workflow in `.github/workflows/publish.yml`.

## Usage

Use the published schema package when a tool or service needs a stable reference to the current Proxy API contract.
