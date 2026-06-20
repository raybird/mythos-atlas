#!/usr/bin/env python3
"""Expand _catalog.json with new cultures and themes, then batch-generate all."""
import json, os, sys
from datetime import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
CATALOG = os.path.join(REPO, "_catalog.json")
CULTURES_DIR = os.path.join(REPO, "cultures")
THEMES_DIR = os.path.join(REPO, "themes")
INDEX_CULTURES = os.path.join(CULTURES_DIR, "00-index.md")
INDEX_THEMES = os.path.join(THEMES_DIR, "00-index.md")

# ── New cultures ────────────────────────────────────────────────────────────
NEW_CULTURES = [
    {
        "id": "yoruba", "name": "約魯巴神話", "name_en": "Yoruba Mythology",
        "region": "西非—奈及利亞/貝南", "era": "約魯巴城邦—現代",
        "sources": ["Ifá系統(占卜詩篇)","口傳傳統","奧杜(Ifá經文)","約魯巴神話集"],
        "motifs": ["至高神Olodumare／Olorun","Orishas眾神體系","Obatala造人","造物主以泥土造人","雷神Shango","蛇神Oshunmare","雙生神Ibeji","祖先Egungun崇拜"],
        "parallels": [["Obatala以泥土造人","女媧/恩基/普羅米修斯"],["Shango雷神","索爾/Perun/因陀羅"],["世界樹(棕櫚樹)","Yggdrasil/建木"],["Ajogun災禍精靈","惡魔/混亂力量"]],
        "creation": "世界最初只有天空與沼澤。至高神Olorun(或Olodumare)命Obatala下凡造地。Obatala以金鍊垂降，將沙倒入原水，白雞將沙耙開成陸地。Obatala以泥土造人，但醉酒後造出殘疾人——Olorun因此禁止他飲酒。Oduduwa接續完成陸地創造，成為約魯巴人的始祖。",
        "flood": "約魯巴神話中洪水與Olokun(海洋之神)相關。Olokun因不滿人類驕傲，以巨浪淹沒大地。Orishas祈求Olorun干預，Obatala以金鍊降下，說服Olokun退水。部分版本保留人類因違反禁忌而遭洪水懲罰的主題。",
        "pantheon": "Olodumare(至高神)、Obatala(造人/純潔)、Oduduwa(先祖)、Shango(雷/火/王權)、Oshun(愛/河/豐收)、Yemaya(海洋之母)、Ogun(鐵/戰)、Orunmila(智慧/占卜)、Oya(風/死亡)、Eshu(Elegba,信使/十字路口)、Oshossi(狩獵)",
        "stories": ["Obatala造人與醉酒","Shango登天成神","Oshun的鏡子","Yemaya的海洋王國","Eshu的惡作劇","Orunmila與Ifá占卜的起源","Ogun打開通往人間的路"],
        "order": 23
    },
    {
        "id": "mongolian", "name": "蒙古神話", "name_en": "Mongolian Mythology",
        "region": "中亞—蒙古高原", "era": "匈奴—蒙古帝國時期",
        "sources": ["《蒙古秘史》","《黃金史》","《格薩爾王》史詩","民間史詩Uliger","薩滿口傳"],
        "motifs": ["長生天Tengri","地母Eje/Gazar Eej","99尊天神","薩滿宇宙三界","祖先狼圖騰","聖山Burkhan Khaldun","Erlik冥界之王"],
        "parallels": [["Tengri天神","希臘Zeus/北歐Odin/中國天"],["大地潛水者造地","北美原住民/芬蘭"],["Erlik冥界","希臘Hades/北歐Hel"]],
        "creation": "最初只有無邊汪洋與黑暗。Bai-Ulgan(創造神)或Lama(受佛教影響版本)以鐵棒攪拌汪洋，生風與火，水中央凝結成大地。另一版本：天神Esege Malan以一把泥土捏出太陽與月亮，再創造萬物。佛教影響版本：釋迦牟尼以金箭射穿金蛙，蛙身化為五大元素與大地。",
        "flood": "蒙古洪水神話常與Tengri的憤怒相關——人類違背天道，Tengri降下洪水毀滅不義者，僅少數善良者得救。薩滿傳說中世界經歷多次毀滅(火、洪水、風)，為佛教宇宙循環觀念的前身。洪水消退後新世界在聖山Burkhan Khaldun重生。",
        "pantheon": "Tengri(永恆藍天/至高神)、Bai-Ulgan(創造/善神)、Esege Malan(天父)、Erlik Khan(冥界之王)、Daichi Tengri(戰神)、Ot(婚姻女神)、Khoormusta(西方55天之首)、Ataa Ulaan(東方44天之首)、Umay(地母/生育)",
        "stories": ["格薩爾王降魔","Jangar史詩","天狼神話","Erlik的墮落","成吉思汗的天命","白老翁神話"],
        "order": 24
    },
    {
        "id": "ainu", "name": "愛努神話", "name_en": "Ainu Mythology",
        "region": "北海道—庫頁島—千島群島", "era": "史前—近代",
        "sources": ["口傳Yukar(英雄敍事詩)","Kamuy Yukar(神謠)","John Batchelor民族誌"],
        "motifs": ["Kamuy萬物有靈","鵡鴒潛水造地","熊神崇拜Iyomante","火神Kamuy-huci","六層天與六層地","文化英雄Ae-oyna-kamuy"],
        "parallels": [["鵡鴒Earth-Diver造地","中央亞細亞/北美原住民Earth-Diver神話"],["熊神/熊祭","西伯利亞熊崇拜"],["世界始於泥濘沼澤","日本/波利尼西亞創世"]],
        "creation": "宇宙最初只有無邊沼澤，巨鱒在其中游動，創造神Kotan-kar-kamuy命鵡鴒(水搖擺鳥)降下。鵡鴒在沼澤上拍打水面、踩踏泥土，形成島嶼與陸地。世界形成後，神以泥土、繁縷與柳枝造人——但因水獺忘記神的指示，人類有了缺陷。文化英雄Ae-oyna-kamuy教導人類生火、狩獵、建築與宗教儀式。",
        "flood": "愛努神話中無獨立的大洪水傳說，但有世界毀滅後重建的主題。部分Yukar敍事詩描述大地震動、山崩海嘯淹沒村莊——可能反映北海道週邊的真實海嘯記憶。熊神祭(Iyomante)中熊被送回神界，象徵生死循環與世界秩序的維持。",
        "pantheon": "Kotan-kar-kamuy(創世神)、Kamuy-huci(火竈女神)、Kim-un-kamuy(熊/山神)、Rep-un-kamuy(海神)、Ae-oyna-kamuy(文化英雄/教導者)、Tokapcup-kamuy(太陽神)、Kunnecup-kamuy(月神)、Wakka-us-kamuy(淡水神)、Chikap-kamuy(貓頭鷹/陸地神)",
        "stories": ["鵡鴒造地","Ae-oyna-kamuy下凡教導","熊神祭的起源","Okikurumi英雄傳說","狐狸娶親","貓頭鷹與人類的約定"],
        "order": 25
    },
    {
        "id": "etruscan", "name": "伊特魯里亞神話", "name_en": "Etruscan Mythology",
        "region": "義大利—托斯卡尼", "era": "公元前8-3世紀",
        "sources": ["皮亞琴察青銅肝模型","伊特魯里亞鏡子銘文","墓室壁畫","羅馬文獻(李維/老普林尼)"],
        "motifs": ["Tinia三雷電","占卜(肝卜/鳥卜)","死者冥界之旅","Charun藍色惡魔","Vanth死亡女神","宇宙分16區","神祇三重奏"],
        "parallels": [["Tinia/Uni/Menrva三主神","宙斯/赫拉/雅典娜"],["肝卜占卜","美索不達米亞肝卜傳統"],["Charun渡冥河","希臘Charon/埃及阿努比斯"]],
        "creation": "伊特魯里亞創世神話記載甚少——世界由Tinia(天空神)以六天創造(類似聖經但更古老)。宇宙分為16個天文區域，每區由特定神祇管轄。Tinia握有三道雷電——第一道用於警告，第二道用於懲戒，第三道僅用於眾神議會同意後。世界將經歷六個千年(六個世代)後終結。",
        "flood": "伊特魯里亞神話記載世界將經歷多次毀滅循環(以雷電、洪水、地震)。Tinia以雷電懲罰人類傲慢。部分傳說描述上古洪水毀滅巨人世代——此主題可能通過伊特魯里亞影響了羅馬神話。",
        "pantheon": "Tinia(天/雷神)、Uni(天后)、Menrva(智慧/戰)、Nethuns(海)、Turms(信使)、Fufluns(酒/狂喜)、Aplu(預言)、Usil(太陽)、Turan(愛)、Laran(戰)、Selvans(邊界)、Culsans(門神)、Aita(冥王)、Phersipnei(冥后)、Charun(渡者)、Vanth(死亡神使)",
        "stories": ["Tages從犁溝中現身傳授占卜","Hercle(赫拉克勒斯)冒險","Vibenna兄弟傳奇","Achle(阿基里斯)在伊特魯里亞藝術中"],
        "order": 26
    },
    {
        "id": "basque", "name": "巴斯克神話", "name_en": "Basque Mythology",
        "region": "西歐—庇里牛斯山脈", "era": "新石器時代—基督教化前",
        "sources": ["José Miguel de Barandiarán田野採集","口傳傳統","地名學","中世紀宗教審判記錄"],
        "motifs": ["大地女神Mari","Sugaar雷蛇","洞穴居住神","Eguzkilore太陽花護符","Basajaun森林野人","Lamiak水精靈","Jentilak巨人"],
        "parallels": [["Mari/Sugaar天地父母","蓋亞/烏拉諾斯/天地父母"],["Basajaun教人農耕","恩基教人/普羅米修斯盜火"],["Herensuge龍","龍/巨蛇神話跨文化"]],
        "creation": "巴斯克神話中無統一書面創世文本。原始信仰中大地女神Mari為中心存在——她居住在山洞中，掌管天氣與自然力量。太陽Eki為Mari之女，月亮Ilargi也為其女。世界由Mari與其配偶Sugaar(雷蛇)共同維持平衡。巴斯克人的先祖Aitor傳說為19世紀建構的現代起源神話。",
        "flood": "巴斯克洪水傳說與Sugaar/龍相關——部分傳說中雨水過多時Mari與Sugaar的爭鬥引發暴風雨與洪水。基督教化後，洪水傳說與聖經挪亞方舟融合。巴斯克沿海村莊保留海平面變化的古老記憶。",
        "pantheon": "Mari(大地/自然之母)、Sugaar(雷/蛇神)、Eki(太陽女神)、Ilargi(月神)、Amalur(大地之母)、Eguzki(太陽)、Ortzi/Urtzi(天空神)、Orko(雷神)、Odei(暴風雲)、Aide(風神)、Basajaun(森林守護者)、Lamiak(水仙女)、Jentilak(巨人)、Tartalo(獨眼巨人)",
        "stories": ["Mari的洞穴","Basajaun教人農耕與製鐵","Lamiak的黃金梳子","Olentzero聖誕傳說","Akelarre女巫集會","Tartalo與牧羊人"],
        "order": 27
    },
    {
        "id": "baltic", "name": "波羅的神話", "name_en": "Baltic (Lithuanian/Latvian) Mythology",
        "region": "東歐—波羅的海沿岸", "era": "鐵器時代—基督教化前(至14-15世紀)",
        "sources": ["民間歌謠Dainas","編年史(馬爾堡/利沃尼亞)","民俗採集","比較神話學重建"],
        "motifs": ["Dievas天父","Perkūnas雷神","Saulė太陽女神","Mēness月神","Laima命運女神","Žemyna地母","世界樹(橡樹)","Ašvieniai神馬雙子"],
        "parallels": [["Perkūnas戰Velnias","索爾戰耶夢加得/因陀羅戰弗栗多"],["Saulė太陽船","希臘Helios馬車/埃及Ra太陽船"],["Dievas天父","希臘Zeus/北歐Odin"]],
        "creation": "最初只有無邊汪洋。Dievas(天父)與Velnias(冥神)為兄弟，二者共同創造世界。Dievas命Velnias潛入海底取泥——Velnias取回泥土，Dievas將其鋪在水面上形成大地。Velnias口中藏泥，吐出後形成山脈、湖泊與石頭。二人永恆鬥爭創造了世界的動態平衡。人類由Dievas行走時吐出的唾液或水滴形成。",
        "flood": "波羅的海神話中洪水與Perkūnas的雷暴相關——Perkūnas以雷斧劈開雲層，降下暴雨沖刷大地。部分傳說記載「上古洪水」淹沒了第一批人類，僅少數在聖橡樹上倖存。Saulė(太陽)在洪水後重新升起，帶來新生命。波羅的海沿岸保留末次冰期冰川融化與海平面上升的古老記憶。",
        "pantheon": "Dievas/Dievs(天父/造物主)、Perkūnas/Perkons(雷神)、Saulė(太陽女神)、Mēness(月神)、Laima(命運/生育)、Žemyna/Zemes māte(地母)、Velnias/Velns(冥神/混沌)、Māra(經濟/身體守護)、Jūras māte(海母)、Meža māte(森林母)、Ašvieniai(神馬雙子)",
        "stories": ["Saulė的婚禮","Perkūnas懲罰月神不忠","Velnias與Dievas造地","Laima決定嬰兒命運","Egle蛇王后","Jūratė與Kastytis(琥珀傳說)"],
        "order": 28
    },
    {
        "id": "vietnamese", "name": "越南神話", "name_en": "Vietnamese Mythology",
        "region": "東南亞—紅河流域", "era": "雄王時代—封建時期",
        "sources": ["《嶺南摭怪》","《大越史記全書》","《越甸幽靈》","口傳傳統"],
        "motifs": ["龍父仙母(Con Rồng Cháu Tiên)","Lạc Long Quân與Âu Cơ","百卵生百子","Sơn Tinh水山神之爭","Thần Trụ Trời撐天柱","四大不死(四不死)"],
        "parallels": [["龍父仙母(蛋生始祖)","中國盤古卵/印度金卵/芬蘭世界蛋"],["Sơn Tinh vs Thủy Tinh山神戰水神","Chaoskampf混沌之戰原型"],["Thần Trụ Trời撐天柱","北歐Yggdrasil/世界樹"]],
        "creation": "最初天地混沌未分，Thần Trụ Trời(撐天神)以頭頂天、腳踏地，將天地分開。天如傘蓋、地如方盤。神以泥土與石柱撐天，天越高越遠，形成今日的天空。另一版本：Lạc Long Quân(龍君)娶Âu Cơ(仙妻)，Âu Cơ生百卵化百子——50子隨父下海、50子隨母上山，成為越南54民族的始祖。",
        "flood": "越南洪水神話以Sơn Tinh(山神)與Thủy Tinh(水神)之戰為代表——每年雨季水神掀起洪水與山神爭奪公主，山神以山巒抵擋。此神話反映紅河三角洲的年度洪水循環。部分傳說記載上古大洪水毀滅萬物，僅少數人在高山避難倖存。",
        "pantheon": "Ông Trời/Ngọc Hoàng(玉皇/天帝)、Lạc Long Quân(龍君)、Âu Cơ(仙母)、Sơn Tinh(山神)、Thủy Tinh(水神)、Thần Trụ Trời(撐天神)、Tản Viên Sơn Thánh(傘圓山聖)、Phù Đổng Thiên Vương(扶董天王)、Chử Đồng Tử(褚童子)、Liễu Hạnh(柳杏公主)、Mười Hai Bà Mụ(十二助產婆)",
        "stories": ["Lạc Long Quân斬妖(木精/魚精/狐精)","Âu Cơ生百卵","Sơn Tinh vs Thủy Tinh","Thánh Gióng(扶董)滅敵","Trọng Thủy與Mỵ Châu","Chử Đồng Tử遇仙"],
        "order": 29
    },
    {
        "id": "inuit", "name": "因紐特神話", "name_en": "Inuit Mythology",
        "region": "北極—阿拉斯加/加拿大/格陵蘭", "era": "史前—現代",
        "sources": ["口傳傳統","薩滿(angakok)傳承","早期探險家記錄","20世紀民族誌"],
        "motifs": ["Sedna海洋女神","日月追逐(Aningan與Malina)","Inua萬物有靈","薩滿靈魂旅程","動物禁忌體系","Tupilak魔法造物"],
        "parallels": [["Sedna海母","希臘Amphitrite/巴比倫Tiamat"],["日月追逐","希臘阿波羅/阿緹蜜絲"],["大地潛水者創世","中央亞細亞/北美原住民"]],
        "creation": "英努伊特(Inuit)創世神話多元——一版本：A'akuluujjusi以衣物擲地創造動物(褲子變北極熊、襪子變馴鹿等)。另一版本：烏鴉之父(Raven/Father)以原始黑暗中的泥土與光創造世界。Sedna傳說：少女Sedna被父拋入海中，手指被砍成海豹、海象與鯨魚，成為海洋之母——從此為因紐特人提供食物。第一對人類Uumarnituq(母)與Aakulujjuusi(父)由泥土中生出。",
        "flood": "因紐特洪水分為兩類——(1)「上古洪水」淹沒巨人時代的世界，少數人乘皮艇或躲山洞倖存。(2)Sedna的憤怒引發海嘯——人類違反禁忌時Sedna以巨浪懲罰，薩滿必須潛入海底梳理她的頭髮以平息之。部分傳說反映末次冰期後海平面急劇上升的集體記憶。",
        "pantheon": "Sedna(海洋之母/海獸提供者)、Aningan(月神)、Malina(太陽女神)、Silap Inua(生命之息/宇宙靈)、Nanook(北極熊主)、Torngasoak(天空大神)、Tekkeitsertok(馴鹿神/狩獵)、Pinga(生育與狩獵女神)、Nerrivik(海之供養者)、Anguta(冥界之神/Sedna之父)、Akna(生育女神)",
        "stories": ["Sedna的手指化為海獸","Aningan追逐Malina(日夜交替)","Kiviuq英雄之旅","烏鴉盜光","Qallupilluit冰下妖怪","Amarok巨狼傳說"],
        "order": 30
    },
    {
        "id": "armenian", "name": "亞美尼亞神話", "name_en": "Armenian Mythology",
        "region": "南高加索—亞美尼亞高原", "era": "烏拉爾圖—基督教化前(至4世紀)",
        "sources": ["莫夫謝斯·霍列納齊《亞美尼亞史》","烏拉爾圖銘文","民間史詩《薩遜的大衛》","希臘-羅馬作家記載"],
        "motifs": ["Hayk建國神話","Aramazd眾神之父","Vahagn雷神","Anahit生育女神","Tir智慧神","Aralez神犬復活","聖山Ararat/Nakhichevan"],
        "parallels": [["Hayk射殺Bel(巨人)","希臘/印度巨人神話"],["Aramazd眾神之父","宙斯/朱庇特/Ahura Mazda"],["Vahagn取草/擊龍","因陀羅戰弗栗多/索爾戰蛇"]],
        "creation": "亞美尼亞創世神話受波斯(阿契美尼德)影響深刻——Aramazd(來自Ahura Mazda)為眾神之父與造物主，掌管天地。世界由Aramazd以六天創造。大地為圓形海洋環繞，聖山Ararat為世界中心。英雄Hayk(亞美尼亞先祖)反抗巨人Bel，以弓箭射殺之，建立亞美尼亞民族——此為建國神話核心。",
        "flood": "亞美尼亞洪水傳說受聖經挪亞方舟影響，但與本土傳統融合——挪亞方舟停泊於Ararat山(亞美尼亞境內)。本土版本：Aramazd以洪水懲罰人類傲慢，Aralez神犬舔舐死者傷口使其復活。傳說大地在三重天之下，洪水來自天地之間的原水破裂。",
        "pantheon": "Aramazd(眾父/造物)、Anahit(生育/醫療/智慧)、Vahagn(雷/火/英雄)、Tir(文字/預言/智慧)、Astghik(愛/美/水)、Nane(戰/母親)、Mihr(太陽/密特拉)、Spandaramet(冥界/地母)、Hayk(先祖英雄)、Aralez(神犬/復活)、Gisane(葡萄/狂喜)",
        "stories": ["Hayk射殺巨人Bel","Vahagn取草戰龍","Artavazd受困於Mashtots山","Ara the Beautiful與Semiramis","薩遜的大衛史詩"],
        "order": 31
    },
    {
        "id": "philippine", "name": "菲律賓神話", "name_en": "Philippine Mythology",
        "region": "東南亞—菲律賓群島", "era": "史前—西班牙殖民前",
        "sources": ["西班牙傳教士記錄","口傳傳統(各地區異文)","《Boxer Codex》","民族誌比較"],
        "motifs": ["Bathala最高神","Malakas與Maganda(強壯與美麗)","竹中生出第一對人類","Luzon/Visayas/Mindanao三島神話","Aswang鬼怪","Sarimanok神鳥"],
        "parallels": [["竹中生人","東南亞/波利尼西亞竹生人神話"],["大洪水後竹中生新人類","南島語系洪水神話共同源頭"],["Bathala","Tengri/天空神跨文化比較"]],
        "creation": "最初世界只有天空、海洋與一隻巨鳥。巨鳥引發風暴，攪動海洋，天空與海洋交戰。從泡沫中誕生Bathala(至高神)與Ulilang Kaluluwa(長蛇神)。二者鬥爭後Bathala以椰子、棕櫚創造大地。另一版本(Maranao)：世界從巨大的竹節中生出——天地最初相連，神以刀斬斷竹子，竹中走出第一對人類兄妹Malakas(強壯)與Maganda(美麗)。",
        "flood": "他加祿族(Tagalog)洪水神話：人類忘記敬拜Bathala，Bathala以洪水懲罰。僅一對兄妹在竹筏/棕櫚樹上倖存，後為世界重新繁衍。米沙鄢(Visayan)版本：洪水源於海神與風神的爭鬥。棉蘭老島(Maranao)傳說：大洪水後世界被巨蛇Bakunawa吞食月亮引發黑暗與洪水。",
        "pantheon": "Bathala(至高神/造物)、Malakas(強壯之父)、Maganda(美麗之母)、Idiyanale(農業)、Sidapa(死亡/月)、Aman Sinaya(海洋)、Kaptan(天空神)、Maguayan(海神)、Bakunawa(月食巨蛇)、Dalikamata(千眼醫神)、Lakapati(豐收/雌雄同體)、Tala(星辰女神)、Mayari(月神)",
        "stories": ["Malakas與Maganda從竹中誕生","Bakunawa吞月(月食由來)","Bernardo Carpio山間巨人","Mariang Makiling山靈傳說","Aswang之夜","Sarimanok神鳥傳說"],
        "order": 32
    },
    {
        "id": "caucasian", "name": "高加索神話", "name_en": "Caucasian (Nart) Mythology",
        "region": "高加索山脈(奧塞提亞/切爾克斯/阿布哈茲)", "era": "史前—中世紀",
        "sources": ["納爾特史詩(Nart sagas)","奧塞提亞口傳","切爾克斯民間故事","喬治亞&亞美尼亞文獻"],
        "motifs": ["納爾特英雄群","Sosruko(文化英雄)","Satana(智慧女巫)","魔法大鍋Nartyamonga","Barastyr冥界","會說話的馬","龍/巨蛇戰"],
        "parallels": [["Sosruko受石頭中出生","希臘雅典娜/赫菲斯托斯"],["納爾特英雄Epic","希臘荷馬史詩/印度摩訶婆羅多"],["魔法大鍋Nartyamonga","凱爾特魔法鍋/聖杯"]],
        "creation": "高加索納爾特創世觀：混沌之初，世界由一位造物主(奧塞提亞語：Xwycau/高加索語：Tkhash)創造。天地最初連接，後被分離。人類從泥土中創造。納爾特人的祖先為半神半人的英雄族群——他們比普通人類更強大、更聰明，但終因傲慢而被神滅絕。世界由一株巨大的宇宙樹支撐，樹頂通天堂、根連冥界。",
        "flood": "納爾特史詩中記載大洪水——人類犯下重罪(或納爾特人傲慢挑戰神)，上天降下洪水毀滅世界。部分納爾特英雄乘坐魔法船/大鍋倖存。洪水消退後，世界由倖存的納爾特人或神重新創造。Uastyrdzhi(聖喬治基督教化版本)成為洪水後人類的保護者。",
        "pantheon": "Xwycau(獨一神/造物)、Uastyrdzhi(聖喬治/戰/旅者)、Washtin(戰神/Fate)、Fælværa(牛羊守護)、Tutyr(狼神)、Donbettyr(海/水神)、Safa(誓言/爐灶神)、Mardagan(雷神)、Naf(祖先靈魂)、Barastyr(冥界王者)",
        "stories": ["Sosruko從石中誕生","Satana的智慧","Batradz's死亡","納爾特盛宴與大鍋","Soslan與戰士之死","Nart大洪水","蛇戰傳說"],
        "order": 33
    },
    {
        "id": "dacian", "name": "達基亞/羅馬尼亞神話", "name_en": "Dacian/Romanian Mythology",
        "region": "東南歐—喀爾巴阡山脈", "era": "達基亞王國—羅馬化後",
        "sources": ["希羅多德《歷史》","斯特拉波《地理學》","羅馬作家記載","羅馬尼亞民間傳說","比較神話學"],
        "motifs": ["Zalmoxis不死神","Gebeleizis雷神","Bendis月亮女神","Derzelas健康神","Kogaionon聖山","Mioriţa牧羊史詩","Căluşari儀式舞蹈"],
        "parallels": [["Zalmoxis不死神","埃及歐西里斯/希臘狄奧尼索斯"],["Gebeleizis雷神","宙斯/索爾/Perun"],["聖山Kogaionon","希臘奧林帕斯/中國崑崙"]],
        "creation": "達基亞人認為Zalmoxis為造物主與不死之神。世界由Zalmoxis創造——最初只有無邊黑暗與原水，Zalmoxis以言創造光明、大地、天空。人類由泥土所造——Zalmoxis將靈魂吹入人體。基督教化後的羅馬尼亞版本將Zalmoxis與聖Elijah融合。羅馬尼亞民間宇宙觀中，世界由三根宇宙柱支撐，柱動則地震。",
        "flood": "達基亞神話中洪水與Gebeleizis的雷暴相關——Gebeleizis以雷電劈開天空，降下滌罪洪水。部分傳說人類因背叛Zalmoxis的教誨而遭洪水毀滅。基督教化後融合為挪亞方舟傳說——但羅馬尼亞民間保留「白鶴引路」的本土元素。喀爾巴阡山區村莊保留關於「上古大浪」的集體記憶。",
        "pantheon": "Zalmoxis(造物/不死/冥界)、Gebeleizis(雷/暴風/光明)、Bendis(月/狩獵)、Derzelas(健康/冥界)、Kotys(大地之母/狂喜)、Heros(騎馬英雄神)、Pleistoros(戰神)、Diana(羅馬化月神/狩獵，融合Bendis)、Dacian Mars(達基亞戰神)",
        "stories": ["Zalmoxis地下居所三千年","Gebeleizis懲罰不義","Mioriţa命運的羊","Meşterul Manole工匠獻祭","Solomonari巫師傳說","Căluşari魔法戰舞"],
        "order": 34
    }
]

