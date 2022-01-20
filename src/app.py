import os
from flask import Flask, render_template

flaskapp = Flask(__name__)

@flaskapp.route('/')
def home():
    return inicio()

@flaskapp.route('/inicio')
def inicio():
    return render_template('index.html', pagina_selecionada = 'inicio')

@flaskapp.route('/producoes')
def producoes():
    return render_template('producoes.html', pagina_selecionada = 'producoes')

@flaskapp.route('/sobre')
def sobre():
    return render_template('sobre.html', pagina_selecionada = 'sobre')


if __name__ == '__main__':
    flaskapp.run('0.0.0.0')
