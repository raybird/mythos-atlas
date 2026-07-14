# Mongolian Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Enrich Mongolian Mythology (the weakest culture at 31 pages) by adding new gods, stories, and comparisons pages with substantive content.

**Architecture:** Direct content creation using LLM knowledge of Mongolian/Tengriist mythology, with cross-cultural analysis connecting to Turkic, Siberian, Chinese, and Persian traditions.

**Tech Stack:** Markdown files following existing AGENTS.md conventions.

## Global Constraints
- All content in Traditional Chinese (繁體中文)
- Each page ≥ 300 words
- Must include cross-cultural parallels (跨文化對應)
- Must include 參考文獻/參考來源 section
- Follow existing file naming conventions (e.g., `DeityName.md` for gods)

## Current State
- Mongolian culture has: 12 gods, 10 stories, 9 comparisons = 31 pages total
- Weakest among all cultures (tied with incan/nubian/tibetan at ~32)
- Priority cultures (sumerian/mayan/persian/yoruba) already have 123-128 pages each

## Tasks

### Task 1: Add New God Pages (3 pages)

**Files:**
- Create: `cultures/mongolian/gods/Asuri.md`
- Create: `cultures/mongolian/gods/Daichi-Tengri-detailed.md` → rename to proper name
- Create: `cultures/mongolian/gods/Gazar-Eej.md`

Add 3 under-documented deities from Mongolian mythology.

### Task 2: Add New Story Pages (3 pages)

**Files:**
- Create: `cultures/mongolian/stories/征服四十四天.md`
- Create: `cultures/mongolian/stories/Erlik的審判.md`
- Create: `cultures/mongolian/stories/Burkhan山的誓言.md`

### Task 3: Add New Comparison Pages (3 pages)

**Files:**
- Create: `cultures/mongolian/comparisons/長生天與跨文化天神比較.md`
- Create: `cultures/mongolian/comparisons/薩滿教跨文化宇宙觀比較.md`
- Create: `cultures/mongolian/comparisons/狼圖騰與歐亞草原文化比較.md`

### Task 4: Update Catalog & Commit

- Update `_catalog.json` motifs/stories if needed
- `git add -A && git commit -m "mythos: enrich mongolian"`
- `git push`
