# FLASK_APP=flask-demo.py flask run

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world'

@app.route('/user/<username>')
def showUser(username):
    return 'User: %s' % username