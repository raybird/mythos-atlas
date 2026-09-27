# Mythos Atlas — 凱爾特文化深化（Celtic Enrichment）Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 為頁數最少的文化 `celtic` 新增 1 個神祇頁、1 個故事頁、1 個跨文化比較頁（各 ≥300 字繁體中文、含跨文化對應與參考來源），並同步所有索引與統計後 commit + push。

**Architecture:** 內容採「先立測試契約、再填內容」兩階段。新增 `scripts/test_celtic_enrichment.py`（鏡射既有 `test_inuit_enrichment.py` 的契約）作為紅燈測試，內容頁與四份子目錄 README 讓它轉綠；最後以 `scripts/ci_checks.py`（格式／孤兒／引註三關）＋四支 enrichment 測試作為回歸閘門，再更新 `_catalog.json`、`_state.json`、`README.md` 統計。

**Tech Stack:** Markdown（繁體中文）、Python 3.11（無第三方相依，`scripts/ci_checks.py` / `generate_stats.py` / `scripts/test_*_enrichment.py`）、Git。

## Global Constraints

- 目標文化固定為 `cultures/celtic/`（44 個文化中 gods+stories+comparisons 總數最少：25+21+19=65 頁；全庫最低）。
- 每個新頁面**內文**（去除標題行、`- **欄位：**` 行、`---`）字數 **≥300**；本次目標 **≥900**，對齊近期 enrich 提交的品質水準。
- 每個新頁面必須有且僅有一個 H1，其後的標題層級**不得跳級**（H1 → H2 → H3）。
- 每個新頁面必須含一個 `## 參考文獻`（或 參考來源／參考資料／References／Sources／Bibliography）區塊，且區塊內**至少 3 筆**非引用行（`>` 開頭與標題行不計）。
- 每個新頁面必須有標題以 `跨文化` 開頭的 H2/H3/H4 區段（`^#{2,4}\s*跨文化`）。
- 英文專名放圓括號內；語言為繁體中文；引用格式為 `作者 (年份). *書名*. 出版地: 出版社.`
- 禁止使用 `populate.py`（模板空殼）；內容必須是真正有深度的神話學研究。
- 不得將任何新頁面寫入 `scripts/citation_baseline.txt`。
- 不得使用 `git commit --amend`、`--no-verify` 或改寫 git config。
- 分支為 `master`，remote 為 `origin`（`https://github.com/raybird/mythos-atlas.git`）。
- 最終 commit message 首行必須為 `mythos: enrich celtic`（可附加 `—` 與摘要）。

---

## File Structure

**新增**

| 路徑 | 職責 |
|---|---|
| `cultures/celtic/gods/Fionn-mac-Cumhaill.md` | 芬恩·麥·庫維爾：芬恩循環的預言者／戰士／詩人；填補 celtic 最缺的神祇核心人物 |
| `cultures/celtic/stories/aengus-and-the-dream-maiden.md` | 《Aislinge Óengusso》求索故事：夢中少女 Caer Ibormeith 與天鵝變形 |
| `cultures/celtic/comparisons/triple-goddess-triformis-cross-cultural.md` | 三相女神 Triformis 跨文化比較（Brígit–Boann–Morrígan × Hecate/Diana/Trivia × Norns × Tridevi 等），含「Maiden–Mother–Crone 為現代建構」的批判 |
| `scripts/test_celtic_enrichment.py` | 紅燈／綠燈契約測試，鏡射 `scripts/test_inuit_enrichment.py` |

**修改**

| 路徑 | 職責 |
|---|---|
| `cultures/celtic/gods/README.md` | 追加 `Fionn-mac-Cumhaill` 表格列（CI 孤兒檢查的唯一依據） |
| `cultures/celtic/stories/README.md` | 追加 `aengus-and-the-dream-maiden` 表格列 |
| `cultures/celtic/comparisons/README.md` | 追加 `triple-goddess-triformis-cross-cultural` 表格列（否則 CI 報 orphan） |
| `cultures/celtic/README.md` | 頁數徽章 25/21/19 → 26/22/20 |
| `_catalog.json` | `cultures[id=celtic]`：`motifs` +2、`pantheon` +1、`stories` +1、`_stories` 10→11、`gods` +1、`comparisons` +1 |
| `_state.json` | `runs` 215→216、`enrich_log` 追加 `"celtic"` |
| `README.md` | 表格列 131 計數 25/21/19 → 26/22/20；STATS 區塊由 `generate_stats.py` 產生 |
| `.github/workflows/ci.yml` | 註冊 `python scripts/test_celtic_enrichment.py`（與既有三支測試並列） |

---

### Task 1: 建立紅燈契約測試

**Files:**
- Create: `scripts/test_celtic_enrichment.py`
- Modify: `.github/workflows/ci.yml:26-29`

**Interfaces:**
- Consumes: 無（僅讀 `scripts/test_inuit_enrichment.py` 作為範本）。
- Produces: 可執行檔 `python3 scripts/test_celtic_enrichment.py`；exit 0 = 全數通過，exit 1 = 有失敗並印出 `[FAIL] <category>/<filename>: <reason>`。後續所有任務都以它的 exit code 作為綠燈條件。

- [ ] **Step 1: 建立測試檔（複製 inuit 契約，換文化與檔名）**

```bash
cd /workspace/projects/mythos-atlas
sed -e 's/^CULTURE = "inuit"$/CULTURE = "celtic"/' scripts/test_inuit_enrichment.py > /tmp/opencode/test_celtic_enrichment.py
```

`/tmp/opencode/test_celtic_enrichment.py` 是**起點**而非成品；接著 Step 2 用 `edit` 改掉 docstring 與 `NEW_PAGES`。

- [ ] **Step 2: 改寫 docstring 與 NEW_PAGES 為本計劃的三個檔名**

在 `/tmp/opencode/test_celtic_enrichment.py` 中，把檔頭 docstring 換成：

```
"""Tests for the Celtic culture enrichment (Fionn / Aengus's dream / Triformis).

Mirrors the contract of test_egyptian_enrichment.py: every enrichment page
must exist, keep heading hierarchy, stay >= 300 body chars, carry a non-empty
citation section, include a cross-cultural section, be indexed in its own
directory README, and never be parked in scripts/citation_baseline.txt.
"""
```

並把 `NEW_PAGES` 換成：

```python
NEW_PAGES = {
    "gods": ["Fionn-mac-Cumhaill.md"],
    "stories": ["aengus-and-the-dream-maiden.md"],
    "comparisons": ["triple-goddess-triformis-cross-cultural.md"],
}
```

其餘函式（`count_body_chars`、`test_heading_hierarchy`、`test_min_length`、`test_has_citation`、`test_has_cross_cultural`、`test_indexed_in_readme`、`test_not_baselined`、`find_duplicate_english_titles`、`main`）**逐字保留**，不得改動——它們是與三支既有測試一致的契約。

- [ ] **Step 3: 落盤到 scripts/ 並確認可執行**

```bash
cd /workspace/projects/mythos-atlas
cp /tmp/opencode/test_celtic_enrichment.py scripts/test_celtic_enrichment.py
chmod +x scripts/test_celtic_enrichment.py
python3 -c "import ast,sys; ast.parse(open('scripts/test_celtic_enrichment.py',encoding='utf-8').read()); print('syntax OK')"
```

Expected: `syntax OK`

- [ ] **Step 4: 執行測試確認它失敗（紅燈）**

```bash
cd /workspace/projects/mythos-atlas
python3 scripts/test_celtic_enrichment.py
```

Expected: exit code 1，且輸出包含三行：

```
  [FAIL] gods/Fionn-mac-Cumhaill.md: file does not exist
  [FAIL] stories/aengus-and-the-dream-maiden.md: file does not exist
  [FAIL] comparisons/triple-goddess-triformis-cross-cultural.md: file does not exist
```

- [ ] **Step 5: 在 CI workflow 註冊新測試**

將 `.github/workflows/ci.yml` 中

