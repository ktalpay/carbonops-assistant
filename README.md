# CarbonOps Assistant

CarbonOps Assistant is a pre-alpha local development project for building a small, testable foundation for a carbon and emissions domain assistant.

The current repository focuses on conservative building blocks: package structure, deterministic helper functions, structured assistant responses, guardrail experiments, documentation, and test workflows.

## Status

Pre-alpha. Not production-ready.

## Current Scope

The current scope is limited to:

- a minimal Python package under `src/carbonops_assistant`
- a local CLI status entry point
- unit-testable modules
- documentation for local development and testing
- planned deterministic emissions helpers and response contracts

## Non-Goals

This project does not currently provide:

- regulatory approval, assurance, or certification
- production deployment automation
- legal or financial advice
- automated regulatory filing
- complete emissions accounting coverage
- authentication, multi-tenant operations, or external paid service integrations

## Local Setup

Use Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
```

The package uses a `src` layout. Installing it in editable mode makes the local CLI and imports available from the repository checkout.

## Running Tests

```bash
python -m pytest -q
```

The current tests are intentionally small and deterministic. They do not call external services.

## Repository Structure

```text
src/carbonops_assistant/   Python package source
tests/                     Unit tests
docs/                      Development, testing, roadmap, and run documents
```

## Development

See [docs/development.md](docs/development.md).

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## Disclaimer

CarbonOps Assistant is experimental software for local development. It should not be used as the sole basis for emissions reporting, business decisions, legal determinations, or regulatory submissions.
