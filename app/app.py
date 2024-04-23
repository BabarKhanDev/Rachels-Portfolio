from os import listdir

from flask import Flask, request, render_template, jsonify, send_from_directory, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home_page():
    return render_template("landing.html")


@app.route('/photo_paths')
def photo_paths():
    dirs = listdir("static/photos")
    return [url_for('static', filename=f'photos/{d}') for d in dirs]