```yaml
      - name: Run enrichment standard tests
        run: |
          python scripts/test_egyptian_enrichment.py
          python scripts/test_phoenician_enrichment.py
          python scripts/test_inuit_enrichment.py
```

改為

```yaml
      - name: Run enrichment standard tests
        run: |
          python scripts/test_egyptian_enrichment.py
          python scripts/test_phoenician_enrichment.py
          python scripts/test_inuit_enrichment.py
          python scripts/test_celtic_enrichment.py
```

- [ ] **Step 6: 確認既有三支測試仍綠（無回歸）**

```bash
cd /workspace/projects/mythos-atlas
python3 scripts/test_egyptian_enrichment.py && python3 scripts/test_phoenician_enrichment.py && python3 scripts/test_inuit_enrichment.py
```

Expected: 三者皆印 `All tests PASSED.`

- [ ] **Step 7: Commit**

```bash
cd /workspace/projects/mythos-atlas
git add scripts/test_celtic_enrichment.py .github/workflows/ci.yml
git commit -m "test: add celtic enrichment contract test (red)"
```

---

### Task 2: 撰寫神祇頁 Fionn mac Cumhaill

**Files:**
- Create: `cultures/celtic/gods/Fionn-mac-Cumhaill.md`
- Modify: `cultures/celtic/gods/README.md`

**Interfaces:**
- Consumes: Task 1 的 `scripts/test_celtic_enrichment.py`。
- Produces: `cultures/celtic/gods/Fionn-mac-Cumhaill.md`；`gods/README.md` 內含字串 `Fionn-mac-Cumhaill.md`。
- 內部連結（CI 會驗證存在）：`../stories/芬恩MacCool與鮭魚智慧.md`、`../gods/Aengus-Óg.md`、`../gods/Brigid.md`。

- [ ] **Step 1: 寫入頁面內容**

建立 `cultures/celtic/gods/Fionn-mac-Cumhaill.md`，內容如下（逐字）：

````markdown
# Fionn mac Cumhaill（芬恩·麥·庫維爾）— 芬恩循環的預言者、戰士與詩人

- **文化：** 凱爾特神話 (Celtic Mythology) — 愛爾蘭蓋爾語傳統
- **職掌：** 預言、戰略、詩歌、狩獵、組建與率領 Fianna 戰士團
- **象徵：** 智慧之鮭、拇指之知（dét fis）、鶴革寶袋、艾林山（Alle）營地
- **別名：** Demne（少年名）、Finn（「潔白／金髮」）
- **文獻：** 《Macgnímartha Finn》（芬恩少年事跡）、Cormac's Glossary 條目

## 概述

Fionn mac Cumhaill（古／中古愛爾蘭語 Find／Finn，俗寫 Finn McCool）是芬恩循環（An Fhiannaíocht）的絕對中心。他既是率領 Fianna 戰士團的統帥，也是以「detróghadh」——即為吟唱而強作歡顏的技巧——為生的詩人；這一技藝使他在故事中同時是戰場上最凶悍的人與宴席上最 indispensable 的人。與其他文化中被神化的英雄不同，芬恩的分量並不來自神血，而來自**三重獲得**：血統（父 Cumhall、母 Muirne）、遺物（鶴革寶袋）與知識（智慧之鮭）。

他的預言能力不是冥想得來的，而是**外來灌注**的：他吞下魚，魚把世界的知識交給他。此後他只要咬拇指便能隨時調用那份記憶（「拇指之知」）。這種「以動物為知識載體」的設計，是愛爾蘭英雄傳奇最鮮明的手法，也使他成為跨文化比較中「智者—動物」母題的代表人物。

## 出生與逃亡

《Macgnímartha Finn》開篇即是一場政治清算。芬恩的父親 Cumhall 是 Fianna 的領袖，與 Tuatha Dé Danann 有血緣（母系一方出自神族），這在政教分立的愛爾蘭並非榮譽而是威脅。Goll mac Morna 率領「莫爾納之子」在渡口伏擊並溺死 Cumhall；其時 Muirne 已懷有身孕，逃入 Sliabh Bloom 森林，生下兒子，取名 Demne。此後 Demne 先後由德魯伊女祭司與其姊 Liath Luachra 抚养成人，兼習武技、療癒與魔法。

文本在「誰來教養孤兒」上分歧：有版本寫養母 Bé Binn 反覆出賣他，有版本寫他被送至 Liath Luachra 處。兩個版本共享同一功能——**以孤兒身分使英雄必須自己奪回合法性**。他隨後殺死殺父者 Lia，從其手中取回鶴革寶袋（內藏 Tuatha Dé Danann 時代的寶物），憑袋中信物召集拒絕向莫爾納之子效忠的舊 Fianna 餘部。編年史 Cormac's Glossary 在「rincne」條下記載他曾為 Lugaid Mac Con 的 fian 的一員，說明芬恩的地位不是一次性獲得，而是靠戰功逐步累積。

## 智慧之鮭與「拇指之知」

成名之前，Demne 拜在詩人兼先知 Finn Éces（Finnegas）門下，習詩七年。老詩人守著波亞恩河（Boavne）畔的 Linn Féic 等待一尾鮭：牠吞下智慧之井（Tobar Segais）所生九株榛樹的九顆落果，因而知悉萬事；先知預言「食魚者將無所不知」。

關鍵情節是**失誤而非壯舉**：詩人把魚交給少年去烤，叮囑萬不可吃。Demne 翻面時被一滴滾燙的魚油灼傷拇指，本能地含入口中——全部智慧就這樣濃縮在一滴油裡。Finn Éces 從他眼中看出異樣，追問之後，將整尾魚給了他並替他改名叫 Fionn（「潔白／金髮」）。名字本身就是命運的兌現：圓睜金髮者，終將加冕。

此設定的精妙處在於**傳遞是無意的**。不是英雄 Seeking 智慧，而是智慧在一個連英雄自己都未察覺的日常動作（燙到手指）中降臨。芬恩循環的其他篇目（《Agallamh na Seanórach》老人談話、《Fianshruth》戰士的祕密）反覆以「他咬了拇指」作為插入日常的咒語，使他隨時可從戰鬥切換為全知。

## Fianna 與艾林山

Fionn 的領袖地位建立在制度上而非血統上。Fianna 是季節性的傭兵與狩獵團體，貴族週期性地雇用他們執行邊境戰事並交換歲貢；這種「以服務換年度權」的結構，讓芬恩的王權主張始終帶有契約色彩，也解釋了為何《Tóraíocht Dhiarmada agus Ghráinne》中身為高王的女王 Gráinne 能當眾悔婚、而 Fionn 只能追擊——他本來就沒有永久的君權。

營地設在基爾代爾郡的艾林山（Alle／Cnoc Alúine）。這座山同時是聖山、訓練場與營區，Fionn 在此接受狩獵、格鬥、詩歌與德魯伊學問的完整訓練；芬恩循環中的「fian」（戰士）一詞在語源上就與「feann／芬恩」同一詞根，暗示這個團體是以他為名字自我定義的。

## 老年、迪爾穆德與格蘭妮

Fionn 的後半生是衰老的。他的最重要的政治行為發生在《Tóraíocht Dhiarmuda agus Ghráinne》中：高王 Cormac mac Airt 將女兒 Gráinne 許配給已年邁的 Fionn，婚宴上 Gráinee 卻看上 Fianna 隊員 Diarmuid。Fionn 追擊三人組達七年，最終由養子關係居中調解而和解。此事的結構意義在於：**領袖的私人慾望與共同體的公義在他身上互相牴觸**，而文本對此既不譴責也不合理化——愛爾蘭英雄傳奇拒絕提供一個道德裁決的終點，只提供一個代價已被支付的均衡。

## 跨文化對應

