# MYTHOS 深化排程 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 並行新增一條每天 2 次的「MYTHOS 深化」Wukong 排程，寫入 `cultures/**`，並設定 GitHub 憑證使 push 成功，避免重蹈既有分析排程的空轉。

**Architecture:** 三個獨立可驗證的交付：(1) repo 外的 git credential 設定並補 push 既有 2 個 commit；(2) Wukong schedule store 新增一筆 turn（prompt 內含 3 項修正）；(3) 驗證 schedule list / runs。不修改既有分析排程，不改動 repo 程式碼。

**Tech Stack:** Wukong CLI (`wukong schedule add-turn/list/enable/runs`)、git credential helper (`store`)、GitHub HTTPS remote。

## Global Constraints

- 工作專案實體路徑：`/workspace/mythos-atlas`；`/workspace/projects/mythos-atlas` 不存在，不得使用。
- 新排程 cron：`0 3,15 * * *`（UTC 03:00/15:00 = 台北 11:00/23:00）。
- scope：`user:tg-915354960`；model：省略 `--model`（用預設）。
- Token 不得寫入排程 prompt、進度檔、任何 commit 或 artifacts；不得以明文出現在 log。
- 既有分析排程 ID `b8051618-cdd0-486e-9cf0-b685ba00d08c` 不得更動。
- 所有 git 操作在 `/workspace/mythos-atlas` 執行。

---

### Task 1: 設定 GitHub 憑證並補 push 既有 commit

**Files:**
- Create: `~/.git-credentials`（repo 外）
- Modify: `~/.gitconfig`（repo 外，`credential.helper=store`）

**Interfaces:**
- Consumes: 使用者於執行時提供的 GitHub token（repo scope）。remote 使用者名稱由 remote URL 得悉為 `raybird`。
- Produces: `git push` 不再要求輸入帳密；`HEAD == origin/master` 且工作樹乾淨。Task 2/3 依賴此狀態。

- [ ] **Step 1: 確認目前阻斷狀態（基準）**

```bash
cd /workspace/mythos-atlas
GIT_TERMINAL_PROMPT=0 git push origin master
```
Expected: `fatal: could not read Username for 'https://github.com': terminal prompts disabled`，exit 128。

- [ ] **Step 2: 寫入 credential（token 由使用者提供，禁止 echo）**

```bash
printf 'https://raybird:%s@github.com\n' "$GH_TOKEN" > "$HOME/.git-credentials"
chmod 600 "$HOME/.git-credentials"
git config --global credential.helper store
```
`$GH_TOKEN` 由使用者於執行階段環境注入；此步驟不得印出變數值、不得寫入 repo。

- [ ] **Step 3: 驗證憑證生效並補 push**

```bash
cd /workspace/mythos-atlas
GIT_TERMINAL_PROMPT=0 git push origin master
git rev-parse HEAD origin/master
git status --short
```
Expected: push 成功；`git rev-parse` 兩行相同；`git status --short` 無輸出。

- [ ] **Step 4: 確認 CI 未被 spec commit 破壞**

```bash
cd /workspace/mythos-atlas && python3 scripts/ci_checks.py
```
Expected: `ALL CHECKS PASSED`，exit 0。

- [ ] **Step 5: Commit**

此 task 僅變更 repo 外設定，repo 內無新變更，無需 commit。既有 2 個 commit 已於 Step 3 push。

---

### Task 2: 建立「MYTHOS 深化」排程

**Files:**
- Create: `/tmp/opencode/mythos-enrich-prompt.md`（暫存，僅供 CLI 讀入）
- Modify: Wukong schedule store（透過 CLI，非直接改檔）

**Interfaces:**
- Consumes: Task 1 的 `HEAD == origin/master` 狀態；spec 第 3.1／3.2 節的設定值。
- Produces: 新排程 ID（後續 Task 3 使用）；排程 prompt 完整內容。

- [ ] **Step 1: 寫入暫存 prompt 檔（完整內容如下，逐字）**

