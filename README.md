# 🧬 DSPBL化合物データ分析プロジェクト

ChemPropを用いた分子特性予測による化合物データセット分析プロジェクトです。

## 📋 プロジェクト概要

### 🎯 目的
- 化合物のSMILES構造から阻害値（Inhibition）を予測
- ChemPropライブラリによる深層学習アプローチ
- 従来手法（Random Forest）との性能比較

### 📊 データセット
- **ファイル**: `starderdized_compounds_20240725.tsv`
- **化合物数**: 2,941個（有効データ2,289個）
- **特徴量**: SMILES構造、化合物名、薬物分類、阻害値

## 🚀 クイックスタート

### 1️⃣ リポジトリのクローン
```bash
git clone https://github.com/your-username/DSPBL.git
cd DSPBL
```

### 2️⃣ 環境構築
```bash
# 必要ライブラリのインストール
pip install chemprop rdkit pandas numpy matplotlib seaborn scikit-learn

# Jupyter Notebookで実行
jupyter notebook
```

### 3️⃣ 分析実行
1. `Chemprop_test_reorganized.ipynb` を開く
2. セルを上から順に実行
3. 結果を確認

## 📁 ファイル構成

```
DSPBL/
├── README.md                          # このファイル
├── .gitignore                         # Git除外設定
├── Chemprop_test_reorganized.ipynb    # 📊 メイン分析ノートブック
├── 化合物データセット分析レポート.md    # 📄 データセット詳細分析
├── starderdized_compounds_20240725.tsv # 🧬 化合物データ（※除外対象）
└── PBL_dataset.csv                     # 🗂️ 変換済みデータ（※除外対象）
```

## 📊 ノートブック実行手順

### 🔄 実行順序（重要！）
ノートブックは**必ず上から順番に**実行してください：

1. **ライブラリインストール** → ChemProp環境構築
2. **データ読み込み** → TSVファイルの前処理
3. **データ準備** → 訓練/テスト分割
4. **基本版ChemProp** → ベースライン性能確認
5. **改善版・記述子強化版** → 精度向上手法

### ⏱️ 実行時間の目安
- **基本版ChemProp**: 5-10分
- **記述子強化版**: 10-20分
- **改善版（アンサンブル）**: 30-60分 ⚠️

## 🤖 ChemPropについて

### 💡 ChemPropとは？
- **深層学習**による分子特性予測ライブラリ
- **グラフニューラルネットワーク**でSMILES構造を学習
- ハーバード大学で開発、**Nature**などトップジャーナルで使用

### 🧠 技術的特徴
- **Message Passing Neural Networks (MPNN)**: 分子グラフ構造を直接学習
- **従来手法との違い**: 分子記述子不要、SMILES構造から直接予測
- **高精度**: 化学構造と活性の複雑な関係を学習可能

## 📈 期待される結果

### 🎯 性能指標
- **RMSE (Root Mean Square Error)**: 予測誤差の大きさ
- **R² (決定係数)**: 予測精度（1.0に近いほど高精度）
- **MAE (Mean Absolute Error)**: 平均絶対誤差

### 📊 ベンチマーク結果（例）
| 手法 | RMSE | R² | 実行時間 |
|------|------|-----|----------|
| Random Forest | 0.247 | -0.0001 | 1分 |
| ChemProp基本版 | 0.202 | 0.327 | 10分 |
| ChemProp記述子強化版 | 0.180 | 0.450 | 20分 |

## ⚠️ 重要な注意点

### 🚨 初回実行時
1. **大容量ファイル**: TSVファイル（19.8MB）は初回ダウンロード必要
2. **計算時間**: ChemProp訓練は時間がかかります
3. **メモリ使用量**: 2GB以上のメモリを推奨

### 🔧 トラブルシューティング
```python
# ChemPropインストールエラー
pip install --upgrade pip
pip install chemprop

# RDKitインストールエラー  
conda install -c conda-forge rdkit
```

## 📊 GitHub操作ガイド（初心者向け）

### 🌟 基本操作
```bash
# 最新コードを取得
git pull origin main

# 変更をコミット
git add .
git commit -m "分析結果を追加"
git push origin main
```

### 📁 ファイル管理のルール
- **✅ 含める**: コード（.py, .ipynb）、ドキュメント（.md）
- **❌ 含めない**: データファイル（.csv, .tsv）、モデル（chemprop_*/）
- **自動除外**: `.gitignore`で設定済み

### 🤝 チーム作業
1. **作業前**: `git pull` で最新版を取得
2. **コミット**: 意味のある単位で変更をまとめる
3. **メッセージ**: 何を変更したかを日本語で記載

## 🆘 よくある質問

### Q: ノートブックがエラーになる
**A**: セルを上から順番に実行してください。途中から実行するとエラーになります。

### Q: ChemPropの訓練に時間がかかりすぎる
**A**: エポック数を減らしてください（100→30など）。記述子強化版は軽量化済みです。

### Q: Gitでデータファイルが追跡されてしまう
**A**: `.gitignore`で除外設定済みです。`git status`で確認してください。

### Q: 結果の解釈方法がわからない
**A**: `化合物データセット分析レポート.md`に詳しい説明があります。

## 📚 参考文献

1. **ChemProp論文**: Yang et al., "Analyzing Learned Molecular Representations for Property Prediction" (2019)
2. **深層学習創薬**: Stokes et al., "A Deep Learning Approach to Antibiotic Discovery" Cell (2020)
3. **SMILES記法**: Weininger, D. "SMILES, a chemical language" (1988)

## 🤝 貢献・質問

- **Issues**: バグ報告や機能要望は[GitHub Issues](https://github.com/your-username/DSPBL/issues)へ
- **討論**: 分析結果の解釈や手法について議論しましょう
- **改善提案**: より良い分析手法のアイデアを共有してください

---

## 🔗 クイックリンク

- [ChemProp公式ドキュメント](https://chemprop.readthedocs.io/)
- [RDKit公式サイト](https://www.rdkit.org/)
- [Jupyter Notebook使い方](https://jupyter-notebook.readthedocs.io/)

**🚀 Happy Analyzing! 分析を楽しんでください！**