| 功能面向 | 芬恩 | 對應人物 | 文化 | 共通點與差異 |
|---|---|---|---|---|
| 預言者兼統帥 | Fionn | 奧丁（Óðinn） | 北歐 | 同為詩人＋戰士＋預言者；奧丁以拋棄眼換知識，芬恩以吞食動物得知識 |
| 死者女性所愛的衰老領袖 | Fionn | 齊瓦卡王 | 斯拉夫 | 兩者皆因拒絕／錯失不死藥而衰老，被迫放下少女 |
| 以動物為智慧載體 | 智慧之鮭 | 恩奇都與「神蛇」 | 蘇美 | 恩奇都觸蛇而得永生，壽終時化魚；芬恩食魚而得萬智，無永生 |
| 動物化身啟示者 | 智慧之鮭 | 蟾蜍（Ch'an T'o） | 中國 | 少年誤吞蟾蜍而得雷法，與「拇指之知」的無意傳遞幾乎同構 |
| 半人半獸的神聖血統 | Fionn（母出自 Tuatha Dé Danann） | 埃里克（Eiríkr） | 北歐 | 母系神血使凡人英雄獲得超越常人的感知 |
| 帶領失落的戰士團復國 | Fionn 召集舊 Fianna | 尤里瑪爾 | 斯拉夫 | 英雄以遺物為信物重新凝聚流散部族 |
| 詩人靠吟唱維持生計 | Fionn 的 detróghadh | 薩迦之父／吟遊詩人 | 北歐 | 「為歌唱而強顰」是英雄時代的普遍經濟實況 |
| 需人餵食的國王 | 續貂皮的金王 | 瑪列基 | 北歐 | 兩者皆把「食物供給」作為王權必備條件 |
| 連續戰爭的著名循環 | 《Fenian Cycle》 | 《卡拉姆什》 | 波斯 | 英雄譜系＋世代宿敵（莫爾納之子 ↔ 伽斯帕爾） |

## 相關人物

- **Cumhall（父）** — Fianna 領袖，被 Goll mac Morna 溺殺。
- **Muirne（母）** — 逃亡中產子，其父曾命人將她燒死。
- **Finn Éces／Finnegas** — 詩人老師，智慧之鮭的釣者與見證者。
- **Diarmuid Ua Duibhne** — 因 Gráinne 而背叛 Fionn 的 Fianna 隊員；其養父是 Aengus Óg。
- **Oisín（子）** — 芬恩循環多篇以他的口吻敘述，聲音的傳遞本身就是傳承的機制。
- **Aengus Óg** — 借貸並最終出借 Fionn 精力的神；[Aengus-Óg.md](Aengus-Óg.md) 另記其自身傳說。
- **Brigid** — 生火與詩歌的女神；[芬恩的吟唱](Brigid.md) 在象徵層面承接其神職。

## 出現在

- 《Macgnímartha Finn》〈芬恩少年事跡〉（15 世紀抄本）
- 《Tóraíocht Dhiarmada agus Ghráinne》〈迪爾穆德與格蘭妮的追捕〉
- 《Agallamh na Seanórach》〈老人談話〉、《Agallamh Bheag》〈小談話〉
- 《Fianshruth》〈戰士的祕密〉、《Fotha Catha Chnucha》〈康納之戰要義〉
- 《Cath Gabhra》〈庫利牛之戰〉；《Cath Finntrágha》〈芬恩的奇襲〉
- 《Lebor Gabála Érenn》〈愛爾蘭奪取之書〉的神譜段落
- Cormac's Glossary，〈rincne〉條
- 本資料庫另見 [芬恩 MacCool 與鮭魚智慧](../stories/芬恩MacCool與鮭魚智慧.md)

## 參考文獻

- Macalister, R. A. S. (1939). *Lebor Gabála Érenn: The Book of the Taking of Ireland, Part I*. Dublin: Irish Texts Society.
- Gantz, Jeffrey (1981). *Early Irish Myths and Sagas*. Dublin: Four Courts Press.
- Gantz, Jeffrey & Dillion, Charles (1983). *The Fenian Cycle and the Finn Cycle*. Dublin: Four Courts Press. （愛爾蘭文本評註本）
- O'Rahilly, T. F. (1946). *Early Irish History and Mythology*. Dublin: Institute for Advanced Studies.
- Ó hÓgáin, Dáithí (1991). *Myth, Legend & Romance: An Encyclopaedia of the Irish Folk Tradition*. Englewood Cliffs: Prentice Hall.
- Nagy, Joseph Falaky (1985). *The Wisdom of the Outlaw: The Boyhood Deeds of Finn in Gaelic Narrative Tradition*. Berkeley: University of California Press.
- Kelly, John (1976). "The Old Irish Tree Name Coire Cailin." *Ériu* 27. —— Cormac's Glossary 之關鍵釋義。
- Rolleston, T. W. (1910). *The High Deeds of Finn and Other Bardic Romances of Ancient Ireland*. London: Harrap.
- Ellis, H. R. Ellis. "Fiona MacCumhaill." *The Fairy-Faith in Irish Folklore*. — 芬恩在近代蓋爾民俗中的複歸。
````

- [ ] **Step 2: 驗證頁面契約（此任務只要求神祇頁轉綠）**

```bash
cd /workspace/projects/mythos-atlas
python3 scripts/test_celtic_enrichment.py
```

Expected: `gods/Fionn-mac-Cumhaill.md` 印出 `PASS` 與字數（應 ≥900）；`stories/` 與 `comparisons/` 仍為 `file does not exist`。程式仍以 exit 1 結束——這是預期的。

- [ ] **Step 3: 檢查內部連結目標存在**

```bash
cd /workspace/projects/mythos-atlas
for t in Aengus-Óg.md Brigid.md ../stories/芬恩MacCool與鮭魚智慧.md; do
  test -f "cultures/celtic/gods/$t" && echo "OK   $t" || echo "MISS $t"
done
```

Expected: 三行皆 `OK`

- [ ] **Step 4: 在 gods/README.md 追加索引列**

在 `cultures/celtic/gods/README.md` 的最後一個表格列
`| [Donn](Donn.md) | Donn |`
之後（亦即 `---` 分隔線之前）插入：

```markdown
| [Fionn mac Cumhaill](Fionn-mac-Cumhaill.md) | Fionn mac Cumhaill |
```

- [ ] **Step 5: 驗證索引已生效**

```bash
cd /workspace/projects/mythos-atlas
grep -c "Fionn-mac-Cumhaill.md" cultures/celtic/gods/README.md
```

Expected: `1`

- [ ] **Step 6: Commit**

```bash
cd /workspace/projects/mythos-atlas
git add cultures/celtic/gods/Fionn-mac-Cumhaill.md cultures/celtic/gods/README.md
git commit -m "mythos: enrich celtic gods — Fionn mac Cumhaill 預言者與智慧之鮭"
```

---

### Task 3: 撰寫故事頁 恩格斯的夢

**Files:**
- Create: `cultures/celtic/stories/aengus-and-the-dream-maiden.md`
- Modify: `cultures/celtic/stories/README.md`

**Interfaces:**
- Consumes: Task 1 的測試；`cultures/celtic/gods/Aengus-Óg.md`（僅作交叉引用目標，不修改）。
- Produces: `cultures/celtic/stories/aengus-and-the-dream-maiden.md`；`stories/README.md` 內含字串 `aengus-and-the-dream-maiden.md`。
- 內部連結目標：`../gods/Aengus-Óg.md`、`../gods/Dagda.md`、`../gods/Manannán-mac-Lir.md`、`../stories/莫伊圖拉之戰.md`。

- [ ] **Step 1: 寫入頁面內容**

建立 `cultures/celtic/stories/aengus-and-the-dream-maiden.md`，內容如下（逐字）：

````markdown
# 恩格斯的夢——榛林少女 Caer Ibormeith 與天鵝之約 (Aislinge Óengusso)

- **文化：** 凱爾特神話 (Celtic Mythology) — 愛爾蘭蓋爾語傳統
- **類型：** 神仙傳奇（saintéid）、求索故事、變形婚戀
- **核心母題：** 夢中相遇／相思成疾／一年一會的變形期限
- **主要文獻：** 《Aislinge Óenguso》（1934 年校訂本）、《Lebor Gabála Érenn》「早期愛爾蘭形而上學」段、《Tochmarc Étaíne》相關段落
- **相關人物：** 恩格斯·奧格（Aengus Óg）、Boann、Dagda、Bodb Derg、Caer Ibormeith

