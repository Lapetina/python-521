#!/usr/bin/python3

import docker

DOCKER_URL = ('tcp://127.0.0.1:2376')

client = docker.DockerClient(base_url=DOCKER_URL, version='auto')

print('{0:<25}{1:<20}{2:>10}'.format('NOME','IMAGEM','STATUS'))
for c in client.containers.list(all=True):
    print('{0:.<25}{1:.<20}{2:.>10}'.format(c.name, c.image.tags[0], c.status))
