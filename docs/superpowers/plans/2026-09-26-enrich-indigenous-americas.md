# Indigenous American Mythologies Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 深化美洲原住民神話（indigenous-americas）——把 6 個殘留的模板空殼頁改寫為有實質神話學內容的頁面，並新增 gods/、stories/、comparisons/ 各一頁，全部 ≥300 繁中字、含跨文化對應與參考文獻，頁數 70 → 73。

**Architecture:** 選題以「內容深度」而非僅頁數為第一原則。以 `wc -m` 掃描全庫 46 文化的 gods/stories/comparisons 最小檔案後，indigenous-americas 是**唯一仍留有 6 個未深化空殼**的文化（其餘 70 頁文化只剩 README 空殼）：

| 檔案 | 現有字元 | 處置 |
|---|---|---|
| `comparisons/大洪水世界重建.md` | 227 | 改寫 |
| `gods/雷鳥.md` | 317 | 改寫 |
| `stories/雙子英雄.md` | 342 | 改寫 |
| `stories/Coyote與眾神.md` | 348 | 改寫 |
| `gods/White-Buffalo-Calf-Woman.md` | 365 | 改寫 |
| `stories/白水牛女送七儀式.md` | 366 | 改寫 |

三個**新增**頁目經 `grep -ril` 全庫確認為真空母題／缺位：

- `gods/Masauwu.md` — 霍皮族「骨架人」Masauwu／Maasaw：死亡之神、大地之神、第四世界之主、第五世界門守與火的守護者、四塊石板的賦予者。現有 `gods/Tawa.md`、`gods/蜘蛛祖母.md`、`stories/hopi-four-worlds-emergence.md` 都直接引用 Masauwu，卻無專頁（神祇層缺位）。
- `stories/mink-woman-and-thunder-man.md` — 黑腳族貂女（Mink Woman）與 Thunder Man 的天界聯姻敘事：公牛皮柳條籃、單股長牛皮繩自天界垂下。本文化**完全沒有太平洋西北文化層**（23 個故事頁全部是平原／西南／東部）。
- `comparisons/twin-hero-motif-cross-cultural.md` — 「雙子英雄」母題跨文化比較。既有 `comparisons/` 19 頁（變形者、湧現神話、騙子神、聖山…）皆未處理雙子母題；北美雙子母題本身在北美與中美洲密度極高（納瓦荷、Arikara、Creek、Skidi Pawnee、Yuma、Winnebago、易洛魁、Pueblo、瑪雅），是全庫真空對照。

**Tech Stack:** Markdown、Python 3（`scripts/ci_checks.py` 字數／引用／孤兒檔檢查、`scripts/generate_stats.py` 統計）、Git（commit+push）。

## Global Constraints

- 每頁 ≥300 繁中字（以 `[\u4e00-\u9fff]` 正則計數）、單一 H1、標題層級不跳階（`#` → `##` → `###`）、`## 參考文獻` 為尾段且非空。
- 引用可稽核：原住民側必須指名可查的具名來源（Swanton《Haida Texts and Myths》1915、Emmons《Tlingit Myths and Texts》1915、Mooney《Myths of the Cherokee》1900、Wissler & Duvall《Mythology of the Blackfoot Indians》1908、Grinnell《Blackfoot Lodge Tales》1892、McLaughlin《Myths and Legends of the Sioux》1916、Brown《The Sacred Pipe》1953、Walker「The Religious Cults of the Sioux」1914、Malotki《Hopi Tales》1979、Courlander《The Fourth World of the Hopis》1971、Barrett「A Composite Myth of the Pomo Indians」JAFL 1908、Emmons「The Haida Indians」AMNH 1915）；非美洲文明側須用可指名文本（《古事記》、Rigveda 1.116–119 Aśvins、Apollonius Rhodius《Argonautica》、Pliny《自然史》10.84、Grimm KHM、Popol Vuh、Proclus《Elements of Theology》、Geertz 1996、Pritzker《Hopi Creation Myth》、Jung《Man and His Symbols》），不得憑空捏造文獻。
- 尊重文化敏感度：Pantheon 頁禁止以「某種泛文化神話學」抹平差異；涉及當代美洲原住民（Lakota 煙斗守護者 Arvol Looking Horse、納瓦荷考古學者 T. J. Tsosie、湯加斯數）時明確標註其為當代活傳統而非「已滅之俗」。
- CI 基準 = `scripts/ci_checks.py` 現行 **14 errors**（9 筆 orphan comparison／缺參考文獻 + 基線豁免），**不得修復、不得新增**。
- commit 訊息格式：`mythos: enrich indigenous-americas`；完成後 `git push`。
- 「三同步＋一」：gods/stories/comparisons 子 README 登錄、文化 `README.md` 計數、`_catalog.json`（pantheon/stories/gods/comparisons/_stories）、`_state.json`（runs 207→208、enrich_log）、根 `README.md` 文化列與 `stats/index.md`（`generate_stats.py` 產生）。
- 本任務為無人值守排程：不得呼叫 `question`，一律自動採用推薦選項。

---

### Task 1: 雷鳥（Thunderbird）神祇頁

- **Files:**
  - Rewrite: `cultures/indigenous-americas/gods/雷鳥.md`（現 317 字元空殼）
  - Modify: `cultures/indigenous-americas/gods/README.md`（登錄既有條目，僅補欄位格式）

- [ ] **Step 1: 確認目標檔為空殼**

Run: `wc -m cultures/indigenous-americas/gods/雷鳥.md && head -9 cultures/indigenous-americas/gods/雷鳥.md`
Expected: `317` 字元，末行 `*Generated on 2026-06-20 12:10 UTC*`

- [ ] **Step 2: 覆寫為完整條目**

必須包含的章節（依 `AGENTS.md` 方式 A 模板）：標題行 `# 雷鳥 (Thunderbird / Wakinyan Tanka)`、`- **文化：**`／`- **職掌：**` 兩個 front-matter 行、`## 概述`、`## 神格與屬性`、`## 神話事蹟`、`## 跨文化對應`（含 Markdown 表格）、`## 相關神祇`、`## 出現在`、`## 參考文獻`。

