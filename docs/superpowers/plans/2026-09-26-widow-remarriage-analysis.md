# Widow Remarriage / Levirate Analysis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新增 `analyses/widow-remarriage-levirate-comparative.md`——一則跨文化「寡婦再婚／利未拉」母題的比較分析（繁體中文 3,000 字以上、含跨文化對照表、具體文本引文與學術參考文獻），登錄 `analysis-index.md` 與 `analyses/README.md`，同步統計，跑過 CI 差異檢查後以 `mythos: analysis widow-remarriage-levirate` 單一 commit 推送。

**Architecture:** 以「繼承權與生育權分離時的介面」為論旨，而非婦女史或婚姻制度史專題。取樣 9 個案例：希伯來 yib'am（申命記 25＋創世記 38）、伊斯蘭 al-ʿaliyya 禁令與姊妹婚交換、魯國「一生一及」與季隗拒絕、高句麗寡后、印加 coya 兄妹婚、草原 emengerlik、Nuer 幽靈婚對照、埃及守護繼承人、羅馬不改嫁法定貞節、北歐晨賦＋《尼雅爾薩迦》婚約清血債。結構分析提出三種解法（血脈延續型＝容器／貞節封存型＝封存／財產補償型＝權利主體）、申命記羞辱機制的對稱性、血脈不對稱、制度需要反面敘事（Ovid）、時間的三種管理。

**Tech Stack:** Markdown（繁體中文）、Python（`scripts/ci_checks.py`、`scripts/generate_stats.py`）、git。

## Global Constraints

- 正文 ≥3,000 字繁體中文（`AGENTS.md` 方式 C 要求 3,000–5,000 字；排程任務最低 500 字）。
- h1 開頭、標題層級不跳級、無空標題（`check_heading_hierarchy`）。
- 內部 `.md` 連結僅指向**已存在**檔案；連結目標不得含括號（MD_LINK 規則）。
- 結尾須有非空 `## 參考文獻`（`check_citations_in_file`）。
- 須登錄 `analysis-index.md` 與 `analyses/README.md`，否則 `check_orphan_analyses` 報 orphan error。
- 基線：`scripts/ci_checks.py` 既有 14 個 ERROR，本次不得新增。
- 不得呼叫 `question`：無人值守模式，直接執行。

---

## File Structure

- Create: `analyses/widow-remarriage-levirate-comparative.md` — 本次唯一新增的分析文章
- Create: `docs/superpowers/plans/2026-09-26-widow-remarriage-analysis.md` — 本計畫
- Modify: `analysis-index.md` — 標題 543→544、附加 `| 544 | widow-remarriage-levirate-comparative.md | … |`
- Modify: `analyses/README.md` — 依字母序插入英文條目
- Modify: `_state.json` — `analysis_log` 追加、`runs` 205→206（**必須沿用 `indent=1` 且檔末無換行**，否則產生全檔雜訊 diff）
- Regenerate: `README.md`（STATS 區塊＋篇數註記）、`stats/index.md`（`python3 scripts/generate_stats.py`）

## Task 1: 撰寫分析文章

**Files:**
- Create: `analyses/widow-remarriage-levirate-comparative.md`

**Interfaces:**
- Consumes（可連結目標，皆須存在）：`ghost-marriage-posthumous-unions-comparative.md`、`cursed-bloodlines-generational-curse-comparative.md`、`divine-incest-sibling-marriage-comparative.md`、`sacred-marriage-across-cultures.md`、`sacred-kingship-comparative.md`、`first-funeral-burial-rites-myths-comparative.md`、`ghosts-restless-dead-comparative.md`、`taboo-breaking-myths-comparative.md`、`blood-covenant-myths-comparative.md`；`../cultures/egyptian/stories/賽特與荷魯斯的王位之爭.md`、`../cultures/egyptian/gods/伊西斯.md`。
- Produces: h1「寡嫂繼承：…」、`## 一、引言`、`## 二、跨文化對照表`、`## 三、各文明的制度敘事`（`### 1.`–`### 9.`）、`## 四、結構分析`（5 節）、`## 五、從神話到制度`、`## 六、結論`、`## 參考文獻`。

- [x] **Step 1: 寫入文章**（繁中 ≥3,000 字，實測 8,176 CJK 字）

