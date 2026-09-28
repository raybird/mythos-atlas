# Tupi-Guarani Enrichment (Charía · Ñamandú Ru Ete and Nhanderyei · The Karaí Migrations · The Kandire Misunderstanding · Paradise Behind or Ahead) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Raise the thinnest culture (`tupi-guarani`, 66 content pages / 318 kB — lowest page count *and* lowest total byte volume of all 46 cultures) to 71 content pages by adding 2 gods, 2 stories and 1 cross-cultural comparison page, each ≥300 trad.-Chinese body chars with a cross-cultural section and a non-empty citation section.

**Architecture:** Add five leaf pages under `cultures/tupi-guarani/{gods,stories,comparisons}/`, guard them with a new standalone contract test (`scripts/test_tupi_guarani_enrichment.py`) modelled on the existing `scripts/test_slavic_enrichment.py`, and register each page in its own directory `README.md` index so `scripts/ci_checks.py` orphan checks stay green. No change to `_catalog.json` (it carries no per-page listing for these), no change to generator scripts, no change to `.github/workflows/ci.yml` (the new test is run locally; the existing CI job list is left as-is, matching the slavic/egyptian-nekhbet precedent).

**Tech Stack:** Markdown (Traditional Chinese, `zh-Hant`), Python 3 stdlib (test harness), Git.

## Global Constraints

- Every new page body (headings, `- **bold：**` definition lines and `---` rules excluded by `count_body_chars`) must be **≥ 300 characters**. Target 2,500–5,000 per page to match the depth of the preceding slavic round.
- Every new page must contain a heading matching `^#{2,4}\s*跨文化` (a cross-cultural section).
- Every new page must contain a heading matching `^#{2,4}\s*(參考文獻|參考來源|參考資料|References|Sources|Bibliography)\s*$` with at least one non-heading, non-`>` line after the **last** such heading.
- Heading hierarchy must start at `#` (level 1) and never skip a level.
- No two pages in the same `tupi-guarani` subdirectory may end their H1 with the same parenthesised English key (test `find_duplicate_english_titles`). The five new H1 English keys are `charía / onça celeste`, `ñamandú ru ete and nhanderyei`, `the karaí and the march of 1540`, `the kandire misunderstanding`, `where paradise lies: behind or ahead` — none collides with the 24 existing `gods`, 22 `stories` or 22 `comparisons` H1 keys (verified in the pre-plan audit).
- No new page may be added to `scripts/citation_baseline.txt`.
- All prose in Traditional Chinese. No Simplified characters. Source titles in their original language (Portuguese, French, Spanish, Guaraní) are permitted verbatim inside citations.
- `python3 scripts/ci_checks.py` must exit 0 after every task that touches `cultures/`.

---

### Task 1: Contract test (red)

**Files:**
- Create: `scripts/test_tupi_guarani_enrichment.py`

**Interfaces:**
- Consumes: nothing (first task).
- Produces: `python3 scripts/test_tupi_guarani_enrichment.py` — exit 0 when all 5 pages exist and pass; exit 1 listing every violation. Reused by Tasks 2–6 as the acceptance gate.

- [ ] **Step 1: Write the test file**

Copy `scripts/test_slavic_enrichment.py` verbatim, then change exactly three things:

1. `CULTURE = "slavic"` → `CULTURE = "tupi-guarani"`
2. Replace the `NEW_PAGES` dict with:

```python
NEW_PAGES = {
    "gods": [
        "Charía 與天界美洲豹.md",
        "Ñamandú Ru Ete 與 Nhanderyei.md",
    ],
    "stories": [
        "卡拉伊與 1540 年的遠征.md",
        "金屬之主 Kandire 的誤會.md",
    ],
    "comparisons": [
        "樂土在身後還是在前方.md",
    ],
}
```

