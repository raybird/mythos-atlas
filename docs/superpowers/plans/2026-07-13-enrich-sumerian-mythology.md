# Sumerian Mythology Enrichment Plan (Phase 2)

> **Goal:** Add 3 new pages to Sumerian mythology (1 god, 1 story, 1 comparison), each 300+ Traditional Chinese characters with cross-cultural parallels and academic references.

**Architecture:** Three new content files following established format conventions. Sumerian chosen as enrichment target: highest documentary base (116 existing pages) but only 116 vs yoruba's 117 — still room for significant expansion.

**Tech Stack:** Markdown, Git

## Global Constraints

- All content in Traditional Chinese (繁體中文)
- Each page minimum 300 characters (actual target: 600+ for depth)
- Cross-cultural correspondence table or analysis section
- Academic references with specific editions
- Follow format patterns from existing enriched pages (Teshub.md, inanna-enki-theft-of-me.md, sumerian-flood-comparison.md)

---

### Task 1: Create Utu god page

**Files:**
- Create: `cultures/sumerian/gods/Utu.md`

**Content:**
- Utu (Akkadian: Shamash): sun god, god of justice and truth
- Daily journey across sky in chariot, nightly journey through underworld
- Brother of Inanna, son of Nanna/Sin
- Role in Gilgamesh Epic (witness, helper)
- Cross-cultural parallels: Ra (Egyptian), Helios (Greek), Surya (Vedic), Sol (Norse)

- [ ] Write Utu.md

### Task 2: Create Lament for Ur story page

**Files:**
- Create: `cultures/sumerian/stories/lament-for-ur.md`

**Content:**
- "Lamentation over the Destruction of Ur" (~2000 BCE)
- Historical context: fall of Third Dynasty of Ur to Elamites and Isin
- Structure: gods decree destruction, city personified as weeping goddess
- Cross-cultural parallels: Book of Lamentations (Hebrew), Lament for Nineveh (Jonah), Siege of Troy lament

- [ ] Write lament-for-ur.md

### Task 3: Create underworld comparison page

**Files:**
- Create: `cultures/sumerian/comparisons/sumerian-underworld-comparison.md`

**Content:**
- Sumerian Kur vs Egyptian Duat vs Greek Hades
- Underworld geography, ferryman, judgment of dead
- Inanna's Descent parallel to Orpheus/Izanagi
- Table comparing underworld structures
- Academic references

- [ ] Write sumerian-underworld-comparison.md

### Task 4: Commit and push

- [ ] `git add -A && git commit -m "mythos: enrich sumerian" && git push`
