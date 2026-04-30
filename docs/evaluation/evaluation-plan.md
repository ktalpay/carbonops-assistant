# Evaluation Plan

## Current baseline

The repository now includes a deterministic evaluation runner that:

- loads JSON case files
- validates required fields (`id`, `question`, `expected_status`)
- validates `expected_status` against the response contract
- executes questions through deterministic guardrails
- returns pass/fail records with expected and actual statuses

## Case format

Evaluation case objects use:

- `id`
- `question`
- `expected_status`
- `notes` (optional)

Allowed statuses:

- `answered`
- `unsupported`
- `needs_more_context`

## Scope limits

This baseline evaluates deterministic local behavior only. It does not evaluate LLM outputs, regulatory readiness, or complete emissions accounting behavior.

## Next evaluation improvements

- add more edge-case questions for boundary and assumption clarity
- add summary reporting for pass-rate snapshots
- add stable regression fixtures for orchestrator responses
