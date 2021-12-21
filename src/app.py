from flask import Flask
from flask.templating import render_template

app = Flask("__name__")

@app.route('/')
def home():
    return inicio()

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/artistas')
def artistas():
    return render_template('artistas.html')