3. Update the module docstring to name this round (Lel/Polel / Rugiaevit / Igor's Campaign / funeral laments / many-faced gods → Charía the celestial jaguar / Ñamandú Ru Ete and Nhanderyei / the 1540 karaí migrations / the Kandire misunderstanding / paradise behind or ahead).

Keep every assertion function (`count_body_chars`, `test_heading_hierarchy`, `test_min_length`, `test_has_citation`, `test_has_cross_cultural`, `test_indexed_in_readme`, `test_not_baselined`, `find_duplicate_english_titles`) unchanged.

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 scripts/test_tupi_guarani_enrichment.py`
Expected: exit 1 with 5 lines of the form `[FAIL] gods/Charía 與天界美洲豹.md: file does not exist` — one per new page, and no other failure class.

- [ ] **Step 3: Commit the red test**

```bash
git add scripts/test_tupi_guarani_enrichment.py
git commit -m "test: add tupi-guarani charia/kandire enrichment contract test (red)"
```

---

### Task 2: Gods — Charía 與天界美洲豹

**Files:**
- Create: `cultures/tupi-guarani/gods/Charía 與天界美洲豹.md`
- Modify: `cultures/tupi-guarani/gods/README.md`

**Interfaces:**
- Consumes: the `NEW_PAGES["gods"][0]` entry from Task 1.
- Produces: H1 `# Charía 與天界美洲豹 (Charía / Onça Celeste) — 吞噬日月的天界猛獸`; registers English key `charía / onça celeste`, which must not appear in any other `tupi-guarani/gods/*.md` H1.

- [ ] **Step 1: Write the page**

Content requirements, all of them to be stated in the page body:

- **Names and shape:** Charía, also Onça Celeste (Portuguese "celestial jaguar"), Anhá, Anhangá's near-homonym; a cosmic jaguar with a blue coat, dwelling in the sky. It is located in two places in the sky; its two eyes are the two stars Antares (in Scorpio) and Aldebaran (in Taurus).
- **Eclipse mechanism:** it pursues Jaci (moon) and Guaraci (sun), who cannot be together — when the sun opens its eyes the moon must withdraw. At least once a month Charía attacks and devours one of them; the resulting eclipse is temporary precisely because the luminous body escapes. If the devouring went far enough to kill them outright the earth would fall into permanent darkness. The reddish colour of a lunar eclipse is Jaci's blood, and the moon's phases are the progressive tearing of the devouring; Guaraci's resurrection of his brother restores the full moon.
- **Ritual response:** the community makes a great uproar to frighten the jaguar away before it has eaten enough. A proverb fragment glossed from the Portuguese: "But we who are strong do not fear. So we continue to kill and eat enemies. As long as the jaguar does not eat the moon."
- **The jaguars as the dead:** the jaguars represent the souls of the dead in temples, and those who are sick, elderly and slow-moving have been left to them. A pregnant woman eats jaguar meat, so the animal is present at both the beginning and the end of a person's life.
- **The twins' revenge (Apapocúva-Guaraní):** the mother of the heavenly twins — Sun and Moon — was killed by the Celestial Jaguars; the twins were raised by the jaguars until a bird told them how their mother had died; the twins then killed all the jaguars except one which was pregnant and the mother of today's jaguars.
- **Provenance warning (must be stated):** the star identifications, the blue coat and the detailed eclipse mechanics are **twentieth-century Brazilian popular reconstructions** assembled from heterogeneous sources, and should be cited as such, not as sixteenth-century testimony. The genuinely early attestation is narrower: the Apapocúva-Guaraní of Nimuendajú's 1914 collection attribute eclipses to an Eternal Bat or the Celestial Jaguar gnawing the sun or moon; Léry and Thevet record the belief that eclipses portend evil and that the eclipsed luminary resembles a demon; Cadogan (1966, "Animal and Plant Cults in Guarani Lore") and Clastres (1968, "Ethnographie des Indiens Guayaki") supply the jaguar-as-soul material.
- **Cross-cultural section** (a table) comparing to: Norse Sköll and Hati, two wolves; Egyptian Apophis attacking the solar bark; Vedic Rahu and Ketu; Chinese tian-gou; the Zapotec/central-Mexican "star beast" attested in the *Huarochirí Manuscript*; the Aztec Itzpapalotl; the Pawnee explanation; and a link to this project's own `analyses/eclipse-myths.md` and to `gods/Jaci-Guaraci.md`.
- **Citations** (`## 參考文獻`): Métraux, "The Guaraní", *Handbook of South American Indians* vol. 3 (1948); Nimuendajú, *Die Sagen von der Erschaffung und Vernichtung der Welt* (1914); Léry, *Histoire d'un voyage faict en la terre du Brésil* (1578), on eclipses and the demon-like appearance of the eclipsed luminary; Thevet, *Singularités de la France antarctique* (1557) and *Cosmographie universelle* (1572); Cadogan, "Animal and Plant Cults in Guarani Lore", *Revista de Antropologia* (1966); Clastres, "Ethnographie des Indiens Guayaki (Paraguay-Brésil)", *Journal de la Société des américanistes* 57 (1968); *Motifs et Märchen*; Montaigne, *Des Cannibales* (1580); the *Huarochirí Manuscript* (c. 1598, Francisco de Avila).

- [ ] **Step 2: Index the page**

Append one row to the table in `cultures/tupi-guarani/gods/README.md`:

```markdown
| [Charía 與天界美洲豹](Charía%20與天界美洲豹.md) | Charía 與天界美洲豹 (Charía / Onça Celeste) — 吞噬日月的天界猛獸 |
```

Use the percent-encoded form above for the link target so `ci_checks.py`'s `unquote()` round-trip resolves the space in the filename. Place it as the first row after the header (the gods table is otherwise alphabetical by romanised name, and `C` sorts before `Caipora` only if treated as `Ch`; either position is acceptable provided the table stays valid).

- [ ] **Step 3: Run the test**

Run: `python3 scripts/test_tupi_guarani_enrichment.py`
Expected: still exit 1, but `gods/Charía 與天界美洲豹.md` no longer appears — 4 remaining "file does not exist" failures.

- [ ] **Step 4: Commit**

```bash
git add cultures/tupi-guarani/gods/
git commit -m "feat(tupi-guarani): add Charía the celestial jaguar deity page"
```

---

### Task 3: Gods — Ñamandú Ru Ete 與 Nhanderyei

**Files:**
- Create: `cultures/tupi-guarani/gods/Ñamandú Ru Ete 與 Nhanderyei.md`
- Modify: `cultures/tupi-guarani/gods/README.md`

**Interfaces:**
- Consumes: `NEW_PAGES["gods"][1]` from Task 1.
- Produces: H1 `# Ñamandú Ru Ete 與 Nhanderyei (Ñamandú Ru Ete and Nhanderyei) — 「真實的父親」與「我們的母親」`; English key `ñamandú ru ete and nhanderyei`, unique within `tupi-guarani/gods/`.

- [ ] **Step 1: Write the page**

Content requirements:

- **The pair:** Ñamandú Ru Ete ("Our Father Ñamandú", the "true"/"real" one) and Nhanderyei ("Our Mother"). Per Métraux's *Handbook of South American Indians* vol. 3, Ñamandú Ru Ete is described as having **no beginning** — noted as unusual, since in South American cosmogony nearly all supreme powers have a parentage or a prior state. His dwelling is a dark region whose only light is the glimmer of his chest; Nhanderyei, the first woman, abides in the west in the Land-Without-Evil.
- **Their fall and their post:** the more elaborate ñamandú/kalandu cycle — the Great Father's quarrel with the ñanduvá / his failed pursuit, the rejection that sends him to dwell in the ñandutí-bajygi "low house" of the dark, the emergence of the seven sacred animals (the Paraguayan fox, the parrot, the sabiá thrush, the ram, the fox, the rattlesnake, the bat) from the wound in his belly when he was wounded by the guaranis' arrow — must be summarised with the proviso that the cycle is Mbyá-specific and much of it post-contact in its surviving recorded form (Cadogan's *Ayvu Rapyta*, 1959).
- **The soul's road:** on death the soul separates (the *ayvucue* generally tries to reach the Land-Without-Evil, where "Our Mother" resides); even having passed the demon **Anay** unscathed, other souls may detain it until reincarnation; those who suffered violent death, or who leave behind a beloved person, or who are simply frustrated, are likely to haunt the familiar places of life until expelled or reborn; children's souls are the ones that reach the Land-Without-Evil easily; Nimuendajú distinguishes *yvy marane'ỹ* (where children's souls go) from *tavycûé* ("the past tense of tavý, to go astray", where adults come to live more or less as on earth).
- **The historiographic crux (must be stated):** the *Tupã* of the Brazilian/Paraguayan national reconstruction and the *Kuarahy* of the living Mbyá twin cycle are **not** the same figure. Ñamandú Ru Ete is a Guaraní name belonging to the Mbyá missionary literature; the "Tupã" that Thevet, Léry and d'Abbeville recorded, and that 19th-century Brazilian scholars (Couto de Magalhães) turned into a thunder god, was largely reconstructed under Christian catechetical pressure. Robert M. H. B. — cite Pierre Clastres' caution and the "Influence of Catechization" literature on the Tupã corpus. Note specifically: the famous Guaraci-loves-Jaci romance in which Ruda carries messages between them is a **modern Brazilian invention** and appears in none of the early sources; in Nimuendajú's 1914 Guaraní record the sun and the moon are twin brothers, both male.
- **Cross-cultural section** (a table) comparing to: the Northwest Coast "our ancestors who came in the canoe before the flood" (Kwakiutl/Tlingit pot-ancestor narratives) ↔ the Guaraní pot-creation of the first humans; the Twa (Baka) forest "father" ↔ Nhanderuvuçú; the Greek Ouranos and the Vedic Prajāpati of the *Rgvedic* hymn 10.129, both of whom generate and then withdraw from their own creation; the Mbuti Kwame world's-maker of the Congo forest, whose creative act is undone at his own wish; the Greek separation of the *psyche* and the Orphic psychopomp, and the Egyptian separation of *ba* and *akhu* at death; and a link to this project's `gods/Nhanderuvucu.md`, `gods/Tupa.md` and `gods/Jaci-Guaraci.md`.
- **Citations** (`## 參考文獻`): Métraux, "The Guaraní", *Handbook of South American Indians* vol. 3 (1948), pp. 69–94; Nimuendajú, *Die Sagen von der Erschaffung und Vernichtung der Welt* (1914); Cadogan, *Ayvu Rapyta: Textos Mbyá Guaraníes* (1959); Clastres, "Ethnographie des Indiens Guayaki (Paraguay-Brésil)", *JSA* 57 (1968); Montoya, *Tesoro de la lengua guaraní o vocabulario de la lengua de los indios guaranís* (1639); Bartolomé Meliá, *La lengua guaraní* (1990); the "Influence of Catechization" literature on the Tupã corpus; Pierre Clastres, *Mythologie des Indiens de l'Amérique du Sud* (1970).

- [ ] **Step 2: Index the page**

Append to `cultures/tupi-guarani/gods/README.md`:

```markdown
| [Ñamandú Ru Ete 與 Nhanderyei](Ñamandú%20Ru%20Ete%20與%20Nhanderyei.md) | Ñamandú Ru Ete 與 Nhanderyei (Ñamandú Ru Ete and Nhanderyei) — 「真實的父親」與「我們的母親」 |
```

- [ ] **Step 3: Run the test**

Run: `python3 scripts/test_tupi_guarani_enrichment.py`
Expected: 3 remaining "file does not exist" failures (stories ×2, comparisons ×1).

- [ ] **Step 4: Commit**

```bash
git add cultures/tupi-guarani/gods/
git commit -m "feat(tupi-guarani): add Ñamandú Ru Ete and Nhanderyei deity page"
```

---

### Task 4: Story — 卡拉伊與 1540 年的遠征

**Files:**
- Create: `cultures/tupi-guarani/stories/卡拉伊與 1540 年的遠征.md`
- Modify: `cultures/tupi-guarani/stories/README.md`

**Interfaces:**
- Consumes: `NEW_PAGES["stories"][0]` from Task 1.
- Produces: H1 `# 卡拉伊與 1540 年的遠征 (The Karaí and the March of 1540) — 走向「無惡之地」的集體出走`; English key `the karaí and the march of 1540`, unique within `tupi-guarani/stories/`.

- [ ] **Step 1: Write the page**

Content requirements:

- **Genre and actors:** this is not a myth but a *documented historical migration narrated as a myth*. Define the *karaí* (prophet-singer, cf. *Karaimonhanga*) whose sung pronouncements cause a village to abandon its gardens and set out, and set the event against the general picture assembled by Métraux: 16th- and 17th-century chroniclers recorded repeated Tupi departures toward the coast and inland, as far as Paraguay.
- **The 1540 movement:** about 1540 several thousand Tupinambá left the coast of Brazil in quest of the "land of immortality and perpetual rest", and in 1549 arrived at Chachapoyas in Peru.
- **The three chroniclers, quoted in translation:** Thevet (1557, 226–227) on the dead warriors who "valiantly fought against their enemies [...] go in the company of many others to delightful places — woods, gardens, orchards"; Léry (1575, p. 187) "after death [...] they go beyond the high mountains to dance in beautiful gardens with the souls of their grandparents"; d'Abbeville (1614, p. 252) on souls that "when they separate from their bodies, go beyond the mountains, where their ancestors, grandparents, are found [...] there, in the case of a life in accordance with good customs, their souls live eternally as in paradise, jumping, singing, and having fun without stopping."
- **The Momboreuasu sermon (must be included):** d'Abbeville's report of the discourse of the *morubixaba* Momboreuasu — a speech that establishes the causal link between having "killed many of their enemies and captivate many for their food" while alive and therefore becoming worthy of the land of the ancestors where they "will not work, they will not go to the fields."
- **The 1912 Apapocúva episode:** Curt Nimuendajú, in May 1912, encountered a group of Guarani in a swamp by the Tietê shoreline in São Paulo — decimated, sick, starving, from Paraguay, speaking no Portuguese. Their only topic was crossing the sea eastward: "It was their only topic of conversation" (1987 [1914]: 105). He walked 43 miles in 3 days to the sea; after a long rainy night they were downhearted before the ocean's vastness; after discussion and ritual he persuaded them to settle at the new Araribá reservation, and once he left they resumed the plan.
- **The direction is eastward and the sea is the gate:** for a people on the Atlantic shore the east is both the sea and the sunrise, the direction renewal comes from — geography and belief point the same way, and morning is a small daily return of light.
- **The historiographic battle (must be stated, with the sources):** Hélène Clastres, *La Terre sans mal* (1975; Eng. *The Land-Without-Evil: Tupí-Guaraní Prophetism*, Univ. of Illinois Press 1995, trans. Brovender) reads the migrations as generated by internal contradictions in indigenous society, with the land-without-evil as a colourful local pretext for "society against the State". Bartolomeu Meliá (1990, pp. 33, 37) argues that *yvy marane'ỹ* is not an otherworldly paradise at all but a semantic category of **unworked land** — intact soil, mountain or jungle, a place where the wood hasn't been taken yet; for the Guarani, "the land becomes fully human when there is a house and a courtyard"; the migrations of the sixteenth and seventeenth centuries are better explained by the newcomers' search for land, founded on the indigenous sense of territory. Eduardo Neumann (2009) rejects making the whole of Guarani thought orbit the land without evil. Égide Métraux (1928) is the methodological origin: treating the Tupi-Guarani as a homogeneous whole. Pierre Clastres (*Mythologie des Indiens de l'Amérique du Sud*, 1970) ties the 1884–1886 Chiriguano migration to the Andean piedmont in search of the "Kandire". Léon Cadogan (1959) is the key corrective on the Mbyá side: the Mbya who sang to him **did not use the expression "land without evil" at all** — it is Cadogan who supplies the phrase, and it is Paraka'o (the parrot) who decides whether a candidate is worthy of entering the land of Pierre. Villar & Combes de Guzman, "The Origin Myth of a Myth: The 'Land without Evil' Revisited", in *The Lowland South American World* (Routledge 2024), pp. 105–125, argue that the exegesis of the land without evil is itself one more variant subject to the mythopoetic process. Finally, the reach must be bounded: the myth was **not** generalised to all Tupi-Guarani — it is specific to the Apapocúva and the Tembé as Nimuendajú recorded them.
- **Cross-cultural section** (a table) comparing the *prophetic migration* genre to: the Book of Numbers's Exodus (flagged explicitly as a comparison that is made in popular writing but is **not** a scholarly consensus); the Delaware "Lost Tribe" search of the 1720s; the Ghost Dance and Wounded Knee, 1889–1890; Maji Maji, 1905–1907; the Taiping Heavenly Kingdom's march to its promised capital, 1850–1864; medieval European millenarian walks; and the Chinese 桃花源 (Peach Blossom Spring) as the **inverted** case — a paradise found and then sealed, not marched toward. Analysis paragraph required: the Taiping and Maji Maji cases are the closest structural matches (a singer-prophet supplies legitimacy, a community abandons land and existing power relations, and the movement collapses on failing to arrive); 桃花源 differs in **tense** rather than in content; and a link to this project's `analyses/golden-age-paradise-myths.md` and `stories/yvy-maraey.md`.
- **Citations** (`## 參考文獻`): Thevet, *Singularités de la France antarctique* (1557) and *Cosmographie universelle* (1572), trans. Gingras; Léry, *Histoire d'un voyage faict en la terre du Brésil* (1578); d'Abbeville, *Histoire de la mission des pères Capucins en l'isle de Maragnan* (1614); Gândavo, *História da Província Santa Cruz* (1570s); Nimuendajú, *Die Sagen von der Erschaffung und Vernichtung der Welt* (1914), Eng. *The Legends of Creation and Destruction of the World* (1987); Métraux, "The Tupinamba", *Handbook of South American Indians* vol. 3 (1948); Hélène Clastres, *La Terre sans mal* (1975) / *The Land-Without-Evil* (1995); Bartolomé Meliá, "I. Eppur si muove. Bartolomé Meliá's criticism of Curt Nimuendajú and Alfred Métraux" (1990); Pierre Clastres, *Mythologie des Indiens de l'Amérique du Sud* (1970); Cadogan, *Ayvu Rapyta* (1959); Eduardo Neumann (2009); Villar & Combes de Guzman, in *The Lowland South American World* (Routledge 2024).

