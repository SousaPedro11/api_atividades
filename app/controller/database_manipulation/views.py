import inspect
import json

from flask import flash, render_template, redirect, url_for, jsonify

from app import app
from app.controller.database_manipulation import DAO
from app.model.forms import FormPessoa
from app.model.tables import Pessoas


@app.route('/cadastrar/pessoa/', methods=['GET', 'POST'])
def cadastrar_pessoa():
    form = FormPessoa()

    if form.validate_on_submit():
        nome = form.nome.data.upper()
        idade = form.idade.data
        pessoa = Pessoas(nome=nome, idade=idade)
        DAO.transacao(pessoa)
        flash('{} cadastrado com sucesso!'.format(nome))
        print('pessoa {} cadastrada'.format(nome))
        return redirect(url_for('cadastrar_pessoa'))
    return render_template('cadastrar_pessoa.html', form=form)


@app.route('/buscar/pessoa/')
def buscar():
    pessoas = Pessoas.query.all()
    pessoasToList = []
    for p in pessoas:
        jsonPessoa = {}
        for i in inspect.getmembers(p):
            key = i[0]
            if not (key.startswith('_') | key.startswith('metadata') | key.startswith('query')):
                if not inspect.ismethod(i[1]):
                    jsonPessoa.update({i[0]: i[1]})
        pessoasToList.append(jsonPessoa)
    return jsonify(pessoasToList)
