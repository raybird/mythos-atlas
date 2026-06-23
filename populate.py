#!/usr/bin/env python3
"""
⚠️  DEPRECATED — 此腳本僅產生模板空殼內容。

請改用大語言模型（LLM）直接撰寫真實內容，填充 gods/、stories/、
analyses/ 中的頁面。詳見 AGENTS.md。

本腳本保留以供下列有限用途：
  --mode ref   更新 references/ 中的跨文化參照矩陣
  --mode new   產生 _catalog.json 中的新條目空白骨架（需後續手動填充）

Usage (limited use only):
  python3 populate.py --mode ref               # 更新參考文獻
  python3 populate.py --mode new --batch 1      # 產生空白骨架
"""

import json
import os
import random
import subprocess
import sys
from datetime import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
CATALOG = os.path.join(REPO, "_catalog.json")
CULTURES_DIR = os.path.join(REPO, "cultures")
THEMES_DIR = os.path.join(REPO, "themes")
ANALYSES_DIR = os.path.join(REPO, "analyses")
REFERENCES_DIR = os.path.join(REPO, "references")
STATE_FILE = os.path.join(REPO, "_state.json")


# ── State tracking ───────────────────────────────────────────────────────────

def load_state():
    if os.path.isfile(STATE_FILE):
        with open(STATE_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"new_index": 0, "theme_index": 0, "enrich_log": [], "analysis_log": [], "runs": 0}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def load_catalog():
    with open(CATALOG, encoding="utf-8") as f:
        return json.load(f)


# ── Content helpers ──────────────────────────────────────────────────────────

def culture_exists(cid):
    d = os.path.join(CULTURES_DIR, cid)
    return os.path.isdir(d) and os.path.isfile(os.path.join(d, "index.md"))

def theme_exists(tid):
    return os.path.isfile(os.path.join(THEMES_DIR, f"{tid}.md"))

def has_god_subpages(cid):
    gods_dir = os.path.join(CULTURES_DIR, cid, "gods")
    return os.path.isdir(gods_dir) and len(os.listdir(gods_dir)) > 0

def has_story_subpages(cid):
    stories_dir = os.path.join(CULTURES_DIR, cid, "stories")
    return os.path.isdir(stories_dir) and len(os.listdir(stories_dir)) > 0


# ── README generation ──────────────────────────────────────────────────────────

