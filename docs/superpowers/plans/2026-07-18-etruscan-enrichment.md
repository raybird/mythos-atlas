# Etruscan Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the Etruscan (伊特魯里亞) mythology culture in Mythos Atlas by adding new gods, stories, and comparisons pages — each at least 300 Traditional Chinese characters with cross-cultural parallels and cited sources.

**Architecture:** Etruscan mythology currently has 37 pages (13 gods, 11 stories, 10 comparisons). While the content quality is good, the volume is the lowest among all cultures. This plan adds 3 new gods, 3 new stories, and 3 new comparisons to bring it to 46 total pages, filling gaps in under-documented deities and narratives.

**Tech Stack:** Markdown files, git, shell commands.

## Global Constraints

- Each page must be ≥300 Traditional Chinese characters
- Each page must include `## 參考文獻` or `## 參考來源` section with at least 1 citation
- Use the AGENTS.md god/story/comparison template formats
- Filenames: lowercase with hyphens for English names, or Chinese characters matching existing conventions
- All content must be real mythological scholarship, not template filler

---

## File Structure

### New Gods (3 files)
- Create: `cultures/etruscan/gods/Sethlans.md` — Fire/god of forge (under-documented)
- Create: `cultures/etruscan/gods/Nortia.md` — Goddess of fate/turning the nail
- Create: `cultures/etruscan/gods/Ani.md` — God of winds/breath

### New Stories (3 files)
- Create: `cultures/etruscan/stories/the-judgment-of-morta.md` — Morta and the fate of souls
- Create: `cultures/etruscan/stories/the-lymphoma-oracle.md` — Origin of haruspicy from Tages
- Create: `cultures/etruscan/stories/the-founding-of-cortona.md` — Mythological founding of Cortona

### New Comparisons (3 files)
- Create: `cultures/etruscan/comparisons/etruscan-fire-deities-comparative.md` — Sethlans vs Hephaestus vs Vulcan vs Agni
- Create: `cultures/etruscan/comparisons/etruscan-fate-goddesses-comparative.md` — Nortia vs Moirai vs Norns
- Create: `cultures/etruscan/comparisons/etruscan-divination-cross-cultural.md` — Haruspicy vs Chinese oracle vs Greek manteia

---

### Task 1: Create gods/Sethlans.md

**Files:**
- Create: `cultures/etruscan/gods/Sethlans.md`

**Interfaces:**
- Consumes: Etruscan mythological data from `_catalog.json`
- Produces: A new god page following the template in AGENTS.md

- [ ] **Step 1: Write Sethlans god page**

Create the file with content covering Sethlans (火神/鍛造神), the Etruscan equivalent of Greek Hephaestus and Roman Vulcan. Include:
- God attributes: fire, forge, metalwork, volcanism
- Mythological narratives: creation of divine weapons, association with Mt. Vulcano
- Cross-cultural parallels: Hephaestus, Vulcan, Hindu Agni, Chinese Zhurong (祝融)
- Sources: de Grummond 2006, Turfa 2013, Bonfante & Bonfante 2003

- [ ] **Step 2: Verify file meets 300-char minimum**

Run: `wc -m cultures/etruscan/gods/Sethlans.md`
Expected: ≥500 characters (300+ Chinese content plus formatting)

- [ ] **Step 3: Commit**

```bash
git add cultures/etruscan/gods/Sethlans.md
git commit -m "mythos: enrich etruscan - add Sethlans god page"
```

---

### Task 2: Create gods/Nortia.md

**Files:**
- Create: `cultures/etruscan/gods/Nortia.md`

**Interfaces:**
- Consumes: Etruscan mythological data
- Produces: A new god page

- [ ] **Step 1: Write Nortia god page**

Create the file covering Nortia (命運女神), goddess of fate who turns the nail (clavus) marking the passage of years. Include:
- God attributes: fate, time, the nail ritual
- Mythological narratives: the nail-driving ritual in the temple of Jupiter Optimus Maximus
- Cross-cultural parallels: Greek Moirai, Norse Norns, Roman Fortuna
- Sources: Livy, Plutarch, de Grummond 2006

- [ ] **Step 2: Verify file meets 300-char minimum**

Run: `wc -m cultures/etruscan/gods/Nortia.md`
Expected: ≥500 characters

- [ ] **Step 3: Commit**

```bash
git add cultures/etruscan/gods/Nortia.md
git commit -m "mythos: enrich etruscan - add Nortia god page"
```

---

### Task 3: Create gods/Ani.md

**Files:**
- Create: `cultures/etruscan/gods/Ani.md`

**Interfaces:**
- Consumes: Etruscan mythological data
- Produces: A new god page

