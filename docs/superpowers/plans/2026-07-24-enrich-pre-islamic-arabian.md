# Pre-Islamic Arabian Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich pre-islamic-arabian culture by adding 1 new god page, 1 new story page, and 1 new comparison page with scholarly content in Traditional Chinese.

**Architecture:** Content-driven enrichment following the AGENTS.md LLM deepening workflow. Each file follows the established template patterns found in the existing culture files. No code changes — pure content creation.

**Tech Stack:** Markdown files with YAML-compatible metadata, Traditional Chinese text, cross-cultural comparison tables.

## Global Constraints

- All content in Traditional Chinese with English names in parentheses
- Each page must contain ≥300 characters of substantive content
- Each page must include cross-cultural correspondences
- Each page must include `## 參考文獻` section with at least 1 citation
- Follow existing file naming conventions (Chinese or English names matching catalog)
- No template/placeholder content — all text must be real mythological scholarship

---

### Task 1: Create gods/Amur.md

**Files:**
- Create: `cultures/pre-islamic-arabian/gods/Amur.md`

**Rationale:** Amur (عمرو) is listed in `_catalog.json` pantheon as "Amur(男神)" but has no dedicated god page. This is the only catalogued deity without a file.

**Content requirements:**
- Header with culture and role
- Overview section: Amur as a male deity of the pre-Islamic Arabian pantheon, his name etymology (possibly related to "life" or "command"), tribal associations
- Mythological deeds: Amur's role in tribal mythology, any known rituals
- Cross-cultural correspondence table (Mesopotamian, Greek, Roman parallels)
- Related deities
- References section with source citations

- [ ] **Step 1: Write the god page**

```markdown
# Amur (عمرو) — 男神

- **文化：** 前伊斯蘭阿拉伯神話 (Pre-Islamic Arabian Mythology)
- **職掌：** [to be filled with accurate mythological content]

## 概述
[Amur overview content]

## 神話事蹟
[Mythological narratives]

## 跨文化對應
| 文化 | 對應神祇 | 關係說明 |
|------|---------|---------|

## 相關神祇
[Related deities]

## 參考文獻
[At least 1 citation]
```

- [ ] **Step 2: Verify content quality**
  - Check: ≥300 characters of body text
  - Check: Contains cross-cultural comparison
  - Check: Has references section with citation

- [ ] **Step 3: Commit**

```bash
git add cultures/pre-islamic-arabian/gods/Amur.md
git commit -m "mythos: enrich pre-islamic-arabian (add Amur god page)"
```

---

### Task 2: Create stories/阿拉特與金角羚羊.md

**Files:**
- Create: `cultures/pre-islamic-arabian/stories/阿拉特與金角羚羊.md`

**Rationale:** The catalog lists 8 stories; the stories/ directory has 13 files (some overlap). Adding a new narrative about Al-Lat's sacred animal associations enriches the story collection.

**Content requirements:**
- Story background: The sacred gazelle/antelope in Al-Lat worship
- Narrative: A tale connecting Al-Lat to the golden-horned gazelle of the Arabian desert
- Cross-cultural parallels: Sacred animal mythology across cultures
- References

- [ ] **Step 1: Write the story page**

```markdown
# 阿拉特與金角羚羊 (Al-Lat and the Golden-Horned Gazelle)

- **文化：** 前伊斯蘭阿拉伯神話 (Pre-Islamic Arabian Mythology)

## 故事背景
[Background content]

## 情節
[Narrative content]

## 跨文化平行
[Cross-cultural parallels]

## 相關主題
[Related themes]

## 參考文獻
[At least 1 citation]
```

- [ ] **Step 2: Verify content quality**
  - Check: ≥300 characters of body text
  - Check: Contains cross-cultural comparison
  - Check: Has references section with citation

- [ ] **Step 3: Commit**

```bash
git add cultures/pre-islamic-arabian/stories/阿拉特與金角羚羊.md
git commit -m "mythos: enrich pre-islamic-arabian (add Al-Lat gazelle story)"
```

---

### Task 3: Create comparisons/阿拉伯部落盟誓與跨文化神聖契約.md

**Files:**
- Create: `cultures/pre-islamic-arabian/comparisons/阿拉伯部落盟誓與跨文化神聖契約.md`

**Rationale:** The comparisons/ directory has 14 files. Adding a comparison of Arabian tribal oath/covenant (ʿahd/bayʿah) with other sacred covenant traditions enriches the cross-cultural analysis.

**Content requirements:**
- Comparison subjects: Arabian ʿahd/bayʿah vs Hebrew covenant, Greek oath rituals, Vedic契约
- Structural comparison table
- Functional analysis of sacred contracts
- References

- [ ] **Step 1: Write the comparison page**

```markdown
# 阿拉伯部落盟誓與跨文化神聖契約 (Arabian Tribal Oaths and Cross-Cultural Sacred Covenants)

- **文化：** 前伊斯蘭阿拉伯神話 → 跨文化比較

## 比較對象
[Comparison subjects]

## 概述
[Overview]

## 結構比較
[Comparison table]

## 功能對應分析
[Analysis]

## 參考文獻
[At least 1 citation]
```

- [ ] **Step 2: Verify content quality**
  - Check: ≥300 characters of body text
  - Check: Contains cross-cultural comparison
  - Check: Has references section with citation

- [ ] **Step 3: Commit**

```bash
git add cultures/pre-islamic-arabian/comparisons/阿拉伯部落盟誓與跨文化神聖契約.md
git commit -m "mythos: enrich pre-islamic-arabian (add tribal oath comparison)"
```

---

### Task 4: Final verification and push

- [ ] **Step 1: Verify all files exist**
  - Check: `cultures/pre-islamic-arabian/gods/Amur.md` exists
  - Check: `cultures/pre-islamic-arabian/stories/阿拉特與金角羚羊.md` exists
  - Check: `cultures/pre-islamic-arabian/comparisons/阿拉伯部落盟誓與跨文化神聖契約.md` exists

- [ ] **Step 2: Run any available lint/CI checks**
  - Check: `python regenerate_all.py` or similar if available
  - Verify no orphan files

- [ ] **Step 3: Final commit and push**

```bash
git add -A
git commit -m "mythos: enrich pre-islamic-arabian"
git push
```