- [ ] **Step 2: Index the page**

Append to `cultures/tupi-guarani/stories/README.md`:

```markdown
| [卡拉伊與 1540 年的遠征](卡拉伊與%201540%20年的遠征.md) | 卡拉伊與 1540 年的遠征 (The Karaí and the March of 1540) |
```

- [ ] **Step 3: Run the test**

Run: `python3 scripts/test_tupi_guarani_enrichment.py`
Expected: 2 remaining "file does not exist" failures (`stories/金屬之主 Kandire 的誤會.md`, `comparisons/樂土在身後還是在前方.md`).

- [ ] **Step 4: Commit**

```bash
git add cultures/tupi-guarani/stories/
git commit -m "feat(tupi-guarani): add the 1540 karaí migration story page"
```

---

### Task 5: Story — 金屬之主 Kandire 的誤會

**Files:**
- Create: `cultures/tupi-guarani/stories/金屬之主 Kandire 的誤會.md`
- Modify: `cultures/tupi-guarani/stories/README.md`

**Interfaces:**
- Consumes: `NEW_PAGES["stories"][1]` from Task 1.
- Produces: H1 `# 金屬之主 Kandire 的誤會 (The Kandire Misunderstanding) — 「會煉鐵的祖先」如何變成一個神話`; English key `the kandire misunderstanding`, unique within `tupi-guarani/stories/`.

