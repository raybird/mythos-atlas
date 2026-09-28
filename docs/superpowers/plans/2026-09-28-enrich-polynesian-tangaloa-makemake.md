# 波利尼西亞神話深化（湯加洛阿／馬克馬克／霍圖・馬圖阿／原初物質比較）Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 為現存最薄弱文化 `polynesian` 新增 4 頁（gods 2／stories 1／comparisons 1），每頁 ≥300 字繁體中文、含跨文化對應與可追溯參考來源，並同步所有索引、catalog 與統計後推送。

**Architecture:** 純內容型變更，與 `docs/superpowers/plans/2026-09-27-enrich-egyptian-nekhbet-apis.md` 完全同構。新頁各自承載一個尚未被本庫覆蓋的子題（東加天界神系、拉帕努伊創世神、拉帕努伊開國史、跨文化「原初物質」母題），並以一支契約測試 `scripts/test_polynesian_enrichment.py` 鏡射既有 11 支 enrichment 測試。驗證依靠 `scripts/ci_checks.py` ＋ 全部 enrichment 契約測試 ＋ `scripts/generate_stats.py`。

**Tech Stack:** Markdown（CommonMark）、Python 3.11（檢查腳本）、Git。

## 目標文化的選擇依據（可複核）

`cultures/*/{gods,stories,comparisons}` 三層頁數（各目錄 `README.md` 不計）並列最低者為 69 頁，共 7 個文化：aboriginal、dacian、hittite、minoan、polynesian、slavic、tupi-guarani。其中 hittite、minoan、slavic、tupi-guarani 已於前幾輪 enrich（見 `git log --oneline | grep enrich`），剩餘 aboriginal、dacian、polynesian。以內容量（`gods/*.md stories/*.md comparisons/*.md` 合併位元組）作次級準則：polynesian 328,335 < aboriginal 333,989 < dacian 354,995。故選 **polynesian**。另檢查內容缺口：polynesian 現存神祇全為夏威夷／大溪地／薩摩亞／庫克群島系，**拉帕努伊（Rapa Nui，復活節島）完全缺席**，東加（Tonga）僅以 `Tangaroa.md` 泛稱帶過——這是本輪的內容缺口。

## Global Constraints

- 語言：繁體中文；外文專名以括號標註（例：馬克馬克 (Makemake)）。
- 每頁正文（去除標題行、`---`、`- **欄位：**` 行）≥300 字，實際目標 ≥1,200 字（god/story ≥1,500，comparison ≥2,000）。
- 每頁必須有 `## 參考文獻`（最後一個引用區塊須有實質內容行，且行首不得為 `>`）。
- 每頁必須有 `## 跨文化…` 開頭的章節。
- H1 必須是第一個標題；標題層級不得跳級；不得有空白標題。
- 所有 `.md` 內部連結必須指向存在的檔案（已 `ls` 驗證的目標見各 Task）。
- 禁用簡體字；禁用 `populate.py`、`regenerate_all.py`。
- 新頁不得寫入 `scripts/citation_baseline.txt`。
- 同一 culture 同一目錄內，H1 括號內的英文標題不得重複（`Tangaloa` vs 既有 `Tangaroa` 不同字，须逐字确认）。
- `gods/`、`stories/`、`comparisons/` 的目錄 `README.md` 皆為 auto-generated 產物，**只手動追加一行**，不得整份重排。
- Git 訊息格式：`mythos: enrich polynesian — <中文副題>`。

## File Structure

