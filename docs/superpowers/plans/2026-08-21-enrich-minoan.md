# Minoan Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the minoan culture — currently the weakest at 63 content pages (gods 23 + stories 20 + comparisons 20) — by adding 3 pages (1 god, 1 story, 1 comparison), each ≥300 繁體中文字 with cross-cultural parallels and cited references.

**Architecture:** Minoan coverage already includes Snake Goddess, Talos, labyrinth, bull-leaping, Thera eruption, peak sanctuaries and sacred caves. The unexplored coherent cluster is **米諾斯的儀式舞蹈與聲音護法 (ritual dance & apotropaic sound)**: the Kouretes (armed shield-dancers guarding infant Zeus) as god page; the Geranos crane dance (Theseus re-enacting the Labyrinth at Delos) as story page; and a global comparison of apotropaic armed/masked dance (Kouretes ↔ Corybantes ↔ Salii ↔ 中國儺 ↔ 日本神樂・追儺 ↔ 藏傳金剛舞). The three pages reinforce one another without overlapping existing pages (Kouretes appear only inside `stories/kouretes-zeus-birth-cave.md`; the Minos-death-in-Sicily tale is already fully covered by `stories/minos-spiral-shell.md`; Britomartis' net legend is covered by `gods/diktynna.md`).

**Tech Stack:** Markdown content files, git version control, `scripts/ci_checks.py` for verification.

## Global Constraints

- All content in Traditional Chinese (繁體中文), English names in parentheses
- Each page ≥300 characters of substantive content
- Each page includes a cross-cultural correspondence table
- Each page includes `## 參考文獻` section with ≥1 citation
- First heading must be h1; no heading-level jumps; no broken internal `.md` links
- Follow existing file formats (`cultures/minoan/gods/Talos.md`, `stories/minos-spiral-shell.md`, `comparisons/labyrinth-spiral-comparative.md`)
- No placeholders; real mythological scholarship (web-verified: Diodorus Siculus 5.65; Strabo 10.3.11–12; Apollodorus *Bibliotheca* 1.1.6–1.5.1; Palaikastro Hymn of the Kouretes; Plutarch *Theseus* 21; Callimachus *Hymn to Delos* 307–315; Homer *Iliad* 18.590–606; Harrison "The Kouretes and Zeus Kouros" *BSA* 1909–10; Jeanmaire *Couroi et Courètes* 1939; Armstrong "The Crane Dance in East and West" *Antiquity* 1952; Hedreen "The Geranos Dance" *Hesperia* 2011; 《周禮·夏官·方相氏》; 《古事記》天岩戶段)
- Commit message: `mythos: enrich minoan`; push to origin/master
- CI baseline: `python3 scripts/ci_checks.py` must stay ✅ ALL CHECKS PASSED before and after

---

### Task 1: Create Kouretes God Page

**Files:**
- Create: `cultures/minoan/gods/kouretes.md`
- Modify: `cultures/minoan/gods/README.md` (add table row)

**Interfaces:**
- Consumes: Kouretes scholarship (Diodorus 5.65 inventors of weapons & pyrrhic war-dance; Strabo 10.3 armed dance dramatizing Zeus' birth; Apollodorus 1.1.6–1.5.1 spears-on-shields drowning the infant's cries; Palaikastro Hymn "greatest Kouros…leap for flocks, ships, cities"; Harrison's seer/magician/metal-worker reading; Vermeule's Arkalochori cave weapons link)
- Produces: God page for the armed shield-dancer daimones who guarded baby Zeus — complements (does not duplicate) `Minoan-Young-God.md` (Velchanos/Kouros himself), `Rhea-Kourotrophos.md`, and `stories/kouretes-zeus-birth-cave.md`

- [ ] **Step 1: Create the god page** — 概述 (name from κούρος "青年", bronze-armed daimones of Rhea's retinue, Cretan vs Aetolian homonyms) → 神話事蹟 (盾矛擊響護嬰宙斯騙過 Cronus；發明青銅武器與 Pyrrhic 戰舞；Palaikastro 頌歌的「跳躍」咒令與成年啟蒙) → 跨文化對應 table (Corybantes/Idaean Dactyls/Salii/方相氏/Ame-no-Uzume/金剛舞護法) → 相關神祇 → 出現在 → 參考文獻
- [ ] **Step 2: Add row to `cultures/minoan/gods/README.md`**
- [ ] **Step 3: Verify** — h1 first heading, ≥300 chars body, citation section present

### Task 2: Create Geranos Story Page

**Files:**
- Create: `cultures/minoan/stories/geranos-crane-dance.md`
- Modify: `cultures/minoan/stories/README.md` (add table row)

**Interfaces:**
- Consumes: Geranos scholarship (Plutarch *Theseus* 21 Delian crane dance around Keraton horn-altar imitating Labyrinth passages; Dicaearchus naming; Callimachus *Hymn to Delos* 307–315; Iliad 18.590–606 Daedalus' dancing-floor at Knossos for Ariadne; scholiasts on first mixed boys-girls dance; Armstrong's Europe-Asia-Malekula crane-dance pattern; Hedreen *Hesperia* 2011 François vase)
- Produces: Story page (故事背景 → 情節: escape → Delos landing → Aphrodite idol dedication → circling dance with rhythmic involutions → Keraton altar & games founding → 故事分析: dance as living map of the Labyrinth, victory commemoration, mixed-dance initiation → 跨文化平行 table → 相關主題 → 參考文獻); must NOT duplicate `theseus-minotaur.md` (the kill itself) or `labyrinth-spiral-comparative.md` (architecture focus)

- [ ] **Step 1: Create the story page**
- [ ] **Step 2: Add row to `cultures/minoan/stories/README.md`**
- [ ] **Step 3: Verify** (format/citation)

### Task 3: Create Apotropaic Armed-Dance Comparison Page

**Files:**
- Create: `cultures/minoan/comparisons/apotropaic-armed-dance-comparative.md`
- Modify: `cultures/minoan/comparisons/README.md` (add table row — REQUIRED by CI orphan check)

**Interfaces:**
- Consumes: comparative dance scholarship (Harrison *Prolegomena/Themis*; Burkert *Greek Religion*; Dionysius of Halicarnassus *Roman Antiquities* 2.70–71 on Salii; 《周禮》方相氏「執戈揚盾…索室驅疫」; 《古事記》天鈿女命岩戶神樂; 藏傳金剛舞 cham 文獻; Armstrong 1952)
- Produces: 7-tradition comparison table (米諾斯庫雷特斯/弗里吉亞科律班特斯/羅馬薩利祭司/中國儺/日本神樂與追儺/藏傳金剛舞/希臘起鶴之舞) + three structural modes (聲音作為驅邪武器；武裝舞蹈作為男性成年啟蒙；舞蹈作為宇宙秩序的重演) + 結語 + 參考文獻. Must be listed in comparisons/README.md (CI orphan check)

- [ ] **Step 1: Create the comparison page**
- [ ] **Step 2: Add row to `cultures/minoan/comparisons/README.md`**
- [ ] **Step 3: Verify** (format/citation/orphan index)

### Task 4: Verify, Commit, Push

- [ ] **Step 1: Run `python3 scripts/ci_checks.py`** — expect ✅ ALL CHECKS PASSED
- [ ] **Step 2: `git add -A && git commit -m "mythos: enrich minoan — Kouretes armed shield-dancers, geranos crane dance at Delos, apotropaic armed-dance comparison"`**
- [ ] **Step 3: `git push`**

## Self-Review

- Spec coverage: weakest culture identified (minoan 63 < next tier 64); priority list sumerian/mayan/persian/yoruba inapplicable (they are now the four deepest at 175–222 pages); 3 pages × ≥300 chars ✓; cross-cultural tables ✓; references ✓; commit+push format ✓
- Placeholder scan: none — all content specified above
- Consistency: filenames match README rows match commit message scope
