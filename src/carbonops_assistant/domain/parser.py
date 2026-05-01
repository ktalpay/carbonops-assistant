from __future__ import annotations

import re
from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True)
class ParserResult:
    input_id: str
    parser_status: str
    factor_value: Decimal | None = None
    factor_unit: str | None = None
    normalized_unit: str | None = None
    confidence_level: str = "low"
    warnings: tuple[str, ...] = field(default_factory=tuple)
    unsupported_reasons: tuple[str, ...] = field(default_factory=tuple)
    extracted_text: str | None = None
    assumptions: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        allowed_statuses = {"parsed", "needs_more_context", "unsupported"}
        if self.parser_status not in allowed_statuses:
            allowed = ", ".join(sorted(allowed_statuses))
            raise ValueError(f"Unsupported parser status: {self.parser_status}. Allowed: {allowed}")

        allowed_confidence = {"low", "medium", "high"}
        if self.confidence_level not in allowed_confidence:
            allowed = ", ".join(sorted(allowed_confidence))
            raise ValueError(f"Unsupported confidence level: {self.confidence_level}. Allowed: {allowed}")

        object.__setattr__(self, "warnings", tuple(self.warnings))
        object.__setattr__(self, "unsupported_reasons", tuple(self.unsupported_reasons))
        object.__setattr__(self, "assumptions", tuple(self.assumptions))

    def to_dict(self) -> dict[str, object]:
        return {
            "input_id": self.input_id,
            "parser_status": self.parser_status,
            "factor_value": str(self.factor_value) if self.factor_value is not None else None,
            "factor_unit": self.factor_unit,
            "normalized_unit": self.normalized_unit,
            "confidence_level": self.confidence_level,
            "warnings": list(self.warnings),
            "unsupported_reasons": list(self.unsupported_reasons),
            "extracted_text": self.extracted_text,
            "assumptions": list(self.assumptions),
        }


_SUPPORTED_UNIT_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"kg\s*co2e\s*/\s*litre\b", "kgCO2e/litre"),
    (r"kg\s*co2e\s*/\s*l\b", "kgCO2e/litre"),
    (r"kg\s*co2e\s+per\s+litre\b", "kgCO2e/litre"),
    (r"kg\s*co2e\s*/\s*kwh\b", "kgCO2e/kWh"),
    (r"kg\s*co2e\s+per\s+kwh\b", "kgCO2e/kWh"),
    (r"kg\s*co2e\s*/\s*m3\b", "kgCO2e/m3"),
)

_UNIT_PATTERN = "|".join(f"(?P<unit_{index}>{pattern})" for index, (pattern, _) in enumerate(_SUPPORTED_UNIT_PATTERNS))
_FACTOR_PATTERN = re.compile(
    rf"(?P<value>\d+(?:\.\d+)?)\s*(?P<unit>{_UNIT_PATTERN})",
    flags=re.IGNORECASE,
)
_NUMBER_PATTERN = re.compile(r"\d+(?:\.\d+)?")
_EMISSION_UNIT_HINT_PATTERN = re.compile(r"kg\s*co2e\s*(?:/|\bper\b)", flags=re.IGNORECASE)


def _clean_unit(unit: str) -> str:
    collapsed = " ".join(unit.strip().split())
    return re.sub(r"\s*/\s*", "/", collapsed)


def _normalized_unit(unit: str) -> str:
    for pattern, normalized in _SUPPORTED_UNIT_PATTERNS:
        if re.fullmatch(pattern, unit.strip(), flags=re.IGNORECASE):
            return normalized
    raise ValueError(f"Unsupported parser unit: {unit}")


def parse_emission_factor_text(input_id: str, raw_text: str) -> ParserResult:
    text = raw_text.strip()
    if not text:
        return ParserResult(
            input_id=input_id,
            parser_status="unsupported",
            unsupported_reasons=("empty_input",),
        )

    numbers = _NUMBER_PATTERN.findall(text)
    if not numbers:
        return ParserResult(
            input_id=input_id,
            parser_status="unsupported",
            unsupported_reasons=("no_numeric_factor",),
            extracted_text=text,
        )

    candidates = list(_FACTOR_PATTERN.finditer(text))
    if len(candidates) > 1:
        return ParserResult(
            input_id=input_id,
            parser_status="needs_more_context",
            warnings=("multiple_factor_candidates",),
            extracted_text=text,
        )

    if not candidates:
        warning = "unsupported_unit" if _EMISSION_UNIT_HINT_PATTERN.search(text) else "missing_unit"
        return ParserResult(
            input_id=input_id,
            parser_status="needs_more_context",
            warnings=(warning,),
            extracted_text=text,
        )

    candidate = candidates[0]
    factor_unit = _clean_unit(candidate.group("unit"))
    return ParserResult(
        input_id=input_id,
        parser_status="parsed",
        factor_value=Decimal(candidate.group("value")),
        factor_unit=factor_unit,
        normalized_unit=_normalized_unit(factor_unit),
        confidence_level="medium",
        extracted_text=candidate.group(0).strip(),
    )
