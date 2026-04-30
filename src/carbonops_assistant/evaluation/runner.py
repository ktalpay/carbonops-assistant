from __future__ import annotations

from dataclasses import dataclass

from carbonops_assistant.assistant.guardrails import respond_to_question
from carbonops_assistant.evaluation.cases import EvaluationCase


@dataclass(frozen=True)
class EvaluationResult:
    case_id: str
    expected_status: str
    actual_status: str
    passed: bool
    scenario: str = ""
    reason: str = ""


def run_cases(cases: tuple[EvaluationCase, ...] | list[EvaluationCase]) -> tuple[EvaluationResult, ...]:
    results: list[EvaluationResult] = []
    for case in cases:
        response = respond_to_question(case.question)
        passed = response.status == case.expected_status
        reason = "status matched"
        if not passed:
            reason = f"expected={case.expected_status}, actual={response.status}"
        results.append(
            EvaluationResult(
                case_id=case.id,
                expected_status=case.expected_status,
                actual_status=response.status,
                passed=passed,
                scenario=case.scenario,
                reason=reason,
            )
        )
    return tuple(results)
