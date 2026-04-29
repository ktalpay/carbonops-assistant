from carbonops_assistant import PROJECT_NAME, PROJECT_STATUS
from carbonops_assistant.cli import status_message


def test_package_imports() -> None:
    assert PROJECT_NAME == "CarbonOps Assistant"
    assert PROJECT_STATUS == "pre-alpha"


def test_cli_status_message_is_conservative() -> None:
    message = status_message()

    assert "CarbonOps Assistant" in message
    assert "pre-alpha" in message
    assert "External services: not used" in message
