import os
from flask import Flask, app, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return inicio()

@app.route('/inicio')
def inicio():
    return render_template('index.html', pagina_selecionada = 'inicio')

@app.route('/producoes')
def producoes():
    return render_template('producoes.html', pagina_selecionada = 'producoes')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', pagina_selecionada = 'sobre')

print(f'rodando script com {__name__}')
port = int(os.environ.get("PORT", 5000))
print(f'na porta {port}')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
