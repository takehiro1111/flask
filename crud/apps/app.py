from flask import Flask,g,render_template
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import sys

# プロジェクトのルートディレクトリを動的に追加
from pathlib import Path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

flask_app = Flask(__name__)

# ORマッパーのインスタンス化
db = SQLAlchemy()
    

def create_app():
  from apps.crud import views  
  # register_blueprint関数を用いて、viewsのcrudをアプリへ登録する。
  flask_app.register_blueprint(views.crud,url_prefix="/crud")
  
  flask_app.config.from_mapping(
  SECRET_KET="testtest",
  SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'locals.sqlite'}",
  SQLALCGEMY_TRACK_MODIFICATIONS=False
)
  
  # SQLAlchemyのアプリの連携
  db.init_app(flask_app)
  
  # Migrateとアプリの連携
  Migrate(flask_app,db)
  
  return flask_app
  
# グローバルで設定。
app =create_app()

if __name__ == "__main__":
    app.run(debug=True)
