# Divine Wrestling Analysis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新增 `analyses/divine-wrestling-myths-comparative.md`——一則跨文化「與神／不可勝者角力」母題的比較分析（繁體中文 3,000 字以上、含跨文化對照表、具體文本引文與學術參考文獻），登錄 `analysis-index.md`，跑過 CI 差異檢查後以 `mythos: analysis divine-wrestling` 單一 commit 推送。

**Architecture:** 以「角力＝宇宙秩序的最小裁定程序」為論旨，而非體育史或競技節慶專題。取樣 9 個案例：雅各 vs 神（創 32）、佩琉斯 vs 忒提斯、赫拉克勒斯 vs 阿刻洛俄斯／塔那托斯、婆薮 vs 婆薩那、佛陀 vs 魔羅、索爾 vs 老年、武甕槌 vs 天宇受賣、毛伊 vs 太陽。結構分析提出三種可勝對手的分類（可變形者／不可變形的抽象／不可握持的循環力量）與「破曉時限」母題，並與既有分析（神聖競技、神判、神話試煉、套日）明確分工、互相連結。

**Tech Stack:** Markdown（繁體中文）、Python（`scripts/ci_checks.py`）、git。

## Global Constraints

- 正文 ≥3,000 字繁體中文（`AGENTS.md` 方式 C 要求 3,000–5,000 字；排程任務最低 500 字）。
- h1 開頭、標題層級不跳級、無空標題（`check_heading_hierarchy`）。
- 內部 `.md` 連結僅指向**已存在**檔案；連結目標不得含括號（MD_LINK 規則）。
- 結尾須有非空 `## 參考文獻`（`check_citations_in_file`）。
- 須登錄 `analysis-index.md` 之表格行，否則 `check_orphan_analyses` 報 orphan error。
- 基線：`scripts/ci_checks.py` 既有 14 個 ERROR（`/workspace/.ci_before.txt`），本次不得新增。
- 不得呼叫 `question`：無人值守模式，直接執行。
- Commit 刻意維持單一（文章＋索引＋本計畫），以符合排程指定的 commit message。

---

## File Structure

- Create: `analyses/divine-wrestling-myths-comparative.md` — 本次唯一新增的分析文章
- Create: `docs/superpowers/plans/2026-09-26-divine-wrestling-analysis.md` — 本計畫
- Modify: `analysis-index.md` — 標題 542→543、依字母序插入 `| 543 | divine-wrestling-myths-comparative.md | … |`

## Task 1: 撰寫分析文章

**Files:**
- Create: `analyses/divine-wrestling-myths-comparative.md`

**Interfaces:**
- Consumes（可連結目標，皆須存在）：`sacred-games-athletic-contests-comparative.md`、`trial-by-ordeal-divine-judgement-comparative.md`、`divine-tests-trials-of-mortals.md`、`sun-snaring-myths-comparative.md`、`ritual-combat-sacred-warfare-comparative.md`、`master-of-animals-comparative.md`；`../cultures/japanese/gods/建御名方神.md`、`../cultures/norse/stories/索爾的烏特迦洛奇之旅.md`。
- Produces: h1「與神摔跤：…」、`## 一、引言`、`## 二、跨文化對照表`、`## 三、各文明的角力敘事`（`### 1.`–`### 8.`）、`## 四、結構分析`、`## 五、從神話到制度`、`## 六、結論`、`## 參考文獻`。

- [ ] **Step 1: 寫入文章**（繁中 ≥3,000 字）

要點：對照表 9 列（角力者／對手／文本／勝負與代價／象徵結構）；雅各段落須寫出「直到破曉」與大腿筋縮短、名字改為以色列；希臘段落須區分「握持變形者」（忒提斯變形、卡帕提斯教以繩索捆綁、Ovid *Met.* 11）與「神力分解」（阿刻洛俄斯變蛇與牛、戰神阿瑞斯被繳械、塔那托斯暫緩）；婆薮段須點出 Karna 授予的「密技」使技術隱匿性成為情節張力；佛陀段須說明文本以「明白魔羅＝欲與死」收束、圖像（觸地印、軍隊消散）才是角力版本；索爾段須精確寫成「雙方皆無法摔倒對方」；日本段須並列建御名方 vs 建御雷神與武甕槌 vs 天宇受賣兩版，指出角力被指派為讓國的裁判程序；毛伊段連結既有套日分析並強調「壓制／按住」而非擊敗。
結構分析四節：破曉的時限、命名與傷痕的記帳、可勝對手三分類、裁判權作為繼承程序。最後以「雅各得名字與跛腳、索爾只學到界限」對稱收束。

- [ ] **Step 2: 本地格式驗證**

Run: `python3 -c` 檢查 h1 開頭、層級、`## 參考文獻` 非空、字數
Expected: 無 format error，正文 CJK 字數 ≥3,000

- [ ] **Step 3: 確認所有內部連結目標存在**

Run: `python3 scripts/ci_checks.py 2>&1 | grep -i "divine-wrestling"`
Expected: 此時僅出現 orphan analysis 一項（索引尚未更新，Task 2 修復），不得出現 broken link／heading／citation 錯誤

## Task 2: 索引登錄、CI 差異檢查與提交

**Files:**
- Modify: `analysis-index.md`

- [ ] **Step 1: 登錄索引**

標題 `# 已分析母題索引（542 篇）` 改為 543；於 `divine-*` 字母序位置插入 `| 543 | divine-wrestling-myths-comparative.md | 與神摔跤：跨文化神話中「凡人與神明角力」母題的比較分析 |`

- [ ] **Step 2: 執行 CI 並與基線比對**

Run: `python3 scripts/ci_checks.py`
Expected: `FAILED — 14 errors`（與 `/workspace/.ci_before.txt` 相同），且錯誤清單中**不含** `divine-wrestling-myths-comparative.md`

- [ ] **Step 3: Commit + push**

Run: `git add -A && git commit -m "mythos: analysis divine-wrestling" && git push`
Expected: push 成功，回報主題與對照重點

## Self-Review

- [ ] 全文無未驗證斷言（已捨棄 Ardashir–Ahriman 摔角與《古今和歌集》神代相撲歌，因未取得可靠原文）
- [ ] 參考文獻 10 筆以上且皆為可查證之原始文本或標準學術著作
- [ ] 與既有分析分工清楚並至少 6 條內部連結
- [ ] CI 未新增錯誤
