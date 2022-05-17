from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    Lezgo = os.environ.get("Lezgo")
    return Lezgo