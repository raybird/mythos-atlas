# Basque Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the basque culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** Four cultures are tied as weakest at 56 pages (basque, incan, mongolian, pre-islamic-arabian, tibetan). basque was enriched least recently among them (enrich_log index 7 of 108; last commit 2026-08-08). Its existing coverage includes Mari/Sugaar (deities), storm/water figures, household imps, wild-men and the flood—but **no founding-king / supernatural-ancestry narrative**, no Jaun Zuria page, and no sea-monster-founder comparative study. Pick a single coherent topic cluster — the founding of the Lordship of Biscay through the sea-serpent ancestor Sugaar — so the god page, story page and comparison page reinforce each other without overlapping existing pages.

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/basque/gods/Galtzagorriak.md`, `stories/sugaar-first-council.md`, `comparisons/helper-spirits-labour-comparative.md`)
- No placeholders; real mythological scholarship (web-verified: Lope García de Salazar, *Bienandanzas e Fortunas* c. 1454; Pedro Afonso, *Livro de Linhagens* 1323–1344; Jon Bilbao 1982; Mañaricua 1976; Fredegar Chronicle; Ferrari 2024)
- Commit message: `mythos: enrich basque`; push to origin/master

---

### Task 1: Create Jaun Zuria God Page

**Files:**
- Create: `cultures/basque/gods/JaunZuria.md`
- Modify: `cultures/basque/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Biscay founding legend (Salazar & Barcelos chronicles), Auñamendi Encyclopedia, Jon Bilbao 1982, Mañaricua 1976
- Produces: God page differentiated from existing Mari/Sugaar pages: Jaun Zuria = mythical first Lord of Biscay, son of the sea-serpent Sugaar and a Scottish princess; elected captain for his royal blood, victor of the Battle of Padura/Arrigorriaga, sworn in under the Tree of Gernika

- [ ] **Step 1: Create the god page** — 概述 (name "White Lord", chronicle sources, Sugaar paternity) → 神話事蹟 (sea birth at Mundaka, the 22-year-old captain, Padura/Arrigorriaga battle & two-wolves omen, Gernika oath) → 形象與象徵 (whiteness as divine mark, noble stranger motif) → 跨文化對應 table (Merovech/Scyld Scefing/Alexander/契·后稷) → 相關神祇 → 出現在 → 參考文獻
- [ ] **Step 2: Add row to `cultures/basque/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present

### Task 2: Create Scottish Princess Story Page

**Files:**
- Create: `cultures/basque/stories/scottish-princess-sea-serpent.md`
- Modify: `cultures/basque/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Salazar *Bienandanzas e Fortunas* (Rodríguez Herrero ed.), Bilbao 1982; must NOT duplicate existing `stories/sugaar-first-council.md` (law-giving) — this story focuses on the founding narrative, battle and oath
- Produces: Story page (故事背景 → 情節 in phases: Mundaka landing → white son & royal blood → Padura battle & Arrigorriaga naming → Gernika oath + Durango marriage epilogue → 故事分析 → 跨文化平行 table → 參考文獻)

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/basque/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Sea-Monster Founder-Kings Comparison Page

**Files:**
- Create: `cultures/basque/comparisons/sea-monster-founder-kings.md`
- Modify: `cultures/basque/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: founding-king / supernatural-ancestry motif (Jaun Zuria–Sugaar; Merovech–Quinotaur; Alexander–Ammon serpent; Scyld Scefing sea-foundling; Romulus–Mars/she-wolf; Theseus–Poseidon; 契 swallow-egg; 后稷 footprint)
- Produces: 8-tradition comparison table + 4 structural analyses (sacral kingship via supernatural paternity; sea/water as liminal generative realm; foreign founder as integrator; whiteness/body-mark as election sign) + 結論 + 參考文獻. Must be listed in comparisons/README.md (CI orphan check)

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/basque/comparisons/README.md`**
- [ ] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (append story to basque `stories`; add Jaun Zuria to `pantheon`+`gods`; add comparison to `comparisons`; `_stories` 7→8), `_state.json` (append `basque` to `enrich_log`; `runs` 119→120), `cultures/basque/README.md` (counts 20/18/18 → 21/19/19)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich basque — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
