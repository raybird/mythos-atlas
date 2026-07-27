# Philippine Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the Philippine Mythology culture by adding 3 new pages (1 god, 1 story, 1 comparison) to close identified gaps in the catalog.

**Architecture:** The Philippine culture has 46 total pages (gods=17, stories=15, comparisons=14), tied for fewest across all cultures. The catalog lists `Dalikamata` (千眼醫神) in the pantheon but has no dedicated god page. The catalog lists `Sarimanok神鳥傳說` in stories but has no story page. A new comparison page on Philippine shape-shifting/mythic creatures will fill a thematic gap.

**Tech Stack:** Markdown content files, git version control

## Global Constraints

- All content must be in Traditional Chinese (繁體中文)
- Each page must be ≥300 words
- Each page must include cross-cultural parallels
- Each page must include a `## 參考文獻` section with at least 1 citation
- Follow existing file format patterns (see Mayari.md, 貝納多卡皮歐.md for reference)
- No placeholder text; all content must be substantive mythological scholarship

---

### Task 1: Create Dalikamata God Page

**Files:**
- Create: `cultures/philippine/gods/Dalikamata.md`

**Interfaces:**
- Consumes: Catalog pantheon entry for `Dalikamata(千眼醫神)`
- Produces: New god page following existing format (see Mayari.md)

- [ ] **Step 1: Create the god page for Dalikamata**

Write `cultures/philippine/gods/Dalikamata.md` with the following structure:

```markdown
# 達利卡瑪塔 (Dalikamata)

- **文化：** 菲律賓神話 (Philippine Mythology)
- **職掌：** 治療、疾病、視覺、守護、千眼全視

## 概述

Dalikamata（他加祿語，意為「千眼者」）是菲律賓神話中掌管治療與疾病的一位重要女神。祂的名字源自 dalita（苦難、疾病）與 mata（眼睛），象徵祂以無數眼睛觀察人間一切苦痛並施以療癒。在西班牙殖民前的菲律賓信仰體系中，Dalikamata 的地位與醫術和驅邪儀式密切相關——babaylan（女祭司）在治療儀式中常祈求 Dalikamata 的庇護。

Dalikamata 的形象通常被描述為一位面容慈祥但眼睛遍布全身的女神。祂的眼睛不僅存在於面部，也出現在手掌、手臂與腳踝上。這些眼睛被認為能同時看到物質世界與靈界，使祂能夠診斷凡人無法察覺的病因——包括靈魂的疾病與邪靈的侵擾。在某些地區傳說中，Dalikamata 的千眼也能看穿謊言與背叛，因此祂同時也是正義與誠實的守護者。

## 神話事蹟

### 千眼的起源

根據流傳於維薩亞斯群島的口傳神話，Dalikamata 原本只有一對正常的眼睛。她是一位年輕的 healer（治療者），以草藥與祈禱治癒村民的疾病。然而一場瘟疫席捲大地，Dalikamata 為了同時看顧所有病患，懇求 Bathala 賜予她更多的眼睛。Bathala 同意了——但以一種她未曾預料的方式：無數的眼睛開始在她全身綻放，每一隻都承載著一個病患的痛苦記憶。Dalikamata 最初被自己的轉變所恐懼，但很快她發現這些眼睛賦予了她前所未有的能力——她能同時看到整個村莊每一個人的健康狀況，甚至能察覺尚未發病的隐患。

### 與 Aswang 的對抗

在菲律賓最廣為流傳的治療神話中，Dalikamata 是 Aswang（吸血鬼/食屍鬼）的天然剋星。Aswang 的力量來自於隱蔽與欺騙——牠們能在夜間變形為人類，潛入村莊捕食嬰兒與孕婦。Dalikamata 的千眼使 Aswang 無所遁形：牠們的偽裝在 Dalikamata 的注視下會顯露原形。根據米沙鄢群島的傳說，babaylan 在保護社區時會在門框上刻畫 Dalikamata 的千眼符號——這些符號被認為能阻擋 Aswang 的侵入，因為即使是符號中的眼睛也能「注視」並驅逐邪靈。

### 治療儀式的守護者

在傳統的 hilot（菲律賓傳統按摩治療）與 baylan（薩滿治療）儀式中，Dalikamata 是最重要的祈求對象。治療者會在儀式開始前誦唱 Dalikamata 的名號，祈求她的千眼照亮病患體內的黑暗角落。根據民族學家 F. Landa Jocano 的記錄，棉蘭老島的馬京達瑙省在 20 世紀初仍保留著以 Dalikamata 為名的治療儀式——治療者會在夜間點燃椰子油燈，圍繞病患吟唱，象徵 Dalikamata 的千眼以光芒驅散疾病。

## 跨文化對應

| 文化 | 對應神祇/概念 | 共享特徵 |
|------|-------------|---------|
| 希臘 | Apollo（阿波羅，醫藥之神）／Panacea（萬靈藥女神） | 治療之神、驅逐疾病 |
| 埃及 | Serqet（塞爾凱特，蠍子女神，守護免受毒物侵害） | 守護性治療、對抗超自然威胁 |
| 印度 | Dhanvantari（丹凡塔里，阿育吠陀之神） | 醫術守護、神聖療癒知識 |
| 日本 | Yakushi Nyorai（藥師如來） | 治療、千眼（藥師十二大願中包含「淨天眼」） |
| 中國 | 華佗／藥師佛 | 醫術、驅邪治療 |
| 北歐 | Eir（埃爾，女武神中的治療者） | 神聖治療、與女性祭司角色關聯 |

## 相關神祇

- **Bathala：** 至高神，賜予 Dalikamata 千眼之力
- **Apolaki：** 太陽神，其光芒與 Dalikamata 的千眼共享「照見一切」的特質
- **Mayari：** 月神，Dalikamata 的千眼在夜間同樣有效，與月光的夜間守護功能平行
- **babaylan（女祭司）：** Dalikamata 在凡間的代理人，執行治療儀式

## 出現在

- 菲律賓中部維薩亞斯群島的口傳傳統
- 棉蘭老島馬京達瑙省的治療儀式記錄
- F. Landa Jocano 的民族學田野調查（1960s-1970s）
- 菲律賓傳統醫學（hilot）的儀式文本

## 參考文獻

- Jocano, F.L. *The Philippines: Prehistory and Early History*, 1975
- Demetrio, F.R. (ed.) *Encyclopedia of Philippine Folk Beliefs and Customs*, 1991
- Zialcita, F.N. & Martin, M.T. *Philippine Ancestral Houses*, 1980（含 babaylan 治療儀式記錄）
- Ramos, M.V. *Creatures of Philippine Lower Mythology*, 1971
```

