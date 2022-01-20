from flask import Flask, app, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', pagina_selecionada = 'inicio')

@app.route('/sobre')
def sobre():
    idade = calcularIdade(date(1994,1,24))
    return render_template('sobre.html', idade = idade, pagina_selecionada = 'sobre')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', pagina_selecionada = 'projetos')    

def calcularIdade(dataAniversario):
    hoje = date.today()
    idade = hoje.year - dataAniversario.year - ((hoje.month, hoje.day) < (dataAniversario.month, dataAniversario.day))
    return idade


if __name__ == '__main__':
    app.run('0.0.0.0')
