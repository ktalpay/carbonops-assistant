# Deterministic Evaluation Architecture

This document describes the current deterministic local evaluation flow in CarbonOps Assistant.

## End-to-end flow

```text
scenario JSON files
  -> case loading/validation
  -> deterministic guardrail/status evaluation
  -> summary report
  -> JSON snapshot
  -> snapshot diff
  -> CLI commands
```

## Modules and responsibilities

- `src/carbonops_assistant/eval.py`  
  Loads scenario cases, runs deterministic evaluations, and builds summary-level report structures.

- `src/carbonops_assistant/guardrails.py`  
  Applies deterministic checks for empty input, risky claim language, and missing context signals.

- `src/carbonops_assistant/assistant.py`  
  Orchestrates deterministic response generation paths used during evaluation.

- `src/carbonops_assistant/eval_snapshot.py`  
  Saves and loads evaluation report snapshots as local JSON artifacts.

- `src/carbonops_assistant/eval_diff.py`  
  Compares two evaluation snapshots and reports deterministic status/case-id transitions.

- `src/carbonops_assistant/cli.py`  
  Exposes local commands to run evaluations and compare snapshots.

## Data contracts (high-level)

- **Scenario case inputs** (JSON under `examples/evaluation/`) include grouped scenario metadata and deterministic expected outcomes.
- **Case result records** include case identifiers, expected status, actual status, and pass/fail fields.
- **Summary report object** includes totals, pass/fail counts, success, scenario-family aggregation, and compact failed-case details.
- **Snapshot files** store deterministic report JSON for local traceability and diffing.
- **Diff output** focuses on stable transition categories such as newly failing, newly passing, and unchanged failures.

## CLI commands

```bash
python -m carbonops_assistant.cli evaluate examples/evaluation/guardrails.json
python -m carbonops_assistant.cli evaluate examples/evaluation/guardrails.json --json
python -m carbonops_assistant.cli compare-evaluations previous.json current.json
python -m carbonops_assistant.cli compare-evaluations previous.json current.json --json
```

## What is measured today

- Deterministic status alignment against expected outcomes.
- Per-run pass/fail totals and overall success.
- Scenario-family level pass/fail breakdowns.
- Stable snapshot-to-snapshot transition summaries.

## What is not measured today

- LLM/model-quality traits such as coherence, factual breadth, or stylistic quality.
- User adoption, external impact, or production reliability metrics.
- Regulatory, certification, or compliance outcomes.
- Complete emissions accounting coverage.

## Why no LLM/model-quality claims are made

The evaluation stack is intentionally deterministic and local. It validates bounded status behaviors rather than probabilistic model performance. Because there are no model calls in the current architecture, claims about model quality, external validity, or production readiness are not supported by current evidence.

## Planned extension points

- Add more scenario families with explicit expected statuses and conservative assumptions.
- Expand diff output only with fields that remain deterministic and regression-testable.
- Add documentation-linked checks to keep evidence language and implementation scope aligned.
- Improve local artifact organization to simplify reviewer navigation across runs.
