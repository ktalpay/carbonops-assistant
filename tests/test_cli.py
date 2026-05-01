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
