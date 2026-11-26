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

> 自動更新於 2026-11-26 01:29 UTC

| 類別 | 進度 |
|------|------|
| 文化體系 | 44/44 |
| 跨文化主題 | 27/27 |
| 分析文章 | 653 |
| 已充實文化 | 44/44 |
| 總頁面數 | 3696 |
| 總執行次數 | 338 |

<!-- STATS_END -->

<!-- CULTURES_START -->

## 🌍 已收錄文化

| 文化 | 區域 | 神祇 | 故事 | 比較 |
|------|------|------|------|------|
| [中國上古神話](cultures/chinese/) | 東亞 | 26 | 26 | 24 |
| [美索不達米亞神話](cultures/mesopotamian/) | 兩河流域 | 30 | 23 | 22 |
| [希臘神話](cultures/greek/) | 地中海—巴爾幹 | 26 | 22 | 19 |
| [埃及神話](cultures/egyptian/) | 北非—尼羅河流域 | 28 | 22 | 21 |
| [北歐神話](cultures/norse/) | 北歐—日耳曼 | 28 | 23 | 23 |
| [印度神話](cultures/hindu/) | 南亞—印度河流域 | 25 | 23 | 24 |
| [馬雅神話](cultures/mayan/) | 中美洲 | 70 | 64 | 62 |
| [日本神話](cultures/japanese/) | 東亞—日本列島 | 26 | 23 | 21 |
| [波利尼西亞神話](cultures/polynesian/) | 太平洋島嶼 | 27 | 22 | 22 |
| [澳洲原住民神話](cultures/aboriginal/) | 大洋洲—澳洲 | 27 | 25 | 25 |
| [非洲諸神話](cultures/african/) | 撒哈拉以南非洲 | 27 | 23 | 23 |
| [美洲原住民神話](cultures/indigenous-americas/) | 北美洲 | 25 | 23 | 19 |
| [印加神話](cultures/incan/) | 南美洲—安地斯山脈 | 25 | 24 | 25 |
| [凱爾特神話](cultures/celtic/) | 西歐—愛爾蘭/不列顛/高盧 | 26 | 22 | 21 |
| [斯拉夫神話](cultures/slavic/) | 東歐—巴爾幹 | 26 | 20 | 20 |
| [波斯神話](cultures/persian/) | 伊朗高原 | 65 | 64 | 66 |
| [韓國神話](cultures/korean/) | 東亞—朝鮮半島 | 26 | 23 | 24 |
| [芬蘭-烏戈爾神話](cultures/finno-ugric/) | 北歐—烏拉爾地區 | 25 | 22 | 23 |
| [西藏神話](cultures/tibetan/) | 青藏高原 | 24 | 22 | 22 |
| [蘇美神話](cultures/sumerian/) | 美索不達米亞南部 | 81 | 76 | 77 |
| [腓尼基神話](cultures/phoenician/) | 黎凡特—迦南 | 25 | 22 | 22 |
| [赫梯神話](cultures/hittite/) | 安納托利亞 | 30 | 26 | 26 |
| [約魯巴神話](cultures/yoruba/) | 西非—奈及利亞/貝南 | 63 | 62 | 65 |
| [蒙古神話](cultures/mongolian/) | 中亞—蒙古高原 | 27 | 22 | 21 |
| [愛努神話](cultures/ainu/) | 北海道—庫頁島—千島群島 | 26 | 22 | 22 |
| [伊特魯里亞神話](cultures/etruscan/) | 義大利—托斯卡尼 | 26 | 22 | 22 |
| [巴斯克神話](cultures/basque/) | 西歐—庇里牛斯山脈 | 24 | 23 | 22 |
| [波羅的神話](cultures/baltic/) | 東歐—波羅的海沿岸 | 27 | 23 | 24 |
| [越南神話](cultures/vietnamese/) | 東南亞—紅河流域 | 23 | 23 | 23 |
| [因紐特神話](cultures/inuit/) | 北極—阿拉斯加/加拿大/格陵蘭 | 27 | 22 | 23 |
| [亞美尼亞神話](cultures/armenian/) | 南高加索—亞美尼亞高原 | 24 | 22 | 23 |
| [菲律賓神話](cultures/philippine/) | 東南亞—菲律賓群島 | 25 | 22 | 22 |
| [高加索神話](cultures/caucasian/) | 高加索山脈(奧塞提亞/切爾克斯/阿布哈茲) | 26 | 21 | 22 |
| [達基亞/羅馬尼亞神話](cultures/dacian/) | 東南歐—喀爾巴阡山脈 | 23 | 24 | 19 |
| [羅馬神話](cultures/roman/) | 地中海—義大利半島 | 27 | 21 | 21 |
| [前伊斯蘭阿拉伯神話](cultures/pre-islamic-arabian/) | 阿拉伯半島 | 25 | 22 | 22 |
| [毛利神話](cultures/maori/) | 紐西蘭—玻里尼西亞三角 | 25 | 22 | 22 |
| [斯基泰神話](cultures/scythian/) | 歐亞草原—黑海北岸至阿爾泰 | 26 | 19 | 21 |
| [米諾斯神話](cultures/minoan/) | 愛琴海—克里特島 | 24 | 21 | 21 |
| [努比亞/庫什神話](cultures/nubian/) | 東北非—尼羅河上游/蘇丹 | 24 | 22 | 23 |
| [馬普切神話](cultures/mapuche/) | 南美洲—智利/阿根廷 | 24 | 24 | 21 |
| [薩米神話](cultures/sami/) | 北歐—芬諾斯堪的亞 | 25 | 24 | 24 |
| [西伯利亞神話](cultures/siberian/) | 西伯利亞—通古斯/雅庫特/楚科奇 | 24 | 24 | 21 |
| [圖皮-瓜拉尼神話](cultures/tupi-guarani/) | 南美洲—巴西/巴拉圭/玻利維亞 | 23 | 22 | 21 |

