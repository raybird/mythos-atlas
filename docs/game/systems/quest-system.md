# 神話任務系統

## 觸發來源
1. 發現 — 首次進入神話地形特徵
2. 里程碑 — 達到新時代
3. 事件鏈 — 來自文化 stories/ 目錄的故事任務
4. 全球事件 — 其他文明完成世界奇觀或達到終局

## 任務結構

{
  "id": "yu-flood-control",
  "title": "大禹治水",
  "culture": "chinese",
  "source_story": "cultures/chinese/stories/鯀禹治水.md",
  "source_analysis": "analyses/flood-myths-geological-origins.md",
  "phases": [
    {
      "id": "phase-1",
      "description": "河流氾濫，人民要求行動。",
      "objective": "在洪泛平原城市中有 3 個建造者次數可用",
      "reward": { "mythos": 10, "favor": {"大禹": 10} },
      "choice": [
        {"text": "築堤（生產力）", "effect": "消耗 2 建造者次數，對當前建築 +15 生產力"},
        {"text": "祈求大禹（神話）", "effect": "獲得 20 神話，大禹恩寵設為 15"}
      ]
    },
    {
      "id": "phase-2",
      "description": "大禹開鑿九條河道引水入海。",
      "objective": "沿境內河流改良 3 個地格",
      "reward": { "mythos": 15, "gold": 50 },
      "unlock": "應龍獨特單位 10 回合"
    },
    {
      "id": "phase-3",
      "description": "洪水退去，大禹成為夏朝開國君主。",
      "objective": "有 5+ 座城市擁有河流鄰接",
      "reward": { "mythos": 25, "great_person_points": {"engineer": 20} },
      "permanent_bonus": "所有沿河城市永久 +1 生產力"
    }
  ]
}

## 任務類別

| 類別 | 來源 | 獎勵特徵 |
|------|------|---------|
| 文明（每文明 3 個） | cultures/{id}/stories/ | 永久獨特加成 |
| 主題（全域，可重複） | analyses/ | 神話 + 隨機資源 |
| 世界事件（每局一次） | themes/world-ages-and-cycles.md | 時代定義加成 |
| 萬神殿（每神） | cultures/{id}/gods/ | 恩寵 + 領域加成 |
