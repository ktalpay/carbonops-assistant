# CarbonOps Assistant Roadmap

## Implemented baseline

- Python package and CLI baseline
- Deterministic response contract and guardrails
- Deterministic units/emissions helpers
- Deterministic local evaluation runner
- Deterministic local knowledge-base loading/search baseline
- Deterministic orchestrator that combines guardrails and optional knowledge lookups

## Next focus

- Expand sample evaluation cases with clearer expected reasoning notes
- Improve orchestrator answer templates while keeping conservative behavior
- Add tighter tests for limitations/sources formatting
- Prepare evidence-oriented backlog and issue queue

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