<!-- CULTURES_END -->

<!-- ANALYSES_START -->

## 📝 分析文章
> 跨文化比較神話學分析文章。共 653 篇。

- [盾之面：神盾、護罩與被圖寫的界線——跨文化神話學](analyses/sacred-shield-divine-cover-cosmic-surface-comparative.md)
- [圖之界：地圖、世界圖與被畫出的宇宙——跨文化神話學](analyses/map-cartography-cosmic-order-comparative.md)
- [苔之緩：苔蘚、地衣與被時間覆寫的表面——跨文化神話學](analyses/moss-lichen-quiet-time-surface-comparative.md)
- [櫛之序：梳篦、分理之齒與離合的跨文化神話學](analyses/comb-hair-order-parting-talisman-comparative.md)
- [風之形：扇、可折的空間與被製造的在場——跨文化神話學](analyses/fan-folding-presence-cooling-symbolic-space-comparative.md)
- [屋脊之界：屋頂、天蓋與被架起的宇宙——跨文化神話學](analyses/roof-ridge-house-cosmos-comparative.md)
- [風之眼：窗、被禁止的凝視與被計數的光——跨文化神話學](analyses/window-wind-eye-forbidden-gaze-comparative.md)
- [水之私海：羊水、胎膜與出生前的水界——跨文化神話學](analyses/amniotic-water-caul-private-sea-comparative.md)
- [土之翻：鼴鼠、被看見的土丘與盲目作為方法——跨文化神話學](analyses/mole-blind-digger-subterranean-omen-comparative.md)
- [殼之餘：蛋殼、被擊碎的容器與可讀的殘片——跨文化神話學](analyses/eggshell-broken-vessel-divinatory-residue-comparative.md)
- [血之溢：鼻衄、自出之血與不可自主的徵兆——跨文化神話學](analyses/nosebleed-unbidden-blood-portent-comparative.md)
- [匙之容：湯匙、可攜的碗與被餵養的他者——跨文化神話學](analyses/spoon-portable-bowl-feeding-measure-comparative.md)
- [土之腸：蚯蚓、地下之犁與被看不見的生——跨文化神話學](analyses/earthworm-intestine-invisible-plough-comparative.md)
- [掌之文：手相、可讀的身體與被書寫的命運——跨文化神話學](analyses/palmistry-hand-as-readable-text-comparative.md)
- [胞衣之藏：胎盤、埋藏的地契與出生前的第二身體——跨文化神話學](analyses/placenta-afterbirth-buried-second-body-comparative.md)
- [棘之界：荊棘、刺痛的邊界與被戴上頭的荊冠——跨文化神話學](analyses/thorn-boundary-crown-wounding-comparative.md)
- [箸之對：筷子、成雙的抓取與被改名的器物——跨文化神話學](analyses/chopsticks-paired-grasp-renamed-utensil-comparative.md)
- [眉之界：眉毛、可讀的表情與眉心之眼——跨文化神話學](analyses/eyebrow-brow-readable-face-comparative.md)
- [被盜的吉祥：卍、萬字符與符號意義的挪用——跨文化神話學](analyses/stolen-auspice-swastika-appropriation-comparative.md)
- [鼾之聲：沉睡者不自知的發聲、睡巨人與被聽見的深淵——跨文化神話學](analyses/snoring-unowned-voice-sleeping-giant-comparative.md)
- [影之針：日晷、倒退的影子與被刻在地面上的太陽——跨文化神話學](analyses/sundial-shadow-retrograde-carved-sun-comparative.md)
- [指南之針：司南、羅盤與被馴服的方向——跨文化神話學](analyses/compass-south-pointing-needle-tamed-direction-comparative.md)
- [眨之隙：眨眼、瞬目與最短事件的跨文化神話學](analyses/blink-wink-shortest-event-comparative.md)
- [枕上之魂：石枕、翻枕與夢境的往返——跨文化神話學](analyses/pillow-dream-soul-threshold-headrest-comparative.md)
- [眼瞼之兆：眼皮跳動、左右吉凶與不自主徵候的跨文化神話學](analyses/eyelid-twitching-omen-comparative.md)
- [針之眼：穿針、不可能之通過與被縫合的世界——跨文化神話學](analyses/needle-eye-threading-impossible-passage-comparative.md)
- [轉之立：陀螺、鞭之促與不穩定的秩序——跨文化神話學](analyses/spinning-top-axis-of-unstable-order-comparative.md)
- [紫之串：葡萄、被壓碎的聖果與集體的血——跨文化神話學](analyses/grape-crushed-cluster-blood-collective-comparative.md)
- [牽之翼：風箏、被牽引的飛行與可切斷的上升——跨文化神話學](analyses/kite-tethered-flight-severable-ascent-comparative.md)
- [漏之頸：沙漏、可翻轉時間與被計量的死——跨文化神話學](analyses/hourglass-neck-reversible-time-measured-death-comparative.md)
- [篩之目：孔徑、過濾與被規定的通過——跨文化神話學](analyses/sieve-aperture-filter-governed-passage-comparative.md)
- [燭之命：自燃之身、不可添的光與被計量的奉獻——跨文化神話學](analyses/candle-self-consuming-wax-mortal-light-comparative.md)
- [斷之權：剪刀、生命線與被發明的分離——跨文化神話學](analyses/scissors-power-to-sever-invented-separation-comparative.md)
- [犁之刃：翻土、邊界與武器的反轉——跨文化神話學](analyses/plow-sacred-furrow-boundary-weapon-reversal-comparative.md)
- [雹之彈：冰雹、天罰之石與「壞掉的雨」的跨文化神話學](analyses/hail-divine-artillery-ambivalent-rain-comparative.md)
- [嚏之應：噴嚏、神意與被迫的第二聲——跨文化神話學](analyses/sneeze-divine-omen-blessing-second-voice-comparative.md)
- [罐底之翼：希望、艾爾庇斯與末日之物的跨文化神話學](analyses/hope-elpis-spes-last-evil-comparative.md)
- [殼中之國：蝸牛、螺殼與攜帶宇宙的跨文化神話學](analyses/snail-shell-portable-cosmos-comparative.md)
- [網之眼：因陀羅網、天網與捕縛之網的跨文化神話學](analyses/sacred-net-indra-web-heavenly-net-comparative.md)
- [罌粟之眠：罌粟、睡眠與遺忘的跨文化神話學](analyses/poppy-sleep-oblivion-comparative.md)
- [皺之文：皺紋、老年紋與時間書寫的跨文化神話學](analyses/wrinkles-time-inscription-comparative.md)
- [哨之召：口哨、夜哨禁忌與呼喚權的跨文化神話學](analyses/whistling-summons-night-taboo-comparative.md)
- [疤之證：傷疤、刺痕與皮膚檔案的跨文化神話學](analyses/scar-recognition-skin-archive-comparative.md)
- [僵之側：麻木、癱瘓與被擊中之身的跨文化神話學](analyses/paralysis-numbness-struck-body-comparative.md)
- [痛之訊：疼痛、苦難與身體訊使的跨文化神話學](analyses/pain-suffering-body-messenger-comparative.md)
- [眩之轉：眩暈、天旋地轉與世界之軸的跨文化神話學](analyses/vertigo-dizziness-world-axis-comparative.md)
- [熱之度：發燒、體內戰爭與清涼他者的跨文化神話學](analyses/fever-heat-war-cooling-comparative.md)
- [咳之律：咳嗽、預兆缺席與禮法靜音的跨文化神話學](analyses/cough-reflex-omen-etiquette-comparative.md)
- [耳中之語：耳鳴占、無源之聲與左右吉凶的跨文化神話學](analyses/tinnitus-ear-ringing-omen-comparative.md)
- [倒落之疾：癲癇、神聖病與附身的跨文化神話學](analyses/epilepsy-sacred-disease-possession-comparative.md)
- [無職之海：腦、髓海與心智治外法權的跨文化神話學](analyses/brain-mind-sea-of-marrow-comparative.md)
- [深湖與溝渠：奇經八脈與「正冊之外」的跨文化神話學](analyses/eight-extraordinary-vessels-comparative.md)
- [無形之官：三焦、心包與「有名而無形」的跨文化神話學](analyses/triple-burner-pericardium-formless-organs-comparative.md)
- [脾之暗房：脾臟、黑膽汁與中央之土的跨文化神話學](analyses/spleen-black-bile-central-earth-comparative.md)
- [肺之風箱：肺臟、氣息與授予之生的跨文化神話學](analyses/lung-breath-gifted-life-comparative.md)