內容要點（全部須有前述來源可支撐）：

- 名號對照表：Lakota/Sioux `Wakinyan`（"神聖的飛者"）、Anishinaabe/Ojibwe `Binesí`／`Animikí`、Cree／Algonquian `Anishinaabek` 系、Iroquois `Hino`／`Oskadagea`（"露之鷹"）、Tlingit `Tlathl'aakwa`、Tsimshian `T'iista'as`、Kwakwaka'wakw `Kwunusela`、Cherokee `Ani Hyuntikwalaski`、Zuni `Shiwanna`（假面舞）。
- **形態學**：拍翅成雷、眨眼成電（Algonquian 與 Iroquois 兩系統）；Osage 型雙雷鳥；X 形／無頭 X 形圖像（Oshkosh midewiwin 圓盤 1250–1400 CE；1710 年 Mohican 酋長面部四枚雷鳥紋身；Audubon 2020 引 *American Antiquity* 密歇根 600–1600 年陶片群集）。
- **宇宙論位置**：Algonquian 中雷鳥統治上界，**水下美洲豹／有角蛇神統治下界**——雷鳥以閃電擊打下界怪獸逼其放水成雨；此「天—水」對立由 Aase Hultkrantz《Belief and Worship in Native North America》1981 稱為泛美洲宇宙組合。
- **護佑與交換條件**：護佑但索取敬意、禱告與獻禮（Audubon 訪談 Stephanie Big Eagle：以刺青作血肉獻給雷鳥）。
- **儀式位置**：Lakota `Heyoka-Wakinyan` 連結神聖小丑（見本庫 `gods/Heyoka.md`）；Anishinaabe 春季 Midewiwin 集會以初雷為訊號；Zuni 夏季 Shiwanna kachina 雨舞。
- **跨文化對照表**至少 6 列：雷鳥 ↔ 北歐 Thor（雷錘）↔ 日本 Raikō／迦楼羅 ↔ 印度 Maruts／Vajra ↔ 中美索聶米亞 An/Ziemsin ↔ 因紐特 Kidilikqerus ↔ 澳洲 Namarrkon（並註明差異：北美雷鳥是**動物形態的上界力量**，Thor 為擬人化神）。
- 端倪差異註記：不是單一「雷鳥神話」，而是從 Algonquian 到 Sioux 的一族相連概念（Barrett 2011 表述）。

- [ ] **Step 3: 驗證字數與章節**

Run: `python3 -c "import re,io; t=io.open('cultures/indigenous-americas/gods/雷鳥.md',encoding='utf-8').read(); print(len(re.findall(r'[\u4e00-\u9fff]',t)), t.count('\n# '), '參考文獻' in t)"`
Expected: 第一個數字 ≥300；第二個數字 `0`（無 H2 以上跳階）；`True`

- [ ] **Step 4: Commit**

```bash
git add cultures/indigenous-americas/gods/雷鳥.md
git commit -m "mythos: enrich indigenous-americas — 雷鳥神祇頁改寫"
```

---

### Task 2: 白水牛女（White Buffalo Calf Woman）神祇頁

- **Files:**
  - Rewrite: `cultures/indigenous-americas/gods/White-Buffalo-Calf-Woman.md`（現 365 字元空殼）

- [ ] **Step 1: 確認目標檔為空殼**

Run: `wc -m cultures/indigenous-americas/gods/White-Buffalo-Calf-Woman.md`
Expected: `365`

- [ ] **Step 2: 覆寫為完整條目**

章節：`# White Buffalo Calf Woman（Ptesáŋwiŋ）— 神聖女人、煙斗與七聖禮的贈予者`、front-matter（文化／職掌）、`## 概述`、`## 神格與屬性`、`## 神話事蹟`、`## 跨文化對應`（表格）、`## 相關神祇`、`## 出現在`、`## 參考文獻`。

內容要點：

- 名號與形態：Lakȟótiyapi `Ptesáŋwiŋ`；Blackfoot 說法作 **Whope**（Lakota 語，見 Walker 1914 逐字記錄）；亦見 Falling Star、Wanbli Wacinyapin 等異名。四日駐留、四度變色（黑→赤→褐／棕→白）、向四方低頭後消失於丘後。
- 兩獵人考驗結構：貪慾者觸摸即被雲吞沒化為白骨（蛇群啃食），潔淨者被遣回報信（McLaughlin 1916；Walker 1914 兩本細節互異，需並列）。
- 教的內容：`čhaŋnúŋpa`／`caŋuŋpa` 石斗煙斗；碗為紅黏土（catlinite）刻小牛＝大地與四足獸；桿為木＝地上生長之物；十二支斑尾鷹羽＝空中有翼者；**一枚與碗同石的圓石＝大地**（Brown《The Sacred Pipe》1953 全段引文）。教誨句「你以此煙斗祈禱，就是為萬物同禱」。
- 七聖禮清單（拉科塔七項）：`Inípi`、`Haŋbléčheyapi`、`Wiwáŋyaŋg Wačhípi`（太陽舞）、`Huŋkalowaŋpi`（結親）、`Išnáthi Awíčhalowaŋpi`（女子初經禮）、`Tȟápa Waŋkáyeyapi`（拋球）、`Wanáǧi Yuhápi`（守魂）。
- 傳承與當代：煙斗由一位聖者世代保管；Arvol Looking Horse 為第 19 任守管者（Yvonne Wakim Dennis 等書）；與 Dennis 等「第七代」復興論述連結。
- 象徵與神學意義：4 與 7 的神聖數（見本庫 `analyses/sacred-numbers-*`）；紅石碗＝子宮、木桿＝男性（Zimmerman 解釋）；**對婦女暴力的神聖制裁**——「凡懷惡意注視者化為塵土」（Winds of the 洞，Washu Niya，「動物進入世界之地」）。
- 跨文化對照表至少 6 列：神聖女人贈予文化器物 ↔ 希臘 Prometheus／希伯來 Moses ↔ 毛利 Tāwhaki 從天階取火種 ↔ 印加 Viracocha 給 Manco Capac 十誠法 ↔ 非洲 Mami Wata 贈物 ↔ 北極 Napi 授人以火鑽與植物知識（Glenbow 傳統故事頁「Katoyissa / Napi」條目佐證）↔ 印度 Prajāpati 造人並賦命。
- 爭議註記：本頁為拉科塔／黑腳族活傳統，1930–1970 年間曾被非原住民「靈性運動」挪用並把「七聖禮」商業化；此段須明寫以免頁面成為靈性消費文本（對應本庫 `comparisons/sacred-pipe-cross-cultural.md`）。

