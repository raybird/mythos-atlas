# Indigenous American Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the indigenous-americas culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** Six cultures are tied as weakest at 56 pages (basque, incan, indigenous-americas, mongolian, pre-islamic-arabian, tibetan). indigenous-americas was enriched least recently (2026-08-05) among them. Its existing coverage includes Coyote/Iktomi/Nanabozho/Raven tricksters but **no Plains creator-trickster (Blackfoot Napi)**, no clay-creation narrative page (only 死亡的起源 covers the immortality test), and no clay-creation comparative study. Pick a single coherent topic cluster — Blackfoot Napi creation — so the god page, story page and comparison page reinforce each other without overlapping existing pages.

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/indigenous-americas/gods/Iktomi.md`, `stories/星辰丈夫.md`, `comparisons/horned-serpent-cross-cultural.md`)
- No placeholders; real mythological scholarship (web-verified: Grinnell 1892 *Blackfoot Lodge Tales*, Wissler & Duvall 1908, Bullchild 1985, Erdoes & Ortiz 1984)
- Commit message: `mythos: enrich indigenous-americas`; push to origin/master

---

### Task 1: Create Napi God Page

**Files:**
- Create: `cultures/indigenous-americas/gods/Napi.md`
- Modify: `cultures/indigenous-americas/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Blackfoot confederacy (Siksika/Kainai/Piikani) oral tradition; Grinnell 1892, Wissler & Duvall 1908, Bullchild 1985
- Produces: God page differentiated from existing tricksters (Coyote/Iktomi/Nanabozho/Raven): Napi = creator-trickster of the Plains who both makes the world from clay and botches it; also the figure who names Blackfoot sacred geography (the Knees, Sweet Grass Hills, Old Man's Sliding Ground)

- [ ] **Step 1: Create the god page** — 概述 (name Na'pi "Old Man", confederacy spread, creator/trickster duality) → 神話事蹟 (south-to-north world-making & place-naming, clay woman-and-child awakened on 4th day, clay buffalo breathed alive, fire-drill & hunting gifts, death-order debate) → 形象與象徵 → 跨文化對應 table (Coyote/Iktomi/Nanabozho/Raven + Viracocha/Prometheus) → 出現在 → 參考文獻 (Grinnell; Wissler & Duvall; McClintock; Bullchild; Erdoes & Ortiz)
- [ ] **Step 2: Add row to `cultures/indigenous-americas/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present (final `scripts/ci_checks.py` run)

### Task 2: Create Napi Creates Humanity Story Page

**Files:**
- Create: `cultures/indigenous-americas/stories/napi-creates-humanity.md`
- Modify: `cultures/indigenous-americas/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Grinnell, *Blackfoot Lodge Tales* (1892) "Blackfoot Genesis" (pp. 137–144); primary account of clay figures covered under a robe and awakened on the fourth day, breath-blown mud humans & buffalo at the Porcupine Mountains, buffalo jump, flint knives, fire-drill
- Produces: Story page (故事背景 → 情節 in phases → 文化意義 → 跨文化平行 table incl. Genesis 2:7 breath, Khnum potter, Tāne's Hine-ahu-one → 參考文獻). Must NOT duplicate existing `stories/死亡的起源.md` (death-origin) or `stories/納皮.md` (none exists)

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/indigenous-americas/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Clay-Creation Cross-Cultural Comparison Page

**Files:**
- Create: `cultures/indigenous-americas/comparisons/clay-creation-cross-cultural.md`
- Modify: `cultures/indigenous-americas/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: clay/original-moulding creation motif (Thompson Motif-Index A1241); Genesis 2:7; Khnum (Egypt), Enki/Nintu (Mesopotamia), Prometheus (Greece), 女媧 (China), Obatala (Yoruba), Tāne/Hine-ahu-one (Māori), Napi (Blackfoot)
- Produces: 8-tradition comparison table + 4 structural analyses (earth-as-life-substance, breath/word as spirit-infusion, potter-as-craftsman-with-flawed-output, food-for-humans created with humans) + 結論 + 參考文獻. Must be listed in comparisons/README.md (CI orphan check)

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/indigenous-americas/comparisons/README.md`**
- [ ] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (append story to indigenous-americas `stories`; add Napi to `pantheon`+`gods`; add comparison to `comparisons`; `_stories` 7→8), `_state.json` (append `indigenous-americas` to `enrich_log`; `runs` 118→119), `cultures/indigenous-americas/README.md` (counts 21/19/16 → 22/20/17)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich indigenous-americas — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