| 檔案 | 動作 | 責任 |
|------|------|------|
| `cultures/polynesian/gods/Tangaloa（湯加洛阿）.md` | 新增 | 東加天界之主、七位同名神的分化、蚯蚓人始祖、天空王權 |
| `cultures/polynesian/gods/Makemake（馬克馬克）.md` | 新增 | 拉帕努伊創世／生育神、鳥人教派主神、紅色與鳥蛋、奧朗戈 |
| `cultures/polynesian/stories/霍圖・馬圖阿的遷徙與建國.md` | 新增 | 哈烏・馬卡的發現之夢、七人探島、雙舨遷徙、安納凱納建國、塔科納 |
| `cultures/polynesian/comparisons/蚯蚓、鳥蛋與黏土：波利尼西亞與全球的原初物質比較.md` | 新增 | 9 傳統對照表＋3 類原初物質＋4 結構分析 |
| `scripts/test_polynesian_enrichment.py` | 新增 | 本輪 4 頁的契約測試（先紅後綠） |
| `cultures/polynesian/gods/README.md` | 修改（+2 列） | 神祇索引 |
| `cultures/polynesian/stories/README.md` | 修改（+1 列） | 故事索引 |
| `cultures/polynesian/comparisons/README.md` | 修改（+1 列） | 比較索引 |
| `_catalog.json` | 修改 | `sources`／`motifs`／`pantheon`／`stories`／`gods`／`comparisons` |
| `_state.json` | 修改 | `enrich_log` 追加 `polynesian`；`runs` 224→225 |
| `README.md`、`stats/index.md` | 修改 | 由 `scripts/generate_stats.py` 產生，不得手改數字 |
| `.github/workflows/ci.yml` | 修改 | 加入本輪契約測試一行 |

`docs/` 已在 `ci_checks.py` 的排除清單，不影響檢查。

---

## Task 1: 建立契約測試（先紅）

**Files:**
- Create: `scripts/test_polynesian_enrichment.py`

**Interfaces:**
- Consumes: `scripts/test_african_enrichment.py` 的檢查函式集合（`count_body_chars`／`test_heading_hierarchy`／`test_min_length`／`test_has_citation`／`test_has_cross_cultural`／`test_indexed_in_readme`／`test_not_baselined`／`find_duplicate_english_titles`）。
- Produces: CLI 契約 `python3 scripts/test_polynesian_enrichment.py`，exit 0 綠 / exit 1 紅。

- [ ] **Step 1: 寫入測試檔**

以 `scripts/test_african_enrichment.py` 為模板逐字複製其檢查邏輯，僅改動 `CULTURE = "polynesian"` 與

```python
NEW_PAGES = {
    "gods": ["Tangaloa（湯加洛阿）.md", "Makemake（馬克馬克）.md"],
    "stories": ["霍圖・馬圖阿的遷徙與建國.md"],
    "comparisons": ["蚯蚓、鳥蛋與黏土：波利尼西亞與全球的原初物質比較.md"],
}
```

- [ ] **Step 2: 執行測試確認失敗**

Run: `python3 scripts/test_polynesian_enrichment.py`
Expected: exit 1，輸出 4 行 `[FAIL] …: file does not exist`。

## Task 2: 撰寫 `gods/Tangaloa（湯加洛阿）.md`

**Files:**
- Create: `cultures/polynesian/gods/Tangaloa（湯加洛阿）.md`
- Modify: `cultures/polynesian/gods/README.md`（+1 列）

**Interfaces:**
- Consumes: 既有 `cultures/polynesian/gods/Tangaroa.md`（泛波利尼西亞海神）作為對照；`cultures/polynesian/comparisons/sea-gods-ocean-realm-comparison.md`。
- Produces: 東加專屬神祇頁。

