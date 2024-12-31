from flask import Flask,render_template,url_for,current_app,g,redirect,request

app = Flask(__name__)


################################################
# Hello World
################################################
@app.get('/')
def index():
  return 'Hello  Flaskbook'

# endpointを指定しない場合は関数名がendpointになる。
@app.route('/index',
          methods=["GET"],
          endpoint="hello-endpoint")
def index():
  return render_template('index.html')

@app.get('/hello/<string:name>')
def hello(name):
  return render_template('index.html',name=name)

@app.get('/name/<string:name>')
def show_name(name):
  name='takehiro1111'
  return render_template('index.html',name=name)


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
    return redirect(url_for("contact_complete"))
  else:
    return redirect(url_for("contact_complete"))

if __name__ == "__main__":
    app.run(debug=True)
    
ctx=app.app_context()
ctx.push()

print(current_app.name)

g.connection = "connection"
print(g.connection)

with app.test_request_context():
  print(url_for("hello-endpoint"))  
  print(url_for("hello",name="takehiro1111"))

with app.test_request_context("/users?updated=true"):
  print(request.args.get("updated"))
