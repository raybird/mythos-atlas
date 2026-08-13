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

> 自動更新於 2026-08-13 02:16 UTC

| 類別 | 進度 |
|------|------|
| 文化體系 | 44/44 |
| 跨文化主題 | 27/27 |
| 分析文章 | 448 |
| 已充實文化 | 44/44 |
| 總頁面數 | 3040 |
| 總執行次數 | 124 |

<!-- STATS_END -->

<!-- CULTURES_START -->

## 🌍 已收錄文化

| 文化 | 區域 | 神祇 | 故事 | 比較 |
|------|------|------|------|------|
| [中國上古神話](cultures/chinese/) | 東亞 | 19 | 21 | 17 |
| [美索不達米亞神話](cultures/mesopotamian/) | 兩河流域 | 23 | 18 | 16 |
| [希臘神話](cultures/greek/) | 地中海—巴爾幹 | 23 | 19 | 16 |
| [埃及神話](cultures/egyptian/) | 北非—尼羅河流域 | 23 | 18 | 17 |
| [北歐神話](cultures/norse/) | 北歐—日耳曼 | 23 | 19 | 16 |
| [印度神話](cultures/hindu/) | 南亞—印度河流域 | 21 | 18 | 19 |
| [馬雅神話](cultures/mayan/) | 中美洲 | 64 | 58 | 56 |
| [日本神話](cultures/japanese/) | 東亞—日本列島 | 22 | 19 | 17 |
| [波利尼西亞神話](cultures/polynesian/) | 太平洋島嶼 | 22 | 18 | 17 |
| [澳洲原住民神話](cultures/aboriginal/) | 大洋洲—澳洲 | 21 | 19 | 17 |
| [非洲諸神話](cultures/african/) | 撒哈拉以南非洲 | 21 | 18 | 16 |
| [美洲原住民神話](cultures/indigenous-americas/) | 北美洲 | 21 | 19 | 16 |
| [印加神話](cultures/incan/) | 南美洲—安地斯山脈 | 20 | 18 | 18 |
| [凱爾特神話](cultures/celtic/) | 西歐—愛爾蘭/不列顛/高盧 | 22 | 18 | 16 |
| [斯拉夫神話](cultures/slavic/) | 東歐—巴爾幹 | 22 | 17 | 16 |
| [波斯神話](cultures/persian/) | 伊朗高原 | 57 | 54 | 60 |
| [韓國神話](cultures/korean/) | 東亞—朝鮮半島 | 20 | 18 | 17 |
| [芬蘭-烏戈爾神話](cultures/finno-ugric/) | 北歐—烏拉爾地區 | 22 | 19 | 19 |
| [西藏神話](cultures/tibetan/) | 青藏高原 | 20 | 18 | 18 |
| [蘇美神話](cultures/sumerian/) | 美索不達米亞南部 | 69 | 64 | 65 |
| [腓尼基神話](cultures/phoenician/) | 黎凡特—迦南 | 22 | 18 | 18 |
| [赫梯神話](cultures/hittite/) | 安納托利亞 | 22 | 18 | 17 |
| [約魯巴神話](cultures/yoruba/) | 西非—奈及利亞/貝南 | 57 | 56 | 59 |
| [蒙古神話](cultures/mongolian/) | 中亞—蒙古高原 | 21 | 18 | 17 |
| [愛努神話](cultures/ainu/) | 北海道—庫頁島—千島群島 | 21 | 17 | 17 |
| [伊特魯里亞神話](cultures/etruscan/) | 義大利—托斯卡尼 | 21 | 18 | 17 |
| [巴斯克神話](cultures/basque/) | 西歐—庇里牛斯山脈 | 21 | 19 | 19 |
| [波羅的神話](cultures/baltic/) | 東歐—波羅的海沿岸 | 21 | 19 | 18 |
| [越南神話](cultures/vietnamese/) | 東南亞—紅河流域 | 20 | 20 | 20 |
| [因紐特神話](cultures/inuit/) | 北極—阿拉斯加/加拿大/格陵蘭 | 21 | 18 | 17 |
| [亞美尼亞神話](cultures/armenian/) | 南高加索—亞美尼亞高原 | 20 | 18 | 19 |
| [菲律賓神話](cultures/philippine/) | 東南亞—菲律賓群島 | 20 | 18 | 17 |
| [高加索神話](cultures/caucasian/) | 高加索山脈(奧塞提亞/切爾克斯/阿布哈茲) | 21 | 17 | 17 |
| [達基亞/羅馬尼亞神話](cultures/dacian/) | 東南歐—喀爾巴阡山脈 | 20 | 21 | 16 |
| [羅馬神話](cultures/roman/) | 地中海—義大利半島 | 23 | 16 | 16 |
| [前伊斯蘭阿拉伯神話](cultures/pre-islamic-arabian/) | 阿拉伯半島 | 21 | 17 | 18 |
| [毛利神話](cultures/maori/) | 紐西蘭—玻里尼西亞三角 | 22 | 17 | 17 |
| [斯基泰神話](cultures/scythian/) | 歐亞草原—黑海北岸至阿爾泰 | 23 | 16 | 18 |
| [米諾斯神話](cultures/minoan/) | 愛琴海—克里特島 | 21 | 18 | 18 |
| [努比亞/庫什神話](cultures/nubian/) | 東北非—尼羅河上游/蘇丹 | 20 | 18 | 19 |
| [馬普切神話](cultures/mapuche/) | 南美洲—智利/阿根廷 | 21 | 21 | 16 |
| [薩米神話](cultures/sami/) | 北歐—芬諾斯堪的亞 | 20 | 19 | 17 |
| [西伯利亞神話](cultures/siberian/) | 西伯利亞—通古斯/雅庫特/楚科奇 | 20 | 20 | 15 |
| [圖皮-瓜拉尼神話](cultures/tupi-guarani/) | 南美洲—巴西/巴拉圭/玻利維亞 | 21 | 20 | 19 |