**必含事實（每項標出處）：**
1. **詞源與同源字**：`Tangaloa` 與 `Tangaroa`／`Tagaloa`／`Taʻaroa`／`Kanaloa` 同源；Tui Atua Tupua Tamasese Taʻisi Efi 稱 Tagaloa 為「a very important founding ancestor」，並主張所有土地與頭銜皆回溯至他（2014: 43；2009: 191）。
2. **必須明確區分**：東加 Tangaloa 是 `Langi`（天界）的統治者，非海神；海神是分出的 `Tangaloa Mana`（Moala 1994: 4）。
3. **創世分工**：Taufulifonua 成人，其姊 Havea Lolofonua 生 Hikuleʻo；Hikuleʻo 取 Pulotu（陽間），Tangaloa 取天界，Māui 取冥界；Hemoana（海蛇形）與 Lupe（鳩形）瓜分其餘，Hemoana 取海、Lupe 取陸（Gifford 1924/1929；Mariner 1819）。
4. **七位同名神**（Lafitani 2017 整理）：Tangaloa ʻEiki（天界統治者）、Tangaloa Tufunga（物質技藝／雕鑿之神，鑿出島嶼）、Tangaloa ʻAtulongolongo（使者，化为金鴿 tulī 巡島）、Tangaloa Tamapoʻuliʻalamafoa、Tangaloa ʻEitumatupuʻa（葬祭與王權，第一位 Tuʻi Tonga 之父）、Tangaloa Langi（自然力）、Tangaloa Mana（海洋）。各家族關係在來源中互相矛盾，須明言此點。
5. **島嶼生成**：Tufunga 拋下木雕碎屑，經三次試探成 ʻEua，後成 Kao、Tofua（Gifford 1924）。
6. **始祖三人**：Kohai、Koau、Momo 由 ʻAtulongolongo 銜著種子、啄斷腐根後咬開一條肥蚯蚓而生（Gifford 1924: 49）。此為本輪比較頁「原初物質」母題的錨點。
7. **王權神話**：ʻAhoʻeitu 攀 `toa`（鐵樹）上天尋父，被四位同父異母兄殺食；Tangaloa 令其兄弟吐入 kumete 碗中復活，再令兄弟四人作 Falefa 侍奉，首位 Tuʻi Tonga 由「蟲之裔」轉為「天之後裔」（Gifford 1929: 49–59；Rutherford 1977: 28；Lagaba, ANU 第三章）。
8. **`fakawai` 誓言**：以 Tangaloa 立誓為東加最高法律效力之誓言；**不得**採用未經一手文獻證實的「懲罰之浪」說法；改以 Gifford 1929 所載王權禁忌與 `moei-moei` 解咒儀式為據，並標明 `fakawai` 為當代東加語仍在使用的詞。
9. **跨文化對應表**（≥6 列）：夏威夷 Kanaloa（海）／薩摩亞 Tagaloa／大溪地 Taʻaroa（`../comparisons/creation-myths-global.md`）／阿蘇神話評述者 Craig 詞典／紐西蘭 Tangaroa-whakamautai（潮汐）＋ `Encyclopaedia.com` 所述「海洋諸形化身」／墨西哥—中部美洲神話（Ollé 2000 語境，僅作背景）。
10. **殖民除神**：歐洲捕鯨與傳教士把 Kanaloa 改寫為撒旦；東加至今無一尊 Tangaloa 木雕傳世（Lafitani 2017）。

已驗證可連結的庫內目標：`../gods/Tangaroa.md`、`../gods/Maui.md`、`../gods/Kane.md`、`../gods/Polynesian-Pantheon.md`、`../comparisons/sea-gods-ocean-realm-comparison.md`、`../comparisons/cosmogonic-genealogy-whakapapa.md`、`../stories/kava-origin.md`、`../index.md`。

- [ ] **Step 2: 把頁面加入 `gods/README.md`**（表格末列後、`---` 前）。
- [ ] **Step 3: 執行測試**（此頁 PASS，其餘 3 檔仍紅）。

## Task 3: 撰寫 `gods/Makemake（馬克馬克）.md`

**Files:**
- Create: `cultures/polynesian/gods/Makemake（馬克馬克）.md`
- Modify: `cultures/polynesian/gods/README.md`（+1 列）

