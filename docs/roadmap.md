# CarbonOps Assistant Roadmap

This roadmap tracks small, reviewable increments. Planned items are not claims of current functionality.

## Implemented baseline

- Python package and CLI baseline
- v0.1.0 release candidate documentation prepared
- Deterministic response contract and guardrails
- Response statuses: `answered`, `unsupported`, `needs_more_context`
- Deterministic emissions calculation helpers
- Basic unit normalization helpers
- Sample question fixture
- Sample question schema validation
- Public examples for supported, unsupported, and context-limited questions
- Parser input contract documentation
- Source metadata model documentation
- Reporting result contract documentation
- Unit test baseline
- Test-only continuous integration
- Deterministic local evaluation case loader and status-check runner
- Deterministic local knowledge-base loading/search baseline
- Deterministic orchestrator that combines guardrails and optional knowledge lookups
- Deterministic local demo command
- Minimal text factor parser for narrow public-safe snippets
- Local parser demo command

## Later increments

- Expanded emission factor parsing
- CSV and table parsing
- Source metadata extraction and validation
- Expanded unit normalization
- Parser fixture examples
- Structured parser object
- Structured input/output examples
- Evaluation summary output
- Reporting result implementation and rendering

## Non-goals

- Production deployment claims
- Regulatory/certification claims
- Complete emissions accounting coverage
- External paid service dependencies
- Automated regulatory filing
