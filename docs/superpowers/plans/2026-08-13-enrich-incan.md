# Incan Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the incan culture by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** incan is the weakest culture at 59 pages (21 gods/19 stories/19 comparisons — fewest total; tied with pre-islamic-arabian which was enriched in the previous run). Existing incan content already covers Inti, Mama Quilla, Illapa (thunder), Urcaguary (rainbow), Apus, etc., and comparisons cover thunder-gods/rainbow-serpent/trickster-creators — but there is **no page for Catequil (卡特基爾)**, the Huamachuco thunder-ORACLE god whose myth is recorded in the 1560 Augustinian chronicle (*Relación de la religión y ritos del Perú*), no story about his oracle's destruction by Atahualpa (Sarmiento de Gamboa 1572), and no comparative study of thunderstone/lightning-stone cults (keraunia / 雷公斧 / gigi petir). Pick a single coherent topic cluster — **卡特基爾：雷電／神諭與雷石崇拜** — so the god page, story page and comparison page reinforce each other without overlapping existing pages.

**Tech Stack:** Markdown content files, git version control, `scripts/generate_stats.py` + `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English/Quechua/Spanish names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes cross-cultural parallels (comparison table)
- Each page includes `## 參考文獻` section with ≥1 citation (CI-clean; baseline error count must stay at 411)
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/incan/gods/Illapa.md`, `stories/會說話的羊駝與洪水.md`, `comparisons/thunder-gods-global.md`)
- No placeholders; real mythological scholarship (web-verified: Augustinian chronicle 1560; Sarmiento de Gamboa *Historia de los Incas* 1572; Topic & Topic Catequil archaeology; Brumm 2018 *Australian Archaeology* on gigi petir; Faraone 2014 *Kernos* on Greek keraunia; Merrifield 1987; Frazer *Golden Bough*; Cobo 1653)
- Commit message: `mythos: enrich incan`; push to origin/master

---

### Task 1: Create Catequil God Page

**Files:**
- Create: `cultures/incan/gods/Catequil.md`
- Modify: `cultures/incan/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Augustinian chronicle (Ataguju → Guamansuri → twin egg-birth of Catequil & Piguerao; slings; expulsion of Guachemines; people pulled from earth with gold/silver tools at Guacat hill; Mama Catequil); Cerro Ichal lightning-mountain shrine (Topic & Topic); Inca adoption (Quito→Cuzco, battle image, children sacrificed, twins-giver, day/tutelary god of good); oracle function; Atahualpa's destruction
- Produces: God page differentiated from existing Illapa page (Illapa = Cuzco official thunder; Catequil = northern provincial thunder + oracle + founding ancestor) with 跨文化對應 table (Thor/Zeus/雷公/Shango, Delphi Apollo for oracle, Dioscuri for twin-brother, Cuniraya Viracocha for disguised-creator motif)

- [x] **Step 1: Create the god page** — 概述 → 起源神話：雙生神卵 → 神話事蹟與職能 → 神諭與帝國的衝突 → 跨文化對應 table → 相關神祇 → 文化遺產 → 參考文獻
- [x] **Step 2: Add row to `cultures/incan/gods/README.md`**

### Task 2: Create Catequil Oracle / Atahualpa Story Page

**Files:**
- Create: `cultures/incan/stories/Catequil神諭與阿塔瓦爾帕的怒火.md`
- Modify: `cultures/incan/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Sarmiento de Gamboa (Atahualpa at Marcahuamachuco consults oracle → disaster prophecy → kills priest, chops stone idol's head with battle ax, razes temple); Wikipedia/Encyclopedia of the Incas; Augustinian re-interpretation (Catequil foretold the Christian army); parallel scholarship: Herodotus Croesus-Delphi, Daniel 5 Belshazzar, Caesar "Beware the Ides of March"
- Produces: Story page (故事背景 → 情節 four acts: 使者求問/帝王的怒火/神像的碎片/殖民者的補刀 → 跨文化平行 table: Croesus/Belshazzar/Caesar → 相關主題 → 參考文獻); must NOT duplicate existing incan stories (Ayar siblings, Inkarri, Manco Capac, Pachamama covenant, etc.)

- [x] **Step 1: Create the story page**
- [x] **Step 2: Add row to `cultures/incan/stories/README.md`**

### Task 3: Create Thunderstone / Lightning-Sacred-Object Comparative Page

**Files:**
- Create: `cultures/incan/comparisons/雷石與閃電聖物跨文化比較.md`
- Modify: `cultures/incan/comparisons/README.md` (add table row)

**Interfaces:**
- Consumes: Andean lightning cult (piedra del rayo, huaca, churi illapa, illa/mama/qunupa/llallawa fertility stones; Cobo/Arriaga/Urton 1981); keraunia/ceraunia scholarship (Faraone 2014; Pliny; Sotacus); Norse Thor-stones; Chinese 雷公斧/雷楔/霹靂砧 (《本草綱目》); Maya jade celt = Chaac's axe; North American Thunderbird stones; Albanian kokrra e rrufesë; Island SE Asia gigi petir (Brumm 2018); Japanese Raijin stones
- Produces: 9-culture comparison table + 4 structural analyses (誤認的考古學 / 以雷禦雷的交感巫術 / 雷擊者神選 vs 天譴 / 山巔到門檻的分層安置) + 結論 + 參考文獻. Must be listed in comparisons/README.md (CI orphan check)

- [x] **Step 1: Create the comparison page**
- [x] **Step 2: Add row to `cultures/incan/comparisons/README.md`**

### Task 4: Sync Metadata & Stats

**Files:**
- Modify: `_catalog.json` (append 卡特基爾神諭與阿塔瓦爾帕的怒火 to incan `stories`, `_stories` 3→4; append 卡特基爾Catequil to `pantheon`), `_state.json` (append `incan` to `enrich_log`; `runs` 126→127), `cultures/incan/README.md` (counts 10/7/7 → 21/19/19), README.md (incan row 20/18/18 → 21/19/19)

- [x] **Step 1:** Apply catalog/state/README edits
- [ ] **Step 2:** Run `python3 scripts/generate_stats.py` (updates README stats block, stats/index.md, SVGs)
- [ ] **Step 3:** Run `python3 scripts/ci_checks.py` — error count must be 411 (0 new), all new pages non-orphan

### Task 5: Commit & Push

- [ ] **Step 1:** `git add -A && git commit -m "mythos: enrich incan — ..."`
- [ ] **Step 2:** `git push origin master`
- [ ] **Step 3:** Report new content added
