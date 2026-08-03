# 神話地圖集 — Mythos Atlas

> 上古的迴聲，比文字更古老；神話是集體記憶的碎屑，等待拼回原貌。

## 核心精神

這個 repository 是一個跨文化神話比較研究的開放式資料庫。目標不是收集「故事」，而是**追溯文明源頭的共同原型**——那些在文字發明之前就已存在的集體記憶與宇宙觀。

### 為什麼做這件事？

在人類文明的深層結構中，存在一組反覆出現的主題模式：

| 主題 | 出現的文化範例 |
|------|--------------|
| **大洪水** | 蘇美《吉爾伽美什》、聖經挪亞、中國鯀禹治水、希臘杜卡利翁、印度摩蹉、馬雅《波波爾·烏》、北歐 Ymir 血 flood |
| **眾神之山** | 希臘奧林帕斯、印度須彌山、中國崑崙山、北歐阿斯嘉特、日本高天原 |
| **語言變亂** | 巴別塔、非洲諸部落的語言分散神話、美索不達米亞 Enmerkar 史詩 |
| **巨蛇與龍** | 北歐耶夢加得、中國應龍/燭龍、印度那伽、中美洲羽蛇神、埃及阿佩普 |
| **世界樹** | 北歐 Yggdrasil、中國建木/若木、西伯利亞世界樹、印度宇宙樹 |
| **原始巨人** | 北歐 Ymir、中國盤古、印度原人 Purusha、波斯 Gayomart |
| **失落的陸塊** | 亞特蘭提斯（柏拉圖）、雷姆利亞（印度洋神話學）、姆大陸（太平洋） |
| **冥界之旅** | 埃及《死者之書》、希臘奧菲斯、日本黃泉國、中國泰山府君、馬雅 Xibalba |
| **洪水後文明傳承** | 七位智者（美索不達米亞）、諾亞三子、伏羲女媧、大禹九鼎 |
| **地磁極移與天傾** | 中國共工怒觸不周山「天傾西北、地陷東南」、希臘法厄同、埃及 Nut 與 Geb 分離、北歐世界傾斜 |

## 研究方法論

本專案遵循以下原則：

1. **結構比較法** — 不只看表面的故事差異，而是萃取深層結構（motif-index 方法）
2. **跨學科整合** — 神話學 × 考古學 × 語言學 × 地質學 × 天文考古學
3. **多元文化平等** — 不做「文明中心主義」判斷，口傳文化與文字文明同等重要
4. **開放溯源** — 可複查的原始文獻引用，鼓勵提出假設與反駁
5. **反殖民視角** — 正視歐洲中心論對神話研究的扭曲，還原各地文明的真實聲音

## 目錄結構

```
mythos-atlas/
├── README.md                 # 本文件：精神脈絡與總綱
├── AGENTS.md                 # AI 協作指南（逐步充實排程用）
├── cultures/                 # 各文化神話深度研究（依文化分類）
│   ├── 00-index.md           # 文化索引總表
│   ├── chinese/              # 中國上古神話
│   ├── mesopotamian/         # 美索不達米亞
│   ├── greek/                # 希臘神話
│   ├── egyptian/             # 埃及神話
│   ├── norse/                # 北歐神話
│   ├── hindu/                # 印度神話
│   ├── mayan/                # 馬雅神話
│   ├── polynesian/           # 波利尼西亞
│   ├── japanese/             # 日本神話
│   ├── african/              # 非洲諸文化
│   ├── indigenous-americas/  # 美洲原住民
│   ├── slavic/               # 斯拉夫神話
│   ├── celtic/               # 凱爾特神話
│   ├── finno-ugric/          # 芬蘭-烏戈爾神話
│   ├── korean/               # 韓國神話
│   ├── persian/              # 波斯神話
│   ├── tibetan/              # 西藏神話
│   └── ...more
├── themes/                   # 跨文化主題分析
│   ├── 00-index.md
│   ├── great-flood.md
│   ├── mountain-of-gods.md
│   ├── world-tree.md
│   ├── dragons-and-serpents.md
│   ├── language-confusion.md
│   ├── afterlife-journey.md
│   ├── lost-continents.md
│   ├── magnetic-pole-shift.md
│   ├── creation-myths.md
│   ├── primordial-giants.md
│   ├── solar-cults.md
│   ├── sacred-marriage.md
│   └── ...more
├── analyses/                 # 綜合比較分析文章
├── references/               # 文獻與參考資料
│   ├── primary-sources.md    # 原始文獻索引
│   ├── secondary-sources.md  # 現代學術研究
│   └── cross-ref.md          # 跨文化對照表
└── daemon.sh                 # （已棄用）僅提示 populate.py 已不再適用
```

## 內容充實方式

本資料庫由 LLM 協作逐步深化。優先填充模板生成的空殼頁面（gods/、stories/、comparisons/），詳見 `AGENTS.md` 的工作流程。

## 如何參與

- **直接閱讀** — clone 或瀏覽 cultures/ 與 themes/ 目錄
- **提供修正** — 開 Issue 或 PR 補充缺漏的文化視角
- **建議來源** — 如果你知道特定的原始文獻或學術著作，歡迎在 references/ 貢獻

<!-- STATS_START -->

## 📊 當前狀態

> 自動更新於 2026-08-03 18:38 UTC

| 類別 | 進度 |
|------|------|
| 文化體系 | 44/44 |
| 跨文化主題 | 27/27 |
| 分析文章 | 396 |
| 已充實文化 | 44/44 |
| 總頁面數 | 2812 |
| 總執行次數 | 74 |

<!-- STATS_END -->

<!-- CULTURES_START -->

## 🌍 已收錄文化

