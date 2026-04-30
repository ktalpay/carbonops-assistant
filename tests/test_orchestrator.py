from carbonops_assistant.assistant.orchestrator import answer_question
from carbonops_assistant.knowledge.documents import load_markdown_sections


def test_empty_input():
    response = answer_question(" ")
    assert response.status == "needs_more_context"


def test_risky_compliance_wording():
    response = answer_question("Is this certified and compliant?")
    assert response.status == "unsupported"


def test_vague_calculation_question():
    response = answer_question("Calculate emissions")
    assert response.status == "needs_more_context"


def test_knowledge_backed_answer_includes_sources():
    sections = load_markdown_sections("docs/knowledge/base.md")
    response = answer_question("What deterministic support exists?", knowledge_sections=sections)
    assert response.status == "answered"
    assert len(response.sources) >= 1


def test_conservative_without_knowledge_base():
    response = answer_question("What assumptions should be listed for an estimate?")
    assert response.status == "answered"
    assert "no local knowledge base" in response.answer.lower()
