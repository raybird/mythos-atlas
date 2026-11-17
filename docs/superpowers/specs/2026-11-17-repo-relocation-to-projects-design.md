# 設計：將 mythos-atlas 搬移至 /workspace/projects/

- **日期：** 2026-11-17
- **流程：** `superpowers/brainstorming`
- **核准狀態：** 已依流程完成動機澄清（單純集中管理）、三段設計逐段核准；使用者最終選擇做法 B（完整搬移），並核准順便修正分析排程的 push 死鎖。
- **範圍：** 搬遷 repo、更新路徑引用、重建兩條 Wukong 排程；**不處理** GitHub 憑證與 push。

## 一、現況探索（本輪實測）

- repo 實體：`/workspace/mythos-atlas`；`/workspace/projects` 不存在。
- git：`master`，工作樹乾淨，`HEAD=dcc0328a`，`origin/master=e1fcfc1e`（本地領先 3 個 commit，尚未 push）。remote 為 `https://github.com/raybird/mythos-atlas.git`。
- 兩條 active 排程：
  - `b8051618-cdd0-486e-9cf0-b685ba00d08c`：`MYTHOS 分析 — 單頁/收尾（每日 2 次）`，`0 1,13 * * *`，enabled，scope `user:tg-915354960`，prompt 檔 `/home/wukong/mythos-schedule-prompt.txt`。
  - `ebc56e89-59df-4349-8ff1-ace535c65723`：`MYTHOS 深化 — 單頁/收尾（每日 2 次）`，`0 3,15 * * *`，enabled，scope `user:tg-915354960`，prompt 檔 `/home/wukong/mythos-enrich-prompt.txt`。
  - 兩份 prompt 的第 1、5 行都硬編碼 `/workspace/mythos-atlas`；`wukong schedule runs` 目前皆為空。
- repo 內共 60 處 `/workspace/projects/mythos-atlas`：57 處是歷史 plan、故事中繼資料與 `scripts/convert_timelines.py:5`（舊路徑，目前失效）；另 3 處在 2026-11-17 的 spec/plan（描述「舊址不存在」）。
- 進度檔只有 `/workspace/.wukong/progress/mythos-analysis.md`，其中第 6、42 行含舊址；`mythos-enrich.md` 尚不存在。
- `scripts/ci_checks.py` 排除 `docs/`，因此改文件不影響 CI。

## 二、做法取捨

| 做法 | 內容 | 取捨 | 結果 |
|---|---|---|---|
| A | 留原地，只改 `convert_timelines.py` | 最小改動、零中斷 | 使用者否決 |
| B（採用） | 完整搬到 `/workspace/projects/mythos-atlas` + 更新引用 + 重建排程 | 目錄集中；需中斷排程、ID 會變 | ✅ |
| C | 建 symlink | 多一層間接，git/排程仍指舊址 | ❌ |

搬遷後 57 處舊路徑**自動變成正確**，因此不需要改寫歷史文件；只需更新 2 份 prompt、進度檔，以及 2026-11-17 兩份文件的 3 行路徑結論。

## 三、選定設計

### 3.1 搬遷與路徑

- 建立 `/workspace/projects/`，用 `mv /workspace/mythos-atlas /workspace/projects/mythos-atlas`；保留 `.git`、branch、commit 與工作樹狀態；不建立 symlink。
- canonical path 改為 `/workspace/projects/mythos-atlas`。
- `scripts/convert_timelines.py:5` 的 `REPO` **不改**：搬遷後自然指向正確位置。
- 更新 `/home/wukong/mythos-schedule-prompt.txt` 與 `/home/wukong/mythos-enrich-prompt.txt`：所有 `/workspace/mythos-atlas` → `/workspace/projects/mythos-atlas`。
- 更新 `/workspace/.wukong/progress/mythos-analysis.md` 第 6、42 行路徑。
- 更新以下 3 行的「舊址不存在」敘述（路徑字串本身不變，改為描述搬遷後狀態）：
  - `docs/superpowers/specs/2026-11-17-mythos-enrich-schedule-design.md:12` → `- repo 實體：\`/workspace/projects/mythos-atlas\`；此為 2026-11-17 搬遷後的 canonical path（先前實體在 \`/workspace/mythos-atlas\`）。`
  - `docs/superpowers/specs/2026-11-17-mythos-enrich-schedule-design.md:42` → `1. 工作目錄與所有 \`cd\` 路徑：統一為 \`/workspace/projects/mythos-atlas\`（2026-11-17 已搬遷）。`
  - `docs/superpowers/plans/2026-11-17-mythos-enrich-schedule.md:13` → `- 工作專案實體路徑：\`/workspace/projects/mythos-atlas\`（2026-11-17 搬遷後）；\`/workspace/mythos-atlas\` 已不存在。`