| 文化 | 區域 | 神祇 | 故事 | 比較 |
|------|------|------|------|------|
| [中國上古神話](cultures/chinese/) | 東亞 | 9 | 11 | 7 |
| [美索不達米亞神話](cultures/mesopotamian/) | 兩河流域 | 9 | 7 | 6 |
| [希臘神話](cultures/greek/) | 地中海—巴爾幹 | 11 | 7 | 5 |
| [埃及神話](cultures/egyptian/) | 北非—尼羅河流域 | 10 | 7 | 6 |
| [北歐神話](cultures/norse/) | 北歐—日耳曼 | 10 | 8 | 6 |
| [印度神話](cultures/hindu/) | 南亞—印度河流域 | 11 | 8 | 7 |
| [馬雅神話](cultures/mayan/) | 中美洲 | 21 | 16 | 14 |
| [日本神話](cultures/japanese/) | 東亞—日本列島 | 20 | 17 | 15 |
| [波利尼西亞神話](cultures/polynesian/) | 太平洋島嶼 | 11 | 8 | 8 |
| [澳洲原住民神話](cultures/aboriginal/) | 大洋洲—澳洲 | 10 | 8 | 6 |
| [非洲諸神話](cultures/african/) | 撒哈拉以南非洲 | 19 | 16 | 14 |
| [美洲原住民神話](cultures/indigenous-americas/) | 北美洲 | 9 | 8 | 5 |
| [印加神話](cultures/incan/) | 南美洲—安地斯山脈 | 10 | 7 | 7 |
| [凱爾特神話](cultures/celtic/) | 西歐—愛爾蘭/不列顛/高盧 | 9 | 7 | 5 |
| [斯拉夫神話](cultures/slavic/) | 東歐—巴爾幹 | 11 | 6 | 5 |
| [波斯神話](cultures/persian/) | 伊朗高原 | 18 | 17 | 17 |
| [韓國神話](cultures/korean/) | 東亞—朝鮮半島 | 10 | 9 | 8 |
| [芬蘭-烏戈爾神話](cultures/finno-ugric/) | 北歐—烏拉爾地區 | 11 | 8 | 8 |
| [西藏神話](cultures/tibetan/) | 青藏高原 | 9 | 7 | 7 |
| [蘇美神話](cultures/sumerian/) | 美索不達米亞南部 | 20 | 17 | 16 |
| [腓尼基神話](cultures/phoenician/) | 黎凡特—迦南 | 10 | 7 | 7 |
| [赫梯神話](cultures/hittite/) | 安納托利亞 | 9 | 6 | 6 |
| [約魯巴神話](cultures/yoruba/) | 西非—奈及利亞/貝南 | 18 | 16 | 16 |
| [蒙古神話](cultures/mongolian/) | 中亞—蒙古高原 | 11 | 8 | 7 |
| [愛努神話](cultures/ainu/) | 北海道—庫頁島—千島群島 | 10 | 7 | 7 |
| [伊特魯里亞神話](cultures/etruscan/) | 義大利—托斯卡尼 | 9 | 7 | 6 |
| [巴斯克神話](cultures/basque/) | 西歐—庇里牛斯山脈 | 11 | 9 | 9 |
| [波羅的神話](cultures/baltic/) | 東歐—波羅的海沿岸 | 8 | 7 | 6 |
| [越南神話](cultures/vietnamese/) | 東南亞—紅河流域 | 10 | 10 | 10 |
| [因紐特神話](cultures/inuit/) | 北極—阿拉斯加/加拿大/格陵蘭 | 9 | 7 | 6 |
| [亞美尼亞神話](cultures/armenian/) | 南高加索—亞美尼亞高原 | 9 | 7 | 7 |
| [菲律賓神話](cultures/philippine/) | 東南亞—菲律賓群島 | 9 | 7 | 6 |
| [高加索神話](cultures/caucasian/) | 高加索山脈(奧塞提亞/切爾克斯/阿布哈茲) | 9 | 6 | 6 |
| [達基亞/羅馬尼亞神話](cultures/dacian/) | 東南歐—喀爾巴阡山脈 | 10 | 11 | 6 |
| [羅馬神話](cultures/roman/) | 地中海—義大利半島 | 12 | 6 | 6 |
| [前伊斯蘭阿拉伯神話](cultures/pre-islamic-arabian/) | 阿拉伯半島 | 10 | 7 | 7 |
| [毛利神話](cultures/maori/) | 紐西蘭—玻里尼西亞三角 | 10 | 6 | 6 |
| [斯基泰神話](cultures/scythian/) | 歐亞草原—黑海北岸至阿爾泰 | 11 | 7 | 6 |
| [米諾斯神話](cultures/minoan/) | 愛琴海—克里特島 | 10 | 7 | 7 |
| [努比亞/庫什神話](cultures/nubian/) | 東北非—尼羅河上游/蘇丹 | 10 | 8 | 8 |
| [馬普切神話](cultures/mapuche/) | 南美洲—智利/阿根廷 | 10 | 8 | 6 |
| [薩米神話](cultures/sami/) | 北歐—芬諾斯堪的亞 | 10 | 9 | 7 |
| [西伯利亞神話](cultures/siberian/) | 西伯利亞—通古斯/雅庫特/楚科奇 | 9 | 9 | 4 |
| [圖皮-瓜拉尼神話](cultures/tupi-guarani/) | 南美洲—巴西/巴拉圭/玻利維亞 | 18 | 17 | 16 |

<!-- CULTURES_END -->

<!-- ANALYSES_START -->

## 📝 分析文章

> 跨文化比較神話學分析文章。共 396 篇。

