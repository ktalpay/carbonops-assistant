import json
from decimal import Decimal

import pytest

from carbonops_assistant.domain.reporting import ReportingResult


def test_valid_calculated_result() -> None:
    result = ReportingResult(
        result_id="result-001",
        input_id="input-001",
        result_status="calculated",
        activity_label="diesel combustion",
        activity_amount=Decimal("100"),
        activity_unit="litre",
        emission_factor_value=Decimal("2.68"),
        emission_factor_unit="kgCO2e/litre",
        calculated_emissions_value=Decimal("268"),
        calculated_emissions_unit="kgCO2e",
        review_status="needs_review",
    )

    assert result.result_status == "calculated"
    assert result.calculated_emissions_value == Decimal("268")
    assert result.review_status == "needs_review"


def test_invalid_result_status_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Unsupported result status"):
        ReportingResult(result_id="result-001", input_id="input-001", result_status="final")


def test_invalid_review_status_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Unsupported review status"):
        ReportingResult(
            result_id="result-001",
            input_id="input-001",
            result_status="calculated",
            review_status="approved",
        )


def test_to_dict_is_json_friendly() -> None:
    result = ReportingResult(
        result_id="result-001",
        input_id="input-001",
        result_status="calculated",
        activity_amount=Decimal("100"),
        emission_factor_value=Decimal("2.68"),
        calculated_emissions_value=Decimal("268"),
        warnings=("missing_source_reference",),
        assumptions=("Example factor supplied by local input.",),
    )

    serialized = result.to_dict()

    assert serialized["activity_amount"] == "100"
    assert serialized["emission_factor_value"] == "2.68"
    assert serialized["calculated_emissions_value"] == "268"
    assert serialized["warnings"] == ["missing_source_reference"]
    assert serialized["assumptions"] == ["Example factor supplied by local input."]
    json.dumps(serialized)


def test_calculated_status_does_not_imply_reviewed_status() -> None:
    result = ReportingResult(
        result_id="result-001",
        input_id="input-001",
        result_status="calculated",
        calculated_emissions_value=Decimal("268"),
        calculated_emissions_unit="kgCO2e",
    )

    assert result.result_status == "calculated"
    assert result.review_status == "not_reviewed"
