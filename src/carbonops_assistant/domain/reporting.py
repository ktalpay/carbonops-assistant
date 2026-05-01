from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

ALLOWED_RESULT_STATUSES = frozenset({"calculated", "needs_more_context", "unsupported", "review_required"})
ALLOWED_REVIEW_STATUSES = frozenset({"not_reviewed", "needs_review", "reviewed", "rejected"})


def _decimal_to_string(value: Decimal | None) -> str | None:
    return str(value) if value is not None else None


@dataclass(frozen=True)
class ReportingResult:
    result_id: str
    input_id: str
    result_status: str
    activity_label: str | None = None
    activity_amount: Decimal | None = None
    activity_unit: str | None = None
    emission_factor_value: Decimal | None = None
    emission_factor_unit: str | None = None
    calculated_emissions_value: Decimal | None = None
    calculated_emissions_unit: str | None = None
    warnings: tuple[str, ...] = field(default_factory=tuple)
    unsupported_reasons: tuple[str, ...] = field(default_factory=tuple)
    assumptions: tuple[str, ...] = field(default_factory=tuple)
    review_status: str = "not_reviewed"

    def __post_init__(self) -> None:
        if self.result_status not in ALLOWED_RESULT_STATUSES:
            allowed = ", ".join(sorted(ALLOWED_RESULT_STATUSES))
            raise ValueError(f"Unsupported result status: {self.result_status}. Allowed: {allowed}")

        if self.review_status not in ALLOWED_REVIEW_STATUSES:
            allowed = ", ".join(sorted(ALLOWED_REVIEW_STATUSES))
            raise ValueError(f"Unsupported review status: {self.review_status}. Allowed: {allowed}")

        object.__setattr__(self, "warnings", tuple(self.warnings))
        object.__setattr__(self, "unsupported_reasons", tuple(self.unsupported_reasons))
        object.__setattr__(self, "assumptions", tuple(self.assumptions))

    def to_dict(self) -> dict[str, object]:
        return {
            "result_id": self.result_id,
            "input_id": self.input_id,
            "result_status": self.result_status,
            "activity_label": self.activity_label,
            "activity_amount": _decimal_to_string(self.activity_amount),
            "activity_unit": self.activity_unit,
            "emission_factor_value": _decimal_to_string(self.emission_factor_value),
            "emission_factor_unit": self.emission_factor_unit,
            "calculated_emissions_value": _decimal_to_string(self.calculated_emissions_value),
            "calculated_emissions_unit": self.calculated_emissions_unit,
            "warnings": list(self.warnings),
            "unsupported_reasons": list(self.unsupported_reasons),
            "assumptions": list(self.assumptions),
            "review_status": self.review_status,
        }