# ── New themes ──────────────────────────────────────────────────────────────
NEW_THEMES = [
    {
        "id": "trickster-figures",
        "name": "騙子神話比較研究",
        "name_en": "Comparative Trickster Myths",
        "cultures_covered": ["African","Native American","Norse","Slavic","Hawaiian","Basque","Yoruba","Japanese","Greek","Polynesian"],
        "key_observations": "騙子(Trickster)是神話中超越善惡的邊緣角色——他們破壞秩序卻同時創造新可能。非洲Anansi(蜘蛛)、美洲Coyote(郊狼)、北歐Loki、斯拉夫Veles、希臘Hermes、波利尼西亞Māui、日本的狐/狸、約魯巴Eshu、夏威夷Kane，皆共享(1)變形能力(2)跨越邊界(3)以智慧挑戰權威(4)性/食慾旺盛(5)意外促成文明進步。騙子既非全善亦非全惡——他們體現宇宙的混沌創造力。",
        "order": 112
    },
    {
        "id": "hero-journey",
        "name": "英雄之旅：神話原型的全球比較",
        "name_en": "Hero's Journey: The Monomyth Across Cultures",
        "cultures_covered": ["Greek","Hindu","Chinese","Mayan","Japanese","Persian","Celtic","Egyptian","Philippine","Norse"],
        "key_observations": "Campbell的「英雄之旅」單一神話框架在跨文化中具有驚人普遍性：(1)平凡世界召喚(2)跨越門檻(3)考驗與盟友(4)最深的洞穴(5)苦難(6)獎賞(7)回歸之路(8)重生。希臘Heracles、印度Rama、中國后羿/孫悟空、瑪雅英雄雙子、日本桃太郎、波斯Rustam、愛爾蘭Cú Chulainn、埃及Horus均遵循此模式。然而此框架也有局限性——女性英雄與集體英雄的故事常被邊緣化。",
        "order": 113
    },
    {
        "id": "lunar-deities",
        "name": "月神崇拜與月神話",
        "name_en": "Lunar Deities and Moon Myths",
        "cultures_covered": ["Greek","Egyptian","Hindu","Incan","Japanese","Baltic","Chinese","Mesopotamian","Mayan","Aboriginal"],
        "key_observations": "月亮在神話中的三相性(盈/滿/虧)對應(1)女性三階段(少女/母親/老婦)(2)生命週期(出生/成熟/死亡)(3)冥界象徵。希臘Selene/Artemis/Hecate三面、埃及Thoth(月之計算)、印度Soma(月之甘露)、印加Mama Quilla、日本月讀命、中國嫦娥、波羅的Mēness、蘇美Nanna/Sin、瑪雅月神Ix Chel。月食跨文化被解釋為天狗/巨蛇/豹吞噬月亮(中國/菲律賓/印加)。",
        "order": 114
    },
    {
        "id": "divine-twins",
        "name": "雙生神與英雄雙子比較",
        "name_en": "Divine Twins and Hero Twins Across Cultures",
        "cultures_covered": ["Greek","Hindu","Mayan","Chinese","Egyptian","Norse","Baltic","Philippine","Native American","African"],
        "key_observations": "雙子主題的跨文化類型：(1)善惡對立雙子(埃及Horus/Set,波斯Ahura Mazda/Angra Mainyu)(2)英雄互助雙子(希臘Castor/Pollux,印度Ashwins,瑪雅英雄雙子,波羅的Ašvieniai)(3)文化對立雙子(中國伏羲/女媧,菲律賓Malakas/Maganda)(4)競爭雙子(以掃/雅各, Romulus/Remus)。雙子常代表二元宇宙觀——光明/黑暗、秩序/混沌、天空/大地。",
        "order": 115
    },
    {
        "id": "thunder-gods",
        "name": "雷神跨文化比較",
        "name_en": "Thunder Gods Across Cultures",
        "cultures_covered": ["Norse","Greek","Hindu","Slavic","Chinese","Aztec","Yoruba","Baltic","Persian","Mongolian","Finno-Ugric","Japanese"],
        "key_observations": "雷神在印歐語系中的共同根源(從*Perkʷunos衍化出北歐Thor/Fjörgyn、斯拉夫Perun、波羅的Perkūnas、赫梯Pirwa、印度Parjanya)。跨文化特質：(1)手持槌/斧/雷電武器(2)乘戰車/山羊/公羊(3)雨水/農業/豐收關聯(4)與巨蛇/混沌怪獸戰鬥(Thor戰耶夢加得、Perun戰Veles、因陀羅戰弗栗多)(5)神王/權威象徵(希臘Zeus、中國雷公雖由天帝管轄)。日本的雷神Raijin、非洲Shango、馬雅Chaac為非印歐系統。",
        "order": 116
    },
    {
        "id": "resurrection-myths",
        "name": "死而復生：救贖與重生的神話原型",
        "name_en": "Resurrection and Rebirth Myths",
        "cultures_covered": ["Egyptian","Greek","Norse","Hindu","Mesopotamian","Mayan","Persian","Celtic","Japanese","Chinese"],
        "key_observations": "死而復生神話的核心共通結構：(1)神/英雄死亡(2)哀悼(3)穿越冥界(4)回歸帶來新生命。類型A—季節循環型(埃及歐西里斯、希臘Persephone、美索不達米亞杜姆茲、北歐巴德爾)：死亡與復活反映農耕/自然周期。類型B—英雄穿越型(希臘奧菲斯、日本伊邪那岐、蘇美伊南娜)：英雄入冥界取回死者或知識。類型C—犧牲轉化型(波斯Mithra、瑪雅玉米神、印度Purusha、北歐Odin自懸)：透過死亡創造新世界。",
        "order": 117
    },
    {
        "id": "sacred-waters",
        "name": "聖水與創世源泉",
        "name_en": "Sacred Waters and Primordial Springs",
        "cultures_covered": ["Mesopotamian","Egyptian","Chinese","Hindu","Norse","Greek","Mayan","Persian","Celtic","African","Japanese","Aboriginal"],
        "key_observations": "原初之水(Chaos/Abzu/Nun/Ymir之血/原海)為跨文化創世最普遍的母題之一。類型：(1)創世原水(美索不達米亞Abzu+Tiamat、埃及Nun、希臘Oceanus、中國混沌如雞子)(2)聖河/井的療癒與淨化功能(印度恆河、凱爾特Brigid井、日本禊祓、基督教洗禮)(3)智慧之泉(北歐Mímir井、希臘Hippocrene)(4)冥界水域(希臘Styx/Léthē、埃及冥河、中國黃泉、日本黃泉比良坂)。原水象徵潛能、混沌與未分化狀態——創造即為對原水的分化與秩序化。",
        "order": 118
    },
    {
        "id": "star-myths",
        "name": "星辰神話與天文信仰",
        "name_en": "Star Myths and Celestial Beliefs",
        "cultures_covered": ["Greek","Chinese","Egyptian","Mayan","Polynesian","Aboriginal","Hindu","Norse","Persian","Mongolian"],
        "key_observations": "星辰神話連結天文觀測與宇宙觀：(1)星座為神話人物/動物(希臘Andromeda/Cassiopeia、中國星宿體系)(2)星宿影響命運(美索不達米亞占星、印度Nakshatra)(3)祖先化為星辰(波利尼西亞航海星圖、澳洲Songlines星之路)(4)北極星/北斗七星為永恆秩序象徵(中國北辰/北斗、埃及Imperishable Stars、北歐世界樹軸心)。銀河跨文化被視作神路(希臘、埃及、波利尼西亞、中國天河)。Songlines(澳洲原住民)中以星辰與地貌交織為史詩級導航系統。",
        "order": 119
    }
]

