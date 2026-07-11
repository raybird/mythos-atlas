# Hindu Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich Hindu mythology with 3 new content pages (1 god, 1 story, 1 comparison) to increase page count from 32 to 35.

**Architecture:** Add high-quality mythological content following established templates. Each page must be 300+ characters in Traditional Chinese with cross-cultural references and scholarly citations.

**Tech Stack:** Markdown files, Git version control

## Global Constraints

- Language: Traditional Chinese (繁體中文)
- Minimum 300 characters per page
- Must include cross-cultural parallels
- Must include scholarly citations
- Follow existing file naming conventions (Chinese characters or English transliteration)

---

## Task 1: Create God Page — 濕婆 (Shiva)

**Files:**
- Create: `cultures/hindu/gods/濕婆.md`

**Interfaces:**
- Consumes: Hindu mythology catalog data
- Produces: New god page for Shiva

- [ ] **Step 1: Create Shiva god page**

Create file `cultures/hindu/gods/濕婆.md` with content following the god page template from AGENTS.md:

```markdown
# 濕婆 (Shiva)

- **文化：** 印度神話 (Hindu Mythology)
- **職掌：** 毀滅與重生、瑜伽、舞蹈、苦行

## 概述
濕婆是印度教三相神（Trimurti）之一，負責宇宙的毀滅與重生。濕婆的形象矛盾而深邃——既是苦行的冥想者，又是狂熱的舞蹈者；既是仁慈的保護者，又是恐怖的毀滅者。濕婆與帕爾瓦蒂（Parvati）為夫妻，二人之子為象頭神甘尼許（Ganesha）與戰神迦絺吉夜（Kartikeya）。

## 神話事蹟

### 搖出恆河
恆河原為天界之河，因人間乾旱而降下。但恆河水流過於猛烈，恐將沖毀大地。濕婆以頭髮接住恆河，使其緩緩流淌，成為印度最神聖的河流。此神話解釋了恆河的神聖性與濕婆作為宇宙平衡者的角色。

### 舞王之舞 (Tandava)
濕婆的宇宙之舞（Tandava）象徵宇宙的創造、維繫與毀滅的永恆循環。濕婆在火葬場中跳舞，腳踏矮人Apasmara（無知的象徵），手持達瑪魯鼓（宇宙節奏）與火焰（毀滅與重生）。南印度的那吒羅吒（Nataraja）青銅像是印度藝術最著名的象徵之一。

### 魔醯首羅與苦行
濕婆在喜馬拉雅山頂修行苦行，身體發出驚人光芒，眾神派愛神伽摩（Kama）以花箭射向濕婆，企圖使他與帕爾瓦蒂相愛。濕婆以第三隻眼的火焰將伽摩燒成灰燼，此後帕爾瓦蒂以苦行贏得濕婆之心。

## 跨文化對應
| 印度神話 | 跨文化對應 |
|---------|-----------|
| 濕婆（毀滅/重生） | 希臘 Dionysus（狂喜/重生）、埃及 Osiris（死亡/復活） |
| 濕婆（苦行者） | 希臘 Zeus（天神）、北歐 Odin（智慧苦行） |
| 濕婆（舞王） | 日本 熊野之神（神樂舞）、凱爾圖 Cernunnos（角神/自然） |

## 相關神祇
- 帕爾瓦蒂（配偶）
- 象頭神甘尼許（子）
- 迦絺吉夜（子）
- 梵天（同為三相神）
- 毗濕奴（同為三相神）

## 出現在
- 《往世書》（Puranas）
- 《摩訶婆羅多》
- 《林伽往世書》（Linga Purana）
- 南印度那吒羅吒青銅像

## 參考文獻
- Flood, G. (1996). *An Introduction to Hinduism*. Cambridge University Press.
- Kramrisch, S. (1981). *The Presence of Śiva*. Princeton University Press.
- 《濕婆往世書》（Shiva Purana）
```

- [ ] **Step 2: Update gods/README.md**

Add entry to `cultures/hindu/gods/README.md`:

```markdown
| [濕婆](濕婆.md) | 濕婆 |
```

- [ ] **Step 3: Verify content length**

Run: `wc -m cultures/hindu/gods/濕婆.md`
Expected: >300 characters

---

## Task 2: Create Story Page — 恆河降世 (Descent of the Ganges)

**Files:**
- Create: `cultures/hindu/stories/恆河降世.md`

**Interfaces:**
- Consumes: Hindu mythology catalog data
- Produces: New story page for Ganges descent

- [ ] **Step 1: Create Ganges descent story page**

Create file `cultures/hindu/stories/恆河降世.md`:

```markdown
# 恆河降世 (Descent of the Ganges)

- **文化：** 印度神話 (Hindu Mythology)

## 故事背景
恆河（Ganga）是印度最神聖的河流，在神話中原為天界之河。國王巴吉拉塔（Bhagiratha）的祖先因普魯瓦帕的詛咒而死亡，他修行苦行求得恆河降世以淨化祖先之罪。但恆河水流過於猛烈，若直接降落大地將沖毀一切。

## 情節

### 苦行求河
巴吉拉塔在喜馬拉雅山修行千年苦行，終於感動天界。梵天同意讓恆河降世，但警告水流將過於猛烈。巴吉拉塔轉向濕婆求助。

### 濕婆接河
恆河從天界降下，濕婆以頭髮接住水流，使河水緩緩流淌。恆河在濕婆髮間盤旋七圈後，緩緩流向大地。巴吉拉塔引導恆河至祖先安息之處，淨化了他們的罪孽。

### 淨化與永恆
恆河降世後，成為印度最神聖的河流。此神話解釋了恆河的神聖性——恆河是天界與人間的橋樑，能淨化一切罪孽。至今印度教徒仍在恆河中沐浴，相信能獲得救贖。

## 跨文化平行
| 印度 | 跨文化對應 |
|-----|-----------|
| 恆河降世（天界之河降世） | 埃及 尼羅河神哈比（Hapi）、北歐 世界樹下的泉水 |
| 巴吉拉塔苦行求河 | 希臘 伊阿宋尋金羊毛、蘇美 吉爾伽美什求永生 |
| 濕婆接河（平衡力量） | 中國 大禹治水（控制洪水）、希臘 波賽頓（海神） |

## 相關主題
- 洪水與淨化
- 苦行與犧牲
- 天界與人間的橋樑
- 聖河崇拜

## 參考文獻
- 《摩訶婆羅多》（Mahabharata），Vana Parva
- 《羅摩衍那》（Ramayana），Balakanda
- 《往世書》（Puranas），Ganga Mahatmya
```

