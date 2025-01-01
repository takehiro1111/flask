
from email_validator import EmailNotValidError, validate_email
import logging
from flask_debugtoolbar import DebugToolbarExtension 
import os
from flask import (
  Flask,
  render_template,
  url_for,
  current_app,g,
  redirect,
  request,
  flash,
  make_response,
  session
)
from flask_mail import Mail,Message
import my_gmail_account
import smtplib, ssl
from email.mime.text import MIMEText

send_address = my_gmail_account.account

# インスタンス化
app = Flask(__name__)

app.config.update(
    SECRET_KEY='testtesttest',  # 環境変数を使わず直接設定
    DEBUG=True
)

# アプリケーションコンテキストの実行環境を有効化
ctx=app.app_context()
ctx.push()

print(current_app.name)

g.connection = "connection"
print(g.connection)

# hello world用のcontextのためコメントアウト
# with app.test_request_context():  
#   print(url_for("hello",name="takehiro1111"))

# test_request_context -> 擬似リクエストしてくれるメソッド
with app.test_request_context("/users?updated=true"):
  print(request.args.get("updated"))
  
# ロギング
app.logger.setLevel(logging.DEBUG)
app.logger.debug("Debug Logger")

# デバッグツール
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)

# Mailクラスのconfigを追加
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_POST"] = os.environ.get("MAIL_POST")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

# flask-mail拡張の登録
mail = Mail(app)

################################################
# Hello World
################################################
@app.get('/')
def index():
  return 'Hello  Flaskbook'

# # endpointを指定しない場合は関数名がendpointになる。
# @app.route('/index',
#           methods=["GET"],
#           endpoint="hello-endpoint")
# def index():
#   return render_template('index.html')

# @app.get('/hello/<string:name>')
# def hello(name):
#   return render_template('index.html',name=name)

# @app.get('/name/<string:name>')
# def show_name(name):
#   name='takehiro1111'
#   return render_template('index.html',name=name)

######################################################
# form
######################################################
@app.get('/contact')
def contact():
  # レスポンスオブジェクトを取得する。
  response = make_response(render_template("contact.html"))
  
  # クッキーを設定する。
  response.set_cookie("key_test", "takehiro1111")
  
  # セッションの設定
  session["username"] = "ichiro"
  
  # レスポンスオブジェクトを返す
  return response
  
  # return render_template('contact.html')

@app.route('/contact/complete',
          methods=["GET","POST"])
def contact_complete():
  if request.method == "POST":
    username = request.form["username"]
    email = request.form["email"]
    description = request.form["description"]
    
    is_valid = True
    if not username:
      flash('ユーザー名は必須です。')
      is_valid = False
      
    elif not email:
      flash('メールアドレスは必須です。')
      is_valid = False
      
    try:
      validate_email(email)
    except EmailNotValidError as e:
      flash(f"{e}:正しいメールアドレスの形式で入力してください。")
      is_valid = False
      
    if not description:
      flash(f"問い合わせ内容は必須です。")
      is_valid = False
  
    elif not is_valid:
      return redirect(url_for("contact"))
  
  # メールを送信する処理の実装
    # send_email(
    #   email,
    #   "お問い合わせありがとうございます。",
    #   "contact_mail",
    #   username=username,
    #   description=description
    # )
    send_test_email()

    flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございます。")
    return redirect(url_for("contact_complete"))
  return render_template("contact_complete.html")

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error(f'Server Error: {e}')
    return 'Internal Server Error from Logger', 500
  
# def send_email(to,subject,template,**kwargs):
#   """
#   for mail send function
#   """
#   msg = Message(subject,recipients =[to])
#   msg.body = render_template(f"{template}.txt",**kwargs)
#   msg.html = render_template(f"{template}.html",**kwargs)

  
# メインの関数になります
def send_test_email():
  msg = make_mime_text(
    mail_to = send_address,
    subject = "テスト送信",
    body = "Pythonでのメール送信です"
  )
  send_gmail(msg)

# 件名、送信先アドレス、本文を渡す関数です
def make_mime_text(mail_to, subject, body):
  msg = MIMEText(body, "html")
  msg["Subject"] = subject
  msg["To"] = mail_to
  msg["From"] = send_address
  return msg

# smtp経由でメール送信する関数です
def send_gmail(msg):
  server = smtplib.SMTP_SSL(
    "smtp.gmail.com", 465,
    context = ssl.create_default_context())
  server.set_debuglevel(0)
  server.login(send_address, my_gmail_account.password)
  server.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)
