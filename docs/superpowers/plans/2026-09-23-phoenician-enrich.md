# Phoenician Culture Enrichment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 深化目前在 44 文化中內容行數最少的腓尼基文化（66 頁、約 2,752 行），新增 gods / stories / comparisons 各 1 頁（每頁 ≥300 字繁中、含跨文化對應與參考來源），並同步索引與統計後 commit+push。

**Architecture:** 新增三頁以「婚育—命運女神」與「埃爾的醉酒神話」兩個迦南獨有母題為主軸：God 頁（科塔拉特 Kotharat）與 Comparisons 頁（婚育與命運女神跨文化比較）互為表裡；Story 頁（埃爾的醉宴，KTU 1.114）以烏加里特原文文獻為依據，呈現迦南至高神罕見的「人性化身體失控」敘事。三頁皆非既有 24 位神祇／20 則故事／20 篇比較之重複主題。

**Tech Stack:** Markdown（繁中）、JSON（`_catalog.json`）、Python 腳本（`scripts/generate_stats.py`、`scripts/ci_checks.py`）、git。

## Global Constraints

- 頁面每篇 ≥300 字繁體中文正文（不含標題與前綴 metadata）。
- 每頁須以 `#` 開頭作 h1，標題層級不得跳級，無空標題。
- 結尾必須有非空之 `## 參考文獻`／`## 參考來源` 區塊（CI citation checks）。
- 比較頁必須登錄於 `cultures/phoenician/comparisons/README.md`（CI orphan check）；並同步登錄 gods/stories README、文化 README、`index.md` 與 `_catalog.json`。
- 內文 `.md` 內部連結只能指向既有檔案，避免 broken-link error。
- 基線：`scripts/ci_checks.py` 目前 14 個既有 ERROR（與本次無關，參見 `/workspace/.ci_before.txt`），新增頁面不得提高此數字。
- 不得呼叫 `question`／使用者確認：無人值守模式，直接執行。

---

## File Structure

- Create: `cultures/phoenician/gods/Kotharat.md` — 科塔拉特（七位婚宴與分娩守護女神）
- Create: `cultures/phoenician/stories/el-banquet.md` — 埃爾的醉宴（KTU 1.114）
- Create: `cultures/phoenician/comparisons/fates-birth-goddesses-comparative.md` — 婚育與命運女神跨文化比較
- Create: `docs/superpowers/plans/2026-09-23-phoenician-enrich.md` — 本計劃
- Modify: `_catalog.json`（phoenician 條目：`stories`+1、`_stories` 7→8、`gods`+1、`comparisons`+1）
- Modify: `cultures/phoenician/README.md`（24→25 神祇、20→21 故事、20→21 比較）
- Modify: `cultures/phoenician/index.md`（重要故事 +1）
- Modify: `cultures/phoenician/gods/README.md`、`stories/README.md`、`comparisons/README.md`（各 +1 列）
- Regenerate: `README.md`（STATS 區塊）、`stats/index.md`、`stats/radar/*.svg` — 由 `generate_stats.py` 產生

## Task 1: 新增神祇頁 `gods/Kotharat.md`

**Files:**
- Create: `cultures/phoenician/gods/Kotharat.md`

**Interfaces:**
- Consumes: 既有 `gods/科薩爾.md`、`gods/埃爾.md`、`gods/妮卡爾.md` 可作為內文連結目標。
- Produces: 檔案名 `Kotharat.md`；h1「科塔拉特 (Kotharat)」；節：`## 概述`、`## 神話事蹟`、`## 跨文化對應`、`## 相關神祇`、`## 出現在`、`## 參考文獻`。

- [ ] **Step 1: 撰寫頁面主體**

內容要點：詞根 kṯr 與工匠神科薩爾同源；七位集團、「新月之女」(bn hll) 之稱號；KTU 1.24（妮卡爾與月神雅里赫婚禮，科塔拉特祝歌祈福）與 KTU 1.15（克雷特史詩七日婚宴中降臨祝福得子）之情節；儀式泥板中作為產育護衛的集團；跨文化對應表（埃及七哈托爾／希臘厄勒堤亞與摩伊賴／北歐諾恩／斯拉夫羅扎尼采／波羅的海萊瑪／中國註生娘娘系／美索不達米亞舒塔什魯與瑪米圖）；結尾 `## 參考文獻` 引用 Wyatt 1998、Pardee 2002、Smith 2001、DDD。

- [ ] **Step 2: 驗證**

Run: `python3 scripts/ci_checks.py`
Expected: phoenician Kotharat.md 不在 14 個既有 ERROR 之列（無格式／文獻錯誤）。

- [ ] **Step 3: Commit（與其餘任務合併為單一 enrich commit）**

## Task 2: 新增故事頁 `stories/el-banquet.md`

**Files:**
- Create: `cultures/phoenician/stories/el-banquet.md`