<!-- CULTURES_END -->

<!-- ANALYSES_START -->

## 📝 分析文章

> 跨文化比較神話學分析文章。共 448 篇。

- [穀靈與首果祭：跨文化收割神話比較分析](analyses/harvest-corn-spirit-first-fruits-comparative.md)
- [亡者的年度歸訪：跨文化亡靈節慶比較分析](analyses/festivals-of-the-dead-comparative.md)
- [神籤定命：跨文化神話與儀式中的抽籤、擲骰與神意之兆](analyses/sortilege-sacred-lots-cleromancy-comparative.md)
- [市集與商旅之神：跨文化神話中的貿易、交換與商業秩序](analyses/merchants-markets-trade-gods-comparative.md)
- [神聖的亂倫：跨文化神話中的兄妹婚與近親婚姻母題](analyses/divine-incest-sibling-marriage-comparative.md)
- [驅蝗之神與蝗蟲天軍：蝗災在跨文化神話中的神格化與象徵比較](analyses/locust-plagues-myths-comparative.md)
- [柏樹：死亡與不朽的常青之樹——跨文化比較神話研究](analyses/cypress-tree-death-immortality-comparative.md)
- [逐蠅之神與蒼蠅之王：蒼蠅作為驅疫、神罰與榮耀的跨文化神話比較](analyses/fly-averter-and-lord-of-flies-comparative.md)
- [神聖友誼：跨文化神話與史詩中的英雄同儕母題](analyses/sacred-friendship-heroic-companion-comparative.md)
- [時間的神格化：Chronos、Zurvān、Kāla 與 Neheh-Djet 的跨文化比較研究](analyses/deified-time-chronos-zurvan-kala-comparative.md)
- [童貞女神：處女作為跨文化神聖類型的比較研究](analyses/virgin-goddess-parthenos-comparative.md)
- [恩義動物：跨文化神話中的動物報恩母題](analyses/grateful-animals-comparative.md)
- [神聖之弦：里拉琴、豎琴與古琴的跨文化神話比較](analyses/sacred-strings-harps-lyres-comparative.md)
- [神聖傘蓋：華蓋、寶傘與天蓋的跨文化神話比較](analyses/sacred-canopy-umbrella-comparative.md)
- [風平浪靜與笑聲破曉：翠鳥跨文化神話比較](analyses/kingfisher-halcyon-myths-comparative.md)
- [南天極的指針：南十字座跨文化神話比較](analyses/southern-cross-constellation-myths-comparative.md)
- [倒反即神聖：跨文化神話中的神聖小丑與儀式逆反](analyses/sacred-clowns-ritual-inversion-comparative.md)
- [虹橋與虹蛇：彩虹作為天地通道的跨文化神話比較](analyses/rainbow-myths-comparative.md)
- [聖林跨文化神聖神祇崇拜比較](analyses/聖林跨文化神聖樹林崇拜比較分析.md)
- [神聖之笛：跨文化神話中的管樂禁忌、誘惑與吹禪](analyses/sacred-flutes-wind-instruments-comparative.md)
- [Zodiac Astrology Myths Comparative](analyses/zodiac-astrology-myths-comparative.md)
- [Wounded Sovereign Fisher King Comparative](analyses/wounded-sovereign-fisher-king-comparative.md)
- [Wounded Healer Comparative](analyses/wounded-healer-comparative.md)
- [World Tree Comparative](analyses/world-tree-comparative.md)
- [World Serpent Cosmic Encircler Comparative](analyses/world-serpent-cosmic-encircler-comparative.md)
- [World Parents Separation](analyses/world-parents-separation.md)
- [World Mountain Axis Mundi Comparative](analyses/world-mountain-axis-mundi-comparative.md)
- [World Ages Cosmic Cycles Comparative](analyses/world-ages-cosmic-cycles-comparative.md)
- [Woodpecker Myths Comparative](analyses/woodpecker-myths-comparative.md)
- [Wisdom Gods Comparative](analyses/wisdom-gods-comparative.md)
- [Wind Deities Comparative](analyses/wind-deities-comparative.md)
- [Willow Mythology Comparative](analyses/willow-mythology-comparative.md)
- [Wild Man Myths Comparative](analyses/wild-man-myths-comparative.md)
- [Wild Hunt Spectral Procession](analyses/wild-hunt-spectral-procession.md)
- [White Sacred Animals Comparative](analyses/white-sacred-animals-comparative.md)
- [Whirlpool Vortex Myths](analyses/whirlpool-vortex-myths.md)
- [Wheel Mythology Comparative](analyses/wheel-mythology-comparative.md)
- [Whale Leviathan Great Fish Comparative](analyses/whale-leviathan-great-fish-comparative.md)
- [Water Of Life Myths Comparative](analyses/water-of-life-myths-comparative.md)

... 及另外 409 篇

<!-- ANALYSES_END -->

---

> *「神話是集體的夢，夢是私人的神話。」—— 約瑟夫·坎貝爾*
>
> *「我們不是繼承了祖先的智慧，而是借用了後代的文化。」—— 原住民諺語*
