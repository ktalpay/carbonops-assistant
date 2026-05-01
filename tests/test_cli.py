import json

from carbonops_assistant.cli import main


def run_cli(capsys, *args: str) -> dict[str, object]:
    main(args)
    captured = capsys.readouterr()
    return json.loads(captured.out)


def test_demo_command_answers_safe_question(capsys) -> None:
    output = run_cli(
        capsys,
        "ask",
        "Calculate emissions for 100 litres with factor 2.68 kgCO2e/litre.",
    )

    assert output["status"] == "answered"
    assert "no local knowledge base" in output["message"]


def test_demo_command_returns_unsupported(capsys) -> None:
    output = run_cli(capsys, "ask", "Is this compliant?")

    assert output["status"] == "unsupported"
    assert "limitations" in output


def test_demo_command_needs_more_context(capsys) -> None:
    output = run_cli(capsys, "ask", "Calculate emissions")

    assert output["status"] == "needs_more_context"
    assert "limitations" in output


def test_demo_command_requires_no_external_service_configuration(capsys, monkeypatch) -> None:
    monkeypatch.delenv("CARBONOPS_PROVIDER_KEY", raising=False)

    output = run_cli(capsys, "ask", "What assumptions should be listed for an estimate?")

    assert output["status"] == "answered"


def test_parse_factor_command_returns_parsed_diesel_result(capsys) -> None:
    output = run_cli(capsys, "parse-factor", "Diesel combustion factor: 2.68 kgCO2e/litre")

    assert output["parser_status"] == "parsed"
    assert output["factor_value"] == "2.68"
    assert output["factor_unit"] == "kgCO2e/litre"
    assert output["normalized_unit"] == "kgCO2e/litre"
    assert output["warnings"] == []
    assert output["unsupported_reasons"] == []


def test_parse_factor_command_returns_needs_more_context(capsys) -> None:
    output = run_cli(capsys, "parse-factor", "Factor: 2.68")

    assert output["parser_status"] == "needs_more_context"
    assert output["warnings"] == ["missing_unit"]


def test_parse_factor_command_returns_unsupported_for_empty_input(capsys) -> None:
    output = run_cli(capsys, "parse-factor", "")

    assert output["parser_status"] == "unsupported"
    assert output["unsupported_reasons"] == ["empty_input"]


def test_parse_factor_command_returns_unsupported_for_no_numeric_input(capsys) -> None:
    output = run_cli(capsys, "parse-factor", "Diesel factor pending")

    assert output["parser_status"] == "unsupported"
    assert output["unsupported_reasons"] == ["no_numeric_factor"]


def test_run_examples_command_returns_summary(capsys) -> None:
    output = run_cli(capsys, "run-examples")

    assert output["total_cases"] == 12
    assert output["passed"] == 12
    assert output["failed"] == 0
    assert output["failures"] == []


def test_run_examples_command_requires_no_external_service_configuration(capsys, monkeypatch) -> None:
    monkeypatch.delenv("CARBONOPS_PROVIDER_KEY", raising=False)

    output = run_cli(capsys, "run-examples")

    assert output["failed"] == 0
