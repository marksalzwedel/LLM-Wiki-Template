"""Check the active Obsidian wiki for common template issues.

This script intentionally checks only the active wiki/ folder. The completed
example vault under examples/ is reference material and should not affect the
health of a project created from this template.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
EXAMPLES = ROOT / "examples"

REQUIRED_STARTER_FILES = [
    WIKI / "Project Index.md",
    WIKI / "Entity Page Template.md",
    WIKI / "Contradictions and Tensions.md",
]

REQUIRED_SECTIONS = [
    "## Summary",
    "## Explanation",
    "## Related Links",
]

EXAMPLE_TITLES = {
    "LLM Papers Index",
    "Attention Is All You Need",
    "BERT",
    "Language Models are Few-Shot Learners",
    "On the Opportunities and Risks of Foundation Models",
    "Training Language Models to Follow Instructions with Human Feedback",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def wiki_links(text: str) -> list[str]:
    links = []
    for match in re.findall(r"\[\[([^\]|#]+)", text):
        name = match.strip()
        if name:
            links.append(name)
    return links


def normalized_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def main() -> int:
    issues: list[str] = []
    warnings: list[str] = []

    if not WIKI.exists():
        issues.append("Missing active wiki/ folder.")
        return report(issues, warnings)

    md_files = sorted(WIKI.glob("*.md"))
    page_names = {path.stem for path in md_files}

    for path in REQUIRED_STARTER_FILES:
        if not path.exists():
            issues.append(f"Missing starter page: {path.relative_to(ROOT)}")

    all_links: list[tuple[Path, str]] = []
    for path in md_files:
        text = read_text(path)
        for link in wiki_links(text):
            all_links.append((path, link))

        if path.name not in {"Project Index.md", "Contradictions and Tensions.md"}:
            for heading in REQUIRED_SECTIONS:
                if heading not in text:
                    warnings.append(f"{path.relative_to(ROOT)} is missing {heading}.")

    missing_links = sorted({link for _, link in all_links if link not in page_names})
    for link in missing_links:
        refs = sorted({path.name for path, candidate in all_links if candidate == link})
        issues.append(f"Unresolved wiki link [[{link}]] referenced from {', '.join(refs)}.")

    normalized = Counter(normalized_name(path.stem) for path in md_files)
    duplicates = sorted(name for name, count in normalized.items() if count > 1)
    for name in duplicates:
        pages = sorted(path.name for path in md_files if normalized_name(path.stem) == name)
        warnings.append(f"Possible duplicate concept pages: {', '.join(pages)}.")

    leaked_examples = sorted(path.name for path in md_files if path.stem in EXAMPLE_TITLES)
    for name in leaked_examples:
        warnings.append(
            f"Possible example content in active wiki: wiki/{name}. "
            "Examples should usually stay under examples/."
        )

    if RAW.exists():
        raw_files = [path for path in RAW.iterdir() if path.is_file() and path.name != "README.md"]
        if raw_files and "Project Index" in page_names:
            index_text = read_text(WIKI / "Project Index.md")
            if "Source Documents" in index_text and "- Add source-document pages here" in index_text:
                warnings.append(
                    "raw/ contains source files, but Project Index.md still has the starter "
                    "Source Documents placeholder."
                )

    if not EXAMPLES.exists():
        warnings.append("examples/ folder is missing. This is fine if you intentionally removed examples.")

    return report(issues, warnings)


def report(issues: list[str], warnings: list[str]) -> int:
    print("Wiki health check")
    print("=================")
    print(f"Issues: {len(issues)}")
    for issue in issues:
        print(f"- ERROR: {issue}")
    print(f"Warnings: {len(warnings)}")
    for warning in warnings:
        print(f"- WARN: {warning}")

    if issues:
        print("\nResult: FAIL")
        return 1

    print("\nResult: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
