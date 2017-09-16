#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint,jsonify,request
from model.Model import Usuarios
import json

user = Blueprint('user',__name__)

@user.route('/user/')
def index_user():
	#listando todos os usuarios
	usuarios = json.loads(Usuarios.objects.to_json())
	print usuarios
	return jsonify({"message":usuarios})


@user.route('/user/',methods=['POST'])
def create_user():
	#recebendo os dados da request
	usuario = request.get_json()
	novo_usuario = Usuarios()

	for u in usuario.keys():
		setattr(novo_usuario,u,usuario[u])

	novo_usuario.save()

	return jsonify({"message":"usuario adicionado com sucesso"})

@user.route('/user/<id>/')
def user_by_id(id):
	user = json.loads(Usuarios.objects(id=id).to_json())
	return jsonify({"message":user})


@user.route('/user/<id>',methods=["DELETE"])
def delete_user(id):
	return jsonify({"message":"Excluindo um usuario"})


@user.route('/user/<id>',methods=['PUT'])
def update_user(id):
	usuario = request.get_json()
	
	novo_usuario = Usuarios.objects(id=id).first()
	

	for u in usuario.keys():
		setattr(novo_usuario,u,usuario[u])

	novo_usuario.save()

	return jsonify({"message":"Alterando um usuario"})
