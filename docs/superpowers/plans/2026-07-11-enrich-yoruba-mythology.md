# Yoruba Mythology Enrichment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich Yoruba mythology by adding 3 new substantive pages (god, story, comparison) and enriching 3 existing thin pages, each with 300+ chars Traditional Chinese, cross-cultural parallels, and academic references.

**Architecture:** Each file lives under `cultures/yoruba/{gods,stories,comparisons}/`. Files follow AGENTS.md templates. All content in Traditional Chinese. New pages follow the god/story/comparison templates from AGENTS.md. Existing pages expanded from ~35-50 lines to 60+ lines.

**Tech Stack:** Markdown, Mythos Atlas conventions per AGENTS.md

---

**Context:** Yoruba has 108 total pages (38 gods + 35 stories + 35 comparisons), all thin at 32-52 lines. After Persian enrichment (fb14ccd), Yoruba is next priority. Existing pages have good structure but lack depth — most contain only 1-2 myth cycles and limited analysis.

---

### Task 1: Create gods/ose.md — Ọṣẹ, the Goddess of Fertility and Divination

**Files:**
- Create: `cultures/yoruba/gods/ose.md`

- [ ] **Write the content**

Content covering:
- Ọṣẹ (also Ọṣẹ̀) as a lesser-known but significant Orisha of fertility, divination, and freshwater
- Her role as one of the wives of Ṣàngó, associated with rivers and rain
- Connection to Ifá divination through Ọ̀ṣẹ́ Odù (one of the 256 Odù)
- The Ọṣẹ festival — purification rituals at rivers, offerings of ebo (sacrifice)
- Cross-cultural parallels: Greek Hera (fertility + river association), Hindu Ganga (sacred river goddess), Japanese Benzaiten (water + fertility), Egyptian Satis (cataract goddess)
- References: Ifá Odù corpus (Odù Ọṣẹ), Bascom 1969, Abiodun 2014

---

### Task 2: Create stories/oya-shango-separation.md — Ọya's Separation from Ṣàngó

**Files:**
- Create: `cultures/yoruba/stories/oya-shango-separation.md`

- [ ] **Write the content**

Content covering:
- The dramatic story of Ọya's departure from Ṣàngó's palace
- Ọya discovering Ṣàngó's infidelity with Oṣun and Ọba
- Her transformation into a water buffalo, destroying the palace walls
- The mythological explanation for the Ọya River's turbulent currents
- Thematic significance: female autonomy, the untameable nature of storm and change
- Cross-cultural parallels: Sita's exile (Hindu Ramayana), Ariadne abandoned by Theseus (Greek), Inanna's descent to underworld (Sumerian), Brünnhilde's separation from Siegfried (Norse)
- References: Ifá oral tradition, Gleason 1987, Johnson 1921

---

### Task 3: Create comparisons/underworld-gatekeepers.md — Guardians of the Underworld Cross-Cultural

**Files:**
- Create: `cultures/yoruba/comparisons/underworld-gatekeepers.md`

- [ ] **Write the content**

Content covering:
- Ọya as guardian of the gates between living and dead in Yoruba cosmology
- Comparison table of underworld gatekeepers across civilizations:
  - Yoruba: Ọya (storm goddess guards the gate)
  - Greek: Cerberus (three-headed dog) + Charon (ferryman) + Hades/Persephone
  - Egyptian: Anubis (jackal-headed, weighs the heart)
  - Mesopotamian: Neti (gates of Kur) + Ereshkigal (queen of underworld)
  - Norse: Hel (half-living half-dead ruler) + Garmr (blood-stained dog)
  - Hindu: Yama (death judge) + Chitragupta (record keeper)
  - Chinese: 閻羅王 (Yama) + 牛頭馬面 (ox-head and horse-face guardians)
  - Japanese: Emma-Ō (閻魔王) + Shikime (十鬼姬, ten demon princesses)
- Analysis: unique Yoruba feature — the gatekeeper is a powerful goddess (not a dog, servant, or male judge), reflecting gendered cosmology
- References: Eliade 1964, Leeming 2010, Awolalu 1979, Bundahishn

---

### Task 4: Enrich gods/obatala.md — Expand Obatala's Page

**Files:**
- Modify: `cultures/yoruba/gods/obatala.md`

- [ ] **Expand existing content**

Current content is ~44 lines. Expand to 65+ lines by adding:
- Detailed account of the Obatala醉酒 (drunkenness) myth — the creation of people with disabilities and Obatala's subsequent role as protector of disabled people
- The 16 children of Oduduwa and Obatala's rivalry narrative
- Obatala's association with craftsmanship and sculpture (the "divine sculptor")
- Additional cross-cultural parallels: Hephaestus (Greek, divine craftsman with disability), Ptah (Egyptian, creator-god of craftsmen), Vishwakarma (Hindu, divine architect)
- Additional references: Thompson 1983, Abiodun 2014

---

### Task 5: Enrich stories/obatala-creates-humans.md — Expand Creation Story

**Files:**
- Modify: `cultures/yoruba/stories/obatala-creates-humans.md`

- [ ] **Expand existing content**

Current content is ~36 lines. Expand to 60+ lines by adding:
- The detailed process of Obatala's creation: the golden chain, the white chicken, the snail shell of white sand
- The drunkenness episode — why Obatala drank palm wine, what happened to the humans he shaped
- Olodumare's correction — the divine mandate for Obatala to protect disabled people
- The theological meaning: imperfection as sacred, not cursed
- Cross-cultural parallels: Prometheus's stolen fire (Greek), Ptah's heart-and-tongue creation (Egyptian), the Golem (Jewish)
- References: Ifá Odù, Idowu 1962, Awolalu 1979

---

### Task 6: Enrich comparisons/high-gods.md — Expand High God Comparison

**Files:**
- Modify: `cultures/yoruba/comparisons/high-gods.md`

- [ ] **Expand existing content**

Current content is ~52 lines. Expand to 70+ lines by adding:
- The "Deus Otiosus" (退隱至高神) concept — Olodumare's non-intervention pattern
- Detailed comparison table with 8+ civilizations
- Analysis of why Yoruba theology developed the delegated authority model (Olodumare → Orishas → humans)
- The philosophical implications: free will, divine distance, intermediary theology
- Cross-cultural parallels: Brahman (Hindu), Tetragrammaton (Judaism), Tao (Chinese), Ahura Mazda (Zoroastrian)
- References: Idowu 1962, Eliade 1959, Campbell 1949

---

### Task 7: Update README Indexes

**Files:**
- Modify: `cultures/yoruba/gods/README.md`
- Modify: `cultures/yoruba/stories/README.md`
- Modify: `cultures/yoruba/comparisons/README.md`

- [ ] **Update gods/README.md** — Add `ose.md` entry
- [ ] **Update stories/README.md** — Add `oya-shango-separation.md` entry
- [ ] **Update comparisons/README.md** — Add `underworld-gatekeepers.md` entry

---

### Task 8: Git Commit and Push

- [ ] `git add -A && git commit -m "mythos: enrich yoruba" && git push`
