from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

from carbonops_assistant.assistant.orchestrator import answer_question
from carbonops_assistant.assistant.response_contract import AssistantResponse
from carbonops_assistant.config import PROJECT_NAME, PROJECT_SCOPE, PROJECT_STATUS
from carbonops_assistant.domain.parser import parse_emission_factor_text
from carbonops_assistant.evaluation.cases import load_cases
from carbonops_assistant.evaluation.runner import run_cases, summarize_results


def status_message() -> str:
    """Return a conservative local project status message."""
    return (
        f"{PROJECT_NAME}\n"
        f"Status: {PROJECT_STATUS}\n"
        f"Scope: {PROJECT_SCOPE}\n"
        "External services: not used"
    )


def format_response(response: AssistantResponse) -> str:
    payload: dict[str, object] = {
        "status": response.status,
        "message": response.answer,
    }
    if response.limitations:
        payload["limitations"] = list(response.limitations)
    if response.assumptions:
        payload["assumptions"] = list(response.assumptions)
    if response.sources:
        payload["sources"] = list(response.sources)
    return json.dumps(payload, indent=2, sort_keys=True)


def format_parser_result(raw_text: str) -> str:
    result = parse_emission_factor_text("cli-input", raw_text)
    return json.dumps(result.to_dict(), indent=2, sort_keys=True)


def format_examples_summary(path: str = "examples/sample_questions.json") -> str:
    cases = load_cases(path)
    results = run_cases(cases)
    return json.dumps(summarize_results(results).to_dict(), indent=2, sort_keys=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="carbonops-assistant",
        description="Run the local CarbonOps Assistant baseline.",
    )
    subparsers = parser.add_subparsers(dest="command")

    ask_parser = subparsers.add_parser(
        "ask",
        help="Run a deterministic local demo question.",
    )
    ask_parser.add_argument("question", help="Question to evaluate locally.")

    parse_factor_parser = subparsers.add_parser(
        "parse-factor",
        help="Parse a narrow local emission factor text snippet.",
    )
    parse_factor_parser.add_argument("raw_text", help="Text snippet to parse locally.")

    subparsers.add_parser(
        "run-examples",
        help="Run deterministic sample question status checks.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> None:
    if argv is None:
        import sys

        argv = sys.argv[1:]

    if not argv:
        print(status_message())
        return

    args = build_parser().parse_args(argv)
    if args.command == "ask":
        print(format_response(answer_question(args.question)))
        return

    if args.command == "parse-factor":
        print(format_parser_result(args.raw_text))
        return

    if args.command == "run-examples":
        print(format_examples_summary())
        return

    print(status_message())


if __name__ == "__main__":
    main()
