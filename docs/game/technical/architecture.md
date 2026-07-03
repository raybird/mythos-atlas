# Godot 架構

## 場景樹

Root (GameManager - AutoLoad)
├── World (Node2D 等距視角)
│   ├── HexMap (TileMapLayer)
│   │   ├── TerrainLayer
│   │   ├── FeatureLayer
│   │   └── DecorationLayer
│   ├── Units (Node2D)
│   │   ├── CivilianUnits
│   │   └── MilitaryUnits
│   ├── Cities (Node2D)
│   │   ├── City_{id}
│   │   └── Districts
│   └── FX (Node2D)
│       ├── FogOfWar
│       └── Animations
├── UI (CanvasLayer)
│   ├── HUD (TopBar + BottomBar)
│   ├── CityView (popup)
│   ├── TechTree (fullscreen)
│   ├── PantheonScreen
│   ├── DiplomacyPanel
│   ├── QuestLog
│   └── Civilopedia
└── Managers (AutoLoads)
    ├── TurnManager — 編排階段轉換
    ├── CombatManager — 解決戰鬥
    ├── DiplomacyManager — AI 決策、關係變更
    ├── MythosManager — 恩寵追蹤、神祇狀態、神聖事件
    ├── QuestManager — 追蹤活躍/已完成任務
    ├── EraManager — 時代進度追蹤
    └── AIController — 每文明效用 AI

## AutoLoad 單例

| 單例 | 職責 |
|------|------|
| GameManager | 遊戲狀態、存檔/讀檔、回合管理 |
| DataCache | 記憶體資源快取（文明資料、科技樹、任務） |
| EventBus | 解耦系統之間的信號轉發 |
| HexGrid | 網格數學、尋路、視野 |
| ResourcePool | 產出計算、資源追蹤 |
| AIController | 中央 AI 決策協調 |

## 信號流（回合階段）

TurnManager.start_edict_phase()
  → EventBus.emit("phase_changed", "edict")
  → HUD.update_phase_indicator()
  → AIController.decide_edicts()

TurnManager.start_divine_phase()
  → MythosManager.accumulate_favor()
  → MythosManager.check_god_mood()
  → EventBus.emit("divine_events", events)
  → QuestManager.check_triggers()