**必含事實：**
1. 拉帕努伊人數之源、生育之神、鳥人教派主神；無妻（Métraux, *Ethnology of Easter Island*, 1940/1971；Wikipedia "Makemake (deity)"）。
2. 可能是波利尼西亞森林神 Tāne 的地方形式（與本庫 `../gods/Tane.md`、`../comparisons/tane-forest-god-comparative.md` 對照）。
3. 鳥人四神與四僕從：Makemake、Haua-tuʻu-take-take（蛋之長）、其妻 Vīʻe Hoa、Vīʻe Kenatea；八名（神與僕）名字由參賽者在競賽前的儀式中吟唱（Métraux 1940；mauhenua 復刻英譯）。
4. 儀式角色：`ivi atua`（具神視者，選定游向 Motu Nui 的人）、`hopu`（實際游者）、`hopu manu`（取得第一枚 `manu tara` 蛋者）、`tangata manu`（由贊助者宣告，非游者本人）（Englert 1948；Wikipedia "Tangata manu"）。
5. 賽制地理：Motu Nui、Motu Roa、Motu Iti 三座小島、Nuku 海峽 300 呎高崖、Rano Kau 火山口、Orongo 村；東側氏族（`miru`）經 Rano Raraku，西側經 Anakena。
6. 紅色與月經：Makemake 與 Tiki 的關係爭議；Rjabchikov 指出創世頌中的「胎盤之血」與 `tiko`（月經）同詞，創世主名為 Tiki，Makemake 為其地方形式；紅色（`mea`）為其象徵，島上曾誤讀島民將「十字」記號解作 Makemake（Thomson 1891: 517）。
7. Haua 為其固定伴神，獻祭公式必含 Haua（Métraux 1940）。
8. 庫內連結：`../gods/Tane.md`、`../gods/Hine-nui-te-po.md`、`../gods/Tangaroa.md`、`../comparisons/navigation-mythology.md`、`../comparisons/creation-myths-global.md`、`../stories/霍圖・馬圖阿的遷徙與建國.md`、`../index.md`。

## Task 4: 撰寫 `stories/霍圖・馬圖阿的遷徙與建國.md`

**Files:**
- Create: `cultures/polynesian/stories/霍圖・馬圖阿的遷徙與建國.md`
- Modify: `cultures/polynesian/stories/README.md`（+1 列）

**必含情節節點（Barthel 1978 *The Eighth Land* 版本為骨架）:**
1. 緣起：哈烏・馬卡（Hau Maka，刺青師／占卜者）之夢遊三小島與 Rano Kau 火山口，逆時針繞島命名二十八處，含 Anakena、Papa o Pea、Ahu Akapu（夏威夷大學 pvs 站 Barthel 摘要）。
2. 七人探島：霍圖命其子 Ira、Raparenga 與 Hua Tava 的五子 Kuukuu、Lingiringi、Nonoma、Uure、Makoi 造舨 `Oraora-ngaru`／`Te Oraora-miro`；Vaitu Nui 第二十五日（四月）啟航，Maro 初一（六月）抵達，五週航程。
3. 命名與職掌分工：Makoi 標記命名，Kuukuu 負責耕作並於 Rano Kau 種芋；Maro 第十日登 Rano Kau；Anakena 第五日繞島。
4. 遷徙原因兩說：父臨終囑「潮水淹地」（Barthel）；Routledge 1919: 277 記為王位繼承戰敗。
5. 主航：Nuku Kehu 造雙體舨，Hora Nui 第二日（九月）啟航，Tangaroa Uri 第十五日（十月）抵達西南，六週；兩舨分道，霍圖走南東、五處漁場由 Honga 的 mana 建立；Hineriru 走西北北、九處漁場由 Teke；霍圖以 `Ka hakamau te konekone!`（「停下划槳！」）使己舟加速、對手滯後，先抵 Hiramoko 海灘（Helulf 版本）。
6. 出生與臍帶禮：長子 Tuʻu Maheke 生於 Hiramoko，Tuʻu Ko Iho 舟上生 Ava Rei Pua Poki；`Vaka`（臍帶禮主持者）依次行之。
7. 拆舟為屋、分苗、Hs／long ears 與 short ears 兩支後裔分居東西部（Routledge 1919: 281）。
8. 奧羅伊的暗藏乘客：殺死霍圖子女的宿敵藏於遷徙舟中，於 Anakena 潛上岸（風險情節）。
9. 死亡與鳥人祭：霍圖最後移居 Rano Kau 火山口南緣、對面即 Orongo；臨終呼喚守護神 Kuihi 與 Kuaha，雞鳴聲自 Hiva 傳來，遂倒地而亡。**須明確標註**：其遺體去向與後世「鳥人（`takona`）」祭的關聯屬後世推論，19 世紀文獻中鳥人賽事與霍圖的關聯有爭議（Métraux 1940: 313–4；Jenkins 1918；Barros 1998）。
10. 學界注意：霍圖・馬圖阿之名近似 Mangarevan 創世神 `Atu Motua`，部分學者認為此名於 1860 年代隨 Mangarevan 語一併進入（Wikipedia "Hotu Matua" 引述）；語言學、DNA、孢粉分析大致支持 300–800 CE 的波利尼西亞定殖（Skjøltoft 2019；NOVA/PBS 2000）。
11. **跨文化平行**：① 拓殖的夢兆指引（毛利 Kupe／Hine 訪 Aotearoa 的夢、瑞典 Gustav Vasa 依預言出海、威克里夫 14 世紀航行的「templar/mission」記載）② 開國之王的遷徙（夏威夷 `ʻĀloha ʻĀkea` 航海谱系）③ 創始者被殺與祖先聖地（`Hokū` 比較另述）④ 數百人的集體拓殖（`Routledge` 的「數百人」說與秘魯編年史的移民潮）——須以 `../comparisons/navigation-mythology.md` 與 `../comparisons/flood-myths-polynesian-global.md` 作內部連結。

