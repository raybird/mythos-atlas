# Mythos Atlas — 斯基泰文化深化（Scythian Enrichment）Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 為最薄弱文化 `scythian` 新增 2 個神祇／聖者頁、3 個故事頁、1 個跨文化比較頁（每頁 ≥300 字繁體中文、含跨文化對應與參考來源），並修正一處既有頁面的文本失準，最後同步索引與統計後 commit + push。

**Architecture:** 採「先立測試契約、再填內容」兩階段。新增 `scripts/test_scythian_enrichment.py`（鏡射 `test_celtic_enrichment.py`）作為紅燈測試，內容頁與子目錄 README 讓它轉綠；最後以 `scripts/ci_checks.py` ＋五支 enrichment 測試作為回歸閘門，再更新 `_catalog.json`、`_state.json`、`README.md` 統計。

**Tech Stack:** Markdown（繁體中文）、Python 3.11（無第三方相依）、Git。

---

## 為何選 scythian（選文依據，可重現）

`gods+stories+comparisons` 總頁數有 **12 個文化並列全庫最低 = 69 頁**：

```
aboriginal 69 | armenian 69 | dacian 69 | egyptian 69 | finno-ugric 69 |
hittite 69 | minoan 69 | nubian 69 | polynesian 69 | scythian 69 |
slavic 69 | vietnamese 69
```

平手時以「三層失衡度 + 來源基礎脆弱度」破平手，`scythian` 勝出：

1. **stories 層僅 20 頁**，是全庫並列最少的類別層（與 egyptian、dacian 並列）。
2. **來源基礎在全庫最窄**：44 個文化中，斯基泰的祭儀與神話幾乎全部只經由希羅多德《歷史》卷四單一載體流傳（Boileau 1980；Ustinova 1999）。任何未收錄的卷四章節都是「全庫獨有」的可見缺口，而非與其他文化重複的選項。
3. 卷四中數段高價值文本經核對後確認**確實尚未收錄**（見下表），可作實質增量。

## 已核對的缺口（逐條比對 `cultures/scythian/` 現有 69 頁）

| 卷四節次 | 內容 | 現況 |
|---|---|---|
| 4.46 | 希羅多德對整個黑海北岸的「愚昧」定調中，**唯獨開一個口子給 Anacharsis** | 缺 |
| 4.76–77 | Anacharsis 的系譜（Gnurus→Lykos→Spargapeithes）、Hylaia、眾神之母祭、被 Saulios 一箭射殺 | 有一頁，但把「眾神之母」直接寫成 Cybele，且漏掉系譜與「唯一例外」的修辭定位 |
| 4.78–80 | **Scyles** 全程：在 Borysthenites（Olbia）城內換希臘衣、白色石雕獅身人面像與格里芬環繞的宅邸、雷擊、酒神入教、塔上目擊、被 Octamasades 斬首 | **全缺** |
| 4.81 | **Ariantas** 徵收全民箭鏃鑄成巨釜以清點人口 | **全缺** |
| 4.82 | Tyras 河畔岩上兩肘長的 Heracles 足印（卷四自承「全境唯一奇觀」） | 缺 |
| 4.103 | **Tauri** 祭「少女」，陶魯人自稱即 Agamemnon 之女 Iphigenia；斬首插竿守屋 | **全缺**（Tauri 在 4.102 首次出現即無頁） |
| 4.108 | Geloni（Borysthenites 自稱米利都人）在 Budini 木城內每三年一次的 Dionysos 節慶 | 缺（且與既有 Dionysus 誤置有關） |

## 關鍵文本紀律（本次最重要的產出）

本計畫在規劃階段發生一次**重大事實攔截**，須記錄於案：

- 規劃中原本擬寫「希羅多德 4.108–109 記載斯基泰的 Dionysos 生於 Zeus 大腿」一頁。
- 逐節核對 Loeb／Godley 譯本（LacusCurtius `4A`–`4F`，全卷 1–144 節）後確認：**該段不在卷四**。卷四 4.108 是 Budini／Geloni 的木城與每三年一次的 Dionysos 節慶，4.109 是 Budini 的湖與海狸。
- 故**取消該頁**。理由：資料庫的職責是記錄文獻所載，不是記錄廣為流傳的轉述。寧可少一頁，不可寫入無法在指定卷次驗證的引文。
- 同理，既有 `gods/Ares.md` 與 `comparisons/斯基泰與希臘神話對應比較.md` 提及的 Dionysos 關聯，應改以 4.108 的 Geloni 節慶為據。

---

## Global Constraints

- 目標文化固定為 `cultures/scythian/`（44 個文化中總頁數並列最少 = 69；stories 層 20 頁為全庫並列最少）。
- 每個新頁面**內文**（去除標題行、`- **欄位：**` 行、`---`）字數 **≥300**；本次目標 gods **≥2,500**、stories **≥2,500**、comparisons **≥4,000**。
- 每個新頁面必須有且僅有一個 H1，其後標題層級**不得跳級**。
- 每個新頁面必須含 `## 參考文獻`（或 參考來源／參考資料／References／Sources／Bibliography）區塊，區塊內**至少 3 筆**非引用行。
- 每個新頁面必須有標題以 `跨文化` 開頭的 H2/H3/H4 區段（`^#{2,4}\s*跨文化`）。
- 英文專名放圓括號內；語言繁體中文；引用格式 `作者 (年份). *書名*. 出版地: 出版社.`
- **所有希羅多德引文須標明卷.節**，且不得使用本計畫已證偽的章次。
- 禁止 `populate.py`；不得將新頁面寫入 `scripts/citation_baseline.txt`。
- 不得 `git commit --amend` / `--no-verify` / 改 git config。
- 最終 commit message 首行為 `mythos: enrich scythian`。

