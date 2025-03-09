import os

from flask import Flask, render_template, g, redirect, request
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Flaskアプリをログイン対象とするための紐付け。
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, userid):
        self.id = userid
        
@login_manager.user_loader
def load_user(userid):
    return User(userid)

# ログインしていない状態では常にログイン画面にリダイレクトされる。
@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    error_message = ""
    userid = ""
    
    if request.method == "POST":
        userid = request.form.get("userid")
        password = request.form.get("password")
        
        # 登録済みのパスワードの取得
        user_pw = get_db().execute(
            "select password from user where userid=?", [userid]
        ).fetchone()
        
        # パスワードの一致確認
        if user_pw and check_password_hash(user_pw[0], password):
            user = User(userid)
            login_user(user)
            return redirect("/")
        else:
            error_message = "入力されたIDまたはパスワードが誤っています。"
        
    return render_template("login.html", userid=userid, error_message=error_message)

# ログアウト時の挙動
@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect("/login")

DATABASE='flaskmemo.db'

@app.route("/signup", methods=["GET", "POST"])
def signup():
    error_message = ""
    if request.method == "POST":
        userid = request.form.get("userid")
        password = request.form.get("password")
        pw_hash = generate_password_hash(password, method = "pbkdf2:sha256")
        
        db = get_db()
        
        # useridが既にテーブル内で登録されていないか確認。
        user_check = db.execute("select userid from user where userid=?",[userid]).fetchall()
        
        if not user_check:
            db.execute("insert into user (userid,password) values(?,?)", [userid, pw_hash])
            db.commit()
            return redirect("/login")
        else:
            error_message = "登録済みのユーザーIDのため別のIDを入力してください。"
    
    return render_template("signup.html", error_message=error_message)

# database
def connect_db():
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, "sqlite.db"):
        g.sqlite_db = connect_db()
        
    return g.sqlite_db

# 表示
@app.route("/")
@login_required
def top():
    memo_list = get_db().execute(
        "select id, title, body from memo"
    ).fetchall()
    return render_template("index.html", memos=memo_list)

# 新規登録
@app.route("/regist", methods=["GET","POST"])
def regist():
    if request.method == "POST":
        # テーブルのカラムと紐づけている。
        title = request.form.get("title")
        body = request.form.get("body")
        
        db = get_db()
        db.execute("insert into memo (title,body) values(?,?)", [title,body])
        db.commit()
        return redirect('/')
        
    return render_template("regist.html")

# 編集画面
@app.route("/<id>/edit", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        # テーブルのカラムと紐づけている。
        title = request.form.get("title")
        body = request.form.get("body")
        db = get_db()
        db.execute("update memo set title=?,body=? where id=?", [title,body,id])
        db.commit()
        return redirect('/')
        
    post = get_db().execute(
        "select id, title, body from memo where id=?",(id)
    ).fetchone()   
    
    return render_template("edit.html", post=post)
    
#削除画面
@app.route("/<id>/delete", methods=["GET", "POST"])
def delete(id):
    if request.method == "POST":
        db = get_db()
        db.execute("delete from memo where id=?", (id))
        db.commit()
        return redirect('/')
        
    post = get_db().execute(
        "select id, title, body from memo where id=?",(id)
    ).fetchone()   
    
    return render_template("delete.html", post=post)


if __name__ == "__maine__":
    app.run()

# memo_list = [
#     {"title": "memo1", "content": "昨日"},
#     {"title": "memo2", "content": "今日"},
#     {"title": "memo3", "content": "明日"},
# ]

# country_list = [
#     "japan",
#     "america",
#     "france",
# ]
# new_country_list = [i.capitalize() for i in country_list]

# @app.route("/<name>")
# def hello_github_user(name):
#     return render_template(
#         "index.html", 
#         name=name, 
#         list=new_country_list
#     )


# @app.route("/<name>")
# def hello_user(name):
#     return f"<p>Hello! {name}</p>"


