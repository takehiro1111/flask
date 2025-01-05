from apps.extensions import db
from apps.crud.models import User
from apps.detector.models import UserImage

# INNER JOIN
db.session.query(User,UserImage).join(UserImage).filter(User.id == UserImage.user_id).all()
## 外部キーが設定されているため、以下でも同様の結果が得られる。
db.session.query(User,UserImage).join(UserImage).all()


# OUTER JOIN
db.session.query(User,UserImage).outerjoin(UserImage).filter(User.id == UserImage.user_id).all()
db.session.query(User,UserImage).outerjoin(UserImage).all()
