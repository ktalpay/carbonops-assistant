"""Small deterministic domain helpers."""

from carbonops_assistant.domain.emissions import calculate_emissions
from carbonops_assistant.domain.units import normalize_amount, normalize_unit

__all__ = ["calculate_emissions", "normalize_amount", "normalize_unit"]
