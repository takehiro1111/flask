from datetime import datetime
from crud.apps.app import db
from werkzeug.security import generate_password_hash
from flask_migrate import Migrate

# db.Modelを継承するUserクラスの作成
class User(db.Model):
  # テーブル名を定義する
  __tablename__ = "users"
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String,index=True)
  email = db.Column(db.String,unique=True,index=True)
  password_hash = db.Column(db.String)
  created_at = db.Column(db.DateTime,default=datetime.now)
  updated_at = db.Column(db.DateTime,default=datetime.now,onupdate = datetime.now)
  
  # パスワードをセットするためのプロパティ
  @property
  def password(self):
    raise AttributeError('読み取り出来ません。')
  
  # パスワードをセットするためのセッター関数でハッシュ化したパスワードをセットする。
  @password.setter
  def password(self,password):
    self.password_hash = generate_password_hash(password)
