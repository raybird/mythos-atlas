# Slavic Mythology Enrichment (Lel/Polel · Rugiaevit · Igor's Campaign · Funeral Laments · Many-Faced Gods) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Raise the thinnest culture (`slavic`, 66 content pages / 297 kB — lowest page count *and* lowest total byte volume of all 46 cultures) to 71 content pages by adding 2 gods, 2 stories and 1 cross-cultural comparison page, each ≥300 trad.-Chinese body chars with a cross-cultural section and a non-empty citation section.

**Architecture:** Add five leaf pages under `cultures/slavic/{gods,stories,comparisons}/`, guard them with a new standalone contract test (`scripts/test_slavic_enrichment.py`) modelled on the existing `scripts/test_polynesian_enrichment.py`, and register each page in its own directory `README.md` index so `scripts/ci_checks.py` orphan checks stay green. No change to `_catalog.json` (it carries no per-page listing for these), no change to generator scripts.

**Tech Stack:** Markdown (Traditional Chinese, `zh-Hant`), Python 3 stdlib (test harness), Git.

## Global Constraints

- Every new page body (headings, `- **bold：**` definition lines and `---` rules excluded by `count_body_chars`) must be **≥ 300 characters**.
- Every new page must contain a heading matching `^#{2,4}\s*跨文化` (a cross-cultural section).
- Every new page must contain a heading matching `^#{2,4}\s*(參考文獻|參考來源|參考資料|References|Sources|Bibliography)\s*$` with at least one non-heading, non-`>` line after the **last** such heading.
- Heading hierarchy must start at `#` (level 1) and never skip a level.
- No two pages in the same `slavic` subdirectory may end their H1 with the same parenthesised English key (test `find_duplicate_english_titles`).
- No new page may be added to `scripts/citation_baseline.txt`.
- All prose in Traditional Chinese. No Simplified characters.
- `python3 scripts/ci_checks.py` must exit 0 after every task that touches `cultures/`.

---

### Task 1: Contract test (red)

**Files:**
- Create: `scripts/test_slavic_enrichment.py`

**Interfaces:**
- Consumes: nothing (first task).
- Produces: `python3 scripts/test_slavic_enrichment.py` — exit 0 when all 5 pages exist and pass; exit 1 listing every violation. Reused by Tasks 2–6 as the acceptance gate.

- [ ] **Step 1: Write the test file**

Copy `scripts/test_polynesian_enrichment.py` verbatim, then change exactly three things:

1. `CULTURE = "polynesian"` → `CULTURE = "slavic"`
2. Replace the `NEW_PAGES` dict with:

```python
NEW_PAGES = {
    "gods": [
        "萊爾與波萊爾.md",
        "魯格耶維特、波列維特與波列努特.md",
    ],
    "stories": [
        "伊戈爾之歌.md",
        "羅斯的喪葬哭喪.md",
    ],
    "comparisons": [
        "多面之神與複數的神.md",
    ],
}
```

