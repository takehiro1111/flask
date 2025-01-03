from flask_wtf import FlaskForm

from wtforms import PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class SignUpForm(FlaskForm):
  username = StringField(
    "user3",
    validations = [
      DataRequired("ユーザー名は必須です。"),
      Length(1,30,"so文字以内で入力してください。")
    ]
  )
  email = StringField(
    "testtesttest@gmail.com",
    validations = [
      DataRequired("メールアドレスは必須です。"),
      Email("メールアドレスの形式で入力してください。")
    ]
  )
  password = PasswordField(
    "takehiro1111",
    validations = [DataRequired("パスワードは必須です。")]
  )
  submit = SubmitField("新規登録")
