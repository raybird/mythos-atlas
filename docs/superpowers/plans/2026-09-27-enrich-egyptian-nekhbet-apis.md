# 埃及神話深化（涅赫貝特／阿匹斯聖牛／活體神諭）Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 為最薄弱文化 egyptian 新增 3 頁（gods／stories／comparisons 各 1），每頁 ≥300 字繁體中文、含跨文化對應與參考來源，並同步所有索引與統計。

**Architecture:** 純內容型變更。三個新頁面各自承載一個獨立子題（護國雙女神／活體神牛傳說／活體神諭比較），再加一支契約測試 `scripts/test_egyptian_nekhbet_enrichment.py` 鏡射既有 enrichment 測試的檢查項。驗證依靠 `scripts/ci_checks.py`（格式、孤兒頁、引用）＋ 全部 11 支 enrichment 契約測試。

**Tech Stack:** Markdown（CommonMark）、Python 3.11（檢查腳本）、Git。

## 目標文化的選擇依據（可複核）

頁數（不含各目錄 `README.md`）並列最低者為 67 頁，共 8 個文化：egyptian、slavic、hittite、polynesian、aboriginal、tupi-guarani、minoan、dacian。以「內容量」（去除標題與 `- **欄位：**` 後的 CJK 字元數）作次級準則後，egyptian 為 112,864 字，遠低於同組其餘（slavic 117,360／hittite 118,268／polynesian 129,339／aboriginal 130,536／minoan 133,238／dacian 141,563）；且 egyptian 有 25 頁被列入 `scripts/citation_baseline.txt`（同組唯一大量缺口），合計 26 頁缺引用。故選 egyptian。

## Global Constraints

- 語言：繁體中文；外文專名以括號標註（例：涅赫貝特 (Nekhbet)）。
- 每頁正文（去除標題行、`---`、`- **欄位：**` 行）≥300 字，實際目標 ≥900 字。
- 每頁必須有 `## 參考文獻`（最後一個引用區塊須有實質內容行，且行首不得為 `>`）。
- 每頁必須有 `## 跨文化…` 開頭的章節。
- H1 必須是第一個標題；標題層級不得跳級；不得有空白標題。
- 所有 `.md` 內部連結必須指向存在的檔案。
- 禁用簡體字；禁用 `populate.py`。
- 新頁不得寫入 `scripts/citation_baseline.txt`。
- 同一 culture 同一目錄內，H1 括號內的英文標題不得重複。
- `comparisons/` 內每個新檔必須列入 `cultures/egyptian/comparisons/README.md`，否則 CI 報 orphan。
- Git 訊息格式：`mythos: enrich egyptian — <中文副題>`。
- 繁體中文校驗：不得出現 `们/为/这/说/后/对/东/门/见/长/车/马/龙/风/飞/鸟/鱼` 等簡體字（此處僅列本計畫易犯者，實際以 `ci_checks.py` 與人工複核為準）。

## File Structure

| 檔案 | 動作 | 責任 |
|------|------|------|
| `cultures/egyptian/gods/涅赫貝特.md` | 新增 | 上埃及護國禿鷹女神、雙女神 (Nebty) 冠、王權正當性 |
| `cultures/egyptian/stories/阿匹斯聖牛的誕生.md` | 新增 | 閃電受孕、二十九徵、孟斐斯神廟、神諭與葬禮、塞拉比斯 |
| `cultures/egyptian/comparisons/活體神諭跨文化比較.md` | 新增 | 8 傳統對照表＋4 功能類型＋4 結構分析 |
| `scripts/test_egyptian_nekhbet_enrichment.py` | 新增 | 本輪 3 頁的契約測試（先紅後綠） |
| `cultures/egyptian/gods/README.md` | 修改（+1 列） | 神祇索引 |
| `cultures/egyptian/stories/README.md` | 修改（+1 列） | 故事索引 |
| `cultures/egyptian/comparisons/README.md` | 修改（+1 列） | 比較索引 |
| `cultures/egyptian/index.md` | 修改 | 原始文獻／核心母題／跨文化平行／重要故事 |
| `_catalog.json` | 修改 | `sources`／`motifs`／`pantheon`／`stories`／`_stories` 20→21／`gods`／`comparisons` |
| `README.md` | 修改 | 文化表 `27\|21\|20` → `28\|21\|21`；總頁面數 3489→3492 |
| `_state.json` | 修改 | `enrich_log` 追加 `egyptian`；`runs` 222→223 |
| `docs/superpowers/plans/2026-09-27-enrich-egyptian-nekhbet-apis.md` | 新增 | 本計畫 |