- [膽中一味：膽囊、苦汁與決斷的跨文化神話學](analyses/gallbladder-bitter-juice-decision-comparative.md)

- [腎中之秘：腎臟、精水與夜間良知的跨文化神話學](analyses/kidney-essence-water-secret-conscience-comparative.md)

- [盤繞之河：腸、內臟與斷裂之情的跨文化神話學](analyses/intestines-entrails-bowels-comparative.md)

- [腹中之器：胃、食慾與吞噬的跨文化神話學](analyses/stomach-belly-vessel-appetite-comparative.md)

- [脊中之柱，髓中之源：脊柱與骨髓的跨文化神話學](analyses/spine-marrow-axis-within-comparative.md)

- [肝之祭壇：肝臟、臟器占卜與再生懲罰的跨文化神話學](analyses/liver-hepatomancy-seat-of-life-comparative.md)

- [排氣之聲：屁、體內之風與神聖喜劇的跨文化神話學](analyses/flatulence-inner-wind-sacred-comedy-comparative.md)

- [體液與宇宙：血、膽、黏液與風的跨文化神話學](analyses/humors-bodily-fluids-cosmology-comparative.md)

- [黏土造人：跨文化創世造人神話比較分析](analyses/creation-from-clay-comparative.md)
- [禁忌語音與沉默律令：跨文化語言禁忌比較分析](analyses/taboo-speech-and-silence-mandates.md)
- [雷石跨文化神話比較分析](analyses/thunderstone-ceraunia-cross-cultural.md)
- [禁止回望：回頭禁忌與跨文化神話比較](analyses/looking-back-taboo-comparative.md)
- [末子之選：么子英雄與幼子繼承的跨文化神話比較](analyses/youngest-child-hero-comparative.md)
- [巨角之下：野牛與水牛神話的跨文化比較](analyses/buffalo-bison-myths-comparative.md)
- [神的化身：跨文化神話中的降世、應化與神體顯現比較](analyses/divine-incarnation-avatara-comparative.md)
- [蒼老女神與巫婆始祖：跨文化神話中的老嫗原型比較](analyses/crone-hag-goddess-comparative.md)
- [追尋的母親女神：哀悼、尋覓與宇宙失衡的跨文化母題比較](analyses/searching-mother-goddess-comparative.md)
- [海之呼吸：潮汐與怒潮的跨文化神話比較](analyses/tides-tidal-bore-myths-comparative.md)
- [樹靈與森林精靈：荒野之心的人格化跨文化比較分析](analyses/tree-forest-spirits-comparative.md)
- [棋局神話：宇宙為盤、命運為局——跨文化神話中的棋戲與神聖遊戲](analyses/board-games-fate-myths-comparative.md)
- [神之坐騎：印度瓦哈納傳統與跨文化神聖座騎比較](analyses/divine-mounts-vahana-comparative.md)
- [以人為祭：跨文化神話中的宇宙債務、替代邏輯與廢止敘事](analyses/human-sacrifice-comparative.md)
- [死亡的化身：死神與收割者的跨文化神話比較](analyses/personifications-of-death-comparative.md)
- [愚者之火與亡魂之光：鬼火／幽靈火球的跨文化神話比較](analyses/phantom-lights-ghost-fires-comparative.md)
- [神明裁判：以火、水與毒驗證真理的跨文化神判神話](analyses/trial-by-ordeal-divine-judgement-comparative.md)
- [椰棗與棕櫚：庇蔭、計時與勝利的聖樹——跨文化比較神話分析](analyses/date-palm-sacred-tree-comparative.md)
- [牛群奪還神話：掠奪、單挑與印歐宇宙秩序的修復——跨文化比較神話學分析](analyses/cattle-raiding-myths-comparative.md)
- [四十日與四十年：數字四十的試煉、淨化與重生週期——跨文化神話比較研究](analyses/number-forty-sacred-cycle-comparative.md)
- [神聖煙草：獻祭之霧與幻視之門——跨文化神話中的煙草](analyses/tobacco-myths-sacred-smoke-comparative.md)
- [掃帚之謎：淨化、飛昇與界線——跨文化神話中的掃帚](analyses/broom-myths-sacred-sweeping-comparative.md)
- [傳奇名劍：王權、犧牲與命運的跨文化比較神話學](analyses/legendary-named-swords-comparative.md)
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
