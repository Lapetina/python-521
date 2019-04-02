#!/usr/bin/python3

from flask import Blueprint, render_template

site = Blueprint('site',__name__, url_prefix='/site')

@site.route('/')
def site_home():
    dados = [{'id' : 2, 'nome' : 'Paramahansa Yogananda'}]
    dados.append({'id' : '3', 'nome' : 'Gabriel o Pensador'})
    dados.append({'id' : '4', 'nome' : 'João Batista'})
    return render_template('index.html', nome='Victor', usuarios=dados)

@site.route('/contato')
def contato():
    return render_template('contato.html')


