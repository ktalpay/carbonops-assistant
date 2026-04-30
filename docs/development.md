# Development

## Local Environment

Use Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

## Deterministic Modules

Current deterministic modules include:

- `assistant/response_contract.py`
- `assistant/guardrails.py`
- `assistant/orchestrator.py`
- `domain/emissions.py`
- `domain/units.py`
- `evaluation/` case loader and runner
- `knowledge/` Markdown section loader and keyword search

## Workflow

1. Implement a small deterministic change.
2. Add/update tests.
3. Run `python -m pytest -q`.
4. Validate changed files with `git status` and `git diff`.
5. Commit only passing changes.
