from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World! This is a Flask app running on Google Cloud Platform.'