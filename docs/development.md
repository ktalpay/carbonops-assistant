# Development

CarbonOps Assistant is a pre-alpha Python project intended for local development and testing.

## Local Environment

Use Python 3.11 or newer from the repository root.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Editable installation is recommended because the project uses a `src` layout.

## Running the CLI

After editable installation:

```bash
carbonops-assistant
python -m carbonops_assistant.cli
```

The CLI only prints local project status information. It does not call external services.

## Running Tests

```bash
python -m pytest -q
```

Run tests before committing changes.

## Expected Workflow

1. Create or update a focused module.
2. Add or update unit tests for deterministic behavior.
3. Run `python -m pytest -q`.
4. Review changed files with `git status` and `git diff`.
5. Commit only passing, focused changes.

Keep dependencies minimal. Do not add deployment, publishing, cloud infrastructure, authentication, or external paid service requirements without an explicit project decision.
