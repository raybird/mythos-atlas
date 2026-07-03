# 引擎選擇：Godot 4

## 比較

| 標準 | Godot 4 | Unity 6 | Unreal 5 |
|------|---------|---------|----------|
| 授權 | MIT（免費） | 每次安裝費用 | 5% 版稅 >100萬美元 |
| 2D/3D 混合 | 原生 2D + 3D | 好 | 對 4X 過度 |
| 回合制邏輯 | GDScript async/await | C# Task | C++/BP 重 |
| 六角格支援 | 內建 TileMapLayer | Tilemap + 自訂 | Blueprint 重 |
| Mod 支援 | .pck 檔案載入 | AssetBundle | Modding 框架 |
| Linux 建置 | 原生 | 好 | 原生 |
| 社群 4X 模板 | 成長中（無成熟套件） | 成熟（文明-like 複刻） | 多為 FPS/TPS |
| 學習曲線 | 低 | 中 | 高 |
| 檔案大小 | ~50MB | ~200MB | ~10GB+ |

**建議：** 回合制 4X 遊戲選擇 Godot 4，因為：
1. TileMapLayer 節點對六角格網格為一等支援
2. GDScript 信號完美匹配事件驅動回合結構
3. 無授權費用——對長期開發路線至關重要
4. .pck mod 支援社群內容擴展
5. Linux 原生建置（伺服器託管、Steam Deck）

## 潛在挑戰
- 無內建大型六角格尋路（將實作 A* 自訂啟發式）
- 無內建外交 AI（將使用加權評分效用 AI）
- 44+ 文明資源載入（將使用懶載入模式）
