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
# 修改 _catalog.json 後，批次生成所有條目：
python3 expand_catalog.py

# 或使用原始逐步模式（每小時一條）：
./populate.sh
```

## 文化資料庫現狀

截至 2026-06-20，已收錄 34 個文化體系、20 個跨文化主題。

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