`docs/` 已在 `ci_checks.py` 的 `EXCLUDED_TOP_DIRS`，不影響檢查。`README.md` 與 `_state.json` 的統計區塊由 `scripts/generate_stats.py` 產生，須以該腳本結果為準，不得手改數字。

---

## Task 1: 建立契約測試（先紅）

**Files:**
- Create: `scripts/test_egyptian_nekhbet_enrichment.py`

**Interfaces:**
- Consumes: `scripts/test_inuit_enrichment.py` 的檢查函式集合（`count_body_chars`／`test_heading_hierarchy`／`test_has_citation`／`test_has_cross_cultural`／`test_indexed_in_readme`／`test_not_baselined`／`find_duplicate_english_titles`）。
- Produces: CLI 契約 `python scripts/test_egyptian_nekhbet_enrichment.py`，exit 0 綠 / exit 1 紅。

- [ ] **Step 1: 寫入測試檔**

以 `scripts/test_inuit_enrichment.py` 為模板，`CULTURE = "egyptian"`，

```python
NEW_PAGES = {
    "gods": ["涅赫貝特.md"],
    "stories": ["阿匹斯聖牛的誕生.md"],
    "comparisons": ["活體神諭跨文化比較.md"],
}
```

並保留其餘常數：`REF_PATTERN`、`CROSS_CULTURAL_PATTERN = re.compile(r"^#{2,4}\s*跨文化", re.MULTILINE)`、`ENGLISH_TITLE_PATTERN = re.compile(r"[(（]([^)）]+)[)）]\s*$")`、`CITATION_BASELINE = ROOT / "scripts" / "citation_baseline.txt"`；`main()` 依模板印出每頁字數與 PASS/FAIL，最後 `sys.exit(0 | 1)`。

- [ ] **Step 2: 執行測試確認失敗**

Run: `python scripts/test_egyptian_nekhbet_enrichment.py`
Expected: exit 1，輸出 3 行 `[FAIL] gods/涅赫貝特.md: file does not exist` 等。

- [ ] **Step 3: Commit（紅燈）**

```bash
git add scripts/test_egyptian_nekhbet_enrichment.py
git commit -m "test: add egyptian nekhbet/apis enrichment contract test (red)"
```

## Task 2: 撰寫 `gods/涅赫貝特.md`

**Files:**
- Create: `cultures/egyptian/gods/涅赫貝特.md`

**Interfaces:**
- Consumes: 本計畫 Global Constraints；`_catalog.json` 中 egyptian 的既有神系與母題。
- Produces: 一個 H1 + 欄位區塊 + 概述／名號與神格／神話事蹟／跨文化對應表／相關條目／參考文獻 的神祇頁。

- [ ] **Step 1: 撰寫頁面**（目標 ≥1,200 字）

必含事實（每項須有出處）：
1. 名 `nḥbt`「涅克貝之女」＝「籃子中的她」，上埃及尼赫貝 (Nekheb／Nekhen，=Hierakonpolis) 的守護神；Herodotus II.38 記其廟在 El-Kab，Graham／Britannica 記 Epithets 含「尼赫貝之 mistress」與第三上埃及 nome 的關聯。
2. 形貌：禿鷹（Griffon vulture，Gardiner 釋種；Kozloff 認為更像 lappet-faced vulture）；亦作鷹身人婦、戴白冠、哺乳法老、展翅覆於王上、爪握 shen 環。
3. 與瓦杰特 (Wadjet) 合稱「雙女神」`nbtj`，五大王名之二 Nebty name；Semerkhet（約前 2920）首見定形；原型以紅冠代替眼鏡蛇。
4. 統一未合併：兩女神並存，合成「雙冠」的守護者；Akhenaten 的 Hebty 名 `Wsr-nswt-mꜣꜥt-ꜥt-ꜣ` 仍承此名。
5. 托勒密王朝埃德夫神廟：Nekhbet 與 Wadjet 為托勒密八世加冕，但兩者頭飾皆畫成禿鷹、眼鏡蛇消失——外來統治者對傳統的誤讀（Wikipedia/Two_Ladies 所述，須標明為現代詮釋）。
6. 跨文化對應表（≥5 列）：印度 Aśvins（原為一體分裂為二的雙生治療神，Naradiya Purana）／中國兩儀—太極（二元合而為一體，周易繫辭「一陰一陽之謂道」）／瑪雅—阿茲特克 雙首蛇柱（Teotihuacan）／羅馬 母狼哺雙子（一頭狼生二子＝單一族裔的雙重起源，Lupa Capitolina）／美國西南 Tewa「雙族」對稱宇宙（Ortiz, *Tewa*）／埃及內部對照：荷魯斯與賽特（王權兩面）。
7. 相關條目：需先確認目標檔存在（`../gods/荷魯斯.md`、`../gods/賽特.md`、`../gods/拉.md`、`../gods/伊西斯.md`、`../stories/蓋布與努特的分離.md` 等），逐一以 `ls` 驗證後再寫連結。

