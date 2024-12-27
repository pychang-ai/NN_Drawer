# Neural Network Architecture Visualization / 神經網絡架構可視化工具 / ニューラルネットワークアーキテクチャ可視化ツール

<div align="center">

[English](docs/README.md) | [中文](docs/README.zh.md) | [日本語](docs/README.ja.md)

</div>

<a name="english"></a>
## English

This repository contains tools and examples for visualizing neural network architectures using TikZ and LaTeX. It provides a clean and professional way to create publication-quality neural network architecture diagrams.

### Features

- Beautiful and customizable neural network architecture visualization
- Support for various layer types (Conv, Pool, FC, etc.)
- Easy-to-use Python interface for generating diagrams
- Multiple example architectures included

### Examples

The repository includes visualizations for several popular neural network architectures:

- PSPNet (Pyramid Scene Parsing Network)
- U-Net
- DeepLabV3+
- Custom CNN architectures

### Requirements

- Python 3.x
- LaTeX distribution (e.g., MiKTeX or TeX Live)
- Required Python packages:
  - graphviz
  - python-graphviz
  - numpy
  - matplotlib

### Usage

1. Clone the repository:
```bash
git clone https://github.com/pychang-ai/NN_Drawer.git
cd NN_Drawer/PlotNeuralNet
```

2. Check the examples in the `pyexamples` directory:
```bash
cd pyexamples
python pspnet.py  # Generates PSPNet architecture
python unet.py    # Generates U-Net architecture
```

3. Create your own architecture:
- Copy one of the example files
- Modify the network structure according to your needs
- Run the Python script to generate the diagram

---

<a name="中文"></a>
## 中文

這個倉庫包含了使用 TikZ 和 LaTeX 來可視化神經網絡架構的工具和示例。它提供了一種創建出版品質的神經網絡架構圖的專業方式。

### 功能特點

- 美觀且可自定義的神經網絡架構可視化
- 支持各種層類型（卷積層、池化層、全連接層等）
- 易於使用的 Python 接口來生成圖表
- 包含多個示例架構

### 示例

本倉庫包含了幾個流行的神經網絡架構的可視化：

- PSPNet（金字塔場景解析網絡）
- U-Net
- DeepLabV3+
- 自定義 CNN 架構

### 環境要求

- Python 3.x
- LaTeX 發行版（如 MiKTeX 或 TeX Live）
- 需要的 Python 包：
  - graphviz
  - python-graphviz
  - numpy
  - matplotlib

### 使用方法

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

---

<a name="日本語"></a>
## 日本語

このリポジトリには、TikZとLaTeXを使用してニューラルネットワークアーキテクチャを可視化するためのツールと例が含まれています。出版品質のニューラルネットワークアーキテクチャ図を作成するための専門的な方法を提供します。

### 特徴

- 美しくカスタマイズ可能なニューラルネットワークアーキテクチャの可視化
- 様々な層タイプ（Conv、Pool、FC等）のサポート
- 図を生成するための使いやすいPythonインターフェース
- 複数のアーキテクチャ例を含む

### 例

このリポジトリには、以下の人気のあるニューラルネットワークアーキテクチャの可視化が含まれています：

- PSPNet（Pyramid Scene Parsing Network）
- U-Net
- DeepLabV3+
- カスタムCNNアーキテクチャ

### 必要条件

- Python 3.x
- LaTeX配布（MiKTeXまたはTeX Live等）
- 必要なPythonパッケージ：
  - graphviz
  - python-graphviz
  - numpy
  - matplotlib

### 使用方法

1. リポジトリをクローン：
```bash
git clone https://github.com/pychang-ai/NN_Drawer.git
cd NN_Drawer/PlotNeuralNet
```

2. `pyexamples`ディレクトリの例を確認：
```bash
cd pyexamples
python pspnet.py  # PSPNetアーキテクチャを生成
python unet.py    # U-Netアーキテクチャを生成
```

3. 独自のアーキテクチャを作成：
- 例のファイルをコピー
- 必要に応じてネットワーク構造を修正
- Python スクリプトを実行して図を生成

---

## Directory Structure / 目錄結構 / ディレクトリ構造

- `layers/`: Contains LaTeX style files and basic building blocks / 包含 LaTeX 樣式文件和基本構建塊 / LaTeXスタイルファイルと基本的なビルディングブロックを含む
- `pycore/`: Core Python utilities / Python 核心工具 / Pythonコアユーティリティ
- `pyexamples/`: Example implementations / 示例實現 / 実装例
  - `pspnet.py`: PSPNet
  - `unet.py`: U-Net
  - `deeplabv3plus.py`: DeepLabV3+
  - `custom_cnn.py`: Custom CNN / 自定義 CNN / カスタムCNN

## License / 許可證 / ライセンス

MIT License - see the LICENSE file for details / 查看 LICENSE 文件了解詳情 / 詳細はLICENSEファイルを参照してください。

## Acknowledgments / 致謝 / 謝辞

Based on PlotNeuralNet framework with additional features and examples / 基於 PlotNeuralNet 框架，並增加了額外的功能和示例 / PlotNeuralNetフレームワークをベースに、追加の機能と例を加えて拡張

## Getting Started
1. Install the following packages on Ubuntu.
    * Ubuntu 16.04
        ```
        sudo apt-get install texlive-latex-extra
        ```

    * Ubuntu 18.04.2
Base on this [website](https://gist.github.com/rain1024/98dd4e2c6c8c28f9ea9d), please install the following packages.
        ```
        sudo apt-get install texlive-latex-base
        sudo apt-get install texlive-fonts-recommended
        sudo apt-get install texlive-fonts-extra
        sudo apt-get install texlive-latex-extra
        ```

    * Windows
    1. Download and install [MikTeX](https://miktex.org/download).
    2. Download and install bash runner on Windows, recommends [Git bash](https://git-scm.com/download/win) or Cygwin(https://www.cygwin.com/)

2. Execute the example as followed.
    ```
    cd pyexamples/
    bash ../tikzmake.sh test_simple
    ```

## TODO

- [X] Python interface
- [ ] Add easy legend functionality
- [ ] Add more layer shapes like TruncatedPyramid, 2DSheet etc
- [ ] Add examples for RNN and likes.

## Latex usage

See [`examples`](examples) directory for usage.

## Python usage

First, create a new directory and a new Python file:

    $ mkdir my_project
    $ cd my_project
    vim my_arch.py

Add the following code to your new file:

```python
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 512, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    to_connection( "pool1", "conv2"),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    to_connection("pool2", "soft1"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
```

Now, run the program as follows:

    bash ../tikzmake.sh my_arch
