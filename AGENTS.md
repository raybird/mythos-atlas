# Mythos Atlas — AI 協作指南

## 核心原則

- 所有文化條目必須提供：創世神話、洪水傳說、神系、核心母題、跨文化平行、重要故事
- 跨文化平行需標註具體對應關係（以 ↔ 連接）
- 每條資料必須引用原始文獻或口傳傳統來源
- 語言使用繁體中文，英文名稱括號標註

## 擴充方向優先級

1. **新文化**: 優先補充目前缺失的 major 文明（如羅馬、伊比利亞、西藏苯教細節）
2. **新主題**: 關注尚未覆蓋的跨文化母題（如 Trickster、英雄之旅、月神）
3. **分析文章**: 在 `analyses/` 中撰寫比較研究論文
4. **文獻索引**: 在 `references/` 中建立原始文獻與學術書目

## 工作流程

```bash
# 修改 _catalog.json 後，重新生成所有條目：
python3 regenerate_all.py

# 或僅增量新增 _catalog.json 中尚未生成檔案的條目：
python3 expand_catalog.py

# 或使用探索模式（推薦 — 自動輪替各種策略）：
python3 populate.py                    # 預設：自動探索
python3 populate.py --mode explore     # 明確指定探索模式
python3 populate.py --mode enrich      # 僅深化既有條目（生成神祇/故事/比較頁）
python3 populate.py --mode analyze     # 僅生成比較分析文章
python3 populate.py --mode new         # 僅生成新條目
python3 populate.py --mode ref         # 僅更新參考文獻
python3 populate.py --batch 3          # 一次處理多項
python3 populate.py --random           # 隨機選取

# 或使用永久排程（每小時自動探索）：
./daemon.sh
```

### 探索模式說明

- **new**: 從 `_catalog.json` 生成尚未建立的條目（原 populate.py 行為）
- **enrich**: 為既有條目深化內容 — 建立神祇子頁 (`gods/`)、故事子頁 (`stories/`)、跨文化比較子頁 (`comparisons/`)
- **analyze**: 在 `analyses/` 中產生比較神話學分析文章（如女神崇拜、冥界之旅、動物象徵等）
- **ref**: 更新 `references/` 中的跨文化參照矩陣
- **explore**: 自動判斷目前最需要的動作（預設模式）

`daemon.sh` 每小時自動輪替不同模式，每 4 次執行一次大規模批量。`--random` 旗標讓每次選擇更具隨機性，避免陷入單一路徑。

## 文化資料庫現狀

截至 2026-06-20，已收錄 44 個文化體系、26 個跨文化主題。

## 新增文化條目標準

```json
{
  "id": "culture-id",
  "name": "中文名稱",
  "name_en": "English Name",
  "region": "地理區域",
  "era": "歷史時期",
  "sources": ["原始文獻1", "原始文獻2"],
  "motifs": ["母題1", "母題2"],
  "parallels": [["本地概念", "跨文化對應"]],
  "creation": "創世神話段落...",
  "flood": "洪水傳說段落...",
  "pantheon": "神系列表...",
  "stories": ["故事1", "故事2"],
  "order": <number>
}
```

## 新增主題標準

```json
{
  "id": "theme-id",
  "name": "中文名稱",
  "name_en": "English Name",
  "cultures_covered": ["Culture1", "Culture2"],
  "key_observations": "關鍵觀察段落...",
  "order": <number>
}
```
