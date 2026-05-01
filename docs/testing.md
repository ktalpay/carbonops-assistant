# Testing

## Test Command

```bash
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q
```

The current test suite is expected to pass locally from the repository root after installing test dependencies.

## Current Coverage

Tests currently cover:

- package import baseline
- local CLI status message
- response contract behavior
- deterministic guardrails
- units and emissions helpers
- sample question fixture schema
- evaluation case loading and deterministic runner behavior
- knowledge-base document loading and keyword ranking
- deterministic assistant orchestrator behavior

## Continuous Integration

GitHub Actions runs a test-only workflow on pushes and pull requests.

The tests do not require:

- external API calls
- provider credentials
- network access for project behavior

## Evaluation Coverage

Evaluation cases are loaded from JSON (for example `examples/sample_questions.json`) and validated against response statuses in the response contract.

The deterministic runner compares expected status to actual guardrail-driven status and returns pass/fail per case.

## Current Gaps

- no parser tests yet
- no CSV or table parsing tests yet
- no source metadata extraction tests yet
- no external model/provider tests
- no reporting pipeline tests
- no exhaustive domain coverage
