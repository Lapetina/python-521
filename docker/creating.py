#!/usr/bin/python3
#Tentar verificar se o container realmente esta escutando
#na porta 10000
#Utilizando o módulo request
import requests
from docker import DockerClient


DOCKER_URL = 'tcp://127.0.0.1:2376'
client = DockerClient(base_url=DOCKER_URL, version='auto')

try:
    client.containers.get('apache').remove(force=True)
except:
    pass

client.containers.run('httpd:alpine',
        detach=True,
        ports={80 : 10000}, 
        name='apache', 
        environment={'NOME' : 'Paramahansa Yogananda'})

response = requests.get('http://127.0.0.1:10000')
if response.status_code == 200:
    print('O container esta de pé mano!:')
