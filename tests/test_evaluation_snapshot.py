import json

import pytest

from carbonops_assistant.evaluation.snapshot import load_report_snapshot, save_report_snapshot


def _sample_report() -> dict:
    return {
        "total_cases": 2,
        "passed_count": 1,
        "failed_count": 1,
        "success": False,
        "by_scenario": {
            "context_gaps": {"total": 1, "passed": 0, "failed": 1},
            "assumptions": {"total": 1, "passed": 1, "failed": 0},
        },
        "failed_cases": [
            {
                "case_id": "c2",
                "scenario": "context_gaps",
                "expected_status": "answered",
                "actual_status": "needs_more_context",
                "reason": "expected=answered, actual=needs_more_context",
            }
        ],
    }


def test_save_and_load_snapshot_and_failed_details(tmp_path):
    path = tmp_path / "snapshot.json"
    save_report_snapshot(_sample_report(), path)
    loaded = load_report_snapshot(path)
    assert loaded["failed_cases"][0]["case_id"] == "c2"
    assert loaded["failed_cases"][0]["reason"]


def test_snapshot_json_is_deterministic(tmp_path):
    path = tmp_path / "snapshot.json"
    save_report_snapshot(_sample_report(), path)
    first = path.read_text(encoding="utf-8")
    save_report_snapshot(_sample_report(), path)
    second = path.read_text(encoding="utf-8")
    assert first == second
    parsed = json.loads(first)
    assert list(parsed["by_scenario"].keys()) == ["assumptions", "context_gaps"]


def test_missing_required_fields_raise_clear_error(tmp_path):
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps({"total_cases": 1}), encoding="utf-8")
    with pytest.raises(ValueError, match="missing required fields"):
        load_report_snapshot(path)
