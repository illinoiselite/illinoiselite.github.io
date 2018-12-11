from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Home page - play with it if you must!"""
    return render_template('index.html')
