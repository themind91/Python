#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint,jsonify

grupos = Blueprint('grupos',__name__) 

@grupos.route('/grupos/')
def index_groups():
	return jsonify({"message":"gerenciamento de grupos"})


@grupos.route('/grupos/',methods=['POST'])
def create_groups():
	return jsonify({"message":"adicionando um grupo"})

@grupos.route('/grupos/<int:id>/')
def get_user_by_id(id):
	return jsonify({"message":"gerenciado apenas um grupo"})

@grupos.route('/grupos/<int:id>/',methods=['PUT'])
def atualizar_grupo(id):
	return jsonify({"message":"atualizando um grupo"})

@grupos.route('/grupos/<int:id>/',methods=['DELETE'])
def excluir_grupo(id):
	return jsonify({"message":"excluindo um grupo"})