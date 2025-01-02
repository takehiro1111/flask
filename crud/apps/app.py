from flask import Flask,render_template
import views,app
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ORマッパーのインスタンス化
db = SQLAlchemy()

def create_app():
  
  # register_blueprint関数を用いて、viewsのcrudをアプリへ登録する。
  app.register_blueprint(views.crud,url_prefix="/crud")
  
  app.config.from_mapping(
  SECRET_KET="testtest",
  SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
  SQLALCGEMY_TRACK_MODIFICATIONS=False
)
  
  # SQLAlchemyのアプリの連携
  db.init_app(app)
  
  # Migrateとアプリの連携
  Migrate(app,db)
  
  return app
  
# flask runで実行されるようにグローバルで設定。
create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

app = create_app()
