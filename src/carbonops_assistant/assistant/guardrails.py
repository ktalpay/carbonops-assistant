from carbonops_assistant.assistant.response_contract import AssistantResponse

RISKY_CLAIM_TERMS = (
    "certified",
    "regulatory approved",
    "compliant",
    "compliance certification",
    "production-ready",
    "complete emissions accounting",
)


def risky_claim_terms(text: str) -> tuple[str, ...]:
    lowered = text.lower()
    return tuple(term for term in RISKY_CLAIM_TERMS if term in lowered)


def has_risky_claim_language(text: str) -> bool:
    return bool(risky_claim_terms(text))


def is_empty_input(question: str | None) -> bool:
    return question is None or not question.strip()


def requires_more_context(question: str) -> bool:
    normalized = " ".join(question.lower().split())
    if not normalized:
        return True

    vague_questions = {
        "calculate emissions",
        "estimate emissions",
        "what are my emissions",
        "what is our footprint",
        "can you calculate this",
        "is this okay",
    }
    if normalized in vague_questions:
        return True

    asks_for_calculation = any(word in normalized for word in ("calculate", "estimate"))
    mentions_emissions = any(word in normalized for word in ("emission", "footprint", "carbon"))
    has_numeric_context = any(character.isdigit() for character in normalized)
    return asks_for_calculation and mentions_emissions and not has_numeric_context


def limitations_required(status: str, uncertain: bool = False) -> bool:
    return uncertain or status in {"unsupported", "needs_more_context"}


def has_required_limitations(response: AssistantResponse, uncertain: bool = False) -> bool:
    if not limitations_required(response.status, uncertain):
        return True
    return bool(response.limitations)


def respond_to_question(question: str | None) -> AssistantResponse:
    if is_empty_input(question):
        return AssistantResponse(
            answer="Please provide a question with enough context to evaluate.",
            status="needs_more_context",
            limitations=("Empty input cannot be evaluated.",),
        )

    assert question is not None
    risky_terms = risky_claim_terms(question)
    if risky_terms:
        return AssistantResponse(
            answer="This project cannot support regulatory, certification, or assurance claims.",
            status="unsupported",
            limitations=(
                "The current baseline is not suitable for regulatory approval, certification, or assurance decisions.",
            ),
            assumptions=(f"Detected risky terms: {', '.join(risky_terms)}",),
        )

    if requires_more_context(question):
        return AssistantResponse(
            answer="More activity data and emission factor context are needed before a deterministic answer can be given.",
            status="needs_more_context",
            limitations=("The question does not include enough activity data, factors, or boundaries.",),
        )

    return AssistantResponse(
        answer="The question can be handled by a future deterministic assistant workflow.",
        status="answered",
        limitations=("This baseline does not call an LLM or external data source.",),
    )