- [ ] **Step 3: 驗證字數與章節**

Run: `python3 -c "import re,io; t=io.open('cultures/indigenous-americas/gods/White-Buffalo-Calf-Woman.md',encoding='utf-8').read(); print(len(re.findall(r'[\u4e00-\u9fff]',t)), '參考文獻' in t)"`
Expected: `>=300 True`

- [ ] **Step 4: Commit**

```bash
git add cultures/indigenous-americas/gods/White-Buffalo-Calf-Woman.md
git commit -m "mythos: enrich indigenous-americas — 白水牛女神祇頁改寫"
```

---

### Task 3: 莫索烏（Masauwu）神祇頁 — 新增

- **Files:**
  - Create: `cultures/indigenous-americas/gods/Masauwu.md`
  - Modify: `cultures/indigenous-americas/gods/README.md`（新增一列）

- [ ] **Step 1: 確認全庫無 Masauwu 專頁**

Run: `ls cultures/*/gods/ | grep -i -c masauwu; grep -ril "masauwu" cultures/indigenous-americas/gods/ | wc -l`
Expected: `0`；第二個數字 ≥1（證明「被引用但無專頁」的缺位）

- [ ] **Step 2: 建立頁面**

章節：`# 莫索烏 (Masauwu / Maasaw) — 霍皮族的死亡之神、大地之神與第五世界門守`、`## 概述`、`## 神格與屬性`、`## 神話事蹟`、`## 跨文化對應`（表格）、`## 相關神祇`、`## 出現在`、`## 參考文獻`。

內容要點：

- 名號與詞源：Hopi `Masauwu`／`Maasaw`；又稱「骨架人」（Skeleton Man）、「大地守護者」。是第四世界之主、火的守護者、第五世界之門的守門者、死亡之神。
- 四塊石板：由 Maasaw 交給第四世界的人，其中三塊給熊氏族、一塊給火氏族（Brook 2018 引 Hopi 口述）。
- 身份降格與復位：他原是第三世界的大地之神，因第三世界的失當行為被降為死亡之神與冥界之主，第四世界成立時復為大地守護者。這是「世界循環＝神的職能循環」的直接例證。
- 面具的雙重描述：同一面具下可被描述為醜陋可怖，也可為俊美戴寶石者——Pritzker 指出此為霍皮諸版本差異的指標（*Hopi Creation Myth*, Book 1）。
- 與蜘蛛祖母／Tawa／Sotuknang 的位階：Sotuknang 造九界並造蜘蛛祖母；蜘蛛祖母護佑心善者。
- 湧出之地 `sipapu`（瓦爾皮版本認為即大峽谷）與「水氏族」名 Patkinyamu（「水上的居所」＝船屋）（Courlander 1971）。
- 跨文化對照表至少 6 列：Maasauwu ↔ 埃及 Khonsu／Osiris（死亡與土地復生）↔ 蘇美 Nergal ↔ 希臘 Hades ↔ 北歐 Hel ↔ 中美索聶米亞 Mictlantecuhtli ↔ 中國后土／幽都 ↔ 印度 Yama 對比表。
- 使用倫理註記：Maasaw 面具僅由 Hopi 敬拜者持有與穿戴；Hopi 對外披露形象有嚴格規範，頁面須標明照片／面具描寫的限制。

- [ ] **Step 3: 登錄 gods/README.md**

在 `| [Heyoka](Heyoka.md) | Heyoka |` 之前插入：
```
| [Masauwu](Masauwu.md) | 莫索烏（骨架人／大地守護者） |
```

- [ ] **Step 4: 驗證**

Run: `python3 scripts/ci_checks.py 2>&1 | tail -4` → 仍為 `14 errors`；`python3 -c "import re,io;t=io.open('cultures/indigenous-americas/gods/Masauwu.md',encoding='utf-8').read();print(len(re.findall(r'[\u4e00-\u9fff]',t)))"` → ≥300

- [ ] **Step 5: Commit**

```bash
git add cultures/indigenous-americas/gods/Masauwu.md cultures/indigenous-americas/gods/README.md
git commit -m "mythos: enrich indigenous-americas — 莫索烏神祇頁"
```

---

### Task 4: 雙子英雄（Hero Twins）故事頁

- **Files:**
  - Rewrite: `cultures/indigenous-americas/stories/雙子英雄.md`（現 342 字元空殼）

- [ ] **Step 1: 確認目標檔為空殼**

Run: `wc -m cultures/indigenous-americas/stories/雙子英雄.md`
Expected: `342`

- [ ] **Step 2: 覆寫**

章節：`# 雙子英雄 (Hero Twins / God Boys) — 母生於死者之腹的四洲英雄`、`## 故事背景`、`## 情節`、`## 跨文化平行`、`## 相關主題`、`## 參考文獻`。

內容要點（四條獨立傳統並置，不混為一談）：

