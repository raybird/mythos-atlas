# 韓國神話深化 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich Korean Mythology (korean/) by adding three new substantive pages — one god, one story, one cross-cultural comparison — each ≥300 characters in Traditional Chinese with cross-cultural correspondences and reference sources.

**Architecture:** Direct content creation using LLM knowledge, following existing file format conventions observed in the korean/ subdirectories. No code changes required.

**Tech Stack:** Markdown content files, Git

## Global Constraints

- All content in Traditional Chinese with English names in parentheses
- Each page must contain ≥300 characters of substantive content
- Must include cross-cultural correspondences (↔ pattern)
- Must cite at least one primary source or academic reference
- Follow existing file format (see korean/gods/桓因.md, korean/stories/檀君神話.md, korean/comparisons/韓國熊女神話跨文化比較.md)

---

### Task 1: Create God Page — 閻羅大王 (Yama)

**Files:**
- Create: `cultures/korean/gods/閻羅大王.md`

**Context:** 韓國神話目前收錄 14 位神祇，但缺少冥界審判者的角色。閻羅大王(염라대왕)是韓國佛教與民間信仰中最重要的冥界裁判者，源自印度 Yama，經中國閻羅王傳入韓半島，與本土巫俗的「死亡判官」觀念融合。

- [ ] **Step 1:** Create `cultures/korean/gods/閻羅大王.md` with ≥300 chars content
- [ ] **Step 2:** Verify file content quality

### Task 2: Create Story Page — 花郎道故事 (Hwarang Tales)

**Files:**
- Create: `cultures/korean/stories/花郎道故事.md`

**Context:** 韓國神話目前收錄 12 則故事，缺少新羅花郎道的神話性敘事。花郎(화랑)是新羅時期的貴族青年組織，其起源神話融合了戰士崇拜、自然精靈信仰與儒家忠義精神。

- [ ] **Step 1:** Create `cultures/korean/stories/花郎道故事.md` with ≥300 chars content
- [ ] **Step 2:** Verify file content quality

### Task 3: Create Comparison Page — 韓國龍神信仰與東亞龍崇拜跨文化比較

**Files:**
- Create: `cultures/korean/comparisons/韓國龍神信仰與東亞龍崇拜跨文化比較.md`

**Context:** 韓國神話目前有 11 篇比較文章，但缺少龍神崇拜的跨文化比較。韓國龍王信仰與中國龍王、日本龍神、印度那伽(Naga)之間存在密切的文化傳播關係。

- [ ] **Step 1:** Create `cultures/korean/comparisons/韓國龍神信仰與東亞龍崇拜跨文化比較.md` with ≥300 chars content
- [ ] **Step 2:** Verify file content quality

### Task 4: Git Commit and Push

- [ ] **Step 1:** `git add cultures/korean/`
- [ ] **Step 2:** `git commit -m "mythos: enrich korean"`
- [ ] **Step 3:** `git push`