- [螺音迴盪山海：海螺與子安貝神話跨文化比較](analyses/conch-cowrie-shell-myths-comparative.md)
- [依依垂枝，仙凡之木：柳樹神話跨文化比較](analyses/willow-mythology-comparative.md)
- [推著太陽的蟲：糞金龜與聖甲蟲神話跨文化比較](analyses/scarab-dung-beetle-myths-comparative.md)
- [雷鳴之鳥與樹木之言：啄木鳥神話跨文化比較](analyses/woodpecker-myths-comparative.md)
- [飛越眾神與人間：鵝與大雁神話跨文化比較](analyses/goose-myths-comparative.md)
- [蛻殼與長鳴：蟬神話跨文化比較](analyses/cicada-myths-comparative.md)
- [橫行之甲：螃蟹神話跨文化比較](analyses/crab-myths-comparative.md)
- [天極之輪：北斗七星（大熊座）跨文化神話比較](analyses/big-dipper-constellation-myths-comparative.md)
- [Octopus Cephalopod Myths Comparative](analyses/octopus-cephalopod-myths-comparative.md)
- [Vulture Myths Comparative](analyses/vulture-myths-comparative.md)
- [Echo Myths Comparative](analyses/echo-myths-comparative.md)
- [Wild Man Myths Comparative](analyses/wild-man-myths-comparative.md)
- [通曉鳥語與動物之語：跨文化比較神話學研究](analyses/animal-language-bird-speech-comparative.md)
- [聖林跨文化神聖樹林崇拜比較分析](analyses/聖林跨文化神聖樹林崇拜比較分析.md)
- [Zodiac Astrology Myths Comparative](analyses/zodiac-astrology-myths-comparative.md)
- [Wounded Sovereign Fisher King Comparative](analyses/wounded-sovereign-fisher-king-comparative.md)
- [Wounded Healer Comparative](analyses/wounded-healer-comparative.md)
- [World Tree Comparative](analyses/world-tree-comparative.md)
- [World Serpent Cosmic Encircler Comparative](analyses/world-serpent-cosmic-encircler-comparative.md)
- [World Parents Separation](analyses/world-parents-separation.md)
- [World Mountain Axis Mundi Comparative](analyses/world-mountain-axis-mundi-comparative.md)
- [World Ages Cosmic Cycles Comparative](analyses/world-ages-cosmic-cycles-comparative.md)
- [Wisdom Gods Comparative](analyses/wisdom-gods-comparative.md)
- [Wind Deities Comparative](analyses/wind-deities-comparative.md)
- [Wild Hunt Spectral Procession](analyses/wild-hunt-spectral-procession.md)
- [Whirlpool Vortex Myths](analyses/whirlpool-vortex-myths.md)
- [Wheel Mythology Comparative](analyses/wheel-mythology-comparative.md)
- [Whale Leviathan Great Fish Comparative](analyses/whale-leviathan-great-fish-comparative.md)
- [Water Of Life Myths Comparative](analyses/water-of-life-myths-comparative.md)
- [Warrior Women Amazons Comparative](analyses/warrior-women-amazons-comparative.md)
- [War Gods Comparative](analyses/war-gods-comparative.md)
- [Volcano Fire Mountain Myths](analyses/volcano-fire-mountain-myths.md)
- [Venus Morning Evening Star Comparative](analyses/venus-morning-evening-star-comparative.md)
- [Veil Sacred Covering Comparative](analyses/veil-sacred-covering-comparative.md)
- [Vampiric Entities Comparative](analyses/vampiric-entities-comparative.md)
- [Unicorn Qilin Comparative](analyses/unicorn-qilin-comparative.md)
- [Underworld Rivers Comparative](analyses/underworld-rivers-comparative.md)
- [Underworld Journey](analyses/underworld-journey.md)
- [Underworld Descent Katabasis Comparative](analyses/underworld-descent-katabasis-comparative.md)
- [Umbilical Cord Cosmic Connection Comparative](analyses/umbilical-cord-cosmic-connection-comparative.md)
- [Twin Myths](analyses/twin-myths.md)
- [Twilight Dusk Deities Comparative](analyses/twilight-dusk-deities-comparative.md)
- [Turtle Myths Comparative](analyses/turtle-myths-comparative.md)
- [Triune Deities Comparative](analyses/triune-deities-comparative.md)
- [Trickster Archetype Comparative](analyses/trickster-archetype-comparative.md)
- [Trickster Across Cultures](analyses/trickster-across-cultures.md)
- [Tornado Whirlwind Myths Comparative](analyses/tornado-whirlwind-myths-comparative.md)
- [Time Distortion Otherworld Comparative](analyses/time-distortion-otherworld-comparative.md)
- [Tiger Myths Comparative](analyses/tiger-myths-comparative.md)
- [Tidal Wave Myths Comparative](analyses/tidal-wave-myths-comparative.md)
- [Thunderbird Lightning Bird Comparative](analyses/thunderbird-lightning-bird-comparative.md)
- [Thunder Gods](analyses/thunder-gods.md)
- [Threshold Crossroads Gods](analyses/threshold-crossroads-gods.md)
- [Three Tiered Cosmos Comparative](analyses/three-tiered-cosmos-comparative.md)
- [Teeth Myths Comparative](analyses/teeth-myths-comparative.md)
- [Tears Weeping Myths Comparative](analyses/tears-weeping-myths-comparative.md)
- [Tea Coffee Origin Myths Comparative](analyses/tea-coffee-origin-myths-comparative.md)
- [Taboo Transgression Comparative](analyses/taboo-transgression-comparative.md)
- [Taboo Breaking Myths Comparative](analyses/taboo-breaking-myths-comparative.md)
- [Swine Boar Myths Comparative](analyses/swine-boar-myths-comparative.md)
- [Swan Maiden Celestial Bride](analyses/swan-maiden-celestial-bride.md)
- [Swallow Myths Comparative](analyses/swallow-myths-comparative.md)
- [Sun Snaring Myths Comparative](analyses/sun-snaring-myths-comparative.md)
- [Sun Myths](analyses/sun-myths.md)
- [Sun Moon Conflict Comparative](analyses/sun-moon-conflict-comparative.md)
- [Steppe Grassland Mythology Comparative](analyses/steppe-grassland-mythology-comparative.md)
- [Spider Weaving Myths](analyses/spider-weaving-myths.md)
- [Sphinx Cross Cultural Comparative](analyses/sphinx-cross-cultural-comparative.md)
- [Sparagmos Dismemberment Comparative](analyses/sparagmos-dismemberment-comparative.md)
- [Soul Ferry Boat Of Dead Comparative](analyses/soul-ferry-boat-of-dead-comparative.md)
- [Soul Concepts Comparative](analyses/soul-concepts-comparative.md)
- [Solstice Equinox Rituals](analyses/solstice-equinox-rituals.md)
- [Solar Years And Kingly Reigns](analyses/solar-years-and-kingly-reigns.md)
- [Smith Forge Gods Comparative](analyses/smith-forge-gods-comparative.md)
- [Sleeping King Mountain](analyses/sleeping-king-mountain.md)
- [Sleep Dreams Mythology](analyses/sleep-dreams-mythology.md)
- [Sky Ladder Heaven Ladder Comparative](analyses/sky-ladder-heaven-ladder-comparative.md)
- [Sky Father Archetype Comparative](analyses/sky-father-archetype-comparative.md)
- [Sirius Dog Star Cross Cultural](analyses/sirius-dog-star-cross-cultural.md)
- [Siren Enchantress Femme Fatale Comparative](analyses/siren-enchantress-femme-fatale-comparative.md)
- [Silk Sericulture Myths Comparative](analyses/silk-sericulture-myths-comparative.md)
- [Sibling Rivalry Fraternal Conflict Comparative](analyses/sibling-rivalry-fraternal-conflict-comparative.md)
- [Shepherd Mythology Comparative](analyses/shepherd-mythology-comparative.md)
- [Shamanism In Myth](analyses/shamanism-in-myth.md)
- [Shark Myths Comparative](analyses/shark-myths-comparative.md)
- [Salmon Myths Comparative](analyses/salmon-myths-comparative.md)
- [Shadow Soul Second Self Comparative](analyses/shadow-soul-second-self-comparative.md)
- [Serpent Venom Divine Medicine Comparative](analyses/serpent-venom-divine-medicine-comparative.md)
- [Separation Of Heaven And Earth Comparative](analyses/separation-of-heaven-and-earth-comparative.md)
- [Seasonal Deities Comparative](analyses/seasonal-deities-comparative.md)
- [Sea Deities Ocean Myths](analyses/sea-deities-ocean-myths.md)
- [Scorpion Myths Comparative](analyses/scorpion-myths-comparative.md)
- [Scapegoat Pharmakos Comparative](analyses/scapegoat-pharmakos-comparative.md)
- [Salt Symbolism Comparative](analyses/salt-symbolism-comparative.md)
- [Sacrificial Creation](analyses/sacrificial-creation.md)
- [Sacred Wounds Cosmic Injury Comparative](analyses/sacred-wounds-cosmic-injury-comparative.md)
- [Sacred Wells Springs Comparative](analyses/sacred-wells-springs-comparative.md)
- [Sacred Weaving Fate Textiles Comparative](analyses/sacred-weaving-fate-textiles-comparative.md)
- [Sacred Waters Springs](analyses/sacred-waters-springs.md)
- [Sacred Wasteland Barren Land Comparative](analyses/sacred-wasteland-barren-land-comparative.md)
- [Sacred Torch Lamp Mythology Comparative](analyses/sacred-torch-lamp-mythology-comparative.md)
- [Sacred Tattooing Mythology](analyses/sacred-tattooing-mythology.md)
- [Sacred Stones Meteorites Mythology](analyses/sacred-stones-meteorites-mythology.md)
- [Sacred Spittle Divine Saliva Comparative](analyses/sacred-spittle-divine-saliva-comparative.md)
- [Sacred Spirals Mythology Comparative](analyses/sacred-spirals-mythology-comparative.md)
- [Sacred Silence Muteness Myths Comparative](analyses/sacred-silence-muteness-myths-comparative.md)
- [Sacred Sexuality Divine Eroticism Comparative](analyses/sacred-sexuality-divine-eroticism-comparative.md)
- [Sacred Seed Mythology Comparative](analyses/sacred-seed-mythology-comparative.md)
- [Sacred Rivers Myths](analyses/sacred-rivers-myths.md)
- [Sacred Ring Myths Comparative](analyses/sacred-ring-myths-comparative.md)
- [Sacred Reed Cross Cultural Comparative](analyses/sacred-reed-cross-cultural-comparative.md)
- [Sacred Prostitution Cross Cultural](analyses/sacred-prostitution-cross-cultural.md)
- [Sacred Plants Entheogens](analyses/sacred-plants-entheogens.md)
- [Sacred Orientation Four Directions Comparative](analyses/sacred-orientation-four-directions-comparative.md)
- [Sacred Numbers Cosmic Order](analyses/sacred-numbers-cosmic-order.md)
- [Sacred Name Power Naming](analyses/sacred-name-power-naming.md)
- [Sacred Nakedness Ritual Nudity Comparative](analyses/sacred-nakedness-ritual-nudity-comparative.md)
- [Sacred Mountains](analyses/sacred-mountains.md)
- [Sacred Milk Myths Comparative](analyses/sacred-milk-myths-comparative.md)
- [Sacred Metals Comparative](analyses/sacred-metals-comparative.md)
- [Sacred Mead Divine Nectar Comparative](analyses/sacred-mead-divine-nectar-comparative.md)
- [Sacred Masks Mythology](analyses/sacred-masks-mythology.md)
- [Sacred Marriage Across Cultures](analyses/sacred-marriage-across-cultures.md)
- [Sacred Lakes World Mythology](analyses/sacred-lakes-world-mythology.md)
- [Sacred Knots Binding Comparative](analyses/sacred-knots-binding-comparative.md)
- [Sacred Kingship Comparative](analyses/sacred-kingship-comparative.md)
- [Sacred Key Mythology Comparative](analyses/sacred-key-mythology-comparative.md)
- [Sacred Islands Blessed Isles Comparative](analyses/sacred-islands-blessed-isles-comparative.md)
- [Sacred Intoxication Wine Beer Myths](analyses/sacred-intoxication-wine-beer-myths.md)
- [Sacred Inscribed Objects Destiny Comparative](analyses/sacred-inscribed-objects-destiny-comparative.md)
- [Sacred Hunt Comparative](analyses/sacred-hunt-comparative.md)
- [Sacred Hand Cross Cultural](analyses/sacred-hand-cross-cultural.md)
- [Sacred Grain Bread Myths Comparative](analyses/sacred-grain-bread-myths-comparative.md)
- [Sacred Geometry Cross Cultural Comparative](analyses/sacred-geometry-cross-cultural-comparative.md)
- [Sacred Geography Cross Cultural Comparative](analyses/sacred-geography-cross-cultural-comparative.md)
- [Sacred Gates Portals Thresholds Comparative](analyses/sacred-gates-portals-thresholds-comparative.md)
- [Sacred Garment Clothing Myths Comparative](analyses/sacred-garment-clothing-myths-comparative.md)
- [Sacred Gardens Comparative](analyses/sacred-gardens-comparative.md)
- [Sacred Frenzy Divine Madness Comparative](analyses/sacred-frenzy-divine-madness-comparative.md)
- [Sacred Footprints Comparative](analyses/sacred-footprints-comparative.md)
- [Sacred Fire Eternal Flame](analyses/sacred-fire-eternal-flame.md)
- [Sacred Feast Banquet Comparative](analyses/sacred-feast-banquet-comparative.md)
- [Sacred Exile Return Myths](analyses/sacred-exile-return-myths.md)
- [Sacred Elephant Myths Comparative](analyses/sacred-elephant-myths-comparative.md)
- [Sacred Drums Comparative](analyses/sacred-drums-comparative.md)
- [Sacred Dance Mythology](analyses/sacred-dance-mythology.md)
- [Sacred Cord Thread Myths Comparative](analyses/sacred-cord-thread-myths-comparative.md)
- [Sacred Cauldron Vessel Myths](analyses/sacred-cauldron-vessel-myths.md)
- [Sacred Cat Myths Comparative](analyses/sacred-cat-myths-comparative.md)
- [Sacred Blood Mythology](analyses/sacred-blood-mythology.md)
- [Sacred Bells Comparative](analyses/sacred-bells-comparative.md)
- [Sacred Axe Labrys Cross Cultural](analyses/sacred-axe-labrys-cross-cultural.md)
- [Sacred Ash Holy Dust Comparative](analyses/sacred-ash-holy-dust-comparative.md)
- [Sacred Asceticism Fasting Comparative](analyses/sacred-asceticism-fasting-comparative.md)
- [Sacred Architecture Temple Myths](analyses/sacred-architecture-temple-myths.md)
- [Sacred Anointing Oil Myths Comparative](analyses/sacred-anointing-oil-myths-comparative.md)
- [Sacred Animals Divine Messengers Comparative](analyses/sacred-animals-divine-messengers-comparative.md)
- [Rooster Myths Comparative](analyses/rooster-myths-comparative.md)
- [Ritual Combat Sacred Warfare Comparative](analyses/ritual-combat-sacred-warfare-comparative.md)
- [Rice Myths Comparative](analyses/rice-myths-comparative.md)
- [Resurrection Comparative](analyses/resurrection-comparative.md)
- [Reincarnation Metempsychosis](analyses/reincarnation-metempsychosis.md)
- [Ravens Crows Mythology](analyses/ravens-crows-mythology.md)
- [Rainbow Serpent Myths Comparative](analyses/rainbow-serpent-myths-comparative.md)
- [Rainbow Myths](analyses/rainbow-myths.md)
- [Rain Gods Rainmaking Comparative](analyses/rain-gods-rainmaking-comparative.md)
- [Rabbit Hare Myths Comparative](analyses/rabbit-hare-myths-comparative.md)
- [Rat Mouse Myths Comparative](analyses/rat-mouse-myths-comparative.md)
- [Quest For Lost Wife Comparative](analyses/quest-for-lost-wife-comparative.md)
- [Quest For Immortality Comparative](analyses/quest-for-immortality-comparative.md)
- [Purification Rites Comparative](analyses/purification-rites-comparative.md)
- [Psychostasia Judgment Of The Dead](analyses/psychostasia-judgment-of-the-dead.md)
- [Psychopomp Comparative](analyses/psychopomp-comparative.md)
- [Primordial Void Abyss Myths Comparative](analyses/primordial-void-abyss-myths-comparative.md)
- [Primordial Transgression Comparative](analyses/primordial-transgression-comparative.md)
- [Primordial Mound First Land](analyses/primordial-mound-first-land.md)
- [Pomegranate Myths Comparative](analyses/pomegranate-myths-comparative.md)
- [Pole Star Cosmic Axis Myths](analyses/pole-star-cosmic-axis-myths.md)
- [Poison Venom Mythology Comparative](analyses/poison-venom-mythology-comparative.md)
- [Pleiades Seven Sisters Cross Cultural](analyses/pleiades-seven-sisters-cross-cultural.md)
- [Planetary Cycles And Deities](analyses/planetary-cycles-and-deities.md)
- [Plague Deities Disease Myths Comparative](analyses/plague-deities-disease-myths-comparative.md)
- [Petrification Myths Comparative](analyses/petrification-myths-comparative.md)
- [Pearls Gems Sacred Jewels](analyses/pearls-gems-sacred-jewels.md)
- [Peacock Myths Comparative](analyses/peacock-myths-comparative.md)
- [Owl Myths Comparative](analyses/owl-myths-comparative.md)
- [Ouroboros Eternal Return](analyses/ouroboros-eternal-return.md)
- [Otter Myths Comparative](analyses/otter-myths-comparative.md)
- [Orphan Exposed Hero Comparative](analyses/orphan-exposed-hero-comparative.md)
- [Orion Constellation Myths Comparative](analyses/orion-constellation-myths-comparative.md)
- [Origin Of Writing Myths](analyses/origin-of-writing-myths.md)
- [Origin Of Death](analyses/origin-of-death.md)
- [Oracle Prophecy Divination Myths](analyses/oracle-prophecy-divination-myths.md)
- [Omphalos Navel Stone Myths Comparative](analyses/omphalos-navel-stone-myths-comparative.md)
- [Oaths Curses Myths](analyses/oaths-curses-myths.md)
- [Nightmare Incubus Succubus Cross Cultural](analyses/nightmare-incubus-succubus-cross-cultural.md)
- [Night Darkness Deities Comparative](analyses/night-darkness-deities-comparative.md)
- [New Year Cosmic Renewal Myths Comparative](analyses/new-year-cosmic-renewal-myths-comparative.md)
- [Mythological Catastrophe Timeline](analyses/mythological-catastrophe-timeline.md)
- [Mythical Ships Boats Comparative](analyses/mythical-ships-boats-comparative.md)
- [Music Origin Myths](analyses/music-origin-myths.md)
- [Mushroom Fungus Mythology Comparative](analyses/mushroom-fungus-mythology-comparative.md)
- [Moon Rabbit Jade Hare Comparative](analyses/moon-rabbit-jade-hare-comparative.md)
- [Moon Myths](analyses/moon-myths.md)
- [Monkey Ape Comparative](analyses/monkey-ape-comparative.md)
- [Mistletoe Golden Bough Comparative](analyses/mistletoe-golden-bough-comparative.md)
- [Mirror Reflection Myths](analyses/mirror-reflection-myths.md)
- [Mirror Divination Catoptromancy Comparative](analyses/mirror-divination-catoptromancy-comparative.md)
- [Mirage Phantom Landscape Myths Comparative](analyses/mirage-phantom-landscape-myths-comparative.md)
- [Miraculous Birth Virgin Conception](analyses/miraculous-birth-virgin-conception.md)
- [Milky Way Origin Myths](analyses/milky-way-origin-myths.md)
- [Metamorphosis Shapeshifting](analyses/metamorphosis-shapeshifting.md)
- [Mermaid Aquatic Humanoids](analyses/mermaid-aquatic-humanoids.md)
- [Mentor Wise Teacher Comparative](analyses/mentor-wise-teacher-comparative.md)
- [Menstrual Taboos Myths Comparative](analyses/menstrual-taboos-myths-comparative.md)
- [Memory Forgetfulness Underworld Comparative](analyses/memory-forgetfulness-underworld-comparative.md)
- [Megalithic Building Myths Comparative](analyses/megalithic-building-myths-comparative.md)
- [Master Of Animals Comparative](analyses/master-of-animals-comparative.md)
- [Mana Supernatural Power Comparative](analyses/mana-supernatural-power-comparative.md)
- [Maize Myths Comparative](analyses/maize-myths-comparative.md)
- [Mantis Praying Insect Myths Comparative](analyses/mantis-praying-insect-myths-comparative.md)
- [Magnetic Pole Shift Comparative](analyses/magnetic-pole-shift-comparative.md)
- [Magic Witchcraft Comparative](analyses/magic-witchcraft-comparative.md)
- [Magic Flight Obstacle Pursuit Comparative](analyses/magic-flight-obstacle-pursuit-comparative.md)
- [Lycanthropy Werewolf Comparative](analyses/lycanthropy-werewolf-comparative.md)
- [Lunar Calendars In Myth](analyses/lunar-calendars-in-myth.md)
- [Love Deities Comparative](analyses/love-deities-comparative.md)
- [Lotus Cross Cultural Myth Comparison](analyses/lotus-cross-cultural-myth-comparison.md)
- [Lost Continents Comparative](analyses/lost-continents-comparative.md)
- [Living Dead Revenant Zombie Comparative](analyses/living-dead-revenant-zombie-comparative.md)
- [Lion Myths Comparative](analyses/lion-myths-comparative.md)
- [Lizard Gecko Myths Comparative](analyses/lizard-gecko-myths-comparative.md)
- [Light Myths Primordial Light Enlightenment Comparative](analyses/light-myths-primordial-light-enlightenment-comparative.md)
- [Left Right Handedness Symbolism](analyses/left-right-handedness-symbolism.md)
- [Language Confusion Myths](analyses/language-confusion-myths.md)
- [Labyrinth Spiral Myths](analyses/labyrinth-spiral-myths.md)
- [Justice Law Comparative](analyses/justice-law-comparative.md)
- [Iron Mythology Comparative](analyses/iron-mythology-comparative.md)
- [Invisibility Myths Comparative](analyses/invisibility-myths-comparative.md)
- [Insects Myths Comparative](analyses/insects-myths-comparative.md)
- [Initiation Rites Of Passage](analyses/initiation-rites-of-passage.md)
- [Indo European Myth Connections](analyses/indo-european-myth-connections.md)
- [Incense Sacred Smoke Comparative](analyses/incense-sacred-smoke-comparative.md)
- [Immortal Bird Phoenix](analyses/immortal-bird-phoenix.md)
- [Ice Snow Myths Comparative](analyses/ice-snow-myths-comparative.md)
- [Hydromancy Water Divination Comparative](analyses/hydromancy-water-divination-comparative.md)
- [Hummingbird Mythology Comparative](analyses/hummingbird-mythology-comparative.md)
- [Hospitality Xenia Theoxenia](analyses/hospitality-xenia-theoxenia.md)
- [Horse Myths](analyses/horse-myths.md)
- [Horn Myths Comparative](analyses/horn-myths-comparative.md)
- [Hoopoe Myths Comparative](analyses/hoopoe-myths-comparative.md)
- [Heros Journey Monomyth](analyses/heros-journey-monomyth.md)
- [Hero Wound Vulnerability Motif](analyses/hero-wound-vulnerability-motif.md)
- [Hearth Fire Domestic Myths Comparative](analyses/hearth-fire-domestic-myths-comparative.md)
- [Heart Symbolism Mythology Comparative](analyses/heart-symbolism-mythology-comparative.md)
- [Healing Medicine Myths](analyses/healing-medicine-myths.md)
- [Head Skull Myths Comparative](analyses/head-skull-myths-comparative.md)
- [Hair Symbolism Mythology Comparative](analyses/hair-symbolism-mythology-comparative.md)
- [Griffin Gryphon Cross Cultural](analyses/griffin-gryphon-cross-cultural.md)
- [Golden Age Paradise Myths](analyses/golden-age-paradise-myths.md)
- [Goat Ram Myths Comparative](analyses/goat-ram-myths-comparative.md)
- [Giant Myths Comparative](analyses/giant-myths-comparative.md)
- [Ghosts Restless Dead Comparative](analyses/ghosts-restless-dead-comparative.md)
- [Frog Toad Myths Comparative](analyses/frog-toad-myths-comparative.md)
- [Fox Spirits Comparative](analyses/fox-spirits-comparative.md)
- [Founding Child Exposed Hero Comparative](analyses/founding-child-exposed-hero-comparative.md)
- [Foundation Sacrifice Immurement](analyses/foundation-sacrifice-immurement.md)
- [Fossils Myth Geomythology Comparative](analyses/fossils-myth-geomythology-comparative.md)
- [Forbidden Lovers Comparative](analyses/forbidden-lovers-comparative.md)
- [Forbidden Container Curiosity Taboo Comparative](analyses/forbidden-container-curiosity-taboo-comparative.md)
- [Flower Myths Comparative](analyses/flower-myths-comparative.md)
- [Flood Myths Geological Origins](analyses/flood-myths-geological-origins.md)
- [Fish Myths Comparative](analyses/fish-myths-comparative.md)
- [Firefly Glowworm Myths Comparative](analyses/firefly-glowworm-myths-comparative.md)
- [First Woman Creation Comparative](analyses/first-woman-creation-comparative.md)
- [First Murder Fratricide](analyses/first-murder-fratricide.md)
- [Fire Theft Promethean Motif](analyses/fire-theft-promethean-motif.md)
- [Fire Myths](analyses/fire-myths.md)
- [Fertility Deities Comparative](analyses/fertility-deities-comparative.md)
- [Female Deities](analyses/female-deities.md)
- [Feline Myths Comparative](analyses/feline-myths-comparative.md)
- [Feathers Wings Flight Symbolism Comparative](analyses/feathers-wings-flight-symbolism-comparative.md)
- [Father Son Conflict Mythology Comparative](analyses/father-son-conflict-mythology-comparative.md)
- [Fate Goddesses Destiny](analyses/fate-goddesses-destiny.md)
- [Fallen Bound Gods](analyses/fallen-bound-gods.md)
- [Eye Symbolism Comparative](analyses/eye-symbolism-comparative.md)
- [External Soul Life Token Comparative](analyses/external-soul-life-token-comparative.md)
- [Evil Eye Comparative](analyses/evil-eye-comparative.md)
- [Eternal Punishment Comparative](analyses/eternal-punishment-comparative.md)
- [Eschatology Apocalyptic Myths](analyses/eschatology-apocalyptic-myths.md)
- [Eclipse Myths](analyses/eclipse-myths.md)
- [Earthquake Myths Comparative](analyses/earthquake-myths-comparative.md)
- [Earth Diver Global Myth Complex](analyses/earth-diver-global-myth-complex.md)
- [Eagle Birds Of Prey Myths](analyses/eagle-birds-of-prey-myths.md)
- [Dying And Rising Gods](analyses/dying-and-rising-gods.md)
- [Dwarf Elf Spirit Beings](analyses/dwarf-elf-spirit-beings.md)
- [Drought Famine Myths Comparative](analyses/drought-famine-myths-comparative.md)
- [Dream Mythology Comparative](analyses/dream-mythology-comparative.md)
- [Dream Incubation Sacred Sleep](analyses/dream-incubation-sacred-sleep.md)
- [Dragons And Serpents Global](analyses/dragons-and-serpents-global.md)
- [Dragonfly Myths Comparative](analyses/dragonfly-myths-comparative.md)
- [Dove Pigeon Myths Comparative](analyses/dove-pigeon-myths-comparative.md)
- [Dolphins World Mythology Comparative](analyses/dolphins-world-mythology-comparative.md)
- [Dogs Wolves Mythology](analyses/dogs-wolves-mythology.md)
- [Donkey Myths Comparative](analyses/donkey-myths-comparative.md)
- [Divine Weapons Armaments Comparative](analyses/divine-weapons-armaments-comparative.md)
- [Divine Wager Cosmic Bet Comparative](analyses/divine-wager-cosmic-bet-comparative.md)
- [Divine Twins Comparative](analyses/divine-twins-comparative.md)
- [Divine Thrones Comparative](analyses/divine-thrones-comparative.md)
- [Divine Staff Scepter Myths Comparative](analyses/divine-staff-scepter-myths-comparative.md)
- [Divine Smith Comparative](analyses/divine-smith-comparative.md)
- [Divine Retribution Comparative](analyses/divine-retribution-comparative.md)
- [Divine Poetry Inspiration Comparative](analyses/divine-poetry-inspiration-comparative.md)
- [Divine Nectar Elixir Immortality](analyses/divine-nectar-elixir-immortality.md)
- [Divine Laughter Comparative](analyses/divine-laughter-comparative.md)
- [Divine Language Sacred Speech Comparative](analyses/divine-language-sacred-speech-comparative.md)
- [Divine Council Celestial Court Comparative](analyses/divine-council-celestial-court-comparative.md)
- [Divine Child Comparative](analyses/divine-child-comparative.md)
- [Divine Chariots Solar Vehicles Comparative](analyses/divine-chariots-solar-vehicles-comparative.md)
- [Divine Breath Vital Force Comparative](analyses/divine-breath-vital-force-comparative.md)
- [Divine Archery Comparative](analyses/divine-archery-comparative.md)
- [Divine Androgyny](analyses/divine-androgyny.md)
- [Deus Otiosus Retired High God Comparative](analyses/deus-otiosus-retired-high-god-comparative.md)
- [Desert Sacred Myths Comparative](analyses/desert-sacred-myths-comparative.md)
- [Demons Evil Spirits Comparative](analyses/demons-evil-spirits-comparative.md)
- [Deer Stag Myths Comparative](analyses/deer-stag-myths-comparative.md)
- [Dawn Deities Comparative](analyses/dawn-deities-comparative.md)
- [Cursed Treasure Hoard Mythology Comparative](analyses/cursed-treasure-hoard-mythology-comparative.md)
- [Cursed Bloodlines Generational Curse Comparative](analyses/cursed-bloodlines-generational-curse-comparative.md)
- [Culture Hero Comparative](analyses/culture-hero-comparative.md)
- [Cuckoo Myths Comparative](analyses/cuckoo-myths-comparative.md)
- [Crown Diadem Myths](analyses/crown-diadem-myths.md)
- [Crossroads Sacred Space Comparative](analyses/crossroads-sacred-space-comparative.md)
- [Crocodile Myths Comparative](analyses/crocodile-myths-comparative.md)
- [Cricket Myths Comparative](analyses/cricket-myths-comparative.md)
- [Creative Word Logos Comparative](analyses/creative-word-logos-comparative.md)
- [Creation Of Humans](analyses/creation-of-humans.md)
- [Crane Heron Stork Myths Comparative](analyses/crane-heron-stork-myths-comparative.md)
- [Cosmic Tree World Tree](analyses/cosmic-tree-world-tree.md)
- [Cosmic River Myths Comparative](analyses/cosmic-river-myths-comparative.md)
- [Cosmic Pillar World Pillar Comparative](analyses/cosmic-pillar-world-pillar-comparative.md)
- [Cosmic Ocean Primordial Waters](analyses/cosmic-ocean-primordial-waters.md)
- [Cosmic Mill Magic Millstone Comparative](analyses/cosmic-mill-magic-millstone-comparative.md)
- [Cosmic Hunt Comparative](analyses/cosmic-hunt-comparative.md)
- [Cosmic Hierarchy Guardianship Comparative](analyses/cosmic-hierarchy-guardianship-comparative.md)
- [Cosmic Harmony Music Of Spheres Comparative](analyses/cosmic-harmony-music-of-spheres-comparative.md)
- [Cosmic Game Divine Play Comparative](analyses/cosmic-game-divine-play-comparative.md)
- [Cosmic Egg](analyses/cosmic-egg.md)
- [Cosmic Egg Creation Myths Comparative](analyses/cosmic-egg-creation-myths-comparative.md)
- [Cosmic Egg Creation Myth Comparative](analyses/cosmic-egg-creation-myth-comparative.md)
- [Cosmic Dream World As Divine Dreaming Comparative](analyses/cosmic-dream-world-as-divine-dreaming-comparative.md)
- [Cosmic Dance Comparative](analyses/cosmic-dance-comparative.md)
- [Cosmic Churning Ocean Mining Myths](analyses/cosmic-churning-ocean-mining-myths.md)
- [Cosmic Chain Fettering Chaos Comparative](analyses/cosmic-chain-fettering-chaos-comparative.md)
- [Cosmic Bridge Myths Comparative](analyses/cosmic-bridge-myths-comparative.md)
- [Cosmic Boundary Myths Comparative](analyses/cosmic-boundary-myths-comparative.md)
- [Cosmic Balance Scales Myths Comparative](analyses/cosmic-balance-scales-myths-comparative.md)
- [Composite Monsters Hybrid Beings](analyses/composite-monsters-hybrid-beings.md)
- [Comets Meteors Mythology](analyses/comets-meteors-mythology.md)
- [Color Symbolism Trichrome](analyses/color-symbolism-trichrome.md)
- [Coins Funerary Myths Comparative](analyses/coins-funerary-myths-comparative.md)
- [Coconut Myths Comparative](analyses/coconut-myths-comparative.md)
- [Cloud Mist Myths Comparative](analyses/cloud-mist-myths-comparative.md)
- [Classical Elements Comparative](analyses/classical-elements-comparative.md)
- [City Foundation Myths Comparative](analyses/city-foundation-myths-comparative.md)
- [Cinderella Persecuted Heroine Comparative](analyses/cinderella-persecuted-heroine-comparative.md)
- [Chaoskampf Order Vs Chaos](analyses/chaoskampf-order-vs-chaos.md)
- [Celestial War Comparative](analyses/celestial-war-comparative.md)
- [Cave Myths Comparative](analyses/cave-myths-comparative.md)
- [Cannibalism Myths Comparative](analyses/cannibalism-myths-comparative.md)
- [Cacao Myths Comparative](analyses/cacao-myths-comparative.md)
- [Butterfly Soul Symbolism Comparative](analyses/butterfly-soul-symbolism-comparative.md)
- [Bull Cattle Myths Comparative](analyses/bull-cattle-myths-comparative.md)
- [Bound Gods Divine Imprisonment Comparative](analyses/bound-gods-divine-imprisonment-comparative.md)
- [Bones Mythology Comparative](analyses/bones-mythology-comparative.md)
- [Bog Swamp Marsh Mythology Comparative](analyses/bog-swamp-marsh-mythology-comparative.md)
- [Blood Covenant Myths Comparative](analyses/blood-covenant-myths-comparative.md)
- [Blindness Inner Vision Comparative](analyses/blindness-inner-vision-comparative.md)
- [Bee Honey Sacred Myths](analyses/bee-honey-sacred-myths.md)
- [Bear Myths Comparative](analyses/bear-myths-comparative.md)
- [Bat Myths Comparative](analyses/bat-myths-comparative.md)
- [Bamboo Myths Comparative](analyses/bamboo-myths-comparative.md)
- [Aurora Borealis Northern Lights Myths Comparative](analyses/aurora-borealis-northern-lights-myths-comparative.md)
- [Astral Myths Stars Constellations](analyses/astral-myths-stars-constellations.md)
- [Artificial Life Crafted Beings Comparative](analyses/artificial-life-crafted-beings-comparative.md)
- [Apple Myths Comparative](analyses/apple-myths-comparative.md)
- [Apotheosis Comparative](analyses/apotheosis-comparative.md)
- [Animal Symbolism](analyses/animal-symbolism.md)
- [Animal Marriage Theriogamy Comparative](analyses/animal-marriage-theriogamy-comparative.md)
- [Ancestor Worship Comparative](analyses/ancestor-worship-comparative.md)
- [Amulet Talisman Protective Objects Cross Cultural](analyses/amulet-talisman-protective-objects-cross-cultural.md)
- [Amber Mythology Comparative](analyses/amber-mythology-comparative.md)
- [Alchemy Transmutation Comparative](analyses/alchemy-transmutation-comparative.md)
- [Agriculture Origin Myths](analyses/agriculture-origin-myths.md)
- [Abduction Myths Comparative](analyses/abduction-myths-comparative.md)
- [Abandoned Hero Exposed Child](analyses/abandoned-hero-exposed-child.md)

<!-- ANALYSES_END -->

---

> *「神話是集體的夢，夢是私人的神話。」—— 約瑟夫·坎貝爾*
>
> *「我們不是繼承了祖先的智慧，而是借用了後代的文化。」—— 原住民諺語*
