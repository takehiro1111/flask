from flask_wtf import FlaskForm

from wtforms import PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class SignUpForm(FlaskForm):
  username = StringField(
    "ユーザー名",
    validators = [
      DataRequired("ユーザー名は必須です。"),
      Length(1,30,"so文字以内で入力してください。")
    ]
  )
  email = StringField(
    "メールアドレス",
    validators = [
      DataRequired("メールアドレスは必須です。"),
      Email("メールアドレスの形式で入力してください。")
    ]
  )
  password = PasswordField(
    "パスワード",
    validators = [DataRequired("パスワードは必須です。")]
  )
  submit = SubmitField("新規登録")

class LoginForm(FlaskForm):
  """
  ログイン機能のフォームクラス
  """
  email = StringField(
    "メールアドレス",
    validators = [
      DataRequired("メールアドレスは必須です。"),
      Email("メールアドレスの形式で入力してください。"),
    ]
  )
  password = PasswordField("パスワード",validators = [
    DataRequired("パスワードは必須です。")
  ])
  submit = SubmitField("ログイン")
