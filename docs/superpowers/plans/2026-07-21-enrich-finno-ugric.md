# Finno-Ugric Mythology Enrichment Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich the weakest culture (finno-ugric, 41 pages) with 6 new content pages and clean up 2 duplicates.

**Architecture:** Add 2 gods pages, 2 stories pages, 2 comparisons pages. Remove 2 duplicate files. Each page must be 300+ words in traditional Chinese with cross-cultural comparisons and academic references.

**Tech Stack:** Markdown content creation, git operations

## Global Constraints

- All content in Traditional Chinese (繁體中文)
- Each page minimum 300 words
- Must include cross-cultural comparisons table
- Must include `## 參考文獻` or `## 參考來源` section with real academic sources
- Follow existing file naming conventions

---

### Task 1: Create gods/Joukahainen.md

**Files:**
- Create: `cultures/finno-ugric/gods/Joukahainen.md`

**Content:** Young Lapland sorcerer who challenges Väinämöinen to a singing duel, loses, and is swallowed into a swamp. His sister Aino is offered as ransom. Cross-cultural comparison with other "young challenger" archetypes.

### Task 2: Create gods/Otava.md

**Files:**
- Create: `cultures/finno-ugric/gods/Otava.md`

**Content:** The Great Bear constellation (Otava/Ursa Major) in Finnish mythology. Seven sisters turned into bears, fleeing a celestial hunter. Cross-cultural comparison with Greek Callisto/Arcturus, Indian Saptarishi, and other bear constellation myths.

### Task 3: Create stories/Väinämöinen的最後離去.md

**Files:**
- Create: `cultures/finno-ugric/stories/Väinämöinen的最後離去.md`

**Content:** The final departure of Väinämöinen in Kalevala — after the birth of the "Son of Marjatta," Väinämöinen leaves in a copper boat, leaving his kantele as legacy. Cross-cultural parallels with prophet departures.

### Task 4: Create stories/Ilmarinen的遠征與失敗.md

**Files:**
- Create: `cultures/finno-ugric/stories/Ilmarinen的遠征與失敗.md`

**Content:** Ilmarinen's failed quest to Pohjola — his four attempts at forging (bow, ship, cow, Sampo), and his later disastrous marriage to Louhi's daughter. Cross-cultural with Hephaestus and other divine craftsmen.

### Task 5: Create comparisons/Lemminkäinen的死亡與復活跨文化比較.md

**Files:**
- Create: `cultures/finno-ugric/comparisons/Lemminkäinen的死亡與復活跨文化比較.md`

**Content:** Comparative analysis of Lemminkäinen's death in Tuonela and resurrection by his mother, vs Osiris, Dionysus, Adonis, Baldur, Christ resurrection patterns.

### Task 6: Create comparisons/芬蘭森林神靈與跨文化自然崇拜比較.md

**Files:**
- Create: `cultures/finno-ugric/comparisons/芬蘭森林神靈與跨文化自然崇拜比較.md`

**Content:** Finnish forest spirits (Tapio, Mielikki) compared with Norse Green Man, Celtic Cernunnos, Japanese Kami, Siberian nature spirits, and indigenous forest worship.

### Task 7: Remove duplicate files

**Files:**
- Delete: `cultures/finno-ugric/stories/庫勒沃的復仇悲劇.md` (duplicate of Kullervo的復仇與命運.md)
- Delete: `cultures/finno-ugric/comparisons/Sampo魔法磨與跨文化豐饒神器比較.md` (duplicate of Sampo與跨文化豐饒神器比較.md)

### Task 8: Git commit and push

- `git add -A`
- `git commit -m "mythos: enrich finno-ugric"`
- `git push`
