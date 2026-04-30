from carbonops_assistant.knowledge.documents import load_markdown_sections


def test_markdown_section_loading(tmp_path):
    path = tmp_path / "k.md"
    path.write_text("# A\nalpha\n# B\nbeta", encoding="utf-8")
    sections = load_markdown_sections(path)
    assert [s.title for s in sections] == ["A", "B"]


def test_stable_section_slugs(tmp_path):
    path = tmp_path / "k.md"
    path.write_text("# Repeat\na\n# Repeat\nb", encoding="utf-8")
    sections = load_markdown_sections(path)
    assert [s.id for s in sections] == ["repeat", "repeat-2"]
