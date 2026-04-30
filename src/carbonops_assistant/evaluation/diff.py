from __future__ import annotations

import json


def _failed_case_ids(snapshot: dict) -> set[str]:
    return {case["case_id"] for case in snapshot["failed_cases"]}


def compare_snapshots(previous: dict, current: dict) -> dict:
    prev_failed = _failed_case_ids(previous)
    curr_failed = _failed_case_ids(current)

    newly_failing = sorted(curr_failed - prev_failed)
    newly_passing = sorted(prev_failed - curr_failed)
    unchanged_failing = sorted(prev_failed & curr_failed)

    return {
        "previous_total": previous["total_cases"],
        "current_total": current["total_cases"],
        "previous_passed": previous["passed_count"],
        "current_passed": current["passed_count"],
        "previous_failed": previous["failed_count"],
        "current_failed": current["failed_count"],
        "newly_failing_case_ids": newly_failing,
        "newly_passing_case_ids": newly_passing,
        "unchanged_failing_case_ids": unchanged_failing,
        "success_changed": previous["success"] != current["success"],
    }


def diff_to_json(diff: dict) -> str:
    return json.dumps(diff, sort_keys=True, separators=(",", ":"))
