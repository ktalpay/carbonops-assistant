import json

import pytest

from carbonops_assistant.evaluation.cases import load_cases


def test_valid_case_loading(tmp_path):
    path = tmp_path / "cases.json"
    path.write_text(json.dumps([{"id": "c1", "question": "hello", "expected_status": "answered"}]), encoding="utf-8")
    cases = load_cases(path)
    assert len(cases) == 1
    assert cases[0].id == "c1"


def test_scenario_files_load_successfully():
    for file_name in ("guardrails.json", "context_gaps.json", "assumptions.json", "calculation_readiness.json"):
        cases = load_cases(f"examples/evaluation/{file_name}")
        assert len(cases) >= 4
        assert all(case.scenario for case in cases)


def test_missing_scenario_in_scenario_file_is_rejected(tmp_path):
    eval_dir = tmp_path / "evaluation"
    eval_dir.mkdir()
    path = eval_dir / "cases.json"
    path.write_text(json.dumps([{"id": "c1", "question": "hello", "expected_status": "answered"}]), encoding="utf-8")
    with pytest.raises(ValueError, match="missing required fields: scenario"):
        load_cases(path)


def test_invalid_expected_status(tmp_path):
    path = tmp_path / "cases.json"
    path.write_text(json.dumps([{"id": "c1", "question": "hello", "expected_status": "bad"}]), encoding="utf-8")
    with pytest.raises(ValueError, match="invalid expected_status"):
        load_cases(path)


def test_sample_questions_file_can_be_loaded():
    cases = load_cases("examples/sample_questions.json")
    assert len(cases) >= 1
