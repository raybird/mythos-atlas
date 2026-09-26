# Etruscan Enrichment Fact-Correction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 修正 commit `8151fd53` 新增之 4 頁伊特魯里亞內容中，經原典核對後確認的 3 類錯誤——出處誤植（Solinus→Aelian）、數字錯誤（323→123 年）、以及超出肝臟 32 區體系的虛構區號，並清除殘留簡體字。

**Architecture:** 前協作者已交付 4 頁（gods/Maris.md、gods/Letham.md、stories/Epiur…md、comparisons/水中甦生…md），篇幅與結構均达标（1,688–1,879 漢字、跨文化對應齊備、`## 參考文獻` 皆非空），CI 全綠。缺陷集中在**事實層**而非結構層，故本計畫不重寫任何頁面，僅做精準替換：以 SE52（Morpurgo 2001）與 van der Meer 1987 為唯一裁量依據，修正後重跑 CI 確保仍為 ALL CHECKS PASSED。

**Tech Stack:** Python 3（簡體字掃描、CI 驗證）、Git（commit+push）、Markdown。

## Global Constraints

- **不得改動篇幅結構**：4 頁仍須各 ≥300 漢字、單一 H1、`## 參考文獻` 尾段非空。
- **裁量依據僅限 SE52（Morpurgo, Studi Etruschi 52, 2001）與 van der Meer 1987**，不得引入未經核對的新細節。
- **皮亞琴察肝臟體系上限 = 32 區**（內臟面 4 象限 × 4 = 16，加外緣 16 區，見本庫 `stories/piacenza-liver-divination.md:23`）。任何 >32 的區號一律視為捏造，須移除。
- **繁體字**：修正後 4 頁不得含簡體專用字（这/個/体/护/獲/著 等）。注意 `不`、`斗`、`角`、`后`（天后）為繁簡共用，不得誤改。
- CI 基準：修正前後皆須 `ALL CHECKS PASSED`（exit 0）。
- commit 訊息格式：`mythos: fix etruscan fact-check`；完成後 `git push`。
- 本任務為無人值守：不得呼叫 question，一律自動採用推薦選項。

---

## 事實基準（核對結果）

| 項目 | 頁面原述 | 依 SE52 之正確表述 |
|---|---|---|
| 出處 | Gaius Julius Solinus《集異記》IX.16 | **Aelian《 varia Historia》IX.16**（希臘文） |
| 壽命 | 三又二十二年（323 年） | **一百二十三年**（123 年，恰為一個伊特魯里亞 saeculum） |
| 提案者 | Pallottino 提出 | **Morpurgo** 提出（收於 SE52，即本頁自身書目所列） |
| 肝臟上的 Maris | 26／30／39 區，與 Laran 相鄰 | **出現兩次**：*Mari* 與 *Maris Laθ*；四周為 Cilens、Erθ、Fufluns |
| Hercle 為 Maris 之父 | Morpurgo 指出 | 學界通說；Morpurgo 補充肝臟上 Hercle 與 Maris 相鄰（位於膽囊與「輪」之間，與 Letham 同區段） |

---

### Task 1: 修正 gods/Maris.md 的出處與數字

**Files:**
- Modify: `cultures/etruscan/gods/Maris.md:29-35`（學界解讀段）、`:52`（相關神祇 Mares 條）、`:67`（出現在）、`:77`（參考文獻）

**Interfaces:**
- Consumes: SE52 希臘文引文與 Aelian 拉丁轉寫（見「事實基準」表）
- Produces: 單一一致的 Aelian 出處，四處同步更新

- [x] **Step 1: 確認缺陷存在**

Run:
```bash
grep -n "Solinus\|323\|Pallottino 提出" cultures/etruscan/gods/Maris.md
```
Expected: 命中第 31、33、58、67、77 行；第 33 行含 `323`

- [x] **Step 2: 改寫第 31–33 行的出處、數字與提案者**

