from decimal import Decimal

import pytest

from carbonops_assistant.domain.emissions import (
    calculate_emissions,
    calculate_emissions_for_unit,
)


def test_basic_emissions_calculation() -> None:
    assert calculate_emissions("100", "0.42") == Decimal("42.00")


def test_decimal_precision_behavior_is_not_rounded() -> None:
    assert calculate_emissions(Decimal("1.25"), Decimal("0.456")) == Decimal("0.57000")


def test_negative_activity_value_is_rejected() -> None:
    with pytest.raises(ValueError, match="activity_amount must be greater than or equal to zero"):
        calculate_emissions("-1", "0.5")


def test_negative_emission_factor_is_rejected() -> None:
    with pytest.raises(ValueError, match="emission_factor must be greater than or equal to zero"):
        calculate_emissions("1", "-0.5")


def test_emissions_calculation_with_unit_normalization() -> None:
    assert calculate_emissions_for_unit("1.5", "MWh", "0.4") == Decimal("600.00")
