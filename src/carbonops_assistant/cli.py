from carbonops_assistant.config import PROJECT_NAME, PROJECT_SCOPE, PROJECT_STATUS


def status_message() -> str:
    """Return a conservative local project status message."""
    return (
        f"{PROJECT_NAME}\n"
        f"Status: {PROJECT_STATUS}\n"
        f"Scope: {PROJECT_SCOPE}\n"
        "External services: not used"
    )


def main() -> None:
    print(status_message())


if __name__ == "__main__":
    main()
