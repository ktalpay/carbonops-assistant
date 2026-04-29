from carbonops_assistant.assistant.guardrails import (
    has_required_limitations,
    has_risky_claim_language,
    requires_more_context,
    respond_to_question,
)
from carbonops_assistant.assistant.response_contract import AssistantResponse


def test_empty_input_returns_needs_more_context() -> None:
    response = respond_to_question("   ")

    assert response.status == "needs_more_context"
    assert response.limitations


def test_risky_compliance_language_detection() -> None:
    assert has_risky_claim_language("Can you say this is certified and compliant?")

    response = respond_to_question("Can you certify this as compliant?")
    assert response.status == "unsupported"
    assert response.limitations


def test_question_requires_more_context() -> None:
    assert requires_more_context("calculate emissions")

    response = respond_to_question("Estimate emissions")
    assert response.status == "needs_more_context"
    assert response.limitations


def test_limitations_included_where_required() -> None:
    uncertain_response = AssistantResponse(
        answer="This may depend on missing data.",
        status="answered",
        limitations=("Input boundaries are not yet verified.",),
    )

    assert has_required_limitations(uncertain_response, uncertain=True)
