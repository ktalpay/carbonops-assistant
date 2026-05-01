# Quickstart

This quickstart runs the local deterministic baseline from a fresh checkout.

## Install

Use Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
```

## Run Tests

```bash
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q
```

## Ask Demo

```bash
python -m carbonops_assistant.cli ask "Calculate emissions for 100 litres with factor 2.68 kgCO2e/litre."
```

The ask demo returns the current deterministic assistant response shape. It does not call external services.

## Parser Demo

```bash
python -m carbonops_assistant.cli parse-factor "Diesel combustion factor: 2.68 kgCO2e/litre"
```

The parser demo supports only narrow simple text snippets. Parser outputs are candidates requiring validation and human review.

## Example Status Summary

```bash
python -m carbonops_assistant.cli run-examples
```

The command loads `examples/sample_questions.json` and returns a JSON summary with total, passed, failed, and failure details.

## Limitations

- Pre-alpha local baseline.
- No external services.
- No external data retrieval.
- No provider integration.
- No CSV or table parser.
- No PDF or OCR extraction.
- No web crawling.
- No production reporting.
- No regulatory filing.
- No certification.
- Outputs require human review before material use.
