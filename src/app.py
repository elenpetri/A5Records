from flask import Flask, app, render_template

app = Flask("__name__")

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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
