from carbonops_assistant.evaluation.cases import EvaluationCase, load_cases
from carbonops_assistant.evaluation.report import build_summary
from carbonops_assistant.evaluation.runner import run_cases


def test_runner_returns_pass_fail_results():
    cases = (
        EvaluationCase(id="ok", question="Calculate emissions for 10 kWh at 0.4 kg CO2e/kWh", expected_status="answered", scenario="calculation_readiness"),
        EvaluationCase(id="bad", question="Calculate emissions", expected_status="answered", scenario="context_gaps"),
    )
    results = run_cases(cases)
    assert results[0].passed is True
    assert results[1].passed is False
    summary = build_summary(results)
    assert summary.by_scenario["context_gaps"]["failed"] == 1


def test_runner_uses_guardrail_behavior():
    sample_cases = load_cases("examples/sample_questions.json")
    results = run_cases(sample_cases)
    by_id = {r.case_id: r for r in results}
    assert by_id["sq-002"].actual_status == "needs_more_context"
    assert by_id["sq-003"].actual_status == "unsupported"
