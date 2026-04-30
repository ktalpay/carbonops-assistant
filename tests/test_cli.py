import json

from carbonops_assistant import cli


def test_status_command_still_works(capsys):
    code = cli.main(["status"])
    out = capsys.readouterr().out
    assert code == 0
    assert "External services: not used" in out


def test_evaluate_text_output(capsys):
    code = cli.main(["evaluate", "examples/evaluation/guardrails.json"])
    out = capsys.readouterr().out
    assert code == 0
    assert "total=" in out and "passed=" in out and "failed=" in out and "success=" in out


def test_evaluate_json_output_parseable(capsys):
    code = cli.main(["evaluate", "examples/evaluation/guardrails.json", "--json"])
    out = capsys.readouterr().out.strip()
    parsed = json.loads(out)
    assert code == 0
    assert parsed["total_cases"] >= 1


def test_evaluate_failure_returns_non_zero(tmp_path, capsys):
    path = tmp_path / "cases.json"
    path.write_text(
        json.dumps([{"id": "x", "question": "Calculate emissions", "expected_status": "answered"}]),
        encoding="utf-8",
    )
    code = cli.main(["evaluate", str(path)])
    _ = capsys.readouterr().out
    assert code != 0


def test_compare_evaluations_text_and_json(tmp_path, capsys):
    previous = tmp_path / "previous.json"
    current = tmp_path / "current.json"
    previous.write_text(json.dumps({
        "total_cases": 2,
        "passed_count": 1,
        "failed_count": 1,
        "success": False,
        "by_scenario": {},
        "failed_cases": [{"case_id": "c1"}],
    }), encoding="utf-8")
    current.write_text(json.dumps({
        "total_cases": 2,
        "passed_count": 0,
        "failed_count": 2,
        "success": False,
        "by_scenario": {},
        "failed_cases": [{"case_id": "c1"}, {"case_id": "c2"}],
    }), encoding="utf-8")

    code = cli.main(["compare-evaluations", str(previous), str(current)])
    out = capsys.readouterr().out
    assert code == 0
    assert "newly_failing=['c2']" in out

    code = cli.main(["compare-evaluations", str(previous), str(current), "--json"])
    out = capsys.readouterr().out.strip()
    assert code == 0
    parsed = json.loads(out)
    assert parsed["newly_failing_case_ids"] == ["c2"]
