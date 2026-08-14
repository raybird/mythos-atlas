# Armenian Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the armenian culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** Three cultures are tied as weakest at 57 content pages (armenian, minoan, nubian). armenian was enriched longest ago (2026-08-04, 7158daf3) and has the fewest god pages (20). Its current coverage (Aramazd, Vahagn, Anahit, Tir, Mihr, Astghik, Spandaramet, Tsovinar, Grogh, Hayk, lunar & solar pages, dragon-slayer stories) has **no sky/weather god page for Barsamin, no Vardavar water-festival story, and no water-festival comparative study** — while both are exceptionally well documented (Movses Khorenatsi's Tʿordan temple, Anania Shirakatsi's Milky Way "straw-thief" tale, Vardavar's pagan→Christian continuity). Pick a single coherent topic cluster — 亞美尼亞的天空與水 (Armenian sky & water) — so the god page (Barsamin the sky/weather god), story page (Vardavar rose-and-water festival) and comparison page (global water-splashing festivals) reinforce each other without overlapping existing pages.

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/armenian/gods/aramazd.md`, `stories/lusin-moon-origin.md`, `comparisons/tsovinar-water-goddess.md`)
- No placeholders; real mythological scholarship (web-verified: Movses Khorenatsi *History of the Armenians* 1.14/2.14 Tʿordan temple; Anania Shirakatsi *Cosmography* Milky Way "straw-thief's path" (Hardagoghi chanaparh); Kurkjian *A History of Armenia* ch. 34 (Tigran transported the idol, Aram/Barsamin Babylon struggle); Agathangelos (Gregory destroyed the Tʿordan temple); ICH Armenia Vardavar dossier; Armenian Prelacy Transfiguration; Fundamental Armenology Devrikyan on Vardavar)
- Commit message: `mythos: enrich armenian`; push to origin/master

---

### Task 1: Create Barsamin God Page

**Files:**
- Create: `cultures/armenian/gods/barsamin.md`
- Modify: `cultures/armenian/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Baalshamin scholarship (Palmyra temple inscription 131 CE; Safaitic rain monopoly; Teixidor *The Pagan God*) + Armenian attestations (Khorenatsi 1.14/2.14; Shirakatsi; Agathangelos; Kurkjian ch. 34)
- Produces: God page differentiated from existing Aramazd (who absorbed Baalshamin's positive functions) and Vahagn (his rival weather god): Barsamin = imported Semitic "Lord of Heaven", temple at Tʿordan, ivory-and-crystal silver-wrought idol, epithet "of white glory" (spitakapʿaṙ), Milky Way straw-thief myth, Aram the giant-slayer parallel

- [ ] **Step 1: Create the god page** — 概述 (etymology from Baal Shamin "天之主", import via Mesopotamia under Tigran, Tʿordan temple, absorption by Aramazd) → 神話事蹟 (Vahagn's straw theft → Milky Way per Anania Shirakatsi; Aram slays the giant Barsamin; state-wars mythologization per Kurkjian) → 跨文化對應 table (Baal Shamin/Hadad/Zeus Olympios/Aramazd/Vahagn/Teisheba/Ahura Mazda) → 相關神祇 → 出現在 → 參考文獻
- [ ] **Step 2: Add row to `cultures/armenian/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present

### Task 2: Create Vardavar Story Page

**Files:**
- Create: `cultures/armenian/stories/vardavar-astghik.md`
- Modify: `cultures/armenian/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Vardavar scholarship (Armenian Prelacy 2025; ICH Armenia dossier 2023; Zograbian *Armat* 2025; Devrikyan *Fundamental Armenology*; Kurkjian ch. 34 on Astghik)
- Produces: Story page (故事背景 → 情節: Astghik's bleeding feet → crimson rose; rose-and-water rites at her temple; dove release (gyuverin panayiri); Noah's command to sprinkle water after the Flood; Gregory's fusion with Transfiguration; khundum rite, Vardavar apple → 故事分析: blood→flower transformation, fire-water balance, flood memory → 跨文化平行 table → 相關主題 → 參考文獻); must NOT duplicate the existing lusin-moon-origin (moon) or tsovinar-water-goddess (storm goddess) pages

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/armenian/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Water-Festival Comparison Page

**Files:**
- Create: `cultures/armenian/comparisons/vardavar-water-festivals-comparative.md`
- Modify: `cultures/armenian/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: water-festival scholarship (Eliade *Patterns in Comparative Religion*; Bakhtin *Rabelais and His World* carnival; National Geographic Songkran 2026; *ASEAN Magazine* 2024; Wikipedia Water Festival & Water-Sprinkling Festival)
- Produces: 9-10 tradition comparison table (Vardavar/Songkran/Thingyan/傣族潑水節/Pi Mai/Chaul Chnam Thmey/Holi/Śmigus-Dyngus/La Batalla del Agua) + 5 structural analyses (water as annual purification; rain-invocation / sympathetic magic; carnivalesque status-inversion vs respect-to-elders; pagan→Christian/Buddhist conversion; rose+colour love subtype) + 結論 + 參考文獻. Must be listed in comparisons/README.md (CI orphan check)

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/armenian/comparisons/README.md`**
- [ ] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (append 瓦爾達瓦：玫瑰與水的節日 to armenian `stories`, `_stories` 11→12; append `Barsamin` to `gods`; append 潑水節慶跨文化比較：瓦爾達瓦與全球水之祭典 to `comparisons`; add `Barsamin(蒼穹/天氣)` to `pantheon`), `_state.json` (append `armenian` to `enrich_log`; `runs` 141→142), `cultures/armenian/README.md` (counts 20/18/19 → 21/19/20)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich armenian — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
