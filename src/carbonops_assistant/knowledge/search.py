from __future__ import annotations

from carbonops_assistant.knowledge.documents import KnowledgeSection


def _score(section: KnowledgeSection, terms: tuple[str, ...]) -> int:
    title = section.title.lower()
    content = section.content.lower()
    score = 0
    for term in terms:
        score += title.count(term) * 3
        score += content.count(term)
    return score


def search_sections(
    sections: tuple[KnowledgeSection, ...] | list[KnowledgeSection], query: str, limit: int = 5
) -> tuple[KnowledgeSection, ...]:
    terms = tuple(term for term in query.lower().split() if term)
    if not terms:
        return ()

    ranked = sorted(
        ((section, _score(section, terms)) for section in sections),
        key=lambda item: (-item[1], item[0].id),
    )
    return tuple(section for section, score in ranked if score > 0)[:limit]