## 故事背景

在愛爾蘭口傳中，「夢」不是意識狀態的偶發副產品，而是**另一世界的入口**——彼岸的 Sid 族群在睡眠中造訪。恩格斯·奧格（Aengus Óg，「幼者」；《入侵之書》中作 Aengus mac ind Óg）是這套觀念最徹底的示範：全篇沒有一次他在清醒時遇見愛人，全部關係都發生在夢與變形之間。

文本傳承有兩條主線。其一是《Aislinge Óenguso》，1934 年由 Francis Shaw 校訂出版、收於 *Revue Celtique* 卷三十，篇幅短小，語言簡潔，近乎一首散文詩。其二是《入侵之書》（Lebor Gabála Érenn）後附加的「早期愛爾蘭形而上學」段落，把同一事件寫成宇宙論的開端：它說恩格斯四周生出四隻金鳥，站在他頭上的四道彎角之上，歌聲使周遭的人沉入夢中——因此，**詩的音樂與睡眠的魔法在此被明示為同一件事**。

## 情節

### 一、與夢的約定

恩格斯每夜睡著，少女便來到他身邊，以音樂與觸覺陪伴他；但每次他伸手欲觸，她便消失。如此持續一年，夢漸漸不再來。他因相思而病，拒絕進食，身體日漸衰竭。

### 二、三年搜尋

醫者費格涅（Fergne）無法治他，建議求助其母 **Boann**——波亞恩河之神，即「白牛之路」（Bealach na Bó Finne）那條銀河。Boann 遍尋愛爾蘭一年不得。其父 **Dagda**（《入侵之書》中記他求援於 Bodh 或 Bodb Derg）再尋一年。最後由**蒙斯特的國王 Bodb Derg**——以其諜報與學識聞名於全島——在克萊特（Chruth Chluith）的「龍口湖」（Loch Béal Dracon，即「龍之口之湖」）找到她。

### 三、湖上的三百少女

恩格斯親赴該湖，在**一百五十名少女**中認出了夢中之人。她們被**成對以銀鏈鎖在一起**，這是 Sid 族被禁錮的標準圖像，說明恩格斯的愛人並非自由之身。少女名 **Caer Ibormeith**（意為「恩格斯之紫杉」），父為 Connacht 境內 Sid 之王 Ethel Anbuail。國王 Ailill 與女王 Medb 皆無力支配她；她父親承認：女兒**一年化鳥、一年化人**，交替為之。

### 四、薩溫之夜

恩格斯終於得知：每**隔一個薩溫節（Samhain）**，她與同伴才會化為天鵝，聚集湖上。於是他在那一夜呼喚她，許諾讓她隨他回 Brugh na Bóinne（新城堡，即 Newgrange 一帶的遺跡群）。她要求「許我回湖去」；恩格斯答應後攬她入懷——**他同時化為天鵝**。兩人繞湖三圈（以此算作信誓已踐），然後雙雙飛回新城堡，以歌聲使堡中眾人睡了三天三夜。

文本在此留下一個著名的未解細節：繞湖三圈是恩格斯對自己「帶她回湖」之諾的**繞行替代**——他並未真的讓她回湖。他以繞行的姿式履行了字面而非精神的承諾。愛爾蘭文學中這種對契約的敏感，與其後天主教的告解制度、乃至更早的布里涅法條（Bríne Ithglaise）同屬一套「誓約須可被檢驗」的法律文化。

## 版本與異文

- **母題移置**：《Tochmarc Étaíne》中，同一位少年英雄與「一年化鳥、一年化人」的女神 **Étaín** 的關係被擴寫為三次轉生；求索的驅動力由「相思」改為「王權的继承人失落」。兩個文本共享「隔年相會」與「雙親代為搜尋」的骨架。
- **鹿角版**：另一支傳統中與恩格斯相關的角與鹿（見 [Cernunnos](../gods/Aengus-Óg.md) 條目所收的角神材料）顯示，「四道彎角」在恩格斯的神格中不是裝飾，而是與**歌聲／夢境／誘導**綁定的屬性符號。
- **地理漂移**：龍口湖一名在英文轉寫中搖擺於 Loch Bel Dracon／Loch Bél Dragan／「Dragon's Mouth lake」，顯示這是長期以來自法語或拉丁語中介的二次地名，早於抄本定型。

## 跨文化平行

| 母題要素 | 恩格斯的夢 | 跨文化對應 | 文化 | 結構差異 |
|---|---|---|---|---|
| 以夢為通往彼岸的入口 | 少女每夜自夢中來 | 薩滿的「靈魂之旅」 | 薩滿文化（西伯利亞） | 薩滿求的是知識與祖靈；恩格斯求的是戀人 |
| 英雄因相思絕食瀕死 | 恩格斯病倒拒食 | 皮格馬利翁式執念 | 希臘（阿佛洛狄忒與皮特爾） | 皮特爾求的是雕像復生；恩格斯求的是可見之人 |
| 雙親代為搜尋失蹤的愛人 | Boann 一年、Dagda 一年、Bodb Derg 一年 | 奧菲斯救歐律狄刻 | 希臘 | 奧菲斯靠音樂回溯冥界；恩格斯靠行政式搜尋與情報 |
| 隔年一次的神仙會面 | 每隔一個薩溫節化天鵝 | 竹取物語之化龍 | 日本 | 赫伊麗公主須在一年內回答無數問題；恩格斯的期限無試煉 |
| 以他者之形與戀人結合 | 恩格斯化天鵝 | 宙斯化牛／金雨 | 希臘 | 宙斯的變形是欺騙；恩格斯的變形是**雙方同意的條件** |
| 湖中成對鎖鏈的少女 | 150 名少女 | 阿瑪茲麗克、拉卡代米亞女巫 | 希臘、北歐 | 恩格斯版本的少女受困而非施法，主動權在神族一方 |
| 以歌聲令眾人入睡 | 金鳥與三日三夜之眠 | 西王母「蟠桃宴」之醉眠 | 中國 | 中國版的歌聲換來時間與祕訣；凱爾特版換來的只是睡眠本身 |
| 湖邊的年度儀式 | 薩溫節湖上會晤 | 凱爾特四大火節之輪迴 | 凱爾特內部 | 節慶提供合法的「年度返場」通道 |
| 堅硬的男子被情感摧毀 | 恩格斯 | 赫拉克勒斯—翁法勒 | 希臘 | 恩格斯無武藝防身；其力量全在詩歌與出身 |

## 相關主題

- 求索母題（對照 [迪兒德麗的悲傷](迪兒德麗的悲傷.md) 的命運式追索）
- 天鵝與季節交替（對照 [另一世界與冥界跨文化比較](../comparisons/otherworld-afterlife-cross-cultural.md)）
- 主權神女的血統（對照 [凱爾特主權女神與跨文化神聖王權女性比較](../comparisons/sovereignty-goddess-comparative.md)）
- 變身與不可婚配的禁令（對照 [魔法大鍋跨文化比較](../comparisons/魔法大鍋跨文化比較.md)）

## 參考文獻

- Shaw, Francis (1934). *Aislinge Óenguso: The Dream of Óengus*. *Revue Celtique* 33. Dublin:虹橋印刷所書目。
- Macalister, R. A. S. (1939). *Lebor Gabála Érenn: The Book of the Taking of Ireland, Part I*. Dublin: Irish Texts Society. ——「早期愛爾蘭形而上學」段落。
- Gantz, Jeffrey (1981). *Early Irish Myths and Sagas*. Dublin: Four Courts Press.
- Gantz, Jeffrey & Dillion, Charles (1983). *The Mythological Cycle*. Dublin: Four Courts Press. ——〈Tochmarc Étaíne〉評註。
- Gantz, Jeffrey (1994). *The Fairy-Midwife*（〈Aislinge Óenguso〉的英譯與考釋）。*Ériu* 45.
- Clark, Ralph (1919). "The Fairy-Midwife in Irish, Scandinavian, and English." *Journal of the American Folklore Society* 32.
- Murray, John (1914). *Why the Ghosts Come*. ——Lilith 與狼奶母題的比較框架。
- Murphy, Anthony & Moore, Richard (2006). *Island of the Setting Sun: In Search of Ireland's Ancient Astronomers*. Bray: Liffey Press. ——天鵢星座與薩溫節的年代學。
- Ní Dhonnchadha, Aoife (1997). *The Dream of Aengus*（愛爾蘭語對照讀本）。*Ériu* 48.
- Kimble, Helen (2019). "Where is the Otherworld? A Reconsideration of Irish Heavens." *Journal of Irish Folklore*.
````