- [ ] **Step 2: 執行測試確認此頁綠、其餘仍紅**

Run: `python scripts/test_egyptian_nekhbet_enrichment.py`
Expected: `gods/涅赫貝特.md: … chars — PASS`，仍 exit 1（另兩檔缺）。

- [ ] **Step 3: Commit**

```bash
git add cultures/egyptian/gods/涅赫貝特.md
git commit -m "mythos: enrich egyptian gods — 涅赫貝特與雙女神王冠"
```

## Task 3: 撰寫 `stories/阿匹斯聖牛的誕生.md`

**Files:**
- Create: `cultures/egyptian/stories/阿匹斯聖牛的誕生.md`

**Interfaces:**
- Consumes: `gods/涅赫貝特.md`（同目錄互鏈）、`gods/Ptah.md`（孟斐斯城名 Ḥwt-kꜣ-Ptah）。
- Produces: 故事頁，結構為 `## 故事背景`／`## 情節`／`## 跨文化平行`／`## 相關主題`／`## 參考文獻`。

- [ ] **Step 1: 撰寫頁面**（目標 ≥1,800 字）

必含情節節點（每節點標明出處）：
1. 受孕：孟斐斯一頭母牛被天降閃電击中而受孕（Herodotus III.28「a ray from heaven」；另有月光說，Aelian *NA* 11.10；Plutarch *De Is. et Os.* 43）。
2. 辨識徵記：Herodotus III.28 的五項（通體黑、額上白色方印、背有鷹形、尾有兩種毛、舌上聖甲蟲狀結節）；Pliny *NH* 8.71 補右側新月角狀白斑；Aelian 11.10 稱二十九徵構成天文—物理系統（晚期累積）。須指出兩份清單不一致本身即為史料學事實。
3. 認養與入城：聖書士在朝東方向建屋、以乳餵養四個月，新月時以聖船送入孟斐斯「普塔之卡宅」大宅（Elean 11.10；Diodorus 1.27；Strabo XVII）。
4. 孟斐斯城名 Ḥwt-kꜣ-Ptah「普塔之卡的宅」＝阿匹斯即普塔之卡 (bꜣw n Ptḥ) 的活像；牛欄、只飲指定井水、每年僅一頭同樣有印記的母牛相會（Pliny *NH* 8.66 條目所引）。
5. 神諭：進入兩間 thalami 之一即為吉凶（Pliny *NH* 8.185）；Diodorus 8.9、Pausanias 7.22.2、Lutatius ad Stat. *Theb.* 3.478 所載之兆；阿匹斯悲鳴／拒食被讀為王死之兆。
6. 壽限與葬禮：至多二十五年（Lucan *Phars.* 8.477；Plutarch 56），逾期則被殺秘葬；自然死亡則公開大葬，木乃伊化後送薩卡拉塞拉比斯地下殿（Oxford Classical Dictionary「Apis」條；Diodorus 1.85、1.96；Pausanias 1.18.4；Plutarch 29）。
7. 塞拉比斯 (Serapis)：托勒密時期 Osir-ḥr-ꜥpy 的綜合；「塞拉比斯＝阿匹斯之墓」為古說（Plutarch 29 所載，該書同時駁斥）；尼坦涅波二世二年石碑與薩卡拉 wꜣbt 遺址為第四世紀重修的直接證據（*Journal of Egyptian Archaeology* 76, 1990）。
8. 跨文化平行（三型）：
   - 非人神父的受孕：宙斯化公牛（Alcmene／Pasiphae）與克里特公牛傳說、米諾斯（Plutarch 29 引菲拉爾科斯把兩頭牛帶進埃及的說法並斥為荒謬）。
   - 印記作為天命：麒麟吐玉書（孔子誕生，《拾遺記》系統）對照額上雙徵。
   - 活體神諭：銜接 Task 4 比較頁。
   須註明：拿破崙 1806 年於孟斐斯諮詢阿匹斯一事僅見於其回憶錄與後世記述，非古典文獻，須標為傳聞層級。