- 其餘 57 處歷史路徑保留原樣，搬到新址後即為有效路徑。

### 3.2 排程重建

CLI 無 edit，必須 disable → rm → add-turn；新 ID 無法保留，名稱／cron／scope／模型維持不變。

1. 先 `wukong schedule disable --id b8051618-cdd0-486e-9cf0-b685ba00d08c` 與 `wukong schedule disable --id ebc56e89-59df-4349-8ff1-ace535c65723`，避免 13:00 UTC 分析排程在搬遷途中撞到舊路徑。
2. 完成 3.1 後 `wukong schedule rm` 兩條，再用更新後的 prompt 檔重新建立：
   - `wukong schedule add-turn --name 'MYTHOS 分析 — 單頁/收尾（每日 2 次）' --cron '0 1,13 * * *' --scope 'user:tg-915354960' --prompt "$(< /home/wukong/mythos-schedule-prompt.txt)"`
   - `wukong schedule add-turn --name 'MYTHOS 深化 — 單頁/收尾（每日 2 次）' --cron '0 3,15 * * *' --scope 'user:tg-915354960' --prompt "$(< /home/wukong/mythos-enrich-prompt.txt)"`
   - 省略 `--model`，沿用預設模型。
3. 分析 prompt 一併修正死鎖（與深化排程一致）：
   - 「殘留」唯一標準為 `git status --short` 有輸出（未提交修改）；已 commit 未 push 不算殘留。
   - push 失敗時記錄於進度檔並於後續輪次重試，不構成殘留、不停止產出。
   - 其餘行為（草稿先收尾、CI ALL PASSED、時間預算）保持原樣。
4. 用 `wukong schedule list` 驗證兩條新 ID 都 enabled、cron 正確、scope 正確；對新 ID 執行 `wukong schedule runs` 應為空。

### 3.3 驗證與回滾

驗證清單：
- `test -d /workspace/projects/mythos-atlas/.git` 通過，且 `/workspace/mythos-atlas` 不存在。
- `git -C /workspace/projects/mythos-atlas status --short` 為空；搬遷前 HEAD 為 `dcc0328a`，文件 commit 後 HEAD 為新 hash，`origin/master` 仍 `e1fcfc1e`。
- `python3 scripts/ci_checks.py` → `ALL CHECKS PASSED`，exit 0。
- 兩份 prompt 與進度檔中舊址 `/workspace/mythos-atlas` 字串數為 0；兩份 2026-11-17 文件中該字串僅出現在「已搬遷／先前實體」的歷史描述。
- `wukong schedule list` 顯示兩條新 ID、名稱不變、cron 不變、`enabled=true`、scope `user:tg-915354960`。

回滾：
- 動手前先備份兩份 prompt 與 `mythos-analysis.md` 到 `/workspace/.wukong/artifacts/user_tg-915354960/29`。
- 任一驗證失敗：`mv /workspace/projects/mythos-atlas /workspace/mythos-atlas` 還原；用備份還原 prompt／進度檔；repo 內 3 行文件變更若尚未 commit 用 `git checkout --` 還原，若已 commit 先 `git reset --soft HEAD^` 再 checkout（本 spec 的 commit 不回退）。
- 排程若已 rm，用備份 prompt 重新 add-turn（ID 再變一次）；若尚未 rm，用 `wukong schedule enable` 恢復。

### 3.4 產出與範圍

- repo 內 3 行文件變更本地 commit，訊息 `docs: update mythos schedule docs for repo relocation`；push 仍因無憑證失敗，屬已知限制。
- 搬遷報告、新舊排程 ID 對照、驗證輸出寫入 `/workspace/.wukong/artifacts/user_tg-915354960/29`。
- 範圍外：GitHub 憑證／push、57 處歷史路徑、文章內容、既有排程名稱／cron／scope。

## 四、風險

- 時程：分析排程 13:00 UTC、深化 15:00 UTC 觸發；必須在 13:00 前完成 disable，或移動後立刻重建。
- 排程 ID 改變：任何以舊 ID 查詢 `runs` 的腳本需改用新 ID。
- push 仍阻塞：新排程會在本地 commit，但遠端不會更新；憑證到位後需手動補 push 既有 commit（3 個既有 + 本 spec + 搬遷文件變更 = 5 個）。
- 兩排程共用 repo，時段錯開 2 小時，寫入衝突風險低但非零。

## 五、轉換

本 spec 經使用者審閱核准後，以 `superpowers/writing-plans` 產生逐步實作計畫，再依計畫執行搬遷。
