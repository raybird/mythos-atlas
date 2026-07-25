# Persian Mythology Enrichment Plan (2026-07-25)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 3 new comparison pages to Persian mythology, each ≥300 Traditional Chinese characters with cross-cultural references and citations.

**Architecture:** Direct content creation using LLM knowledge, following existing file format conventions in `cultures/persian/comparisons/`.

**Tech Stack:** Markdown files, git

## Global Constraints

- All content in Traditional Chinese with English names in parentheses
- Each page must include `## 參考來源` section with at least 1 citation
- Follow existing file naming and formatting conventions from `cultures/persian/comparisons/`
- Minimum 300 characters per page
- No `populate.py` usage

## Analysis

Among priority cultures (sumerian=164, mayan=148, persian=145, yoruba=146), **Persian** has the fewest total pages (145). The existing content is substantive and scholarly. Three genuine gaps identified in the comparisons/ directory:

1. No Zurvanism/cyclical time comparison page (Zurvan.md exists as god, but no cross-cultural comparison)
2. No Persian-Islamic eschatology comparison (persian-abrahamic-influence.md exists but focuses on Abrahamic broadly, not specifically Islamic afterlife)
3. No Zoroastrian dream/prophecy comparison page

---

### Task 1: Create Comparison — Zurvanism與永恆時間觀

**Files:**
- Create: `cultures/persian/comparisons/zurvanism-eternal-time.md`

### Task 2: Create Comparison — 瑣羅亞斯德教與伊斯蘭教來世觀

**Files:**
- Create: `cultures/persian/comparisons/persian-islamic-eschatology.md`

### Task 3: Create Comparison — 瑣羅亞斯德教的夢境與預言

**Files:**
- Create: `cultures/persian/comparisons/zoroastrian-dreams-prophecy.md`

### Task 4: Commit and Push

```bash
cd /workspace/projects/mythos-atlas
git add -A
git commit -m "mythos: enrich persian"
git push
```
