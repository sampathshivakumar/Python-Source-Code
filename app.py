from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Thank you for staying till end. I am looking for DevOps fresher role, If anyone has a requirement please let me know</h1>'
