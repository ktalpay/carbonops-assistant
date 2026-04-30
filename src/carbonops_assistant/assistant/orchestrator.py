from __future__ import annotations

from carbonops_assistant.assistant.guardrails import respond_to_question
from carbonops_assistant.assistant.response_contract import AssistantResponse
from carbonops_assistant.knowledge.search import search_sections
from carbonops_assistant.knowledge.documents import KnowledgeSection

BASELINE_LIMITATION = "This is a deterministic baseline without LLM generation or external data calls."


def answer_question(
    question: str | None,
    knowledge_sections: tuple[KnowledgeSection, ...] | list[KnowledgeSection] | None = None,
) -> AssistantResponse:
    base_response = respond_to_question(question)

    if base_response.status != "answered":
        return base_response

    if not knowledge_sections:
        return AssistantResponse(
            answer="The question appears in-scope, but no local knowledge base was provided for grounded details.",
            status="answered",
            limitations=(BASELINE_LIMITATION,),
        )

    assert question is not None
    matches = search_sections(knowledge_sections, question, limit=2)
    if not matches:
        return AssistantResponse(
            answer="The question appears in-scope, but no relevant local knowledge sections matched the query.",
            status="answered",
            limitations=(BASELINE_LIMITATION,),
        )

    sources = tuple(f"{m.source_path}#{m.id}" for m in matches)
    summary = "; ".join(f"{m.title}: {m.content.splitlines()[0]}" for m in matches)
    return AssistantResponse(
        answer=f"Deterministic knowledge summary: {summary}",
        status="answered",
        limitations=(BASELINE_LIMITATION,),
        sources=sources,
    )
