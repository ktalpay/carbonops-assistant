# CarbonOps Assistant

CarbonOps Assistant is a pre-alpha local development project for building a small, testable foundation for a carbon and emissions domain assistant.

## Status

Pre-alpha. v0.1.0 release candidate documentation and deterministic baseline. Not a production implementation.

## Implemented Baseline

- Python package baseline under `src/carbonops_assistant`
- Deterministic response contract with allowed statuses (`answered`, `unsupported`, `needs_more_context`)
- Guardrail checks for empty input, unsupported or risky wording patterns, and missing context
- Emissions calculation helpers for `activity amount * emission factor`
- Basic unit normalization helpers for a narrow set of energy and emissions units
- Sample question fixture in `examples/sample_questions.json`
- Sample question schema validation
- Public question examples in `docs/examples.md`
- Local evaluation case loading and deterministic status checks
- Local Markdown knowledge section loading and keyword search baseline
- Deterministic assistant orchestrator that combines guardrails with optional local knowledge sections
- Parser input contract documentation in `docs/parser-contract.md`
- Source metadata model documentation in `docs/source-metadata-model.md`
- Reporting result contract documentation in `docs/reporting-result-contract.md`
- v0.1.0 release notes in `docs/release-notes/v0.1.0.md`
- Unit tests for the implemented baseline
- Test-only continuous integration workflow

## Current Limitations

- No emission factor parser
- No CSV or table parsing
- No source metadata extraction from external references
- No model/provider integration
- No broad evaluation scoring workflow
- No production reporting pipeline
- No external API calls or external data retrieval
- No deployment, authentication, or multi-tenant support
- Not carbon accounting certification
- Not suitable as the sole basis for reporting or submissions
- Outputs require human review

## Planned

- emission factor parsing experiments
- source metadata extraction and validation
- reporting result implementation
- expanded unit normalization
- parser fixture examples

## Non-Goals

This project does not currently provide:

- regulatory approval, assurance, or certification
- production deployment automation
- legal or financial advice
- automated regulatory filing
- complete emissions accounting coverage
- reporting correctness guarantees

## Local Setup

Use Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
```

## Running Tests

```bash
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q
```

Tests do not require provider credentials or external service access.

## Repository Structure

```text
src/carbonops_assistant/   Python package source
tests/                     Unit tests
docs/                      Development, testing, roadmap, release notes, examples, parser/source/reporting contracts, and evaluation notes
examples/                  Small public fixtures, including sample question examples
.github/workflows/         Test-only continuous integration
```

## Disclaimer

CarbonOps Assistant is experimental software for local development. It is not legal advice, not carbon accounting certification, and not suitable as the sole basis for reporting or regulatory submissions. Outputs should be reviewed by qualified humans before use.