**Interfaces:**
- Produces: 檔案名 `el-banquet.md`；h1「埃爾的醉宴 (El's Drunken Banquet)」；節：`## 故事背景`、`## 情節`（### 第一幕…）、`## 跨文化平行`、`## 參考文獻`。

- [ ] **Step 1: 撰寫頁面主體**

內容要點：KTU 1.114（=RS 24.258）醫療—儀式文本，至高神埃爾於其山中居所宴飲至醉倒嘔吐，眾神尋醫，由荷龍（Horon）行驅邪淨化之術救回；學者視為治療「仆倒／昏厥」儀式的神話病因；與聖經挪亞醉酒（創 9:20-27，迦南受咒詛）形成最直接近東平行；並列塞克邁特血酒、狄俄尼索斯、因陀羅蘇摩酒、北歐眾神酒宴、中國儀狄杜康傳說。該文本為近東罕見直接描寫至高神身體失控的段落。`## 參考文獻`：KTU 1.114、Wyatt 1998、Smith 1994、Pardee 2002、DDD s.v. El、創世記 9。

- [ ] **Step 2: 驗證**（同上，無新增 ERROR）

## Task 3: 新增比較頁 `comparisons/fates-birth-goddesses-comparative.md`

**Files:**
- Create: `cultures/phoenician/comparisons/fates-birth-goddesses-comparative.md`
- Modify: `cultures/phoenician/comparisons/README.md`（新增資料表列，否則 orphan error）

**Interfaces:**
- Produces: 檔案名 `fates-birth-goddesses-comparative.md`；h1「婚育與命運女神跨文化比較」；節：`## 比較：從接生到裁命`（內含 `### 對照表`，7 文化 × 面向）、`## 結構比較分析`（### 1. / ### 2. / ### 3.）、`## 跨文化延伸`、`## 參考文獻`。

- [ ] **Step 1: 撰寫頁面主體**

對照表文化：迦南科塔拉特／埃及七哈托爾／希臘厄勒堤亞與摩伊賴／北歐諾恩／斯拉夫羅扎尼采／波羅的海萊瑪與卡爾塔／中國註生娘娘與月老。分析三大結構：(1) 出生／婚姻之「閾限時間」裁命；(2) 媒介分異——迦南用歌聲、希臘用紡錘、北歐以潑水與編織、中國以紅線簿籍；(3) 從接生護衛到執掌命運之神話演化譜系；並以科塔拉特—科薩爾同詞根說明「工藝＝編織命運」的隱喻。`## 參考文獻` 含烏加里特文本、Hesiod/Snorri 原始文獻、Gimbutas 1971、Pinch 1994、CAD、《三教搜神大全》與《續玄怪錄·定婚店》等。

- [ ] **Step 2: 同步 `comparisons/README.md`**：新增資料表列 `| [fates-birth-goddesses-comparative](fates-birth-goddesses-comparative.md) | 婚育與命運女神跨文化比較 |`

- [ ] **Step 3: 驗證**（無新增 ERROR）

## Task 4: 同步索引與 catalog

**Files:**
- Modify: `_catalog.json`、`cultures/phoenician/README.md`、`cultures/phoenician/index.md`、`cultures/phoenician/gods/README.md`、`cultures/phoenician/stories/README.md`

- [ ] **Step 1: `_catalog.json`**：phoenician 條目 `stories` 列表新增「埃爾的醉宴（KTU 1.114，眾神之父的醉酒與療愈）」；`_stories` 7→8；`gods` 列表新增「科塔拉特（Kotharat，婚宴與分娩守護女神）」；`comparisons` 列表新增「婚育與命運女神跨文化比較」。
- [ ] **Step 2: `cultures/phoenician/README.md`**：24→25 位神祇／20→21 則故事／20→21 篇比較。
- [ ] **Step 3: `index.md`**：`## 重要故事` 新增一行「- 埃爾的醉宴（KTU 1.114）」。
- [ ] **Step 4: 子目錄 README**：gods/stories 各 +1 列，格式 `| [slug](slug.md) | 中文名 |`（依 README 現有排序）。

## Task 5: 統計與 CI 驗證

- [ ] Run: `python3 scripts/generate_stats.py`（更新 README STATS 區塊、stats/index.md、SVG）
- [ ] Run: `python3 scripts/ci_checks.py 2>&1 | grep -E "\[(ERROR|WARN)\]" | wc -l`
  Expected: 14（與基線一致，0 新增）
- [ ] Commit: `git add -A && git commit -m "mythos: enrich phoenician (科塔拉特婚育女神/埃爾的醉宴/婚育與命運女神跨文化比較)"`
- [ ] Push: `git push origin master`

## Self-Review

1. **Spec 覆蓋**：三頁主題（科塔拉特／埃爾醉宴／婚育命運女神比較）皆與既有 24/20/20 頁不重疊 ✓；每頁 ≥300 字並含跨文化對應與參考來源 ✓；索引、catalog、README、統計同步 ✓；commit/push 格式「mythos: enrich phoenician」✓。
2. **Placeholder 掃描**：本計劃不含 TBD/TODO，所有產出物皆以具體檔案與內容要點規範 ✓。
3. **型別一致**：三檔名（Kotharat.md / el-banquet.md / fates-birth-goddesses-comparative.md）與 README/catalog 登錄名稱一致；CI 所要求的 `## 參考文獻` 區塊在三頁中皆存在且非空 ✓；內部連結目標均為既有或本次新建之檔案 ✓。