```markdown
MYTHOS 深化 — 單頁/收尾（無人值守，每輪嚴守時間預算）。工作專案：/workspace/mythos-atlas

【第 1 步・接續】先讀 /workspace/.wukong/progress/mythos-enrich.md（可能不存在）。若記錄有未完成事項，優先續做該事項，不要重新研究。

【第 2 步・檢查工作目錄】cd /workspace/mythos-atlas && git status --short。上一輪逾時可能留下未提交修改，必須先處理：
- 判斷「殘留」的唯一標準是 git status --short 有輸出（未提交修改）。已 commit 的頁面即使尚未 push，也不算殘留，不得因此只收尾而不開新主題。
- 若有 cultures/** 未提交修改：本輪「只做收尾」、不開新主題。驗證已寫好的頁面（每頁 ≥300 字繁體中文、含「參考文獻」與跨文化對應段落）、確認各 README 與 _catalog.json 計數已同步、跑 python3 scripts/ci_checks.py 需 ALL PASSED。
- 若有 analyses/*.md 孤兒檔（非本排程產物）：在 analysis-index.md 補上索引列使其通過 orphan check，一併提交並在回報中註明。

【第 3 步・僅當無殘留時新增】依 _catalog.json 選頁數最少的文化，只新增 1 個頁面（gods/、stories/、comparisons/ 中頁數最少的那個目錄），≥300 字繁體中文，含跨文化對應與參考文獻；同步該目錄 README 與 _catalog.json 計數。

【第 4 步・驗證與交付】python3 scripts/ci_checks.py 必須 ALL PASSED → git add -A && git commit -m "mythos: enrich <culture>" && git push → 確認 HEAD==origin/master 且工作樹乾淨。若 push 失敗，記錄失敗原因於進度檔並在後續輪次重試；push 失敗不構成「殘留」，不得因此停止產出。

【時間預算・強制】開始後 12 分鐘內停止一切新增研究，轉入收尾；20 分鐘內必須完成 commit 與 push。時間不足就只交付已完成的部分，寧可少做不可不收尾。

【第 5 步・寫進度（不可省略）】無論完成到哪一步，都把「本輪排程名、文化/主題、已完成項目、驗證結果、下一步待辦」寫入 /workspace/.wukong/progress/mythos-enrich.md。最後回報成果、證據（commit hash、CI 結果、頁面字數）與待續事項。
```

- [ ] **Step 2: 確認 CLI 參數格式**

```bash
wukong schedule add-turn --help
```
Expected: 顯示必要參數 `--name --cron --scope --prompt`，選用 `--model`。

- [ ] **Step 3: 建立排程**

```bash
wukong schedule add-turn \
  --name 'MYTHOS 深化 — 單頁/收尾（每日 2 次）' \
  --cron '0 3,15 * * *' \
  --scope 'user:tg-915354960' \
  --prompt "$(< /tmp/opencode/mythos-enrich-prompt.md)"
```
Expected: 輸出新排程 ID（Record the ID as `NEW_ID`）。

- [ ] **Step 4: 確認啟用狀態，必要時補 enable**

```bash
wukong schedule list
```
Expected: 出現 `name=MYTHOS 深化 — 單頁/收尾（每日 2 次）`、`cron=0 3,15 * * *`、`enabled=true`。若為 `enabled=false`，執行：

```bash
wukong schedule enable --id "$NEW_ID"
wukong schedule list
```
Expected: 該列顯示 `enabled=true`。

- [ ] **Step 5: 確認既有分析排程未被更動**

```bash
wukong schedule list
```
Expected: `b8051618-cdd0-486e-9cf0-b685ba00d08c` 仍存在、`enabled=true`、`cron=0 1,13 * * *`。

- [ ] **Step 6: Commit**

此 task 變更 Wukong schedule store（CLI 管理）與 `/tmp` 暫存檔，repo 內無變更，無需 commit。

---

### Task 3: 驗證排程與交付

**Files:**
- Verify: Wukong schedule store、`/workspace/.wukong/progress/mythos-enrich.md`（由排程首次執行時產生）

**Interfaces:**
- Consumes: Task 2 的 `NEW_ID`。
- Produces: 可供使用者確認的驗證證據。

- [ ] **Step 1: 驗證排程清冊**

```bash
wukong schedule list
```
Expected: 兩筆排程皆存在且 `enabled=true`：分析 `0 1,13 * * *`、深化 `0 3,15 * * *`。

- [ ] **Step 2: 驗證排程執行政務**

```bash
wukong schedule runs
```
Expected: 尚未到首次觸發時間時無深化排程紀錄，屬正常。

- [ ] **Step 3: 驗證 repo 狀態**

```bash
cd /workspace/mythos-atlas && git rev-parse HEAD origin/master && git status --short
```
Expected: 兩行相同、工作樹乾淨。

- [ ] **Step 4: Commit**

無 repo 變更，無需 commit。首次觸發（台北 11:00 或 23:00）後由 `wukong schedule runs` 與 `mythos-enrich.md` 驗證端到端產出。

---

## Self-Review

- **Spec coverage：** 3.1 排程配置 → Task 2 Step 3–5；3.2 prompt 修正 → Task 2 Step 1（完整 prompt）；3.3 憑證 → Task 1；3.4 驗證 → Task 3；第四節風險（分析排程不修）→ Task 2 Step 5 確認未更動。
- **Placeholder scan：** 無 TBD/TODO；`$GH_TOKEN` 與 `$NEW_ID` 為執行期輸入／輸出，非待辦佔位。
- **Type consistency：** `NEW_ID` 於 Task 2 Step 3 產生、Step 4 與 Task 3 引用，名稱一致。
