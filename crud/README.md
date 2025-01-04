# Flask CRUD Application
## Overview
このプロジェクトはFlaskを使用した基本的なCRUD（Create, Read, Update, Delete）アプリケーションです。ユーザー認証機能も実装しています。

## 機能
1. ユーザー登録
2. ログイン/ログアウト
3. ユーザー情報の表示
4. ユーザー情報の更新
5. データベースとの連携（SQLite）

## 必要要件
- Python 3.12以上
- その他の依存パッケージは、`requirements.txt`を参照

## インストール方法
### リポジトリのクローン
#### flask [リポジトリURL]
```bash
cd crud
```

#### 仮想環境の作成と有効化
- `requirements.txt`のインストール
```bash
python -m venv venv
source venv/bin/activate  # Unix/Linux
```

- `requirements.txt`の生成
```bash
# requirements.txt の生成（必要な場合）
# メインの依存関係管理は Pipenv で行う
pipenv lock -r > requirements.txt
```

#### 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

#### データベースの初期化
```bash
flask db upgrade
```

#### 起動方法
```bash
flask run --debug
```

> [!CAUTION]
> アプリケーションは http://127.0.0.1:5000 で実行されます。

## プロジェクト構造
```bash
╰─ tree -I '__pycache__'                                                                       ─╯
.
├── README.md
├── __init__.py
├── app.py
├── auth
│   ├── forms.py
│   ├── templates
│   │   └── auth
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── login.html
│   │       └── signup.html
│   └── views.py
├── config.py
├── crud
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── views.py
├── extensions.py
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── de90b56d73b0_.py
├── static
│   └── style.css
└── templates
    └── crud
        ├── base.html
        ├── create.html
        ├── edit.html
        ├── index.html
        └── migrate.html

10 directories, 26 files
```
## 開発環境
- Python 3.12
- Flask 3.1.0
- その他の詳細は `requirements.txt` を参照
