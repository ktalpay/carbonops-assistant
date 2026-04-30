# CarbonOps Assistant

CarbonOps Assistant is a pre-alpha local development project for building a small, testable foundation for a carbon and emissions domain assistant.

## Status

Pre-alpha. Not production-ready.

## Implemented

- Python package baseline under `src/carbonops_assistant`
- Deterministic response contract with allowed statuses (`answered`, `unsupported`, `needs_more_context`)
- Deterministic guardrails for empty input, risky claim language, and missing context
- Deterministic domain helpers for units and emissions calculations
- Local evaluation case loader and deterministic evaluation runner
- Local Markdown knowledge-base section loader and keyword search baseline
- Deterministic assistant orchestrator that combines guardrails with optional local knowledge sections

## Current Limitations

- No LLM calls
- No external APIs or external data retrieval
- No deployment, authentication, or multi-tenant support
- Not suitable for regulatory approval, certification, or assurance decisions
- Not complete emissions accounting coverage

## Planned

- richer evaluation datasets and scoring checks
- improved deterministic assistant answer shaping
- incremental domain examples and evidence-oriented artifacts

## Non-Goals

This project does not currently provide:

- regulatory approval, assurance, or certification
- production deployment automation
- legal or financial advice
- automated regulatory filing
- complete emissions accounting coverage

## Local Setup

Use Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
```

## Running Tests

```bash
python -m pytest -q
```
