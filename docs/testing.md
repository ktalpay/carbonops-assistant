# Testing

## Test Command

```bash
python -m pytest -q
```

## Current Coverage

The current tests cover:

- package imports
- the conservative local CLI status message

As the project grows, tests should continue to favor deterministic behavior and small units.

## Not Tested Yet

The project does not yet test:

- assistant response contracts
- guardrail behavior
- emissions calculation helpers
- evaluation datasets or benchmark scoring
- integrations with external services

External service behavior is intentionally outside the current baseline.

## Future Evaluation Tests

Evaluation tests may be added later as structured cases with:

- a stable question identifier
- the user question
- expected response status
- expected limitation or unsupported-behavior notes

These evaluation cases should remain conservative and should not require an LLM provider for the initial baseline.
