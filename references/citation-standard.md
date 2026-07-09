# 資料來源追溯與引用規範

> 本文件定義 Mythos Atlas 專案的原始文獻引用標準。
> 目標：確保**每個條目至少包含 1 筆原始文獻引用**，且格式一致。

## 強制要求

| 條目類型 | 至少引用數 | 預期章節標題 | 備註 |
|---------|-----------|-------------|------|
| 神祇頁面 (`gods/*.md`) | 1 | `## 參考文獻` 或 `## 參考來源` | 可包含原始文獻 + 學術著作 |
| 故事頁面 (`stories/*.md`) | 1 | `## 參考文獻` | 必須標註故事來源 |
| 比較頁面 (`comparisons/*.md`) | 1 | `## 參考文獻` 或 `## 參考來源` | 至少 1 筆學術比較參考 |
| 分析文章 (`analyses/*.md`) | 3 | `## 參考文獻` 或 `### 參考文獻` | 至少 3 筆學術來源 |
| 主題頁面 (`themes/*.md`) | 1 | `## 參考文獻` 或 `## 參考來源` | 跨文化主題需支持來源 |

## 格式規範

### 原始文獻（Primary Sources）

```
- 《文獻名稱》．著者／時期
- *Title*．Author／Period
```

範例：

```
- 《山海經》．戰國—漢
- 《梨俱吠陀》/ Ṛgveda, 曼陀羅 10
- *Popol Vuh*．Maya creation epic
- *Prose Edda*, Gylfaginning．Snorri Sturluson, 13th c.
```

### 學術著作（Secondary Sources）

```
- 作者．《書名》(Title)．出版者，年份
- Author．*Title*．Publisher, Year
```

範例：

```
- 鍾敬文．〈蟾蜍、兔子和嫦娥〉．《鍾敬文民間文學論集》，上海文藝出版社，1990
- Eliade, M. *Patterns in Comparative Religion*. Sheed & Ward, 1958
- Campbell, J. *The Hero with a Thousand Faces*. Pantheon, 1949
```

### 期刊論文

```
- Author．"Article Title"．*Journal Name*, Vol(X), pp Y-Z, Year
```

範例：

```
- Thuillard, M. "A Statistical and Comparative Analysis of the 'Man or Animal in the Moon' Motif". *Folklore: Electronic Journal of Folklore*, 84, pp 87-110, 2021
```

## ⚠️ 常見缺失與修正指引

| 缺失狀況 | 修正方式 |
|---------|---------|
| 無 `## 參考文獻` 區塊 | 補上，列出至少 1 筆該條目內容的實際來源 |
| 只有維基百科 | 維基百科可作起點，但必須補 1 筆原始文獻或學術著作 |
| 引用不完整（無出版者/年份） | 補齊完整書目資訊 |
| 參考文獻與條目內容無關 | 確認每一筆引用確實與該條目的論述相關 |

## 自動化檢查

CI 流程中的 `scripts/ci_checks.py` 會自動檢查：

1. 每個條目是否包含 `## 參考文獻` 或 `## 參考來源`
2. 參考文獻區塊是否非空
3. 缺少引用者以 error 輸出

## 原始文獻總索引

各文化的原始文獻請參考：

- `references/primary-sources.md` — 按文化分類的原始文獻清單
- `references/secondary-sources.md` — 現代學術著作索引
