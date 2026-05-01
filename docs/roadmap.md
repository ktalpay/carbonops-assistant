# CarbonOps Assistant Roadmap

This roadmap tracks small, reviewable increments. Planned items are not claims of current functionality.

## Implemented baseline

- Python package and CLI baseline
- Deterministic response contract and guardrails
- Response statuses: `answered`, `unsupported`, `needs_more_context`
- Deterministic emissions calculation helpers
- Basic unit normalization helpers
- Sample question fixture
- Unit test baseline
- Test-only continuous integration
- Deterministic local evaluation case loader and status-check runner
- Deterministic local knowledge-base loading/search baseline
- Deterministic orchestrator that combines guardrails and optional knowledge lookups

## Next focus

- Parser input contract
- Sample question schema validation
- Source metadata model
- Reporting result contract
- Clearer public examples for supported and unsupported questions

## Later increments

- Emission factor parsing
- CSV and table parsing
- Expanded unit normalization
- Evaluation summary output
- Reporting result rendering

## Non-goals

- Production deployment claims
- Regulatory/certification claims
- Complete emissions accounting coverage
- External paid service dependencies
- Automated regulatory filing
