from flask import Flask
from flask.templating import render_template

app = Flask("__name__")

@app.route('/')
def home():
    return inicio()

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/producoes')
def producoes():
    return render_template('producoes.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