- [ ] **Step 2: 執行測試確認 stories 綠、comparisons 仍紅**

Run: `python scripts/test_egyptian_nekhbet_enrichment.py`
Expected: `stories/阿匹斯聖牛的誕生.md: … chars — PASS`，仍 exit 1（comparisons 缺）。

- [ ] **Step 3: Commit**

```bash
git add cultures/egyptian/stories/阿匹斯聖牛的誕生.md
git commit -m "mythos: enrich egyptian stories — 阿匹斯聖牛的誕生與神諭"
```

## Task 4: 撰寫 `comparisons/活體神諭跨文化比較.md`

**Files:**
- Create: `cultures/egyptian/comparisons/活體神諭跨文化比較.md`
- Modify: `cultures/egyptian/comparisons/README.md`（+1 列，否則 CI orphan）

**Interfaces:**
- Consumes: Task 3 的阿匹斯神諭節點作為埃及錨點。
- Produces: 比較頁，結構為 `## 跨文化對照總表`（Markdown 表）＋各傳統小節＋`## 四種功能類型`＋`## 結構分析`＋`## 參考文獻`。

- [ ] **Step 1: 撰寫頁面**（目標 ≥2,000 字）

八傳統對照表，欄位：文化／神聖動物／傳訊方式／判讀者／典型問題／出處：
1. 埃及 — 阿匹斯（雙室、姿態）／聖甲蟲（*Papyrus Anastasi* I「甲蟲已藏一年」）
2. 希臘 — 多多納（鴿／橡樹葉／青銅器叮噹，Herodotus II.55–57、Strabo VII）；奧利斯三頭黑牛（Iliad XVI.140–144；Euripides *Aeacus*）
3. 波斯 — 帕爾邦加爾白牛 Gopat Shāh（`cultures/persian/gods/gopat-shah.md`，末世執行者）
4. 印度 — 母牛初鳴（*Ṛgveda* 10.129.7）與南迪／馬祭的行為判讀
5. 羅馬 — 法列里烏姆公牛走向 Gemonian 刑架（Livy I.31，前 40）；卡比托利烏斯母狼之存亡（Tacitus *Hist.* 5.3 以後的羅馬命運預示）
6. 安第斯 — 庫斯科科里坎卡的羊駝神像（西班牙編年史《秘魯征服記》系）
7. 中國 — 殷墟甲骨龜卜（《周禮·卜師／大卜》、《史記·龜策列傳》、《易經·繫辭上》）
8. 北歐 — Huginn 與 Muninn 每日回報（*Prose Edda*, Gylfaginning）

四功能類型：A 容姿判讀、B 聲音判讀、C 出現即神諭、D 代理傳訊。
四結構分析：① 活體的不可馴服性即可信度；② 集中於遷都、開戰、災疫、王位等邊界時刻；③ 解讀權構成實質政治權（神書士階級）；④ 聖獸之死被讀作國運危機（阿匹斯之葬 vs 母狼之亡）。

- [ ] **Step 2: 把新頁加入 `cultures/egyptian/comparisons/README.md`**

在既有表列最後一行之後、`---` 之前插入：
`| [活體神諭跨文化比較](活體神諭跨文化比較.md) | 活體神諭跨文化比較 |`

- [ ] **Step 3: 執行測試確認全綠**

Run: `python scripts/test_egyptian_nekhbet_enrichment.py`
Expected: 三頁皆 PASS，`All tests PASSED.`，exit 0。

- [ ] **Step 4: Commit**

```bash
git add cultures/egyptian/comparisons/活體神諭跨文化比較.md cultures/egyptian/comparisons/README.md
git commit -m "mythos: enrich egyptian comparisons — 活體神諭跨文化比較"
```

## Task 5: 索引、catalog、統計同步

**Files:**
- Modify: `cultures/egyptian/gods/README.md`、`cultures/egyptian/stories/README.md`、`cultures/egyptian/index.md`、`_catalog.json`、`README.md`、`_state.json`

