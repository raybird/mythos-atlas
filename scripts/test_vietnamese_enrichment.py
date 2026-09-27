#!/usr/bin/env python3
"""Tests for the Vietnamese culture enrichment (Long Do / Bach Ma, the 1010
naming of Thang Long, ascending-animal toponyms across cultures).

Mirrors the contract of test_armenian_enrichment.py: every enrichment page
must exist, keep heading hierarchy, stay >= 300 body chars, carry a non-empty
citation section, include a cross-cultural section, be indexed in its own
directory README, and never be parked in scripts/citation_baseline.txt.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CULTURE = "vietnamese"

NEW_PAGES = {
    "gods": ["Long-Do-Bach-Ma.md"],
    "stories": ["thang-long-1010.md"],
    "comparisons": ["ascending-animal-toponyms.md"],
}

# Minimum CJK character count per page (the bare contract is 300; the three
# Vietnamese pages are expected to be research-length, not stubs).
MIN_CJK = {
    "gods/Long-Do-Bach-Ma.md": 1500,
    "stories/thang-long-1010.md": 1500,
    "comparisons/ascending-animal-toponyms.md": 1500,
}

# Cross-links between the three new pages must resolve to real files.
INTERNAL_LINKS = {
    "gods/Long-Do-Bach-Ma.md": ["../stories/thang-long-1010.md"],
    "stories/thang-long-1010.md": [
        "../gods/Long-Do-Bach-Ma.md",
        "../gods/long-vuong.md",
        "../gods/kim-quy.md",
        "../gods/lac-long-quan-au-co.md",
        "../comparisons/ascending-animal-toponyms.md",
    ],
    "comparisons/ascending-animal-toponyms.md": [
        "../gods/Long-Do-Bach-Ma.md",
        "../stories/thang-long-1010.md",
    ],
}

REF_PATTERN = re.compile(
    r"^#{2,4}\s*(參考文獻|參考來源|參考資料|References|Sources|Bibliography)\s*$",
    re.MULTILINE,
)

CROSS_CULTURAL_PATTERN = re.compile(r"^#{2,4}\s*跨文化", re.MULTILINE)

CJK_PATTERN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")

ENGLISH_TITLE_PATTERN = re.compile(r"[(（]([^)）]+)[)）]\s*$")

CITATION_BASELINE = ROOT / "scripts" / "citation_baseline.txt"


def count_body_chars(text: str) -> int:
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


def count_cjk(text: str) -> int:
    return len(CJK_PATTERN.findall(text))


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


def test_min_cjk(text: str, label: str) -> bool:
    return count_cjk(text) >= MIN_CJK[label]


def test_has_citation(text: str) -> bool:
    matches = list(REF_PATTERN.finditer(text))
    if not matches:
        return False
    remaining = text[matches[-1].end():].strip()
    ref_lines = sum(
        1
        for l in remaining.split("\n")
        if l.strip() and not l.strip().startswith("#") and not l.strip().startswith(">")
    )
    return ref_lines > 0


def test_has_cross_cultural(text: str) -> bool:
    return bool(CROSS_CULTURAL_PATTERN.search(text))


def test_internal_links(path: Path, links) -> list:
    broken = []
    text = path.read_text(encoding="utf-8")
    for link in links:
        if link not in text:
            broken.append(f"missing reference to {link}")
            continue
        if not (path.parent / link).resolve().exists():
            broken.append(f"dangling link {link}")
    return broken


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
            cjk_count = count_cjk(text)
            checks = [
                (test_heading_hierarchy(text), "heading hierarchy broken"),
                (test_min_length(text), f"body too short ({char_count} chars, need >= 300)"),
                (test_min_cjk(text, label), f"CJK depth too shallow ({cjk_count}, need >= {MIN_CJK[label]})"),
                (test_has_citation(text), "missing or empty citation section"),
                (test_has_cross_cultural(text), "no cross-cultural section"),
                (test_indexed_in_readme(category, filename), "not listed in directory README.md"),
                (test_not_baselined(path), "new page is parked in citation_baseline.txt"),
            ]
            for ok, message in checks:
                if not ok:
                    errors.append(f"[FAIL] {label}: {message}")
            for message in test_internal_links(path, INTERNAL_LINKS[label]):
                errors.append(f"[FAIL] {label}: {message}")
            print(f"  {label}: {char_count} chars / {cjk_count} CJK — {'PASS' if not any(label in e for e in errors) else 'FAIL'}")

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