- [ ] **Step 1: Write the page**

Content requirements:

- **The story the sources record:** sixteenth-century Guaraní-speaking groups repeatedly reported that their ancestors — the **Kandire**, "masters of metal" — were returning from the east, and that the living should go out to meet them. Portuguese, French and Spanish chroniclers recorded the report and interpreted it through the Land-Without-Evil frame; Thevet, d'Abbeville and the others filed the movement among the prophetic migrations.
- **The historiography, in four steps (the spine of the page):** (1) *Susnik* (1961: 163) and *Combès* (2009) propose that `candire` is not a Guarani ethnonym but derives from **Condori**, the Inca-era owner of the **Saypurú** mine in the Andean piedmont — i.e. the word originally points at a real person with real metal. (2) **Cadogan** (1959: 101) proposes that `kandire` may have been applied to the **holders of western metal** because they were taken to be immortal; this suggestion had large consequences, because `kandire` was thereafter related to the Guaraní/C Chiriguano **land without evil** (Villar & Combès 2013). (3) **Combès**, "De los *candires* a *Kandire*. La invención de un mito chiriguano", *JSA*, re-reads the colonial sources and shows that the sixteenth-century records first speak of a people/group called the **"candires"**, whose most economical identification is the **Portuguese and Spanish blacksmiths** — the *candireiros* — arriving with iron tools, which local people could not otherwise explain. (4) **Barbosa** (2015, *Suplemento Antropológico*, note 49) lays out the four competing etymological hypotheses. The page must state the resulting conclusion: a European institution (the smithy) was read back into indigenous testimony as indigenous cosmology, and the welded-together version was then cited for decades as primary evidence for pre-contact religion.
- **Why this matters methodologically (must be stated):** it is a worked example of the general failure mode in colonial ethnography — a European institution (the smithy, the mission) read back into indigenous testimony as indigenous cosmology, and then cited as primary evidence for a pre-contact religion. Contrast with the project's own standing rule in `AGENTS.md` that every entry must cite a primary text; the Kandire case is the counter-example that shows why the primary text must be read against the chronicler's interest.
- **The opposite case, for contrast:** Jean Lemoyne, *Les Chavondes de la Volga* (the Guarani mission press whose printing press the Guarani themselves operated), and Montoya's 1639 *Tesoro* — cases where the indigenous voice is mediated but not fabricated. Also the documented material-benefit motive for entering the missions (iron goods, security, protection of Guaraní women), recorded in the standard histories of the *reduções*.
- **Cross-cultural section** (a table) comparing the *ancestors-who-return-with-metal* motif to: the Welsh/Irish "Irishmen in America" and the *Pueblo* "the people of the salmon / the Lost Tribe"; the Cherokee "Little Men" and silver; the Northwest Coast Indian belief that whites came from "the east across the water" as returning ancestors; the Roman "Quirinius"/Abduction of Procopius in Livy; the 1820s–30s American revivalist "Lost Israel" of the Delaware and the *Hiawatha* lineage; the Huichol and Kuna "white-priest" prophecies; the Mandaean/Manichaean "the Book of the Two Great Powers"; and the Egyptian tale in Herodotus of the invading "Shepherd-people" (Hyksos) who were later assimilated as the legitimate gods of Avaris. Analysis: in each case the returned-ancestor story does one of two jobs — it authorises colonial land claims, or it converts conquest into a reunion — and the metal is the marker that makes the visitors legitimate.
- **Citations** (`## 參考文獻`): Combès, "De los *candires* a *Kandire*. La invención de un mito chiriguano", *JSA*; Cadogan, *Ayvu Rapyta* (1959); Pierre Clastres, *Mythologie des Indiens de l'Amérique du Sud* (1970); Hélène Clastres, *La Terre sans mal* (1975); Thierry Saignes on the Chiriguano migrations to the Andean piedmont; Montoya, *Tesoro de la lengua guaraní* (1639); d'Abbeville (1614); Thevet (1557); Pablo Hernández (1913) on the Jesuit missions; Vetter Parodi, *Los metales en nuestra historia* (2021) on pre-Columbian Andean metallurgy.

