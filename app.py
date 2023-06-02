from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Sampath, You Can Only Help Yourself'
