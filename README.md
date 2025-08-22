# 🧬 DSPBL化合物データ分析プロジェクト

分子特性予測による化合物データセット分析プロジェクトです。

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
1. `.ipynb` を開く
2. セルを上から順に実行
3. 結果を確認
```

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

## ⚠️ 重要な注意点

### 🚨 初回実行時
1. **大容量ファイル**: TSVファイル（19.8MB）は自分で追加
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

## 📊 GitHub操作ガイド

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
**A**: エポック数を減らしてください（100→30など）。

### Q: Gitでデータファイルが追跡されてしまう
**A**: `.gitignore`を確認してください。

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
