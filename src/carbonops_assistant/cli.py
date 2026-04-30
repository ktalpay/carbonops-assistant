from __future__ import annotations

import argparse

from carbonops_assistant.config import PROJECT_NAME, PROJECT_SCOPE, PROJECT_STATUS
from carbonops_assistant.evaluation.cases import load_cases
from carbonops_assistant.evaluation.report import build_summary
from carbonops_assistant.evaluation.runner import run_cases


def status_message() -> str:
    """Return a conservative local project status message."""
    return (
        f"{PROJECT_NAME}\n"
        f"Status: {PROJECT_STATUS}\n"
        f"Scope: {PROJECT_SCOPE}\n"
        "External services: not used"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="carbonops_assistant.cli")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("status")
    eval_parser = subparsers.add_parser("evaluate")
    eval_parser.add_argument("path")
    eval_parser.add_argument("--json", action="store_true", dest="json_output")

    args = parser.parse_args(argv)

    if args.command in (None, "status"):
        print(status_message())
        return 0

    if args.command == "evaluate":
        try:
            cases = load_cases(args.path)
            summary = build_summary(run_cases(cases))
        except Exception as exc:
            print(f"Evaluation failed: {exc}")
            return 1

        if args.json_output:
            print(summary.to_json())
        else:
            print(
                f"total={summary.total_cases} passed={summary.passed_count} "
                f"failed={summary.failed_count} success={summary.success}"
            )
        return 0 if summary.success else 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
