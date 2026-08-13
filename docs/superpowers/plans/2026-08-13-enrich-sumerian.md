# Sumerian Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the sumerian culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** sumerian is the enrichment-priority culture (priority order sumerian > mayan > persian > yoruba; it is the deepest at 201 pages = 70 gods/65 stories/66 comparisons). Existing sumerian content already covers the major pantheon (An/Enlil/Enki/Inanna/Ninhursag/Utu/Nanna/Nergal), the flood cycle, underworld journeys, sacred marriage, city-laments, wisdom/debate literature, and astral sun/moon gods — but there is **no page for the personal god (diĝir)**, the individual tutelary deity at the heart of Sumerian "family religion", no story for the Sumerian "Job" text *A Dialogue between a Man and his God* (ETCSL 5.1.4, the earliest known theodicy), and no comparative study of theodicy/suffering across cultures. Pick a single coherent topic cluster — **個人守護神／受苦者／神義論** — so the god page, story page and comparison page reinforce each other without overlapping existing pages (Venus/morning-star and justice comparisons are already covered elsewhere and must NOT be reused).

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), Sumerian/Akkadian/English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/sumerian/gods/Nungal.md`, `stories/ur-namma-death.md`, `comparisons/underworld-queens-comparison.md`)
- No placeholders; real mythological scholarship (ETCSL 5.1.4; Kramer 1955 "Man and His God"; Lambert 1960 *Babylonian Wisdom Literature*; van der Toorn 1996 *Family Religion in Babylonia, Syria and Israel*; Jacobsen 1976 *Treasures of Darkness*; Lichtheim 1973 on the Egyptian Dispute of a Man with his Ba; 《約伯記》、屈原〈天問〉、《史記·伯夷列傳》、《摩訶婆羅多》Yakṣa 問答)
- Commit message: `mythos: enrich sumerian`; push to origin/master

---

### Task 1: Create Personal God (Diĝir) God Page

**Files:**
- Create: `cultures/sumerian/gods/dingir-personal-god.md`
- Modify: `cultures/sumerian/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Sumerian "family religion" scholarship (van der Toorn 1996); personal god as intercessor before the divine assembly; personal god's withdrawal → suffering (ETCSL 5.1.4); votive inscriptions "for the life of X, to his god"; personal goddess (lamma)
- Produces: God page (概述 → 神話與宗教事蹟: 個人神與神義論／個人神與護佑 → 跨文化對應 table → 相關神祇 → 出現在 → 參考文獻), differentiated from the state/city pantheon pages; must be listed in gods/README.md (CI orphan safety)

- [ ] **Step 1: Create the god page** (≥300 字; 跨文化對應: Roman Genius, Greek daimōn, guardian angel, 道教神隱/本命神, 灶神家神, ishta-devatā, šēdu)
- [ ] **Step 2: Add row to `cultures/sumerian/gods/README.md`**

### Task 2: Create Man-and-his-God Story Page

**Files:**
- Create: `cultures/sumerian/stories/man-and-his-god-dialogue.md`
- Modify: `cultures/sumerian/stories/README.md` (add table row)

**Interfaces:**
- Consumes: ETCSL 5.1.4 (first-person lament: sickness, slander, social isolation; personal god's withdrawal; prayer/repentance/sacrifice; god's silent mercy; closing hymn); Kramer 1955; Lambert 1960
- Produces: Story page (故事背景 → 情節 four acts: 苦難的全面壓迫／尋找苦難的根源／禱告懺悔與重歸於好／神義論的妥協 → 跨文化平行 table: Job/Psalms/Ludlul/屈原/Buddhist karma → 相關主題 → 參考文獻); must NOT duplicate existing sumerian stories (adapa, flood, laments already present)

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/sumerian/stories/README.md`**

### Task 3: Create Theodicy Comparative Page

**Files:**
- Create: `cultures/sumerian/comparisons/theodicy-suffering-comparative.md`
- Modify: `cultures/sumerian/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: Sumerian Dialogue (ETCSL 5.1.4); Babylonian Ludlul bēl nēmeqi + Babylonian Theodicy (Lambert 1960); Biblical Job; Egyptian Dispute of a Man with his Ba (Lichtheim 1973); Greek tragic theodicy / phthonos theōn; Chinese 屈原〈天問〉 + 《史記·伯夷列傳》; Indian karma / Yakṣa Prashna (《摩訶婆羅多》)
- Produces: 7-culture comparison table + 3 structural analyses (苦難歸因: 契約破裂 vs 業力 vs 天庭試煉／神回應方式: 沉默救贖 vs 旋風發言 vs 悲劇宿命／神義論的社會功能) + 結論 + 參考文獻. Must be listed in comparisons/README.md (CI orphan check)

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/sumerian/comparisons/README.md`**

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (append `Diĝir（個人守護神）` to sumerian `gods`; append `〈人神對話〉（蘇美版約伯記）` to `stories`, `_stories` 8→9; append `苦難與神義論跨文化比較` to `comparisons`; append `、Diĝir(個人守護神)` to `pantheon`), `_state.json` (append `sumerian` to `enrich_log`; `runs` 127→128), `cultures/sumerian/README.md` (counts → 71 位神祇/66 則故事/67 篇比較, update timestamp), README.md (sumerian row 69/64/65 → 71/66/67)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich sumerian — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