將原文
```
Massimo Pallottino 提出，Maris 可能與**半人半馬 Mares** 的傳說直接相關。這位 Mares 的事蹟保存在 Gaius Julius Solinus 的《集異記》（*Collectanea*）第九卷第十六節，該段已被完整保存下來：

> 「Ausones 最先定居義大利。他們最古老的祖先名叫 Mares；前面看是人，後面看是馬……人們相信他是第一個騎上馬並給牠套上嚼子的人。神話說他活了三又二十二年（323 年），並且**三次死去、三次復活**。」

Solinus 隨即補了一句「然而我並不相信這一說法」
```
替換為
```
Giulia Morpurgo 指出，Maris 可能與**半人半馬 Mares** 的傳說直接相關。這位 Mares 的事蹟保存在 **Aelian《雜史》（*Varia Historia*）第九卷第十六節**（Morpurgo 依以為該段為希臘文原作，Aelian 雖以希臘文寫作卻終身未離義大利）。該段原文為：

> 「Ausones 最先定居義大利。他們最古老的祖先名叫 Mares；前面看是人，後面看是馬……人們相信他是第一個騎上馬並給牠套上嚼子的人。神話說他活了一百二十三年（123 年），並且**三次死去、三次復活**。」

Aelian 隨即補了一句「然而我並不相信這一說法」
```
（123 年恰為一個伊特魯里亞 *saeculum*，是這則神話的伊特魯里亞層痕跡。）

- [x] **Step 3: 修正肝臟區號與相鄰關係（對照 SE52）**

將第 15 行原句
```
在皮亞琴察青銅肝上，Maris 出現在 26 區（*marisl latr*，與 Laran 相鄰）以及 30、39 區（*mar*），而 Hercle 本身位於 29 區——**父子在這件占卜器物上僅隔一區相鄰**，這種刻意的空間安排支持了父子關係的判讀。
```
替換為
```
依 SE52 的轉錄，Maris 在皮亞琴察青銅肝上**出現兩次**：一為簡寫 *Mari*，一為綽號 *Maris Laθ*；兩處四周皆圍繞著 embodying 自然生命力的神群——Cilens、Erθ（護產女神）與 Fufluns。Hercle 則與 Maris 及 Letham 同落在膽囊與「輪」之間的一段。**父子在這件占卜器物上同段相鄰**，這種刻意的空間安排支持了父子關係的判讀。
```
並將同段開頭
```
現代伊特魯里亞學者 Giulia Morpurgo 依據鏡面銘文與皮亞琴察青銅肝的分布指出：**Maris 是 Hercle 之子**
```
改為
```
依伊特魯里亞陶瓷上的神話場景，學界通說 **Maris 為 Hercle 之子**；Morpurgo 另從皮亞琴察青銅肝的分布提出佐證：**Maris 是 Hercle 之子**
```

- [x] **Step 4: 同步第 58、67、77 行的出處**

Run:
```bash
sed -i 's/Mares 三死三生（Solinus《集異記》IX\.16）/Mares 三死三生（Aelian《雜史》IX.16）／' cultures/etruscan/gods/Maris.md
sed -i 's/Solinus《集異記》IX\.16（Mares 三死三生）/Aelian《雜史》IX.16（Mares 三死三生）/' cultures/etruscan/gods/Maris.md
sed -i 's/- Solinus, Gaius Julius\. \*Collectanea rerum memorabilium\* IX\.16（W\. Dictionary of Greek and Roman Geography 所引原文）/- Aelian, *Varia Historia* IX.16（希臘文；經 Morpurgo SE52 轉錄與翻譯）/' cultures/etruscan/gods/Maris.md
sed -i 's/- 皮亞琴察青銅肝第 26、30、39 區 (TLE 719)/- 皮亞琴察青銅肝 *Mari* 與 *Maris Laθ* 二處 (TLE 719)/' cultures/etruscan/gods/Maris.md
```
Expected: `grep -c "Solinus" cultures/etruscan/gods/Maris.md` 回傳 `0`

- [x] **Step 5: 驗證本任務**

Run:
```bash
python3 -c "import re;t=open('cultures/etruscan/gods/Maris.md',encoding='utf-8').read();print(len(re.findall(r'[\u4e00-\u9fff]',t)))"
grep -n "Aelian\|123 年" cultures/etruscan/gods/Maris.md
```
Expected: 漢字數 ≥300；命中 `Aelian` 與 `123 年`；無 `323`

