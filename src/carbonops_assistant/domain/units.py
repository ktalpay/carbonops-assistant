from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class UnitNormalization:
    canonical_unit: str
    multiplier: Decimal


_UNIT_NORMALIZATIONS = {
    "wh": UnitNormalization("kwh", Decimal("0.001")),
    "watt-hour": UnitNormalization("kwh", Decimal("0.001")),
    "watt-hours": UnitNormalization("kwh", Decimal("0.001")),
    "kwh": UnitNormalization("kwh", Decimal("1")),
    "kilowatt-hour": UnitNormalization("kwh", Decimal("1")),
    "kilowatt-hours": UnitNormalization("kwh", Decimal("1")),
    "mwh": UnitNormalization("kwh", Decimal("1000")),
    "megawatt-hour": UnitNormalization("kwh", Decimal("1000")),
    "megawatt-hours": UnitNormalization("kwh", Decimal("1000")),
    "gco2e": UnitNormalization("kg_co2e", Decimal("0.001")),
    "g_co2e": UnitNormalization("kg_co2e", Decimal("0.001")),
    "kgco2e": UnitNormalization("kg_co2e", Decimal("1")),
    "kg_co2e": UnitNormalization("kg_co2e", Decimal("1")),
    "tco2e": UnitNormalization("kg_co2e", Decimal("1000")),
    "t_co2e": UnitNormalization("kg_co2e", Decimal("1000")),
}


def _to_decimal(value: Decimal | int | float | str, field_name: str) -> Decimal:
    try:
        return Decimal(str(value))
    except Exception as exc:
        raise ValueError(f"{field_name} must be numeric") from exc


def get_unit_normalization(unit: str) -> UnitNormalization:
    normalized = unit.strip().lower().replace(" ", "-")
    try:
        return _UNIT_NORMALIZATIONS[normalized]
    except KeyError as exc:
        supported = ", ".join(sorted(_UNIT_NORMALIZATIONS))
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {supported}") from exc


def normalize_unit(unit: str) -> str:
    return get_unit_normalization(unit).canonical_unit


def normalize_amount(value: Decimal | int | float | str, unit: str) -> Decimal:
    amount = _to_decimal(value, "amount")
    if amount < 0:
        raise ValueError("amount must be greater than or equal to zero")

    normalization = get_unit_normalization(unit)
    return amount * normalization.multiplier
