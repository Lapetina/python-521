#!/usr/bin/python3
from datetime import datetime
from flask import Flask, jsonify, make_response, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'mensagem':'Rodando...'})

@app.route('/data')
def data():
    print('Paramahansa Yogananda')
    return jsonify({'hoje': datetime.now()})

@app.route('/naotemnadaaqui')
def naotemnadaaqui():
    return redirect('/')

@app.route('/cadastrar', methods=['POST'])
def bunda():
    dados = request.get_json()
    #Se dados for nulo, return 400
    #{"mensagem":"Corpo não pode ser vazio"}
    if dados is None:
        return make_response(jsonify({"mensagem" : "Corpo não pode ser vazio"}),400)
    dados['lapetina'] = 'fumacinha'
    return (jsonify(dados),400)

@app.route('/site')
def site():
    dados = [{'id' : 2, 'nome' : 'Paramahansa Yogananda'}]
    dados.append({'id' : '3', 'nome' : 'Gabriel o Pensador'})
    dados.append({'id' : '4', 'nome' : 'João Batista'})
    return render_template('index.html', nome='Victor', usuarios=dados)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

