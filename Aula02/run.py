#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from BluePrints.usuarios import user
from BluePrints.grupos import grupos




#pegando as configuraçoes do flas
app = Flask(__name__)

app.register_blueprint(grupos)

@app.route("/usuarios/<int:id>")
def get_usuario(id):
	return  "aqui sera listado o usuario %s" %id

@app.route("/")
def hello():
	return  " Hello World python is rocking"

@app.route("/usuarios/")
def usuarios():
	return " <script>alert('atualizando users')</script> "

@app.route("/usuarios/",methods=['POST'])
def inserir_usuarios():
	return " <script>alert('atualizando users')</script> "

if __name__ == "__main__":
	app.run(debug=True, host= "192.168.0.1", port=8081)