def load_catalog():
    with open(CATALOG, encoding="utf-8") as f:
        return json.load(f)

def save_catalog(catalog):
    with open(CATALOG, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

# ---- Write generation functions (same as populate.py) ----
def generate_culture_index(cat):
    from datetime import datetime
    lines = [
        f"# {cat['name']} ({cat['name_en']})\n",
        f"\n",
        f"- **區域：** {cat['region']}\n",
        f"- **時期：** {cat['era']}\n",
        f"\n",
        f"## 原始文獻\n\n",
    ]
    for s in cat["sources"]:
        lines.append(f"- {s}\n")
    lines.append(f"\n## 創世神話\n\n{cat['creation']}\n\n")
    lines.append(f"## 洪水傳說\n\n{cat['flood']}\n\n")
    lines.append(f"## 神系\n\n{cat['pantheon']}\n\n")
    lines.append(f"## 核心母題\n\n")
    for m in cat["motifs"]:
        lines.append(f"- {m}\n")
    lines.append(f"\n## 跨文化平行\n\n")
    for p in cat["parallels"]:
        lines.append(f"- **{p[0]}** ↔ {p[1]}\n")
    lines.append(f"\n## 重要故事\n\n")
    for s in cat["stories"]:
        lines.append(f"- {s}\n")
    lines.append(f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n")
    return "".join(lines)

def generate_theme_index(th):
    from datetime import datetime
    lines = [
        f"# {th['name']}\n",
        f"## {th['name_en']}\n\n",
        f"## 涉及文化\n\n",
    ]
    for c in th["cultures_covered"]:
        lines.append(f"- {c}\n")
    lines.append(f"\n## 關鍵觀察\n\n{th['key_observations']}\n\n")
    lines.append(f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n")
    return "".join(lines)

def update_cultures_index():
    entries = []
    for d in sorted(os.listdir(CULTURES_DIR)):
        if d == "00-index.md" or d.startswith("."):
            continue
        ipath = os.path.join(CULTURES_DIR, d, "index.md")
        if os.path.isfile(ipath):
            with open(ipath, encoding="utf-8") as f:
                first_line = f.readline().strip().lstrip("# ")
            entries.append((d, f"{first_line} ({d})"))
    lines = [
        "# 文化索引\n\n",
        "> 自動生成的索引 — 涵蓋所有已收錄的文化神話體系。\n\n",
        "| 目錄 | 文化 |\n",
        "|------|------|\n",
    ]
    for d, name in entries:
        lines.append(f"| [{d}]({d}/index.md) | {name} |\n")
    lines.append(f"\n\n*總計 {len(entries)} 個文化體系*\n")
    with open(INDEX_CULTURES, "w", encoding="utf-8") as f:
        f.writelines(lines)

def update_themes_index():
    entries = []
    for fname in sorted(os.listdir(THEMES_DIR)):
        if fname == "00-index.md" or fname.startswith("."):
            continue
        fpath = os.path.join(THEMES_DIR, fname)
        if os.path.isfile(fpath):
            with open(fpath, encoding="utf-8") as f:
                first_line = f.readline().strip().lstrip("# ")
            name_noext = fname.replace(".md", "")
            entries.append((name_noext, first_line))
    lines = [
        "# 主題索引\n\n",
        "> 自動生成的索引 — 跨文化主題分析。\n\n",
        "| 檔案 | 主題 |\n",
        "|------|------|\n",
    ]
    for fname, title in entries:
        lines.append(f"| [{fname}]({fname}.md) | {title} |\n")
    lines.append(f"\n\n*總計 {len(entries)} 個主題*\n")
    with open(INDEX_THEMES, "w", encoding="utf-8") as f:
        f.writelines(lines)

def main():
    # Step 1: Expand catalog
    catalog = load_catalog()
    existing_ids = {c["id"] for c in catalog["cultures"]}
    added_cultures = []
    for nc in NEW_CULTURES:
        if nc["id"] not in existing_ids:
            catalog["cultures"].append(nc)
            added_cultures.append(nc["id"])
            print(f"  ✓ Added culture: {nc['name']} ({nc['name_en']})")

    existing_themes = {t["id"] for t in catalog["themes"]}
    added_themes = []
    for nt in NEW_THEMES:
        if nt["id"] not in existing_themes:
            catalog["themes"].append(nt)
            added_themes.append(nt["id"])
            print(f"  ✓ Added theme: {nt['name']} ({nt['name_en']})")

    save_catalog(catalog)
    print(f"\nExpansion summary: {len(added_cultures)} new cultures, {len(added_themes)} new themes")

    # Step 2: Batch generate all culture files
    print("\n── Generating culture files ──")
    for cat in catalog["cultures"]:
        cid = cat["id"]
        cdir = os.path.join(CULTURES_DIR, cid)
        fpath = os.path.join(cdir, "index.md")
        if os.path.isfile(fpath):
            print(f"  ∃ Already exists: cultures/{cid}/index.md")
        else:
            os.makedirs(cdir, exist_ok=True)
            content = generate_culture_index(cat)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  + Generated: cultures/{cid}/index.md")
    update_cultures_index()
    print("  ✓ Updated cultures index")

    # Step 3: Batch generate all theme files
    print("\n── Generating theme files ──")
    for th in catalog["themes"]:
        tid = th["id"]
        fpath = os.path.join(THEMES_DIR, f"{tid}.md")
        if os.path.isfile(fpath):
            print(f"  ∃ Already exists: themes/{tid}.md")
        else:
            content = generate_theme_index(th)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  + Generated: themes/{tid}.md")
    update_themes_index()
    print("  ✓ Updated themes index")

    print("\n✅ All expansions complete!")

if __name__ == "__main__":
    main()
