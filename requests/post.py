#!/usr/bin/python3

#Tentar cadastrar um usuário pela API
#Capturar os dados pelo temrinal
#E inserir o usuário na API


from requests import post


nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
idade = input("Idade: ")

data = {"nome":nome,"email":email,"idade": idade}
response = post('http://192.168.202.79/usuarios',json=data)

print(response.text)
