#!/usr/bin/env python3
"""
Mythos Atlas — 自動充實與探索腳本
不再受限於固定框架：除了生成新條目，還會隨機探索、深化既有條目、
產出跨文化分析與參考文獻，讓傳說資料庫持續成長。

Usage:
  python3 populate.py                          # 預設：探索模式（隨機挑選動作）
  python3 populate.py --mode new               # 僅生成新條目
  python3 populate.py --mode enrich            # 僅深化既有條目
  python3 populate.py --mode analyze           # 僅產生分析文章
  python3 populate.py --mode ref               # 僅產生參考文獻
  python3 populate.py --batch 3                # 一次處理 3 項
  python3 populate.py --random                 # 隨機選取而非依序
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
    {
        "slug": "female-deities",
        "title": "女神崇拜比較研究",
        "title_en": "Comparative Study of Goddess Worship",
        "description": "跨文化中女神形象的比較——從大地母神到戰爭女神，從智慧女神到愛神。"
    },
    {
        "slug": "underworld-journey",
        "title": "冥界之旅：死亡與重生",
        "title_en": "The Underworld Journey: Death and Rebirth",
        "description": "英雄/神祇進入冥界並返回的主題，從伊南娜到奧菲斯，從伊邪那岐到耶穌。"
    },
    {
        "slug": "animal-symbolism",
        "title": "神話動物象徵體系",
        "title_en": "Mythological Animal Symbolism",
        "description": "龍、鳳凰、蛇、狼、熊、烏鴉等動物在不同神話體系中的象徵意義比較。"
    },
    {
        "slug": "sacred-mountains",
        "title": "聖山：天地之間的橋樑",
        "title_en": "Sacred Mountains: Axis Mundi Across Cultures",
        "description": "崑崙、須彌、奧林帕斯、西奈、富士——聖山作為宇宙軸心的跨文化比較。"
    },
    {
        "slug": "origin-of-death",
        "title": "死亡的起源：神話中的解釋",
        "title_en": "The Origin of Death: Mythological Explanations",
        "description": "為什麼人會死？——從月神訊息傳達失誤到香蕉樹神話，跨文化如何解釋死亡的起源。"
    },
    {
        "slug": "rainbow-myths",
        "title": "彩虹神話與象徵",
        "title_en": "Rainbow Myths and Symbolism",
        "description": "彩虹作為橋樑、蛇、神之弓的跨文化比較。"
    },
    {
        "slug": "cosmic-egg",
        "title": "宇宙卵：創世原型的全球比較",
        "title_en": "The Cosmic Egg: A Global Creation Archetype",
        "description": "從印度金卵到中國盤古卵，從芬蘭世界蛋到波利尼西亞宇宙蛋——卵生創世的跨文化比較。"
    },
    {
        "slug": "sacrificial-creation",
        "title": "犧牲創世：巨人化生萬物",
        "title_en": "Sacrificial Creation: The Dismembered Giant",
        "description": "盤古、Ymir、Purusha、Gayomart——巨人被殺後身體化為宇宙各部分的跨文化比較。"
    },
    {
        "slug": "sun-myths",
        "title": "太陽神話與太陽崇拜",
        "title_en": "Sun Myths and Solar Worship",
        "description": "從Ra的阿頓船到Inti的金子，從阿波羅的馬車到天照大神——太陽崇拜的跨文化比較。"
    },
    {
        "slug": "twin-myths",
        "title": "神話中的雙生子",
        "title_en": "Twins in World Mythology",
        "description": "創世雙子、英雄雙子、善惡雙子——雙生子神話的跨文化類型學。"
    },
    {
        "slug": "earth-diver-comparative",
        "title": "大地潛水者創世神話",
        "title_en": "The Earth-Diver Creation Myth",
        "description": "動物潛入原始海洋取泥造地的廣泛分布——從北亞到北美，從東歐到南亞。"
    },
    {
        "slug": "shamanism-in-myth",
        "title": "神話中的薩滿元素",
        "title_en": "Shamanic Elements in World Mythology",
        "description": "薩滿式靈魂旅程、宇宙樹、動物助手等元素在神話中的體現與比較。"
    },
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

    save_state(state)

    if total == 0:
        print("  ℹ Nothing to do in this mode. Try another mode or add new catalog entries.")
    else:
        print(f"  ✔ Done: {total} item{'s' if total>1 else ''} processed")

    git_push()
    cleanup_temp_files()


if __name__ == "__main__":
    main()
