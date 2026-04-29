# Evaluation Plan

## Why Evaluation Matters

CarbonOps Assistant is intended to handle carbon and emissions questions conservatively. Evaluation cases help keep behavior consistent as local response contracts, guardrails, and domain helpers evolve.

The current project is pre-alpha and does not run an LLM evaluation pipeline.

## Planned Case Format

Evaluation cases may use JSON objects with fields such as:

- `id`
- `question`
- `expected_status`
- `notes`

Expected statuses should align with the local response contract:

- `answered`
- `unsupported`
- `needs_more_context`

## Unsupported-Question Behavior

Questions requesting certification, regulatory approval, assurance, or unsupported completeness claims should be classified as `unsupported`.

Questions without enough activity data, emission factor context, or boundary information should be classified as `needs_more_context`.

## Future Benchmark Direction

Future evaluation work may add:

- deterministic guardrail test cases
- emissions-helper calculation cases
- structured assistant-response snapshots
- small benchmark reports for local development

Any future benchmark should clearly state its dataset, assumptions, and limitations.

## Current Limitations

The current evaluation plan is a placeholder. It does not measure model quality, factual accuracy against external datasets, reporting readiness, or end-to-end emissions accounting coverage.
