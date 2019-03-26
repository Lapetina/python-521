#!/usr/bin/python3

#Pegar o CEP do temrinal -> input
#Exibir apenas o logradouro -> ?

import requests 

cep = input(str("Informe um cep: "))

response = requests.get('http://viacep.com.br/ws/{0}/json/'.format(cep))

if response.status_code == 200:
    json = response.json()
    print(json['logradouro'])

