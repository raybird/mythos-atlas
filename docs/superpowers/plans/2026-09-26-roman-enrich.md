# Roman Enrichment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 深化羅馬神話（roman）——新增 gods/、stories/、comparisons/ 各一頁，每頁 ≥300 繁中字、含跨文化對應與參考文獻，並完成「三同步」登錄後提交推送。

**Architecture:** 選題以「無重疊」為第一原則：先對 analyses/ 與 cultures/ 全庫 grep 主題關鍵字，確認三主題皆為空白後書寫。新頁格式沿用既有 roman 頁慣例（單一 H1、情境段落、跨文化對應表格或條列、`## 參考文獻` 尾段）。完成後同步 catalog／_state／子 README／根 README 統計，最後跑 CI 確認維持 14 筆既有基準、新檔零命中。

**Tech Stack:** Python 3（字數統計、CI 驗證）、Git（commit+push）、Markdown。

## Global Constraints

- 每頁 ≥300 繁中字（'[\u4e00-\u9fff]' 計數）、單一 H1、含 `## 參考文獻`（尾段非空）。
- 跨文化對應需可稽核：優先使用原典（Ovid、Livy、Valerius Maximus、《史記》《莊子》、《撒母耳記上》……），不得憑空捏造文獻。
- CI 基準 = 14 筆既有錯誤（/workspace/.ci_before.txt），不得修復；新檔關鍵字命中須為 0。
- commit 訊息格式：`mythos: enrich <culture-name>`；完成後 `git push`。
- 三同步：子 README 登錄、_catalog.json（roman gods/stories/comparisons +1）、_state.json（enrich_log +'roman'、runs 204→205）、根 README roman 文化列＝實際檔數 (27,21,20)。
- 本任務為無人值守：不得呼叫 question，一律自動採用推薦選項。

---