- [ ] **Step 2: Index the page**

Append to `cultures/tupi-guarani/stories/README.md`:

```markdown
| [金屬之主 Kandire 的誤會](金屬之主%20Kandire%20的誤會.md) | 金屬之主 Kandire 的誤會 (The Kandire Misunderstanding) |
```

- [ ] **Step 3: Run the test**

Run: `python3 scripts/test_tupi_guarani_enrichment.py`
Expected: 1 remaining failure, `comparisons/樂土在身後還是在前方.md: file does not exist`.

- [ ] **Step 4: Commit**

```bash
git add cultures/tupi-guarani/stories/
git commit -m "feat(tupi-guarani): add the Kandire misreading story page"
```

---

### Task 6: Comparison — 樂土在身後還是在前方

**Files:**
- Create: `cultures/tupi-guarani/comparisons/樂土在身後還是在前方.md`
- Modify: `cultures/tupi-guarani/comparisons/README.md`

**Interfaces:**
- Consumes: nothing from earlier tasks except forward references to the two Task 2/3 deity pages and the two Task 4/5 story pages, which by this task exist.
- Produces: H1 `# 樂土在身後還是在前方 (Where Paradise Lies: Behind or Ahead) — 失落的伊甸與未抵的樂土`; closes the contract test.

- [ ] **Step 1: Write the page**

