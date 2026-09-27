# 會說話的遺物（物件作證）跨文化分析文章 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `analyses/` 新增一篇繁體中文跨文化比較分析，主題為「無生命物體留下物證並自行發聲控訴」，涵蓋古希臘、日耳曼／北歐民歌、日本、中國、希伯來與北美原住民六組傳統。

**Architecture:** 純內容型變更——新增一個 Markdown 分析檔，並同步兩個索引檔（`analyses/README.md` 字母序條目、`analysis-index.md` 編號表列）。無程式邏輯、無資料庫遷移。驗證依靠既有的 `scripts/ci_checks.py`（格式、孤兒頁、引用檢查）與三個 enrichment 契約測試。

**Tech Stack:** Markdown（CommonMark）、Python 3.11（CI 檢查腳本）、Git。

## Global Constraints

- 語言：繁體中文；外文專名以括號標註（例：格林童話《會唱歌的骨頭》(Der singende Knochen)）。
- 每條事實必須引用原始文獻或口傳傳統來源，標註章節／行號。
- 跨文化平行需以 `↔` 連接對應關係（見 `/workspace/projects/mythos-atlas/AGENTS.md`）。
- 禁止簡體字。
- 不得使用 `populate.py` 產生內容。
- 既有 `analyses/bones-mythology-comparative.md` 已涵蓋骨作為創世／占卜／重生素材；本篇只做「物件作證與自我發聲」，不得重複該文範圍。
- `analyses/README.md` 與 `analysis-index.md` 必須同步，否則 CI 會報 orphan。
- Git 訊息格式：`mythos: analysis <topic> — <中文副題>`。

---

## File Structure

| 檔案 | 動作 | 責任 |
|------|------|------|
| `analyses/speaking-relics-object-testimony-comparative.md` | 新增 | 唯一內容來源：摘要、對照總表、六則個案、結構分析、參考文獻 |
| `analyses/README.md` | 修改（+1 行） | 字母序索引條目 |
| `analysis-index.md` | 修改（+2 行） | 標題計數 `（546 篇）`→`（548 篇）` 與編號 548 的表列 |
| `docs/superpowers/plans/2026-09-27-speaking-relic-object-testimony-analysis.md` | 新增 | 本計畫（隨 commit 一起入庫，與 `2026-09-26-widow-remarriage-analysis.md` 同例） |

`analyses/README.md` 標示為 auto-generated，但 `2026-09-26` 的三次新分析 commit（`7ce48b94`、`4dc09680`、`61253c8a`）皆以手動插入一行維護，**不要**執行 `regenerate_all.py`，否則會重排整份索引。

---

## Task 1: 建立計畫檔

- [ ] 寫入本計畫檔（已完成）
- [ ] 確認計畫檔不破壞 CI：`docs/` 已在 `ci_checks.py` 的 `EXCLUDED_TOP_DIRS` 中

## Task 2: 撰寫分析文章

- [ ] 建立 `analyses/speaking-relics-object-testimony-comparative.md`
- [ ] 結構：H1 中文標題 → H2 英文副標 → `### 摘要` → `### 跨文化對照總表` → `### 一、`…`### 六、` → `### 結構分析` → `### 參考文獻`（`#### 原始文獻` / `#### 研究與工具書` / `#### 延伸閱讀（本專案既有分析）`）
- [ ] 六則個案逐一落實（含可查證的章節／行號）：

| # | 傳統 | 核心物證 | 出處 |
|---|------|---------|------|
| 1 | 古希臘 | 佩羅普斯肩胛骨被投入海中、逆流回捲繞船；撈起後答應神諭「以爾後裔償還」 | Pausanias 5.10.6；Aeschylus *Agamemnon* 復元片段 104–105 |
| 2 | 古希臘 | 提恩德亞立石流汗洩露波呂丟刻斯被殺 | Apollodorus 1.9.7；Hyginus *Fabulae* 97 |
| 3 | 日耳曼／北歐民歌 | 被害姊妹遺骨製成豎琴，琴自奏並以死者聲音告發凶手 | Grimm KHM 28《會唱歌的骨頭》；Ballad Index「Twa Sisters／Binnorie」 |
| 4 | 日本 | 夜泣石夜啼，磨刀石撞痕反推凶手 | 鳥山石燕《今昔百鬼拾遺》〈小夜の中山〉 |
| 5 | 中國 | 甲骨灼裂為神答；沉香木為血緣信物、山腹回聲傳母訊 | 《甲骨文合集》；《沉香寶卷》 |
| 6 | 希伯來 | 土地本身喊出兇手 | 《創世記》4:10；`go'el ha-dam` 贖血者 |
| 7 | 北極圈原住民 | 馴鹿肩胛骨裂紋為尋路之答 | Innu / Naskapi scapulimancy |

- [ ] 對照總表欄位：`類型 | 文化／文本 | 案例 | 物證如何指認凶手 | 超自然機制`
- [ ] 結尾「延伸閱讀」只連到 `analyses/` 下**確實存在**的檔案（執行 `ls` 驗證後再寫）

## Task 3: 同步索引

- [ ] `analyses/README.md`：在 `Soul Concepts Comparative` 與 `Sphinx Comparative` 之間（字母序）插入一行
- [ ] `analysis-index.md`：標題計數改為 `（548 篇）`；表格末尾追加 `| 548 | speaking-relics-object-testimony-comparative.md | … |`

## Task 4: 驗證

- [ ] `python3 scripts/ci_checks.py` → 須為 `ALL CHECKS PASSED`
- [ ] `python3 scripts/test_egyptian_enrichment.py` → PASS
- [ ] `python3 scripts/test_phoenician_enrichment.py` → PASS
- [ ] `python3 scripts/test_inuit_enrichment.py` → PASS
- [ ] `wc -c analyses/speaking-relics-object-testimony-comparative.md` → 應 > 8,000 字元（遠高於 500 字下限）
- [ ] `grep -c '↔' analyses/speaking-relics-object-testimony-comparative.md` → 應 > 0
- [ ] 簡體字掃描：`grep -oP '[\x{4e00}-\x{9fff}]' file | grep -f <簡體集>` → 人工複核
- [ ] 手動檢查每條 `延伸閱讀` 連結目標存在：`for f in $(grep -oP '\]\(\K[^)]+' file); do test -e analyses/$f || echo MISSING $f; done`

## Task 5: Commit 與 push

- [ ] `git add -A`
- [ ] `git commit -m "mythos: analysis speaking-relics-object-testimony — 會說話的遺骸：物件作證跨文化比較"`
- [ ] `git push`
- [ ] 回報使用者：主題、六組傳統、對照總表歸納的三種機制、commit hash

---

## 風險與退路

- **ctext.org 與 zh.wikisource 抓取被封鎖**（《列子·湯問》櫾木條文無法取得）→ 不引用該條；中國案例改以甲骨文獻與《沉香寶卷》為準。
- **RSC PDF 404、Perseus 逾時**（Euripides *Helen* 1086–89 原文未取得）→ 不使用該處；希臘案例改以 Pausanias 與 Apollodorus 為主，Aeschylus 僅用康妥（Conington）英譯本殘句。
- **若某個案無法取得可查證出處，直接刪除該列**，不得以「據傳」「民間說法」含糊帶過——`AGENTS.md` 明令禁止空殼內容。