- **納瓦荷（Diné）**：變遷之女生下 `Naayééʼ Neizghání`（怪物殺手）與 `Tóbájíshchíní`（水中生／生於水者），父為太陽。太陽屢次企圖殺子，最終賜直閃電與曲閃電。兄長獨行，弟弟守祈禱棒（prayer sticks），棒燃即代表兄長遇險。殺死巨怪 Yeitso（太陽的長子）後帶頭皮歸鄉，母親以雷擊藥草救活二人（Ehrlich 1947 引用 Roheim 1950:319–321）。頁面須連到既有 `stories/monster-slayer-and-born-for-water.md`。
- **Arikara（Long Teeth 與 Drinks Brains）**：母被殺，父自母體取出長子，以鹿腦湯餵養；**長牙（Long Teeth）自胎盤／胞衣中生出**並在荒野長大（Wissler 1908；native-languages 詞條）。
- **Cherokee（Thunder Boys）**：Kanati（幸運獵人）與 Selu（玉米母神）之二子不羈，遂西遷至「日落之地」Darkening Land；自西方傳來的低沉雷聲即二人在彼此交談。他們後被納入 `Ani Hyuntikwalaski`（Mooney 1900；James Mooney 對 Eastern Band 的記錄）。
- **Pueblo（Quères 的 Máw-Sahv 與 Oó-yah-wee）**：太陽為父、母死於產褥；祖母講述南方山峽女巨人；雙子奪其屋中儲存的雷電，風暴王 Shée-wo-nah 索回不成而降雨滅之，穴熊（Tee-oh-pee）挖洞排水救之（*Pueblo Indian Stories*，Carlisle 1900）。
- **Skidi Pawnee 的 Long Tooth Boy** 與 **Creek 的 Bead Spiner 與 Thrown Away**：胎盤／臍帶人化為第二子（Hall 1989, 1997；Myers 2002 論文引述）。
- **禁忌面**：中部美洲通常視雙生為不祥（一說出生後須殺一），而北美諸族多視為超能者甚至受祝福者（Miller & Taube 1993；Sullivan 1988）——此差異必須寫出，不能抹平。
- 跨文化平行段落：指名《克里特島》的歐洲雙子神話如何從未被收集（Thomsen 問題）反襯北美材料的豐富；並指 Popol Vuh 的 Hunahpu／Xbalanque 為本庫另一文化（mayan）條目，不在此頁重複。

- [ ] **Step 3: 驗證 + Commit**

Run: 字數檢查（見 Task 1 Step 3 的 python 片段，替換檔名）→ ≥300
```bash
git add cultures/indigenous-americas/stories/雙子英雄.md
git commit -m "mythos: enrich indigenous-americas — 雙子英雄故事頁改寫"
```

---

### Task 5: Coyote 與眾神故事頁

- **Files:**
  - Rewrite: `cultures/indigenous-americas/stories/Coyote與眾神.md`（現 348 字元空殼）

- [ ] **Step 1: 確認目標檔為空殼**

Run: `wc -m cultures/indigenous-americas/stories/Coyote與眾神.md`
Expected: `348`

- [ ] **Step 2: 覆寫**

章節：`# Coyote 與眾神 — 竊火者、竊日者與被逐出天界者`、`## 故事背景`、`## 情節`、`## 跨文化平行`、`## 相關主題`、`## 參考文獻`。

內容要點（以「郊狼與神族的三種結構」為骨架）：

- **竊火（Salish／Cherokee 型的「三個火之存在」）**：Coyote 觀察火之存在在山頂輪班守火，注意到每日破曉交班時換班者遲緩而睡眼惺忪，遂趁隙奪火而逃；火之存在追至山腳抓住了他尾尖，遂留下白尾尖。他們追趕松鼠／花栗鼠／蛙，最後火被「木」吞下，Coyote 教人以鑽木取火（Kellogg 教材本；可與本庫 `comparisons/…` 竊火母題對讀）。
- **竊日（Pomo 的複合神話）**：Coyote 用四隻老鼠啃斷懸掛太陽的 withy，並以魔杖誘使太陽人入睡；太陽被取下後由兩位烏鴉兄弟掛上天心。Barrett 1908 JAFL 同時指出 Pomo／Yuki／Maidu 三版本並列（Maidu 版由 Angle Worm 與 Gopher 驅逐日月，二者協商誰晝誰夜）。Coyote 隨後因不滿而把人變成動物——「變形者的權力」母題。
- **天界的門檻與被逐**：Pomo 複合敘事中三人經蜘蛛（天界門守）與羽繩逃到天界，遇 Madiłmda；Madiłmda 對 Coyote 的行為不滿，將他送回地上並指令其未來所為。**結構意義：郊狼的能力在神界被重新界定，而不是被消滅。**
- **天／水二分與季節協議**：Glenbow 黑腳族傳統記載：Ninastako（首領山）是 Thunder（Ksiistsikomm）的居所，Raven（Omahkai'stoo）於 Crow's Nest Mountain 與雷交戰，之後雙方議定一年分兩季——夏屬雷、冬屬 Raven。
- **平原創世敘事中的郊狼角色**：Coyote／Old Man／Napi 與「大地潛水者」的黏土創世（Encyclopedia of the Great Plains〈Plains Indian Narratives〉；Wissler & Duvall 1908）。
- **季節與敘事規範**：平原諸族只在霜降之後至春雷之間的冬季夜晚講 Coyote 故事，聽者須以「ée（是）」應和，否則立即中止（Encyclopedia of the Great Plains）——這條是本頁最有價值的「儀式學」細節，須寫入。
- 跨文化平行段落：Prometheus ↔ 中國鰲/google「盜火」與 燧人取火 ↔ 毛利 Tāwhaki 自天階取火 ↔ 波利尼西亞 Māui 之火 ↔ 西非 Anansi 取火 ↔ 日本天石屋火之加賀之助。
- 註明與既有頁的分工：與 `stories/Coyote與雷鳥之戰.md`、`gods/Horned-Serpent.md`、`comparisons/騙子神跨文化比較.md` 互為補充而非重複。

- [ ] **Step 3: 驗證 + Commit**

```bash
git add cultures/indigenous-americas/stories/Coyote與眾神.md
git commit -m "mythos: enrich indigenous-americas — Coyote 與眾神故事頁改寫"
```

---

### Task 6: 白水牛女送七儀式故事頁

- **Files:**
  - Rewrite: `cultures/indigenous-americas/stories/白水牛女送七儀式.md`（現 366 字元空殼）

- [ ] **Step 1: 確認目標檔為空殼**

Run: `wc -m cultures/indigenous-americas/stories/白水牛女送七儀式.md`
Expected: `366`

- [ ] **Step 2: 覆寫**

章節：`# 白水牛女送七儀式 — 聖煙斗的贈予與七聖禮的傳授`、`## 故事背景`、`## 情節`、`## 跨文化平行`、`## 相關主題`、`## 參考文獻`。

