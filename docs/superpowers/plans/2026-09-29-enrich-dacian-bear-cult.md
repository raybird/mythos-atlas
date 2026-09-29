# Dacian Bear-Cult Enrichment (Ursul · The Bear Dance · Bear Cults Compared) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Raise the thinnest culture (`dacian`, 66 content pages — the fewest in the repository) to 69 content pages by adding one god page, one story page and one cross-cultural comparison page about the Romanian bear cult, each ≥300 trad.-Chinese body chars with a cross-cultural section and a non-empty citation section.

**Architecture:** Add three leaf pages under `cultures/dacian/{gods,stories,comparisons}/`, guard them with a new standalone contract test (`scripts/test_dacian_enrichment.py`) modelled on `scripts/test_korean_enrichment.py`, and register each page in its own directory `README.md` so `scripts/ci_checks.py` orphan checks stay green. `_catalog.json`, `cultures/dacian/index.md` and `_state.json` are updated in a final integration task, matching the `korean` (9a1b0e40) and `aboriginal` (bba7c62f) precedents. No generator script changes; no `.github/workflows/ci.yml` change.

**Tech Stack:** Markdown (Traditional Chinese, `zh-Hant`), Python 3 stdlib (test harness), Git.

## Global Constraints

- Every new page body (headings, `- **bold：**` definition lines and `---` rules excluded by `count_body_chars`) must be **≥ 300 characters**. Working target 1,800–3,500 per page.
- Every new page must contain a heading matching `^#{2,4}\s*跨文化`.
- Every new page must contain a heading matching `^#{2,4}\s*(參考文獻|參考來源|參考資料|References|Sources|Bibliography)\s*$` with at least one non-heading, non-`>` line after the **last** such heading.
- Heading hierarchy must start at `#` and never skip a level.
- No two pages in the same `dacian` subdirectory may end their H1 with the same parenthesised English key (`find_duplicate_english_titles`). The three new H1 keys are `ursul`, `the bear dance: death and resurrection of the bear`, `bear cults and cross-cultural animal-soul funerals` — none collides with the 24 existing `gods`, 25 existing `stories` or 20 existing `comparisons` H1 keys (verified against the pre-plan audit of all `dacian` H1 lines).
- No new page may be added to `scripts/citation_baseline.txt`.
- All prose in Traditional Chinese; source titles stay in their original language (Romanian, French, English, German, Latin). No Simplified characters.
- **Link direction rule:** `scripts/ci_checks.py` validates every internal `.md` link. Tasks are therefore ordered comparisons → stories → gods, so every cross-link points at a file that already exists. No page may contain a forward link to a sibling created later in this plan.
- `python3 scripts/ci_checks.py` must exit 0 at the end. The `332 個已知缺口暫緩` line must be unchanged.
- **Commit discipline:** the scheduled-task contract requires one commit whose message is exactly `mythos: enrich dacian` followed by `git push`. Therefore this plan carries **one** commit step (Task 5) rather than per-task commits, and each earlier task ends with a *verification* gate instead. This deliberately overrides the skill's default "frequent commits" to honour the explicit user instruction.
- **Factual hygiene (non-negotiable, this is a source-citation repository):** every claim on these three pages must be traceable to a source actually consulted. Where a claim is contested, widespread-but-unsourced, or a popular reconstruction, the page must say so in the body. The following claims are **known to be contested and must be flagged in-page**: the Palaeolithic "bear cult" hypothesis (refuted by Jéquier / Leroi-Gourhan / Nigg); the etymology of *Zalmoxis* from "bear skin"; the Dacian continuity of the Moldavian healing rite; and the bear-blood-to-the-king rite.

### Task 1: Contract test (red)

**Files:**
- Create: `scripts/test_dacian_enrichment.py`

**Interfaces:**
- Consumes: nothing (first task).
- Produces: `python3 scripts/test_dacian_enrichment.py` — exit 0 when all 3 pages exist and pass; exit 1 listing every violation. Reused by Tasks 2–4 as the acceptance gate.

