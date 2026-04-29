from decimal import Decimal

from carbonops_assistant.domain.units import normalize_amount


def _to_decimal(value: Decimal | int | float | str, field_name: str) -> Decimal:
    try:
        return Decimal(str(value))
    except Exception as exc:
        raise ValueError(f"{field_name} must be numeric") from exc


def calculate_emissions(
    activity_amount: Decimal | int | float | str,
    emission_factor: Decimal | int | float | str,
) -> Decimal:
    """Calculate emissions as activity amount multiplied by emission factor."""
    activity = _to_decimal(activity_amount, "activity_amount")
    factor = _to_decimal(emission_factor, "emission_factor")

    if activity < 0:
        raise ValueError("activity_amount must be greater than or equal to zero")
    if factor < 0:
        raise ValueError("emission_factor must be greater than or equal to zero")

    return activity * factor


def calculate_emissions_for_unit(
    activity_amount: Decimal | int | float | str,
    activity_unit: str,
    emission_factor_per_canonical_unit: Decimal | int | float | str,
) -> Decimal:
    normalized_activity = normalize_amount(activity_amount, activity_unit)
    return calculate_emissions(normalized_activity, emission_factor_per_canonical_unit)
