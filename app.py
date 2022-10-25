import sys

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, World from {sys.version} {sys.version_info}!'
