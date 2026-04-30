import json

from carbonops_assistant.evaluation.diff import compare_snapshots, diff_to_json


def _snap(failed_cases: list[str], success: bool) -> dict:
    return {
        "total_cases": 3,
        "passed_count": 3 - len(failed_cases),
        "failed_count": len(failed_cases),
        "success": success,
        "by_scenario": {},
        "failed_cases": [{"case_id": case_id} for case_id in failed_cases],
    }


def test_diff_newly_failing_newly_passing_and_unchanged():
    previous = _snap(["c2", "c3"], success=False)
    current = _snap(["c3", "c4"], success=False)
    diff = compare_snapshots(previous, current)
    assert diff["newly_failing_case_ids"] == ["c4"]
    assert diff["newly_passing_case_ids"] == ["c2"]
    assert diff["unchanged_failing_case_ids"] == ["c3"]


def test_diff_success_changed_and_deterministic_json():
    previous = _snap(["c2"], success=False)
    current = _snap([], success=True)
    diff = compare_snapshots(previous, current)
    assert diff["success_changed"] is True
    first = diff_to_json(diff)
    second = diff_to_json(diff)
    assert first == second
    parsed = json.loads(first)
    assert parsed["current_failed"] == 0
