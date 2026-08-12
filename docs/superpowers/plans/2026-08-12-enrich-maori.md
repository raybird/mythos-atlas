# Maori Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the Māori culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** Māori is tied at the bottom tier (56 content pages: 22 gods/17 stories/17 comparisons). The most significant untapped Māori topic cluster is **Matariki（昂宿星團）與毛利新年歲首**：gods/ 目前僅有星神 Rehua 與彩虹神 Uenuku，缺乏以星簇為神格的主條目；stories/ 已覆蓋 Rona 月、Māui 釣島與盜火、Tinirau 鯨等天文題材，但完全沒有昂宿升起與新年祭儀的故事頁；comparisons/ 則完全沒有「歲首星象與曆法」的跨文化比較（全球分析 `analyses/new-year-cosmic-renewal-myths-comparative.md` 與 `pleiades-seven-sisters-cross-cultural.md` 皆未以「歲首星象曆法」為軸心）。故選定 Matariki 歲首星象群為切入點。

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` / `## 參考來源` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/maori/gods/Uenuku.md`, `cultures/maori/stories/rona-moon.md`, `cultures/maori/comparisons/rainbow-deities-comparison.md`)
- No placeholders; real mythological scholarship (web-verified: Best 1922/1924, Rangi Mātāmua *Matariki: The Star of the Year* 2017, Grey 1855, Harris/Matamua et al. 2013, Orbell 1995, Krupp 1991)
- Commit message: `mythos: enrich maori`; push to origin/master

---

### Task 1: Create Matariki God Page

**Files:**
- Create: `cultures/maori/gods/Matariki.md`
- Modify: `cultures/maori/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Matariki = Ngā Mata o te Ariki Tāwhirimātea（風神 Tāwhirimātea 之眼）創世起源；毛利傳統計數九顆星（含母星 Matariki、Waitī、Waitā、Tupuānuku、Tupuārangi、Waipunarangi、Ururangi、Pōhutukawa 等）；2022 年紐西蘭立法為公共假日（Matariki Public Holiday Act 2022）；曆法/農業/航海/亡靈記憶功能（Harris, Matamua, Smith & Kerr 2013；Mātāmua 2017）
- Produces: God page with 概述 → 神格與形象（風神之眼／九星家族／歲首星象）→ 神話事蹟 → 跨文化對應 table（希臘七姊妹／印度 Kṛttikā／日本 Subaru／中國昴宿／澳洲七姊妹／阿茲特克 Tzab-ek）→ 相關神祇 → 出現在 → 參考文獻

- [ ] **Step 1: Create the god page** — with ≥300字 body + comparison table + refs
- [ ] **Step 2: Add row to `cultures/maori/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present

### Task 2: Create Matariki New-Year Story Page

**Files:**
- Create: `cultures/maori/stories/matariki-new-year-stars.md`
- Modify: `cultures/maori/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Tāwhirimātea 挖眼擲天的創世母題；昂宿在六月（Matariki 月在 winter solstice 前後）清晨偕日升作為毛利歲首；觀察九星象徵來年豐欠（Mātāmua 2017）；與 Puanga（獵戶座 Rigel）的替代傳統；現代復振（2022 立法）
- Produces: Story page with 故事背景 → 情節（風神之眼／黎明朝覲／九星與來年）→ 跨文化平行 table（印度 Kṛttikā 節／希臘航海曆／中國七月七／澳洲七姊妹歌線／古埃及 Sothis 曆）→ 文化意義 → 參考文獻

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/maori/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Year-Star Calendar Comparison Page

**Files:**
- Create: `cultures/maori/comparisons/new-year-stars-calendars-comparative.md`
- Modify: `cultures/maori/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: 以「歲首星象（heliacal rising 定歲首）」為軸的跨文化比較：毛利 Matariki／埃及 Sothis（天狼星）／希臘 Pleiades 航海曆／印度 Kṛttikā／日本 Subaru／中國昴宿與二十八宿／澳洲七姊妹歌線／阿茲特克 Xiuhtecuhtli 新火／美索不達米亞
- Produces: 8–9 文化比較表 + 4 結構分析（偕日升天文機制／星簇作為歲首閾限／農業-航海-節慶三功能／殖民斷裂與復振） + 參考來源

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/maori/comparisons/README.md`**
- [ ] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (pantheon += Matariki(昂宿星團/毛利新年); stories += 昂宿升空：毛利新年與歲首星象; `_stories` 13→14; add `gods` + `comparisons` keys), `_state.json` (append `maori` to `enrich_log`; `runs` 115→116), `cultures/maori/README.md` (counts 22/17/17 → 23/18/18)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Strip regenerated SVG clip-path/timestamp noise (keep meaningful stats changes); run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich maori — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
