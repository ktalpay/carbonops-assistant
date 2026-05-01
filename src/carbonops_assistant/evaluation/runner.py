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
    reason: str = ""


@dataclass(frozen=True)
class EvaluationSummary:
    total_cases: int
    passed: int
    failed: int
    failures: tuple[dict[str, str], ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "total_cases": self.total_cases,
            "passed": self.passed,
            "failed": self.failed,
            "failures": list(self.failures),
        }


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
                reason=reason,
            )
        )
    return tuple(results)


def summarize_results(results: tuple[EvaluationResult, ...] | list[EvaluationResult]) -> EvaluationSummary:
    failures = tuple(
        {
            "case_id": result.case_id,
            "expected_status": result.expected_status,
            "actual_status": result.actual_status,
            "reason": result.reason,
        }
        for result in results
        if not result.passed
    )
    passed = sum(1 for result in results if result.passed)
    total_cases = len(results)
    return EvaluationSummary(
        total_cases=total_cases,
        passed=passed,
        failed=total_cases - passed,
        failures=failures,
    )
