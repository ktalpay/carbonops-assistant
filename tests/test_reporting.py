import json
from decimal import Decimal

import pytest

from carbonops_assistant.domain.reporting import ReportingResult, render_reporting_result_markdown


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


def test_markdown_renderer_includes_calculated_value() -> None:
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
    )

    rendered = render_reporting_result_markdown(result)

    assert "Calculated emissions: 268 kgCO2e" in rendered
    assert "Activity: diesel combustion 100 litre" in rendered
    assert "Emission factor: 2.68 kgCO2e/litre" in rendered


def test_markdown_renderer_includes_warnings() -> None:
    result = ReportingResult(
        result_id="result-001",
        input_id="input-001",
        result_status="review_required",
        warnings=("missing_source_reference",),
    )

    rendered = render_reporting_result_markdown(result)

    assert "- missing_source_reference" in rendered


def test_markdown_renderer_includes_human_review_note() -> None:
    result = ReportingResult(result_id="result-001", input_id="input-001", result_status="needs_more_context")

    rendered = render_reporting_result_markdown(result)

    assert "This is a local deterministic summary and requires human review." in rendered


def test_markdown_renderer_handles_unsupported_result() -> None:
    result = ReportingResult(
        result_id="result-001",
        input_id="input-001",
        result_status="unsupported",
        unsupported_reasons=("unsupported_reporting_use",),
        review_status="rejected",
    )

    rendered = render_reporting_result_markdown(result)

    assert "Result status: unsupported" in rendered
    assert "Review status: rejected" in rendered
    assert "- unsupported_reporting_use" in rendered
