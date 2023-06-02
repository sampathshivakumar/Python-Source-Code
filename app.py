from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hi All, Hope you have enjoyed the Post.</h1>'
