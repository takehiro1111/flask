from flask import Blueprint,render_template,flash,url_for,redirect,request
from apps.auth.forms import SignUpForm
from flask_login import login_user,logout_user
from apps.crud.models import User
from apps.app import db
from apps.auth.forms import SignUpForm,LoginForm

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

@auth.route("/signup",methods = ["GET","POST"])
def signup():
    # SignUpFormクラスのインスタンス化
    form = SignUpForm()
    
    if form.validate_on_submit():
      user = User(
        username=form.username.data,
        email=form.email.data,
        password=form.password.data,
      )
      
      # メールアドレスの重複チェック
      if user.is_duplicate_email():
        flash("メールアドレスは登録済みで重複しています。")
        return redirect(url_for("auth.signup"))
      
      # ユーザー情報を登録する。
      db.session.add(user)
      db.session.commit()
      
      # ユーザー情報をセッションに格納する。
      login_user(user)
      
      # GETパラメータにnextキーが存在し、値がない場合はユーザーの一覧ページへリダイレクトする。
      ## サインアップ完了時のリダイレクト先をdetector_bp.indexに変更する。
      next_ = request.args.get("next")
      if next_ is None or not next_.startswith("/"):
        next_ = url_for("detector_bp.index")
        
      return redirect(next_)
    
    return render_template("auth/signup.html",form=form)

@auth.route("/login",methods = ["GET","POST"])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    # メールアドレスからユーザーを取得する。
    user = User.query.filter_by(email=form.email.data).first()
    
    # ユーザーが存在しパスワードが一致する場合はログインを許可する。
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      return redirect(url_for("detector_bp.index"))
    
    # ログイン失敗メッセージを設定する。
    flash("メールアドレスかパスワードが不正です。")
    
  return render_template("auth/login.html",form=form)

@auth.route("/logout",methods=["GET"])
def logout():
  logout_user()
  return redirect(url_for("auth.login"))
