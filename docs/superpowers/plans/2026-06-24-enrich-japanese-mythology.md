# Japanese Mythology Enrichment — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich Japanese mythology from 10 pages to 22+ pages by adding 4 gods, 4 stories, and 4 comparisons (300+ trad. Chinese chars each).

**Architecture:** Add leaf pages under `cultures/japanese/gods/`, `stories/`, `comparisons/` following existing page patterns. Update respective README indexes.

**Tech Stack:** Markdown, Git

---

### Task 1: Add missing gods (4 pages)

**Files:**
- Create: `cultures/japanese/gods/伊邪那美.md`
- Create: `cultures/japanese/gods/天鈿女命.md`
- Create: `cultures/japanese/gods/瓊瓊杵尊.md`
- Create: `cultures/japanese/gods/建御雷神.md`
- Modify: `cultures/japanese/gods/README.md`

- [ ] **Create 伊邪那美 (Izanami) page** — death/creation goddess, Yomi ruler, 300+ chars with cross-cultural parallels (Persephone, Ereshkigal, Hel)
- [ ] **Create 天鈿女命 (Ame-no-Uzume) page** — dawn/dance goddess who lured Amaterasu out, 300+ chars with parallels to African trickster-dancers, Dionysian maenads
- [ ] **Create 瓊瓊杵尊 (Ninigi) page** — heavenly grandson, founder of imperial lineage, 300+ chars with parallels to culture heroes bringing civilization
- [ ] **Create 建御雷神 (Takemikazuchi) page** — thunder/lightning god, central in Kuni-yuzuri, 300+ chars with parallels to Thor, Indra, Zeus
- [ ] **Update gods/README.md** with the 4 new entries

### Task 2: Add missing stories (4 pages)

**Files:**
- Create: `cultures/japanese/stories/因幡之白兔.md`
- Create: `cultures/japanese/stories/國讓神話.md`
- Create: `cultures/japanese/stories/天孫降臨.md`
- Create: `cultures/japanese/stories/海幸彥山幸彥.md`
- Modify: `cultures/japanese/stories/README.md`

- [ ] **Create 因幡之白兔 story** — Hare of Inaba, Ōkuninushi's kindness rewarded, 300+ chars with parallels to trickster tales
- [ ] **Create 國讓神話 (Kuni-yuzuri) story** — land transfer from Ōkuninushi to Ninigi, 300+ chars with parallels to peaceful political transition myths
- [ ] **Create 天孫降臨 (Tenson Kōrin) story** — Ninigi's descent with three treasures, 300+ chars with parallels to divine kingship myths
- [ ] **Create 海幸彥山幸彥 (Umisachi-Yamasachi) story** — luck of sea vs mountain, 300+ chars with parallels to brothers' rivalry myths (Cain/Abel, Romulus/Remus)
- [ ] **Update stories/README.md** with 4 new entries

### Task 3: Add comparisons (4 pages)

**Files:**
- Create: `cultures/japanese/comparisons/太陽女神比較.md`
- Create: `cultures/japanese/comparisons/三神器跨文化.md`
- Create: `cultures/japanese/comparisons/暴風神混沌神.md`
- Create: `cultures/japanese/comparisons/國讓與王權神話.md`
- Modify: `cultures/japanese/comparisons/README.md`

- [ ] **Create 太陽女神比較** — Amaterasu vs Ra, Surya, Inti, Sol, 300+ chars with table
- [ ] **Create 三神器跨文化** — Three Sacred Treasures vs other regalia myths, 300+ chars
- [ ] **Create 暴風神混沌神** — Susanoo vs Loki, Set, Enlil, Rudra, 300+ chars with table
- [ ] **Create 國讓與王權神話** — Kuni-yuzuri vs other peaceful power transfer myths, 300+ chars
- [ ] **Update comparisons/README.md** with 4 new entries

### Task 4: Git commit & push

**Files:** All above

- [ ] **Stage and commit**: `git add -A && git commit -m "mythos: enrich japanese" && git push`

### Task 5: Report

- [ ] **Report** which content was added (tables by category)
