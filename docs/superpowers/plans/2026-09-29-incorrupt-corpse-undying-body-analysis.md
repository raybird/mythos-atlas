# 屍身不朽（身體防腐與靈魂之錨）跨文化分析文章 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `analyses/` 新增一篇繁體中文跨文化比較分析，主題為「屍身不朽」——把肉身防腐、保存與「不死」當作靈魂錨點的儀式技術，涵蓋古埃及、希臘—羅馬、佛教舍利、中國馬王堆與殭屍／尸解、西藏虹化、安第斯（帕拉卡斯／摩雪）、東正教與天主教聖髑、斯堪的納維亞沼澤屍、馬達加斯加法馬迪哈納共九組傳統。

**Architecture:** 純內容型變更——新增一個 Markdown 分析檔，並同步兩個索引檔（`analyses/README.md` 字母序條目、`analysis-index.md` 編號表列與篇數標題）。無程式邏輯、無資料庫遷移。驗證依靠既有的 `scripts/ci_checks.py`（標題層級、內部連結、孤兒頁、引用區塊非空）。

**Tech Stack:** Markdown（CommonMark）、Python 3.11（CI 檢查腳本）、Git。

## Global Constraints

- 語言：繁體中文；外文專名以括號標註（例：開啟聖口儀式 (Opening of the Mouth)）。禁止簡體字。
- 每條事實必須引用原始文獻、考古報告或學術研究，標註卷／章／篇／編號；不確定者必須明說「傳說」或「學界未定論」。
- 跨文化平行需以 `↔` 連接對應關係（見 `/workspace/projects/mythos-atlas/AGENTS.md`）。
- 不得使用 `populate.py` 產生內容。
- 既有覆蓋範圍必須在文中聲明邊界以避免重複：`analyses/speaking-relics-object-testimony-comparative.md`（遺物**發聲作證**）、`analyses/straw-man-substitute-bodies-comparative.md`（**替身**）、`analyses/reincarnation-metempsychosis.md`（**靈魂輪迴**）、`analyses/external-soul-life-token-comparative.md`（**外部靈魂道具**）、`analyses/esoteric` 類不存在的類別（勿引用）、`analyses/first-funeral-burial-rites-myths-comparative.md`（**首次葬禮**）。本篇只做「屍身本身的保存與不朽宣稱」，不重做上述範圍。
- `analyses/README.md` 與 `analysis-index.md` 必須同步，否則 CI 報 orphan。
- 檔名與索引標題的既有慣例：檔名 `<topic>-comparative.md`；`analysis-index.md` 標題欄以「副題——母題名＋跨文化比較（案例串）」格式撰寫。
- Git 訊息格式：`mythos: analysis incorrupt-corpse-undying-body`。

---

## File Structure

| 檔案 | 動作 | 責任 |
|------|------|------|
| `analyses/incorrupt-corpse-undying-body-comparative.md` | 新增 | 唯一內容來源：摘要、不朽公式、對照表、九則個案、結構分析、參考文獻、相关條目 |
| `analyses/README.md` | 修改（+1 行） | 字母序索引條目（插在 `incense-sacred-smoke-comparative.md` 與 `indo-european-myth-connections.md` 之間） |
| `analysis-index.md` | 修改（+2 行） | 標題計數 `（554 篇）`→`（555 篇）` 與編號 555 的表列 |
| `docs/superpowers/plans/2026-09-29-incorrupt-corpse-undying-body-analysis.md` | 新增 | 本計畫（隨 commit 一起入庫，與 `2026-09-27-speaking-relic-object-testimony-analysis.md` 同例） |

`analyses/README.md` 標示為 auto-generated，但近期 `mythos: analysis` commit（`9b84355d` 等）皆以手動插入一行維護，**不要**執行 `regenerate_all.py`，否則會重排整份索引。

---

## Task 1: 建立計畫檔