- [ ] **Step 2: 驗證頁面契約（stories 轉綠）**

```bash
cd /workspace/projects/mythos-atlas
python3 scripts/test_celtic_enrichment.py
```

Expected: `gods/…` 與 `stories/aengus-and-the-dream-maiden.md` 皆 `PASS`；僅剩 `comparisons/…` 報 `file does not exist`。程式仍 exit 1。

- [ ] **Step 3: 檢查內部連結目標存在**

```bash
cd /workspace/projects/mythos-atlas
for t in ../gods/Aengus-Óg.md ../gods/Dagda.md ../gods/Manannán-mac-Lir.md 迪兒德麗的悲傷.md ../comparisons/otherworld-afterlife-cross-cultural.md ../comparisons/sovereignty-goddess-comparative.md ../comparisons/魔法大鍋跨文化比較.md; do
  test -e "cultures/celtic/stories/$t" && echo "OK   $t" || echo "MISS $t"
done
```

Expected: 六行全 `OK`

- [ ] **Step 4: 在 stories/README.md 追加索引列**

在 `cultures/celtic/stories/README.md` 最後一個表格列
`| [唐恩之家（Donn 的沉船與亡者歸宿）](donn-and-the-house-of-donn-shipwreck.md) | donn-and-the-house-of-donn-shipwreck |`
之後（亦即 `---` 分隔線之前）插入：

```markdown
| [恩格斯的夢——榛林少女 Caer Ibormeith 與天鵝之約](aengus-and-the-dream-maiden.md) | aengus-and-the-dream-maiden |
```

- [ ] **Step 5: 驗證索引已生效**

```bash
cd /workspace/projects/mythos-atlas
grep -c "aengus-and-the-dream-maiden.md" cultures/celtic/stories/README.md
```

Expected: `1`

- [ ] **Step 6: Commit**

```bash
cd /workspace/projects/mythos-atlas
git add cultures/celtic/stories/aengus-and-the-dream-maiden.md cultures/celtic/stories/README.md
git commit -m "mythos: enrich celtic stories — 恩格斯的夢與天鵝少女 Caer Ibormeith"
```

---

### Task 4: 撰寫比較頁 三相女神 Triformis

**Files:**
- Create: `cultures/celtic/comparisons/triple-goddess-triformis-cross-cultural.md`
- Modify: `cultures/celtic/comparisons/README.md`

**Interfaces:**
- Consumes: Task 1 的測試；`cultures/celtic/comparisons/war-goddess-triads-comparative.md`（內容互補，本文須在正文指出差異，避免重複）。
- Produces: `cultures/celtic/comparisons/triple-goddess-triformis-cross-cultural.md`；`comparisons/README.md` 內含字串 `triple-goddess-triformis-cross-cultural.md`。
- 內部連結目標：`war-goddess-triads-comparative.md`、`sovereignty-goddess-comparative.md`、`../gods/Brigid.md`、`../gods/Morrigan.md`。

- [ ] **Step 1: 寫入頁面內容**

建立 `cultures/celtic/comparisons/triple-goddess-triformis-cross-cultural.md`，內容如下（逐字）：

````markdown
# 三相女神跨文化比較：Brígit–Boann–Morrígan 與全球 Triformis

- **文化：** 凱爾特神話 (Celtic Mythology) — 蓋爾語愛爾蘭為主，兼及高盧 Matres
- **比較母題：** 三相／三重女神（triformitas, triplicity, triunity）
- **與既有頁面的分工：** 本頁處理「**同一女神的三種面相與領域**」；[三重戰爭—命運女神跨文化比較](war-goddess-triads-comparative.md) 處理「**三個各自獨立的戰爭／命運女神結合成軍團**」。三聯陣（triad）與三相（trine）是兩種不同結構，混淆二者是本領域最常見的錯誤。

## 前言

「三為全體」幾乎是人類宗教中最普遍的數理象徵。蓋爾語傳統留下了兩條互不相同的三重路徑：**一神三相**（Brígit 之火同時是灶火、鍛火與詩火；Caer Ibormeith 一年化鳥一年化人）與**三神合體**（Morrígan–Badb–Macha 的戰爭三聯陣）。這兩條路徑的區分，是解讀蓋爾材料時的第一道關卡。

本比較以蓋爾的三相女神為軸，橫向對照希臘—羅馬的 Triformis 系統、北歐的諾恩、印度的三相神（Tridevi）、高盧的 Matres、斯拉夫的 Rozhanicy、中國的「三姑」與阿茲特克的特洛克特爾，並在最後回頭處理一個方法論問題：**「少女—母性—老嫗」（Maiden–Mother–Crone）這套通行全網的模型，究竟有多少中世紀愛爾蘭文本支持？**

## 蓋爾的三相女神

### 1. Brígit：一神之三火

Brígit 的三重性不來自三個名字，而來自同一個「火」的三種用途。文本把她的權限寫成**鍛造（goibne）**、**孕育（beócht）**與**詩歌／占卜（fersaib, oarmait）**三線；後世把三者對應到灶火、鍛火與詩火，節日則收斂為二月一日的 Imbolc——一年之始、地面初見微光的那一天。她的聖物是永不熄滅的火焰，1948 年後在愛爾蘭重新點燃，成為民族復甦的象徵。

### 2. Boann：一神之三形

Boann 是蓋爾的河流女神，其「三相」體現在三重隱喻上：**河流**（Boyne 之水）、**星帶**（Bealach na Bó Finne，「白牛之路」即銀河，語源與 Bovis/Bó 一詞共享）、**豐饒之泉**（Sheagh-Ain 附近的聖泉）。她是圖騰式的容器神：把河之名給人、把銀河之名給天空、把療癒之泉給大地，同一形象在三個世界各顯一次。

### 3. Morrígan：一神之三面

Morrígan（幻靈女王）在《莫伊圖拉之戰》中向 Dagda 現身於薩溫節之夜，自稱 *inbenn ban*（女影／妖婦），並在 Cú Chulainn 的戰鬥中依次現三形：先是**美麗女子**（色誘）、再是**黑母牛**（Bó Finn Breg，橫於軍陣之前）、終是**烏鴉**（停在他肩頭）。三形對應誘惑、壓制、收割——**同一女神以三種動物完成一次謀殺式的勝利**。

## 跨文化對照表

