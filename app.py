from flask import Flask, render_template, request
from previsao import prever_preco

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prever', methods=['POST'])
def prever():
    dados = [float(request.form.get(campo)) for campo in ['tamanho', 'quartos', 'banheiros', 'ano']]
    modelo = request.form.get('modelo')
    preco = prever_preco(dados, modelo)
    return render_template('index.html', previsao=preco, modelo=modelo)

if __name__ == '__main__':
    app.run(debug=True)
