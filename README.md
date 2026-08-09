# 割り勘計算ライブラリ：warikan
[![pytest](https://github.com/kinokonu/warikan/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/kinokonu/warikan/actions/workflows/test.yml)

支払い者と支払額が記載された辞書を渡すと、誰が誰に何円払えば差額を清算できるかを計算する Python ライブラリ・CLI ツールです。

---

## 📌 機能

- **Python ライブラリ**: `warikan()` 関数に支払額の辞書を渡すことで、精算結果（誰が誰にいくら支払うか）を取得できます。
- **CLI ツール**: ターミナル上で対話的に名前と金額を入力し、その場で割り勘結果を出力できます。

---

## 💻 使い方

### 1. Python ライブラリとして使う

自作スクリプトからインポートして利用できます。

```python
from warikan import warikan

# Aさんが5000円、Bさんが3000円、Cさんが10000円支払った場合
result = warikan({"A": 5000, "B": 3000, "C": 10000})
print(result)
# 出力例: 
# AさんがCさんに1000円支払う
# BさんがCさんに3000円支払う
```

### 2. CLI（コマンドラインツール）として使う

ターミナルで以下のコマンドを実行すると、対話形式で入力・計算が行えます。

```bash
uv run warikan
```

**実行イメージ:**
```text
=== 割り勘計算ツール ===
名前を入力してください (終了する場合は Enter のみ): 田中
田中 さんの支払額を入力してください: 5000
名前を入力してください (終了する場合は Enter のみ): 鈴木
鈴木 さんの支払額を入力してください: 2000
名前を入力してください (終了する場合は Enter のみ): 

--- 割り勘計算結果 ---
# 鈴木さんが田中さんに1500円支払う
```

---

## 🛠️ インストール・セットアップ

本プロジェクトではパッケージ管理に [uv](https://docs.astral.sh/uv/) を使用しています。

```bash
# リポジトリのクローン
git clone https://github.com/kinokonu/warikan.git
cd warikan

# 仮想環境構築 & 依存関係のインストール
uv sync
```

---

## 🧪 開発環境 & テスト

開発モードでの環境同期や、`pytest` によるテストの実行手順です。

```bash
# 依存関係の同期（開発用パッケージを含む）
uv sync

# テストの実行
uv run pytest
```

---

## 🔄 CI (Continuous Integration)

GitHub Actions を導入しており、コード変更時に自動でテストを実行しています。

- **ワークフロー定義**: `.github/workflows/test.yml`
- **実行タイミング**: `push` 時
- **実行プロセス**:
  1. `actions/checkout@v6` によるリポジトリコードの取得
  2. `astral-sh/setup-uv@v9.0.0` による `uv` 環境の自動構築
  3. `uv sync --locked` による `uv.lock` に基づいた再現性のある依存関係の検証・インストール
  4. `uv run pytest` による全テストケースの自動実行