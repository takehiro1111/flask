from flask import Flask,g,render_template
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sys
from apps.extensions import db
from apps.crud.models import User
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

csrf = CSRFProtect()

# プロジェクトのルートディレクトリを動的に追加
from pathlib import Path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

flask_app = Flask(__name__)

# # ORマッパーのインスタンス化
# db = SQLAlchemy()

# loginmanagerをインスタンス化する。
login_manager = LoginManager()
# login_view属性に未ログイン時にリダイレクトするエンドポイントを指定する。
login_manager.login_view = "auth.signup"
# login_message属性にログイン後に表示するメッセージを指定する。
login_manager.login_message = ""

def create_app():
  
  flask_app.config.from_mapping(
    SECRET_KEY="testtest",
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'locals.sqlite'}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO = True,
    WTF_CSRF_SECRET_KEY="testtest"
  )
  csrf.init_app(flask_app)
  
  # SQLAlchemyのアプリの連携
  db.init_app(flask_app)
  
  # Migrateとアプリの連携
  Migrate(flask_app,db)
  
  # アプリケーションコンテキスト内でBlueprintを登録
  with flask_app.app_context():
    from apps.crud.views import crud
    # register_blueprint関数を用いて、viewsのcrudをアプリへ登録する。
    flask_app.register_blueprint(crud,url_prefix="/crud")
    
    # user = User(
    #   username = "user2",
    #   email = "tttttgggsssssggg@gmail.com",
    #   password = "flaskbook2"
    # )
    # db.session.add(user)
    # db.session.commit()
    
    user = db.session.query(User).filter_by(id=1).first()
    if user:
      user.username = "user2"
      user.email = "fffffffsddsddsfa@gmail.com"
      user.password = "flaskbook2"
      db.session.add(user)
      db.session.commit()
  
  # login_managerをアプリケーションと連携する。
  login_manager.init_app(flask_app)
  from apps.auth import views as auth_views
  flask_app.register_blueprint(auth_views.auth,url_prefix="/auth")
  
  return flask_app


# グローバルで設定。
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
