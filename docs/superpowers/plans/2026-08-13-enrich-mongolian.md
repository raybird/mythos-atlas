# Mongolian Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the mongolian culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** Four cultures are tied as weakest at 56 content pages (incan, mongolian, pre-islamic-arabian, tibetan). mongolian is a major world mythology whose current coverage (Tengri, Erlik, water-spirits, wolf-totem, shamanism, sun/moon gods) has **no wealth/fortune deity page, no wealth-punishment story, and no wealth-deity comparative study** — while Namsarai (財神) and the Karunbai (greedy-rich-man) tale are both extremely well documented. Pick a single coherent topic cluster — 蒙古財富與福佑 (Mongolian wealth & fortune) — so the god page, story page and comparison page reinforce each other without overlapping existing pages.

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/mongolian/gods/白老翁.md`, `stories/蒼狼白鹿傳說.md`, `comparisons/長生天與跨文化天神比較.md`)
- No placeholders; real mythological scholarship (web-verified: Encyclopedia of Buddhism Vaiśravaṇa; face-music.ch Namsrai tsam mask; Buryat Museum thangka corpus 18th–20th c.; Cambridge "Dordzhi-Tseren bagshi, a prayer to the god of wealth"; *Folk-Lore Journal* vol.3 (1885) "Folk-Lore in Mongolia" Karunbai tale; Qur'an Qarun/Korah parallel)
- Commit message: `mythos: enrich mongolian`; push to origin/master

---

### Task 1: Create Namsarai God Page

**Files:**
- Create: `cultures/mongolian/gods/南斯拉伊.md`
- Modify: `cultures/mongolian/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Vaiśravaṇa/Kubera/Jambhala scholarship (Encyclopedia of Buddhism; Wikipedia Vaiśravaṇa; face-music.ch Namsrai/Bisman tengri; Buryat thangka corpus at National Museum of Buryatia; Cambridge prayer manuscript)
- Produces: God page differentiated from existing 白老翁 (longevity) and Ot (fire) pages: Namsarai = Mongolian wealth god (Баян Намсрай Bayan Namsrai), Buddhist syncretism of Kubera→Vaiśravaṇa→rnam thos sras, seated on snow lion with mongoose spitting jewels, one of the arban khangal ten protectors, "Bain Namsrin Khural" wealth ritual

- [ ] **Step 1: Create the god page** — 概述 (names: Namsarai/Bayan Namsrai/Bisman tengri, etymology from Tibetan rnam thos sras "全聞之君") → 神話事蹟 (Kubera origin, wealth-giver & dharma-protector dual role, Tibetan Jambhala kinship, Kalmyk/Buryat wealth khural ritual) → 形象與象徵 (snow lion mount, mongoose vomiting jewels as wealth/dominion-over-nāga symbol, victory banner) → 跨文化對應 table (Kubera/Jambhala/毘沙門天/財神/惠比壽/Lakshmi) → 相關神祇 → 出現在 → 參考文獻
- [ ] **Step 2: Add row to `cultures/mongolian/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present

### Task 2: Create Karunbai Story Page

**Files:**
- Create: `cultures/mongolian/stories/卡倫拜與土撥鼠.md`
- Modify: `cultures/mongolian/stories/README.md` (add table row)

**Interfaces:**
- Consumes: *Folk-Lore Journal* vol. 3 (1885) "Folk-Lore in Mongolia" (Wikisource transcription, Tarbagatai Kirghis Djastaban tribe): the rich man Karun bai who refused alms and was turned into a marmot, crying "Amanbul" (farewell); cross-referenced with Qur'anic Qarun/Korah (wealth swallowed by earth)
- Produces: Story page (故事背景 → 情節: Karunbai's wealth, beggars refused, prayer to God, transformation, the marmot's cry "Anguit!"=Amanbul → 故事分析: wealth-ethics & etiological aetiology → 跨文化平行 table → 相關主題 → 參考文獻); must NOT duplicate the existing 蒼狼白鹿傳說 (origin) or 白老翁神話 (longevity)

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/mongolian/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Wealth & Greed-Punishment Comparison Page

**Files:**
- Create: `cultures/mongolian/comparisons/財神與貪婪懲戒跨文化比較.md`
- Modify: `cultures/mongolian/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: wealth-deity scholarship (Namsarai/Kubera/Jambhala/Vaiśravaṇa/財神趙公明/毘沙門天/惠比壽/大黑天/Lakshmi/Aje/Renenutet) + greed-punishment motif (Karunbai/Qarun-Korah/Midas/石崇)
- Produces: 9-10 tradition comparison table + 4 structural analyses (wealth as conditional divine gift; treasure-beast iconography; greed-punishment as etiological morality tale; Buddhist wealth-god diffusion chain Kubera→Vaiśravaṇa→Namsarai→Bishamonten) + 結論 + 參考文獻. Must be listed in comparisons/README.md (CI orphan check)

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/mongolian/comparisons/README.md`**
- [ ] **Step 3: Verify** (orphan check passes)

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (append 卡倫拜與土撥鼠 to mongolian `stories`, `_stories` 9→10; append 南斯拉伊 to `gods`; append 財神與貪婪懲戒跨文化比較 to `comparisons`; add 南斯拉伊 to `pantheon`), `_state.json` (append `mongolian` to `enrich_log`; `runs` 122→123), `cultures/mongolian/README.md` (counts 21/18/17 → 22/19/18)

- [ ] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich mongolian — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
