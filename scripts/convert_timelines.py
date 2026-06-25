#!/usr/bin/env python3
"""Convert _catalog.json era strings to structured timeline objects."""
import json, re, sys

REPO = "/workspace/projects/mythos-atlas"
CATALOG = f"{REPO}/_catalog.json"

catalog = json.load(open(CATALOG, encoding="utf-8"))

def parse_bc_range(s):
    """Parse strings like '公元前1600-1200' or '公元前8-3世紀' into (start, end) years."""
    s = s.strip()
    m = re.match(r'公元前(\d+)-(\d+)年?', s)
    if m:
        return (-int(m.group(1)), -int(m.group(2)))
    m = re.match(r'公元前(\d+)-(\d+)世紀', s)
    if m:
        return ( -int(m.group(1))*100,  -int(m.group(2))*100)
    return None

def generate_timeline(cat):
    """Generate structured timeline from existing era string."""
    cid = cat["id"]
    era = cat.get("era", "")
    tl = {"precision": "era_label"}

    if cid == "chinese":
        tl.update({"start_year": -3000, "end_year": -256,
                    "periods": [{"name": "神農—夏", "start": -3000, "end": -1600},
                                 {"name": "商", "start": -1600, "end": -1046},
                                 {"name": "周", "start": -1046, "end": -256}],
                    "overlap_with": ["mesopotamian", "egyptian", "minoan", "hittite"],
                    "precision": "century"})
    elif cid == "mesopotamian":
        tl.update({"start_year": -3500, "end_year": -539,
                    "periods": [{"name": "蘇美城邦", "start": -3500, "end": -2334},
                                 {"name": "阿卡德帝國", "start": -2334, "end": -2154},
                                 {"name": "巴比倫", "start": -1894, "end": -539},
                                 {"name": "亞述帝國", "start": -1363, "end": -609}],
                    "overlap_with": ["egyptian", "hittite", "minoan", "sumerian"],
                    "precision": "century"})
    elif cid == "greek":
        tl.update({"start_year": -1600, "end_year": 146,
                    "periods": [{"name": "邁錫尼時期", "start": -1600, "end": -1100},
                                 {"name": "黑暗時期", "start": -1100, "end": -800},
                                 {"name": "古風時期", "start": -800, "end": -480},
                                 {"name": "古典時期", "start": -480, "end": -323},
                                 {"name": "希臘化時期", "start": -323, "end": 146}],
                    "overlap_with": ["egyptian", "mesopotamian", "minoan", "roman"],
                    "precision": "century"})
    elif cid == "egyptian":
        tl.update({"start_year": -3100, "end_year": 30,
                    "periods": [{"name": "古王國", "start": -2686, "end": -2181},
                                 {"name": "中王國", "start": -2055, "end": -1650},
                                 {"name": "新王國", "start": -1550, "end": -1069},
                                 {"name": "晚期", "start": -664, "end": -332},
                                 {"name": "托勒密時期", "start": -332, "end": 30}],
                    "overlap_with": ["mesopotamian", "hittite", "minoan", "nubian", "greek"],
                    "precision": "century"})
    elif cid == "norse":
        tl.update({"start_year": 200, "end_year": 1066,
                    "periods": [{"name": "日耳曼鐵器時代", "start": 200, "end": 800},
                                 {"name": "維京時期", "start": 793, "end": 1066}],
                    "overlap_with": ["celtic", "roman", "slavic", "finno-ugric"],
                    "precision": "century"})
    elif cid == "hindu":
        tl.update({"start_year": -1500, "end_year": 1200,
                    "periods": [{"name": "吠陀時期", "start": -1500, "end": -500},
                                 {"name": "史詩—往世書時期", "start": -500, "end": 500},
                                 {"name": "中世紀印度教", "start": 500, "end": 1200}],
                    "overlap_with": ["mesopotamian", "persian", "greek", "chinese"],
                    "precision": "century"})
    elif cid == "mayan":
        tl.update({"start_year": -2000, "end_year": 1697,
                    "periods": [{"name": "前古典期", "start": -2000, "end": 250},
                                 {"name": "古典期", "start": 250, "end": 900},
                                 {"name": "後古典期", "start": 900, "end": 1697}],
                    "overlap_with": ["incan", "indigenous-americas"],
                    "precision": "century"})
    elif cid == "japanese":
        tl.update({"start_year": -300, "end_year": 794,
                    "periods": [{"name": "彌生", "start": -300, "end": 250},
                                 {"name": "古墳", "start": 250, "end": 538},
                                 {"name": "飛鳥", "start": 538, "end": 710},
                                 {"name": "奈良", "start": 710, "end": 794}],
                    "overlap_with": ["chinese", "korean"],
                    "precision": "century"})
    elif cid == "polynesian":
        tl.update({"start_year": -1500, "end_year": 1800,
                    "periods": [{"name": "拉皮塔時期", "start": -1500, "end": -500},
                                 {"name": "波利尼西亞大遷徙", "start": -500, "end": 1200},
                                 {"name": "古典波利尼西亞", "start": 1200, "end": 1800}],
                    "overlap_with": ["aboriginal", "maori"],
                    "precision": "century"})
    elif cid == "incan":
        tl.update({"start_year": -3000, "end_year": 1572,
                    "periods": [{"name": "前陶器時期", "start": -3000, "end": -1800},
                                 {"name": "形成期", "start": -1800, "end": -200},
                                 {"name": "區域發展期", "start": -200, "end": 600},
                                 {"name": "瓦里—蒂亞瓦納科", "start": 600, "end": 1100},
                                 {"name": "印加帝國", "start": 1438, "end": 1572}],
                    "overlap_with": ["mayan", "indigenous-americas", "mapuche"],
                    "precision": "century"})
    elif cid == "celtic":
        tl.update({"start_year": -800, "end_year": 1200,
                    "periods": [{"name": "哈爾施塔特", "start": -800, "end": -450},
                                 {"name": "拉坦諾", "start": -450, "end": -1},
                                 {"name": "羅馬—中世紀", "start": 1, "end": 1200}],
                    "overlap_with": ["norse", "roman", "greek", "basque"],
                    "precision": "century"})
    elif cid == "slavic":
        tl.update({"start_year": 400, "end_year": 1200,
                    "periods": [{"name": "早期斯拉夫", "start": 400, "end": 800},
                                 {"name": "基輔羅斯", "start": 882, "end": 1200}],
                    "overlap_with": ["norse", "finno-ugric", "baltic"],
                    "precision": "century"})
    elif cid == "persian":
        tl.update({"start_year": -1000, "end_year": 651,
                    "periods": [{"name": "阿契美尼德帝國", "start": -550, "end": -330},
                                 {"name": "帕提亞", "start": -247, "end": 224},
                                 {"name": "薩珊帝國", "start": 224, "end": 651}],
                    "overlap_with": ["mesopotamian", "greek", "hindu", "pre-islamic-arabian"],
                    "precision": "century"})
    elif cid == "korean":
        tl.update({"start_year": -2333, "end_year": 935,
                    "periods": [{"name": "古朝鮮", "start": -2333, "end": -108},
                                 {"name": "三國時代", "start": -57, "end": 668},
                                 {"name": "統一新羅", "start": 668, "end": 935}],
                    "overlap_with": ["chinese", "japanese"],
                    "precision": "century"})
    elif cid == "finno-ugric":
        tl.update({"start_year": -1000, "end_year": 1300,
                    "periods": [{"name": "烏拉爾共同期", "start": -1000, "end": -500},
                                 {"name": "芬蘭—烏戈爾分化", "start": -500, "end": 500},
                                 {"name": "基督教化前", "start": 500, "end": 1300}],
                    "overlap_with": ["norse", "slavic", "siberian", "sami"],
                    "precision": "century"})
    elif cid == "tibetan":
        tl.update({"start_year": -500, "end_year": 800,
                    "periods": [{"name": "張雄", "start": -500, "end": 600},
                                 {"name": "吐蕃帝國", "start": 600, "end": 842}],
                    "overlap_with": ["chinese", "hindu", "mongolian"],
                    "precision": "century"})
    elif cid == "sumerian":
        tl.update({"start_year": -4500, "end_year": -2004,
                    "periods": [{"name": "烏魯克時期", "start": -4000, "end": -3100},
                                 {"name": "早王朝時期", "start": -2900, "end": -2334},
                                 {"name": "烏爾第三王朝", "start": -2112, "end": -2004}],
                    "overlap_with": ["mesopotamian", "egyptian", "minoan"],
                    "precision": "century"})
    elif cid == "phoenician":
        tl.update({"start_year": -1500, "end_year": -146,
                    "periods": [{"name": "青銅時代", "start": -1500, "end": -1200},
                                 {"name": "腓尼基城邦", "start": -1200, "end": -539},
                                 {"name": "波斯—希臘化", "start": -539, "end": -146}],
                    "overlap_with": ["mesopotamian", "egyptian", "greek", "pre-islamic-arabian"],
                    "precision": "century"})
    elif cid == "hittite":
        tl.update({"start_year": -1750, "end_year": -1178,
                    "periods": [{"name": "古王國", "start": -1650, "end": -1500},
                                 {"name": "新王國", "start": -1430, "end": -1178}],
                    "overlap_with": ["mesopotamian", "egyptian", "minoan", "phoenician"],
                    "precision": "century"})
    elif cid == "yoruba":
        tl.update({"start_year": 1000, "end_year": 1900,
                    "periods": [{"name": "約魯巴城邦形成", "start": 1000, "end": 1400},
                                 {"name": "奧約帝國", "start": 1400, "end": 1835},
                                 {"name": "殖民時期", "start": 1835, "end": 1900}],
                    "overlap_with": ["african", "egyptian", "nubian"],
                    "precision": "century"})
    elif cid == "mongolian":
        tl.update({"start_year": -209, "end_year": 1368,
                    "periods": [{"name": "匈奴", "start": -209, "end": 100},
                                 {"name": "突厥—回鶻", "start": 552, "end": 840},
                                 {"name": "蒙古帝國", "start": 1206, "end": 1368}],
                    "overlap_with": ["chinese", "tibetan", "siberian", "persian"],
                    "precision": "century"})
    elif cid == "ainu":
        tl.update({"start_year": -300, "end_year": 1900,
                    "periods": [{"name": "繩文晚期", "start": -300, "end": 300},
                                 {"name": "鄂霍次克文化", "start": 500, "end": 1200},
                                 {"name": "愛努文化期", "start": 1200, "end": 1900}],
                    "overlap_with": ["japanese", "siberian", "ainu"],
                    "precision": "century"})
    elif cid == "etruscan":
        tl.update({"start_year": -900, "end_year": -27,
                    "periods": [{"name": "維拉諾瓦", "start": -900, "end": -700},
                                 {"name": "伊特魯里亞城邦", "start": -700, "end": -396},
                                 {"name": "羅馬化", "start": -396, "end": -27}],
                    "overlap_with": ["greek", "roman", "phoenician"],
                    "precision": "century"})
    elif cid == "basque":
        tl.update({"start_year": -5000, "end_year": 1000,
                    "periods": [{"name": "新石器時代", "start": -5000, "end": -2500},
                                 {"name": "青銅—鐵器時代", "start": -2500, "end": -1},
                                 {"name": "羅馬化前", "start": 1, "end": 1000}],
                    "overlap_with": ["celtic", "roman", "phoenician"],
                    "precision": "century"})
    elif cid == "baltic":
        tl.update({"start_year": -2000, "end_year": 1400,
                    "periods": [{"name": "波羅的部落聯合", "start": -2000, "end": -500},
                                 {"name": "鐵器時代", "start": -500, "end": 1000},
                                 {"name": "基督教化前", "start": 1000, "end": 1400}],
                    "overlap_with": ["norse", "slavic", "finno-ugric"],
                    "precision": "century"})
    elif cid == "vietnamese":
        tl.update({"start_year": -2879, "end_year": 1400,
                    "periods": [{"name": "雄王時代", "start": -2879, "end": -258},
                                 {"name": "北屬時期", "start": -207, "end": 939},
                                 {"name": "獨立封建時期", "start": 939, "end": 1400}],
                    "overlap_with": ["chinese", "chinese"],
                    "precision": "century"})
    elif cid == "inuit":
        tl.update({"start_year": -2000, "end_year": 1900,
                    "periods": [{"name": "古愛斯基摩", "start": -2000, "end": -500},
                                 {"name": "前因紐特", "start": -500, "end": 1000},
                                 {"name": "圖勒文化", "start": 1000, "end": 1600},
                                 {"name": "歷史因紐特", "start": 1600, "end": 1900}],
                    "overlap_with": ["siberian", "indigenous-americas", "norse"],
                    "precision": "century"})
    elif cid == "armenian":
        tl.update({"start_year": -860, "end_year": 301,
                    "periods": [{"name": "烏拉爾圖", "start": -860, "end": -590},
                                 {"name": "亞美尼亞王國", "start": -331, "end": 1},
                                 {"name": "基督教化", "start": 1, "end": 301}],
                    "overlap_with": ["mesopotamian", "hittite", "persian", "caucasian"],
                    "precision": "century"})
    elif cid == "philippine":
        tl.update({"start_year": -2000, "end_year": 1521,
                    "periods": [{"name": "南島民族遷徙", "start": -2000, "end": -500},
                                 {"name": "呂宋—米沙鄢城邦", "start": 900, "end": 1521}],
                    "overlap_with": ["polynesian", "chinese", "indigenous-americas"],
                    "precision": "century"})
    elif cid == "caucasian":
        tl.update({"start_year": -2000, "end_year": 1500,
                    "periods": [{"name": "青銅—鐵器時代", "start": -2000, "end": -500},
                                 {"name": "科爾基斯—伊比利亞", "start": -500, "end": 500},
                                 {"name": "中世紀高加索", "start": 500, "end": 1500}],
                    "overlap_with": ["hittite", "armenian", "persian", "greek"],
                    "precision": "century"})
    elif cid == "dacian":
        tl.update({"start_year": -1600, "end_year": 106,
                    "periods": [{"name": "達基亞文化形成", "start": -1600, "end": -500},
                                 {"name": "達基亞王國", "start": -500, "end": 106},
                                 {"name": "羅馬達基亞", "start": 106, "end": 271}],
                    "overlap_with": ["greek", "roman", "celtic", "scythian"],
                    "precision": "century"})
    elif cid == "roman":
        tl.update({"start_year": -753, "end_year": 476,
                    "periods": [{"name": "羅馬王政", "start": -753, "end": -509},
                                 {"name": "羅馬共和", "start": -509, "end": -27},
                                 {"name": "羅馬帝國", "start": -27, "end": 476}],
                    "overlap_with": ["greek", "egyptian", "celtic", "etruscan", "phoenician", "persian"],
                    "precision": "century"})
    elif cid == "pre-islamic-arabian":
        tl.update({"start_year": -1200, "end_year": 622,
                    "periods": [{"name": "早期閃族", "start": -1200, "end": -500},
                                 {"name": "南阿拉伯王國", "start": -500, "end": 300},
                                 {"name": "賈希利亞", "start": 300, "end": 622}],
                    "overlap_with": ["mesopotamian", "egyptian", "phoenician", "persian"],
                    "precision": "century"})
    elif cid == "maori":
        tl.update({"start_year": 1250, "end_year": 1840,
                    "periods": [{"name": "早期毛利", "start": 1250, "end": 1500},
                                 {"name": "古典毛利", "start": 1500, "end": 1800},
                                 {"name": "歐洲接觸期", "start": 1769, "end": 1840}],
                    "overlap_with": ["polynesian"],
                    "precision": "century"})
    elif cid == "scythian":
        tl.update({"start_year": -900, "end_year": -200,
                    "periods": [{"name": "斯基泰形成期", "start": -900, "end": -700},
                                 {"name": "斯基泰王國", "start": -700, "end": -300},
                                 {"name": "薩爾馬提亞", "start": -300, "end": -200}],
                    "overlap_with": ["greek", "persian", "caucasian", "dacian", "slavic"],
                    "precision": "century"})
    elif cid == "minoan":
        tl.update({"start_year": -2600, "end_year": -1100,
                    "periods": [{"name": "前王宮時期", "start": -2600, "end": -1900},
                                 {"name": "古王宮時期", "start": -1900, "end": -1700},
                                 {"name": "新王宮時期", "start": -1700, "end": -1450},
                                 {"name": "後王宮時期", "start": -1450, "end": -1100}],
                    "overlap_with": ["egyptian", "hittite", "mesopotamian", "greek"],
                    "precision": "century"})
    elif cid == "nubian":
        tl.update({"start_year": -2000, "end_year": 350,
                    "periods": [{"name": "Kerma文化", "start": -2500, "end": -1500},
                                 {"name": "庫什王國", "start": -800, "end": 350}],
                    "overlap_with": ["egyptian", "yoruba", "african"],
                    "precision": "century"})
    elif cid == "mapuche":
        tl.update({"start_year": -500, "end_year": 1888,
                    "periods": [{"name": "前哥倫布時期", "start": -500, "end": 1541},
                                 {"name": "阿勞科戰爭", "start": 1541, "end": 1818},
                                 {"name": "併入智利", "start": 1818, "end": 1888}],
                    "overlap_with": ["incan", "indigenous-americas"],
                    "precision": "century"})
    elif cid == "sami":
        tl.update({"start_year": -2000, "end_year": 1700,
                    "periods": [{"name": "早期薩米", "start": -2000, "end": -500},
                                 {"name": "北歐鐵器時代", "start": -500, "end": 1000},
                                 {"name": "中世紀晚期", "start": 1000, "end": 1700}],
                    "overlap_with": ["norse", "finno-ugric", "slavic"],
                    "precision": "century"})
    elif cid == "siberian":
        tl.update({"start_year": -3000, "end_year": 1800,
                    "periods": [{"name": "新石器—青銅時代", "start": -3000, "end": -500},
                                 {"name": "斯基泰—西伯利亞", "start": -500, "end": 500},
                                 {"name": "突厥—蒙古期", "start": 500, "end": 1500},
                                 {"name": "俄羅斯擴張期", "start": 1500, "end": 1800}],
                    "overlap_with": ["mongolian", "sami", "ainu", "finno-ugric"],
                    "precision": "century"})
    elif cid == "tupi-guarani":
        tl.update({"start_year": -1000, "end_year": 1760,
                    "periods": [{"name": "前哥倫布時期", "start": -1000, "end": 1500},
                                 {"name": "殖民接觸期", "start": 1500, "end": 1760}],
                    "overlap_with": ["indigenous-americas", "incan", "mapuche"],
                    "precision": "century"})
    elif cid == "aboriginal":
        tl.update({"start_year": -50000, "end_year": 1800,
                    "periods": [{"name": "史前澳洲", "start": -50000, "end": -10000},
                                 {"name": "神話夢世紀", "start": -10000, "end": 1788},
                                 {"name": "殖民接觸", "start": 1788, "end": 1900}],
                    "overlap_with": ["polynesian", "maori"],
                    "precision": "millennium"})
    elif cid == "african":
        tl.update({"start_year": -5000, "end_year": 1900,
                    "periods": [{"name": "史前非洲", "start": -5000, "end": -500},
                                 {"name": "撒哈拉以南王國", "start": 500, "end": 1500},
                                 {"name": "奴隸貿易—殖民", "start": 1500, "end": 1900}],
                    "overlap_with": ["egyptian", "nubian", "yoruba"],
                    "precision": "century"})
    elif cid == "indigenous-americas":
        tl.update({"start_year": -12000, "end_year": 1600,
                    "periods": [{"name": "古印第安期", "start": -12000, "end": -8000},
                                 {"name": "古風期", "start": -8000, "end": -1000},
                                 {"name": "林地區—平原區", "start": -1000, "end": 1000},
                                 {"name": "密西西比文化", "start": 800, "end": 1600}],
                    "overlap_with": ["inuit", "mayan", "incan", "mapuche", "tupi-guarani"],
                    "precision": "millennium"})
    else:
        # Fallback: minimal timeline from era string
        tl.update({"start_year": None, "end_year": None,
                    "periods": [{"name": era, "start": None, "end": None}],
                    "overlap_with": [],
                    "precision": "era_label"})

    return tl

for cat in catalog["cultures"]:
    cat["timeline"] = generate_timeline(cat)

with open(CATALOG, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"✓ Updated {len(catalog['cultures'])} cultures with structured timelines")