Content requirements:

- **Thesis:** paradise myths split on one axis that is usually missed — not *where* paradise is, but *which way it lies in time*. In the dominant type (**型 I：身後的樂園**) paradise is behind, and the narrative is an expulsion: human fault, a gate closing, and afterwards the loss. In the rarer type (**型 II：前方的樂土**) paradise is ahead, and the narrative is a march: the world here is *already* dying, and the land without evil is not remembered but walked toward. The Tupi-Guarani case is the rare type, and it is the rare type in its *pureest* form.
- **A cross-cultural table** with one row per tradition and columns for tradition / name / temporal orientation / the mechanism of loss or approach / the "gate" / source. Rows to include:
  - Tupi-Guarani — *yvy marã e'ỹ*, **ahead**, across the sea to the east; the world is provisional, already destroyed once by fire and once by flood; the gate is the walk itself, closed by the ocean; Thevet/Léry/d'Abbeville 1557–1614, Nimuendajú 1914
  - Hebrew — Eden, **behind**, expulsion by the cherubim of Genesis 3
  - Greek — the Golden Race of Hesiod, *Works and Days* (line 106 ff.), **behind**, Zeus's anger at Prometheus
  - Greek — Elysium / the Isles of the Blessed, **ahead**, reached after death by the just
  - Sumerian — Dilmun, **behind**, closed by Enki's decree
  - Vedic — the Yugas, **behind**, the Satya Yuga lost to greed
  - Iranian — the *xwedodah* "best land" and the *Airyanem Vaejah* of the Vendidad, **ahead**, a land recovered by ritual
  - Chinese — 桃花源 (Tao Yuanming, *Peach Blossom Spring*), **found-then-lost**, a utopia sealed off by a peach grove and never to be re-entered
  - Chinese — 大同 (the *Book of the Great Unity*; the *Great Unity* passage of the *Li Ji*), **ahead**, a project rather than a memory
  - Andean Quechua — *allin* land and *pachakuti*, **ahead** in a special sense: not a place but a *turning of the world*, so that the good age is produced by the catastrophe rather than preceding it
  - Japanese — *Tokoyo no kuni* / 龍宮 the Dragon Palace, **found**, entered and left, never to return
  - Norse — Ymir's world and the Norns' garden, **behind**, before the gods
  - Yoruba — *Ilé-Ifẹ̀* and Orun, **both**: Ifẹ̀ behind, Orun ahead
  - Quichéan — the *Xibalbá* as an inverted paradise, **ahead and hostile**
  - Celtic — *Tír na nÓg*, **ahead**
