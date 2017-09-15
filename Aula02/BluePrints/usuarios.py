#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint,jsonify
from model.Model import Usuarios
import json

user = Blueprint('user',__name__)

@user.route('/user/')
def index_user():
	#listando todos os usuarios
	usuarios = Usuarios.objects.to_json()
	print usuarios
	return jsonify({"message":usuarios})


@user.route('/user/',methods=['POST'])
def create_user():
	#recebendo os dados da request
	usuario = request.get_json()
	novo_usuario = Usuarios()
	novo_usuario.save(usuario)

	return jsonify({"message":"adicionando um usuario"})

@user.route('/user/<int:id>')
def user_by_id(id):
	usuarios = Usuarios.objects.to_json()
	return jsonify({"message":"Index do gerenciamento de usuarios %s" %id})


@user.route('/user/<int:id>',methods=["DELETE"])
def delete_user(id):
	return jsonify({"message":"Excluindo um usuario"})


@user.route('/user/<int:id>',methods=['PUT'])
def update_user(id):
	return jsonify({"message":"Alterando um usuario"})