內容要點（與 Task 2 頁分工：神祇頁寫「她是誰」，本頁寫「儀式如何運作」）：

- **逐節儀式流程**（McLaughlin 1916 + Brown 1953 合併的骨架）：兩獵人 → 潔淨者報信 → 日中四柱煙的預兆 → 立大帳 → 圍坐低頭 → 一人抬頭被煙灼眼（「你違逆我，眼中將一生有煙」）→ 她入圈 → 先餵兒童、再婦女、最後男人 → 遞煙斗 → 教採柳皮與煙葉 → 交給首領 Hehlokecha Najin（Standing Hollow Horn）→ 留居多日逐帳探訪 → 離去：命婦女備乾三角葉楊火，薩滿置甜草成煙 → 她走入煙中消失 → 眾薩滿確認「是 Whope 賜的煙斗」，立守管者，並聲明：只要以莊重儀式吸煙，Whope 就在任何一支煙斗的煙裡。
- **烟斗的装填仪式**（復旦 eScholarship 論文）：聖人先以唾「封」碗桿接合處以啟動煙斗之力；左手托鼠尾草，右手七次投煙，每次對四方、祖母地、斑尾鷹、Wakan Tanka 祈禱。
- **七聖禮各與煙斗的關係**（逐一對應上文七項）。
- **禁令與條件**：不潔者不得見 lela wakan；忘記煙斗即滅亡。
- **考古與物質證據**：明尼蘇達 Pipestone 石場採石已 3,000 年（連接 1710 年 Mohican 酋長雷鳥紋身與當代）；碗＝子宮形。
- 跨文化平行：授予型創始事件 ↔ 印加 Manco Capac 與 Coya 求婚（Garcilaso《印加人王室述要》）↔ 蘇美 Nanshe 之巡行與烏爾的分配 ↔ 日本 天日隅宮（Takamagahara）覺神授藝 ↔ 毛利 Rākaihautū ↔ 西非 聖化的王室寶物（Mali 的 sika）。
- 註明尊重條款：非原住民不得持有／使用聖煙斗，須經族人收養；本頁僅作文獻記錄用途。

- [ ] **Step 3: 驗證 + Commit**

```bash
git add cultures/indigenous-americas/stories/白水牛女送七儀式.md
git commit -m "mythos: enrich indigenous-americas — 白水牛女送七儀式故事頁改寫"
```

---

### Task 7: 貂女與雷人故事頁 — 新增

- **Files:**
  - Create: `cultures/indigenous-americas/stories/mink-woman-and-thunder-man.md`
  - Modify: `cultures/indigenous-americas/stories/README.md`（新增一列）

- [ ] **Step 1: 確認本文化無太平洋西北故事頁**

Run: `grep -ril "mink\|貂" cultures/indigenous-americas/stories/ | wc -l`
Expected: `0`

- [ ] **Step 2: 建立頁面**

章節：`# 貂女與雷人 (Mink Woman and Thunder Man) — 黑腳族天界聯姻與一條牛皮繩的下降`、`## 故事背景`、`## 情節`、`## 跨文化平行`、`## 相關主題`、`## 參考文獻`。

內容要點（據 James Willard Schultz《Blackfeet Tales of Glacier National Park》逐字記錄）：

- 三位姊妹（貂女最小）同行拾柴，貂女唱著歌走在最後；叢林中走出外貌俊美、衣著講究的男人說「我來接你了」。
- 貂女隨雷人上天界，在那裡「溫暖晴朗、有如地上而無風暴」；她忘記故土與族人。
- 地上的人以歌聲呼喚，貂女因此被召回。雷人召集獵人取大量野牛皮、命婦女把皮切成長條相連，並親自**以公牛皮與柳條做成一具高邊的籃子**（內襯軟皮），連同**一條單股長牛皮繩**，帶到貂女撕開的天穹洞口。
- 雷人將貂女安置籃中，命人以籃沿洞口緩緩放下，繩逐寸放出；地上人只見緩緩旋轉下降之物，如陌鳥。
- 籃子觸地，貂女步出；眾人圍迎；籃子隨即升空消失於遠藍。
- 雷人隨後到訪貂女的族帳（駐於 Lame Bull 帳），宣布自己是她的父；**Craw Man（烏人）** 屢次求親，貂女婉拒；某次以低語勸誘成功。族眾因恐雷人發怒毀滅全帳，擠在帳門外求「把女兒還給她父親」。
- 兩造衝突幾乎引發滅族；雷人最終認回貂女，並把天界的器物（太陽舞用的大帳、Thunderbird 圖騰、煙斗）留在地上。**這一段是全頁的關鍵：天界不是禁地，而是外交場合。**
- 補充 Glenbow 傳統：Ninastako（首領山）為雷之居所，Raven 與雷於 Crow's Nest Mountain 交戰後議定兩季（夏雷／冬 Raven）；Crow's Nest 現址即 Raven 所居。此為「季節協商」的宇宙神話版本。
- 跨文化平行：天界以繩／階梯相連 ↔ 日本《古事記》天石屋見（あまのはら）天梯 ↔ 蘇美 Etana 以鷹下降 ↔ 印度 Väṇṇarasatha 猴王降世 ↔ 印加 Manco Capac 由 `Pachacamac` 處受命（Garcilaso）↔ 秘魯 `Qoyllur Rit'i` 之梯 ↔ 易洛魁 Sky Woman 以樺皮小舟自天而降（本庫既有頁）。
- 「天界繩索」母題的儀式性：與黑腳族「以歌謠歌召喚」及 Schmidt 記錄的「以聖歌對石與人問答」互相對讀。
- 註明檔案限制：本頁為 Schultz 1918–1934 年間在兩醫藥河（Two Medicine）一帶蒐集、由 Yellow Wolf 口述的轉寫稿，帶有明顯的「歷史被重述」痕跡（他於 1896 年去世）；頁面須標明其為特定蒐集情境下的口述版本，而非唯一「原典」。

- [ ] **Step 3: 登錄 stories/README.md**

在 `| [雷夢之人：嘿約卡的反向智慧](heyoka-reverse-wisdom.md) |` 之前插入：
```
| [貂女與雷人 (Mink Woman and Thunder Man)](mink-woman-and-thunder-man.md) | 貂女與雷人 |
```

