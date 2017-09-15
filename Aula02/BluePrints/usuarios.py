#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint,jsonify

user = Blueprint('user',__name__)

@user.route('/user/')
def index_user():
	return jsonify({"message":"Index do gerenciamento de usuarios"})


@user.route('/user/',methods=['POST'])
def create_user():
	return jsonify({"message":"adicionando um usuario"})

@user.route('/user/<int:id>')
def user_by_id(id):
	return jsonify({"message":"Index do gerenciamento de usuarios %s" %id})


@user.route('/user/<int:id>',methods=["DELETE"])
def delete_user(id):
	return jsonify({"message":"Excluindo um usuario"})


@user.route('/user/<int:id>',methods=['PUT'])
def update_user(id):
	return jsonify({"message":"Alterando um usuario"})
