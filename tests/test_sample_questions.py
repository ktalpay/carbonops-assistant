import json
from pathlib import Path


ALLOWED_STATUSES = {"answered", "unsupported", "needs_more_context"}
REQUIRED_FIELDS = {"id", "question", "expected_status"}


def test_sample_questions_fixture_schema() -> None:
    path = Path(__file__).resolve().parents[1] / "examples" / "sample_questions.json"

    assert path.exists()

    items = json.loads(path.read_text(encoding="utf-8"))

    assert isinstance(items, list)
    assert items

    ids: set[str] = set()
    statuses: set[str] = set()

    for item in items:
        assert isinstance(item, dict)
        assert REQUIRED_FIELDS <= set(item)

        item_id = item["id"]
        question = item["question"]
        expected_status = item["expected_status"]

        assert isinstance(item_id, str)
        assert item_id.strip()
        assert item_id not in ids
        ids.add(item_id)

        assert isinstance(question, str)
        assert question.strip()

        assert expected_status in ALLOWED_STATUSES
        statuses.add(expected_status)

    assert "unsupported" in statuses
    assert "needs_more_context" in statuses
