from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from carbonops_assistant.assistant.response_contract import ALLOWED_STATUSES

REQUIRED_FIELDS = ("id", "question", "expected_status")
SCENARIO_FILE_REQUIRED_FIELDS = REQUIRED_FIELDS + ("scenario",)


@dataclass(frozen=True)
class EvaluationCase:
    id: str
    question: str
    expected_status: str
    scenario: str = ""
    notes: str = ""


def _validate_case(raw: dict, index: int, *, require_scenario: bool) -> EvaluationCase:
    required = SCENARIO_FILE_REQUIRED_FIELDS if require_scenario else REQUIRED_FIELDS
    missing = [field for field in required if field not in raw]
    if missing:
        raise ValueError(f"Case at index {index} missing required fields: {', '.join(missing)}")

    expected_status = str(raw["expected_status"])
    if expected_status not in ALLOWED_STATUSES:
        allowed = ", ".join(sorted(ALLOWED_STATUSES))
        raise ValueError(f"Case '{raw['id']}' has invalid expected_status '{expected_status}'. Allowed: {allowed}")

    return EvaluationCase(
        id=str(raw["id"]),
        question=str(raw["question"]),
        expected_status=expected_status,
        scenario=str(raw.get("scenario", "")),
        notes=str(raw.get("notes", "")),
    )


def load_cases(path: str | Path) -> tuple[EvaluationCase, ...]:
    path_obj = Path(path)
    data = json.loads(path_obj.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Evaluation cases file must contain a JSON list")

    require_scenario = path_obj.parent.name == "evaluation"
    return tuple(_validate_case(item, index, require_scenario=require_scenario) for index, item in enumerate(data))
