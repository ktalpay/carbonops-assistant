# CarbonOps Assistant

CarbonOps Assistant is a pre-alpha local development project for building a small, testable foundation for a carbon and emissions domain assistant.

## Status

Pre-alpha. v0.2.0 release candidate: minimal deterministic local demo baseline. Not a production implementation.

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
- Deterministic local demo command for evaluating a question without external services
- Minimal text factor parser for narrow public-safe snippets
- Parser result JSON-friendly serialization
- Minimal reporting result model and Markdown summary renderer
- Evaluation summary output for sample questions
- Parser input contract documentation in `docs/parser-contract.md`
- Source metadata model documentation in `docs/source-metadata-model.md`
- Reporting result contract documentation in `docs/reporting-result-contract.md`
- v0.1.0 release notes in `docs/release-notes/v0.1.0.md`
- Unit tests for the implemented baseline
- Test-only continuous integration workflow

## Current Limitations

- Parser supports only narrow simple text snippets
- No CSV or table parsing
- No PDF, OCR, or web extraction
- No source metadata extraction from external references
- No model/provider integration
- No broad evaluation scoring workflow
- No production reporting pipeline
- No external API calls or external data retrieval
- No deployment, authentication, or multi-tenant support
- Not carbon accounting certification
- Not suitable as the sole basis for reporting or submissions
- Outputs require human review

## Quickstart

See `docs/quickstart.md` for install, local demo, parser demo, and example status summary commands.

## Planned

- expanded emission factor parsing experiments
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

## Local Demo

Run a deterministic local question through the current baseline:

```bash
python -m carbonops_assistant.cli ask "Calculate emissions for 100 litres with factor 2.68 kgCO2e/litre."
```

Sample output:

```json
{
  "limitations": [
    "This is a deterministic baseline without LLM generation or external data calls."
  ],
  "message": "The question appears in-scope, but no local knowledge base was provided for grounded details.",
  "status": "answered"
}
```

The demo command is a local baseline only. It does not run the parser, call an external model/provider, retrieve external data, or produce production reporting. Outputs require human review.

### Parser Demo

Run a narrow text factor parser example:

```bash
python -m carbonops_assistant.cli parse-factor "Diesel combustion factor: 2.68 kgCO2e/litre"
```

Sample output:

```json
{
  "assumptions": [],
  "confidence_level": "medium",
  "extracted_text": "2.68 kgCO2e/litre",
  "factor_unit": "kgCO2e/litre",
  "factor_value": "2.68",
  "input_id": "cli-input",
  "normalized_unit": "kgCO2e/litre",
  "parser_status": "parsed",
  "unsupported_reasons": [],
  "warnings": []
}
```

The parser demo supports only narrow simple text snippets. Parser outputs are candidates requiring validation and human review.

### Example Status Summary

Run the sample question status checks:

```bash
python -m carbonops_assistant.cli run-examples
```

Sample output:

```json
{
  "failed": 0,
  "failures": [],
  "passed": 12,
  "total_cases": 12
}
```

### Markdown Summary Example

Reporting results can be rendered as concise Markdown summaries for local review output. The summary includes status, visible warnings, assumptions, review status, and the note: `This is a local deterministic summary and requires human review.`

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
