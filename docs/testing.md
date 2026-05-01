# Testing

## Test Command

```bash
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q
```

The current test suite is expected to pass locally from the repository root after installing test dependencies.

## Example Summary Command

```bash
python -m carbonops_assistant.cli run-examples
```

The command loads `examples/sample_questions.json` and returns a JSON summary with `total_cases`, `passed`, `failed`, and `failures`.

## Current Coverage

Tests currently cover:

- package import baseline
- local CLI status message
- local CLI demo command statuses
- local parser demo command statuses
- response contract behavior
- deterministic guardrails
- units and emissions helpers
- minimal text factor parser
- sample question fixture schema
- evaluation case loading and deterministic runner behavior
- evaluation summary output
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

- no expanded parser coverage yet
- no CSV or table parsing tests yet
- no source metadata extraction tests yet
- no external model/provider tests
- no reporting pipeline tests
- no exhaustive domain coverage
