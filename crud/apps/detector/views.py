from flask import Blueprint,render_template
from apps.extensions import db
from apps.crud.models import User
from apps.detector.models import UserImage


# template_folderを指定する。(他dirでcssファイルを入れていたstaticは指定しない。)
detector_bp = Blueprint(
  "detector",
  __name__,
  template_folder="templates"
)

# dtアプリケーションを使用してエンドポイントを作成する。
@detector_bp.route("/",methods=["GET"])
def index():
  # UserとUserImnageをJoinして画像一覧を取得する。
  user_images = (
    db.session.query(User,UserImage)
    .join(UserImage)
    .filter(User.id == UserImage.user_id)
    .all()
  )
  
  return render_template("detector/index.html",user_images=user_images)