def generate_sub_readme(dir_path, title, files, now):
    lines = [
        f"# {title}\n\n",
        f"| 檔案 | 名稱 |\n",
        f"|------|------|\n",
    ]
    for fname in sorted(files):
        name = fname.replace(".md", "")
        lines.append(f"| [{name}]({fname}) | {name} |\n")
    lines.append(f"\n---\n*Auto-generated on {now}*\n")
    with open(os.path.join(dir_path, "README.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)

def update_main_readme(catalog, state):
    readme_path = os.path.join(REPO, "README.md")
    if not os.path.isfile(readme_path):
        return
    with open(readme_path, encoding="utf-8") as f:
        content = f.read()

    culture_count = len(catalog["cultures"])
    theme_count = len(catalog["themes"])
    existing_cultures = sum(1 for c in catalog["cultures"] if culture_exists(c["id"]))
    existing_themes = sum(1 for t in catalog["themes"] if theme_exists(t["id"]))
    analysis_files = [f for f in os.listdir(ANALYSES_DIR) if f.endswith(".md") and f != "README.md"] if os.path.isdir(ANALYSES_DIR) else []
    now = datetime.now().strftime('%Y-%m-%d %H:%M UTC')

    # ── Stats section ──
    stats_section = (
        f"\n## 📊 當前狀態\n\n"
        f"> 自動更新於 {now}\n\n"
        f"| 類別 | 進度 |\n"
        f"|------|------|\n"
        f"| 文化體系 | {existing_cultures}/{culture_count} |\n"
        f"| 跨文化主題 | {existing_themes}/{theme_count} |\n"
        f"| 分析文章 | {len(analysis_files)} |\n"
        f"| 總執行次數 | {state['runs']} |\n\n"
    )

    marker_start = "<!-- STATS_START -->"
    marker_end = "<!-- STATS_END -->"
    if marker_start in content and marker_end in content:
        pre = content[:content.find(marker_start) + len(marker_start)]
        post = content[content.find(marker_end):]
        content = pre + "\n" + stats_section + post
    else:
        content += "\n" + marker_start + "\n" + stats_section + marker_end + "\n"

    # ── Cultures list section ──
    cultures_lines = ["\n## 🌍 已收錄文化\n\n", "| 文化 | 區域 | 神祇 | 故事 | 比較 |\n", "|------|------|------|------|------|\n"]
    for cat in sorted(catalog["cultures"], key=lambda x: x.get("order", 999)):
        cid = cat["id"]
        if not culture_exists(cid):
            continue
        gods_dir = os.path.join(CULTURES_DIR, cid, "gods")
        stories_dir = os.path.join(CULTURES_DIR, cid, "stories")
        comp_dir = os.path.join(CULTURES_DIR, cid, "comparisons")
        g = len([f for f in os.listdir(gods_dir) if f.endswith(".md") and f != "README.md"]) if os.path.isdir(gods_dir) else 0
        s = len([f for f in os.listdir(stories_dir) if f.endswith(".md") and f != "README.md"]) if os.path.isdir(stories_dir) else 0
        c = len([f for f in os.listdir(comp_dir) if f.endswith(".md") and f != "README.md"]) if os.path.isdir(comp_dir) else 0
        cultures_lines.append(f"| [{cat['name']}](cultures/{cid}/) | {cat['region']} | {g} | {s} | {c} |\n")
    cultures_lines.append("\n")

    cm_start = "<!-- CULTURES_START -->"
    cm_end = "<!-- CULTURES_END -->"
    section = "".join(cultures_lines)
    if cm_start in content and cm_end in content:
        pre = content[:content.find(cm_start) + len(cm_start)]
        post = content[content.find(cm_end):]
        content = pre + "\n" + section + post
    else:
        content += "\n" + cm_start + "\n" + section + cm_end + "\n"

    # ── Analyses list section ──
    analyses_lines = ["\n## 📝 分析文章\n\n", "> 跨文化比較神話學分析文章。共 {} 篇。\n\n".format(len(analysis_files))]
    for fname in sorted(analysis_files, reverse=True)[:20]:
        title = fname.replace(".md", "").replace("-", " ").title()
        analyses_lines.append(f"- [{title}](analyses/{fname})\n")
    if len(analysis_files) > 20:
        analyses_lines.append(f"\n... 及另外 {len(analysis_files) - 20} 篇\n")
    analyses_lines.append("\n")

    am_start = "<!-- ANALYSES_START -->"
    am_end = "<!-- ANALYSES_END -->"
    section = "".join(analyses_lines)
    if am_start in content and am_end in content:
        pre = content[:content.find(am_start) + len(am_start)]
        post = content[content.find(am_end):]
        content = pre + "\n" + section + post
    else:
        content += "\n" + am_start + "\n" + section + am_end + "\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

def update_directory_readmes(catalog):
    now = datetime.now().strftime('%Y-%m-%d %H:%M UTC')

    # cultures/README.md
    os.makedirs(CULTURES_DIR, exist_ok=True)
    lines = [
        "# 文化目錄\n\n",
        "> 此目錄包含所有已收錄的神話文化體系，依文明或區域分門別類。\n\n",
        "| 目錄 | 文化名稱 | 區域 |\n",
        "|------|---------|------|\n",
    ]
    for cat in sorted(catalog["cultures"], key=lambda x: x.get("order", 999)):
        cid = cat["id"]
        if culture_exists(cid):
            lines.append(f"| [{cid}]({cid}/index.md) | {cat['name']} ({cat['name_en']}) | {cat['region']} |\n")
    lines.append(f"\n---\n*Auto-generated on {now}*\n")
    with open(os.path.join(CULTURES_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)

    # themes/README.md
    os.makedirs(THEMES_DIR, exist_ok=True)
    lines = [
        "# 主題目錄\n\n",
        "> 跨文化神話主題分析，追蹤同一母題在不同文明中的表現形式與深層結構。\n\n",
        "| 檔案 | 主題名稱 |\n",
        "|------|---------|\n",
    ]
    for t in sorted(catalog["themes"], key=lambda x: x.get("order", 999)):
        tid = t["id"]
        if theme_exists(tid):
            lines.append(f"| [{tid}]({tid}.md) | {t['name']} ({t['name_en']}) |\n")
    lines.append(f"\n---\n*Auto-generated on {now}*\n")
    with open(os.path.join(THEMES_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)

    # analyses/README.md
    os.makedirs(ANALYSES_DIR, exist_ok=True)
    lines = ["# 分析文章目錄\n\n", "> 跨文化比較神話學分析文章，探討各文明之間的深層連結。\n\n"]
    for fname in sorted(os.listdir(ANALYSES_DIR)):
        if fname.endswith(".md") and fname != "README.md":
            title = fname.replace(".md", "").replace("-", " ").title()
            lines.append(f"- [{title}]({fname})\n")
    lines.append(f"\n---\n*Auto-generated on {now}*\n")
    with open(os.path.join(ANALYSES_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)

    # references/README.md
    os.makedirs(REFERENCES_DIR, exist_ok=True)
    ref_files = [f for f in os.listdir(REFERENCES_DIR) if f.endswith(".md") and f != "README.md"]
    lines = [
        "# 參考文獻目錄\n\n",
        "> 原始文獻索引、母題索引與跨文化參照矩陣，供深入研究使用。\n\n",
    ]
    for fname in sorted(ref_files):
        name = fname.replace(".md", "")
        lines.append(f"- [{name}]({fname})\n")
    lines.append(f"\n---\n*Auto-generated on {now}*\n")
    with open(os.path.join(REFERENCES_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)

    # Per-culture README.md
    for cat in catalog["cultures"]:
        cid = cat["id"]
        cdir = os.path.join(CULTURES_DIR, cid)
        if not os.path.isdir(cdir):
            continue

        lines = [
            f"# {cat['name']} ({cat['name_en']})\n\n",
            f"- **區域：** {cat['region']}\n",
            f"- **時期：** {cat['era']}\n\n",
            f"## 目錄\n\n",
            f"- [文化總覽](index.md) — 該文化的完整神話介紹\n",
        ]

        gods_dir = os.path.join(cdir, "gods")
        stories_dir = os.path.join(cdir, "stories")
        comp_dir = os.path.join(cdir, "comparisons")

        if os.path.isdir(gods_dir):
            gods = sorted(f for f in os.listdir(gods_dir) if f.endswith(".md") and f != "README.md")
            if gods:
                lines.append(f"- [神祇列表](gods/) — {len(gods)} 位神祇\n")
                generate_sub_readme(gods_dir, f"{cat['name']} — 神祇", gods, now)

        if os.path.isdir(stories_dir):
            stories = sorted(f for f in os.listdir(stories_dir) if f.endswith(".md") and f != "README.md")
            if stories:
                lines.append(f"- [故事列表](stories/) — {len(stories)} 則故事\n")
                generate_sub_readme(stories_dir, f"{cat['name']} — 故事", stories, now)

        if os.path.isdir(comp_dir):
            comps = sorted(f for f in os.listdir(comp_dir) if f.endswith(".md") and f != "README.md")
            if comps:
                lines.append(f"- [跨文化比較](comparisons/) — {len(comps)} 篇比較\n")
                generate_sub_readme(comp_dir, f"{cat['name']} — 跨文化比較", comps, now)

        lines.append(f"\n---\n*Auto-generated on {now}*\n")
        with open(os.path.join(cdir, "README.md"), "w", encoding="utf-8") as f:
            f.writelines(lines)


# ── Mode 1: Generate NEW entries ─────────────────────────────────────────────

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
    with open(os.path.join(CULTURES_DIR, "00-index.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)
    return len(entries)

def update_themes_index():
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
    with open(os.path.join(THEMES_DIR, "00-index.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)
    return len(entries)

def do_new_entries(catalog, state, batch=1, random_mode=False):
    """Generate new culture/theme entries not yet on disk."""
    items = []
    for cat in catalog["cultures"]:
        cid = cat["id"]
        if not culture_exists(cid):
            items.append(("culture", cat))

    for th in catalog["themes"]:
        tid = th["id"]
        if not theme_exists(tid):
            items.append(("theme", th))

    if not items:
        return 0

    if random_mode:
        random.shuffle(items)
    else:
        items.sort(key=lambda x: x[1].get("order", 999))

    count = 0
    for kind, data in items[:batch]:
        if kind == "culture":
            cid = data["id"]
            cdir = os.path.join(CULTURES_DIR, cid)
            os.makedirs(cdir, exist_ok=True)
            content = generate_culture_index(data)
            fpath = os.path.join(cdir, "index.md")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            n = update_cultures_index()
            print(f"  ✓ New culture: {cid}/index.md — {data['name']} (now {n} total)")
        else:
            tid = data["id"]
            content = generate_theme_index(data)
            fpath = os.path.join(THEMES_DIR, f"{tid}.md")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            n = update_themes_index()
            print(f"  ✓ New theme: {tid}.md — {data['name']} (now {n} total)")
        count += 1

    return count


# ── Mode 2: ENRICH existing entries ──────────────────────────────────────────

def parse_pantheon(pantheon_str):
    """Parse pantheon string like 'Tinia(天/雷神)、Uni(天后)、...' into list of dicts."""
    entries = []
    for part in pantheon_str.replace("/ ", "/").split("、"):
        part = part.strip()
        if not part:
            continue
        if "(" in part and part.endswith(")"):
            name, rest = part.split("(", 1)
            domain = rest.rstrip(")")
            entries.append({"name": name.strip(), "domain": domain.strip()})
        else:
            entries.append({"name": part, "domain": ""})
    return entries

def enrich_gods(cid, cat):
    """Generate individual god pages from the pantheon string."""
    gods_dir = os.path.join(CULTURES_DIR, cid, "gods")
    os.makedirs(gods_dir, exist_ok=True)
    gods = parse_pantheon(cat["pantheon"])
    count = 0
    for god in gods:
        safe_name = god["name"].replace("/", "-").replace(" ", "-")
        fpath = os.path.join(gods_dir, f"{safe_name}.md")
        if os.path.isfile(fpath):
            continue
        lines = [
            f"# {god['name']}\n\n",
            f"- **文化：** {cat['name']} ({cat['name_en']})\n",
            f"- **職掌：** {god['domain']}\n\n",
            f"## 概述\n\n",
            f"{god['name']} ({god['domain']}) 是{cat['name']}中的神祇。\n\n",
            f"## 相關神祇\n\n",
            f"- 所屬神系：{cat['name']}\n",
        ]
        # Add parallels that mention this god
        for p in cat.get("parallels", []):
            if god["name"] in p[0]:
                lines.append(f"- 跨文化對應：{p[1]}\n")
        # Add cross-references from other cultures
        lines.extend([
            f"\n## 出現在\n\n",
            f"- {cat['name']} 神系\n",
            f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n",
        ])
        with open(fpath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        count += 1
    return count

def enrich_stories(cid, cat):
    """Generate individual story pages from the stories list."""
    stories_dir = os.path.join(CULTURES_DIR, cid, "stories")
    os.makedirs(stories_dir, exist_ok=True)
    count = 0
    for story in cat.get("stories", []):
        safe_name = story.replace("/", "-").replace(" ", "-")[:40]
        fpath = os.path.join(stories_dir, f"{safe_name}.md")
        if os.path.isfile(fpath):
            continue
        lines = [
            f"# {story}\n\n",
            f"- **文化：** {cat['name']} ({cat['name_en']})\n\n",
            f"## 故事簡介\n\n",
            f"{story} 是{cat['name']}中的重要傳說。\n\n",
            f"## 文化脈絡\n\n",
            f"此故事屬於{cat['name']}的敘事傳統，反映該文化的核心價值與宇宙觀。\n\n",
            f"## 相關主題\n\n",
        ]
        for m in cat.get("motifs", []):
            if any(w in story for w in m.split()):
                lines.append(f"- {m}\n")
        lines.append(f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n")
        with open(fpath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        count += 1
    return count

def enrich_comparisons(cid, cat):
    """Generate cross-cultural comparison sub-pages."""
    comp_dir = os.path.join(CULTURES_DIR, cid, "comparisons")
    os.makedirs(comp_dir, exist_ok=True)
    count = 0
    catalog = load_catalog()
    for p in cat.get("parallels", []):
        local_concept = p[0]
        foreign_refs = p[1]
        safe_name = local_concept.replace("/", "-").replace(" ", "-")[:30]
        fpath = os.path.join(comp_dir, f"{safe_name}.md")
        if os.path.isfile(fpath):
            continue
        # Find which cultures also mention this concept
        related = []
        for other in catalog["cultures"]:
            if other["id"] == cid:
                continue
            for op in other.get("parallels", []):
                if local_concept in op[0] or local_concept in op[1]:
                    related.append(other["name"])
        lines = [
            f"# {local_concept} — 跨文化比較\n\n",
            f"## 比較：{cat['name']} vs 其他文化\n\n",
            f"在{cat['name']}中，{local_concept} 對應於 {foreign_refs}。\n\n",
        ]
        if related:
            lines.append("## 其他提及此母題的文化\n\n")
            for r in related[:10]:
                lines.append(f"- {r}\n")
        lines.append(f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n")
        with open(fpath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        count += 1
    return count

def find_enrichment_target(catalog, random_mode=False):
    """Pick a culture entry to enrich — prefer ones with least enrichment."""
    candidates = []
    for cat in catalog["cultures"]:
        cid = cat["id"]
        if not culture_exists(cid):
            continue
        score = 0
        if has_god_subpages(cid):
            score += 1
        if has_story_subpages(cid):
            score += 1
        if os.path.isdir(os.path.join(CULTURES_DIR, cid, "comparisons")):
            score += 1
        candidates.append((score, cat))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0])
    if random_mode:
        # Weight: prefer lower scores but add randomness
        candidates = candidates[:max(3, len(candidates)//3)]
        return random.choice(candidates)[1]
    return candidates[0][1]

def do_enrich(catalog, state, batch=1, random_mode=False):
    """Enrich existing entries with deeper sub-pages."""
    count = 0
    for _ in range(batch):
        cat = find_enrichment_target(catalog, random_mode)
        if not cat:
            break
        cid = cat["id"]
        enrichments = []

        if not has_god_subpages(cid):
            n = enrich_gods(cid, cat)
            if n > 0:
                enrichments.append(f"gods/{n} pages")

        if not has_story_subpages(cid):
            n = enrich_stories(cid, cat)
            if n > 0:
                enrichments.append(f"stories/{n} pages")

        if not os.path.isdir(os.path.join(CULTURES_DIR, cid, "comparisons")):
            n = enrich_comparisons(cid, cat)
            if n > 0:
                enrichments.append(f"comparisons/{n} pages")

        if enrichments:
            print(f"  ✓ Enriched {cid}: {', '.join(enrichments)}")
            count += 1
        else:
            # Already fully enriched; add to state to track
            pass
    return count


# ── Mode 3: ANALYZE — generate comparative analyses ─────────────────────────

ANALYSIS_TEMPLATES = [
    # ── Existing 12 templates (preserved) ──
    {"slug": "female-deities", "title": "女神崇拜比較研究", "title_en": "Comparative Study of Goddess Worship", "description": "跨文化中女神形象的比較——從大地母神到戰爭女神，從智慧女神到愛神。"},
    {"slug": "underworld-journey", "title": "冥界之旅：死亡與重生", "title_en": "The Underworld Journey: Death and Rebirth", "description": "英雄/神祇進入冥界並返回的主題，從伊南娜到奧菲斯，從伊邪那岐到耶穌。"},
    {"slug": "animal-symbolism", "title": "神話動物象徵體系", "title_en": "Mythological Animal Symbolism", "description": "龍、鳳凰、蛇、狼、熊、烏鴉等動物在不同神話體系中的象徵意義比較。"},
    {"slug": "sacred-mountains", "title": "聖山：天地之間的橋樑", "title_en": "Sacred Mountains: Axis Mundi Across Cultures", "description": "崑崙、須彌、奧林帕斯、西奈、富士——聖山作為宇宙軸心的跨文化比較。"},
    {"slug": "origin-of-death", "title": "死亡的起源：神話中的解釋", "title_en": "The Origin of Death: Mythological Explanations", "description": "為什麼人會死？——從月神訊息傳達失誤到香蕉樹神話，跨文化如何解釋死亡的起源。"},
    {"slug": "rainbow-myths", "title": "彩虹神話與象徵", "title_en": "Rainbow Myths and Symbolism", "description": "彩虹作為橋樑、蛇、神之弓的跨文化比較。"},
    {"slug": "cosmic-egg", "title": "宇宙卵：創世原型的全球比較", "title_en": "The Cosmic Egg: A Global Creation Archetype", "description": "從印度金卵到中國盤古卵，從芬蘭世界蛋到波利尼西亞宇宙蛋——卵生創世的跨文化比較。"},
    {"slug": "sacrificial-creation", "title": "犧牲創世：巨人化生萬物", "title_en": "Sacrificial Creation: The Dismembered Giant", "description": "盤古、Ymir、Purusha、Gayomart——巨人被殺後身體化為宇宙各部分的跨文化比較。"},
    {"slug": "sun-myths", "title": "太陽神話與太陽崇拜", "title_en": "Sun Myths and Solar Worship", "description": "從Ra的阿頓船到Inti的金子，從阿波羅的馬車到天照大神——太陽崇拜的跨文化比較。"},
    {"slug": "twin-myths", "title": "神話中的雙生子", "title_en": "Twins in World Mythology", "description": "創世雙子、英雄雙子、善惡雙子——雙生子神話的跨文化類型學。"},
    {"slug": "earth-diver-comparative", "title": "大地潛水者創世神話", "title_en": "The Earth-Diver Creation Myth", "description": "動物潛入原始海洋取泥造地的廣泛分布——從北亞到北美，從東歐到南亞。"},
    {"slug": "shamanism-in-myth", "title": "神話中的薩滿元素", "title_en": "Shamanic Elements in World Mythology", "description": "薩滿式靈魂旅程、宇宙樹、動物助手等元素在神話中的體現與比較。"},

    # ── New templates (25 articles — geomythology, flood, pole-shift, lost worlds) ──
    {"slug": "shanhaijing-mythological-geography", "title": "《山海經》神話地理的跨文化平行", "title_en": "Shanhaijing Mythological Geography: Cross-Cultural Parallels", "description": "崑崙、四方神、海外異域——《山海經》中的神話空間觀與其他文明（印度須彌山、希臘奧林帕斯、北歐九界）的地理宇宙論比較。"},
    {"slug": "babel-post-flood-civilization", "title": "巴別塔與洪水後文明分散", "title_en": "Babel and Post-Diluvian Civilization Dispersal", "description": "洪水後人類分散（挪亞三子、巴別塔、伏羲女媧、大禹九鼎）的神話類型學——語言變亂是否記憶了史前遷徙事件。"},
    {"slug": "geomythology-catastrophe-coding", "title": "地質神話學：自然災害如何編碼為神話", "title_en": "Geomythology: How Natural Catastrophes Become Myth", "description": "從共工觸山（地軸傾斜）到Thera火山（亞特蘭提斯），從冰壩潰決（大洪水）到隕石撞擊——神話如何保存地質災害的跨代記憶。"},
    {"slug": "atlantis-santorini-connection", "title": "亞特蘭提斯的地質核心：錫拉火山與米諾斯文明", "title_en": "Atlantis and the Thera Eruption: Geological Core of a Myth", "description": "柏拉圖亞特蘭提斯敘事與錫拉火山爆發（~1600 BCE）摧毀米諾斯文明的比對——從地質證據到神話轉化的完整鏈條。"},
    {"slug": "polar-wander-myths", "title": "地極漂移的神話痕跡", "title_en": "Polar Wander and Its Mythological Traces", "description": "天傾西北、地陷東南——從中國共工到希臘法厄同，從北歐世界傾斜到埃及天地分離：神話中保存的地極移動記憶。"},
    {"slug": "pleistocene-megafauna-memory", "title": "更新世巨型動物在神話中的殘留記憶", "title_en": "Pleistocene Megafauna in Mythological Memory", "description": "猛獁象、大地懶、劍齒虎——各地神話中的巨獸描寫是否保留更新世滅絕動物的口傳記憶？從澳洲夢世紀到西伯利亞長毛象傳說。"},
    {"slug": "precession-equinox-myths", "title": "歲差運動的神話編碼", "title_en": "Precession of the Equinoxes Encoded in Myth", "description": "世界年齡的週期（黃金、白銀、青銅、黑鐵時代）與歲差運動的對應——從希臘赫西俄德到印度Yuga、馬雅長曆法。"},
    {"slug": "axis-mundi-comparative", "title": "宇宙軸心（Axis Mundi）的跨文化比較", "title_en": "The Axis Mundi Across Cultures", "description": "世界樹（Yggdrasil/建木）、聖山（崑崙/須彌/奧林帕斯）、世界支柱——宇宙軸心神話的三種基本形式的全球分布與深層結構。"},
    {"slug": "golden-age-degeneration", "title": "黃金時代與人類退化神話", "title_en": "The Golden Age and Human Degeneration Myths", "description": "從赫西俄德五時代到印度四Yuga，從中國上古聖王到波斯的Gayomart——人類從完美走向墮落的跨文化敘事及其社會功能。"},
    {"slug": "smiting-god-divine-punishment", "title": "擊打之神：神罰類型的跨文化比較", "title_en": "The Smiting God: Divine Punishment Across Cultures", "description": "雷擊（Tinia/Zeus/Indra）、洪水（Ea/Yahweh）、瘟疫（阿波羅/Resheph）、火焰（Sodom/Shango）——神罰的跨文化類型學。"},
    {"slug": "deluge-survivor-technology", "title": "洪水倖存者與文明技術傳承", "title_en": "Deluge Survivors and the Transmission of Technology", "description": "從美索不達米亞Atrahasis的造船技術到挪亞的方舟、大禹的治水工程——洪水敘事中保存的古代技術知識。"},
    {"slug": "stars-as-ancestors", "title": "星辰祖先與天界起源神話", "title_en": "Star Ancestors: Celestial Origins in World Mythology", "description": "從埃及法老昇星到波利尼西亞航海祖先，從中國星宿分野到馬雅銀河——人類將祖先起源投射於星辰的跨文化模式。"},
    {"slug": "serpent-feathered-dragon", "title": "羽蛇/宇宙蛇/龍的神話演化", "title_en": "Feathered Serpents, Cosmic Serpents, and Dragons", "description": "從中美洲羽蛇神到中國龍，從北歐耶夢加得到印度那伽，從埃及阿佩普到澳洲彩虹蛇——蛇形神話生物的演化樹。"},
    {"slug": "seven-sages-worldwide", "title": "七智者與文化英雄的全球分布", "title_en": "The Seven Sages and Culture Heroes Worldwide", "description": "美索不達米亞Apkallu、印度七仙人、希臘七賢、中國三皇五帝、波爾兄弟——文明奠基者的七人組原型比較。"},
    {"slug": "sacred-mushroom-entheogen", "title": "神聖蘑菇與致幻植物在神話中的角色", "title_en": "Sacred Mushrooms and Entheogens in Mythology", "description": "從西伯利亞蠅傘到中美洲聖菇，從印度Soma到波斯Haoma，從亞馬遜死藤水到希臘Kykeon——致幻植物與宗教體驗的跨文化比較。"},
    {"slug": "were-creatures-transformation", "title": "變形者：狼人/虎人/熊人神話比較", "title_en": "Were-Creatures: Lycanthropy and Therianthropy Across Cultures", "description": "從北歐Berserker到非洲豹人，從南美美洲虎薩滿到中國狐妖，從歐洲狼人到印度虎人——人類-動物變形的神話類型學。"},
    {"slug": "bear-worship-comparative", "title": "熊崇拜的全球比較：從尼安德塔人到薩滿", "title_en": "Bear Worship Worldwide: From Neanderthals to Shamans", "description": "北極圈熊崇拜（薩米/尼夫赫/愛努）、北美原住民熊儀式、歐洲聖熊傳統、中國熊圖騰（黃帝有熊氏）——熊作為至上動物的跨文化證據。"},
    {"slug": "three-worlds-cosmic-levels", "title": "三界宇宙觀的跨文化分布", "title_en": "The Three-World Cosmos Across Cultures", "description": "天堂/人間/冥界的三分宇宙模式——從北歐九界簡化為三界到中國天/地/水官，從印度Trailokya到基督教天堂/煉獄/地獄。"},
    {"slug": "subterranean-worlds", "title": "地下世界與地心文明神話", "title_en": "Subterranean Worlds and Inner Earth Myths", "description": "阿加爾塔/香巴拉、地心空洞說、地下冥界入口——從宗教神話到現代祕密史的「地下文明」敘事傳統。"},
    {"slug": "volcano-fire-mountains", "title": "火山神話與火山的跨文化解釋", "title_en": "Volcano Myths: Cross-Cultural Explanations of Eruptions", "description": "夏威夷Pele、日本富士山神、義大利Vulcan、中美洲波波卡特佩特、冰島Hekla——火山噴發在各文化中如何被神話化。"},
    {"slug": "water-deities-comparative", "title": "水神/海神跨文化比較", "title_en": "Water Deities and Sea Gods Across Cultures", "description": "海神（Poseidon/Neptune/Njord）、河神（Oshun/Hapi/黃河伯）、雨神（Tlaloc/Chac/雷公）、泉神——水的神格化跨文化類型。"},
    {"slug": "megalithic-world-age", "title": "巨石文明與世界年齡計算", "title_en": "Megalithic Monuments and the Age of the World", "description": "哥貝克力石陣、巨石陣、卡納克列石——神話中的上古巨人時代是否對應新石器時代的巨石建造者傳統。"},
    {"slug": "hollow-earth-agartha", "title": "中空地球理論與阿加爾塔神話", "title_en": "The Hollow Earth Theory and the Myth of Agartha", "description": "從印度神話的Patala到佛教的香巴拉，從18世紀科學的Halley空心地球到神秘學的Agartha/Schamballah——地心神話的演化。"},
    {"slug": "human-sacrifice-ritual", "title": "活人獻祭的神話基礎與儀式比較", "title_en": "Human Sacrifice: Mythological Foundations and Ritual Patterns", "description": "阿茲特克太陽祭、迦太基兒童祭、印度Sati、中國甲骨文中的獻祭記錄、北歐人祭——神話如何合理化獻祭行為。"},
    {"slug": "cosmic-mill-myth", "title": "宇宙磨與天體運轉神話", "title_en": "The Cosmic Mill: Celestial Mechanics in Myth", "description": "北歐Frod麵粉磨（Mystery Mill）、芬蘭Sampo、中國天梯/璇璣玉衡、薩滿旋轉宇宙——天體運轉的神話化為旋轉巨輪/磨。"},
]

def do_analyze(catalog, state, batch=1, random_mode=False):
    """Generate comparative analysis articles in analyses/."""
    os.makedirs(ANALYSES_DIR, exist_ok=True)
    done = set(state.get("analysis_log", []))
    available = [t for t in ANALYSIS_TEMPLATES if t["slug"] not in done]
    if not available:
        return 0

    if random_mode:
        random.shuffle(available)
    chosen = available[:batch]
    count = 0
    for tmpl in chosen:
        fpath = os.path.join(ANALYSES_DIR, f"{tmpl['slug']}.md")
        if os.path.isfile(fpath):
            done.add(tmpl["slug"])
            continue

        # Gather relevant cultures from catalog
        related_cultures = []
        for cat in catalog["cultures"]:
            related_cultures.append(cat["name"])

        lines = [
            f"# {tmpl['title']}\n\n",
            f"## {tmpl['title_en']}\n\n",
            f"### 摘要\n\n",
            f"{tmpl['description']}\n\n",
            f"### 涉及文化\n\n",
        ]
        random.shuffle(related_cultures)
        for c in related_cultures[:8]:
            lines.append(f"- {c}\n")
        lines.extend([
            f"\n### 比較分析\n\n",
            f"本分析探討{tmpl['title']}在不同文化中的表現形式與深層結構。\n\n",
            f"### 核心發現\n\n",
            f"1. 跨文化普遍性：此主題在各大洲神話中均有體現\n",
            f"2. 結構相似性：儘管文化差異顯著，深層敘事結構具有共通性\n",
            f"3. 獨特變異：每種文化根據其地理、社會與歷史背景發展出獨特版本\n\n",
            f"### 參考文獻\n\n",
            f"- 本專案收錄的神話條目\n",
            f"- 比較神話學研究\n\n",
            f"---\n\n",
            f"*Analysis generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n",
        ])
        with open(fpath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        done.add(tmpl["slug"])
        print(f"  ✓ Analysis: {tmpl['slug']}.md — {tmpl['title']}")
        count += 1

    state["analysis_log"] = list(done)
    return count


# ── Mode 4: REF — expand reference materials ────────────────────────────────

def do_reference(catalog, state, batch=1, random_mode=False):
    """Expand reference materials and cross-links. Regenerates cross-ref every 10 runs."""
    os.makedirs(REFERENCES_DIR, exist_ok=True)
    count = 0

    cross_ref_path = os.path.join(REFERENCES_DIR, "cross-ref.md")
    should_regenerate = (not os.path.isfile(cross_ref_path) or
                         random_mode or
                         state.get("runs", 0) % 10 == 0)
    if should_regenerate:
        lines = [
            "# 跨文化參照矩陣\n\n",
            "> 自動生成的跨文化參照 — 記錄各文化之間的神話母題連結。\n\n",
            "| 文化 A | 母題 | 文化 B |\n",
            "|--------|------|--------|\n",
        ]
        pairs = set()
        # Find cultures sharing similar motifs via parallels
        for cat in catalog["cultures"]:
            for p in cat.get("parallels", []):
                for other in catalog["cultures"]:
                    if other["id"] == cat["id"]:
                        continue
                    for op in other.get("parallels", []):
                        if p[1] == op[1] or p[0] == op[0]:
                            pair = tuple(sorted([cat["name"], other["name"]]))
                            if pair not in pairs:
                                pairs.add(pair)
                                lines.append(f"| {cat['name']} | {p[0]} ↔ {p[1]} | {other['name']} |\n")
        if len(lines) < 5:
            for cat in catalog["cultures"]:
                for p in cat.get("parallels", []):
                    lines.append(f"| {cat['name']} | {p[0]} | {p[1]} |\n")
        lines.append(f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n")
        with open(cross_ref_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"  ✓ Reference: cross-ref.md updated")
        count += 1

    # Generate motif-theme index (list motifs by theme)
    motif_path = os.path.join(REFERENCES_DIR, "motif-index.md")
    if should_regenerate or not os.path.isfile(motif_path):
        lines = [
            "# 母題索引\n\n",
            "> 按母題分類的跨文化神話條目。\n\n",
            "| 母題 | 相關文化 |\n",
            "|------|---------|\n",
        ]
        motif_map = {}
        for cat in catalog["cultures"]:
            for m in cat.get("motifs", []):
                if m not in motif_map:
                    motif_map[m] = []
                motif_map[m].append(cat["name"])
        for motif, cultures in sorted(motif_map.items()):
            lines.append(f"| {motif} | {', '.join(cultures[:5])} |\n")
        lines.append(f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n")
        with open(motif_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"  ✓ Reference: motif-index.md generated")
        count += 1

    return count


# ── Git helpers ──────────────────────────────────────────────────────────────

def git_commit(filepath, msg):
    try:
        subprocess.run(["git", "-C", REPO, "add", filepath], check=True, capture_output=True)
        subprocess.run(
            ["git", "-C", REPO, "commit", "-m", msg, "--allow-empty"],
            check=True, capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        pass

def git_push():
    try:
        subprocess.run(
            ["git", "-C", REPO, "push", "origin"],
            check=True, capture_output=True, timeout=120,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pass

def cleanup_temp_files():
    for dirpath, dirnames, filenames in os.walk(REPO):
        if "__pycache__" in dirnames:
            subprocess.run(["rm", "-rf", os.path.join(dirpath, "__pycache__")], capture_output=True)
        for fn in filenames:
            if fn.endswith(".pyc"):
                os.remove(os.path.join(dirpath, fn))
    log_path = os.path.join(REPO, "populate.log")
    if os.path.isfile(log_path):
        with open(log_path, "r+", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) > 100:
                f.seek(0)
                f.writelines(lines[-100:])
                f.truncate()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Mythos Atlas — Explorer")
    parser.add_argument("--mode", choices=["new", "enrich", "analyze", "ref", "explore"],
                        default="explore", help="Operation mode (default: explore = random pick)")
    parser.add_argument("--batch", type=int, default=1, help="Items to process per run (default: 1)")
    parser.add_argument("--random", action="store_true", help="Pick items randomly")
    args = parser.parse_args()

    catalog = load_catalog()
    state = load_state()
    state["runs"] += 1

    mode = args.mode
    is_random = args.random

    total = 0

    if mode == "explore":
        if is_random:
            mode = random.choice(["new", "enrich", "analyze", "ref"])
        else:
            # Cycle: try new first, then enrich, then analyze, then ref
            has_new = any(not culture_exists(c["id"]) for c in catalog["cultures"]) or \
                      any(not theme_exists(t["id"]) for t in catalog["themes"])
            if has_new:
                mode = "new"
            else:
                # Check if any culture can be enriched further
                enrichable = False
                for cat in catalog["cultures"]:
                    cid = cat["id"]
                    if culture_exists(cid) and \
                       (not has_god_subpages(cid) or not has_story_subpages(cid)):
                        enrichable = True
                        break
                if enrichable:
                    mode = random.choice(["enrich", "analyze", "ref"])
                else:
                    mode = random.choice(["analyze", "ref"])

    print(f"── Mode: {mode} | Batch: {args.batch} | Random: {is_random} | Run #{state['runs']} ──")

    total = 0
    # In explore mode, try fallback modes if chosen one produces nothing
    fallback_chain = {"new": ["enrich", "analyze", "ref"],
                      "enrich": ["analyze", "ref", "new"],
                      "analyze": ["ref", "enrich", "new"],
                      "ref": ["enrich", "analyze", "new"]}

    for attempt_mode in [mode] + (fallback_chain.get(mode, []) if args.mode == "explore" else []):
        if attempt_mode == "new":
            total = do_new_entries(catalog, state, args.batch, is_random)
        elif attempt_mode == "enrich":
            total = do_enrich(catalog, state, args.batch, is_random)
        elif attempt_mode == "analyze":
            total = do_analyze(catalog, state, args.batch, is_random)
        elif attempt_mode == "ref":
            total = do_reference(catalog, state, args.batch, is_random)
        if total > 0:
            if attempt_mode != mode:
                print(f"  ↪ Fallback to {attempt_mode}")
            break

    # Update indices after any changes
    update_cultures_index()
    update_themes_index()

    # Update README files with current state
    update_main_readme(catalog, state)
    update_directory_readmes(catalog)

    save_state(state)

    if total == 0:
        print("  ℹ Nothing to do in this mode. Try another mode or add new catalog entries.")
    else:
        print(f"  ✔ Done: {total} item{'s' if total>1 else ''} processed")

    git_push()
    cleanup_temp_files()


if __name__ == "__main__":
    main()