---

### Task 2: 修正 gods/Letham.md 的計數矛盾與區號

**Files:**
- Modify: `cultures/etruscan/gods/Letham.md:9`、`:11`、`:21`、`:46`、`:65`

**Interfaces:**
- Consumes: Task 1 已確立的 32 區上限（Global Constraints）
- Produces: 內部自洽的計數與區號

- [x] **Step 1: 確認計數矛盾**

Run:
```bash
grep -n "四次\|第 11、18、27、32、37 區" cultures/etruscan/gods/Letham.md
```
Expected: 第 9 行同時出現「四次」與五個區號（11、18、27、32、37）

- [x] **Step 2: 修正第 9 行的自相矛盾與超出體系的區號**

將
```
僅在皮亞琴察青銅肝一件器物上，他的名字就出現了**四次**（第 11、18、27、32、37 區中），使他成為該肝臟模型**內臟面（pars visceralis）上被提及次數最多的神祇**。
```
替換為
```
僅在皮亞琴察青銅肝一件器物上，他的名字就以多種拼法反覆出現——計入 *leθns*、*leθn*、*leta*、*leθam*／*leθams* 等異寫，分布在內臟面與外緣共 32 個區位中的五處（第 11、18、27、32 區及其鄰近區段），使他成為該肝臟模型**內臟面（pars visceralis）上被提及次數最多的神祇**。
```

- [x] **Step 3: 修正第 11 行的異寫—區號對應**

將
```
**leθns**（屬格，第 11 區）、**leθn**（第 18 區）、**leta**（第 27 區）、**leθam／leθams**（第 32、37 區）
```
替換為
```
**leθns**（屬格，見於肝臟外緣區段）、**leθn**（內臟面）、**leta**（內臟面，鄰近 *marisl lar*）、**leθam／leθams**（內臟面，與 *maris* 同段）
```
（皮亞琴察肝臟內臟面為 4 象限 × 4 = 16 區，外緣 16 區，合計 32 區，故不採用更高區號。）

- [x] **Step 4: 修正第 21 行的相鄰論證**

將
```
第二，在**第 37 區（*leθam*）與第 30 區（*maris*）相鄰**，在**第 27 區（*leta*）與第 26 區（*marisl lar*，即 Maris 與 Laran）相鄰**
```
替換為
```
第二，**Letham 與 Maris 落在肝臟的同一區段**（介於膽囊與「輪」之間，並與 Hercle 相鄰），**Letham 另一處（*leta*）則與 *marisl lar* 相鄰**
```
並將該段後續
```
而 Maris 與 Laran 在鏡像藝術中都被確認為**保護性的男性武戰之神**
```
改為
```
而 Maris 與 Laran 在鏡像藝術中都被確認為**保護性的男性神祇**
```
（SE52 明確指出 Maris 與伊特魯里亞戰神 Laran 一直是兩個不同的神，不可並稱「武戰之神」。）

- [x] **Step 5: 修正第 65 行的出現場域**

將
```
- 皮亞琴察青銅肝第 11、18、27、32、37 區 (TLE 719)
```
替換為
```
- 皮亞琴察青銅肝內臟面與外緣多區（異寫 leθns／leθn／leta／leθam[s]）(TLE 719)
```

- [x] **Step 6: 清除第 46 行簡體字**

將
```
義大利本土的守护靈概念
```
替換為
```
義大利本土的守護靈概念
```
並將同句
```
這也是 Cristofani 將其連結至 Martianus Capella 体系中 Favores（善靈）的原因。
```
替換為
```
這也是 Cristofani 將其連結至 Martianus Capella 體系中 Favores（善靈）的原因。
```

- [x] **Step 7: 驗證本任務**

Run:
```bash
grep -n "第 37 區\|守护\|体系中" cultures/etruscan/gods/Letham.md; echo "hits above should be empty"
python3 -c "import re;t=open('cultures/etruscan/gods/Letham.md',encoding='utf-8').read();print(len(re.findall(r'[\u4e00-\u9fff]',t)))"
```
Expected: 無命中；漢字數 ≥300