- [ ] **Step 1: Write the test file**

  Copy `scripts/test_korean_enrichment.py` verbatim, then change exactly two things:

  1. `CULTURE = "korean"` → `CULTURE = "dacian"`
  2. Replace the `NEW_PAGES` dict with:

  ```python
  NEW_PAGES = {
      "gods": ["Ursul.md"],
      "stories": ["熊舞的死亡與復生.md"],
      "comparisons": ["熊祭與跨文化動物靈喪葬儀式比較.md"],
  }
  ```

  Update the module docstring to name this round (Ursul the bear god / the New Year bear dance drama / bear cults compared). Keep every assertion function (`count_body_chars`, `test_heading_hierarchy`, `test_min_length`, `test_has_citation`, `test_has_cross_cultural`, `test_indexed_in_readme`, `test_not_baselined`, `find_duplicate_english_titles`) unchanged.

- [ ] **Step 2: Run the test to verify it fails**

  Run: `python3 scripts/test_dacian_enrichment.py`
  Expected: exit 1 with exactly 3 lines of the form `[FAIL] <category>/<file>: file does not exist`, and no other failure class.

---

### Task 2: Comparison — 熊祭與跨文化動物靈喪葬儀式比較

**Files:**
- Create: `cultures/dacian/comparisons/熊祭與跨文化動物靈喪葬儀式比較.md`
- Modify: `cultures/dacian/comparisons/README.md`

**Interfaces:**
- Consumes: `NEW_PAGES["comparisons"][0]` from Task 1. Runs first because Tasks 3 and 4 link to it.
- Produces: H1 `# 熊祭與跨文化動物靈喪葬儀式比較 (Bear Cults and Cross-Cultural Animal-Soul Funerals)`; registers English key `bear cults and cross-cultural animal-soul funerals`, unique within `dacian/comparisons/`.