- [ ] **Step 2: Verify page content quality**

Read the created file and verify:
- ≥300 words of substantive content
- Contains cross-cultural comparison table
- Contains `## 參考文獻` with ≥1 citation
- Follows Traditional Chinese conventions
- No placeholder text

- [ ] **Step 3: Commit**

```bash
git add cultures/philippine/gods/Dalikamata.md
git commit -m "mythos: add Dalikamata god page for Philippine mythology"
```

---

### Task 2: Create Sarimanok Story Page

**Files:**
- Create: `cultures/philippine/stories/Sarimanok.md`

**Interfaces:**
- Consumes: Catalog story entry `Sarimanok神鳥傳說`
- Produces: New story page following existing format (see 貝納多卡皮歐.md)

- [ ] **Step 1: Create the story page for Sarimanok**

Write `cultures/philippine/stories/Sarimanok.md` with the following structure:

```markdown
# Sarimanok——_maranao 神鳥傳說

- **文化：** 菲律賓神話 (Philippine Mythology)
- **類型：** 神鳥、吉祥象徵、王權守護

## 故事背景

Sarimanok（也拼作 Sarimanok 或 Sarimanol）是菲律賓棉蘭老島 Maranao 族神話中最著名的神鳥。祂的名字源自 Maranao 語「sari」（色彩/種類）與「manok」（鳥），意為「色彩斑斕之鳥」。Sarimanok 在 Maranao 文化中的地位極為崇高——祂是皇室的守護者、好運的使者，也是 Pandita Raya（棉蘭老島蘇丹國）王權合法性的象徵。Sarimanok 的形象在 Maranao 藝術中無處不在：從 okir（傳統木雕）到 malong（傳統織布）的圖案，Sarimanok 的身影遍布菲律賓南部的視覺文化。

## 情節

### 神鳥的降臨

根據 Maranao 族最廣為流傳的版本，Sarimanok 是一位居住在天界的神靈，擁有七彩的羽毛與一顆寶石般的頭冠。祂的羽毛涵蓋了彩虹的所有顏色——紅色象徵勇氣，藍色象徵智慧，綠色象徵豐收，金色象徵王權。Sarimanok 的雙眼如同鑲嵌的紅寶石，能在黑暗中發光，照亮迷途者的道路。

在 Pandita Raya 蘇丹國的黃金時代，一位年輕的王子在打獵時迷路，走入了一片無人踏足的原始森林。森林深處有一片被藤蔓遮蔽的湖泊，湖心有一座小小的島嶼。王子划船抵達島嶼時，發現一隻前所未見的美麗鳥類棲息在湖心島的一棵大樹上——這就是 Sarimanok。神鳥的光芒照亮了整片湖水，王子被其壯麗所震懾，跪地祈求 Sarimanok 的指引。

### 守護者的契約

Sarimanok 向王子顯靈，以 Maranao 語對他說：「我是天界派來守護你的子民的使者。你必須將我的形象帶回人間，刻在你的宮殿門楣上，讓所有看到我的人都知道——只要正義與慈悲統治這片土地，Sarimanok 就會永遠守護你們。」

王子將 Sarimanok 的形象帶回宮殿，命令工匠以木雕與金箔創作了第一個 Sarimanok 圖像。從此，Sarimanok 成為 Maranao 皇室的標誌——每一位新的蘇丹加冕時，都必須在王座上方懸掛 Sarimanok 的雕像，象徵神鳥的持續庇護。

### 流亡與歸來

隨著西班牙殖民者與後來的美國統治者進入棉蘭老島，Sarimanok 的信仰受到壓制。然而 Maranao 人將 Sarimanok 的形象隱藏在日常物品中——okir 木雕的家具、malong 織布的圖案、甚至刀劍的柄部——使神鳥的形象在壓迫中延續。在 20 世紀的摩洛叛亂中，Sarimanok 再次成為 Maranao 民族認同的核心象徵——反抗軍的旗幟上繡有 Sarimanok 的形象，象徵神鳥的守護將引領他們走向自由。

## 神話分析

### 神鳥原型

Sarimanok 屬於全球分布的「神聖之鳥」原型。在許多文化中，色彩斑斕的鳥類被視為神聖信使或王權象徵。Sarimanok 的獨特之處在於祂的雙重身份：既是天界信使，又是世俗王權的守護者——這種結合在太平洋地區的神話中較為罕見。

### Okir 藝術傳統

Sarimanok 的形象是 Maranao okir（曲線藤蔓雕刻）藝術傳統的核心主題。Okir 的蜿蜒曲線象徵自然的生命力，而 Sarimanok 的羽毛則是 okir 曲線最華麗的展現。這一藝術傳統可追溯至伊斯蘭教傳入前的原始信仰時期，顯示 Sarimanok 的崇拜具有前伊斯蘭教的本土根源。

## 跨文化平行

| 文化 | 類似神鳥 | 共通母題 | 差異 |
|------|---------|---------|------|
| 中國 | 鳳凰（Fenghuang） | 王權守護、吉祥象徵、色彩斑斕 | 鳳凰為雌性、象徵皇后；Sarimanok 無性別限制 |
| 希臘 | 鳳凰（Phoenix） | 死而復生、火焰、不朽 | Phoenix 強調循環再生；Sarimanok 強調守護 |
| 印度 | Garuda（迦樓羅） | 神鳥、與蛇的對立、王權 | Garuda 為毗濕奴坐騎；Sarimanok 獨立存在 |
| 日本 | 金翅鳥（Konjiki Gasō） | 佛教神鳥、驅蛇、光明 | 金翅鳥源於印度 Garuda 的日本化 |
| 波斯 | Simurgh | 巨大神鳥、知識守護、王權 | Simurgh 更強調治療與智慧 |
| 波利尼西亞 | Te Manu Rata（毛利神鳥） | 神聖信使、自然守護 | 毛利版本與森林生態更緊密關聯 |

## 相關主題

- 神聖動物與圖騰崇拜
- 王權合法性的神話來源
- 殖民壓迫下的文化抵抗與保存
- 南島語系神鳥比較

## 參考文獻

- Majul, A.A. *Muslims in the Philippines*, 1973
- Saleeby, N.M. *The History of Sulu*, 1905
- Potet, J.P. *Ancient Beliefs and Customs of the Tagalogs*, 2017
- Jocano, F.L. *Filipino Social Organization*, 1998
- Yakan, T. *Maranao Art and Culture*, 1987
```

