from flask import Flask, request, render_template
import os
import sys

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Home page - play with it if you must!"""
    return render_template('index.html')
