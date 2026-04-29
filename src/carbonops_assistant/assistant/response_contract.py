from dataclasses import dataclass, field

ALLOWED_STATUSES = frozenset({"answered", "unsupported", "needs_more_context"})


@dataclass(frozen=True)
class AssistantResponse:
    """Deterministic response shape for local assistant behavior."""

    answer: str
    status: str
    assumptions: tuple[str, ...] = field(default_factory=tuple)
    limitations: tuple[str, ...] = field(default_factory=tuple)
    sources: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.status not in ALLOWED_STATUSES:
            allowed = ", ".join(sorted(ALLOWED_STATUSES))
            raise ValueError(f"Unsupported response status: {self.status}. Allowed: {allowed}")

        object.__setattr__(self, "assumptions", tuple(self.assumptions))
        object.__setattr__(self, "limitations", tuple(self.limitations))
        object.__setattr__(self, "sources", tuple(self.sources))

        if self.status in {"unsupported", "needs_more_context"} and not self.limitations:
            raise ValueError(f"{self.status} responses must include at least one limitation")


def build_response(
    *,
    answer: str,
    status: str,
    assumptions: tuple[str, ...] | list[str] = (),
    limitations: tuple[str, ...] | list[str] = (),
    sources: tuple[str, ...] | list[str] = (),
) -> AssistantResponse:
    return AssistantResponse(
        answer=answer,
        status=status,
        assumptions=tuple(assumptions),
        limitations=tuple(limitations),
        sources=tuple(sources),
    )
