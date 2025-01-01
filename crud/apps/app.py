from flask import Flask,render_template
import views,app

app = Flask(__name__)

# @app.route('/')
# def index():
#   return render_template("crud/index.html")
  
def create_app():
  # register_blueprint関数を用いて、viewsのcrudをアプリへ登録する。
  app.register_blueprint(views.crud,url_prefix="/crud")
  return app

# flask runで実行されるようにグローバルで設定。
create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
