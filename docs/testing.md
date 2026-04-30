# Testing

## Test Command

```bash
python -m pytest -q
```

## Current Coverage

Tests currently cover:

- package import baseline
- local CLI status message
- response contract behavior
- deterministic guardrails
- units and emissions helpers
- evaluation case loading and deterministic runner behavior
- knowledge-base document loading and keyword ranking
- deterministic assistant orchestrator behavior

## Evaluation Baseline

Evaluation cases are loaded from JSON (for example `examples/sample_questions.json`) and validated against response statuses in the response contract.

The deterministic runner compares expected status to actual guardrail-driven status and returns pass/fail per case.

## Out of Scope

- LLM quality measurement
- external API integration behavior
- end-to-end reporting or compliance workflows

## CLI evaluation checks

```bash
python -m carbonops_assistant.cli status
python -m carbonops_assistant.cli evaluate examples/evaluation/guardrails.json
python -m carbonops_assistant.cli evaluate examples/evaluation/guardrails.json --json
```

`evaluate` exits `0` only when all cases pass. It returns non-zero for failed expectations or invalid case files.
