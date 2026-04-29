import pytest

from carbonops_assistant.assistant.response_contract import AssistantResponse, build_response


def test_valid_response_creation() -> None:
    response = build_response(
        answer="Use the provided activity data and factor.",
        status="answered",
        assumptions=["Activity data is in kWh."],
        limitations=["Example only."],
        sources=["local test"],
    )

    assert response.status == "answered"
    assert response.assumptions == ("Activity data is in kWh.",)
    assert response.limitations == ("Example only.",)
    assert response.sources == ("local test",)


def test_invalid_status_is_rejected() -> None:
    with pytest.raises(ValueError, match="Unsupported response status"):
        AssistantResponse(answer="No", status="complete")


def test_unsupported_status_requires_limitations() -> None:
    with pytest.raises(ValueError, match="must include at least one limitation"):
        AssistantResponse(answer="Unsupported", status="unsupported")
