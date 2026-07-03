# 資料管線：Mythos Atlas → Godot

## 轉換策略
不在執行階段解析 `_catalog.json`。而是在建置時用 Python 腳本從 markdown + JSON 資料生成 Godot `.tres`（文字資源）檔案。

## 管線

_catalog.json ─┐
cultures/*.md ─┼──► build_civ_data.py ──► resources/civ_data/ ──► civ_{id}.tres
themes/*.md  ──┘                        ├── resources/tech_tree/ ──► tech_{id}.tres
analyses/*.md ───► build_quest_data.py ──┴── resources/quests/ ──► quest_{id}.tres

## Godot .tres 範例

[gd_resource type=Resource script=ext:RaceData]
[resource]
script = ResourceScript("res://scripts/data/RaceData.gd")
id = "chinese"
name = "中國上古神話"
name_en = "Chinese Mythology"
region = "East Asia"
unique_ability = "龍脈"
unique_unit = "Yinglong"
unique_building = "Kunlun Altar"
patron_gods = ["nuwa", "huangdi", "shennong", "dayu"]
start_bias = { "river": 10, "plains": 8 }

## 建置腳本

| 腳本 | 輸入 | 輸出 |
|------|------|------|
| tools/build_civ_data.py | _catalog.json + cultures/{id}/gods/*.md | 每文明 .tres + CivIndex.tres |
| tools/build_tech_tree.py | themes/*.md | TechTree.tres |
| tools/build_quests.py | cultures/{id}/stories/*.md + analyses/*.md | 任務 .tres |
| tools/build_civilopedia.py | 所有 markdown | CivilopediaEntries.tres |
