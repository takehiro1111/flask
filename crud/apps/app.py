from flask import Flask

def create_app():
  app = Flask(__name__)
  
  import views
  
  # register_blueprint関数を用いて、viewsのcrudをアプリへ登録する。
  app.register_blueprint(views.crud,url_prefix="/crud")
  return app

if __name__ == "__main__":
    import app
    app.run(debug=True)
