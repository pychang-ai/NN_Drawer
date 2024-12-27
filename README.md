# 神經網絡架構可視化工具

這個倉庫包含了使用 TikZ 和 LaTeX 來可視化神經網絡架構的工具和示例。它提供了一種創建出版品質的神經網絡架構圖的專業方式。

## 功能特點

- 美觀且可自定義的神經網絡架構可視化
- 支持各種層類型（卷積層、池化層、全連接層等）
- 易於使用的 Python 接口來生成圖表
- 包含多個示例架構

## 示例

本倉庫包含了幾個流行的神經網絡架構的可視化：

- PSPNet（金字塔場景解析網絡）
- U-Net
- DeepLabV3+
- 自定義 CNN 架構

## 環境要求

- Python 3.x
- LaTeX 發行版（如 MiKTeX 或 TeX Live）
- 需要的 Python 包：
  - graphviz
  - python-graphviz
  - numpy
  - matplotlib

## 使用方法

1. 克隆倉庫：
```bash
git clone https://github.com/pychang-ai/NN_Drawer.git
cd NN_Drawer/PlotNeuralNet
```

2. 查看 `pyexamples` 目錄中的示例：
```bash
cd pyexamples
python pspnet.py  # 生成 PSPNet 架構
python unet.py    # 生成 U-Net 架構
```

3. 創建自己的架構：
- 複製一個示例文件
- 根據需要修改網絡結構
- 運行 Python 腳本生成圖表

## 目錄結構

- `layers/`：包含 LaTeX 樣式文件和基本構建塊
- `pycore/`：用於生成網絡圖的 Python 核心工具
- `pyexamples/`：網絡架構實現示例
  - `pspnet.py`：PSPNet 實現
  - `unet.py`：U-Net 實現
  - `deeplabv3plus.py`：DeepLabV3+ 實現
  - `custom_cnn.py`：自定義 CNN 示例

## 許可證

本項目採用 MIT 許可證 - 詳見 LICENSE 文件。

## 致謝

本項目基於 PlotNeuralNet 框架，並增加了額外的功能和示例。
