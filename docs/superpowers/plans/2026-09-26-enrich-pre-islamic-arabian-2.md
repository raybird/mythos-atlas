# Pre-Islamic Arabian Mythology Enrichment Plan (Round 2)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 深化前伊斯蘭阿拉伯神話（pre-islamic-arabian）——新增 gods/、stories/、comparisons/ 各一頁，每頁 ≥300 繁中字、含跨文化對應與參考文獻，完成「三同步」登錄後提交推送。

**Architecture:** 選題以「無重疊」為第一原則。本次複選後，pre-islamic-arabian 為全庫最薄弱：總頁數 65（gods 24／stories 20／comparisons 21，與 mongolian 並列最低）且內容深度 2,960 字元為 44 文化中**最低**。三主題經 grep 全庫確認為空白：

- gods/Jinn.md — 精靈 Jinn：本庫已兩篇 jinn 比較頁與兩篇詩靈故事頁，但**神祇層缺位**（gods/ 無 Jinn 頁），Jinn 為賈希利亞最具代表性的超自然族群。
- stories/iram-dhat-al-imad.md — 伊蘭柱城 Iram：《古蘭經》89:6-8 的「柱之城」僅存在於 catalog 文字描述，無故事頁；與既有示巴／所羅門頁不重疊。
- comparisons/flood-refuge-cave-origins-comparative.md — 洪水避難洞穴與岩洞起源：既有的 lost-continents、cannibalism、sacred-islands、evil-eye、origin-of-writing、flood-myths-geological-origins 等主題**均未觸及**「洞穴」母題（已逐項 grep 確認），為全庫真空母題。

**Tech Stack:** Markdown、Python 3（字數統計／CI 驗證）、Git（commit+push）。

## Global Constraints

- 每頁 ≥300 繁中字（`[\u4e00-\u9fff]` 計數）、單一 H1、標題層級不跳階、`## 參考文獻` 尾段非空。
- 跨文化對應需可稽核：阿拉伯側以原典（《古蘭經》、Ibn Hisham《聖傳》、al-Ṭabarī《歷史》、al-Masudi《黃金草原》、Ibn Qutayba《詩與詩人》）、學術專著（Encyclopaedia Iranica "Genie"、Encyclopaedia of Islam、Scofield 1982、Harunaga 2002）與考古報告（Charloux et al. 2024 PLOS One、Haupt & Binder 人像石碑）為據；他文明側用可指名文本（《古事記》、Florentine Codex、Proclus、ETC SL 1.4 等），不得憑空捏造文獻。
- CI 基準 = `scripts/citation_baseline.txt` + `/workspace/.ci_before.txt` 既有筆數，不得修復、不得新增。
- commit 訊息格式：`mythos: enrich pre-islamic-arabian`；完成後 `git push`。
- 三同步＋一：gods/stories/comparisons 子 README 登錄、文化 README 計數、_catalog.json、_state.json（runs 206→207）、根 README 文化列與 stats/index.md（generate_stats.py 產生）。
- 本任務為無人值守：不得呼叫 question，一律自動採用推薦選項。

---

### Task 1: 精靈 Jinn 神祇頁

- [ ] 建立 `cultures/pre-islamic-arabian/gods/Jinn.md`
- [ ] `gods/README.md` 登錄

### Task 2: 伊蘭柱城故事頁

- [ ] 建立 `cultures/pre-islamic-arabian/stories/iram-dhat-al-imad.md`
- [ ] `stories/README.md` 登錄

### Task 3: 洞穴母題跨文化比較頁

- [ ] 建立 `cultures/pre-islamic-arabian/comparisons/flood-refuge-cave-origins-comparative.md`
- [ ] `comparisons/README.md` 登錄

### Task 4: 同步與驗證

- [ ] 執行 `python3 scripts/generate_stats.py` 更新根 README／stats
- [ ] 執行 `python3 scripts/ci_checks.py --with-stats` 確認無新增錯誤
- [ ] 字數統計：每頁 `[\u4e00-\u9fff]` ≥300

### Task 5: 提交與推送

- [ ] `git add -A && git commit -m "mythos: enrich pre-islamic-arabian"` && `git push`