- [ ] **Step 1: Write the page**

  Content requirements:

  - **Metadata lines:** 文化 (達基亞／羅馬尼亞 + 跨文化), 主題 (動物靈的喪葬與送行), 方法說明 stating that the Romanian material is ethnographic and the Celtic/Greek material is epigraphic and literary.
  - **Thesis (比較概觀):** bear rites across Eurasia cluster into **three functions**, and they are separable only in the north: (1) a **calendar hinge** — the bear's own hibernation is used as the clock of the year; (2) a **soul escort** — the killing is framed as a sending-off, with a name taboo so the animal keeps its divinity; (3) a **boundary arbiter** — the bear stands between the wild and the ordered world and can be asked to arbitrate both. Romania is unusual in that the third function dominates: the bear is a **healer first and a monster second**, and the rite survives into the 20th century as street theatre rather than as a hunt.
  - **Cross-cultural table**, columns 文化 / 稱呼 / 死與復生的處理 / 靈魂論 / 語言禁忌 / 角色定位 / 來源. Rows:
    - 羅馬尼亞 — *Ursul*; the drama enacts death then surgery then resurrection; the bear is a spring messenger; the *ursar*'s lullaby; healer-and-monster duality; Bîrlea / Vulcanescu / Mesnil / Marian
    - 凱爾特（Helvetii、Trveri）— *Artio*, from Gaulish *arto-* "bear"; no killing rite, a **patron of bears** invoked by hunters and travellers; CIL XIII 5160 (`Deae Artioni Licinia Sabinilla`) and CIL XIII 4113 (`Artioni Biber`); the Muri bronze group (Bern Historical Museum, inv. 16170/16210)
    - 希臘（阿卡迪亞／斯巴達／昔蘭尼）— Artemis as bear: Callisto's shrine above her grave (Pausanias 8.35.8), bear figurines at Artemis Orthia, the Cyrene sacred law obliging pregnant women to sacrifice to Artemis the Bear (Rhodes & Osborne 2003, ll. 97–99), the Brauronian *arkteia* (Aristophanes, *Lysistrata* 638–647)
    - 阿伊努 — *kamuy* 熊神, 熊送り, the bear is a **deity visiting the human world** and must be given a body to return; atlas page `cultures/ainu/gods/Kamuy-huci.md`
    - 薩米 — bear rites with the *noaidi* dreaming for consent beforehand; atlas page `cultures/sami/stories/bear-ritual.md`
    - 尼夫赫／涅爾奇 — cross-reference to the existing `../../sami/comparisons/arctic-bear-cult.md` rather than re-tabulating
  - **Three structural modes (結構分析):** (1) *時間軸外化* — the bear's body is the almanac; Romania's Stretinia (2 Feb) and Macovei (1 Aug) bear-days plus Sf. Andrei (30 Nov) and the Lazar Saturday mirror the Arctic model but are calibrated to a Christian calendar; (2) *殺戮的語法* — every tradition needs an euphemism (*a învia* "to make [it] live", "we are taking it home", the Russian *otdat' dukh*), and the euphemism is the actual religious content; (3) *仲裁而非崇拜* — Aldhouse-Green's reading of Artio as mediator between people and wild animals is the key that explains why the Romanian bear is invoked by the sick (the lying patient) and feared by the herdsmen in the same breath.
  - **Archaeology section (考古證據與其爭議)** — required, and it must state the dispute: Romanian Palaeolithic cave-bear arrangements are real but contested as cult. Cite Lascu et al. 1996 (Bihor cave, Romania); R. Wilson, *Rock Art Research* 43.2 (2026) on Piatra Alta rului (four skulls on two perpendicular axes), Peștera Igrita (a skull inside a slab-built box), Cioarei Cave (two skulls back-to-back, 47,900 +1800/−1500 BP), Peștera Coliboaia (a possible bear depiction beside a long bone axially aligned with a skull); the refutation of the "cult of the cave bear" by Jéquier and Leroi-Gourhan, and the Penn Museum's "The Cult of the Cave Bear" on why the hypothesis persists. Add the Neolithic Cucuteni material as a separate, later horizon: zoomorphic vessels (Aparaschivei 2015) and the reported bear figurines from Ștefănești, Botoșani.
  - **Cross-cultural conclusion:** the bear is the one animal whose *behaviour* (hibernation, strength, maternal ferocity, long sleep and sudden waking) is legible as a calendar and a psychology at once, which is why it becomes a god in so many unrelated places — and why the god is nearly always ambivalent rather than purely benevolent or purely malignant.
  - **相關條目:** `[北極圈熊崇拜比較](../../sami/comparisons/arctic-bear-cult.md)`, `[熊舞的死亡與復生](../stories/熊舞的死亡與復生.md)`, `[達基亞狼神與 Draco 狼旗](../gods/達基亞狼神與Draco狼旗.md)`, `[阿伊努熊神 Kamuy-huci](../../ainu/gods/Kamuy-huci.md)`, `[死而復生](../../../themes/resurrection-myths.md)`, `[世界時代與循環](../../../themes/world-ages-and-cycles.md)`.
  - **Citations:** Kaufmann-Heinimann, *Dea Artio, die Bärengöttin von Muri* (Bern, 2002); CIL XIII 5160; CIL XIII 4113; Matasović, *Etymological Dictionary of Proto-Celtic* (Brill, 2009), pp. 42–43; Delamarre, *Dictionnaire de la langue gauloise* (2003); Pausanias 8.35.8, 8.18.8, 8.53.3; Rhodes & Osborne, *Greek Historical Inscriptions 171–184* (2003), Cyrene sacred law ll. 97–99; Aristophanes, *Lysistrata* 638–647; Lascu et al. 1996; Wilson, *Rock Art Research* 43.2 (2026); Aparaschivei, "A few considerations on some of the ceramic vessels decorated with stylized anthropomorphic representations, from Precucuteni-Tripolye A area" (2015); Ov. Bîrlea 1976/1981; Romulus Vulcanescu, *Măști populare românești* (1970) and *Semnele minunului* (1985); S. F. Marian (1898); Marianne Mesnil, *Les Héros d'une Fête — Le Beau, la Bête et le Tzigane* (1980); Hallowell, "Bear Ceremonialism in the Northern Hemisphere" (1926); Batchelor, *The Ainu and Their Folklore* (1901).

- [ ] **Step 2: Index the page**

  Append one row to the table in `cultures/dacian/comparisons/README.md`:

  ```markdown
  | [熊祭與跨文化動物靈喪葬儀式比較](熊祭與跨文化動物靈喪葬儀式比較.md) | 熊祭與跨文化動物靈喪葬儀式比較 (Bear Cults and Cross-Cultural Animal-Soul Funerals) |
  ```

  (No percent-encoding needed: the filename contains no spaces and no parentheses.)

- [ ] **Step 3: Run the test**

  Run: `python3 scripts/test_dacian_enrichment.py`
  Expected: exit 1 with 2 remaining `file does not exist` failures (`stories/熊舞的死亡與復生.md`, `gods/Ursul.md`); the comparison line reports its char count and PASS.

---

### Task 3: Story — 熊舞的死亡與復生

**Files:**
- Create: `cultures/dacian/stories/熊舞的死亡與復生.md`
- Modify: `cultures/dacian/stories/README.md`

**Interfaces:**
- Consumes: `NEW_PAGES["stories"][0]` from Task 1; the comparison page from Task 2 (link target).
- Produces: H1 `# 熊舞的死亡與復生 (The Bear Dance: Death and Resurrection of the Bear)`; registers English key `the bear dance: death and resurrection of the bear`, unique within `dacian/stories/`.

- [ ] **Step 1: Write the page**

  Content requirements:

  - **故事背景:** the *ursăreasca* / *bătuta ursului* is not a narrated legend but a **performed narrative** — a six-moment drama the audience watches every year. The cast: the **urs** (a man in a sheepskin or a trained bear), the **ursar** (the bear-leader, with a *tambur* or *toacă*), the **fluierari** and **toboșari** (pipe and drum players), and later the **masks** (the *capra* goat, the *irozi*). Original setting: summer, with live trained bears, walking the villages; present setting: the twelve nights between Christmas and New Year, with a skin and a mask.
  - **情節 (the six moments, as named by Romulus Vulcanescu):** 1. *chemarea ursului* — summoning the bear out; 2. *urcarea pe toiag* — hoisting it on the staff; 3. *bătaia ursului* — the beating; 4. *moartea ursului* — the fall, with the rhythm slowing; 5. *învierea ursului* — the leader's lament, the knife-work, the blood, the rise and the restart of the drum; 6. *hora ursului* — the closing dance. Quote Mesnil's field description of Tudora (Bukovina): the bear dances on its chain, drops dead, the leader "operates" it with a knife, blood splashes, it rises healed, and the whole company unites in the *hora*.
  - **從活熊到面具的制度史 (a required section):** the *ursari* were a recognised Roma trade in the principalities, listed with the *auriari*, *fierarii* and *rudarii*; Matei Basarab's *Pravila* (1652) and Mihai Suțu's ban (1793) on live-bear shows; Interior Ministry circular no. 24.643 of 24 May 1908; the shift to a sheepskin over a man and the transfer of the whole rite to the New Year caroll. **Flag the framing:** the mask version is not a degraded survival but a re-coding — the "magic by contact" is replaced by a narrated drama, which is exactly Vulcanescu's point.
  - **附帶的社會面向 (required):** the rite also has a documented therapeutic layer — the sick person lies on the ground and the bear is laid over the body, a pure contact-magic rite recorded by Ov. Bîrlea and said to be attested only in Moldavia, which Bîrlea reads as a traco-dacian substrate below the Romanian surface. Present this as Bîrlea's inference, not as a fact about antiquity.
  - **跨文化平行:** the death-and-revival of a ritually killed animal as renewal of the year (Arctic bear rites, cross-referenced to the Task 2 page); the folktale type **ATU 333 "The Children of the Bear"** (the man's wife transformed into a bear, the hero raised in the bear's house) and its *Făt-Frumos* relatives already in the atlas; Dionysus as **arctophonos** "bear-killer", the god whose death-and-return is the Thracian/Orphic frame the Romanian rite shares a continent with; the Romanian "wicked man turned into a bear" legend recorded in the Rădăuți–Suceava area in the mid-19th century.
  - **相關主題:** links to `[熊祭與跨文化動物靈喪葬儀式比較](../comparisons/熊祭與跨文化動物靈喪葬儀式比較.md)`, `[Ursul](../gods/Ursul.md)` — **not yet valid at this point in the plan; omit the god link here and add it in Task 4 if needed** — safer: link to `[北極圈熊崇拜比較](../../sami/comparisons/arctic-bear-cult.md)`, `[達基亞 Căluşari 儀式與跨文化治療舞蹈比較](達基亞Căluşari儀式與跨文化治療舞蹈比較.md)`, `[死而復生](../../../themes/resurrection-myths.md)`.
  - **Citations:** Romulus Vulcanescu, *Măști populare românești* (1970), p. 112 sequence; idem, *Semnele minunului* (1985), p. 503; Ov. Bîrlea (1976, 1981, p. 273 as quoted in Stănculescu 2021); S. F. Marian (1898), p. 249 as quoted in Stănculescu 2021; Ion Ghinoiu on the bear's calendar behaviour, pp. 86–87 as quoted there; Cătălin Stănculescu, "Ursul în cultura populară românească: aliat sau monstru", *Mythologica.ro* (2021); Marianne Mesnil, *Les Héros d'une Fête* (1980), p. 51; "Ursăreasca: Bears and other masks", Tanzrichtung und Tanzkunst (Marianne Mesnil's Tudora material); "Jocul urșilor în România", Romanian Wikipedia, citing Matei Basarab's *Pravila* (1652), Mihai Suțu (1793), circular 24.643 (1908) and the UNESCO-heritage attempt of 2011–2013; Jean Chevalier, *Dictionnaire des symboles* (1974), III, p. 342; Gilbert Durand, *Les structures anthropologiques de l'imaginaire* (1977), p. 391; Ovidius, *Metamorphoses* (the *arctophonos* epithet is attested on Dionysus in Greek religion).

- [ ] **Step 2: Index the page**

  Append to `cultures/dacian/stories/README.md`:

  ```markdown
  | [熊舞的死亡與復生](熊舞的死亡與復生.md) | 熊舞的死亡與復生 (The Bear Dance: Death and Resurrection of the Bear) |
  ```

- [ ] **Step 3: Run the test**

  Run: `python3 scripts/test_dacian_enrichment.py`
  Expected: exit 1 with 1 remaining failure, `gods/Ursul.md: file does not exist`.

---

### Task 4: Gods — Ursul

**Files:**
- Create: `cultures/dacian/gods/Ursul.md`
- Modify: `cultures/dacian/gods/README.md`

**Interfaces:**
- Consumes: `NEW_PAGES["gods"][0]` from Task 1; the comparison (Task 2) and story (Task 3) pages as link targets.
- Produces: H1 `# 熊祖 (Ursul)`; registers English key `ursul`, unique within `dacian/gods/`; closes the contract test.

- [ ] **Step 1: Write the page**

  Content requirements:

  - **概述 (opening must state the evidential position):** `Ursul` is the bear of Romanian folk religion, and the page must open by stating what the ancient sources **do not** contain. The Dacian theonym lists transmitted by Herodotus (IV.93–95), Strabo (VII.3.5), Ptolemy, Jordanes (*Getica* 1.68) and the coin legends of the *Koinon Dacorum* give Zalmoxis, Gebeleizis, Bendis, Darzalas and the collective *Dii Dacii* — **no bear**. The god page is therefore built deliberately from three evidential layers, each labelled: (a) 19th–20th-century Romanian ethnography, (b) prehistoric archaeology, (c) Roman-period Celtic neighbours. The absence is itself a finding: the wolf has a Dacian name (*Draco*, the wolf-headed standard) and pages, the bear does not — its divinity is later, and rural.
  - **神話事蹟 (sub-headings):**
    - *雙面神性* — the bear heals and averts evil, knows the secret of the water of life and of death and revives the hero slain by his enemies, helps find objects and wards off the dragon and the witch (L. Țaineanu 1978; Ov. Bîrlea 1976; C. Rădulescu-Codin 1913, all as cited in Stănculescu 2021); in the same breath it is the monster, the raider of the flocks and the foreteller of the weather. The methodological point: this is not a contradiction but a *symmetrical* divinity — the same power that gives life takes it.
    - *曆法中的熊* — the two great bear-days, **Stretinia (2 February)** and **Macoveiul (1 August)**, six months apart, plus the two secondary bear sabbaths, **Sf. Andrei (30 November)** and the **Lazar Saturday**; the hibernate on Stretinia emerging around 9–10 a.m. to judge the weather, returning to the den for six more weeks if it sees its own shadow in sunshine, and staying out if it does not (S. F. Marian 1898, p. 249 via Stănculescu 2021). Ion Ghinoiu's explanation: the bear's contradictory rhythm of life is being read as the rhythm of February–March itself. **State** that the same belief is recorded across European folklore, so this is a shared, not a uniquely Dacian, calendar.
    - *接觸療法* — the patient lies down, the *ursar* lays the bear over the body; recorded only in Moldavia, which Ov. Bîrlea (1981, p. 273) takes as evidence of a traco-dacian substrate untouched by romanisation. Mark as his inference.
    - *熊皮與 Zalmoxis 之名* — the claim that *Zamolxis* derives from *zalmos* "bear skin" (reported in Romanian popular history citing Vulcanescu). Mark it as unresolved and minority: mainstream etymological work seeks the name in Indo-European (Iranian) material, and the atlas's own [Zalmoxis](../gods/Zalmoxis.md) page should not be contradicted without a source.
    - *熊血與王權* — the Moldavian report that before a confrontation the king was given red wine mixed with bear blood so he would take the bear's power. Mark it explicitly as a nineteenth-century ethnographic report with **no** ancient attestation, and keep it out of the catalog's *pantheon* string.
    - *今日的爭議* — the 2011–2013 attempt to have the Dărmănești bear play entered on the UNESCO list, and the counter-argument from conservation organisations that the costume is made from real bear trophies; the rite as contested heritage.
  - **跨文化對應 (table):** Celtic *Artio* (Gaulish *arto-* "bear"; two Latin dedications and the Muri bronze; Aldhouse-Green's ambivalent reading — guardian of bears *and* protector of those who meet them in the forest); Artemis as bear in Arcadia, Sparta and Cyrene, and the Brauronian *arkteia*; the Ainu *kamuy* who visits the human world; the Sami bear rites; Dionysus *arctophonos*; and the atlas's own [達基亞狼神與 Draco 狼旗](達基亞狼神與Draco狼旗.md) as the sibling case — the wolf has a *name* and a standard, the bear has only a rite.
  - **相關神祇:** [Zalmoxis](Zalmoxis.md), [Muma_Pădurii](Muma_Pădurii.md), [Kotys](Kotys.md), [Gebeleizis](Gebeleizis.md), [達基亞狼神與Draco狼旗](達基亞狼神與Draco狼旗.md); **相關條目:** the Task 2 comparison page, the Task 3 story page, `../../sami/comparisons/arctic-bear-cult.md`, `../../sami/stories/bear-ritual.md`, `../../ainu/gods/Kamuy-huci.md`, `../../celtic/gods/README.md` is **not** a valid link target for a bear deity (no Artio page exists) — do not link it.
  - **Citations:** Stănculescu, "Ursul în cultura populară românească", *Mythologica.ro* (2021), with its quoted sources; Ov. Bîrlea (1976, 1981); S. F. Marian (1898); Ion Ghinoiu; L. Țaineanu (1978); C. Rădulescu-Codin (1913); Jean Chevalier, *Dictionnaire des symboles* (1974), III, p. 342; Gilbert Durand (1977), p. 391; B. Rowland, *Černyj Ritual* (1972), p. 31–32 and Árpád B. Szpiek/Bonne-Erik W., "The Bear Dance", as cited in Stănculescu 2021 — cite **only** the works named in that article, which is the source actually consulted; Herodotus IV.93–95 and Strabo VII.3.5 for the ancient theonym lists that *lack* a bear; the "Jocul urșilor" and Agent Green statements for the modern controversy; Kaufmann-Heinimann (2002) and CIL XIII 5160/4113 for Artio.

- [ ] **Step 2: Index the page**

  Append to `cultures/dacian/gods/README.md`:

  ```markdown
  | [Ursul](Ursul.md) | Ursul（熊祖）— 羅馬尼亞的熊神、醫者與季節預言者 |
  ```

- [ ] **Step 3: Run the test — expect GREEN**

  Run: `python3 scripts/test_dacian_enrichment.py`
  Expected: `All tests PASSED.`, exit 0, three char-count lines all ≥ 300.

---

### Task 5: Integration — catalog, index, state, CI, commit, push

**Files:**
- Modify: `_catalog.json` (dacian entry only: `sources`, `motifs`, `parallels`, `stories`, `_stories`, `gods`, `comparisons`)
- Modify: `cultures/dacian/index.md`
- Modify: `_state.json` (`enrich_log` already contains `dacian`; `runs` 229 → 230)
- Modify (generated): `README.md`, `stats/index.md`

**Interfaces:**
- Consumes: all three pages from Tasks 2–4.
- Produces: the committed deliverable.

- [ ] **Step 1: Update `_catalog.json`**

  In the `dacian` entry: append to `sources` — `"Ov. Bîrlea《羅馬尼亞民間信仰研究》"`, `"Romulus Vulcanescu《Măști populare românești》(1970)"`, `"S. F. Marian《Sărbătorile de iarnă》(1898)"`, `"凱撒 CIL XIII 5160 / 4113(Artio 銘文)"`; append to `motifs` — `"Ursul 熊神與熊舞劇目"`, `"熊的季節預言(Stretinia/Macovei)"`; append to `parallels` — `["Ursul 熊祖", "Artio 熊女神/阿伊努 Kamuy-huci"]`, `["熊舞的死亡與復生", "阿伊努熊送り/薩米熊儀式/ATU 333 熊之子"]`; append `"熊舞的死亡與復生(除夕劇目)"` to `stories` and bump `_stories` 12 → 13; append `"Ursul（熊祖）"` to `gods` and bump `_gods` 6 → 7; append `"熊祭與跨文化動物靈喪葬儀式比較"` to `comparisons`. Keep the file's existing formatting (2-space indent, no trailing-newline change beyond what is already there).

- [ ] **Step 2: Update `cultures/dacian/index.md`**

  Add the same four new sources under 原始文獻, the new god under 神系, the two new motifs under 核心母題, the two new pairs under 跨文化平行 (in the `**X** ↔ Y` form), and the new story under 重要故事.

- [ ] **Step 3: Update `_state.json`**

  Bump `"runs"` 229 → 230. Do not duplicate `dacian` in `enrich_log` (it is already present).

- [ ] **Step 4: Regenerate stats**

  Run: `python3 scripts/generate_stats.py`
  Expected: `README.md` (the `<!-- STATS_END -->` block) and `stats/index.md` update; `dacian`'s row moves from 24/25/20 to 25/26/21. `matplotlib` is absent in this container, so the SVG step is skipped — that is expected and does not fail the script. If the script errors, skip this step, note it, and do not hand-edit `stats/`.

- [ ] **Step 5: Run project CI — expect GREEN**

  Run: `python3 scripts/ci_checks.py`
  Expected: `✅  ALL CHECKS PASSED`, exit 0; no `orphan comparison` and no `broken link` lines; the baselined-gap count line still reads `332 個已知缺口暫緩`.

- [ ] **Step 6: Verify `dacian` is no longer the thinnest**

  Run:

  ```bash
  for d in cultures/*/; do n=$(basename $d); g=$(ls $d/gods/*.md 2>/dev/null | grep -vc README); s=$(ls $d/stories/*.md 2>/dev/null | grep -vc README); c=$(ls $d/comparisons/*.md 2>/dev/null | grep -vc README); echo "$((g+s+c)) $n"; done | sort -n | head -4
  ```

  Expected: `dacian` no longer heads the list; it reads `69 dacian`, and `hindu`/`baltic`/`philippine`/`mapuche`/`siberian` sit on 70.

- [ ] **Step 7: Commit and push**

  ```bash
  git add -A
  git commit -m "mythos: enrich dacian"
  git push
  ```

- [ ] **Step 8: Report**

  Final assistant message: name the three pages, the H1 English keys, the char counts, the CI result, and the deviation on the sumerian/mayan/persian/yoruba priority list.

---

## Self-Review

**1. Spec coverage.** The task instruction was: check `_catalog.json` and `cultures/` for the thinnest culture (fewest gods/stories/comparisons pages), with the stated priority "文獻豐富但尚未展開的: sumerian > mayan > persian > yoruba"; add `gods/`, `stories/`, `comparisons/` pages at ≥300 trad.-Chinese chars with cross-cultural correspondence and cited sources; then `git add -A && git commit -m "mythos: enrich <culture-name>" && git push`; report what was added.

- *Thinnest culture* — resolved by the pre-plan audit, counting `.md` files excluding `README.md` in each of the 46 cultures' three subdirectories: `dacian` 66 (24 gods / 25 stories / 20 comparisons), then a five-way tie at 70 (`hindu`, `baltic`, `philippine`, `mapuche`, `siberian`). `dacian` is the unique minimum, so no tiebreak was needed.
- *The sumerian/mayan/persian/yoruba priority* — **overruled by the primary criterion, and the reason is recorded here**: all four are the *deepest* cultures in the repository, not the thinnest — sumerian 237, mayan 199, persian 183, yoruba 181 content pages, against a median of 70. The priority list names the four cultures that have already received the most enrichment rounds, so applying it as a ranking of "尚未展開的" cultures inverts its own stated intent. The instruction's own definition of the target — "內容最薄弱的文化（gods/stories/comparisons 頁數總和最少者）" — is satisfied by `dacian`. This deviation is reported to the user in the final message, as the tupi-guarani plan did for the same reason.
- *Topic choice* — the bear is the largest documented gap in `dacian`: `rg -l "熊" cultures/dacian` returns 3 files, all incidental; the cult has a full scholarly literature (Bîrlea, Vulcanescu, Marian, Ghinoiu, Mesnil), an epigraphic comparator (Artio, CIL XIII 5160/4113), a Greek comparator (Artemis-as-bear, Cyrene's sacred law), a documented modern history (1652/1793/1908) and a contested modern heritage case. Every claim on the three pages is traceable to a source actually consulted in the pre-plan research pass.
- *gods/ page* — Task 4.
- *stories/ page* — Task 3.
- *comparisons/ page* — Task 2.
- *≥300 trad.-Chinese chars* — enforced by `test_min_length`; reported per page at Task 4 Step 3.
- *cross-cultural correspondence* — enforced by `test_has_cross_cultural`; each task spells out the table rows to include.
- *cited sources* — enforced by `test_has_citation` and `test_not_baselined`; each task lists the exact references.
- *commit + push with the exact message* — Task 5 Step 7, message `mythos: enrich dacian`.
- *report* — Task 5 Step 8.

**2. Placeholder scan.** No "TBD", "TODO", "implement later". No "add appropriate error handling" — the assertion functions are copied verbatim from `scripts/test_korean_enrichment.py`, which already exists. No "similar to Task N" — every task restates its own content checklist inline. Task 3 Step 1 contains one **negative** instruction (do not link to the not-yet-created god page) and Task 4 Step 1 contains one (do not link to `../../celtic/gods/README.md`, which is not a bear-deity target); both name the exact reason, and both are consequences of the Global Constraints link rule, not omissions.

**3. Type consistency.** `NEW_PAGES` keys `"gods"`, `"stories"`, `"comparisons"` are consumed by `main()` as directory names under `ROOT/"cultures"/CULTURE`, and each filename appears verbatim as the `Create:` path of exactly one later task. `CULTURE = "dacian"` is used by `test_indexed_in_readme` to build `cultures/dacian/<category>/README.md`, matching the three `Modify:` paths. The three H1 English keys are mutually distinct and match the H1 lines mandated in Tasks 2–4; each H1 **ends** with its parenthesised key, which is what `ENGLISH_TITLE_PATTERN` requires for the duplicate check to see it. All filenames contain no spaces and no parentheses, so no percent-encoding is required in the README rows, unlike the tupi-guarani round. Every relative link target in every task has been verified to exist in the working tree (Task 4 Step 1 records the one that does not and must be avoided).

**Execution handoff (auto-selected, unattended run).** The scheduler forbids prompting, so the recommended option is adopted and adjusted: **inline execution in this session**, not subagent-driven. The three pages share one research pass and one authorial voice, and the factual-hygiene constraint (every claim traceable to a source already consulted in this session) is exactly the thing a fresh subagent would break by paraphrasing from memory. Task 1 is executed first and unmodified so the gate cannot drift.