- [ ] **Step 1: Write Ani god page**

Create the file covering Ani (風神), god of winds and breath in Etruscan cosmology. Include:
- God attributes: wind, breath, air, spirit
- Mythological narratives: role in the six-day creation, winds as divine messengers
- Cross-cultural parallels: Greek Aeolus/Boreas, Roman Aeolus, Norse Véar, Vedic Vayu
- Sources: Varro (via Augustine), Martianus Capella, Bonfante 1986

- [ ] **Step 2: Verify file meets 300-char minimum**

Run: `wc -m cultures/etruscan/gods/Ani.md`
Expected: ≥500 characters

- [ ] **Step 3: Commit**

```bash
git add cultures/etruscan/gods/Ani.md
git commit -m "mythos: enrich etruscan - add Ani wind god page"
```

---

### Task 4: Create stories/the-judgment-of-morta.md

**Files:**
- Create: `cultures/etruscan/stories/the-judgment-of-morta.md`

**Interfaces:**
- Consumes: Etruscan eschatological data
- Produces: A new story page

- [ ] **Step 1: Write the Judgment of Morta story**

Create the file covering the Etruscan afterlife judgment narrative. Include:
- Story background: Etruscan beliefs about the soul's journey after death
- Plot: the soul crossing the underworld, facing judgment by Aita and Phersipnai
- Cross-cultural parallels: Egyptian weighing of the heart, Greek Minos judgment, Zoroastrian Chinvat Bridge
- Sources: Etruscan tomb paintings (Tomb of the Augurs, Tomb of the Leopards), Pallottino 1952

- [ ] **Step 2: Verify file meets 300-char minimum**

Run: `wc -m cultures/etruscan/stories/the-judgment-of-morta.md`
Expected: ≥500 characters

- [ ] **Step 3: Commit**

```bash
git add cultures/etruscan/stories/the-judgment-of-morta.md
git commit -m "mythos: enrich etruscan - add Judgment of Morta story"
```

---

### Task 5: Create stories/the-lymphoma-oracle.md

**Files:**
- Create: `cultures/etruscan/stories/the-lymphoma-oracle.md`

**Interfaces:**
- Consumes: Etruscan divinatory origin myths
- Produces: A new story page

- [ ] **Step 1: Write the origin of haruspicy story**

Create the file covering how Tages emerged from a plowed field and taught Etruscans divination. Include:
- Story background: the Etrusca Disciplina and its divine origin
- Plot: Tages (a child-deity) rising from the earth at Tarquinia, teaching augury to the first Etruscans
- Cross-cultural parallels: Chinese oracle bone divination origins, Greek Delphic oracle, Vedic divination rituals
- Sources: Ovid Fasti, Livy, Virgil Aeneid Book 8, Turfa 2013

- [ ] **Step 2: Verify file meets 300-char minimum**

Run: `wc -m cultures/etruscan/stories/the-lymphoma-oracle.md`
Expected: ≥500 characters

- [ ] **Step 3: Commit**

```bash
git add cultures/etruscan/stories/the-lymphoma-oracle.md
git commit -m "mythos: enrich etruscan - add Tages oracle origin story"
```

---

### Task 6: Create stories/the-founding-of-cortona.md

**Files:**
- Create: `cultures/etruscan/stories/the-founding-of-cortona.md`

**Interfaces:**
- Consumes: Etruscan city-foundation myths
- Produces: A new story page

- [ ] **Step 1: Write the founding of Cortona story**

Create the file covering the mythological founding of Cortona, one of the oldest Etruscan cities. Include:
- Story background: Cortona's legendary origin and its connection to the Etruscan hero-god
- Plot: the divine decree of city boundaries, the founding ritual, connection to the saecula system
- Cross-cultural parallels: Roman founding of Rome (Romulus), Greek founding myths, Chinese Yu the Great founding settlements
- Sources: Dionysius of Halicarnassus, Plutarch, Etruscan inscriptions

- [ ] **Step 2: Verify file meets 300-char minimum**

Run: `wc -m cultures/etruscan/stories/the-founding-of-cortona.md`
Expected: ≥500 characters

- [ ] **Step 3: Commit**

```bash
git add cultures/etruscan/stories/the-founding-of-cortona.md
git commit -m "mythos: enrich etruscan - add founding of Cortona story"
```

---

### Task 7: Create comparisons/etruscan-fire-deities-comparative.md

**Files:**
- Create: `cultures/etruscan/comparisons/etruscan-fire-deities-comparative.md`

**Interfaces:**
- Consumes: Cross-cultural fire deity data
- Produces: A new comparison page

- [ ] **Step 1: Write fire deities comparison**