## Task 5: 撰寫 `comparisons/蚯蚓、鳥蛋與黏土：波利尼西亞與全球的原初物質比較.md`

**Files:**
- Create: `cultures/polynesian/comparisons/蚯蚓、鳥蛋與黏土：波利尼西亞與全球的原初物質比較.md`
- Modify: `cultures/polynesian/comparisons/README.md`（+1 列）

- [ ] **Step 1: 撰寫頁面**（目標 ≥2,000 字）

九傳統對照表，欄位：文化／原初物質／人類如何被造／神自己的身體如何被用／死亡與腐敗的關聯／出處：
1. **東加（Tonga）** — 肥蚯蚓 → 三始祖 Kohai／Koau／Momo（Gifford 1924: 49）
2. **拉帕努伊** — 鳥蛋（`manu tara` 蛋）＋紅色／月經之血（Thomson 1891: 517；Rjabchikov 1996b）
3. **大溪地／庫克群島** — 卵（`../comparisons/creation-myths-global.md` 已載 Taʻaroa 敲破卵殼）
4. **毛利／因紐特** — 地潛者取土；自動存在由心念與言說生成（`../comparisons/cosmogonic-genealogy-whakapapa.md`；`cultures/inuit/comparisons/earth-diver-creation-comparative.md`）
5. **埃及** — Khepera 集合肢體、以淚造男女（Budge, *Legends of the Gods*）；Heracleopolis 的「蛆王」與 Khepri 的蛆形認同（Budge, *The Gods of the Egyptians*, 1904）；奧西里斯遺體生 Kheperi
6. **印度** — 婆樓那金胎（*Ṛgveda* 10.121；`cultures/hindu/gods/梵天.md`）與人牲（Purusha）自我分解為宇宙
7. **北歐** — 巨人 Ymir 屍體化生大地、其血成海（`Grímnismál` 13–14；`Gylfaginning`；庫內 `cultures/norse/gods/` 無 Ymir 頁，改以 `cultures/norse/comparisons/` 之創世比較連結）
8. **中國** — 女媧摶黃土造人（`cultures/chinese/gods/女媧.md`）
9. **安第斯（印加）** — Viracocha 以黏土造人於海岸，風災後自山中再造（`cultures/incan/gods/Viracocha.md`）

三類原初物質：**A 腐敗物與小動物**（蚯蚓、蛆）／**B 生殖與血**（卵、經血、胎盤血）／**C 泥土與屍體**（黏土、黃土、神與巨人的屍體）。

