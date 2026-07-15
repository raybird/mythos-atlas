#!/usr/bin/env python3
"""Tests for Phoenician culture enrichment — TDD RED phase.

Validates that new gods/stories/comparisons pages meet project standards:
1. File exists
2. First heading is h1
3. Content >= 300 characters (body text, excluding headings/metadata)
4. Has a reference/citation section (## 參考文獻 or ## 參考來源)
5. Reference section is non-empty
6. Contains cross-cultural comparison content
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CULTURE = "phoenician"

NEW_PAGES = {
    "gods": ["eshmun.md"],
    "stories": ["horon-vs-serpent.md"],
    "comparisons": ["phoenician-greek-underworld.md"],
}

REF_PATTERN = re.compile(
    r"^#{2,4}\s*(參考文獻|參考來源|參考資料|References|Sources|Bibliography)\s*$",
    re.MULTILINE,
)

CROSS_CULTURAL_KEYWORDS = [
    "希臘", "希腊", "Greek",
    "埃及", "Egyptian",
    "美索不達米亞", "Mesopotamian",
    "印度", "Hindu",
    "北歐", "Norse",
    "赫梯", "Hittite",
    "跨文化", "平行", "對應",
]


def count_body_chars(text: str) -> int:
    """Count characters in body text, excluding headings and metadata lines."""
    lines = text.split("\n")
    body_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if stripped.startswith("- **") and "：" in stripped:
            continue
        if stripped == "---":
            continue
        body_lines.append(stripped)
    return len("".join(body_lines))


def test_file_exists(path: Path) -> bool:
    return path.exists()


def test_heading_hierarchy(text: str) -> bool:
    headings = [(i, l.strip()) for i, l in enumerate(text.split("\n"), 1) if l.strip().startswith("#")]
    if not headings:
        return False
    first_level = len(headings[0][1]) - len(headings[0][1].lstrip("#"))
    if first_level != 1:
        return False
    prev = 1
    for ln, h in headings[1:]:
        level = len(h) - len(h.lstrip("#"))
        if level > prev + 1:
            return False
        prev = level
    return True


def test_min_length(text: str, min_chars: int = 300) -> bool:
    return count_body_chars(text) >= min_chars


def test_has_citation(text: str) -> bool:
    matches = list(REF_PATTERN.finditer(text))
    if not matches:
        return False
    remaining = text[matches[-1].end():].strip()
    ref_lines = sum(
        1 for l in remaining.split("\n")
        if l.strip() and not l.strip().startswith("#") and not l.strip().startswith(">")
    )
    return ref_lines > 0


def test_has_cross_cultural(text: str) -> bool:
    for kw in CROSS_CULTURAL_KEYWORDS:
        if kw in text:
            return True
    return False


def main():
    errors = []
    for category, files in NEW_PAGES.items():
        for filename in files:
            path = ROOT / "cultures" / CULTURE / category / filename
            label = f"{category}/{filename}"

            if not test_file_exists(path):
                errors.append(f"[FAIL] {label}: file does not exist")
                continue

            text = path.read_text(encoding="utf-8")

            if not test_heading_hierarchy(text):
                errors.append(f"[FAIL] {label}: heading hierarchy broken")

            char_count = count_body_chars(text)
            if not test_min_length(text):
                errors.append(f"[FAIL] {label}: body too short ({char_count} chars, need >= 300)")

            if not test_has_citation(text):
                errors.append(f"[FAIL] {label}: missing or empty citation section")

            if not test_has_cross_cultural(text):
                errors.append(f"[FAIL] {label}: no cross-cultural comparison content")

            print(f"  {label}: {char_count} chars — {'PASS' if not any(label in e for e in errors) else 'FAIL'}")

    if errors:
        print(f"\n{len(errors)} test(s) FAILED:")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)
    else:
        print("\nAll tests PASSED.")
        sys.exit(0)


if __name__ == "__main__":
    main()
