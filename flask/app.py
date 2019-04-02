#!/usr/bin/python3
import json
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime
from blueprint.site import site
from flask import Flask, jsonify, make_response, redirect, request, render_template

app = Flask(__name__)
app.register_blueprint(site)


client = MongoClient()
db = client.segunda
#for u in db.usuarios.find():
#    print(u)
#exit()



@app.route('/')
def home():
    usuarios = []
    return jsonify([json.loads(dumps(u)) for u in db.usuarios.find()])
            #del u['_id']
#            usuarios.append(json.loads(dumps(u)))
#    return jsonify(usuarios)

#    return jsonify({'mensagem':'Rodando...'})

@app.route('/cadastrar', methods=['POST'])
def bunda():
    dados = request.get_json()
    #Se dados for nulo, return 400
    #{"mensagem":"Corpo não pode ser vazio"}
    if dados is None:
        return make_response(jsonify({"mensagem" : "Corpo não pode ser vazio"}),400)
    dados['lapetina'] = 'fumacinha'
    return (jsonify(dados),400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

