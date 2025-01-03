from flask import Blueprint,render_template

# Blueprintを使用してauthを生成する。
auth = Blueprint(
  "auth",
  __name__,
  template_folder="templates",
  static_folder="static"
)

@auth.route("/")
def index():
  return render_template("auth/index.html")