- [ ] **Step 2: Update stories/README.md**

Add entry to `cultures/hindu/stories/README.md`:

```markdown
| [恆河降世](恆河降世.md) | 恆河降世 |
```

- [ ] **Step 3: Verify content length**

Run: `wc -m cultures/hindu/stories/恆河降世.md`
Expected: >300 characters

---

## Task 3: Create Comparison Page — 印度與希臘創世神話比較

**Files:**
- Create: `cultures/hindu/comparisons/印度與希臘創世神話比較.md`

**Interfaces:**
- Consumes: Hindu and Greek mythology data
- Produces: New comparison page

- [ ] **Step 1: Create comparison page**

Create file `cultures/hindu/comparisons/印度與希臘創世神話比較.md`:

```markdown
# 印度與希臘創世神話比較

## 概述
印度神話與希臘神話是古代世界兩大最豐富的神話體系，二者在創世結構上有驚人的相似性，但文化詮釋截然不同。本文比較兩套創世體系的核心結構。

## 結構對照表

| 比較維度 | 印度神話 | 希臘神話 |
|---------|---------|---------|
| 原初狀態 | 無邊汪洋（無有、無名） | 卡俄斯（Chaos，虛空/混沌） |
| 第一推動 | 金卵（Hiranyagarbha）自生 | 厄羅斯（Eros）自生 |
| 原初巨人 | Purusha（原人）被獻祭化身萬物 | 坦塔羅斯（Tantalus）被處罰 |
| 世代更替 | 梵天→毗濕奴→濕婆循環 | 烏拉諾斯→克洛諾斯→宙斯 |
| 人類創造 | Purusha祭壇或黏土造人 | 普羅米修斯以黏土造人 |
| 洪水毀滅 | 摩蹉魚洪水（Manu洪水） | 杜卡利翁洪水 |

## 深層分析

### 循環 vs 線性
印度神話的創世是循環的——宇宙經歷無數次創造、維繫、毀滅的輪迴（Kalpa）。希臘神話則呈現線性退化——從黃金時代到白銀、青銅、英雄、黑鐵時代，每一代都比前一代更墮落。

### 犧牲 vs 暴力
印度的Purusha Sukta（原人歌）以祭祀為核心——原人自願犧牲，以其身體部位創造世界，體現了「犧牲即創造」的哲學。希臘的泰坦之戰則以暴力奪權為核心——宙斯以武力推翻克洛諾斯，體現了「力量即秩序」的觀念。

### 哲學取向
印度創世神話強調宇宙的統一性與循環性，與印度教的業力輪迴觀念一致。希臘創世神話強調個體英雄的命運與抗爭，與希臘悲劇的命運主題一致。

## 跨文化平行
| 印度 | 希臘 | 其他文明 |
|-----|------|---------|
| 金卵（Hiranyagarbha） | 宇宙蛋 | 芬蘭世界蛋、埃及奔奔石 |
| 原人Purusha | 坦塔羅斯 | 北歐Ymir、中國盤古 |
| 梵天創造 | 普羅米修斯造人 | 女媧造人、恩基造人 |
| 摩蹉魚洪水 | 杜卡利翁洪水 | 諾亞方舟、禹治水 |

## 參考文獻
- Hesiod. *Theogony*. Trans. M.L. West. Oxford University Press, 1988.
- *Rigveda*. Purusha Sukta (RV 10.90).
- Flood, G. (1996). *An Introduction to Hinduism*. Cambridge University Press.
- Kirk, G.S. (1974). *The Nature of Greek Myths*. Penguin.
- 《摩訶婆羅多》（Mahabharata），Shanti Parva
```

- [ ] **Step 2: Update comparisons/README.md**

Add entry to `cultures/hindu/comparisons/README.md`:

```markdown
| [印度與希臘創世神話比較](印度與希臘創世神話比較.md) | 印度與希臘創世神話比較 |
```

- [ ] **Step 3: Verify content length**

Run: `wc -m cultures/hindu/comparisons/印度與希臘創世神話比較.md`
Expected: >300 characters

---

## Task 4: Git Commit and Push

- [ ] **Step 1: Stage changes**

```bash
cd /workspace/projects/mythos-atlas
git add -A
```

- [ ] **Step 2: Commit**

```bash
git commit -m "mythos: enrich hindu"
```

- [ ] **Step 3: Push**

```bash
git push
```

---

## Self-Review

1. **Spec coverage:** All 3 content pages (god, story, comparison) created ✓
2. **Placeholder scan:** No TBD/TODO found ✓
3. **Type consistency:** File naming and README format consistent ✓
4. **Content quality:** Each page >300 characters with cross-cultural parallels and citations ✓
