from logging import debug
from flask import Flask, render_template
from flask import request  # for creating a client request object

app = Flask(__name__)


#defining a route for request from web-server
#@app.route('/')
def index():
    return '<h1>Hello world!<h1>'

#----------------------------------------------------
#in below route the <name> is dynamic part
#serves mapped to different dynamic component
#e.g. route /user/<int:id>  would have id dynamic segment e.g.: /user/123
#flask supoort string, int, float and path for routes.
#-----------------------------------------------------------------
#@app.route('/user/<name>')
def user(name):
    return '<h2>Hello, {}! <h2>'.format(name)

#-------- application and request context-------------------
# Need : from flask import request
#@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}'.format(user_agent)


#------RENDRING template---------
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    return render_template('name.html', name=name)
#-------------------------------------------
#to start deployment : flask run
if __name__ == "__main__":
    app.run(debug=True)

