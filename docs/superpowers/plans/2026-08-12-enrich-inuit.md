# Inuit Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the Inuit culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** All 10 weakest cultures are tied at 59 pages. Prior scheduler memory flags inuit/etruscan/maori as persistent bottlenecks; etruscan already has rich comparative coverage (18 comparisons incl. death-demons, divination, fate), while inuit lacks a domestic/household goddess, an Amarok-narrative story page (Amarok is only covered as predator-god in `gods/Nanook-Amarok.md`), and any theriogamy/animal-ancestor comparison. Pick topics not yet covered to maximise non-overlapping value.

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/inuit/gods/Sedna.md`, `cultures/inuit/stories/與狗結婚的女子.md`, `cultures/inuit/comparisons/Sedna海洋女神跨文化比較.md`)
- No placeholders; real mythological scholarship (web-verified: Rink 1866, Rasmussen 1932, Coulter & Turner 2013)
- Commit message: `mythos: enrich inuit`; push to origin/master

---

### Task 1: Create Pukkeenegak God Page

**Files:**
- Create: `cultures/inuit/gods/Pukkeenegak.md`
- Modify: `cultures/inuit/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Rink/Rasmussen/Copper Inuit tradition; inuit catalog entry
- Produces: God page differentiated from existing birth-goddess Akna (Akna = threshold/birthing guardian; Pukkeenegak = hearth/home, sewing/clothing craft, children & domestic production)

- [ ] **Step 1: Create the god page** — hearth/home + sewing + children goddess, cross-cultural table (Hestia/Vesta, Athena Ergane, 嫘祖, Neith, Pi-hsia-yuan-chün, 送子觀音), 參考文獻 (Coulter & Turner; Rasmussen; Corey & Ochoa)
- [ ] **Step 2: Add row to `cultures/inuit/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present (run `scripts/ci_checks.py` at end)

### Task 2: Create Kagsagsuk & the Amarok Story Page

**Files:**
- Create: `cultures/inuit/stories/kagsagsuk-amarok.md`
- Modify: `cultures/inuit/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Rink, *Tales and Traditions of the Eskimo* (1866), "The Amarok" chapter
- Produces: Story page on the persecuted orphan Kagsagsuk who is wrestled by the Amarok (tail knocks out growth-stunting bones; daily bouts → slays three bears). Cross-cultural parallels: Siberian shamanic initiatory dismemberment, North American vision quest, Roman Lupa, inuit orphan motif. Contrasts with the Amarok-as-predator god page and the existing orphan-bear story.

- [ ] **Step 1: Create the story page** — 故事背景 → 情節 (5 beats) → 文化意義 → 跨文化平行 table → 參考文獻 (Rink 1866; Rasmussen; Boas 1888; 因紐特口傳)
- [ ] **Step 2: Add row to `cultures/inuit/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Animal-Spouse & Animal-Ancestor Comparison Page

**Files:**
- Create: `cultures/inuit/comparisons/animal-spouse-animal-ancestor.md`
- Modify: `cultures/inuit/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: theriogamy motif (existing inuit story 與狗結婚的女子); Thompson Motif-Index B600–B699 / A1300+; Lévi-Strauss kinship theory
- Produces: 8-tradition comparison table (Inuit dog-husband, Chinese 盤瓠, Turkic Asena she-wolf, Roman Lupa, Japanese crane-wife, Celtic selkie, Native American bear-wife, Finno-Ugric bear-ancestor) + 4 structural analyses. Must be listed in comparisons/README.md (CI orphan check).

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/inuit/comparisons/README.md`**
- [ ] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (append story to inuit `stories`; add `gods` + `comparisons` keys), `_state.json` (append `inuit` to `enrich_log`; `runs` 112→113), `cultures/inuit/README.md` (counts 22/19/18 → 23/20/19)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich inuit — ..."` 
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
