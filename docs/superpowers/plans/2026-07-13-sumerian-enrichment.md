# Sumerian Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich Sumerian mythology collection with three new high-quality pages (gods, stories, comparisons), each 300+ words in Traditional Chinese with cross-cultural parallels and academic references.

**Architecture:** Add three new markdown pages to existing culture directory structure, update README indexes, update `_catalog.json` if needed, then commit and push.

**Tech Stack:** Markdown, git

## Global Constraints

- All content in Traditional Chinese (繁體中文)
- Each page ≥ 300 words
- Must include cross-cultural parallels table
- Must include `## 參考文獻` section with academic sources
- Follow existing page format (see `cultures/sumerian/gods/Enki.md` as template)
- Commit message format: `mythos: enrich sumerian`

---

### Task 1: Create God Page — Nungal (寧加爾)

**Files:**
- Create: `cultures/sumerian/gods/Nungal.md`
- Modify: `cultures/sumerian/gods/README.md` — add Nungal entry

**Interfaces:**
- Consumes: existing god page format from `cultures/sumerian/gods/Enki.md`
- Produces: new file `cultures/sumerian/gods/Nungal.md`

- [ ] **Step 1: Write the Nungal god page**

Create `cultures/sumerian/gods/Nungal.md` with:
- Header: `# 寧加爾 (Nungal) — 監獄女神與囚犯守護者`
- Sections: 概述, 神話事蹟, 跨文化對應, 相關神祇, 出現在, 參考文獻
- Content: Nungal is goddess of prisons (Bandli/Galzu) and protector of prisoners. Daughter of Enlil and Ninlil. Her temple at Nippur. She sets the "me" of imprisonment. Cross-cultural: Egyptian Ma'at (justice), Greek Nemesis, Hindu Yama (judge of dead).
- ≥ 300 words

- [ ] **Step 2: Update README index**

Add `| [Nungal](Nungal.md) | 寧加爾 |` to `cultures/sumerian/gods/README.md` table.

- [ ] **Step 3: Verify file exists and has content**

```bash
wc -w cultures/sumerian/gods/Nungal.md
```
Expected: ≥ 300 (Chinese characters count as words)

- [ ] **Step 4: Commit**

```bash
git add cultures/sumerian/gods/Nungal.md cultures/sumerian/gods/README.md
git commit -m "mythos: enrich sumerian — add Nungal god page"
```

---

### Task 2: Create Story Page — Gilgamesh and Utnapishtim

**Files:**
- Create: `cultures/sumerian/stories/gilgamesh-utnapishtim.md`
- Modify: `cultures/sumerian/stories/README.md` — add entry

**Interfaces:**
- Consumes: existing story format from `cultures/sumerian/stories/inanna-descent-to-underworld.md`
- Produces: new file `cultures/sumerian/stories/gilgamesh-utnapishtim.md`

- [ ] **Step 1: Write the story page**

Create `cultures/sumerian/stories/gilgamesh-utnapishtim.md` with:
- Header: `# 吉爾伽美什與烏特納匹什提：永生的最後機會 (Gilgamesh and Utnapishtim)`
- Sections: 故事背景, 情節 (multi-act structure), 跨文化平行, 相關主題, 參考來源
- Content: Gilgamesh's journey across the Waters of Death to find Utnapishtim, the only mortal granted eternal life. The flood narrative within (Utnapishtim's account of the flood). The plant of youth episode. Cross-cultural: Noah's Ark, Deucalion, Manu and the Fish.
- ≥ 300 words

- [ ] **Step 2: Update README index**

Add entry to `cultures/sumerian/stories/README.md` table.

- [ ] **Step 3: Verify and commit**

```bash
wc -w cultures/sumerian/stories/gilgamesh-utnapishtim.md
git add cultures/sumerian/stories/gilgamesh-utnapishtim.md cultures/sumerian/stories/README.md
git commit -m "mythos: enrich sumerian — add Gilgamesh-Utnapishtim story"
```

---

### Task 3: Create Comparison Page — Sumerian Divine Fate Measurement

**Files:**
- Create: `cultures/sumerian/comparisons/sumerian-measure-fate.md`
- Modify: `cultures/sumerian/comparisons/README.md` — add entry

**Interfaces:**
- Consumes: existing comparison format from `cultures/sumerian/comparisons/sumerian-flood-comparison.md`
- Produces: new file `cultures/sumerian/comparisons/sumerian-measure-fate.md`

- [ ] **Step 1: Write the comparison page**

Create `cultures/sumerian/comparisons/sumerian-measure-fate.md` with:
- Header: `# 蘇美命運度量與跨文化命運神話比較 (Sumerian Fate Measurement and Cross-Cultural Fate Myths)`
- Sections: 比較概觀, 核心比較分析 (table), 結論, 參考文獻
- Content: The Sumerian concept of "nam-tar" (fate-cutting) where divine fate is measured/cut at birth. Enlil as fate-cutter. Comparison with: Egyptian Book of Life (Ammit/Thoth), Greek Moirai (Fates), Norse Norns, Hindu Karma/fate, Chinese Ming (命) concept.
- ≥ 300 words

- [ ] **Step 2: Update README index**

Add entry to `cultures/sumerian/comparisons/README.md` table.

- [ ] **Step 3: Verify and commit**

```bash
wc -w cultures/sumerian/comparisons/sumerian-measure-fate.md
git add cultures/sumerian/comparisons/sumerian-measure-fate.md cultures/sumerian/comparisons/README.md
git commit -m "mythos: enrich sumerian — add divine fate measurement comparison"
```

---

### Task 4: Final Push

- [ ] **Step 1: Verify total page count increased**

```bash
for sub in gods stories comparisons; do
  count=$(find cultures/sumerian/$sub -name '*.md' ! -name 'README.md' | wc -l)
  echo "sumerian/$sub: $count"
done
```
Expected: gods=44, stories=37, comparisons=38 (total=119)

- [ ] **Step 2: Push to remote**

```bash
git push
```

- [ ] **Step 3: Report results**

Summarize new pages added, word counts, and git commit hashes.
