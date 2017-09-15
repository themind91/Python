#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"db":"mymodel"}

db = MongoEngine(app)

# criando a estrutura do banco de dados

class Usuarios(db.Document):
	nome = db.StringField()
	email = db.StringField(unique=True)
	dt_cadastro = db.DateTimeField(default=datetime.now())

class Grupos(db.Document):
	nome = db.StringField(unique=True)
	integrantes = db.ListField()



# testando


if __name__ == '__main__':
	u = Usuarios()
	print 'teste'
	u.nome = " Mariana "
	u.email = " themind1991@gmail.com "

	g = Grupos()
	g.nome = "Analistas"
	g.integrantes.append(u)
	u.save()
	g.save()