- [ ] **Step 1: 加入兩個目錄索引**

`gods/README.md` 與 `stories/README.md` 各在表格末列後、`---` 前插入一列（本目錄索引為 auto-generated 產物，僅手動追加一行，**不得**執行 `regenerate_all.py`）。

- [ ] **Step 2: 更新 `cultures/egyptian/index.md`**

在「原始文獻」補《塞拉比斯與阿匹斯相關銘文與古典作家記述》；「核心母題」補「護國雙女神 (Nebty)」與「活體神牛神諭」；「跨文化平行」補 2 條 `↔`；「重要故事」補「阿匹斯聖牛的誕生」。

- [ ] **Step 3: 更新 `_catalog.json` 的 egyptian 條目**

`sources` 補 `《Papyrus Anastasi I》`、`Diodorus Siculus《歷史》`、`Plutarch《Isis and Osiris》`；`motifs` 補 `護國雙女神(Nebty)`、`活體神牛神諭`；`pantheon` 補 `涅赫貝特(上埃及)`、`阿匹斯(孟斐斯聖牛)`；`stories` 補 `阿匹斯聖牛的誕生`；`_stories` 20→21；`gods` 補 `涅赫貝特`；`comparisons` 補 `活體神諭跨文化比較`。編輯後必須 `python -c "import json;json.load(open('_catalog.json'))"` 驗證可解析。

- [ ] **Step 4: 重新產生統計**

Run: `python scripts/generate_stats.py`
Expected: `README.md` 統計區塊更新（總頁面數 3489→3492、文化表 egyptian `27|21|20`→`28|21|21`、總執行次數 222→223）。以腳本輸出為準，不手改數字。

- [ ] **Step 5: 記錄本輪執行於 `_state.json`**

`enrich_log` 末項 `"finno-ugric"` 後追加 `"egyptian"`；`runs` 222→223。
Run: `python -c "import json;json.load(open('_state.json'))"`

- [ ] **Step 6: 全面驗證**

Run:
```bash
python scripts/ci_checks.py
python scripts/test_egyptian_nekhbet_enrichment.py
for f in scripts/test_*_enrichment.py; do python "$f" >/dev/null || echo "FAIL $f"; done
```
Expected: `ci_checks.py` 輸出 `✅  ALL CHECKS PASSED`（錯誤數與 HEAD 相同，不得新增）；本輪測試 exit 0；既有 10 支測試無 FAIL。

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "mythos: enrich egyptian — 涅赫貝特／阿匹斯聖牛／活體神諭"
```

## Task 6: 推送

- [ ] **Step 1: 推送**

Run: `git push`
Expected: `master -> master`，無 non-fast-forward 錯誤。

## Self-Review

1. **規格覆蓋**：使用者要求 4 件事——(a) 檢查 `_catalog.json` 與 `cultures/` 找最薄弱文化（Global Constraints 上方「目標文化的選擇依據」記錄可複核的三層量測）、(b) 新增 gods／stories／comparisons 各一頁且每頁 ≥300 字含跨文化對應與來源（Task 2–4，契約測試強制）、(c) `git add -A && git commit -m "mythos: enrich <culture-name>" && git push`（Task 5 Step 7、Task 6）、(d) 回報新增內容（Execution Handoff）。全數有對應 Task。
2. **無佔位符**：三頁內容以具體出處（Herodotus III.28、Pliny *NH* 8.185、Iliad XVI.140–144、Livy I.31、*Ṛgveda* 10.129.7 等）逐點指定，無 TBD／TODO／「類似 Task N」。
3. **型別／名稱一致性**：`NEW_PAGES` 三個鍵與 Task 2–4 建立的三個檔名逐字一致；索引與 catalog 新增的名稱與檔名一致；`_state.json` 與 `README.md` 統計一律交由 `generate_stats.py`，避免手改數字造成兩處不一致。
4. **風險登記**：
   - Task 2 Step 1.7 要求寫連結前先 `ls` 驗證目標檔存在（埃及目錄中檔名為中文，錯字會造成 broken link 導致 CI 失敗）。
   - 比較頁引用其他文化的既有頁面（`cultures/persian/gods/gopat-shah.md`）前同樣需驗證。
   - `README.md`／目錄 `README.md` 為 auto-generated 產物，只手動追加一行，禁止執行 `regenerate_all.py`（會重排整份索引）。
