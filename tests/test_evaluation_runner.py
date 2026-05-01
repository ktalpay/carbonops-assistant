from carbonops_assistant.evaluation.cases import EvaluationCase, load_cases
from carbonops_assistant.evaluation.runner import run_cases, summarize_results


def test_runner_returns_pass_fail_results():
    cases = (
        EvaluationCase(id="ok", question="Calculate emissions for 10 kWh at 0.4 kg CO2e/kWh", expected_status="answered"),
        EvaluationCase(id="bad", question="Calculate emissions", expected_status="answered"),
    )
    results = run_cases(cases)
    assert results[0].passed is True
    assert results[1].passed is False


def test_runner_uses_guardrail_behavior():
    sample_cases = load_cases("examples/sample_questions.json")
    results = run_cases(sample_cases)
    by_id = {r.case_id: r for r in results}
    assert by_id["sq-002"].actual_status == "needs_more_context"
    assert by_id["sq-003"].actual_status == "unsupported"


def test_sample_question_summary_passes_current_fixture():
    sample_cases = load_cases("examples/sample_questions.json")
    summary = summarize_results(run_cases(sample_cases))

    assert summary.total_cases == 12
    assert summary.passed == 12
    assert summary.failed == 0
    assert summary.failures == ()


def test_summary_reports_failures():
    cases = (
        EvaluationCase(id="bad", question="Calculate emissions", expected_status="answered"),
    )
    summary = summarize_results(run_cases(cases))

    assert summary.to_dict() == {
        "total_cases": 1,
        "passed": 0,
        "failed": 1,
        "failures": [
            {
                "case_id": "bad",
                "expected_status": "answered",
                "actual_status": "needs_more_context",
                "reason": "expected=answered, actual=needs_more_context",
            }
        ],
    }
