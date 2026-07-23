# Mythos Atlas — Persian Culture Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 3 new scholarly pages to Persian mythology: 1 god page, 1 story page, 1 comparison page, each ≥300 Traditional Chinese characters with cross-cultural references and citations.

**Architecture:** Direct content creation using LLM knowledge, following existing file format conventions observed in the Persian culture directory.

**Tech Stack:** Markdown files, git

## Global Constraints

- All content in Traditional Chinese with English names in parentheses
- Each page must include `## 參考來源` section with at least 1 citation
- Follow existing file naming and formatting conventions from `cultures/persian/`
- Minimum 300 characters per page
- No `populate.py` usage

---

### Task 1: Create God Page — Vivanhan (Vivanghant)

**Files:**
- Create: `cultures/persian/gods/Vivanhan.md`

**Context:** Vivanghant (Avestan: Vivanhant) is the Avestan dawn deity and father of Yima (Jamshid). He is mentioned in the Avesta as a solar figure associated with the first light. This deity does not yet have a dedicated page.

### Task 2: Create Story Page — Kay Kavus's Flight to Heaven

**Files:**
- Create: `cultures/persian/stories/kay-kavus-demons.md`

**Context:** One of the most fantastical episodes in the Shahnameh: King Kay Kavus ties demons to his throne and attempts to fly to heaven. He is struck down by the simurgh. This famous story is not yet covered in the stories directory.

### Task 3: Create Comparison Page — Persian-Mesoamerican Dualism

**Files:**
- Create: `cultures/persian/comparisons/persian-mesoamerican-dualism.md`

**Context:** Comparing Zoroastrian Ahura Mazda vs Angra Mainyu with Mesoamerican cosmic polarity (Quetzalcoatl vs Tezcatlipoca). This cross-cultural comparison does not exist yet.

### Task 4: Commit and Push

```bash
cd /workspace/projects/mythos-atlas
git add -A
git commit -m "mythos: enrich persian"
git push
```