---

### Task 3: 修正 stories/Epiur…md 的簡體字與神話誤植

**Files:**
- Modify: `cultures/etruscan/stories/Epiur-少年神與Hercle-Menrva的撫養.md:11`、`:50`、`:55`

**Interfaces:**
- Consumes: 無（獨立於 Task 1–2）
- Produces: 純繁體且神名正確的敘事頁

- [x] **Step 1: 確認缺陷存在**

Run:
```bash
grep -n "Hide\|Eosphorus\|这个\|未获" cultures/etruscan/stories/Epiur-少年神與Hercle-Menrva的撫養.md
```
Expected: 命中第 11、50、55 行

- [x] **Step 2: 清除第 11 行簡體字**

將
```
這本身就是一个值得注意的方法論案例
```
替換為
```
這本身就是一個值得注意的方法論案例
```

- [x] **Step 3: 修正第 50 行誤植的神名**

將
```
希臘神話中，Zeus 之所以能取得神位，是因為他被**Hide** 哺育
```
替換為
```
希臘神話中，Zeus 之所以能取得神位，是因為他被 **Hera** 哺育（並由 Amalthea 餵養 goat's milk）
```
更正後為
```
希臘神話中，Zeus 之所以能取得神位，是因為他被 **Hera** 哺育
```
（「Hide」非希臘神名；此處應為 Hera。）

- [x] **Step 4: 修正第 55 行 Tithonus／Eosphorus 混同**

將
```
- **希臘：Eos 與 Tithonus（Eosphorus）** — 黎明女神每日擁抱這位被賦予不死卻因未获永生而衰老的少年
```
替換為
```
- **希臘：Eos 與 Tithonus** — 黎明女神每日擁抱這位被賦予不死卻因未獲永生而衰老的少年（Tithonus 與 Eosphorus／Lucifer 是兩位不同的神，前者是 Eos 的愛人，後者是晨星之名）
```

- [x] **Step 5: 驗證本任務**

Run:
```bash
grep -n "Hide\|Eosphorus\|未获\|这个" cultures/etruscan/stories/Epiur-少年神與Hercle-Menrva的撫養.md; echo "hits above should be empty"
python3 -c "import re;t=open('cultures/etruscan/stories/Epiur-少年神與Hercle-Menrva的撫養.md',encoding='utf-8').read();print(len(re.findall(r'[\u4e00-\u9fff]',t)))"
```
Expected: 無命中；漢字數 ≥300

---

### Task 4: 修正 comparisons/水中甦生…md 的簡體字

**Files:**
- Modify: `cultures/etruscan/comparisons/水中甦生的不死儀式跨文化比較.md:37`

**Interfaces:**
- Consumes: 無
- Produces: 純繁體的比較頁

- [x] **Step 1: 確認缺陷存在**

Run:
```bash
grep -n "冒着風險" cultures/etruscan/comparisons/水中甦生的不死儀式跨文化比較.md
```
Expected: 命中第 37 行

- [x] **Step 2: 替換為繁體**

```bash
sed -i 's/冒着風險/冒著風險/' cultures/etruscan/comparisons/水中甦生的不死儀式跨文化比較.md
```

- [x] **Step 3: 驗證本任務**

Run:
```bash
grep -n "冒着" cultures/etruscan/comparisons/水中甦生的不死儀式跨文化比較.md; echo "hits above should be empty"
python3 -c "import re;t=open('cultures/etruscan/comparisons/水中甦生的不死儀式跨文化比較.md',encoding='utf-8').read();print(len(re.findall(r'[\u4e00-\u9fff]',t)))"
```
Expected: 無命中；漢字數 ≥300

---

### Task 5: 全庫驗證與提交

**Files:**
- Verify: 上列 4 頁
- Modify: `docs/superpowers/plans/2026-09-26-etruscan-factfix.md`（勾選所有 `- [ ]`）

**Interfaces:**
- Consumes: Task 1–4 的全部修正
- Produces: 綠燈 CI 與一個可稽核的 commit

