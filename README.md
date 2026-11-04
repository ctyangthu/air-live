# 台灣三大航空航班動態系統

把[長榮航空](https://ctyangthu.github.io/eva-live/)、[中華航空](https://ctyangthu.github.io/ci-live/)、[星宇航空](https://ctyangthu.github.io/jx-live/)三個航班動態系統合在同一張世界地圖上，依 2026/27 冬季班表（2026/10/25–2027/3/27）推算每一個航班的位置，並提供桃園、松山、清泉崗、高雄的出發／抵達看板、時刻表、航線網路與資料查核。

## 功能

- **六類航班可切換**：長榮、立榮、華航、華信、星宇（預設顯示），以及他航共掛（預設隱藏）。飛機與航班號依航空公司上色，航線依區域上色。
- **依日期套用班表**：每行記錄行駛星期與期間，各機場時區與日光節約時間由瀏覽器換算。
- **即時與模擬**：預設使用現在時間；可切換日期、拖曳時間軸（臺北時間），並以 1×–3600× 播放。前一兩天起飛、仍在空中的長程航班會繼續顯示。
- **地圖、航班詳情、看板、空中、時刻表、航點**：與三個單一航空系統相同。查詢班號時可不打航空代碼；同一個數字對應多家航空時，會改列在時刻表。
- **查核**：四座機場各類航班的每週班次與航點、這次查核補入的航班、查核範圍與限制。

## 限制

- 航班狀態與位置依表定時間推算（扣除約 14 分鐘滑行出發、6 分鐘滑行抵達，沿大圓航線移動），不含延誤、取消、改降等即時資訊；實際航路會因空域與風向繞行，兩岸航線尤其明顯。
- 三家的資料來源與完整度不同，各自的限制見單一航空系統的 README。共掛航班由他航排班，班期與時刻只是代表值。
- 本系統為非官方展示，與各航空公司無關，實際航班請以各航空公司公告為準。

## 專案結構

```
src/app.html            網頁原始碼（資料以佔位字串嵌入）
data/schedule-eva.txt   長榮班表（由 tools/sync.py 從 eva-live 複製）
data/schedule-ci.txt    華航班表（由 tools/sync.py 從 ci-live 複製）
data/schedule-jx.txt    星宇班表（由 tools/sync.py 從 jx-live 複製）
data/airports.json      三家合併的機場：中英文名稱、區域、座標、IANA 時區
data/map.json           投影並簡化後的陸地、國界與臺灣路徑
data/audit-notes.json   查核分頁的內容（手動維護）
tools/sync.py           複製三個專案的班表
tools/schedule.py       解析三份班表並判斷航班類別
tools/build.py          組出 dist/index.html
```

## 建置

```bash
python3 tools/build.py
```

產出的 `dist/index.html` 可直接用瀏覽器開啟。推送到 `main` 後，GitHub Actions 會自動建置並部署到 GitHub Pages。

單一航空的班表有更新時，先同步再建置（三個專案要放在這個專案的上一層目錄）：

```bash
python3 tools/sync.py
```

```bash
python3 tools/build.py
```

## 資料來源

- [長榮航空航班動態系統](https://github.com/ctyangthu/eva-live)、[中華航空航班動態系統](https://github.com/ctyangthu/ci-live)、[星宇航空航班動態系統](https://github.com/ctyangthu/jx-live)。
- 地圖：[world-atlas](https://github.com/topojson/world-atlas)（Natural Earth 1:50m，公有領域）。
