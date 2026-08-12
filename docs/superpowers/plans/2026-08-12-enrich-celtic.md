# Celtic Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the Celtic culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** Celtic is at the bottom tier (59 content pages: 23 gods/19 stories/17 comparisons), tied as the weakest alongside basque/incan/tibetan/pre-islamic-arabian/mongolian/indigenous-americas. Priority cultures sumerian(201)/mayan(181)/persian(174)/yoruba(175) are already the deepest tier, so the weakest-literature-rich culture wins. Celtic retains one of the richest surviving literary corpora (Ulster Cycle, Mythological Cycle). The selected cluster is the **Morrígna / Macha / Ces Noínden Ulad** (三重戰爭—命運女神): gods/ lacks Macha (主權/戰爭/馬女神，Morrígna 三合一); stories/ has the Táin but not its narrative premise *Noínden Ulad* (阿爾斯特人的虛弱，Macha 賽馬詛咒)；comparisons/ has sovereignty/horse-goddess pages but no triple war-fate goddess (Morrígna vs Moirai/Parcae/Norns/Valkyries/Matres) structural comparison.

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` / `## 參考來源` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/celtic/gods/Lugh.md`, `cultures/celtic/stories/Cú-Chulainn少年傳奇.md`, `cultures/celtic/comparisons/sovereignty-goddess-comparative.md`)
- No placeholders; real mythological scholarship (web-verified: Hull 1968 *Celtica* 8; Macalister 1956 LGE V; Kinsella 1969 *The Táin*; Sjoestedt 1982; Mac Cana 1970; Tatár 2007 JIES; Rees & Rees 1961; Hennessey 1870 *Revue Celtique*)
- Commit message: `mythos: enrich celtic`; push to origin/master

---

### Task 1: Create Macha God Page

**Files:**
- Create: `cultures/celtic/gods/Macha.md`
- Modify: `cultures/celtic/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Macha = 主權/戰爭/馬女神；Morrígna 三位一體（Badb 戰鴉、Macha、Nemain 狂亂）；Emain Macha（納文堡）與 Ard Macha（阿馬）地名；Ces Noínden Ulad 賽馬詛咒；Macha Mong Ruad 人間女王；《奧馬爾康尼詞彙表》「戰死者之頭」銘記；Cú Chulainn 的 Liath Macha 坐騎（Hull 1968；Macalister 1956；Sjoestedt 1982）
- Produces: God page with 概述 → 神格與形象（三重面相／主權女神）→ 神話事蹟（賽馬詛咒／Cú Chulainn／人間女王）→ 跨文化對應 table（Sekhmet/Athena/Freyja/Bellona/Matres/Ériu/Eileithyia）→ 相關神祇 → 出現在 → 參考文獻

- [x] **Step 1: Create the god page** — 1220 CJK字 + comparison table + refs
- [x] **Step 2: Add row to `cultures/celtic/gods/README.md`**
- [x] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present

### Task 2: Create Ces Noínden Ulad Story Page

**Files:**
- Create: `cultures/celtic/stories/ces-noiden-ulad.md`
- Modify: `cultures/celtic/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Crunnchu mac Agnomain 之妻；Conchobar 賽馬集會；丈夫誇口妻子快過御馬；王以死脅迫；孕中賽馬勝出、終點產下雙胞胎 Fír/Fial；詛咒阿爾斯特男子九代、五天四夜產婦虛弱；Emain Macha 地名由來；詛咒應驗於 Táin，唯 Cú Chulainn 倖免（Hull 1968；Book of Leinster；Kinsella 1969；Carmody 2015）
- Produces: Story page with 故事背景 → 情節（神祕妻子／國王集會／被迫競賽／詛咒／應驗）→ 跨文化平行 table（得墨忒耳／Leto 難產／Atalanta 競速／天鵝少女／北歐狂暴之禁／忒拜世代詛咒／Sekhmet／Dindshenchas）→ 文化意義 → 相關主題 → 參考文獻

- [x] **Step 1: Create the story page**
- [x] **Step 2: Add row to `cultures/celtic/stories/README.md`**
- [x] **Step 3: Verify** (format/citation)

### Task 3: Create Triple War-Fate Goddess Comparison Page

**Files:**
- Create: `cultures/celtic/comparisons/war-goddess-triads-comparative.md`
- Modify: `cultures/celtic/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: 以「三合女神」為軸的跨文化比較：凱爾特 Morrígna（Morrígan/Badb/Macha/Nemain）／希臘 Moirai 與 Erinyes／羅馬 Parcae 與 Matres／北歐 Norns 與 Valkyries／斯拉夫 Rožanicy／高盧-羅馬 Matronae；Dumézil 系三合結構研究
- Produces: 8 文化比較表 + 4 結構分析（三為全體象徵／主動介入光譜／女神與王權連結／三合與二元張力） + 參考來源

- [x] **Step 1: Create the comparison page**
- [x] **Step 2: Add row to `cultures/celtic/comparisons/README.md`**
- [x] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (pantheon += Macha(戰爭/主權/馬女神); stories += 阿爾斯特人的虛弱：Macha的賽馬詛咒; `_stories` 7→8; `gods` += Macha; `comparisons` += 三重戰爭—命運女神跨文化比較), `_state.json` (append `celtic` to `enrich_log`; `runs` 116→117), `cultures/celtic/README.md` (counts 23/19/17 → 24/20/18)

- [x] **Step 1:** Apply catalog/state/README edits
- [x] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [x] **Step 3:** Run `python3 scripts/ci_checks.py` — error count 411 (0 新增), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich celtic — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
