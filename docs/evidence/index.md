# Technical Evidence Index

This index consolidates implemented technical evidence in this repository as of April 30, 2026. It is intended for reviewer navigation and conservative evidence tracking.

## Deterministic assistant foundation

- **Implemented artifacts**: `src/carbonops_assistant/assistant.py`, `src/carbonops_assistant/models.py`.  
- **Why it matters technically**: establishes a deterministic orchestration path and a stable response structure for local evaluation.  
- **GTV relevance (conservative)**: demonstrates structured engineering work on a traceable assistant baseline rather than ad hoc outputs.  
- **Current limitation**: no model calls and limited answer-shaping sophistication.  
- **Next improvement candidate**: expand deterministic response templates while preserving strict guardrail behavior.

## Response contract and guardrails

- **Implemented artifacts**: `src/carbonops_assistant/guardrails.py`, `src/carbonops_assistant/models.py`, `tests/test_guardrails.py`.  
- **Why it matters technically**: codifies explicit status outcomes (`answered`, `unsupported`, `needs_more_context`) and blocks risky claim language.  
- **GTV relevance (conservative)**: provides repeatable behavior boundaries that can be evaluated and evidenced.  
- **Current limitation**: rule-based checks are intentionally narrow and do not cover full domain semantics.  
- **Next improvement candidate**: add carefully scoped deterministic checks with test coverage for ambiguous edge cases.

## Emissions helper baseline

- **Implemented artifacts**: `src/carbonops_assistant/emissions.py`, `src/carbonops_assistant/units.py`, `tests/test_emissions.py`, `tests/test_units.py`.  
- **Why it matters technically**: provides deterministic numeric helpers for unit handling and simple emissions calculations.  
- **GTV relevance (conservative)**: shows practical domain-oriented code artifacts that are testable and reviewable.  
- **Current limitation**: not complete emissions accounting coverage and no external factor retrieval.  
- **Next improvement candidate**: expand helper scenarios and explicit assumptions documentation.

## Evaluation scenario families

- **Implemented artifacts**: `examples/evaluation/guardrails.json`, `examples/evaluation/context_gaps.json`, `examples/evaluation/assumptions.json`, `examples/evaluation/calculation_readiness.json`.  
- **Why it matters technically**: enables repeatable local checks across grouped deterministic scenarios.  
- **GTV relevance (conservative)**: supports evidence that behavior validation is systematic and scenario-driven.  
- **Current limitation**: scenario coverage is still limited and does not imply model-quality benchmarking.  
- **Next improvement candidate**: add carefully selected edge-case families with explicit expected statuses.

## Evaluation summary reporting

- **Implemented artifacts**: `src/carbonops_assistant/eval.py`, `tests/test_eval.py`.  
- **Why it matters technically**: generates deterministic summary output including totals, pass/fail counts, and scenario aggregation.  
- **GTV relevance (conservative)**: provides machine-readable evidence outputs suitable for run-to-run review.  
- **Current limitation**: metric surface is intentionally small and focuses on deterministic status outcomes.  
- **Next improvement candidate**: introduce additional stable summary fields only when determinism is preserved.

## Snapshot and diff tooling

- **Implemented artifacts**: `src/carbonops_assistant/eval_snapshot.py`, `src/carbonops_assistant/eval_diff.py`, `tests/test_eval_snapshot.py`, `tests/test_eval_diff.py`.  
- **Why it matters technically**: supports deterministic artifact storage and run comparison focused on status/case transitions.  
- **GTV relevance (conservative)**: improves traceability of incremental quality changes without overstating capability.  
- **Current limitation**: diffing scope is narrow by design and not a full analytics framework.  
- **Next improvement candidate**: evaluate selective extension of diff fields with regression tests.

## CLI commands

- **Implemented artifacts**: `src/carbonops_assistant/cli.py`, `tests/test_cli.py`.  
- **Why it matters technically**: exposes local deterministic evaluation and comparison commands for reproducible workflows.  
- **GTV relevance (conservative)**: demonstrates operable tooling for evidence generation in development contexts.  
- **Current limitation**: local-only interface and no deployment/runtime integration.  
- **Next improvement candidate**: improve CLI documentation examples and artifact organization guidance.

## Testing and CI baseline

- **Implemented artifacts**: `tests/`, `.github/workflows/ci.yml`, `pyproject.toml`.  
- **Why it matters technically**: enforces local deterministic regression checks using test automation.  
- **GTV relevance (conservative)**: shows repeatable engineering discipline and verification practices.  
- **Current limitation**: test-only CI with limited quality dimensions beyond deterministic status behavior.  
- **Next improvement candidate**: add targeted tests for response formatting and documentation-linked invariants.

## Limitations and non-goals

- **Implemented artifacts**: `README.md`, `docs/roadmap.md`, `docs/evidence-backlog.md`.  
- **Why it matters technically**: maintains explicit scope boundaries and reduces risk of overstated claims.  
- **GTV relevance (conservative)**: supports credibility by documenting what is and is not currently implemented.  
- **Current limitation**: conservative scope means capability breadth remains early-stage.  
- **Next improvement candidate**: maintain periodic evidence updates tied to completed deterministic milestones.