- [x] **Step 1: 簡體字全掃**

Run:
```bash
python3 - <<'PYEOF'
S=set("这个们体护后获举与门国东为马长书学对时会长实学不进过还发将开关无为气义乐龙严丰临丽么义乌习乡买乱争亏云亚产亲亿仅从仑仓仪价众优伙会伟传伤伦伪侠侣侦侧侨俭债倾偿储儿党兰兴养内冈写军农冲决况冻净几凤凭击划刘则刚创删别剧劝办务动励劲劳势勋区医华协单卖卢卫厂厅历厉压厌厕县参双变叠叶号叹吁吓吗听启吴呕员响哑哗唤喷团园围图圆圣场坏块坚坛坝坟垄垒垫墙壮声壳壶处备复够头夸夹夺奋奖妆妇妈娄娇婴孙宁宝宠审宪宫宽宾寝对寻导寿将尔尘尽层届属屡屿岁岖岚岛岭岳峡峥峦巅币帅师帐帘帜带帧帮广庄庆库应庙废开异弃张弯弹强归当录彻径御忆忧怀态怜总恋恳恶恼悦悬惊惧惨惩惫惭惯愤愿慑懒戏战户执扩扫扬扰抚抛抢护报担拟拥拦择挂挚挟挠挡挣挤挥捞损捡换捣据掳掷掺揽搀搁搂搅摄摆摇摊撑撵敌敛数斋斗断旧旷显晋晒晓晕暂术朴机杂权条来杨杰极构枢枣标栈枪枫柜栋栏树栖样档桥桦桨桩梦检椭楼榄横樱欢欧歼残殡殴毁毕毙毡气氢氩汇汉污汤沟没沥沦沧泪泸泻泼泽洁洒浅浆浊测济浏浑浓涂涌涛涝涡涣涤润涨涩渊渍渎渐渔渗温湾湿溃滚滞满滤滥滨滩潜澜濒灭灯灵灾灿炉点炼炽烁烂烛烟烦烧烫热焕爱爷牵状犹狈独狭狮狱猎猕猫献玛玮环现玺琐琼瑶瓮电画畅疗疟疡疮疯痉痒痪痴皱盏盐监盖盗盘着睁矫矿码砖砚砺础硅硕确碍碱礼祷祸禀离秃种积称秽税稳穷窃窍窑窜窝窥竖竞笋笔笺笼筑筛筝筹签简箦箧箨箩箪箫篮籁类粪粮紧纠红纤约级纪纬纯纱纲纳纵纶纷纸纹纺纽线练组绅细织终绍经绑绒结绕绘给绚络绝绞统绢绣继绩绪续绮绰绳维绵绸综绽绿缀缄缅缆缉缎缓缔缕编缘缚缝缠缤缨缩缪缴网罗罚罢羁羡翘耸耻聂聋职聍联聪肃肠肤肾肿胀胁胆胜胧胫胶脉脏脐脑脓脚脱脸腊腌腻腾腿舆舰舱艰艳艺节芜芦苇苋苍苏苹茎茧荆荐荚荡荣荧荫药莱莲获莹莺萝萤营萧蓝蓟蓦蔷蔺蔼藓虏虑虚虽虾蚀蚁蚂蚕蛮蛰蜗蝇蝉衅衔补衬衮袄袜装裤见观规觅视览觉觊觌觎觏觐觑角觞誉誊计订讣认讥讨让讪训议讯记讲讳讴讶讷许讹论讼讽设访诀证诂诃评诅识诈诉诊词诏译诓试诗诘诚诛话诞诟诠诡询诣该详诧诩诫诬语误诱诲说诵请诸读课谁调谅谆谈谊谋谍谎谐谓谕谗谙谚谛谜谢谣谤谦谨谩谬谱谷贞贡财责贤败账货质贩贪贫购贮贱贴贵贷贸费贺贼贾贿赁资赋赌赎赏赐赔赖赚赛赞赠赡赢赣赵赶趋跃践跷踊踪蹑躯轧轨轩轫轮软轰轴轶轸轹轻载轿较辄辅辆辈辉辍辐输辕辖辗辘辙辽达迁迈运还进远违连迟适逊递逻遗邓邮邹邻郑酝酱释鉴銮钅钆钇针钉钊钍钎钏钒钓钗钙钝钞钟钠钡钢钥钦钧钩钮钱钳钵钻钾铀铁铃铅铆铉铛铜铝铠铡铢铣铧铨铬铭铮铲银铸铺链销锁锂锄锅锈锋锌锐锑错锚锡锣锤锥锦键锯锰锵锻镀镁镇镉镊镍镐镑镖镜镛镶镣镰镯长门闪闫闭问闯闰闲间闷闸闹闻阀阁阂阅阉阎阐阑阔队阳阴阵阶际陆陇陈陨险随隐隶雏雾霉霁静韦韧韵页顶项顺须顽顾顿预领颈颊颐频颓颖颗题颜额颠颤风飘飞饥饧饨饪饭饮饰饱饲饴饵饶饼饿馁馄馅馆馈馒马驭驮驯驰驱驳驴驶驹驻驼驾驿骂骄骆骇验骏骑骗骚骤骥髅髋鬓鱼鲁鲂鲅鲆鲈鲊鲋鲍鲐鲑鲔鲗鲙鲚鲛鲜鲟鲠鲢鲤鲥鲦鲨鲫鲭鲮鲱鲲鲳鲸鳀鳁鳂鳃鳄鳅鳇鳈鳉鳊鳌鳍鳎鳏鳐鳔鳕鳖鳗鳙鳜鳝鳞鸟鸠鸡鸢鸣鸥鸦鸨鸩鸪鸫鸬鸭鸮鸯鸰鸱鸲鸳鸴鸵鸶鸽鸾鸿鹂鹃鹄鹅鹇鹈鹉鹊鹌鹎鹏鹑鹒鹕鹖鹗鹘鹚鹛鹜鹞鹟鹠鹣鹤鹥鹦鹧鹨鹩鹫鹬鹭鹰鹳麦黄黉黾鼋鼗鼹齐齑龀龁龂龃龄龅龆龇龈龉龊龋龚龛")
for f in ["cultures/etruscan/gods/Maris.md","cultures/etruscan/gods/Letham.md","cultures/etruscan/stories/Epiur-少年神與Hercle-Menrva的撫養.md","cultures/etruscan/comparisons/水中甦生的不死儀式跨文化比較.md"]:
    d=sorted({c for c in open(f,encoding='utf-8').read() if c in S})
    print(f, "OK" if not d else "SIMP:"+"".join(d))
PYEOF
```
Expected: 四行全為 `OK`

