import json

import pytest

from carbonops_assistant.evaluation.cases import load_cases


def test_valid_case_loading(tmp_path):
    path = tmp_path / "cases.json"
    path.write_text(json.dumps([{"id": "c1", "question": "hello", "expected_status": "answered"}]), encoding="utf-8")
    cases = load_cases(path)
    assert len(cases) == 1
    assert cases[0].id == "c1"


def test_missing_required_field(tmp_path):
    path = tmp_path / "cases.json"
    path.write_text(json.dumps([{"id": "c1", "question": "hello"}]), encoding="utf-8")
    with pytest.raises(ValueError, match="missing required fields"):
        load_cases(path)


def test_invalid_expected_status(tmp_path):
    path = tmp_path / "cases.json"
    path.write_text(json.dumps([{"id": "c1", "question": "hello", "expected_status": "bad"}]), encoding="utf-8")
    with pytest.raises(ValueError, match="invalid expected_status"):
        load_cases(path)


def test_sample_questions_file_can_be_loaded():
    cases = load_cases("examples/sample_questions.json")
    assert len(cases) >= 1
