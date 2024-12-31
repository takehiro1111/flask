
from email_validator import EmailNotValidError, validate_email
from flask import (
  Flask,
  render_template,
  url_for,
  current_app,g,
  redirect,
  request,
  flash
)

# インスタンス化
app = Flask(__name__)

app.config.update(
    SECRET_KEY='testtesttest',  # 環境変数を使わず直接設定
    DEBUG=True
)

ctx=app.app_context()
ctx.push()

print(current_app.name)

g.connection = "connection"
print(g.connection)

# hello world用のcontextのためコメントアウト
# with app.test_request_context():  
#   print(url_for("hello",name="takehiro1111"))

with app.test_request_context("/users?updated=true"):
  print(request.args.get("updated"))

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
  return render_template('contact.html')

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
      
    if not email:
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
      
    if not is_valid:
      return redirect(url_for("contact"))
  
  # ↓メールを送信する処理の実装
    

    flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございます。")
    return redirect(url_for("contact_complete"))
  return render_template("contact_complete.html")

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error(f'Server Error: {e}')
    return 'Internal Server Error from Logger', 500


if __name__ == "__main__":
    app.run(debug=True)
