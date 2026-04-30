from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class KnowledgeSection:
    id: str
    title: str
    content: str
    source_path: str


def _slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "section"


def load_markdown_sections(path: str | Path) -> tuple[KnowledgeSection, ...]:
    source = Path(path)
    text = source.read_text(encoding="utf-8")

    sections: list[KnowledgeSection] = []
    title = "Introduction"
    lines: list[str] = []
    seen: dict[str, int] = {}

    def flush(current_title: str, current_lines: list[str]) -> None:
        content = "\n".join(current_lines).strip()
        if not content:
            return
        base = _slugify(current_title)
        seen[base] = seen.get(base, 0) + 1
        suffix = f"-{seen[base]}" if seen[base] > 1 else ""
        sections.append(
            KnowledgeSection(
                id=f"{base}{suffix}",
                title=current_title,
                content=content,
                source_path=str(source),
            )
        )

    for line in text.splitlines():
        if line.startswith("#"):
            flush(title, lines)
            title = line.lstrip("#").strip() or "Untitled"
            lines = []
            continue
        lines.append(line)

    flush(title, lines)
    return tuple(sections)
