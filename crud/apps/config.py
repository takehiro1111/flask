from pathlib import Path

basedir = Path(__file__).parent.parent

# BaseConfigクラスを作成する。
class BaseConfig(object):
  SECRET_KEY = "hogehoge"
  WTF_CSRF_SECRET_KEY = "fugafuga"
  
# BaseConfigクラスを継承してLocalConfigクラスを作成する。
class LocalConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'locals.sqlite'}"
  SECRET_KEY="testtest"
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SQLALCHEMY_ECHO = True
  WTF_CSRF_SECRET_KEY="testtest"
  
# BaseConfigクラスを継承してTestingConfigクラスを作成する。
class TestingConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'locals.sqlite'}"
  WTF_CSRF_ENABLED = False
  SECRET_KEY="testtest"
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SQLALCHEMY_ECHO = True
  WTF_CSRF_SECRET_KEY="testtest"
  
# 辞書にマッピングする。
config = {
  "testing": TestingConfig,
  "local": LocalConfig,
}
