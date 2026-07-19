# Sumerian Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 3 new substantive pages to the Sumerian mythology section — one god, one story, one cross-cultural comparison — each ≥300 Traditional Chinese characters with academic references.

**Architecture:** Create 3 new markdown files in the existing `cultures/sumerian/` directory structure, following established conventions observed in existing files (Baba.md, adapa-legend.md, dying-and-rising-deities.md).

**Tech Stack:** Markdown, Traditional Chinese, academic mythological sources

## Global Constraints

- Each page ≥ 300 Traditional Chinese characters
- Must include cross-cultural correspondences (table or structured list)
- Must include ≥ 3 academic reference sources per page
- Follow existing file naming conventions (kebab-case)
- Language: 繁體中文 with English names in parentheses
- Do NOT use `populate.py` — all content must be written from LLM knowledge

## File Structure

- Create: `cultures/sumerian/gods/Gula.md`
- Create: `cultures/sumerian/stories/journey-of-nanna-to-nippur.md`
- Create: `cultures/sumerian/comparisons/sumerian-vedic-cosmogony.md`

---

### Task 1: Create Gula god page

**Files:**
- Create: `cultures/sumerian/gods/Gula.md`

**Interfaces:**
- Consumes: None (standalone page)
- Produces: New god page following existing format (Baba.md as template)

**Content:** Gula (古拉) — Sumerian/Akkadian healing goddess. She evolved from earlier Sumerian deities Baba/Bau and Nintinugga. Cover: her origin and syncretism with Baba, her role as patron of medicine and veterinary healing, her temples (E-gal-ma), her consort Ninurta/Ningirsu, her sacred dogs, her appearance in medical incantation texts. Cross-cultural parallels: with Egyptian Sakhmet/Bastet (lion/healing), Greek Hygieia/Asclepius, Hindu Dhanvantari. Include comparison table.

- [ ] **Step 1: Create the Gula god page**

Write `cultures/sumerian/gods/Gula.md` with content following the structure of `cultures/sumerian/gods/Baba.md`:
- Title, culture, role
- 概述 section (syncretism history, role in pantheon)
- 神話事蹟 section (medical texts, temple inscriptions, mythology)
- 跨文化對應 table (at least 5 correspondences)
- 相關神祇 section
- 出現在 section (which texts)
- 參考文獻 section (≥3 references)

- [ ] **Step 2: Verify file content**

Read the created file and verify it is ≥300 Chinese characters, has cross-cultural table, and has references.

- [ ] **Step 3: Commit**

```bash
git add cultures/sumerian/gods/Gula.md
git commit -m "mythos: add Gula healing goddess page to Sumerian mythology"
```

---

### Task 2: Create Journey of Nanna to Nippur story page

**Files:**
- Create: `cultures/sumerian/stories/journey-of-nanna-to-nippur.md`

**Interfaces:**
- Consumes: None (standalone page)
- Produces: New story page following existing format (adapa-legend.md as template)

**Content:** "Nanna's Journey to Nippur" (南那赴尼普爾) — A Sumerian courtship/visitation poem where the moon god Nanna (Sin) travels from Ur to Nippur to court the goddess Inanna and seek the approval of her father Enlil. Cover: the literary structure (travel narrative + courtship), the historical context (Ur III period, royal hymns), the mythological significance (divine marriage, cosmic order). Cross-cultural parallels: with Sumerian "Marriage of Martu" (different tone), Greek myth of Zeus visiting other deities, Indian Kama's courtship narratives. Include comparison of courtship journey motifs across cultures.

- [ ] **Step 1: Create the story page**

Write `cultures/sumerian/stories/journey-of-nanna-to-nippur.md` with content following the structure of `cultures/sumerian/stories/adapa-legend.md`:
- Title, culture, genre
- 故事背景 section (literary context, historical period)
- 情節 section (multi-part narrative of the journey and courtship)
- 跨文化平行 section (structured parallels with other cultures)
- 參考文獻 section (≥3 references)

- [ ] **Step 2: Verify file content**

Read the created file and verify it is ≥300 Chinese characters, has cross-cultural parallels, and has references.

- [ ] **Step 3: Commit**

```bash
git add cultures/sumerian/stories/journey-of-nanna-to-nippur.md
git commit -m "mythos: add Journey of Nanna story to Sumerian mythology"
```

---

### Task 3: Create Sumerian-Vedic Cosmogony comparison page

**Files:**
- Create: `cultures/sumerian/comparisons/sumerian-vedic-cosmogony.md`

**Interfaces:**
- Consumes: None (standalone page)
- Produces: New comparison page following existing format (dying-and-rising-deities.md as template)

**Content:** Compare Sumerian and Vedic (Hindu) creation cosmogonies. Key parallels: both begin with primordial waters (Nammu / Apas), both feature a cosmic separation of heaven and earth (An-Ki / Dyaus-Prithivi), both use a "cosmic egg" or "primordial mound" motif, both describe creation through divine speech or sacrifice. Include detailed comparison table covering: primordial state, separation act, creation mechanism, first beings, cosmic mountain (Ekur / Meru). Discuss scholarly debates (Indo-European vs. Sumerian substrate theories). Cross-cultural parallels: also bring in Egyptian Nun/primordial mound and Chinese Hundun/Pangu.

- [ ] **Step 1: Create the comparison page**

Write `cultures/sumerian/comparisons/sumerian-vedic-cosmogony.md` with content following the structure of `cultures/sumerian/comparisons/dying-and-rising-deities.md`:
- Title, overview
- 跨文化比較表 (detailed comparison table with at least 4 rows covering different cosmogonic elements)
- 結構分析 section (analyzing parallel structures and divergences)
- 學術爭論 section (scholarly perspectives on these parallels)
- 參考文獻 section (≥3 references)

- [ ] **Step 2: Verify file content**

Read the created file and verify it is ≥300 Chinese characters, has comparison table, and has references.

- [ ] **Step 3: Commit**

```bash
git add cultures/sumerian/comparisons/sumerian-vedic-cosmogony.md
git commit -m "mythos: add Sumerian-Vedic cosmogony comparison to Sumerian mythology"
```

---

### Task 4: Final commit and push

- [ ] **Step 1: Stage all remaining files and push**

```bash
git add -A && git commit -m "mythos: enrich sumerian" && git push
```