---

## File Structure

**新增**

| 路徑 | 職責 |
|---|---|
| `cultures/scythian/gods/Anacharsis.md` | 被希臘世界聖化的斯基泰智者；「野蠻智者」構形的形成與 4.46 的唯一例外修辭 |
| `cultures/scythian/gods/Neuri-wolf-changes.md` | 4.105 紐里人每年化狼數日的「人狼變形」信仰及其薩滿解讀 |
| `cultures/scythian/stories/scyles-and-the-bacchic-initiation.md` | Scyles 換衣入城、酒神入教、雷擊宅邸、塔上目擊、被斬首（4.78–80） |
| `cultures/scythian/stories/ariantas-and-the-arrowhead-census.md` | Ariantas 徵集箭鏃鑄釜清點人口（4.81）與 Tyras 足印（4.82） |
| `cultures/scythian/stories/tauroi-and-iphigenia.md` | Tauri 祭「少女」＝ Iphigenia，斬首插竿守屋（4.103） |
| `cultures/scythian/comparisons/barbarian-sage-and-barbarian-madman.md` | 「野蠻智者」／「野蠻醉漢」對位構形的全球比較（10 文明） |
| `scripts/test_scythian_enrichment.py` | 紅燈／綠燈契約測試，鏡射 `scripts/test_celtic_enrichment.py` |

**修改**

| 路徑 | 職責 |
|---|---|
| `cultures/scythian/gods/README.md` | 追加 2 列 |
| `cultures/scythian/stories/README.md` | 追加 3 列 |
| `cultures/scythian/comparisons/README.md` | 追加 1 列 |
| `cultures/scythian/README.md` | 頁數徽章 27/20/22 → 29/23/23 |
| `cultures/scythian/stories/Anacharsis的悲劇.md` | 修正「Cybele」→ 眾神之母（Μήτηρ Θεῶν）並補系譜與 4.46 定位 |
| `_catalog.json` | `cultures[id=scythian]`：`motifs`、`pantheon`、`stories`、`_stories` 14→17、`gods` 5→7、`comparisons` 5→6 |
| `_state.json` | `runs` 216→217、`enrich_log` 追加 `"scythian"` |
| `README.md` | 計數列與 STATS 區塊（`generate_stats.py`） |
| `.github/workflows/ci.yml` | 註冊 `python scripts/test_scythian_enrichment.py` |

---

## Task 1: 建立紅燈契約測試

- [ ] `cp scripts/test_celtic_enrichment.py scripts/test_scythian_enrichment.py`
- [ ] 改 `CULTURE = "scythian"`，`NEW_PAGES` 填入上表 6 個檔案
- [ ] 改 docstring
- [ ] `python scripts/test_scythian_enrichment.py` → 必須紅燈（6 個 `file does not exist`）
- [ ] `.github/workflows/ci.yml` 註冊

## Task 2: 內容頁（6 頁）

- [ ] `gods/Anacharsis.md`
- [ ] `gods/Neuri-wolf-changes.md`
- [ ] `stories/scyles-and-the-bacchic-initiation.md`
- [ ] `stories/ariantas-and-the-arrowhead-census.md`
- [ ] `stories/tauroi-and-iphigenia.md`
- [ ] `comparisons/barbarian-sage-and-barbarian-madman.md`

## Task 3: 索引與既有頁修正

- [ ] 四份 README（3 子目錄 + 1 文化層）補列與更新徽章
- [ ] 修正 `stories/Anacharsis的悲劇.md`
- [ ] `_catalog.json`／`_state.json`（**注意：`indent=1` 且檔尾無換行**，見下方工程紀律）
- [ ] `python scripts/generate_stats.py` 重生 `README.md` STATS

## Task 4: 閘門

- [ ] `python scripts/ci_checks.py` → ALL CHECKS PASSED
- [ ] 五支 enrichment 測試全綠
- [ ] `git status` 乾淨（除暫存）
- [ ] `git add -A && git commit -m "mythos: enrich scythian — ..." && git push`

---

## 工程紀律（沿用前次教訓）

1. **JSON 格式**：`_catalog.json`／`_state.json` 實為 `indent=1` 且**檔尾無換行**。務必以 `json.dump(..., indent=1, ensure_ascii=False)` 寫回且不補換行，否則產生全檔重排 diff。
2. **`enrich_log` 語意**：是「每次執行一筆」（每文化 2–8 筆），非去重集合。本次只**追加一筆** `"scythian"`，不可用任何去重 guard，否則靜默丟失記錄。
3. **暫存目錄**：`/tmp/opencode` 為 root 所有不可寫；研究用暫存一律放 repo 內 `.tmp-research/`，且**必須在 commit 前刪除**。
4. **重複英文標題**：契約測試的 duplicate gate 會抓 `[(...)]` 結尾相同者；新增頁的英文名不得與既有頁重複。
5. **連結**：新頁互鏈與指向既有頁的連結必須命中真實檔名（`迪兒德麗` → `deirdre-of-the-sorrows` 為前次教訓）。
