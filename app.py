from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Dev Ops is cool!!! Test #3'
