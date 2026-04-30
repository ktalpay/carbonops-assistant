# CarbonOps Assistant Roadmap

## Implemented baseline

- Python package and CLI baseline
- Deterministic response contract and guardrails
- Deterministic units/emissions helpers
- Deterministic local evaluation runner
- Deterministic local knowledge-base loading/search baseline
- Deterministic orchestrator that combines guardrails and optional knowledge lookups

## Next focus

- Expand scenario-family evaluation cases with explicit deterministic expectations
- Add tighter deterministic regression tests for response formatting and limits language
- Improve local artifact navigation for reviewer-friendly run comparisons
- Progress evidence-backlog items in small, test-backed increments

## Non-Goals

- Production deployment claims
- Regulatory/certification claims
- Complete emissions accounting coverage
- External paid service dependencies

## Current evaluation status

- Scenario-family deterministic evaluation fixtures are implemented.
- Deterministic summary reporting with scenario-level aggregation is implemented.
- Local CLI evaluation command and JSON summary output are implemented.
- Deterministic snapshot save/load helpers and snapshot diff tooling are implemented.

## Next-phase candidates

- add markdown report export for run history comparisons
- expand diffing beyond status transitions only when stable and justified

## Evidence consolidation status (2026-04-30)

- Technical evidence index is implemented at `docs/evidence/index.md`.
- Deterministic evaluation architecture summary is implemented at `docs/evaluation/architecture.md`.
- README navigation now links evidence and architecture docs for reviewer access.

