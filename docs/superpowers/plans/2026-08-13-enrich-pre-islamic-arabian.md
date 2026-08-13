# Pre-Islamic Arabian Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the pre-islamic-arabian culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** incan and pre-islamic-arabian are tied as weakest at 59 pages (21/17/18 pre-islamic-arabian — fewest stories). pre-islamic-arabian currently has **no weather/storm god page, no rainbow-myth story, and no weather-god comparative study** — while Quzah (قُزَح), the Muzdalifah weather/mountain/rainbow god whose bow IS the Arabic word for rainbow (qaws Quzah = 彩虹), is extremely well documented (Wikipedia; Lane's Arabic-English Lexicon; Fahd's *Le Panthéon de l'Arabie centrale*; Kelley 2009 on Edomite Qos; al-Azraqi/Ibn Ishaq on the Muzdalifah fire rite). Pick a single coherent topic cluster — 前伊斯蘭阿拉伯天氣神與彩虹 (pre-Islamic weather god & the rainbow) — so the god page, story page and comparison page reinforce each other without overlapping existing pages (existing 21 gods have no storm/weather deity; existing comparisons cover pilgrimage/divination/goddesses/stone-cult but no weather/rainbow topic).

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English/Arabic names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/pre-islamic-arabian/gods/Dhu-al-Shara.md`, `stories/Marib大壩的崩潰傳說.md`, `comparisons/pre-islamic-pilgrimage-comparative.md`)
- No placeholders; real mythological scholarship (web-verified: Wikipedia "Quzah"; Lane's Lexicon entry قَوْسُ قُزَحَ; Ibn Ishaq Sīra on Muzdalifah; al-Azraqī Akhbār Makka; Fahd 1968; Kelley 2009 "Toward a new synthesis of the god of Edom and Yahweh"; Koran/NT rainbow-covenant parallels)
- Commit message: `mythos: enrich pre-islamic-arabian`; push to origin/master

---

### Task 1: Create Quzah God Page

**Files:**
- Create: `cultures/pre-islamic-arabian/gods/庫札Quzah.md`
- Modify: `cultures/pre-islamic-arabian/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Quzah scholarship (Wikipedia "Quzah": weather/mountain/rainbow god, worshiped by people of Muzdalifah, Ifada rite after September equinox facing his sanctuary; qaws Quzah = rainbow; Lane's Lexicon: rainbow colors red/yellow/green, tradition "Say not qaws Quzah for Quzah is a devil, but say qaws Allah"; Ibn Ishaq / al-Azraqī: fires lit on Jabal Quzah in sacred month, halt at hill of Quzah before sunrise, Qusai ibn Kilab fire-worship; Josephus/Qos identification; Kelley 2009 storm-god analysis)
- Produces: God page differentiated from existing Dhat-Badan (oasis-rain goddess) and Hubal (oracle): Quzah = Muzdalifah storm god, bow = rainbow, hailstones as arrows, consort of Manat in north, "bow of Allah" Islamic reformulation

- [ ] **Step 1: Create the god page** — 概述 (names: Quzah/قُزَح, qaws Quzah etymology, Muzdalifah cult) → 神格特徵 (weather/mountain/rainbow; hailstones as arrows; Ifada rite; fire rite on Jabal Quzah; Qos identification) → 神話事蹟 (storm-bow myth, Manat pairing, Islam's "qaws Allah" reform) → 跨文化對應 table (Indra/Indradhanush, Zeus, Thor, Baal-Hadad, Tishtrya, Hebrew covenant rainbow) → 相關神祇 → 文化遺產 → 參考文獻
- [ ] **Step 2: Add row to `cultures/pre-islamic-arabian/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present

### Task 2: Create Quzah's Bow Story Page

**Files:**
- Create: `cultures/pre-islamic-arabian/stories/庫札的弓與彩虹的傳說.md`
- Modify: `cultures/pre-islamic-arabian/stories/README.md` (add table row)

**Interfaces:**
- Consumes: rain-making (istisqa') rite context at Muzdalifah; Lane's Lexicon tradition replacing qaws Quzah with qaws Allah; Ibn Abbas' hadith that qaws Quzah "is a protection for the inhabitants of the earth from drowning" (rainbow as flood-guard → Noah covenant parallel); Hajj pre-Islamic fire rite at Muzdalifah
- Produces: Story page (故事背景 → 情節: pre-Islamic bow-in-sky belief, fires on Jabal Quzah, halt before sunrise, Ifada, rainbow as flood-guard vs Noah covenant → 跨文化平行 table: Norse Bifröst bridge / Greek Iris / Chinese 虹 dragon-serpent / Aboriginal Rainbow Serpent / biblical covenant / Yoruba Oshumare → 相關主題 → 參考文獻); must NOT duplicate existing stories (Marib dam flood, Hubal, three goddesses, pilgrimage)

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/pre-islamic-arabian/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Weather-God / Rainbow Comparative Page

**Files:**
- Create: `cultures/pre-islamic-arabian/comparisons/天氣神與彩虹之弓跨文化比較.md`
- Modify: `cultures/pre-islamic-arabian/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: storm-god scholarship (Quzah/قُزَح, Baal-Hadad, Zeus, Thor, Indra, Tishtrya; Fahd 1968; Kelley 2009; West 2007) + rainbow-myth scholarship (Lane Lexicon qaws Quzah; Bifröst/Iris/Oshumare/彩虹蛇; Noah covenant)
- Produces: 10-tradition comparison table + 4 structural analyses (rainbow as deity's bow/weapon; storm god as rain-giver = fertility; monotheistic re-sacralization of pagan symbol; weather god as mountain-top dweller) + 結論 + 參考文獻. Must be listed in comparisons/README.md (CI orphan check)

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/pre-islamic-arabian/comparisons/README.md`**
- [ ] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (append 庫札的弓與彩虹的傳說 to pre-islamic-arabian `stories`, `_stories` 11→12; append 庫札Quzah to `gods`; append 天氣神與彩虹之弓跨文化比較 to `comparisons`; add Quzah to `pantheon`), `_state.json` (append `pre-islamic-arabian` to `enrich_log`; `runs` 125→126), `cultures/pre-islamic-arabian/README.md` (counts 21/17/18 → 22/18/19)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich pre-islamic-arabian — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
