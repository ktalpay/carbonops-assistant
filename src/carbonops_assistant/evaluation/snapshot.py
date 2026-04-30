from __future__ import annotations

import json
from pathlib import Path

_REQUIRED_FIELDS = (
    "total_cases",
    "passed_count",
    "failed_count",
    "success",
    "by_scenario",
    "failed_cases",
)


def normalize_report_payload(payload: dict) -> dict:
    missing = [field for field in _REQUIRED_FIELDS if field not in payload]
    if missing:
        missing_fields = ", ".join(missing)
        raise ValueError(f"Snapshot payload missing required fields: {missing_fields}")

    normalized = {
        "total_cases": int(payload["total_cases"]),
        "passed_count": int(payload["passed_count"]),
        "failed_count": int(payload["failed_count"]),
        "success": bool(payload["success"]),
        "by_scenario": dict(sorted(dict(payload["by_scenario"]).items())),
        "failed_cases": list(payload["failed_cases"]),
    }
    return normalized


def save_report_snapshot(report: dict, path: str | Path) -> None:
    snapshot = normalize_report_payload(report)
    Path(path).write_text(
        json.dumps(snapshot, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )


def load_report_snapshot(path: str | Path) -> dict:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Snapshot payload must be a JSON object")
    return normalize_report_payload(payload)