- [ ] 寫入本計畫檔（已完成）
- [ ] 確認計畫檔不破壞 CI：`docs/` 已在 `ci_checks.py` 的 `EXCLUDED_TOP_DIRS` 中（`'docs'`）

## Task 2: 事實查證（網路搜尋）

- [ ] 查證古埃及：死者書卷「不死」咒組（Sprüche 154–160、434–440）、開啟聖口儀式 (Opening of the Mouth)、卡 (Ka) 與屍體的關係、70 日防腐流程、第廿六王朝 Djehuty 墓
- [ ] 查證西藏：不死灌頂／虹化 (gti lng／'pho ba)、昌帕嘉措（Csangpa Gyatso, 1617）自製木乃伊、1992–93 年甘丹洞（Kung thang／江孜）開挖的木乃伊報告
- [ ] 查證佛教舍利 (śarīra)：羯語佛經中舍利的定義（色、香、味、觸法）、斯里蘭卡康提佛牙寺牙舍利的供奉與月例瞻禮
- [ ] 查證中國：馬王堆一號墓辛追（西元前 168 年下葬、1972 年發掘、屍體與絲質保存）、「尸解」與「殭屍」信仰的文獻依據
- [ ] 查證安第斯：帕拉卡斯墓地（Julio C. Tello, 1925–30）與 2021 年 *Current Biology* 同位素研究（顛倒屍與多元來源）、摩雪「西潘王墓」1987–96 發掘與墓中六名殉葬者、印加瓦卡（waca）與木乃伊崇拜
- [ ] 查證基督教：東正教「不腐」（ἀ-σηψία, a-saphthia）教義與實例（聖母瑪利亞、特羅伊基姆與塞拉菲姆、斯維爾斯克）、天主教「不腐聖人」與 Palermo 方濟各會墓穴地下墓室（1599–1877，約 4,000 具）
- [ ] 查證希臘：失去不死神飲（ambrosia／kleio）而致死的神話殘篇（Callimachus fr. 384 Schneider）、柏拉圖《斐多》對「身體腐爛＝靈魂被囚」的論述
- [ ] 查證斯堪的納維亞：泥炭沼澤屍（bog bodies）Borgund／Skeby／Tollund Man 的儀式性絞殺與「貴賓獻祭」三人公式；以及馬達加斯加 Sakalava 法馬迪哈納 (famadihana) 的遺骨重繃儀式（Bronwyn Douglas 1978）

**Commands:**

```bash
# 逐項搜尋後，把可引用事實寫入草稿；不使用任何自動抓站工具
```

## Task 3: 撰寫分析文章

- [ ] 建立 `analyses/incorrupt-corpse-undying-body-comparative.md`
- [ ] 結構（依 `analyses/human-classes-origin-myths-comparative.md` 的房內格式）：
  - `# 屍身不朽：身體防腐與靈魂之錨——「屍身不朽母題」的跨文化比較`
  - `## The Undying Body: Mummification and the Anchor of the Soul — A Cross-Cultural Comparative Analysis`
  - `### 摘要`
  - `### 一、引言：身體是靈魂的容器，還是靈魂的牢房？`
  - `### 二、不朽公式 U：母題解剖`（四命題：製成、保存劑、驗證程序、失竊／威脅者）
  - `### 三、跨文化對照表`（9 列 × 6 欄）
  - `### 四、個案分述`（4.1–4.9）
  - `### 五、分析：四不變式與第五項`
  - `### 六、與本站其他分析的關係`
  - `## 參考文獻`（`### 原始文獻` / `### 研究文獻`）
  - `### 相關條目`（`[[wiki-links]]`，對應 `speaking-relics-object-testimony-comparative`、`external-soul-life-token-comparative`、`reincarnation-metempsychosis`、`first-funeral-burial-rites-myths-comparative`、`straw-man-substitute-bodies-comparative`、`quests-for-immortality`…）
- [ ] 字數：≥3000 字（`AGENTS.md` 方式 C 要求 3000–5000 字）
- [ ] 每個個案至少一筆可驗證的出處（卷／章／編號／年份）
- [ ] 不可使用 `[[不存在的檔名]]`（CI 檢查內部連結）

**Run:**

```bash
cd /workspace/projects/mythos-atlas
python - <<'PY'
import pathlib, re
p = pathlib.Path('analyses/incorrupt-corpse-undying-body-comparative.md')
t = p.read_text(encoding='utf-8')
body = re.sub(r'\s', '', t)
print('chars(no-space):', len(body))
print('has_refs:', '## 參考文獻' in t)
print('simplified_hits:', re.findall(r'[这说个们对时间国东车马鸟龙]', t)[:5])
PY
```

Expected: `chars(no-space)` ≥ 9000（含英文專名）、`has_refs: True`、`simplified_hits: []`

## Task 4: 同步索引

- [ ] `analyses/README.md`：在字母序正確位置插入一行
  `- [Incorrupt Corpse Undying Body Comparative](incorrupt-corpse-undying-body-comparative.md)`
- [ ] `analysis-index.md`：
  - 標題行 `# 已分析母題索引（554 篇）` → `（555 篇）`
  - 表尾追加：
    `| 555 | incorrupt-corpse-undying-body-comparative.md | 屍身不朽：身體防腐與靈魂之錨——「屍身不朽母題」的跨文化比較（死者書卷「不死」咒與開啟聖口／卡與屍體／舍利的四法／馬王堆辛追與「尸解」「殭屍」／藏式不死灌頂與昌帕嘉措自製木乃伊／帕拉卡斯顛倒屍與西潘王墓殉者／東正教「不腐」與 Palermo 墓穴／沼澤屍的絞殺貴賓獻與 Sakalava 重繃遺骨／希臘失去神飲致死；不朽公式 U：製成＋保存劑＋驗證程序＋失竊者；四不變式：保存必須可見驗證、腐敗必須被指認為敵人、屍體必須被命名與繼承、保存使死者仍然在場、每一次不朽宣稱都出現在一次死亡觀的斷裂中） |`

**Run:**

```bash
cd /workspace/projects/mythos-atlas
grep -c "^| [0-9]" analysis-index.md   # 應為 555
```

## Task 5: 驗證

- [ ] 執行 `python scripts/ci_checks.py`
- [ ] 執行既有 enrichment 契約測試，確認未迴歸
- [ ] 確認 `git status` 只有預期的四個檔案

**Run:**

```bash
cd /workspace/projects/mythos-atlas
python scripts/ci_checks.py
python scripts/test_egyptian_enrichment.py
git status --porcelain
```

Expected: `✅  ALL CHECKS PASSED`；測試腳本回傳 0；`git status --porcelain` 只列出四個檔案

## Task 6: Commit

- [ ] 依 House Rules 步驟 1 先取得使用者明示同意後再 commit
- [ ] 未取得明示同意時，**只**回報待 commit 的檔案清單，不執行 `git commit`

**Commands:**

```bash
cd /workspace/projects/mythos-atlas
git add -A
git commit -m "mythos: analysis incorrupt-corpse-undying-body"
git push origin master
```

**git commit -a 用法說明:** 本次新增檔案（`analyses/incorrupt-corpse-undying-body-comparative.md`、本計畫檔）必須先 `git add`，`git commit -a` 不會納入未追蹤檔案；`analysis-index.md` 與 `analyses/README.md` 為已追蹤的修改。故需 `git add -A && git commit -m "mythos: analysis incorrupt-corpse-undying-body"`。

## Execution Handoff

**Plan complete and saved to `docs/superpowers/plans/2026-09-29-incorrupt-corpse-undying-body-analysis.md`. Two execution options:**

**1. Subagent-Driven (recommended)** - 每個 task 派發全新的 subagent，task 之間做兩階段審查

**2. Inline Execution** - 在本 session 內以 executing-plans 分批執行並設置檢查點

**Which approach?**
