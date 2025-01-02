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
  db.session.query(User).all()
  return "コンソールログを確認してください"
