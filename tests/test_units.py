from decimal import Decimal

import pytest

from carbonops_assistant.domain.units import normalize_amount, normalize_unit


def test_simple_unit_normalization() -> None:
    assert normalize_unit("kWh") == "kwh"
    assert normalize_unit("megawatt-hours") == "kwh"
    assert normalize_unit("tCO2e") == "kg_co2e"


def test_normalize_amount_to_canonical_unit() -> None:
    assert normalize_amount("2.5", "MWh") == Decimal("2500.0")
    assert normalize_amount(750, "gCO2e") == Decimal("0.750")


def test_unsupported_unit_has_clear_error() -> None:
    with pytest.raises(ValueError, match="Unsupported unit: liter"):
        normalize_unit("liter")


def test_negative_amount_is_rejected() -> None:
    with pytest.raises(ValueError, match="amount must be greater than or equal to zero"):
        normalize_amount("-1", "kWh")