- [ ] **Step 4: 驗證 + Commit**

```bash
git add cultures/indigenous-americas/stories/mink-woman-and-thunder-man.md cultures/indigenous-americas/stories/README.md
git commit -m "mythos: enrich indigenous-americas — 貂女與雷人故事頁"
```

---

### Task 8: 大洪水世界重建比較頁

- **Files:**
  - Rewrite: `cultures/indigenous-americas/comparisons/大洪水世界重建.md`（現 227 字元空殼）

- [ ] **Step 1: 確認目標檔為空殼**

Run: `wc -m cultures/indigenous-americas/comparisons/大洪水世界重建.md`
Expected: `227`

- [ ] **Step 2: 覆寫**

章節：`# 大洪水世界重建 — 世界毀滅與再生的跨文化循環比較`、`## 比較：美洲原住民神話 vs 其他文化`、`## 結構分析：四種毀滅機制`、`## 跨文化對照表`、`## 參考文獻`。

內容要點：

- **霍皮四世界循環**（Malotki《Hopi Tales》1979 譯；Stephen 1929 引；Brook 2018 引口述）：第一世界由 **Tokpela**（無限空間）構成，Tokonangh／Sotuknang 依 Tawa（Taiowa）計畫造九界、造蜘蛛祖母、造雙子 **Palongo-Haya 與 Pokan-Haya**，雙子賦予世人「創世之歌」；世人忘歌 → **火** 毀第一世界（倖存者託付螞蟻）→ 第二世界 → **冰**（凍結而失衡、旋轉短暫中止）→ 第三世界（有「飛行的箱子」、大城、戰爭）→ **大洪水**（下了一整個月亮，約 28 天）→ 第四世界現今。地下世界第四世界成為死者樂土（Cloud People）。
- **兩種湧出版本**（Pritzker：sipapu 說；Oraibi 說）：蘆竹／香蒲（cane reed）與 竹筏 兩版；「水氏族 Patkinyamu = 水上的居所」。
- **Shungopavi 水蛇村的毀滅**（Malotki）：領袖因旱而向水蛇人求水與平地，觸怒神靈 → 洪水與地震 → 領袖全滅。水被表述為**有意志的實體**，褻瀆即反噬。
- **Haudenosaunee 的單一舊世界 + 大法**：Leon Shenandoah 述第一世界五族互相伏殺、擄掠食人，Dekanawida／和平締造者立 *Kayanerenhkowa*（見本庫 `stories/hiawatha-great-law.md`）。
- **Ajiw/Chippewa（Blackfoot）洪水後的四種水**（Blackfoot mythology 條目）：Napi／老人在山上發給眾人四色水，飲後各說不同語言，唯飲黑水者語言同——即今日 Blackfoot、Piegan、Siksika、Blood（Kainai）四部族。
- **四種毀滅機制分類表**：水（大洪水）／火（世界樹焚毀）／冰（冰期封凍）／地（地震、山嶺抬升）。
- **跨文化對照表至少 8 列**：

| 文化 | 毀滅機制 | 倖存條件 | 出處 |
|---|---|---|---|
| Hopi | 火→冰→洪水 | 記得創世之歌、託付螞蟻／乘蘆竹 | Malotki 1979；Brook 2018 |
| Haudenosaunee | 戰爭／食人退化 | 締造者立大法 | Leon Shenandoah 口述 |
| Blackfoot (Ajiw) | 洪水 | 登上高山、飲黑水者同語 | Blackfoot mythology |
| Ojibwe | 洪水 | 麝香獻祭→納納博佐毀納加島 | 本庫 `stories/nanabozho-great-flood.md` |
| Sumer (Ziusudra) | 洪水 | 木舟 | *Epic of Gilgamesh* / *Enuma Elish* |
| Greek (Deucalion) | 洪水 | 石舟 | Apollodorus *Library* 1.7.3 |
| Hebrew (Noah) | 洪水 | 方舟、逐類動物 | *Genesis* 6–9 |
| Hindu (Manu) | 洪水 | 魚腹中構舟 | *Mahabharata* / Purāṇic |
| Chinese (Gun-Yu) | 洪水 | 鰲五色山，禹 | 《尚書·禹貢》《淮南子》 |
| Japanese (Ōkuninushi) | 洪水 | 稱平氏巨魚之救 | 《古事記》 |
| Greek (Prometheus) | 火（準洪水） | 火種藏於木 | Hesiod *Theogony* |
| Hopi (Shungopavi) | 洪水＋地震 | 敬畏水蛇 | Malotki 1979 |

- 結構分析：北美獨特處在**多次循環**（霍皮三世界）而非單次洪水；且毀滅者由「道德失序」觸發（用了靈力、貪婪、遺忘歌聲），這與西亞「神決定滅族」及東亞「治水」三者形成三種不同因果結構。
- 註明反覆出現的挪用史：霍皮「預言」在 1950–70 年代被非原住民末世論大量改寫（Brook 2018），與「地質學上把四世界當作冰期四次」的偽科學並置，頁面須明確切割。

- [ ] **Step 3: 驗證 + Commit**

```bash
git add cultures/indigenous-americas/comparisons/大洪水世界重建.md
git commit -m "mythos: enrich indigenous-americas — 大洪水世界重建比較頁改寫"
```

---

### Task 9: 雙子英雄母題跨文化比較頁 — 新增

- **Files:**
  - Create: `cultures/indigenous-americas/comparisons/twin-hero-motif-cross-cultural.md`
  - Modify: `cultures/indigenous-americas/comparisons/README.md`（新增一列；CI 檢查孤兒檔）

- [ ] **Step 1: 確認全庫無雙子母題比較頁**

Run: `grep -rl "雙子英雄\|Hero Twins" cultures/*/comparisons/ analyses/ | wc -l`
Expected: `0`

- [ ] **Step 2: 建立頁面**