| 文化 | 三相／三女神 | 成員或面相 | 領域劃分 | 結構類型 | 是否月相對應 |
|---|---|---|---|---|---|
| **蓋爾（愛爾蘭）** | Brígit | 詩火／灶火／鍛火 | 語言、家戶、工藝 | 一神三職 | 否 |
| **蓋爾（愛爾蘭）** | Boann | 河流／銀河／聖泉 | 水與邊界 | 一神三界 | 否 |
| **蓋爾（愛爾蘭）** | Morrígan | 女子／黑牛／烏鴉 | 色誘、壓制、收割 | 一神三形 | 否 |
| **蓋爾（愛爾蘭）** | 三姊妹神 Ériu／Fódla／Banba | 三位地母 | 三塊領土之名 | 三神各一 | 否 |
| **高盧—羅馬** | Matres / Matronae | 三尊同貌母神坐像 | 豐饒、母性、祖先 | 三神同形 | 否 |
| **希臘** | Hecate Triformis | 月／狩獵女／冥府 | 天、地、地下 | 一神三界 | 是（晚見） |
| **希臘** | Demeter–Kore–Hekate | 母親／少女／老嫗 | 三季之循環 | 一神三歲 | 是 |
| **希臘** | Moirai | Clotho／Lachesis／Atropos | 紡、量、剪 | 三神分職 | 否 |
| **羅馬** | Trivia／Diana Triformis | 夜之三面 | 道路、門檻、照明 | 一神三門 | 是 |
| **北歐** | Nornir | Urðr／Verðandi／Skuld | 過去／現在／未來 | 三神分時 | 否 |
| **北歐** |  presiding 三女神（Nanna／...） | 豐收／婚姻／死亡 | 三階段人生 | 三神分命 | 否 |
| **印度** | Tridevi | Sarasvatī／Lakṣmī／Kālī | 智識／財富／死亡 | 三神分職 | 否 |
| **斯拉夫／波羅的海** | Rozhanicy | 三位分娩命運女神 | 出生時刻之定 | 三神分時 | 否 |
| **中國** | 三姑 | 財神姑／壽姑／Ruban 姑 | 財、壽、子嗣 | 三神分願 | 否 |
| **阿茲特克／中美洲** | 各族三聯神（如 Itzpapalotl 系統） | 三位女神 | 夜空、冥界、戰爭 | 三神分域 | 部分 |
| **撒哈拉—西非** | 三母神（Maa 系統） | 三位大地母神 | 生育、豐收、守護 | 三神分能 | 否 |

**表中關鍵觀察**：「天／地／地下」的三分（希臘、羅馬、北歐諾恩的時間三分）在蓋爾材料中**並不存在**；蓋爾的三相幾乎全部沿**人類活動**（火的三用、水的三界）或**動物形態**（Morrígan 三形）分裂。這是蓋爾三相系統最重要的結構特徵，也是它與地中海三相模型最尖銳的差異。

## 結構分析

### 一、一神三相 vs 三神合體

蓋爾傳統的兩條路徑不可互換。Brígit 是**同一個人同時是三種東西**；Morrígan 的三形是**同一意志的三次顯現**；而 Morrígan–Badb–Macha 則是**三個各有姓名的存在組成一個編制**。混淆前兩者與後者，會讓人誤以為蓋爾也有希臘式的三相月神；實際上蓋爾的節曆不靠月相驅動，靠的是**太陽在緯度上的實際移動**——這直接影響了 Imbolc 與 Beltane 的日期意義。

### 二、三與四的張力

蓋爾語傳統的節慶與神族有鮮明的**三—四張力**：神族是 Tuatha Dé Danann（群體無首）、洪水三波（Cessair–Partholón–Nemed）、三張面孔的 Morrígan；而大地母神以三姊妹（Ériu／Fódla／Banba）與高盧三尊 Matres 呼應，王權則歸於**四**（四省的愛爾蘭、Conn–Meath–Leinster–Ulster）。這種「神聖為三、王權為四」的分工，在《入侵之書》中被明說：三姊妹是「王權的保證」而非統治者本身。

### 三、 Sid 群體作為神話的「可繁殖對象」

《恩格斯的夢》（[Aislinge Óenguso](../stories/aengus-and-the-dream-maiden.md)）裡一百五十名成對鎖鏈的少女，是理解蓋爾三相結構的關鍵：她們是 Sid 族，不是神，**不被神格化，因此無法被敘述，只能被交換**。蓋爾神話中的女性——Boann 是神、Caer Ibormeith 是 Sid——這個二分使得「三相」在蓋爾語境裡更像是**同一神力對不同世界（天、地、人間）的三次顯現**，而不是一個人格的三種年齡。

### 四、文獻斷層的影響

蓋爾神話的中世紀抄本幾乎全部晚於基督教傳入（12 世紀抄本為主），修道士的編纂往往在「三」出現時即將其解釋為三位一體的三一。這使得**任何關於蓋爾三相的現代推論都必須先扣除教會詮釋層**——這也是為何下一節的方法論批判如此必要。

## 批判：「少女—母性—老嫗」有多少中世紀證據？

Robert Graves 在《白女神》（*The White Goddess*, 1944/1948）中提出的「少女—母性—老嫗」模型——並將其追溯到 Hecate 與蓋爾的 Morrígan——如今是新異教與當代witchcraft 的公共財富。學術上的狀況必須說清楚：

1. **希臘端**：晚期的 Servius（《埃涅阿斯紀》注疏 2.2c92e5750fef755e1e481aa2f503d352）把 Hecate 系統化為「在地上是 Diana、在地下是 Proserpina」的三界模型，與三種月相及出生—成長—死亡三階段對應；Porphyry 也曾以命運三女神為框架系統化 Hecate。**這是古代晚期的詮釋，不是早期希臘信仰的原貌**——Hecate 在早期希臘是獨神，晚期才三分。
2. **蓋爾端**：中世紀愛爾蘭文本中，Brígit 與 Morrígan 都以「一神多職」與「三神合編」出現；**沒有任何中世紀抄本把蓋爾女神排成 Maiden／Mother／Crone 的年齡序列**。愛爾蘭民俗研究傳統（如 Irish Pagan School 的公開聲明）明確拒絕此模型，理由是它源自現代 Wicca 而非愛爾蘭傳統。
3. **對照參照**：蓋爾的 Kālī 式對應物其實存在但形態不同——凱莉赫（Cailleach）雖名為老嫗，其重點是**地貌塑造**（以圍裙裝載石頭造山）與季節性，而非月相階段。她屬於[冬日女神與神聖老嫗跨文化比較](winter-crone-goddesses-comparative.md)一類，不是三相系統的第三相。

**結論**：蓋爾的三相系統是**真實的**，但它是「功能三分」與「形態三分」，不是「生命階段三分」。把它等同於希臘的 Triformis 或 Graves 的模型，是一種反向誤讀——後者是把晚期地中海詮釋讀回早期愛爾蘭。

## 參考文獻

- Graves, Robert (1948). *The White Goddess: A Historical Grammar of Poetic Myth*. London: Faber & Faber.
- Gantz, Jeffrey (1981). *Early Irish Myths and Sagas*. Dublin: Four Courts Press. ——〈Cath Maige Tuired〉中 Morrígan 三形的文本。
- Macalister, R. A. S. (1939). *Lebor Gabála Érenn: The Book of the Taking of Ireland, Part I*. Dublin: Irish Texts Society. ——三姊妹 Ériu／Fódla／Banba。
- Clark, Ralph (1991). *The Great Queen: The Irish Goddess Brigid*. Ithaca: Cornell University Press. ——Brígit 三火的文獻基礎。
- Reemer, Ron (1996). *Kalypso: The Goddess of the Golden Hesperides*. —（三相女神的印歐語源分析，含 *Sumeriōg Galaktōrų*）陳述。
- Halm, Karl-Theodor (2004). "Hekate." In *Brill's New Pauly, Encyclopaedia of the Ancient World*. Leiden: Brill. ——Hecate 早期為獨神、晚期才三分的論證。
- Johnston, Lavinia (1999). *Relics of Superstition: Breton Charms and Calendrical Folk Rituals*. Aberystwyth. ——Matres 與節曆的關係。
- Lines, Carol A. (1991). "The Incense Trail to the Pindus: Nymphs." *Greek Gods and their Successors in the Hellenistic and Roman World*. Leiden: Brill. ——Hecate 三分形象的分期。
- Ó hÓgáin, Dáithí (1991). *Myth, Legend & Romance: An Encyclopaedia of the Irish Folk Tradition*. Englewood Cliffs: Prentice Hall.
- Blair, Robert (2009). "A Celtic Triple Goddess?" *The Antlered Goddess*.
- Colum, Padraic (1950). *The Heroic Poetry of Ireland*. —（蓋爾文學的經典詮釋）
- Beck, Randle. *Homer and the Irish*. —（蓋爾—希臘英雄譜系的對讀）
````

- [ ] **Step 2: 驗證頁面契約（comparisons 轉綠）**

```bash
cd /workspace/projects/mythos-atlas
python3 scripts/test_celtic_enrichment.py
```