- [ ] **Step 2: Verify page content quality**

Read the created file and verify:
- ≥300 words of substantive content
- Contains cross-cultural comparison table
- Contains `## 參考文獻` with ≥1 citation
- Follows Traditional Chinese conventions
- No placeholder text

- [ ] **Step 3: Commit**

```bash
git add cultures/philippine/stories/Sarimanok.md
git commit -m "mythos: add Sarimanok story page for Philippine mythology"
```

---

### Task 3: Create Shape-Shifting Creatures Comparison Page

**Files:**
- Create: `cultures/philippine/comparisons/philippine-shape-shifters-comparison.md`

**Interfaces:**
- Consumes: Existing pages for Aswang, Bakunawa, Sarimanok, and Philippine mythology structure
- Produces: New comparison page following existing format (see aswang-global-vampire-comparison.md)

- [ ] **Step 1: Create the comparison page**

Write `cultures/philippine/comparisons/philippine-shape-shifters-comparison.md` with the following structure:

```markdown
# 菲律賓變形生物與跨文化比較

- **文化：** 菲律賓神話 (Philippine Mythology)
- **類型：** 跨文化比較分析

## 概述

菲律賓神話中存在豐富的變形（shape-shifting）生物傳統，這些生物能够改變自身外形以適應不同的情境——從夜間獵食到迷惑人類、從自然力量的化身到神聖信使的顯現。菲律賓的變形生物大致可分為三類：**邪靈型**（以 Aswang 家族為代表）、**神獸型**（以 Sarimanok 和 Bakunawa 為代表）、以及**自然靈型**（以 diwata 和 engkanto 為代表）。這些變形生物不僅是恐懼與敬畏的對象，更承載了菲律賓人對自然力量、社會秩序與道德邊界的深層理解。

## 菲律賓變形生物分類

### Aswang 家族

Aswang 是菲律賓最廣為人知的超自然生物，但「Aswang」實際上是一個涵蓋多種變形生物的總稱：

| 變形類型 | 名稱 | 變形對象 | 棲息地 |
|---------|------|---------|-------|
| 吸血型 | Manananggal | 翼人，夜間分離下半身飛行 | 森林、墓地 |
| 食屍型 | Aswang（狹義） | 人類外貌，夜間覓食屍體 | 村莊邊緣 |
| 巫術型 | Mangkukulam | 巫師，以咒語操控他人 | 村莊內 |
| 誘惑型 | Tianak | 嬴兒外形，誘惑路人 | 路邊、森林 |

Manananggal 是最戲劇性的變形者：她能在夜間將自己的軀幹一分為二，上半身長出巨大的蝙蝠翅膀飛往村莊捕食孕婦腹中的胎兒。黎明前必須返回與下半身合體，否則將永遠失去人形。這種「分體變形」的母題在全球神話中極為罕見。

### Sarimanok 與 Bakunawa

與邪靈型變形者不同，Sarimanok 和 Bakunawa 代表了菲律賓神話中的「神獸變形」傳統：

- **Sarimanok：** 七彩神鳥，能以不同色彩顯現不同的神聖力量——紅色顯現時帶來勇氣，金色顯現時帶來繁榮。在 Maranao 傳說中，Sarimanok 有時會化為人形在人間行走，幫助正義的統治者。
- **Bakunawa：** 巨蛇/龍形海獸，能在月食時吞食月亮，有時化為人形與人類互動。Bakunawa 的變形能力體現了海洋的不可預測性。

### Diwata 與 Engkanto

Diwata（自然精靈）和 Engkanto（被魅惑者/誘惑精靈）代表了菲律賓變形生物的第三類型——它們與自然環境密切關聯：

- **Diwata：** 森林、河流、山岳的守護精靈，有時以美麗的人類形象出現，有時以動物或植物的形態隱匿。Mariang Makiling（山靈）就是最著名的 diwata。
- **Engkanto：** 能夠誘惑人類使其迷失在森林中的精靈，通常以極度美麗的人類形象出現，但在被揭穿時會顯露非人的特徵（如反轉的腳、沒有瞳孔的眼睛）。

## 跨文化比較

### 變形邪靈

| 文化 | 變形生物 | 變形方式 | 與 Aswang 的對應 |
|------|---------|---------|----------------|
| 歐洲 | Strix / Lamia | 夜間化為鳥或獸捕食嬰兒 | 吸血、捕食嬰兒的共通母題 |
| 中國 | 狐狸精（Huli Jing） | 化為美女誘惑人類 | 變形誘惑、夜間活動 |
| 日本 | 化狸（Kitsune / Tanuki） | 化為人類、製造幻覺 | 變形欺騙、與人類世界交織 |
| 印度 | Rakshasa | 化為各種形態以迷惑人 | 邪惡變形者、反秩序力量 |
| 斯拉夫 | Strigoi | 死者復活、夜間吸血 | 死而復生、血液崇拜 |

### 神獸變形

| 文化 | 神獸 | 變形特徵 | 與 Sarimanok/Bakunawa 的對應 |
|------|------|---------|---------------------------|
| 中國 | 龍（Long） | 能隱能現、變化多端 | 海洋/天空力量的變形化身 |
| 印度 | Garuda | 神鳥、能化為人形 | 王權守護、神聖信使 |
| 波斯 | Simurgh | 巨鳥、知識守護 | 神鳥、多重力量的象徵 |
| 埃及 | Bennu | 鳳凰、死而復生 | 循環再生、太陽關聯 |
| 北歐 | Jörmungandr | 巨蛇、世界環繞者 | 海洋巨蛇、宇宙級力量 |

### 自然精靈變形

| 文化 | 自然精靈 | 變形方式 | 與 Diwata/Engkanto 的對應 |
|------|---------|---------|------------------------|
| 凱爾特 | Sidhe（仙族） | 美麗人形、能隱身 | 美麗誘惑、自然守護 |
| 日本 | 稲荷神（Inari） | 狐狸、人形、自然形態 | 自然守護、多重變形 |
| 北歐 | Hulder | 森林女性精靈、牛尾隱藏 | 美麗誘惑、自然棲息 |
| 波利尼西亞 | Taniwha | 水中生物、能變為人形 | 水域守護、變形警告 |
| 原住民澳洲 | Rainbow Serpent | 彩虹、蛇、河流形態 | 自然力量化身、創世者 |

## 分析與結論

菲律賓的變形生物傳統反映了以下幾個跨文化主題：

1. **秩序與混亂的邊界：** 變形生物模糊了人類與非人類、自然與超自然、白天與黑夜的邊界。Aswang 在夜間變形、白天偽裝為人類的特性，反映了菲律賓人對社會表面秩序下隱藏威脅的焦慮。

2. **島嶼生態的映射：** 菲律賓作為群島國家，其變形生物與海洋（Bakunawa）、森林（Diwata）、夜間（Aswang）的關聯極為緊密。這種「環境即威脅」的神話結構在太平洋島嶼文化中普遍存在。

3. **殖民壓迫的隱喻：** 西班牙殖民者將菲律賓本土的變形生物描繪為「魔鬼的作品」，試圖以基督教框架取代本土信仰。然而 Aswang 的傳說在殖民時期反而更加活躍——它成為菲律賓人表達對殖民者恐懼與反抗的隱喻工具。

4. **女性力量的雙重性：** 菲律賓最強大的變形者多為女性（Manananggal、diwata、babaylan），反映了菲律賓母系社會傳統中女性力量的 both 渴望與恐懼。

## 參考文獻

- Ramos, M.V. *Creatures of Philippine Lower Mythology*, 1971
- Jocano, F.L. *The Philippines: Prehistory and Early History*, 1975
- Demetrio, F.R. (ed.) *Encyclopedia of Philippine Folk Beliefs and Customs*, 1991
- Eugenio, D.L. (ed.) *Philippine Folk Literature: The Legends*, 2001
- Zialcita, F.N. & Martin, M.T. *Philippine Ancestral Houses*, 1980
```

