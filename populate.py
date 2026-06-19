#!/usr/bin/env python3
"""
Mythos Atlas — 自動充實腳本
每小時由 cron 呼叫（每小時第 10 分鐘），逐步產生各文化神話條目與主題分析。
"""

import json
import os
import subprocess
import sys
from datetime import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
CATALOG = os.path.join(REPO, "_catalog.json")
CULTURES_DIR = os.path.join(REPO, "cultures")
THEMES_DIR = os.path.join(REPO, "themes")
INDEX_CULTURES = os.path.join(CULTURES_DIR, "00-index.md")
INDEX_THEMES = os.path.join(THEMES_DIR, "00-index.md")


def load_catalog():
    with open(CATALOG, encoding="utf-8") as f:
        return json.load(f)


def culture_exists(cid):
    d = os.path.join(CULTURES_DIR, cid)
    return os.path.isdir(d) and os.path.isfile(os.path.join(d, "index.md"))


def theme_exists(tid):
    f = os.path.join(THEMES_DIR, f"{tid}.md")
    return os.path.isfile(f)


def generate_culture_index(cat):
    lines = [
        f"# {cat['name']} ({cat['name_en']})\n",
        f"\n",
        f"- **區域：** {cat['region']}\n",
        f"- **時期：** {cat['era']}\n",
        f"\n",
        f"## 原始文獻\n\n",
    ]
    for s in cat["sources"]:
        lines.append(f"- {s}\n")
    lines.append(f"\n## 創世神話\n\n{cat['creation']}\n\n")
    lines.append(f"## 洪水傳說\n\n{cat['flood']}\n\n")
    lines.append(f"## 神系\n\n{cat['pantheon']}\n\n")

    lines.append(f"## 核心母題\n\n")
    for m in cat["motifs"]:
        lines.append(f"- {m}\n")

    lines.append(f"\n## 跨文化平行\n\n")
    for p in cat["parallels"]:
        lines.append(f"- **{p[0]}** ↔ {p[1]}\n")

    lines.append(f"\n## 重要故事\n\n")
    for s in cat["stories"]:
        lines.append(f"- {s}\n")

    lines.append(f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n")

    return "".join(lines)


def generate_theme_index(th):
    lines = [
        f"# {th['name']}\n",
        f"## {th['name_en']}\n\n",
        f"## 涉及文化\n\n",
    ]
    for c in th["cultures_covered"]:
        lines.append(f"- {c}\n")
    lines.append(f"\n## 關鍵觀察\n\n{th['key_observations']}\n\n")
    lines.append(f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n")
    return "".join(lines)


def update_cultures_index():
    """Rebuild cultures/00-index.md"""
    entries = []
    for d in sorted(os.listdir(CULTURES_DIR)):
        if d == "00-index.md" or d.startswith("."):
            continue
        ipath = os.path.join(CULTURES_DIR, d, "index.md")
        if os.path.isfile(ipath):
            with open(ipath, encoding="utf-8") as f:
                first_line = f.readline().strip().lstrip("# ")
            entries.append((d, f"{first_line} ({d})"))

    lines = [
        "# 文化索引\n\n",
        "> 自動生成的索引 — 涵蓋所有已收錄的文化神話體系。\n\n",
        "| 目錄 | 文化 |\n",
        "|------|------|\n",
    ]
    for d, name in entries:
        lines.append(f"| [{d}]({d}/index.md) | {name} |\n")
    lines.append(f"\n\n*總計 {len(entries)} 個文化體系*\n")

    with open(INDEX_CULTURES, "w", encoding="utf-8") as f:
        f.writelines(lines)


def update_themes_index():
    """Rebuild themes/00-index.md"""
    entries = []
    for fname in sorted(os.listdir(THEMES_DIR)):
        if fname == "00-index.md" or fname.startswith("."):
            continue
        fpath = os.path.join(THEMES_DIR, fname)
        if os.path.isfile(fpath):
            with open(fpath, encoding="utf-8") as f:
                first_line = f.readline().strip().lstrip("# ")
            name_noext = fname.replace(".md", "")
            entries.append((name_noext, first_line))

    lines = [
        "# 主題索引\n\n",
        "> 自動生成的索引 — 跨文化主題分析。\n\n",
        "| 檔案 | 主題 |\n",
        "|------|------|\n",
    ]
    for fname, title in entries:
        lines.append(f"| [{fname}]({fname}.md) | {title} |\n")
    lines.append(f"\n\n*總計 {len(entries)} 個主題*\n")

    with open(INDEX_THEMES, "w", encoding="utf-8") as f:
        f.writelines(lines)


def git_commit(filepath, msg):
    """Stage and commit the given file."""
    try:
        subprocess.run(["git", "-C", REPO, "add", filepath], check=True, capture_output=True)
        subprocess.run(
            ["git", "-C", REPO, "commit", "-m", msg, "--allow-empty"],
            check=True, capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e.stderr.decode()}", file=sys.stderr)


def main():
    catalog = load_catalog()

    # Process cultures
    for cat in sorted(catalog["cultures"], key=lambda x: x["order"]):
        cid = cat["id"]
        if culture_exists(cid):
            continue

        # Create culture directory
        cdir = os.path.join(CULTURES_DIR, cid)
        os.makedirs(cdir, exist_ok=True)

        # Generate content
        content = generate_culture_index(cat)
        fpath = os.path.join(cdir, "index.md")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

        # Update index
        update_cultures_index()

        # Commit
        git_commit(fpath, f"mythos: add {cat['name']} ({cat['name_en']})")
        git_commit(INDEX_CULTURES, f"mythos: update cultures index")
        print(f"✓ Generated: cultures/{cid}/index.md — {cat['name']}")
        return  # One item per run

    # If all cultures done, process themes
    for th in sorted(catalog["themes"], key=lambda x: x["order"]):
        tid = th["id"]
        if theme_exists(tid):
            continue

        content = generate_theme_index(th)
        fpath = os.path.join(THEMES_DIR, f"{tid}.md")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

        # Update index
        update_themes_index()

        git_commit(fpath, f"mythos: add theme {th['name']}")
        git_commit(INDEX_THEMES, f"mythos: update themes index")
        print(f"✓ Generated: themes/{tid}.md — {th['name']}")
        return  # One item per run

    # If all cultures and themes are done, log completion
    print("🏁 All entries generated. Nothing more to do.")


if __name__ == "__main__":
    main()