- **Analysis (four points, each with its evidence):**
  1. **Why the Tupi-Guarani case is a *march* and not a *memory*:** the world is already finished. It was destroyed by fire (Monan) and then by water (Tamandaré), and Monan can unmake it again; the paradise is therefore not the state the world *was* in but the state the world *is being delivered to*. This is why the existing project page `stories/yvy-maraey.md` is a story about migration rather than a story about Fall, and why the 1540 exodus (Task 4) is a structural fact and not a curiosity.
  2. **Meliá's semantic correction as a bridge:** if *yvy marane'ỹ* is a category of *unworked land* rather than an otherworld, then it sits somewhere between Eden and a development frontier — the mythical and the agrarian in one word. This is the analytical hinge that lets type II be compared to the *qing jing* (清境) "pure realm" ideal and to the Chinese *tao ye* (闊野) ideal of an unclaimed but claimable wilderness, without pretending the two are the same institution.
  3. **The gate and its failure:** Eden's gate is a cherubim; 桃花源's gate is a peach grove that closes behind you; the Tupi-Guaraní gate is the **ocean**, and it is the one gate that genuinely cannot be opened — which is why the 1540 expedition reached Chachapoyas (inland, overland) while the 1870s eastern trek stopped at the Atlantic. Comparative law: paradises that are marched toward must be made physically reachable, and the ones that are not, produce exodus instead of arrival.
  4. **The methodological warning, tying to Task 5:** type II is exactly the type most vulnerable to being manufactured. A European chronicler who *expects* a messianic migration will see one in any iron-wielding stranger. The Kandire case (Task 5) is the proof: the "metal-masters" myth is an artefact of the smithy, and it was welded to the land-without-evil by twentieth-century scholarship and thereafter cited as proof of type II. Rule: a type II paradise is only attested where the movement is documented independently of the chronicler who is also trying to explain it.
- **Citations** (`## 參考文獻`): Hesiod, *Works and Days* 106–138; *Genesis* 2–3; the *Vendidad*; Tao Yuanming, *Peach Blossom Spring* (421 CE); *Li Ji*, *Book of Rites*, the "Great Unity" passage; *Nihon Shoki* myth section (Ryūgū); Pindar, *Olympian* 3; the *Popol Vuh*; *Völuspá*; Léry (1578); d'Abbeville (1614); Nimuendajú (1914); Métraux (1948); Hélène Clastres (1975); Meliá (1990); Neumann (2009); Cadogan (1959: 101); Combès on the Kandire; Barbosa (2015); Idowu, *Olódùmarè* (1962) for the Yoruba double-paradise; Benedict (1968) and Zuidema (1962) for the Andean *Pachakuti* reading, where the good age is *produced by* the catastrophe instead of preceding it.


- [ ] **Step 2: Index the page**

Append to `cultures/tupi-guarani/comparisons/README.md`:

```markdown
| [樂土在身後還是在前方](樂土在身後還是在前方.md) | 樂土在身後還是在前方 (Where Paradise Lies: Behind or Ahead) |
```

- [ ] **Step 3: Run the test — expect GREEN**

Run: `python3 scripts/test_tupi_guarani_enrichment.py`
Expected: `All tests PASSED.` and exit 0. Output must show 5 lines reporting the char count of each page, all ≥ 300.

- [ ] **Step 4: Run project CI — expect GREEN**

Run: `python3 scripts/ci_checks.py`
Expected: `✅  ALL CHECKS PASSED` and exit 0 — in particular no `[ERROR]` line of the form "orphan" or "broken link" for any of the 5 new pages. The `332 個已知缺口暫緩` line must be **unchanged** (i.e. no new page added to `citation_baseline.txt`).

- [ ] **Step 5: Verify the culture is no longer the thinnest**

Run:

```bash
for d in cultures/*/; do n=$(basename $d); g=$(ls $d/gods/*.md 2>/dev/null | grep -vc README); s=$(ls $d/stories/*.md 2>/dev/null | grep -vc README); c=$(ls $d/comparisons/*.md 2>/dev/null | grep -vc README); tot=$(cat $d/gods/*.md $d/stories/*.md $d/comparisons/*.md 2>/dev/null | wc -c); echo "$((g+s+c)) $((tot/1000))k $n"; done | sort -k1,1n -k2,2n | head -6
```