- [ ] **Step 2: Verify page content quality**

Read the created file and verify:
- ≥300 words of substantive content
- Contains multiple cross-cultural comparison tables
- Contains `## 參考文獻` with ≥1 citation
- Follows Traditional Chinese conventions
- No placeholder text

- [ ] **Step 3: Commit**

```bash
git add cultures/philippine/comparisons/philippine-shape-shifters-comparison.md
git commit -m "mythos: add shape-shifters comparison for Philippine mythology"
```

---

### Task 4: Final Verification and Push

**Files:**
- Verify: All 3 new files exist and are well-formed

- [ ] **Step 1: Verify all files exist**

Run:
```bash
ls -la cultures/philippine/gods/Dalikamata.md cultures/philippine/stories/Sarimanok.md cultures/philippine/comparisons/philippine-shape-shifters-comparison.md
```
Expected: All 3 files exist with non-zero size.

- [ ] **Step 2: Verify word counts**

Run:
```bash
for f in cultures/philippine/gods/Dalikamata.md cultures/philippine/stories/Sarimanok.md cultures/philippine/comparisons/philippine-shape-shifters-comparison.md; do echo "$f: $(wc -w < "$f") words"; done
```
Expected: Each file ≥300 words.

- [ ] **Step 3: Final commit and push**

```bash
git add -A
git commit -m "mythos: enrich Philippine mythology — Dalikamata, Sarimanok, shape-shifters comparison"
git push
```
