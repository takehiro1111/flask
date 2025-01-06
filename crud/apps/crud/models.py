from datetime import datetime
from apps.app import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_migrate import Migrate
from flask_login import UserMixin
from apps.detector.models import UserImage


# db.Modelを継承するUserクラスの作成
class User(db.Model,UserMixin):
  # テーブル名を定義する
  __tablename__ = "users"
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String,index=True)
  email = db.Column(db.String,unique=True,index=True)
  password_hash = db.Column(db.String)
  created_at = db.Column(db.DateTime,default=datetime.now)
  updated_at = db.Column(db.DateTime,default=datetime.now,onupdate = datetime.now)
  
  # backrefは「逆参照」を自動的に設定するため、片方のモデルでのみ定義すればもう片方(UserImage)では定義する必要がない。
  # order_byを用いることでidを降順で取得する。
  user_images = db.relationship("UserImage",backref="user",order_by="desc(UserImage.id)")
  
  # パスワードをセットするためのプロパティ
  @property
  def password(self):
    raise AttributeError('読み取り出来ません。')
  
  # パスワードをセットするためのセッター関数でハッシュ化したパスワードをセットする。
  @password.setter
  def password(self,password):
    self.password_hash = generate_password_hash(password)

  # パスワードのチェック
  def verify_password(self,password):
    return check_password_hash(self.password_hash,password)

  # メールアドレスに重複がないかチェックする。
  def is_duplicate_email(self):
    return User.query.filter_by(email=self.email).first() is not None

# ログイン中のユーザー情報を取得する関数を作成する。
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)
