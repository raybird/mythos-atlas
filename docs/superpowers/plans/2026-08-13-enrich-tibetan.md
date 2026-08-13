# Tibetan Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the tibetan culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** Three cultures are tied as weakest at 56 content pages (incan, tibetan, pre-islamic-arabian). Of these, tibetan has the clearest catalogued gap: its `pantheon` entry lists **魯（龍/水精靈）** — one of the five core Tibetan spirit classes alongside 念、贊 — yet there is **no dedicated god page, no water-spirit story, and no naga comparative study** (the existing 聖湖與大洪水跨文化比較 covers flood, not the lu/naga spirit class). Pick a single coherent topic cluster — 西藏魯與水界 (Tibetan Lu & the Water Realm) — so the god page, story page and comparison page reinforce each other without overlapping existing pages (Tibetan-Pantheon.md mentions lu only in passing; padmasambhava-subdues-* pages cover mountain/tenma, not nagas).

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/tibetan/gods/Tibetan-Pantheon.md`, `cultures/mongolian/gods/南斯拉伊.md`, `cultures/mongolian/stories/卡倫拜與土撥鼠.md`)
- No placeholders; real mythological scholarship (web-verified: Nebesky-Wojkowitz klu=nāga fusion; Bön *Klu 'bum dkar nag khra* three-volume White/Black/Variegated; PLB Phenyul klu manuscript (Bazhen Zeren 2023); Rigpa Wiki nāga entry; Oxford Pitt Rivers Dzamling Chisang/Lukhang festival record; Encyclopedia.com "Healing and Medicine in Tibet"; Harvard waterstories.org Ladakh lu ritual; Wikipedia Lhamo La-tso; Dalai Lama *Freedom in Exile*; dalailama.com "Birth to Exile"; Tibet.net Kashag statement)
- Commit message: `mythos: enrich tibetan`; push to origin/master

---

### Task 1: Create Lu God Page

**Files:**
- Create: `cultures/tibetan/gods/魯.md`
- Modify: `cultures/tibetan/gods/README.md` (add table row)

**Interfaces:**
- Consumes: nāga/klu scholarship (Nebesky-Wojkowitz 1956; Rigpa Wiki; Bön Klu 'bum; PLB; Ladakh Eight Great Nagas ritual; Dzamling Chisang festival)
- Produces: God page differentiated from existing mountain-spirit (Nyenchen-Thanglha) and flood (manasarovar) pages: 魯 = the Tibetan water-spirit class, fusion of indigenous lu with Indian nāga, bestows wealth & rain, inflicts skin disease/leprosy (klu'i nad) when offended

- [ ] **Step 1: Create the god page** — 概述 (names: 魯/klu, etymology, indigenous + nāga fusion) → 神話事蹟 (Bön 《十萬龍經》白黑花三部、Sangs po 與 Chu lcam 龍王誕生、九種龍病、三大聖湖為龍居、佛教轉化 Apalala/Vajrapani、蓮花生降伏龍眾、龍王節 Dzamling Chisang 於龍王潭 Lukhang) → 形象與象徵 (蛇身人首、白黑花三色、龍珠) → 跨文化對應 table (印度Nāga/中國龍王/日本龍神/蒙古蘆斯/美索不達米亞Abzu/北歐Jörmungandr) → 相關神祇 → 出現在 → 參考文獻
- [ ] **Step 2: Add row to `cultures/tibetan/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present

### Task 2: Create Lhamo Latso Story Page

**Files:**
- Create: `cultures/tibetan/stories/拉姆拉錯神諭之湖.md`
- Modify: `cultures/tibetan/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Lhamo La-tso oracle lake tradition (regents seek visions since 2nd Dalai Lama; Palden Lhamo as lake guardian); 1935 Reting Rinpoche vision (letters Ah/Ka/Ma, three-storied monastery, small house) → discovery of 14th Dalai Lama (Taktser); object tests (rosary, walking stick, damaru); documented in *Freedom in Exile* and official accounts
- Produces: Story page (故事背景 → 情節 → 故事分析 → 跨文化平行 table → 相關主題 → 參考文獻); ties the Lu water-world to the lake-as-oracle mirror; must NOT duplicate 松贊干布與二妃 (Jokhang) or manasarovar-flood-rebirth

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/tibetan/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Water-Spirit Comparison Page

**Files:**
- Create: `cultures/tibetan/comparisons/龍族水靈跨文化比較.md`
- Modify: `cultures/tibetan/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: naga/lu scholarship + comparative water-spirit material (Indian Nāga/Vasuki/Shesha/Apalala; Chinese 四海龍王; Japanese 龍神/龍宮; Mongolian Lus; Mesopotamian Abzu/Tiamat; Norse Jörmungandr; Greek Oceanus/Python; Egyptian Nun/Apep; Australian Rainbow Serpent)
- Produces: 9-tradition comparison table + 4 structural analyses (water as liminal membrane between worlds; wealth/disease duality as environmental-ethics myth; serpentine iconography & shared dragon-pearl/naga-mani symbol; from animistic spirits to hierarchized dragon-kings & Buddhist dharma-protectors) + 結論 + 參考文獻. Must be listed in comparisons/README.md (CI orphan check)

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/tibetan/comparisons/README.md`**
- [ ] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (append 魯 to tibetan `gods`; append 拉姆拉錯神諭之湖 to `stories`, `_stories` 7→8; append 龍族水靈跨文化比較 to `comparisons`), `_state.json` (append `tibetan` to `enrich_log`; `runs` 123→124), `cultures/tibetan/README.md` (counts 19/17/17 → 21/19/19)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich tibetan — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