四結構分析：① **邊界物質**——最卑賤的腐敗物反而承載神性（東加的蟲裔被王權神話貶抑、卻是全體人民之祖；埃及 Kheperi 同理）；② **材料與社會價值的反比**——被貶低者作材料，須以儀式（東加吐入 `kumete` 碗、埃及的腐爛奧西里斯）翻轉；③ **造人材料的一致性**——黏土（女媧、Viracocha）與淚（Khepera）顯示「人由可塑性材料成」，與波利尼西亞「人由已死之物成」構成海洋／大陸的環境分野（島嶼缺乏黏土、土壤薄）；④ **地理決定神學**——島嶼社會缺少可塑性材料，故以腐敗物、血、骨為材料，並發展出「取回型」而非「塑造型」創世（連結 `cultures/inuit/comparisons/earth-diver-creation-comparative.md`）。

- [ ] **Step 2: 加入 `comparisons/README.md`**。
- [ ] **Step 3: 執行測試確認全綠。**

## Task 6: 索引、catalog、統計同步

- [ ] **Step 1: `gods/README.md` 加 2 列、`stories/README.md` 加 1 列、`comparisons/README.md` 加 1 列**（皆在 `---` 前追加）。
- [ ] **Step 2: 更新 `_catalog.json` 的 polynesian 條目**：`sources` 補 `Gifford《Tongan Myths and Tales》(BPB Bulletin 8, 1924)`、`Barthel《The Eighth Land》(1978)`、`Métraux《Ethnology of Easter Island》(1940/1971)`、`Cramer《Dictionary of Polynesian Mythology》(1989)`；`motifs` 補 `天界王權與神聖後裔(Tuʻi Tonga)`、`拉帕努伊鳥人祭(tangata manu)`、`原初物質：蚯蚓與鳥蛋`；`pantheon` 補 `Tangaloa（東加天界）`、`Makemake（拉帕努伊創世神）`；`stories` 補 `霍圖・馬圖阿的遷徙與建國`；`gods` 補 `湯加洛阿 (Tangaloa)`、`馬克馬克 (Makemake)`；`comparisons` 補 `原初物質跨文化比較`。驗證 `python3 -c "import json;json.load(open('_catalog.json'))"`。
- [ ] **Step 3: `python3 scripts/generate_stats.py`**（以腳本輸出為準，不手改數字）。
- [ ] **Step 4: `_state.json` 追加 `"polynesian"`、`runs` 224→225**，並驗證可解析。
- [ ] **Step 5: `.github/workflows/ci.yml` 加入 `python scripts/test_polynesian_enrichment.py`。**

## Task 7: 全面驗證、提交、推送

```bash
python3 scripts/ci_checks.py
python3 scripts/test_polynesian_enrichment.py
for f in scripts/test_*_enrichment.py; do python3 "$f" >/dev/null || echo "FAIL $f"; done
git add -A
git commit -m "mythos: enrich polynesian — 湯加洛阿／馬克馬克／霍圖・馬圖阿遷徙建國／原初物質比較"
git push
```

## Self-Review

1. **規格覆蓋**：(a) 找最薄弱文化（上方可複核的兩層量測 ＋ 拉帕努伊缺口）；(b) 新增 gods／stories／comparisons，每頁 ≥300 字含跨文化對應與來源（Task 2–5，契約測試強制）；(c) `git add -A && git commit -m "mythos: enrich <culture-name>" && git push`（Task 7）；(d) 回報新增內容。全數對應。
2. **無佔位符**：每頁以具體出處（Gifford 1924: 49；Budge *Legends of the Gods*；Barthel 1978；Métraux 1940；Cramer 1989 等）逐點指定。
3. **名稱一致性**：`NEW_PAGES` 四個檔名與 Task 2–5 完全一致；`_catalog.json` 與三份目錄 README 的名稱與檔名一致；統計一律交由 `generate_stats.py`。
4. **風險登記**：
   - `Tangaloa` vs 既有 `Tangaroa.md` 的 H1 英文標題不同字，須以 `find_duplicate_english_titles` 驗證不誤判（大小寫正規化後 `tangaloa` ≠ `tangaroa`）。
   - 東加 `fakawai` 的「懲罰之浪」說法未獲一手文獻支持，**不寫入**。
   - 霍圖・馬圖阿與鳥人祭的關聯、後世 Mani 語源說皆為學界爭議，頁內須標明層級。
   - 檔名含全形括號與全形冒號，README 連結須逐字一致。