3. Update the module docstring to name this round (Tangaloa/Makemake → Lel and Polel / Rugiaevit / The Tale of Igor's Campaign / Russian funeral laments / many-faced gods).

Keep every assertion function (`count_body_chars`, `test_heading_hierarchy`, `test_min_length`, `test_has_citation`, `test_has_cross_cultural`, `test_indexed_in_readme`, `test_not_baselined`, `find_duplicate_english_titles`) unchanged.

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 scripts/test_slavic_enrichment.py`
Expected: exit 1 with 5 lines of the form `[FAIL] gods/萊爾與波萊爾.md: file does not exist` — one per new page, and no other failure class.

- [ ] **Step 3: Commit the red test**

```bash
git add scripts/test_slavic_enrichment.py
git commit -m "test: add slavic lel/polel + rugiaevit enrichment contract test (red)"
```

---

### Task 2: Gods — 萊爾與波萊爾 (Lel and Polel)

**Files:**
- Create: `cultures/slavic/gods/萊爾與波萊爾.md`
- Modify: `cultures/slavic/gods/README.md`

**Interfaces:**
- Consumes: the `NEW_PAGES["gods"][0]` entry from Task 1.
- Produces: H1 `# 萊爾與波萊爾 (Lel and Polel) — 重建與偽造的爭議`; registers English key `lel and polel`, which must not appear in any other `slavic/gods/*.md` H1.

- [ ] **Step 1: Write the page**

Content requirements, all of them to be stated in the page body:

- **Domain:** twin rustic/youth deities, invoked in *koleda* (Koliada) songs, wedding and Yule-cycle festivities; mother identified as Łada.
- **Primary source:** Maciej Miechowita, *Chronica Polonorum* (1519, printed 1521), III.18–19, quoting the refrain `Łada, Łada, Ileli i Leli Poleli` with clapping and hand-striking, and asserting Łada = Leda (not Mars, contra Jan Długosz), Lel = Castor, Polel = Pollux.
- **Corroboration:** Karol Potkański's appeal to the names Lel/Lal and the Russian song `Лелій, лелій, лелій зеленый и Ладо мое` (cf. dialect *лелек* "strong, healthy youth") and to *vodiть leli* — a women's pageant honouring young brides; the 1829 *Pamiętnik Sandomierski* record of three idols Łada, Boda and Leli at Łysiec; the 1468 record of a ban on fairs at the same site on Pentecost.
- **Material evidence:** 1969 finds on Fischerinsel, Mecklenburg (Tollensesee): a 178 cm oak idol of two fused moustached male figures with a shared head/headgear, and a 157 cm female figure; dated to the turn of the 11th–12th c.
- **The historiographic dispute:** Aleksander Brückner's rejection (Lel/Polel as a drunken ditty from *lelać* "to sway"); Andrzej Szyjewski's "zodiacal twins" reading; Alexander Gieysztor's grain-double reading; Grzegorz Niedzielski's alternative (Łada + Leli as the twins, Lel/Polel being Miechowita's invention); late-medieval *lelum polelum* = "slow, sluggish" as desacralisation.
- **Cross-cultural section** comparing to: Greek Dioscuri + Leda; Vedic Aśvins + Sūryā; Lithuanian Ašvieniai + Saulė; a note on the project's own `analyses/divine-twins-comparative.md`.
- **Literary afterlife:** Słowacki *Lilla Weneda*; Mickiewicz *Pan Tadeusz* ("Castor and his brother Pollux glittered at their head, once called among the Slavs Lele and Polele").
- **Citations** (`## 參考文獻`): Miechowita *Chronica Polonorum* 1519/1521 III.18–19; Brückner on Polish mythology; Potkański; Szyjewski, *Religia Słowian*; Gieysztor; Niedzielski; *Pamiętnik Sandomierski* 1829; Fischerinsel 1969 finds; Aleksander Gieysztor, *Mitologia Słowian*; Mieczysław Wojciechowski.

- [ ] **Step 2: Index the page**

Append one row to the table in `cultures/slavic/gods/README.md`:

```markdown
| [萊爾與波萊爾](萊爾與波萊爾.md) | 萊爾與波萊爾 (Lel and Polel) |
```

Place it after the `Lada` row so the table stays roughly alphabetical.

- [ ] **Step 3: Run the test**

Run: `python3 scripts/test_slavic_enrichment.py`
Expected: still exit 1, but `gods/萊爾與波萊爾.md` no longer appears — 4 remaining "file does not exist" failures.

- [ ] **Step 4: Commit**

```bash
git add cultures/slavic/gods/萊爾與波萊爾.md cultures/slavic/gods/README.md
git commit -m "feat(slavic): add Lel and Polel deity page"
```

---

### Task 3: Gods — 魯格耶維特、波列維特與波列努特

**Files:**
- Create: `cultures/slavic/gods/魯格耶維特、波列維特與波列努特.md`
- Modify: `cultures/slavic/gods/README.md`

**Interfaces:**
- Consumes: `NEW_PAGES["gods"][1]` from Task 1.
- Produces: H1 `# 魯格耶維特、波列維特與波列努特 (Rugiaevit / Porevit / Porenut) — 查倫察的三首戰神群像`; registers English key `rugiaevit / porevit / porenut`, unique within `slavic/gods/`.

- [ ] **Step 1: Write the page**

Content requirements:

- **Setting:** the triad of gods of the Rani at Charenza (probably modern Garz, Rügen), destroyed June 1168 after the fall of Arkona. Only two sources: Saxo Grammaticus, *Gesta Danorum* (bk. 14), and the *Knýtlinga saga*.
- **Iconography, per Saxo:**
  - Rugiaevit — oak idol, seven faces under one skull, seven sheathed swords on one belt plus an eighth unsheathed sword nailed into the right fist (it could not be removed without cutting off the hand — the pretext for dismembering), swallows nesting under the lip and fouling the chest; Absalon had to stand on tiptoe to reach the chin; "power almost matching that of Mars".
  - Porevit — five faces, five swords (Saxo, bk. 16).
  - Porenut — five faces, five swords (Saxo, bk. 16).
  - Temple construction: vestibule closed off with purple hangings instead of walls, roof borne on separate columns.
  - The sexual-punishment superstition: copulation in the manner of dogs, and the men unable to separate, sometimes fastened to posts on opposite sides.
- **Etymology:** the `-vitъ` suffix from `vitędzь` "warrior, hero, lord" (contra Michał Łuczyński's `-ovitъ` reading, *Ling Varia* X/2(20), 2015; and contra Kalik & Uchitel, *Slavic Gods and Heroes*, Routledge 2018, who derive Sventovit from St Vitus); Alexander Gieysztor's `ru-` root "roar, heat, oestrus" cf. Russian `ружень`, Czech `říjen`, Bulgarian `руен` (an autumn month) — reading Rugiaevit as a Perun hypostasis; Jacek Banaszkiewicz's reading of Rugiaevit as chief god with Porevit and Porenut as a pair of divine twins completing him (against the Dumézil trinity at Uppsala).
- **Public vs private cult:** the "private" cult at Charenza competing with the theocratic public cult of Sventovit at Arkona; the 300 mounted horsemen of the Arkona temple as the army's core.
- **Cross-cultural section:** link to the project's existing `Svyatovit.md`, `Triglav.md`, `Radegast.md`, plus the three other four-/five-/seven-faced Slavic cases (Sventovit's four heads facing N/S/E/W, Chetyrebog at Tesnovka near Kyiv until 1850, the 1848 Zbruch pillar found in the Zbruch river near Husiatyn, now in the Kraków Archaeological Museum, whose upper register has four faces under one tall hat) and the `comparisons/多面之神與複數的神.md` page created in Task 6.
- **Citations** (`## 參考文獻`): Saxo, *Danorum Regum Heroumque Historia* XIV.564 and XVI; *Knýtlinga saga*; Gieysztor; Łuczyński 2015; Banaszkiewicz; Kalik & Uchitel 2018; Żarnowska-Damelska, "Rugian Slavic God Sventovit — Once More"; C. Schuchhardt's 1921 excavations at Arkona.

- [ ] **Step 2: Index the page**

Append to `cultures/slavic/gods/README.md`:

```markdown
| [魯格耶維特、波列維特與波列努特](魯格耶維特、波列維特與波列努特.md) | 魯格耶維特、波列維特與波列努特 (Rugiaevit / Porevit / Porenut) |
```

- [ ] **Step 3: Run the test**

Run: `python3 scripts/test_slavic_enrichment.py`
Expected: 3 remaining "file does not exist" failures (stories ×2, comparisons ×1).

- [ ] **Step 4: Commit**

```bash
git add cultures/slavic/gods/魯格耶維特、波列維特與波列努特.md cultures/slavic/gods/README.md
git commit -m "feat(slavic): add Rugiaevit/Porevit/Porenut deity page"
```

---

### Task 4: Story — 《伊戈爾之歌》

**Files:**
- Create: `cultures/slavic/stories/伊戈爾之歌.md`
- Modify: `cultures/slavic/stories/README.md`

**Interfaces:**
- Consumes: `NEW_PAGES["stories"][0]` from Task 1.
- Produces: H1 `# 《伊戈爾之歌》(The Tale of Igor's Campaign) — 1185 年佩切內格的敗仗與「我已看見戰場」的預言`; English key `the tale of igor's campaign`, unique within `slavic/stories/`.

- [ ] **Step 1: Write the page**

Content requirements:

- **Subject:** the failed 1185 campaign of Igor Svyatoslavich of Novgorod-Seversk against the Polovtsy; surviving in a single 16th-c. codex, discovered 1792–1795 in A. I. Musin-Pushkin's collection, announced 1797 in the *Spectateur du Nord*, first printed 1800 in a bilingual edition (Malinovsky's translation, Bantysh-Kamensky's Old Russian text), the codex burnt in the Moscow fire of 1812. Generally dated 1185 to the late 1190s; author unknown.
- **Genre and structure:** the "-song" (*пѣсь*) / "word" (*слово*) hybrid that combines *slava* (glorification) with *plach* (lament); the narrator's opening claim that it is "not proper (*не лепо*) for us, brothers, to begin with old words about the severe tale of Igor's host"; Boyan the songster's clairvoyant descent through the "thought-tree" (*мыслену древу*).
- **Key passages to quote in translation:** the two falcon simile of the princes; the boyars' bad-omen speech (two suns dimmed, two young moons, the Kayala river covered in darkness, the "Gothic red maidens" singing Bus's time and gladdening their vengeance on Sharukan); Igor's escape, metamorphosing weasel → white gull → bare foot wolf → falcon; Yaroslav Osmomysl's digression on the fratricidal *kramos* and the famous line about princes saying "this one is mine and that one is mine" and forging *kramos* against themselves; Sviatoslav Vsevolodovich's prophetic dream in which he is clothed in burial garments with pearls (tears) heaped on his breast, and his lament ending "Се ли створисте моей сребреней седине!" ("Have you done this to my silver [hair]?"); the appeal to the sun and the winds, the etymology of *větrъ*/*Stribog's* grandchildren.
- **Historicising frame:** the poem blames the fragmentation of Rus' rather than any single villain, and is composed from the point of view of a contemporary — an unusual stance for a lament.
- **Cross-cultural section:** the lament genre compared to the Greek *threnos*; the Old English elegiac *The Ruin* and *The Wanderer*; the *Śaka* lament tradition; and — closest in structure — the epic lament over a fratricidal civil war, e.g. the "curse and lament" mode of the *Mahabharata*'s Ganga-descents and the closing lament of the *Shahnameh*.
- **Citations** (`## 參考文獻`): *Слово о полку Игореве* (1185–1190s), ed. Musin-Pushkin/Bantysh-Kamansky/Malinovsky, 1800; Likhachev, *Слово о полку Игореве*; Tvorogov's entry in the *Словарь книжников и книжности Древней Руси*; Busul' & Kormushin, "Задонщина"; Baiburin, *Домострой* (on the *kramos*).

- [ ] **Step 2: Index the page**

Append to `cultures/slavic/stories/README.md`:

```markdown
| [伊戈爾之歌](伊戈爾之歌.md) | 《伊戈爾之歌》(The Tale of Igor's Campaign) |
```

- [ ] **Step 3: Run the test**

Run: `python3 scripts/test_slavic_enrichment.py`
Expected: 2 remaining "file does not exist" failures (stories/羅斯的喪葬哭喪.md, comparisons/多面之神與複數的神.md).

- [ ] **Step 4: Commit**

```bash
git add cultures/slavic/stories/伊戈爾之歌.md cultures/slavic/stories/README.md
git commit -m "feat(slavic): add Tale of Igor's Campaign story page"
```

---

### Task 5: Story — 羅斯的喪葬哭喪

**Files:**
- Create: `cultures/slavic/stories/羅斯的喪葬哭喪.md`
- Modify: `cultures/slavic/stories/README.md`

**Interfaces:**
- Consumes: `NEW_PAGES["stories"][1]` from Task 1.
- Produces: H1 `# 羅斯的喪葬哭喪 (Russian Funeral Laments) — 從《米哈伊爾・特維爾哀歌》到受雇的哭喪婦`; English key `russian funeral laments`, unique within `slavic/stories/`.

- [ ] **Step 1: Write the page**

Content requirements:

- **The text:** the *Плач Михаила Тверского*, the lament over Mikhail of Tver, murdered in 1329, preserved in the 1650 *Tverian* compilation of witnesses of holy wonder-workers. Presented as the earliest substantial specimen of a Russian *причитание* (lament-chant).
- **The institution:** the lament is not a lyric but a required ritual element. N. P. Andreev & V. G. Vinogradov state that where relatives could not or would not mourn, professional *плакальщицы* were hired; the same institution is attested in ancient Egypt and ancient Greece, and in prerevolutionary Russian peasant practice. Baiburin: "physical death is not social death" — the burial rite is the transition that must be performed, often over an odd number of years, after which the deceased loses individuality and joins the collective, faceless mass of *нави*.
- **The canonical question:** every lament asks the same question — *why did you die? / what did you lack in this world?* — recorded by Fletcher (1588–89), Margeret, Olearius and Lubicz-Luse; documented in the *Стоглав* prescription that people gather at the Trinity Saturday to weep at the graves "with a great outcry".
- **Professional mourners in the foreigners' accounts:** faces covered with cloth because they were not to be looked at; their cries compared to wolves and dogs; women throwing themselves into the grave and being pulled out just before the earth was shovelled in (Lubicz-Luse at Moscow).
- **The church's suppression:** lists of St John Chrysostom's words on weeping over dead infants; Metropolitan Daniel (d. 1539) condemning weeping over unbaptised and baptised infants alike; the questions of the 15th–16th-c. *Требники* (whether one wept without measure over the dead, tore one's hair, rent one's clothes, cut one's own hair) with the *Ульяния Оsorvina* case in *Повесть об Ульянии Оsorvиной* praised precisely for "not crying without beauty, not tearing her hair, as other wives do, according to the custom of the pagans".
- **Ritual terms and the hiding of the name:** the substitution vocabulary of Sedakova — *смертушка*, *новоренок*, the coffin as "light boatlet" (*легкая лодочка*) that ferries the soul across the water, and hence cemeteries on the far bank of a river; the archaic layer of *нави* behind the Christian *заупокойное богослужение*.
- **Cross-cultural section:** professional mourning women in ancient Egypt and ancient Greece (as Andreev & Vinogradov note); the Greek *threnos* (*threnody*) at the *genos* of the Stelai; the Indian *funeral hymns* of the Rigveda and the Saptapadī rite; the Japanese professional mourers; and the Wailing Wall — plus a link to `comparisons/winter-death-rebirth-goddesses-comparative.md`.
- **Citations** (`## 參考文獻`): *Плач Михаила Тверского* (1650 collection); Fletcher, *Of the Russe Common Wealth* (1591); Olearius, *Description of Muscovy*; Margeret, *Memoirs*; Lubicz-Luse, *Travels to Moscow*; Stoglav (1551); *Slovar' russkogo naroda* (1889–1903) on *плакальщицы*; Sedakova on substitutive ritual vocabulary; Gruznova, *Погребение и проводы*; Baiburin, *Домострой*; Manasikka on Old East Slavic lamenting.

- [ ] **Step 2: Index the page**

Append to `cultures/slavic/stories/README.md`:

```markdown
| [羅斯的喪葬哭喪](羅斯的喪葬哭喪.md) | 羅斯的喪葬哭喪 (Russian Funeral Laments) |
```

- [ ] **Step 3: Run the test**

Run: `python3 scripts/test_slavic_enrichment.py`
Expected: 1 remaining failure, `comparisons/多面之神與複數的神.md: file does not exist`.

- [ ] **Step 4: Commit**

```bash
git add cultures/slavic/stories/羅斯的喪葬哭喪.md cultures/slavic/stories/README.md
git commit -m "feat(slavic): add Russian funeral lament story page"
```

---

### Task 6: Comparison — 多面之神與複數的神

**Files:**
- Create: `cultures/slavic/comparisons/多面之神與複數的神.md`
- Modify: `cultures/slavic/comparisons/README.md`

**Interfaces:**
- Consumes: nothing from earlier tasks except forward references to the two Task 2/3 pages, which by this task exist.
- Produces: H1 `# 多面之神與複數的神 (Many-Faced and Multiplied Gods) — 從魯格耶維特的七張臉到波列維特兄弟`; closes the contract test.

- [ ] **Step 1: Write the page**

Content requirements:

- **Thesis:** the ancient world solved "one god, many mandates" two ways — **(A) 多面／多頭** giving a single deity N faces/heads/limbs on one body, and **(B) 複數化** multiplying the deity into N co-equal figures. Slavic evidence is unusually complete for both.
- **A cross-cultural table** with one row per case and columns for tradition / name / N / medium / governing idea / source. Rows to include:
  - Slavic — Rugiaevit, 7 faces, oak idol, war + sexual, Saxo XIV
  - Slavic — Porevit & Porenut, 5 faces each, oak, war, Saxo XVI
  - Slavic — Sventovit, 4 heads facing N/S/E/W, wood, war + harvest, Saxo XIV.564
  - Slavic — Zbruch pillar (1848, Zbruch river near Husiatyn; now Kraków), 4 faces under one tall hat on a three-register column, cosmic axis, Famintsyn 1884; Rybakov 1987's four-god reading (Perun with horse and sword, Mokosh with the cornucopia, Lada with the ring, Dazbog with the solar symbol, Veles below); Łowmiański 1979's non-Slavic reading
  - Roman — Janus Quadrifons, 4 faces, Janus as the hinge of past and future
  - Iranian — Verethrna, 4 faces, victorious warrior goddess
  - Hindu — Brahmā, 4 faces, *caturmukha* behind and on the four quarters
  - Yoruba — Èṣù, 2 faces (one frontal, one on the rear of the phallic #gọ emblem), crossroads and double vision; Matory's "he is also a Janus"
  - Greek — Dioscuri, 2 co-equal bodies, one mortal one divine (mode B)
  - Vedic — Aśvins, 2 co-equal bodies, physicians of the gods (mode B)
  - Baltic — Ašvieniai + Saulė, twin brothers with the sun goddess as mother (mode B)
  - Gaulish — Tarvos Trigaranus, bull with three cranes, numeric tripling rather than facial multiplication
  - Slavic — the Fate pair Доля/Настя and the two halves of Zorya (mode B) — link to the existing `comparisons/slavic-fate-goddesses.md`
- **Analysis:** (1) why Slavs multiplied faces rather than names — the `-vitъ` titles (`svętъ` + `vitъ`) name a *rank*, not a being, so the same title could be borne by several figures at several sites; (2) the many-faced image makes the deity *co-present* at four or seven points of a ritual circle at once, which is why Sventovit's four heads correspond to the four free posts of his temple barbican; (3) the Zbruch pillar shows the two modes fused — a four-faced top over a three-register cosmos — and Famintsyn was first to read it as linked to Triglav; (4) the cult-of-strength reading in which the seven faces of Rugiaevit index the seven planets or the seven days; (5) the historiographic warning: multi-face counts survive only in hostile Christian chroniclers (Saxo, Adam of Bremen, Helmold) and in a single manuscript tradition, so the numbers are as suspect as the interpretations built on them.
- **Citations** (`## 參考文獻`): Saxo, *Gesta Danorum* XIV.564, XVI; *Chronicon Rethra* (quoted in Widukind of Corvey's *Res gestae Saxonicae* and in Thietmar of Merseburg); Famintsyn, *Древние славянские божества* (1884); Rybakov, *Язычество древней Руси* (1987); Łowmiański, *Religia Słowian* (1979); Banaszkiewicz, *Kultury wczesnego średniowiecza*; Matory on Èṣù; Dumézil, *L'Homme Indo-Européen*; Bopp's comparative mythology on the Aśvins/Dioscuri.

- [ ] **Step 2: Index the page**

Append to `cultures/slavic/comparisons/README.md`:

```markdown
| [多面之神與複數的神](多面之神與複數的神.md) | 多面之神與複數的神 (Many-Faced and Multiplied Gods) |
```

- [ ] **Step 3: Run the test — expect GREEN**

Run: `python3 scripts/test_slavic_enrichment.py`
Expected: `All tests PASSED.` and exit 0. Output must show 5 lines reporting the char count of each page, all ≥ 300.

- [ ] **Step 4: Run project CI — expect GREEN**

Run: `python3 scripts/ci_checks.py`
Expected: `✅  ALL CHECKS PASSED` and exit 0 — in particular no `[ERROR]` line of the form "orphan" or "broken link" for any of the 5 new pages.

- [ ] **Step 5: Verify the culture is no longer the thinnest**

Run:

```bash
for d in cultures/*/; do n=$(basename $d); g=$(ls $d/gods/*.md 2>/dev/null | grep -vc README); s=$(ls $d/stories/*.md 2>/dev/null | grep -vc README); c=$(ls $d/comparisons/*.md 2>/dev/null | grep -vc README); tot=$(cat $d/gods/*.md $d/stories/*.md $d/comparisons/*.md 2>/dev/null | wc -c); echo "$((g+s+c)) $((tot/1000))k $n"; done | sort -k1,1n -k2,2n | head -6
```

Expected: `slavic` no longer heads the list (it should now read `71 <total>k slavic`, with `tupi-guarani`/`aboriginal`/`dacian` on 66 above it).

- [ ] **Step 6: Commit and push**

```bash
git add -A
git commit -m "mythos: enrich slavic"
git push
```

---

## Self-Review

**1. Spec coverage.** Task instruction was: find the thinnest culture by page count; add `gods/`, `stories/`, `comparisons/` pages at ≥300 trad.-Chinese chars each with cross-cultural correspondence and cited sources; then `git add -A && git commit -m "mythos: enrich <culture-name>" && git push`; report what was added.
- *Thinnest culture* — resolved in the pre-plan audit: 46 cultures, `slavic` lowest at 66 content pages *and* lowest total volume (297 kB) among the four-way tie (`aboriginal`, `dacian`, `slavic`, `tupi-guarani`, all 66). Covered by Task 6 Step 5, which re-verifies.
- *gods/ page* — 2 pages, Task 2, Task 3.
- *stories/ page* — 2 pages, Task 4, Task 5.
- *comparisons/ page* — 1 page, Task 6.
- *≥300 trad.-Chinese chars* — enforced by `test_min_length` in Task 1 and reported per page in Task 6 Step 3.
- *cross-cultural correspondence* — enforced by `test_has_cross_cultural`; each page's required content is spelled out in the relevant task.
- *cited sources* — enforced by `test_has_citation` and `test_not_baselined`; each task lists the exact references to cite.
- *commit + push with the exact message* — Task 6 Step 6.
- *report* — final assistant message after Task 6.

**2. Placeholder scan.** No "TBD"/"TODO"/"implement later". No "add appropriate error handling" — the checks are copied verbatim from a file that already exists in the repo. No "similar to Task N" — every task restates the full page content requirements inline. Every file path is absolute-relative to the repo root. The only non-code step is prose authoring, and for those the required facts, sources and structure are given as a checklist rather than as a template to fill.

**3. Type consistency.** `NEW_PAGES` keys `"gods"`, `"stories"`, `"comparisons"` are consumed by `main()` as the directory names under `ROOT/"cultures"/CULTURE`, and every filename listed in Task 1 appears verbatim as the `Create:` path of exactly one later task. `CULTURE = "slavic"` is used by `test_indexed_in_readme` to build `cultures/slavic/<category>/README.md`, matching the three `Modify:` paths. H1 English keys declared in Tasks 2–6 are all distinct and none collides with an existing page's key (existing `slavic` H1s use the forms `斯瓦羅日奇`, `斯維亞托維特（Svyatovit）`, `Radegast`, etc.).

**Execution handoff (auto-selected, unattended run).** The scheduler forbids prompting, so the recommended option is adopted: subagent-driven execution, one subagent per task, with a review gate between tasks. Task 1 is executed directly because every later task's test depends on its exact contents.