要點：對照表 9 列。希伯來段須寫出脫鞋、`nāqaʿ ʿal-pānāw`（向臉面吐唾）、`və-meʾtō tippeah ha-yārek`（大腿被打開），並指出**執行羞辱者是寡婦本人**；俄南段須連結 `被詛咒的血脈`。伊斯蘭段須寫 al-ʿaliyya、艾莎解釋 al-ʿulūla、「若娶須同時娶亡者之妹」的交換條件、《古蘭經》4:19。中國段須用**何休注**「父死子繼曰生，兄死弟繼曰及……是魯之常也」與公羊「魯一生一及」（莊公三十二年），並以《左傳》僖公二十三／二十四季隗「我二十五年矣，又如是而嫁，則就木焉」為核心。高句麗段附印加 coya 兄妹婚對照。埃及段為「對稱面」——寡婦守住繼承人而非被移交。羅馬段為 vacatio annua→biennis、60／50 歲門檻、caduca、dos／actio rei uxoriae。北歐段為 morgongåva＋改嫁即分割遺產＋克努特法系禁止強迫再婚；《尼雅爾薩迦》ch. 158 芙洛西以 Hildigunn 許配 Kári 作為血債清償。
結構分析五節：容器／封存／權利主體三分；羞辱的對稱性；血脈不對稱（俄南—猶大、al-ʿaliyya 交換條件）；制度需要反面（Ovid 鐵器時代「Husbands longed for the death of their wives, wives for the death of their husbands」，以及耶利米 2:22 生銹的鐵）；時間的三種管理（含日本舊民法 767／新民法 733 再婚禁止期間 2013 違憲、2016 改 100 日）。

- [x] **Step 2: 本地格式驗證**

Run: `python3 -c` 檢查 h1 開頭、U+FFFD 數量為 0、層級、`## 參考文獻` 非空、CJK 字數
Expected: 無 format error，U+FFFD = 0（撰寫過程曾出現 mojibake 與英文字串誤植，已逐項修回）

- [x] **Step 3: 確認所有內部連結目標存在**

Run: `python3 scripts/ci_checks.py 2>&1 | grep -i "widow-remarriage"`
Expected: 索引更新前僅出現 orphan analysis 一項，不得出現 broken link／heading／citation 錯誤

## Task 2: 索引登錄、統計同步與提交

**Files:** `analysis-index.md`、`analyses/README.md`、`_state.json`、`README.md`、`stats/index.md`

- [x] **Step 1: 登錄索引**

`analysis-index.md` 標題 543→544，附加第 544 列；`analyses/README.md` 依字母序插入 `Widow Remarriage Levirate Comparative`（位置在 `Wild Hunt Spectral Procession` 之前）。

- [x] **Step 2: 同步狀態與統計**

`_state.json` 以 `json.dumps(..., indent=1)` 改寫（`indent=2` 會造成全檔 241 行雜訊 diff）；`README.md` 篇數註記 543→544；執行 `python3 scripts/generate_stats.py` 重生成 `stats/index.md` 與 README STATS 區塊。

- [x] **Step 3: 執行 CI 並與基線比對**

Run: `python3 scripts/ci_checks.py`
Expected: `FAILED — 14 errors`（與基線相同），且錯誤清單中**不含** `widow-remarriage-levirate-comparative.md`

- [x] **Step 4: Commit + push**

Run: `git add -A && git commit -m "mythos: analysis widow-remarriage-levirate" && git push`
Expected: push 成功，回報主題與對照重點

## Self-Review

- [x] 全文無未驗證斷言——已捨棄未取得原文的冰島「娶遺孀清償血債」通說化敘述（改以《尼雅爾薩迦》ch. 158 實錄取代）、Maya 寡婦繼承、阿拉伯的兄弟代身
- [x] 修正兩處錯誤引用：`父死子繼、兄死弟及` **不是**公羊傳本文（係何休《解詁》注，原文作「魯一生一及」，見莊公三十二年）；季隗一段屬《左傳》**僖公二十三年**（非二十四年）
- [x] Ovid 引文照錄 Kline 譯本（University of Virginia 版），因原譯段落標註與通行行號不一致，改以「Book I 世代序列末尾」定位，不虛構行號
- [x] 聖訓編號標明「異本編號有差異」而非硬寫單一號碼
- [x] 參考文獻 20 筆以上且皆為可查證之原始文本或標準學術著作
- [x] 與既有分析分工清楚並含 11 條內部連結
- [x] CI 未新增錯誤
