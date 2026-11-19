#!/usr/bin/env python3
"""Regenerate culture and theme markdown files from _catalog.json."""
import argparse, json, os, sys

REPO = os.path.dirname(os.path.abspath(__file__))
CATALOG = os.path.join(REPO, "_catalog.json")
CULTURES_DIR = os.path.join(REPO, "cultures")
THEMES_DIR = os.path.join(REPO, "themes")
MANUAL_BASELINE = os.path.join(REPO, "scripts", "regen_manual_baseline.json")


def load_catalog():
    with open(CATALOG, encoding="utf-8") as f:
        return json.load(f)


def norm(line):
    return line.strip()


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
    lines.append(f"\n## 核心母題\n\n")
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


def generate_cultures_index(catalog):
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
    return "".join(lines)


def generate_themes_index(catalog):
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
    return "".join(lines)


def generated_files(catalog):
    files = []
    for cat in catalog["cultures"]:
        files.append((f"cultures/{cat['id']}/index.md", generate_culture_md(cat)))
    for th in catalog["themes"]:
        files.append((f"themes/{th['id']}.md", generate_theme_md(th)))
    files.append(("cultures/00-index.md", generate_cultures_index(catalog)))
    files.append(("themes/00-index.md", generate_themes_index(catalog)))
    return files


def read_current(rel):
    path = os.path.join(REPO, rel)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines(keepends=True)


def orphan_lines(generated, current):
    gen = {norm(line) for line in generated if norm(line)}
    cur = {norm(line) for line in current if norm(line)}
    return sorted(cur - gen)


def missing_lines(generated, current):
    cur = {norm(line) for line in current if norm(line)}
    return [line for line in generated if norm(line) and norm(line) not in cur]


def merge_lines(generated, current):
    current_keys = {norm(line) for line in current if norm(line)}
    generated_by_section = {}
    section = None
    for line in generated:
        if line.startswith("## "):
            section = line
        key = norm(line)
        if key:
            generated_by_section[key] = section
    positions = {}
    for line in generated:
        key = norm(line)
        if not key or key in current_keys:
            continue
        section = generated_by_section.get(key)
        pos = len(current)
        if section in current:
            start = current.index(section)
            pos = start
            for i in range(start + 1, len(current)):
                if current[i].startswith("## "):
                    break
                pos = i
            pos += 1
        positions.setdefault(pos, []).append(line)
    merged = []
    for i, line in enumerate(current):
        for extra in positions.get(i, []):
            merged.append(extra)
        merged.append(line)
    for extra in positions.get(len(current), []):
        merged.append(extra)
    return merged


def load_manual_baseline():
    if not os.path.exists(MANUAL_BASELINE):
        return {}
    with open(MANUAL_BASELINE, encoding="utf-8") as f:
        data = json.load(f)
    return {key: set(norm(line) for line in value) for key, value in data.items()}


def write_file(rel, lines):
    path = os.path.join(REPO, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def mode_write_baseline(catalog):
    baseline = {}
    for rel, content in generated_files(catalog):
        orphans = orphan_lines(content.splitlines(keepends=True), read_current(rel))
        if orphans:
            baseline[rel] = orphans
    with open(MANUAL_BASELINE, "w", encoding="utf-8") as f:
        json.dump({k: sorted(v) for k, v in sorted(baseline.items())}, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Baseline written: {len(baseline)} files, {sum(len(v) for v in baseline.values())} manual lines")
    return 0


def mode_check(catalog):
    baseline = load_manual_baseline()
    destructive = []
    total_orphans = 0
    total_missing = 0
    for rel, content in generated_files(catalog):
        generated = content.splitlines(keepends=True)
        current = read_current(rel)
        orphans = orphan_lines(generated, current)
        missing = missing_lines(generated, current)
        total_orphans += len(orphans)
        total_missing += len(missing)
        new_orphans = [line for line in orphans if line not in baseline.get(rel, set())]
        if new_orphans:
            destructive.append((rel, new_orphans))
    print(f"Drift: {total_missing} catalog-only lines, {total_orphans} manual-only lines")
    print(f"Unlogged manual lines at risk: {sum(len(v) for _, v in destructive)}")
    for rel, lines in destructive:
        print(f"  ! {rel}: {len(lines)} unlogged lines would be deleted")
        for line in lines[:5]:
            print(f"      {line}")
        if len(lines) > 5:
            print(f"      ...另有 {len(lines) - 5} 行")
    if destructive:
        print("Result: UNSAFE — run with --merge or update the manual baseline")
        return 1
    print("Result: SAFE — no unlogged manual content would be deleted")
    return 0


def mode_merge(catalog):
    changed = 0
    added = 0
    for rel, content in generated_files(catalog):
        generated = content.splitlines(keepends=True)
        current = read_current(rel)
        merged = merge_lines(generated, current)
        if merged != current:
            write_file(rel, merged)
            changed += 1
            added += len(merged) - len(current)
    print(f"Merged {changed} files, added {added} catalog-only lines; manual lines preserved")
    return 0


def mode_force(catalog):
    for rel, content in generated_files(catalog):
        write_file(rel, content.splitlines(keepends=True))
    print("Forced overwrite completed")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Safe regeneration of generated markdown from _catalog.json")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="report drift without writing (default)")
    group.add_argument("--merge", action="store_true", help="add catalog-only lines while preserving manual lines")
    group.add_argument("--force", action="store_true", help="overwrite generated files (destructive)")
    group.add_argument("--write-baseline", action="store_true", help="record current manual-only lines as approved")
    args = parser.parse_args()
    catalog = load_catalog()
    print(f"Loaded: {len(catalog['cultures'])} cultures, {len(catalog['themes'])} themes")
    if args.write_baseline:
        return mode_write_baseline(catalog)
    if args.merge:
        return mode_merge(catalog)
    if args.force:
        return mode_force(catalog)
    return mode_check(catalog)


if __name__ == "__main__":
    sys.exit(main())