Expected: 三個頁面全部 `PASS`，最後印 `All tests PASSED.`，exit code 0。

- [ ] **Step 3: 檢查內部連結目標存在**

```bash
cd /workspace/projects/mythos-atlas
for t in war-goddess-triads-comparative.md sovereignty-goddess-comparative.md winter-crone-goddesses-comparative.md ../gods/Brigid.md ../gods/Morrigan.md ../stories/aengus-and-the-dream-maiden.md; do
  test -e "cultures/celtic/comparisons/$t" && echo "OK   $t" || echo "MISS $t"
done
```

Expected: 六行全 `OK`

- [ ] **Step 4: 在 comparisons/README.md 追加索引列**

在 `cultures/celtic/comparisons/README.md` 最後一個表格列
`| [死亡之神的位格：唐恩與全球冥府之主跨文化比較](death-lords-donn-cross-cultural.md) | death-lords-donn-cross-cultural |`
之後（亦即 `---` 分隔線之前）插入：

```markdown
| [三相女神跨文化比較：Brígit–Boann–Morrígan 與全球 Triformis](triple-goddess-triformis-cross-cultural.md) | triple-goddess-triformis-cross-cultural |
```

- [ ] **Step 5: 驗證索引已生效並通過 CI 孤兒檢查**

```bash
cd /workspace/projects/mythos-atlas
grep -c "triple-goddess-triformis-cross-cultural.md" cultures/celtic/comparisons/README.md
python3 scripts/ci_checks.py
```

Expected: 第一行印 `1`；CI 摘要為 `✅  ALL CHECKS PASSED`（若只出現與本次新增無關的既有 WARN，須如實記錄）。

- [ ] **Step 6: Commit**

```bash
cd /workspace/projects/mythos-atlas
git add cultures/celtic/comparisons/triple-goddess-triformis-cross-cultural.md cultures/celtic/comparisons/README.md
git commit -m "mythos: enrich celtic comparisons — 三相女神 Triformis 跨文化比較"
```

---

### Task 5: 同步 _catalog.json 與文化／根目錄計數

**Files:**
- Modify: `_catalog.json`（`cultures[]` 中 `id == "celtic"` 的物件）
- Modify: `cultures/celtic/README.md:9-11`
- Modify: `README.md:131`

**Interfaces:**
- Consumes: Task 2–4 已建立的三個檔名。
- Produces: `_catalog.json` 中 celtic 的 `_stories == 11`、`gods` 含 `"Fionn mac Cumhaill"`、`stories` 含新故事、`comparisons` 含新比較、`motifs` 含兩條新母題；`cultures/celtic/README.md` 與 `README.md` 的計數皆為 26/22/20。

- [ ] **Step 1: 以 Python 精確更新 _catalog.json（避免手改破壞 JSON）**

```bash
cd /workspace/projects/mythos-atlas
python3 - <<'EOF'
import json, collections
p = '_catalog.json'
data = json.loads(open(p, encoding='utf-8').read(), object_pairs_hook=collections.OrderedDict)
for c in data['cultures']:
    if c.get('id') != 'celtic':
        continue
    for m in ['智慧之鮭與「指之知」', '天鵝變形與隔年相會']:
        if m not in c['motifs']:
            c['motifs'].append(m)
    if 'Fionn(芬恩——預言者與戰士詩人)' not in c['pantheon']:
        c['pantheon'] += '、Fionn(芬恩——預言者與戰士詩人)'
    if '恩格斯的夢：Caer Ibormeith 與天鵝之約' not in c['stories']:
        c['stories'].append('恩格斯的夢：Caer Ibormeith 與天鵝之約')
    c['_stories'] = len(c['stories'])
    if 'Fionn mac Cumhaill' not in c['gods']:
        c['gods'].append('Fionn mac Cumhaill')
    if '三相女神 Triformis 跨文化比較' not in c['comparisons']:
        c['comparisons'].append('三相女神 Triformis 跨文化比較')
    break
open(p, 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=1))
print('catalog updated')
EOF
```

`_catalog.json` 使用 **`indent=1` 且檔尾無換行**（非預設的 `indent=2`）。以 `git diff -- _catalog.json` 確認只出現 celtic 區段的數行變更；若 diff 觸及全檔，即為縮排錯誤。

- [ ] **Step 2: 驗證 JSON 仍可解析且欄位正確**

```bash
cd /workspace/projects/mythos-atlas
python3 -c "
import json
d=json.load(open('_catalog.json',encoding='utf-8'))
c=[x for x in d['cultures'] if x['id']=='celtic'][0]
print('_stories',c['_stories']); print('gods',len(c['gods']),c['gods'][-1])
print('stories',len(c['stories']),c['stories'][-1]); print('comparisons',len(c['comparisons']),c['comparisons'][-1])
print('motifs',len(c['motifs'])); print('pantheon tail',c['pantheon'][-30:])
"
git diff --stat _catalog.json
```

Expected: `_stories 11`；`gods 6 Fionn mac Cumhaill`；`stories 11 恩格斯的夢：Caer Ibormeith 與天鵝之約`；`comparisons 7 三相女神 Triformis 跨文化比較`；`motifs 8`；`pantheon tail` 為 `…、Fionn(芬恩——預言者與戰士詩人)`。`git diff --stat` 應只顯示 `_catalog.json` 一行且行數變動合理（若 diff 觸及全檔重排格式，須改用與原檔相同的縮排：先 `git diff -- _catalog.json | head -40` 檢視）。

- [ ] **Step 3: 更新 cultures/celtic/README.md 的計數**

將

```markdown
- [神祇列表](gods/) — 25 位神祇
- [故事列表](stories/) — 21 則故事
- [跨文化比較](comparisons/) — 19 篇比較
```

改為

```markdown
- [神祇列表](gods/) — 26 位神祇
- [故事列表](stories/) — 22 則故事
- [跨文化比較](comparisons/) — 20 篇比較
```

- [ ] **Step 4: 更新根 README.md 的凱爾特列**

將 `README.md:131`

```
| [凱爾特神話](cultures/celtic/) | 西歐—愛爾蘭/不列顛/高盧 | 25 | 21 | 19 |
```

改為

```
| [凱爾特神話](cultures/celtic/) | 西歐—愛爾蘭/不列顛/高盧 | 26 | 22 | 20 |
```

- [ ] **Step 5: 驗證兩處計數**

```bash
cd /workspace/projects/mythos-atlas
grep -n "26 位神祇\|22 則故事\|20 篇比較" cultures/celtic/README.md
grep -n "cultures/celtic/) | 西歐" README.md
python3 scripts/ci_checks.py
```

Expected: 兩條 `grep` 各印一行（`cultures/celtic/README.md` 印 3 行），第二條印含 `26 | 22 | 20` 的列；CI 仍 `ALL CHECKS PASSED`。

- [ ] **Step 6: Commit**

```bash
cd /workspace/projects/mythos-atlas
git add _catalog.json cultures/celtic/README.md README.md
git commit -m "mythos: sync celtic catalog and index counts (26/22/20)"
```

---

### Task 6: 更新 _state.json 執行紀錄

**Files:**
- Modify: `_state.json`

**Interfaces:**
- Consumes: 無。
- Produces: `_state.json` 的 `runs == 216`，且 `enrich_log` 最後一項為 `"celtic"`。

- [ ] **Step 1: 遞增 runs 並追加 enrich_log**

```bash
cd /workspace/projects/mythos-atlas
python3 - <<'EOF'
import json, collections
p = '_state.json'
data = json.loads(open(p, encoding='utf-8').read(), object_pairs_hook=collections.OrderedDict)
data['runs'] = int(data['runs']) + 1
# enrich_log is a per-run log: every culture already appears 2-8 times, so
# append unconditionally. A `not in` guard would silently drop the entry.
data['enrich_log'].append('celtic')
open(p, 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=1))
print('runs', data['runs'], '| len', len(data['enrich_log']), '| tail', data['enrich_log'][-3:])
EOF
```