章節：`# 雙子英雄母題跨文化比較 — 英雄雙子、雙極世界與「一者降冥界」的三種結構`、`## 比較：北美雙子英雄 vs 全球神話中的雙子神`、`## 三種結構模型`、`## 跨文化對照表`、`## 為何歐洲沒有收集到北美神話（Thomsen 問題）`、`## 參考文獻`。

三種結構模型：

- **模型 A：相剋型（善惡／白黑雙生）** — 易洛魁與 Oneida 的 Good Spirit／Bad Spirit（Sky Woman 與其雙子孫）；Yuma 雙子亦以此結構為代表（Myers 2002）。原型對照：Castor & Polydeuces（Castor 死而 Pollux 不死 → 對照「不死者成神」）、Romulus & Remus（創建＋兄弟屠殺）、Ībeji（Yoruba 雙子崇拜：母神 *Ọ̀ṣun* 之力使生雙子；雙子一人「落入`Ọ̀ṣun`的恩寵並帶走炊煮之匙」而成為神，餘者失一足、留地為人）——此為跨大西洋最可對照的「一者成神、一者留世」結構。
- **模型 B：同為英雄型** — 納瓦荷怪物殺手與水中生（`monster-slayer-and-born-for-water.md`）；Skidi Pawnee Long Tooth Boy；Quères 的 Máw-Sahv 與 Oó-yah-wee；Caddo 的 The God Boys；Camayurá（南美）Kwat 與 Yali 自葫蘆孵出（Sullivan 1988）。全球對照：*Rigveda* 1.116–119 的 **Aśvins**（雙生醫者、以奇蹟醫術行之、快速）、希臘 Dioscuri、芬蘭與愛沙尼亞「雙子建國」、波利尼西亞「雙子航海者」。
- **模型 C：一者降冥界（死／生二分）** — 邁阿密（易洛魁）— 依 Myers 2002 與 Hall 1989；最完整的「雙子一者沉於水界、一者留於日界」結構在北美不若印歐常見，印歐最接近者為：*Rigveda* 的雙子對 **Nṛti**（亡靈集團）之戰、以及希臘 Castor／Pollux 的陰間轮流（Leucippus／Ida 洞中交替）；東亞則以 **Souma no Kuninohito** 與 **Hikohō** 的左右座（C. Lévi-Strauss）提供三向表。頁面需明確標示：這一段是**結構相似但功能不同**，不可宣稱歷史關聯。
- **「雙子即金星」的假說**：Robert Hall（1989）與 Michael D. Coe 均論證 Winnebago 的 Red Horn ↔ 瑪雅 One Hunahpu 同為金星之人化；Radin 1948 亦主張同一象徵系統。頁面須把它標為「有影響力但未定論的假說」。
- **Thomsen 問題**：Christian Thomsen 指出歐洲早於蒐集時期已存在「大量北美神話」的主張並不可考；Brinton 與 R. H. Lowie 對此有不同處理。此段是本頁的方法論骨架，用以說明「北美雙子母題的獨特密度不能被『世界文明普遍性』一語帶過」。

跨文化對照表至少 10 列（文化／雙子名／結構模型／異常情節／後果／出處）：

| 文化 | 雙子 | 模型 | 異常情節 | 後果 | 出處 |
|---|---|---|---|---|---|
| Diné | 怪物殺手／水中生 | B | 母死、父欲殺子 | 賜閃電，殺巨怪 | Ehrlich 1947；Roheim 1950 |
| Arikara | 長牙／飲腦湯 | B | 母被殺、長子自胞衣生 | 荒野長大後復仇 | Wissler & Duvall 1908 |
| Skidi Pawnee | 長牙子 | B | 胞衣／臍帶化人 | 與 Popol Vuh 結構同 | Hall 1997；Myers 2002 |
| Creek | 珠紡人／拋棄兒 | B | 母被殺、臍帶拋入灌木 | 英雄雙子 | Hall 1989, 1997 |
| Winnebago | Red Horn | B | 與巨人球戲、斷首 | 兒子復仇 | Radin 1948；Tedlock 1996 |
| 易洛魁／Oneida | 善靈／惡靈 | A | Sky Woman 之孫 | 世界分善惡 | Mooney 1900；native-languages |
| Quères Pueblo | Máw-Sahv／Oó-yah-wee | B | 母死於產褥 | 竊雷電，氣象戰 | Carlisle 1900 |
| Maya | Hunahpu／Xbalanque | B | 父被殺、首卡樹叉 | 冥界復仇 → 日月 | *Popol Vuh*（見 mayan 條目） |
| Yoruba | Ìbeji | A/C | 母神賦能 | 一者帶炊匙成神 | Johnson 1970；Ogbar 2014 |
| 印度 | Aśvins | B | 雙生醫者 | 逆生、療癒 | *Ṛgveda* 1.116–119 |
| 希臘 | Castor／Pollux | A/C | 一死一不死 | 交替冥界、董農 | Apollodorus 1.3.1–3；*Hom. Hymn* 17 |
| 羅馬 | Romulus／Remus | A | 母被殺 | 創城 + 屠兄 | Ovid *Fasti* 2 |
| 芬蘭-烏戈爾 | 雙子（Amminki/Saarni） | B | 兄殺弟或反之 | 重建家系 | Lönnrot *Kalevala* 追溯 |
| 中部美洲 | Quetzalcoatl／Tezcatlipoca | A | 爭奪太陽之位 | 化身晨星 | León-Portilla |

- 結論段：**三種模型在北美皆可見，但分布不均**——模型 A（善惡相剋）主要在東北部與加州，中部美洲傾向「出生即凶」的禁忌版本；模型 B（共同英雄）在平原與西南最盛；模型 C（雙子即金星／日月）在中部美洲被文字與碑銘實證，宜與北美口傳版本區分證據強度。

- [ ] **Step 3: 登錄 comparisons/README.md**

在 `| [神聖小丑的節慶反轉…` 之前插入：
```
| [雙子英雄母題跨文化比較](twin-hero-motif-cross-cultural.md) | twin-hero-motif-cross-cultural |
```
（此格式為該 README 現有風格；CI 的 `get_indexed_entries` 只需檔名出現在索引中。）

- [ ] **Step 4: 驗證**

