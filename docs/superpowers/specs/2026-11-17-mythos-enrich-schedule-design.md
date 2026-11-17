# 設計：新增「MYTHOS 深化」排程（單頁／收尾，每日 2 次）

- **日期：** 2026-11-17
- **流程：** `superpowers/brainstorming`
- **核准狀態：** 已依流程完成澄清問題（意圖／push 死鎖／憑證／頻率）、做法提案（選 A）、設計第 1 段與第 2 段逐段核准。
- **範圍：** 建立新排程（寫 `cultures/**`）並設定 GitHub 憑證；**不修改**現有「MYTHOS 分析」排程。

## 一、探索專案脈絡

- 現有排程：`MYTHOS 分析 — 單篇/收尾（每日 2 次）`，ID `b8051618-cdd0-486e-9cf0-b685ba00d08c`，cron `0 1,13 * * *`（UTC 01:00/13:00 = 台北 09:00/21:00），`enabled=true`，scope `user:tg-915354960`，寫 `analyses/*.md`。
- 上傳設定（`Mythos_Atlas_深化_9914af6f.txt`）：ID `9914af6f-f636-47f1-8094-c724db3acb3b`，cron `0 2,8,14,20 * * *`，`enabled=False`，寫 `cultures/**`（gods/stories/comparisons）。與分析排程**工作類型不同、互補**。
- repo 實體：`/workspace/mythos-atlas`；上傳設定中的 `/workspace/projects/mythos-atlas` 不存在。
- git 狀態：工作樹乾淨；`HEAD=f720a125`、`origin/master=e1fcfc1e`，本地領先 1 commit。
- 環境實測：**無任何 GitHub 寫入憑證**（credential.helper / ~/.git-credentials / ~/.netrc / gh auth / GITHUB* env / ssh 執行檔皆無）；`git push` 回 `could not read Username`，exit 128。此為既有分析排程空轉的根因。
- 進度檔：分析排程用 `/workspace/.wukong/progress/mythos-analysis.md`；深化排程應另用 `mythos-enrich.md`（目前不存在）。
- `scripts/ci_checks.py` 的 `EXCLUDED_TOP_DIRS` 含 `docs`，故於 `docs/superpowers/specs/` 新增文件不影響 CI。

## 二、做法取捨

| 做法 | 內容 | 取捨 | 結果 |
|---|---|---|---|
| A（採用） | 新建排程 + 修正 prompt 缺陷 + 注入憑證 | 兼顧可用與穩健；需使用者給 token | ✅ |
| B | 照附件原樣建立（僅修路徑） | 最快，但沿用 `enabled=False` 與 push 死鎖，幾乎肯定空轉 | ❌ |
| C | 不建排程，改用 `schedule trigger` 手動觸發 | 不符「排程」需求 | ❌ |

## 三、選定設計

### 3.1 排程配置

```
name  MYTHOS 深化 — 單頁/收尾（每日 2 次）
cron  0 3,15 * * *        # UTC 03:00/15:00 = 台北 11:00/23:00
scope user:tg-915354960
model 預設（省略 --model）
```

- 與分析排程各差 2 小時（01→03、13→15）；兩者時間預算 18/20 分鐘，不重疊。
- 建立後確認 `enabled=true`；若 `add-turn` 預設停用，補 `wukong schedule enable --id <new-id>`。

### 3.2 prompt 修正（以上傳設定為底，最小改动）

1. 工作目錄與所有 `cd` 路徑：`/workspace/projects/mythos-atlas` → `/workspace/mythos-atlas`。
2. 第 2 步「殘留」明確定義：`git status --short` **有輸出（未提交修改）才算殘留；已 commit 的頁面不算**。避免重蹈分析排程「檔案存在就只收尾」的誤判而零產出。
3. 第 4 步補 push 失敗處理：push 失敗時記錄於進度檔並在後續輪次重試，**不因此判定為殘留或空轉**（憑證到位後自然成功）。
4. 第 5 步進度檔路徑：`/workspace/.wukong/progress/mythos-enrich.md`（不變）。
5. 其餘照原設定：12/20 分鐘時間預算、每頁 ≥300 字繁體中文、含跨文化對應與參考文獻、孤兒 `analyses/*.md` 補索引、`python3 scripts/ci_checks.py` 需 ALL PASSED、`git add -A && git commit -m "mythos: enrich <culture>" && git push`。

### 3.3 憑證機制

- 使用者稍後直接提供 token（repo scope）；由實作階段寫入 `~/.git-credentials`（`chmod 600`）並設 `credential.helper=store`。
- Token **不得**寫入排程 prompt、進度檔、任何 commit 或 artifacts。
- 先確認 HEAD 與 origin 現有 1 commit 落差補 push 成功，再建立／啟用排程，避免首次觸發即卡在舊 commit。

### 3.4 驗證

1. `GIT_TERMINAL_PROMPT=0 git push origin master` 成功。
2. `git rev-parse HEAD origin/master` 一致、`git status --short` 為空。
3. `wukong schedule list` 顯示新排程 `enabled=true`、cron `0 3,15 * * *`。
4. 首次觸發後 `wukong schedule runs` 出現執行紀錄，且 `mythos-enrich.md` 被寫入。

## 四、風險與不在範圍

- **既有分析排程仍空轉**：其 prompt 的「草稿存在就只收尾」歧義已造成連續 3 輪零產出。CLI 無 edit 指令，需 `rm` + `add-turn` 重建（ID 會變）。本次**不處理**，列為後續建議。
- 兩排程共用 repo，時段錯開 2h，寫入衝突風險低但非零。
- Token 到期／撤銷需使用者更新；新版 prompt 已容錯 push 失敗，不會回到空轉。
- 本 spec 先 commit 於本地，待憑證到齊後與既有 commit 一併 push。

## 五、轉換

本 spec 核准後，以 `superpowers/writing-plans` 產生實作計畫。