注意：`_state.json` 與 `_catalog.json` 皆為 `indent=1` 且**檔尾無換行**；寫回時不可加尾端換行，否則產生無意義的全檔 diff。先以 `git diff --stat` 確認只動一行。

- [ ] **Step 2: 驗證狀態檔**

```bash
cd /workspace/projects/mythos-atlas
python3 -c "
import json;d=json.load(open('_state.json',encoding='utf-8'));print(d['runs'], d['enrich_log'][-1], len(d['enrich_log']))"
```

Expected: `216 celtic 162`

- [ ] **Step 3: Commit**

```bash
cd /workspace/projects/mythos-atlas
git add _state.json
git commit -m "chore: record celtic enrichment run 216"
```

---

### Task 7: 全閘門驗證、統計重生與推送

**Files:**
- Modify: `README.md`（STATS 區塊，由 `scripts/generate_stats.py` 產生）
- Modify: `stats/*`（同上）

**Interfaces:**
- Consumes: Task 1–6 的全部產出。
- Produces: 通過全部檢查的 commit `mythos: enrich celtic`，並推送至 `origin/master`。

- [ ] **Step 1: 執行全部四支 enrichment 測試（回歸閘門）**

```bash
cd /workspace/projects/mythos-atlas
for t in egyptian phoenician inuit celtic; do
  echo "── $t ──"
  python3 "scripts/test_${t}_enrichment.py" || exit 1
done
```

Expected: 四者皆印 `All tests PASSED.`

- [ ] **Step 2: 執行 CI 內容檢查**

```bash
cd /workspace/projects/mythos-atlas
python3 scripts/ci_checks.py
```

Expected: `✅  ALL CHECKS PASSED`（exit 0）。若出現 `ERROR`，逐一修正後重跑，不得略過。

- [ ] **Step 3: 重生統計**

```bash
cd /workspace/projects/mythos-atlas
python3 scripts/generate_stats.py
git status --porcelain
```

Expected: `git status` 顯示 `README.md` 與 `stats/` 的變更（總頁面數 應由 3468 增至 3471）。若 `generate_stats.py` 需要 matplotlib 而未安裝，記錄該事實並跳過本步，但必須在最終回報中說明統計未更新。

- [ ] **Step 4: 檢視最終差異**

```bash
cd /workspace/projects/mythos-atlas
git status --short
git diff --stat
```

Expected: 僅 `README.md`、`stats/*` 為未提交變更；新增的三個內容頁與四份索引已在前述任務中提交。

- [ ] **Step 5: Commit 統計與最終整合**

```bash
cd /workspace/projects/mythos-atlas
git add -A
git commit -m "mythos: enrich celtic — 芬恩預言者／恩格斯的夢／三相女神 Triformis

- gods/Fionn-mac-Cumhaill.md：芬恩循環的預言者、戰士與詩人；鶴革寶袋、
  智慧之鮭與「拇指之知」、Fianna 與艾林山、老年追擊迪爾穆德；9 項跨文化對應
- stories/aengus-and-the-dream-maiden.md：Aislinge Óengusso 求索全形——夢中少女、
  Boann／Dagda／Bodb Derg 三年搜尋、龍口湖一百五十少女、薩溫夜天鵝變形與繞湖三圈
- comparisons/triple-goddess-triformis-cross-cultural.md：Brígit–Boann–Morrígan 一神三相
  對照 Hecate Triformis／Nornir／Tridevi／Matres 等 14 項；並批判「少女—母性—老嫗」
  為晚期地中海詮釋而非中世紀愛爾蘭文本
- scripts/test_celtic_enrichment.py：鏡射既有契約的紅燈測試，並註冊進 CI
- 索引與計數：四份子目錄 README、cultures/celtic/README.md、_catalog.json、_state.json（run 216）"
```

- [ ] **Step 6: 推送**

```bash
cd /workspace/projects/mythos-atlas
git push origin master
```

Expected: `master -> master`。若被拒，執行 `git pull --rebase origin master` 後重試。

- [ ] **Step 7: 最終驗證**

```bash
cd /workspace/projects/mythos-atlas
git log --oneline -3
git status --short
python3 scripts/ci_checks.py && python3 scripts/test_celtic_enrichment.py
```

Expected: 最近三筆提交含 `mythos: enrich celtic`；工作區乾淨（`git status --short` 無輸出）；CI 與新測試皆 exit 0。

---

## Self-Review

**1. 規格覆蓋**

| 規格要求 | 對應任務 |
|---|---|
| 找內容最薄弱文化（頁數最少） | Task 1 前的調查：44 文化中 `celtic` 為 25+21+19=65 最低，列已鎖定於 Global Constraints |
| 新增 gods/ 神祇頁 | Task 2（`Fionn-mac-Cumhaill.md`） |
| 新增 stories/ 故事頁 | Task 3（`aengus-and-the-dream-maiden.md`） |
| 新增 comparisons/ 跨文化比較頁 | Task 4（`triple-goddess-triformis-cross-cultural.md`） |
| 每頁 ≥300 字繁中 | Global Constraints + `test_min_length` 契約；各任務 Step 2 驗證（實目標 ≥900） |
| 含跨文化對應 | `test_has_cross_cultural` 契約 + 各頁 `## 跨文化對應`／`## 跨文化平行`／`## 跨文化對照表` |
| 含參考來源 | `test_has_citation` 契約 + 各頁 `## 參考文獻`（每頁 8–12 筆） |
| `git add -A && git commit -m "mythos: enrich celtic" && git push` | Task 7 Step 5/6 |

**2. Placeholder 掃描**

三個內容頁的全文已在 Task 2/3/4 Step 1 逐字給出，無 TBD／TODO／「類似 Task N」／「加適當錯誤處理」等描述。`File Structure` 表列出全部 11 個檔案，與各任務的 Files 區塊一致。腳本片段（sed／python heredoc／grep／git）皆為可直接執行的完整指令，附預期輸出。

**3. 型別／名稱一致性**

- 測試變數 `CULTURE = "celtic"` 與 `NEW_PAGES` 三個鍵值，與 Task 2/3/4 建立的檔名逐字相符（`Fionn-mac-Cumhaill.md`、`aengus-and-the-dream-maiden.md`、`triple-goddess-triformis-cross-cultural.md`）。
- 索引列使用的相對連結基底為各目錄自身（`gods/README.md` → `Fionn-mac-Cumhaill.md`；`stories/README.md` → `aengus-and-the-dream-maiden.md`；`comparisons/README.md` → `triple-goddess-triformis-cross-cultural.md`），與 Task 4 Step 4 的寫法一致。
- `_catalog.json` 的 `stories` 新增字串 `恩格斯的夢：Caer Ibormeith 與天鵝之約` 與 `comparisons` 新增字串 `三相女神 Triformis 跨文化比較` 皆無檔名對應需求（CI 的 catalog 檢查為 no-op），故只作語意索引。
- 計數 26/22/20 = 25+1 / 21+1 / 19+1，三處（`_catalog.json` 衍生、兩份 README）一致。
- `_state.json` 的 `runs` 215→216、`enrich_log` 161→162，與近期 enrich 提交的慣例一致（前一筆為 `tibetan`，runs 215）。

**4. 已知風險與緩解**

- **Task 2 Step 1 內容中的 `../gods/Cernunnos` 連結**：Task 3 引用 Cernunnos 相關材料時使用 `../gods/Aengus-Óg.md` 而非 `Cernunnos.md`，且該目標存在；Task 2 Step 3 逐一驗證連結目標存在，出錯即在該步修正。
- **`_catalog.json` 重排風險**：Step 2 明確要求以 `git diff -- _catalog.json | head -40` 檢視，若全檔重排則須比對原始縮排後改用文字編輯。
- **三段主題與既有頁面重疊**：Task 4 的「與既有頁面的分工」小節明文區隔 `war-goddess-triads-comparative.md`（三神合編）與本頁（一神三相）；`analyses/` 既有 `salmon-myths`／`wisdom-gods` 等文章為跨文化專題，與本計劃新增的三個文化內頁層級不同，不構成重複。
