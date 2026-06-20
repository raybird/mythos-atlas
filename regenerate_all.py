#!/usr/bin/env python3
"""Regenerate ALL culture and theme markdown files from _catalog.json."""
import json, os, sys

REPO = os.path.dirname(os.path.abspath(__file__))
CATALOG = os.path.join(REPO, "_catalog.json")
CULTURES_DIR = os.path.join(REPO, "cultures")
THEMES_DIR = os.path.join(REPO, "themes")

def load_catalog():
    with open(CATALOG, encoding="utf-8") as f:
        return json.load(f)

def generate_culture_md(cat):
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
    lines.append(f"\n---\n*Generated on 2026-06-20 from _catalog.json*\n")
    return "".join(lines)

def generate_theme_md(th):
    lines = [
        f"# {th['name']}\n",
        f"## {th['name_en']}\n\n",
        f"## 涉及文化\n\n",
    ]
    for c in th["cultures_covered"]:
        lines.append(f"- {c}\n")
    lines.append(f"\n## 關鍵觀察\n\n{th['key_observations']}\n\n")
    lines.append(f"\n---\n*Generated on 2026-06-20 from _catalog.json*\n")
    return "".join(lines)

def regenerate_all_cultures(catalog):
    print(f"\n── Regenerating {len(catalog['cultures'])} culture files ──")
    for cat in catalog["cultures"]:
        cid = cat["id"]
        cdir = os.path.join(CULTURES_DIR, cid)
        fpath = os.path.join(cdir, "index.md")
        os.makedirs(cdir, exist_ok=True)
        content = generate_culture_md(cat)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ cultures/{cid}/index.md")

def regenerate_all_themes(catalog):
    print(f"\n── Regenerating {len(catalog['themes'])} theme files ──")
    for th in catalog["themes"]:
        tid = th["id"]
        fpath = os.path.join(THEMES_DIR, f"{tid}.md")
        content = generate_theme_md(th)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ themes/{tid}.md")

def update_cultures_index(catalog):
    entries = []
    for cat in catalog["cultures"]:
        cid = cat["id"]
        entries.append((cid, f"{cat['name']} ({cat['name_en']}) ({cid})"))
    lines = [
        "# 文化索引\n\n",
        "> 自動生成的索引 — 涵蓋所有已收錄的文化神話體系。\n\n",
        "| 目錄 | 文化 |\n",
        "|------|------|\n",
    ]
    for cid, name in entries:
        lines.append(f"| [{cid}]({cid}/index.md) | {name} |\n")
    lines.append(f"\n\n*總計 {len(entries)} 個文化體系*\n")
    with open(os.path.join(CULTURES_DIR, "00-index.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"  ✓ Updated cultures index: {len(entries)} entries")

def update_themes_index(catalog):
    entries = []
    for th in catalog["themes"]:
        tid = th["id"]
        entries.append((tid, th['name']))
    lines = [
        "# 主題索引\n\n",
        "> 自動生成的索引 — 跨文化主題分析。\n\n",
        "| 檔案 | 主題 |\n",
        "|------|------|\n",
    ]
    for tid, name in entries:
        lines.append(f"| [{tid}]({tid}.md) | {name} |\n")
    lines.append(f"\n\n*總計 {len(entries)} 個主題*\n")
    with open(os.path.join(THEMES_DIR, "00-index.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"  ✓ Updated themes index: {len(entries)} entries")

def main():
    print("Mythos Atlas — Full Regeneration\n" + "="*35)
    catalog = load_catalog()
    print(f"Loaded: {len(catalog['cultures'])} cultures, {len(catalog['themes'])} themes")
    
    regenerate_all_cultures(catalog)
    regenerate_all_themes(catalog)
    update_cultures_index(catalog)
    update_themes_index(catalog)
    
    print("\n✅ All files regenerated successfully!")

if __name__ == "__main__":
    main()
