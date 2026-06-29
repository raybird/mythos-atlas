# Persian Mythology Enrichment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich Persian (Zoroastrian) mythology by adding three substantive pages (god, story, comparison) with cross-cultural parallels and references.

**Architecture:** Each file lives under `cultures/persian/{gods,stories,comparisons}/`. Files follow the AGENTS.md templates for god pages, story pages, and comparison articles. All content in Traditional Chinese, 300+ chars each.

**Tech Stack:** Markdown, Mythos Atlas conventions per AGENTS.md

---

**Context:** Mayan already enriched (48 pages). Persian is the weakest priority culture (46 pages: 16 gods + 15 stories + 15 comparisons).

---

### Task 1: Create gods/Vayu.md — Vāyu, the Wind/Space God

**Files:**
- Create: `cultures/persian/gods/Vayu.md`

- [ ] **Write the content**

Content covering:
- Vāyu/Vāta as wind and atmosphere god in Zoroastrian cosmology
- Dual nature — associated with both Spenta Mainyu (Holy Spirit) and Angra Mainyu (Destructive Spirit)
- Role in the Chinvat Bridge judgment (aid to the righteous)
- Cross-cultural parallels: Hindu Vāyu, Egyptian Shu, Greek Anemoi, Chinese Feng Bo, Aztec Ehecatl
- References: Avesta (Yasht 15 dedicated to Vayu), Bundahishn

---

### Task 2: Create stories/rostam-seven-labors.md — The Seven Labors of Rostam

**Files:**
- Create: `cultures/persian/stories/rostam-seven-labors.md`

- [ ] **Write the content**

Content covering:
- Haft Khān-e Rostam (Rostam's Seven Labors) from Ferdowsi's Shahnameh
- Each labor: (1) slay the lion, (2) cross the desert, (3) slay the dragon, (4) kill the witch, (5) capture the bandit, (6) fight the Div (demon) Arzhang, (7) defeat the Div-e Sepid
- Key themes: perseverance, divine favor (xvarenah), the hero's journey
- Cross-cultural parallels: Heracles' Labors (Greek), Gilgamesh/Enkidu (Mesopotamian), Arjuna's trials (Hindu), Cú Chulainn (Celtic)
- References: Shahnameh (Ferdowsi), Campbell's Hero with a Thousand Faces

---

### Task 3: Create comparisons/amesha-spenta-cross-culture.md — Amesha Spentas Cross-Cultural

**Files:**
- Create: `cultures/persian/comparisons/amesha-spenta-cross-culture.md`

- [ ] **Write the content**

Content covering:
- The six Amesha Spentas (Holy Immortals): Vohu Manah (Good Mind), Asha Vahishta (Truth), Khshathra Vairya (Desirable Dominion), Spenta Armaiti (Holy Devotion), Haurvatat (Wholeness), Ameretat (Immortality)
- Seven-fold deity structure with Ahura Mazda
- Cross-cultural comparison table:
  - Hindu Adityas (Varuna, Mitra, Aryaman, etc.)
  - Christian Archangel hierarchy
  - Buddhist Bodhisattva perfections (pāramitās)
  - Greek: the six Olympians + Zeus
  - Egyptian: Ogdoad of Hermopolis
  - Neoplatonic emanations
- References: Avesta (Yasna 38-42), Bundahishn, Plato's Timaeus

---

### Task 4: Git Commit and Push

- [ ] `git add -A && git commit -m "mythos: enrich persian" && git push`