Create the file comparing Sethlans (Etruscan) with Hephaestus (Greek), Vulcan (Roman), Agni (Vedic), Zhurong (Chinese), and Ptah (Egyptian). Include:
- Comparison table of attributes
- Analysis of forge-fire vs sacrificial-fire vs cosmic-fire
- References to specific myths and rituals
- Sources: Eliade 1958, Dumézil 1973, de Grummond 2006

- [ ] **Step 2: Verify file meets 300-char minimum**

Run: `wc -m cultures/etruscan/comparisons/etruscan-fire-deities-comparative.md`
Expected: ≥500 characters

- [ ] **Step 3: Commit**

```bash
git add cultures/etruscan/comparisons/etruscan-fire-deities-comparative.md
git commit -m "mythos: enrich etruscan - add fire deities comparison"
```

---

### Task 8: Create comparisons/etruscan-fate-goddesses-comparative.md

**Files:**
- Create: `cultures/etruscan/comparisons/etruscan-fate-goddesses-comparative.md`

**Interfaces:**
- Consumes: Cross-cultural fate goddess data
- Produces: A new comparison page

- [ ] **Step 1: Write fate goddesses comparison**

Create the file comparing Nortia (Etruscan) with Moirai (Greek), Norns (Norse), and Parcae (Roman). Include:
- Comparison table of attributes and domains
- Analysis of the nail-turning vs thread-spinning vs weaving metaphors
- Connection to saecula (world-age) system
- Sources: Turfa 2013, de Grummond 2006, Larrain 2003

- [ ] **Step 2: Verify file meets 300-char minimum**

Run: `wc -m cultures/etruscan/comparisons/etruscan-fate-goddesses-comparative.md`
Expected: ≥500 characters

- [ ] **Step 3: Commit**

```bash
git add cultures/etruscan/comparisons/etruscan-fate-goddesses-comparative.md
git commit -m "mythos: enrich etruscan - add fate goddesses comparison"
```

---

### Task 9: Create comparisons/etruscan-divination-cross-cultural.md

**Files:**
- Create: `cultures/etruscan/comparisons/etruscan-divination-cross-cultural.md`

**Interfaces:**
- Consumes: Cross-cultural divination data
- Produces: A new comparison page

- [ ] **Step 1: Write divination comparison**

Create the file comparing Etruscan haruspicy (liver divination) with Chinese oracle bone divination, Greek manteia, and Vedic sacrificial rituals. Include:
- Comparison table of methods, tools, and social roles
- Analysis of the liver as cosmic map vs turtle shell as cosmic map
- The concept of reading divine will from natural signs
- Sources: Pfiffig 1975, Turfa 2013, Keightley 1978, Heesterman 1993

- [ ] **Step 2: Verify file meets 300-char minimum**

Run: `wc -m cultures/etruscan/comparisons/etruscan-divination-cross-cultural.md`
Expected: ≥500 characters

- [ ] **Step 3: Commit**

```bash
git add cultures/etruscan/comparisons/etruscan-divination-cross-cultural.md
git commit -m "mythos: enrich etruscan - add cross-cultural divination comparison"
```

---

### Task 10: Update catalog and push

**Files:**
- Modify: `_catalog.json` (update etruscan story count if needed)

**Interfaces:**
- Consumes: All new files from Tasks 1-9
- Produces: Updated catalog, git push

- [ ] **Step 1: Update _catalog.json**

Update the etruscan entry in `_catalog.json` to reflect the new stories count (currently 11, will become 14 after adding 3 stories).

- [ ] **Step 2: Final commit and push**

```bash
git add -A
git commit -m "mythos: enrich etruscan - add 9 pages (3 gods, 3 stories, 3 comparisons)"
git push
```

- [ ] **Step 3: Report results**

Report what was added and confirm push succeeded.

---

## Self-Review

**1. Spec coverage:** 
- ✅ Target culture identified: etruscan (fewest pages at 37)
- ✅ 3 new gods pages: Sethlans, Nortia, Ani
- ✅ 3 new stories pages: Judgment of Morta, Tages oracle, Founding of Cortona
- ✅ 3 new comparisons pages: Fire deities, Fate goddesses, Cross-cultural divination
- ✅ Each page ≥300 Traditional Chinese characters
- ✅ Cross-cultural parallels included in every page
- ✅ Source citations included in every page
- ✅ Git commit and push at end

**2. Placeholder scan:** All tasks contain specific content descriptions with named entities, sources, and cross-cultural references. No TBD/TODO markers.

**3. Type consistency:** All pages follow the AGENTS.md template formats (god template with attributes/mythology/cross-cultural/related/sources, story template with background/plot/parallels/themes, comparison table format). File naming follows existing etruscan conventions.
