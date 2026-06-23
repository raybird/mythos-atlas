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
└── populate.sh               # 自動充實排程腳本（每小時:10執行）
```

## 自動化充實機制

本 repo 透過 cron 排程，每小時在 **第 10 分鐘**自動執行 `populate.sh`，逐步：

1. 新增一個文化的神話條目（依循環順序）
2. 新增或擴充一個主題分析
3. 更新索引與交叉對照表
4. 自動 commit 進度

預計完成時間：約 **3-6 個月**可達初步完整的跨文化覆蓋。

## 如何參與

- **直接閱讀** — clone 或瀏覽 cultures/ 與 themes/ 目錄
- **提供修正** — 開 Issue 或 PR 補充缺漏的文化視角
- **建議來源** — 如果你知道特定的原始文獻或學術著作，歡迎在 references/ 貢獻

<!-- STATS_START -->

## 📊 當前狀態

> 自動更新於 2026-06-23 14:10 UTC

| 類別 | 進度 |
|------|------|
| 文化體系 | 44/44 |
| 跨文化主題 | 26/26 |
| 分析文章 | 78 |
| 總執行次數 | 35 |

<!-- STATS_END -->

<!-- CULTURES_START -->

## 🌍 已收錄文化

| 文化 | 區域 | 神祇 | 故事 | 比較 |
|------|------|------|------|------|
| [中國上古神話](cultures/chinese/) | 東亞 | 5 | 8 | 4 |
| [美索不達米亞神話](cultures/mesopotamian/) | 兩河流域 | 6 | 4 | 3 |
| [希臘神話](cultures/greek/) | 地中海—巴爾幹 | 11 | 6 | 4 |
| [埃及神話](cultures/egyptian/) | 北非—尼羅河流域 | 7 | 4 | 3 |
| [北歐神話](cultures/norse/) | 北歐—日耳曼 | 7 | 4 | 2 |
| [印度神話](cultures/hindu/) | 南亞—印度河流域 | 8 | 5 | 3 |
| [馬雅神話](cultures/mayan/) | 中美洲 | 7 | 4 | 3 |
| [日本神話](cultures/japanese/) | 東亞—日本列島 | 6 | 3 | 1 |
| [波利尼西亞神話](cultures/polynesian/) | 太平洋島嶼 | 6 | 3 | 3 |
| [澳洲原住民神話](cultures/aboriginal/) | 大洋洲—澳洲 | 5 | 3 | 3 |
| [非洲諸神話](cultures/african/) | 撒哈拉以南非洲 | 7 | 4 | 2 |
| [美洲原住民神話](cultures/indigenous-americas/) | 北美洲 | 5 | 4 | 2 |
| [印加神話](cultures/incan/) | 南美洲—安地斯山脈 | 5 | 2 | 2 |
| [凱爾特神話](cultures/celtic/) | 西歐—愛爾蘭/不列顛/高盧 | 6 | 4 | 2 |
| [斯拉夫神話](cultures/slavic/) | 東歐—巴爾幹 | 8 | 3 | 2 |
| [波斯神話](cultures/persian/) | 伊朗高原 | 4 | 3 | 3 |
| [韓國神話](cultures/korean/) | 東亞—朝鮮半島 | 4 | 3 | 3 |
| [芬蘭-烏戈爾神話](cultures/finno-ugric/) | 北歐—烏拉爾地區 | 6 | 3 | 3 |
| [西藏神話](cultures/tibetan/) | 青藏高原 | 6 | 4 | 4 |
| [蘇美神話](cultures/sumerian/) | 美索不達米亞南部 | 7 | 4 | 4 |
| [腓尼基神話](cultures/phoenician/) | 黎凡特—迦南 | 5 | 2 | 2 |
| [赫梯神話](cultures/hittite/) | 安納托利亞 | 6 | 3 | 3 |
| [約魯巴神話](cultures/yoruba/) | 西非—奈及利亞/貝南 | 6 | 4 | 4 |
| [蒙古神話](cultures/mongolian/) | 中亞—蒙古高原 | 3 | 3 | 2 |
| [愛努神話](cultures/ainu/) | 北海道—庫頁島—千島群島 | 6 | 3 | 3 |
| [伊特魯里亞神話](cultures/etruscan/) | 義大利—托斯卡尼 | 5 | 3 | 2 |
| [巴斯克神話](cultures/basque/) | 西歐—庇里牛斯山脈 | 3 | 3 | 3 |
| [波羅的神話](cultures/baltic/) | 東歐—波羅的海沿岸 | 5 | 4 | 3 |
| [越南神話](cultures/vietnamese/) | 東南亞—紅河流域 | 3 | 3 | 3 |
| [因紐特神話](cultures/inuit/) | 北極—阿拉斯加/加拿大/格陵蘭 | 5 | 3 | 3 |
| [亞美尼亞神話](cultures/armenian/) | 南高加索—亞美尼亞高原 | 6 | 4 | 4 |
| [菲律賓神話](cultures/philippine/) | 東南亞—菲律賓群島 | 4 | 3 | 2 |
| [高加索神話](cultures/caucasian/) | 高加索山脈(奧塞提亞/切爾克斯/阿布哈茲) | 4 | 2 | 2 |
| [達基亞/羅馬尼亞神話](cultures/dacian/) | 東南歐—喀爾巴阡山脈 | 4 | 5 | 1 |
| [羅馬神話](cultures/roman/) | 地中海—義大利半島 | 8 | 3 | 3 |
| [前伊斯蘭阿拉伯神話](cultures/pre-islamic-arabian/) | 阿拉伯半島 | 6 | 3 | 3 |
| [毛利神話](cultures/maori/) | 紐西蘭—玻里尼西亞三角 | 5 | 3 | 3 |
| [斯基泰神話](cultures/scythian/) | 歐亞草原—黑海北岸至阿爾泰 | 9 | 4 | 4 |
| [米諾斯神話](cultures/minoan/) | 愛琴海—克里特島 | 6 | 3 | 3 |
| [努比亞/庫什神話](cultures/nubian/) | 東北非—尼羅河上游/蘇丹 | 5 | 3 | 3 |
| [馬普切神話](cultures/mapuche/) | 南美洲—智利/阿根廷 | 5 | 3 | 2 |
| [薩米神話](cultures/sami/) | 北歐—芬諾斯堪的亞 | 6 | 5 | 4 |
| [西伯利亞神話](cultures/siberian/) | 西伯利亞—通古斯/雅庫特/楚科奇 | 5 | 5 | 1 |
| [圖皮-瓜拉尼神話](cultures/tupi-guarani/) | 南美洲—巴西/巴拉圭/玻利維亞 | 4 | 3 | 2 |

<!-- CULTURES_END -->

<!-- ANALYSES_START -->

## 📝 分析文章

> 跨文化比較神話學分析文章。共 78 篇。

- [World Parents Separation](analyses/world-parents-separation.md)
- [Wisdom Gods Comparative](analyses/wisdom-gods-comparative.md)
- [Wind Deities Comparative](analyses/wind-deities-comparative.md)
- [War Gods Comparative](analyses/war-gods-comparative.md)
- [Underworld Journey](analyses/underworld-journey.md)
- [Twin Myths](analyses/twin-myths.md)
- [Trickster Across Cultures](analyses/trickster-across-cultures.md)
- [Thunder Gods](analyses/thunder-gods.md)
- [Threshold Crossroads Gods](analyses/threshold-crossroads-gods.md)
- [Sun Myths](analyses/sun-myths.md)
- [Spider Weaving Myths](analyses/spider-weaving-myths.md)
- [Smith Forge Gods Comparative](analyses/smith-forge-gods-comparative.md)
- [Sleep Dreams Mythology](analyses/sleep-dreams-mythology.md)
- [Shanhaijing Mythological Geography](analyses/shanhaijing-mythological-geography.md)
- [Shamanism In Myth](analyses/shamanism-in-myth.md)
- [Sea Deities Ocean Myths](analyses/sea-deities-ocean-myths.md)
- [Sacrificial Creation](analyses/sacrificial-creation.md)
- [Sacred Waters Springs](analyses/sacred-waters-springs.md)
- [Sacred Rivers Myths](analyses/sacred-rivers-myths.md)
- [Sacred Plants Entheogens](analyses/sacred-plants-entheogens.md)

... 及另外 58 篇

<!-- ANALYSES_END -->

---

> *「神話是集體的夢，夢是私人的神話。」—— 約瑟夫·坎貝爾*
>
> *「我們不是繼承了祖先的智慧，而是借用了後代的文化。」—— 原住民諺語*
