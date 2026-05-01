import json
from decimal import Decimal

from carbonops_assistant.domain.parser import parse_emission_factor_text


def test_parses_diesel_factor() -> None:
    result = parse_emission_factor_text("diesel-1", "Diesel combustion factor: 2.68 kgCO2e/litre")

    assert result.parser_status == "parsed"
    assert result.factor_value == Decimal("2.68")
    assert result.factor_unit == "kgCO2e/litre"
    assert result.normalized_unit == "kgCO2e/litre"
    assert result.confidence_level == "medium"
    assert result.warnings == ()
    assert result.unsupported_reasons == ()


def test_parses_electricity_factor() -> None:
    result = parse_emission_factor_text("electricity-1", "Electricity factor: 0.21 kgCO2e/kWh")

    assert result.parser_status == "parsed"
    assert result.factor_value == Decimal("0.21")
    assert result.factor_unit == "kgCO2e/kWh"
    assert result.normalized_unit == "kgCO2e/kWh"


def test_normalizes_per_litre_style() -> None:
    result = parse_emission_factor_text("diesel-2", "Diesel factor: 2.68 kg CO2e per litre")

    assert result.parser_status == "parsed"
    assert result.factor_value == Decimal("2.68")
    assert result.factor_unit == "kg CO2e per litre"
    assert result.normalized_unit == "kgCO2e/litre"


def test_numeric_value_without_unit_needs_more_context() -> None:
    result = parse_emission_factor_text("missing-unit-1", "Factor: 2.68")

    assert result.parser_status == "needs_more_context"
    assert result.warnings == ("missing_unit",)


def test_multiple_numeric_factor_candidates_need_more_context() -> None:
    result = parse_emission_factor_text(
        "multiple-1",
        "Diesel factor: 2.68 kgCO2e/litre. Backup factor: 2.71 kgCO2e/litre.",
    )

    assert result.parser_status == "needs_more_context"
    assert result.factor_value is None
    assert result.warnings == ("multiple_factor_candidates",)


def test_no_numeric_factor_is_unsupported() -> None:
    result = parse_emission_factor_text("no-number-1", "Diesel combustion factor pending.")

    assert result.parser_status == "unsupported"
    assert result.unsupported_reasons == ("no_numeric_factor",)


def test_empty_input_is_unsupported() -> None:
    result = parse_emission_factor_text("empty-1", "  ")

    assert result.parser_status == "unsupported"
    assert result.unsupported_reasons == ("empty_input",)


def test_parser_does_not_require_external_calls(monkeypatch) -> None:
    def fail_external_call(*args, **kwargs):
        raise AssertionError("External call attempted")

    monkeypatch.setattr("socket.create_connection", fail_external_call)
    monkeypatch.setattr("urllib.request.urlopen", fail_external_call)

    result = parse_emission_factor_text("local-1", "Factor 1.5 kgCO2e/m3")

    assert result.parser_status == "parsed"
    assert result.normalized_unit == "kgCO2e/m3"


def test_parsed_result_serializes_to_json_friendly_dict() -> None:
    result = parse_emission_factor_text("diesel-serialized", "Diesel factor: 2.68 kgCO2e/litre")

    serialized = result.to_dict()

    assert serialized == {
        "input_id": "diesel-serialized",
        "parser_status": "parsed",
        "factor_value": "2.68",
        "factor_unit": "kgCO2e/litre",
        "normalized_unit": "kgCO2e/litre",
        "confidence_level": "medium",
        "warnings": [],
        "unsupported_reasons": [],
        "extracted_text": "2.68 kgCO2e/litre",
        "assumptions": [],
    }
    json.dumps(serialized)


def test_context_limited_result_serializes_warning_list() -> None:
    result = parse_emission_factor_text("missing-unit-serialized", "Factor: 2.68")

    serialized = result.to_dict()

    assert serialized["warnings"] == ["missing_unit"]
    assert serialized["unsupported_reasons"] == []
    json.dumps(serialized)


def test_unsupported_result_serializes_cleanly() -> None:
    result = parse_emission_factor_text("empty-serialized", "")

    serialized = result.to_dict()

    assert serialized["factor_value"] is None
    assert serialized["warnings"] == []
    assert serialized["unsupported_reasons"] == ["empty_input"]
    json.dumps(serialized)
