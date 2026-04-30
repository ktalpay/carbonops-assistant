from carbonops_assistant.knowledge.documents import load_markdown_sections
from carbonops_assistant.knowledge.search import search_sections


def test_search_finds_relevant_sections():
    sections = load_markdown_sections("docs/knowledge/base.md")
    results = search_sections(sections, "deterministic emissions")
    assert len(results) >= 1


def test_search_returns_empty_for_unrelated_query():
    sections = load_markdown_sections("docs/knowledge/base.md")
    assert search_sections(sections, "xylophone nebula") == ()


def test_ranking_is_deterministic(tmp_path):
    path = tmp_path / "k.md"
    path.write_text("# One\ncarbon carbon\n# Two\ncarbon", encoding="utf-8")
    sections = load_markdown_sections(path)
    first = search_sections(sections, "carbon")
    second = search_sections(sections, "carbon")
    assert first == second