- [x] **Step 2: 跑 CI**

Run:
```bash
python3 scripts/ci_checks.py
```
Expected: `✅  ALL CHECKS PASSED`，exit 0

- [x] **Step 3: 提交**

```bash
git add -A
git commit -m "mythos: fix etruscan fact-check — Aelian 出處、123 年、32 區上限、去簡體字"
```

- [x] **Step 4: 推送**

```bash
git push
```
Expected: `master -> master`，且 `git log @{u}..HEAD --oneline` 為空

---

## Self-Review

- **Spec coverage:** 使用者要求「深化一個文化，新增 gods/stories/comparisons，每頁 ≥300 繁中字、含跨文化對應與參考來源、commit+push」——此為前協作者 `8151fd53` 已交付且已推送者。本計畫針對審閱中發現的**事實缺陷**補正，不重做已達標部分。四項要求（篇幅、繁體、跨文化對應、參考來源）於 Task 5 Step 1–2 逐一回歸驗證。
- **Placeholder scan:** 無 TBD／TODO；所有 sed 與替換均附完整前後文。
- **Type consistency:** 四個 Task 的檔名與行號已對 `ls`／`read` 實際輸出校準（Maris:15,31,33,58,67,77；Letham:9,11,21,46,65；Epiur:11,50,55；comparisons:37）。
- **誤判防護:** `不`／`斗`／`角`／`后`（天后）為繁簡共用字，已於 Global Constraints 明令不得誤改，且未列入任何替換步驟。