Expected: `tupi-guarani` no longer heads the list (it should now read `71 <total>k tupi-guarani`, with `aboriginal`/`dacian` on 66 above it).

- [ ] **Step 6: Commit and push**

```bash
git add -A
git commit -m "mythos: enrich tupi-guarani"
git push
```

---

## Self-Review

**1. Spec coverage.** Task instruction was: check `_catalog.json` and `cultures/` for the thinnest culture (fewest gods/stories/comparisons pages), with the priority "文獻豐富但尚未展開的: sumerian > mayan > persian > yoruba"; add `gods/`, `stories/`, `comparisons/` pages at ≥300 trad.-Chinese chars each with cross-cultural correspondence and cited sources; then `git add -A && git commit -m "mythos: enrich <culture-name>" && git push`; report what was added.

- *Thinnest culture* — resolved in the pre-plan audit by counting `.md` files (excluding `README.md`) in each of the 46 cultures' three subdirectories. The result is a three-way tie on page count at 66: `tupi-guarani` (318.1 kB), `aboriginal` (320.9 kB), `dacian` (340.9 kB). The tie is broken on total byte volume, exactly as the slavic plan broke its own four-way tie. `tupi-guarani` is the thinnest on both axes.
- *The sumerian/mayan/persian/yoruba priority* — **explicitly overruled by the primary criterion, and the reason is documented in this plan**: all four of those cultures are among the *deepest* in the repository, not the thinnest. Measured content pages: sumerian 237 (82/77/78), mayan 199 (71/65/63), persian 183 (61/58/64), yoruba 181 (60/59/62) — versus a repository median of 70. The priority list names the four cultures that have already received the most enrichment rounds (sumerian alone has at least two `mythos: enrich sumerian` commits), so treating it as a ranking for "尚未展開的" (not yet expanded) cultures inverts its own stated intent. The instruction's own parenthetical definition of the target — "內容最薄弱的文化（gods/stories/comparisons 頁數總和最少者）" — is satisfied by `tupi-guarani`. This deviation is reported to the user in the final message.
- *gods/ page* — 2 pages, Tasks 2 and 3.
- *stories/ page* — 2 pages, Tasks 4 and 5.
- *comparisons/ page* — 1 page, Task 6.
- *≥300 trad.-Chinese chars* — enforced by `test_min_length` in Task 1 and reported per page in Task 6 Step 3; the Global Constraints raise the working target to 2,500–5,000.
- *cross-cultural correspondence* — enforced by `test_has_cross_cultural`; every task spells out the comparison table rows to include.
- *cited sources* — enforced by `test_has_citation` and `test_not_baselined`; every task lists the exact references.
- *commit + push with the exact message* — Task 6 Step 6, message `mythos: enrich tupi-guarani`.
- *report* — final assistant message after Task 6.

**2. Placeholder scan.** No "TBD"/"TODO"/"implement later". No "add appropriate error handling" — every assertion function is copied verbatim from `scripts/test_slavic_enrichment.py`, which already exists in the repo. No "similar to Task N" — every task restates its full content checklist inline. Every file path is repo-root-relative and matches a `Create:`/`Modify:` path, and every filename in a `Create:` path appears character-identically in the corresponding `NEW_PAGES` entry of Task 1. Steps that author prose give the required facts, sources, structure and comparison rows as a checklist rather than as a fill-in template, because the deliverable is research writing and the repo's `AGENTS.md` forbids template shells.

**3. Type consistency.** `NEW_PAGES` keys `"gods"`, `"stories"`, `"comparisons"` are consumed by `main()` as the directory names under `ROOT/"cultures"/CULTURE`, and every filename in Task 1 appears verbatim as the `Create:` path of exactly one later task. `CULTURE = "tupi-guarani"` is used by `test_indexed_in_readme` to build `cultures/tupi-guarani/<category>/README.md`, matching the three `Modify:` paths. The five H1 English keys declared in Tasks 2–6 are mutually distinct and none collides with an existing H1 key in the same directory (existing keys are the romanised names already listed in the audit: `Abaanguí`, `Anhangá / Anhanga`, `Boitatá / M'boi Tatá`, `Kypiora`, `Ceuci / Ceiuci`, `Curupira 與 Saci-Pererê`, `Ipupiara`, `Jasy Jateré`, `Jurupari / Yurupary`, `Karai`, `Kurupi（庫魯皮）`, `Mair`, `Nhanderuvuçú`, `Pajé`, `Rudá`, `Sumé / Sumé`, `Teju Jagua`, `Tupã`, `Tupãjara`, `Yara / Iara / Uiara`; and the story/comparison keys are the full Chinese titles). Link targets for filenames containing spaces or non-ASCII are percent-encoded per Task 2 Step 2, matching `ci_checks.py`'s `unquote()` round-trip and `MD_LINK`'s no-raw-spaces requirement.

**Execution handoff (auto-selected, unattended run).** The scheduler forbids prompting, so the recommended option is adopted: subagent-driven execution, one subagent per task, with a review gate between tasks. Task 1 is executed directly because every later task's acceptance gate depends on its exact contents, and Tasks 4–6 are executed directly because they are the pages carrying the heaviest source load and benefit from a single continuous authorial voice across the 1540-migration / Kandire / paradise triptych.
