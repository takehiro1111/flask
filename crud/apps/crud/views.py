from flask import Flask,Blueprint , render_template
from apps.crud.models import User
from apps.app import db

crud = Blueprint(
  "crud",
  "__name__",
  template_folder = "templates",
  static_folder = "static"
)

@crud.route("/")
def index():
  return render_template("crud/index.html")

@crud.route("/sql")
def sql():
  db.session.query(User).paginate(
    page=2,      # ページ番号
    per_page=10,    # 1ページあたりの項目数
    error_out=False # ページが存在しない場合のエラー制御
  )
  return "コンソールログを確認してください"
