# Etruscan Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the Etruscan culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** Etruscan is tied at the bottom tier (56 content pages: 21 gods/18 stories/17 comparisons) and is the least-recently enriched bottleneck culture (last enrich 9b834f76, 2026-08-01). The dawn-goddess topic (Thesan) is already covered by the global analysis `analyses/dawn-deities-comparative.md`; Phersu/funeral-games and general fire deities are also covered (`sacred-masks-mythology.md`, `ritual-combat-sacred-warfare-comparative.md`, `etruscan-fire-deities-comparative.md`). Chosen cluster instead: the chthonic fire-wolf god Śuri/Soranus (attested in Pyrgi graffiti) + the aetiological fire-walking legend of the Hirpi Sorani (Servius ad Aen. 11.785) + a fire-walking/wolf-priest cross-cultural comparison — a genuine non-overlapping gap.

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` / `## 參考來源` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/etruscan/gods/Morta.md`, `cultures/etruscan/stories/Vibenna兄弟傳奇.md`, `cultures/etruscan/comparisons/Culsans-與-Selvans-門檻與邊界之神跨文化比較.md`)
- No placeholders; real mythological scholarship (web-verified: Colonna 1992, De Grummond 2006, Franklin 1921, Hiltebeitel 1991, Xygalatas 2012, Eliade 1964)
- Commit message: `mythos: enrich etruscan`; push to origin/master

---

### Task 1: Create Śuri / Soranus God Page

**Files:**
- Create: `cultures/etruscan/gods/Suri-Soranus.md`
- Modify: `cultures/etruscan/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Pyrgi "śuri" graffiti (Colonna's derivation of Soranus from Etruscan Śuri); Servius ad Aen. 11.785; Pliny NH 7.19; De Grummond 2006
- Produces: God page on the chthonic solar fire god (underworld + sun, plague/health, oracular, volcanic lightning, Novensiles), wolf & goat sacred animals, Mt. Soracte cult, identifications with Aita/Manth/Vetis/Calu/Usil/Apulu and Roman Dis Pater/Vejovis/Summanus

- [ ] **Step 1: Create the god page** — 概述 → 神話事蹟 → 跨文化對應 table (羅馬/希臘/印度/北歐/中國/馬雅) → 相關神祇 → 出現在 → 參考文獻
- [ ] **Step 2: Add row to `cultures/etruscan/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present (run `scripts/ci_checks.py` at end)

### Task 2: Create Hirpi Sorani Fire-Walking Story Page

**Files:**
- Create: `cultures/etruscan/stories/hirpi-sorani-fire-walking.md`
- Modify: `cultures/etruscan/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Servius ad Aen. 11.785 (wolves steal entrails → cave fumes → plague → oracle to imitate wolves → Hirpi Sorani); Pliny NH 7.19 (Senate exemption); Virgil Aen. 11.784–787 (Arruns' prayer); Strabo 5.2.9 (Feronia link); Franklin, *The Lupercalia* (1921)
- Produces: 5-chapter aetiological legend (祭品被奪 / 毒氣洞穴 / 瘟疫 / 神諭效法群狼 / 不焚之足) + 文化意義 + 跨文化平行 table (Lupercalia / Lycaon / Draupadī Theemithi / Anastenaria / 上刀山下火海) + 參考文獻

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/etruscan/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Fire-Walking & Wolf-Priest Comparison Page

**Files:**
- Create: `cultures/etruscan/comparisons/fire-walking-wolf-priests-comparative.md`
- Modify: `cultures/etruscan/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: fire-walking ordeals and wolf-cult priesthoods worldwide; Frazer/Eliade comparative method; extreme-ritual anthropology (Xygalatas 2012)
- Produces: 8-tradition comparison table (Etruscan Hirpi Sorani / Greek Lycaea / Roman Lupercalia / Indian Theemithi / Balkan Anastenaria / Tahitian umu ti / 中國-東亞儺戲科儀 / 滿洲-西伯利亞薩滿火行) + 4 structural analyses (火作閾限 / 獸形神與化獸祭司 / 極限儀式與豁免 / 瘟疫→神諭→祭儀病因敘事) + 參考來源

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/etruscan/comparisons/README.md`**
- [ ] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (pantheon += Śuri/Soranus; stories += 希爾皮·索拉尼的狼祭火行; `_stories` 7→8; add `gods` + `comparisons` keys), `_state.json` (append `etruscan` to `enrich_log`; `runs` 114→115), `cultures/etruscan/README.md` (counts 21/18/17 → 22/19/18)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Strip regenerated SVG clip-path/timestamp noise (keep meaningful stats changes); run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich etruscan — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
