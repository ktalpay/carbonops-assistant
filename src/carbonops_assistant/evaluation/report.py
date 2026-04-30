from __future__ import annotations

import json
from dataclasses import dataclass

from carbonops_assistant.evaluation.runner import EvaluationResult


@dataclass(frozen=True)
class EvaluationSummary:
    total_cases: int
    passed_count: int
    failed_count: int
    success: bool
    by_scenario: dict[str, dict[str, int]]
    failed_cases: tuple[dict[str, str], ...]

    def to_dict(self) -> dict:
        return {
            "total_cases": self.total_cases,
            "passed_count": self.passed_count,
            "failed_count": self.failed_count,
            "success": self.success,
            "by_scenario": self.by_scenario,
            "failed_cases": list(self.failed_cases),
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), sort_keys=True, separators=(",", ":"))


def build_summary(results: tuple[EvaluationResult, ...] | list[EvaluationResult]) -> EvaluationSummary:
    total_cases = len(results)
    passed_count = sum(1 for result in results if result.passed)
    failed_count = total_cases - passed_count
    success = failed_count == 0

    by_scenario: dict[str, dict[str, int]] = {}
    failed_cases: list[dict[str, str]] = []

    for result in results:
        if result.scenario:
            scenario_stats = by_scenario.setdefault(result.scenario, {"total": 0, "passed": 0, "failed": 0})
            scenario_stats["total"] += 1
            scenario_stats["passed"] += int(result.passed)
            scenario_stats["failed"] += int(not result.passed)

        if not result.passed:
            failed_cases.append(
                {
                    "case_id": result.case_id,
                    "scenario": result.scenario,
                    "expected_status": result.expected_status,
                    "actual_status": result.actual_status,
                    "reason": result.reason,
                }
            )

    return EvaluationSummary(
        total_cases=total_cases,
        passed_count=passed_count,
        failed_count=failed_count,
        success=success,
        by_scenario=dict(sorted(by_scenario.items())),
        failed_cases=tuple(failed_cases),
    )
