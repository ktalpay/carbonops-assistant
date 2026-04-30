import json

from carbonops_assistant.evaluation.report import build_summary
from carbonops_assistant.evaluation.runner import EvaluationResult


def test_all_pass_report():
    summary = build_summary([
        EvaluationResult("c1", "answered", "answered", True, scenario="guardrails", reason="status matched"),
        EvaluationResult("c2", "answered", "answered", True, scenario="guardrails", reason="status matched"),
    ])
    assert summary.total_cases == 2
    assert summary.passed_count == 2
    assert summary.failed_count == 0
    assert summary.success is True


def test_mixed_and_failed_details_and_json_stability():
    summary = build_summary([
        EvaluationResult("c1", "answered", "answered", True, scenario="assumptions", reason="status matched"),
        EvaluationResult("c2", "answered", "needs_more_context", False, scenario="context_gaps", reason="expected=answered, actual=needs_more_context"),
    ])
    assert summary.success is False
    assert summary.by_scenario["assumptions"]["passed"] == 1
    assert summary.by_scenario["context_gaps"]["failed"] == 1
    assert summary.failed_cases[0]["case_id"] == "c2"
    parsed = json.loads(summary.to_json())
    assert parsed["failed_count"] == 1
    assert parsed["by_scenario"]["context_gaps"]["total"] == 1
