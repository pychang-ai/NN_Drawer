# ニューラルネットワークアーキテクチャ可視化ツール

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md)

このリポジトリには、TikZとLaTeXを使用してニューラルネットワークアーキテクチャを可視化するためのツールと例が含まれています。出版品質のニューラルネットワークアーキテクチャ図を作成するための専門的な方法を提供します。

## 特徴

- 美しくカスタマイズ可能なニューラルネットワークアーキテクチャの可視化
- 様々な層タイプ（Conv、Pool、FC等）のサポート
- 図を生成するための使いやすいPythonインターフェース
- 複数のアーキテクチャ例を含む

## 例

このリポジトリには、以下の人気のあるニューラルネットワークアーキテクチャの可視化が含まれています：

- PSPNet（Pyramid Scene Parsing Network）
- U-Net
- DeepLabV3+
- カスタムCNNアーキテクチャ

## 必要条件

- Python 3.x
- LaTeX配布（MiKTeXまたはTeX Live等）
- 必要なPythonパッケージ：
  - graphviz
  - python-graphviz
  - numpy
  - matplotlib

## 使用方法

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

## ディレクトリ構造

- `layers/`：LaTeXスタイルファイルと基本的なビルディングブロックを含む
- `pycore/`：ネットワーク図を生成するためのPythonコアユーティリティ
- `pyexamples/`：ネットワークアーキテクチャの実装例
  - `pspnet.py`：PSPNetの実装
  - `unet.py`：U-Netの実装
  - `deeplabv3plus.py`：DeepLabV3+の実装
  - `custom_cnn.py`：カスタムCNNの例

## 貢献

以下の方法で貢献できます：
1. バグや機能リクエストのissueを開く
2. 改善のためのプルリクエストを提出
3. 新しいネットワークアーキテクチャの例を追加

## ライセンス

このプロジェクトはMITライセンスの下で提供されています - 詳細はLICENSEファイルを参照してください。

## 謝辞

このプロジェクトはPlotNeuralNetフレームワークをベースにし、追加の機能と例を加えて拡張されています。