Run: `python3 scripts/ci_checks.py 2>&1 | grep -c "twin-hero"` → `0`（不得出現新的 orphan 錯誤）
Run: 字數 ≥300

- [ ] **Step 5: Commit**

```bash
git add cultures/indigenous-americas/comparisons/twin-hero-motif-cross-cultural.md cultures/indigenous-americas/comparisons/README.md
git commit -m "mythos: enrich indigenous-americas — 雙子英雄母題比較頁"
```

---

### Task 10: 登錄同步（catalog／state／README／stats）

- **Files:**
  - Modify: `_catalog.json`、`_state.json`、`cultures/indigenous-americas/README.md`、根 `README.md`、`stats/index.md`

- [ ] **Step 1: 更新 `_catalog.json` 的 indigenous-americas 条目**

以 `python3` 修改：向 `pantheon` 追加 `Masauwu(骨架人/死亡與大地守護者)`；向 `stories` 追加 `貂女與雷人`；`gods` 追加 `莫索烏`；`comparisons` 追加 `雙子英雄母題跨文化比較`；`_stories` 由 10 → 12。寫回時用 `json.dump(..., ensure_ascii=False, indent=2)` 並保留原檔的無尾換行風格（用 `newline=''` 避免額外改動整檔）。

Run: `git diff --stat _catalog.json` → 只顯示 1 檔約 6 行增減。

- [ ] **Step 2: 更新 `_state.json`**

`runs` 207 → 208；`enrich_log` 末尾追加 `"indigenous-americas"`。

- [ ] **Step 3: 更新文化 README 與根 README**

- `cultures/indigenous-americas/README.md`：頁數計數由 70 → 73（依既有欄位名稱更新三個數字）。
- 根 `README.md`：文化列 `| [美洲原住民神話](cultures/indigenous-americas/) | 北美洲 | 22 | 20 | 17 |` 的計數欄依 `generate_stats.py` 輸出更新（以 Task 11 產生的 `stats/index.md` 為準）。

- [ ] **Step 4: 產生統計**

Run: `python3 scripts/generate_stats.py`
Expected: 重新產生 `README.md` 統計區與 `stats/index.md`、`stats/overview`、`stats/radar`。若 matplotlib 缺失，改以手動更新 `README.md` 與 `stats/index.md` 的三處計數（並在 commit 訊息中註明）。

- [ ] **Step 5: Commit**

```bash
git add -A _catalog.json _state.json README.md stats cultures/indigenous-americas/README.md
git commit -m "mythos: enrich indigenous-americas — 同步 catalog／state／README／stats"
```

---

### Task 11: 驗證與推送

- [ ] **Step 1: 全部九頁字數檢查**

Run:
```bash
for f in cultures/indigenous-americas/gods/雷鳥.md \
         cultures/indigenous-americas/gods/White-Buffalo-Calf-Woman.md \
         cultures/indigenous-americas/gods/Masauwu.md \
         cultures/indigenous-americas/stories/雙子英雄.md \
         cultures/indigenous-americas/stories/Coyote與眾神.md \
         cultures/indigenous-americas/stories/白水牛女送七儀式.md \
         cultures/indigenous-americas/stories/mink-woman-and-thunder-man.md \
         cultures/indigenous-americas/comparisons/大洪水世界重建.md \
         cultures/indigenous-americas/comparisons/twin-hero-motif-cross-cultural.md; do
  python3 -c "import re,io,sys;t=io.open(sys.argv[1],encoding='utf-8').read();print(len(re.findall(r'[\u4e00-\u9fff]',t)), sys.argv[1])" "$f"
done
```
Expected: 每一行第一個數字皆 ≥300。

- [ ] **Step 2: 確認已無任何空殼頁殘留**

Run: `for f in cultures/indigenous-americas/{gods,stories,comparisons}/*.md; do [ "$(wc -m < "$f")" -lt 1200 ] && echo "SHELL: $f"; done`
Expected: 無輸出（或僅列出非本次範圍者並記錄原因）。

- [ ] **Step 3: CI 錯誤數維持 14**

Run: `python3 scripts/ci_checks.py 2>&1 | tail -3`
Expected: `❌ FAILED — 14 errors, 0 warnings`，且錯誤清單與本計畫開始時完全相同（不得出現 indigenous-americas 相關錯誤）。

- [ ] **Step 4: 最終提交與推送**

```bash
git add -A
git commit -m "mythos: enrich indigenous-americas" --amend --no-edit 2>/dev/null || git commit -m "mythos: enrich indigenous-americas"
git push
```
（若 Task 1–10 已各自 commit，此處以一個空的最終 commit 為佳；若 `git commit` 回報無變更則略過該步，直接 push。）

- [ ] **Step 5: 回報**

回報需含：新增／改寫的 9 個檔名與各自主題、頁數變化（70 → 73）、CI 錯誤數（14 / 0 新增）、commit hash、以及三組跨文化對照要點摘要（雷鳥的天—水宇宙對立、白水牛女的授予型創始與七聖禮、雙子母題的三種結構模型）。

---

## Self-Review

1. **Spec coverage**：使用者要求「找最薄弱文化（頁數最少）→ 新增 gods/stories/comparisons 各一頁（≥300 繁中字、含跨文化對應與參考來源）→ 三同步 → commit+push → 回報」。Task 1–9 覆蓋內容（3 新增 + 6 改寫，後者因為該文化實為「內容最薄弱」而非僅頁數最少）；Task 10 覆蓋三同步；Task 11 覆蓋驗證、commit、push、回報。全部有對應 task。
2. **Placeholder scan**：無 TBD／TODO；每個頁面任務均列出必須寫入的具體章節、名號、情節節點、對照表列數與具名文獻。
3. **Type consistency**：檔名在 Task 3/7/9 首次建立、Task 10 同步、Task 11 檢查，三處一致（`Masauwu.md`、`mink-woman-and-thunder-man.md`、`twin-hero-motif-cross-cultural.md`）。
4. **已知的自我修正**：Task 11 Step 4 的 `--amend` 在 Task 1–10 已各自 commit 時不適用，故補上 `|| git commit` fallback 與「空 commit 則略過」的說明，避免執行者卡在 no-change 錯誤。
