#!/usr/bin/env python3
"""Tests for the Egyptian culture enrichment (Neith / Book of the Heavenly Cow / weaving).

Same contract as test_phoenician_enrichment.py, plus two guards that the
Egyptian corpus previously violated:

  7. Every enrichment page is registered in its own directory README index
  8. No two pages of one culture claim the same English work title
     (a culture must hold one page per myth, not two shells for one text)
  9. New enrichment pages are never parked in scripts/citation_baseline.txt —
     the baseline exists for pre-existing debt, not as an escape hatch
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CULTURE = "egyptian"

NEW_PAGES = {
    "gods": ["奈特.md"],
    "stories": ["天母牛之書.md"],
    "comparisons": ["織機即宇宙：奈特與全球織造創世母題比較.md"],
}

REF_PATTERN = re.compile(
    r"^#{2,4}\s*(參考文獻|參考來源|參考資料|References|Sources|Bibliography)\s*$",
    re.MULTILINE,
)

CROSS_CULTURAL_PATTERN = re.compile(r"^#{2,4}\s*跨文化", re.MULTILINE)

LINK_PATTERN = re.compile(r"\[[^\]]*\]\(((?:[^()\n]|\([^()\n]*\))+)\)")

ENGLISH_TITLE_PATTERN = re.compile(r"[(（]([^)）]+)[)）]\s*$")

CITATION_BASELINE = ROOT / "scripts" / "citation_baseline.txt"


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
    return bool(CROSS_CULTURAL_PATTERN.search(text))


def test_indexed_in_readme(category: str, filename: str) -> bool:
    index = ROOT / "cultures" / CULTURE / category / "README.md"
    if not index.exists():
        return False
    return filename in index.read_text(encoding="utf-8")


def test_not_baselined(path: Path) -> bool:
    if not CITATION_BASELINE.exists():
        return True
    baselined = {
        line.strip()
        for line in CITATION_BASELINE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }
    return str(path.relative_to(ROOT)) not in baselined


def find_duplicate_english_titles(category: str):
    """Return {english_title: [filenames]} for titles claimed by 2+ pages."""
    seen: dict = {}
    for path in sorted((ROOT / "cultures" / CULTURE / category).glob("*.md")):
        if path.name == "README.md":
            continue
        h1 = path.read_text(encoding="utf-8").split("\n")[0]
        match = ENGLISH_TITLE_PATTERN.search(h1)
        if not match:
            continue
        key = match.group(1).strip().lower()
        seen.setdefault(key, []).append(path.name)
    return {k: v for k, v in seen.items() if len(v) > 1}


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
            char_count = count_body_chars(text)
            checks = [
                (test_heading_hierarchy(text), "heading hierarchy broken"),
                (test_min_length(text), f"body too short ({char_count} chars, need >= 300)"),
                (test_has_citation(text), "missing or empty citation section"),
                (test_has_cross_cultural(text), "no cross-cultural section"),
                (test_indexed_in_readme(category, filename), "not listed in directory README.md"),
                (test_not_baselined(path), "new page is parked in citation_baseline.txt"),
            ]
            for ok, message in checks:
                if not ok:
                    errors.append(f"[FAIL] {label}: {message}")
            print(f"  {label}: {char_count} chars — {'PASS' if not any(label in e for e in errors) else 'FAIL'}")

    for category in ("gods", "stories", "comparisons"):
        for title, files in find_duplicate_english_titles(category).items():
            errors.append(
                f"[FAIL] {CULTURE}/{category}: {len(files)} pages claim the same English title "
                f"“{title}” — {', '.join(files)}"
            )

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
