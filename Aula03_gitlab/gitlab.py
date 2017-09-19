#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests

token = 'y5BAhu9Tdmi84XjSY2yR'
recurso = "users"
url = "http://192.168.0.3/api/v3/%s?private_token=%s"%(recurso,token)

print url

class Gitlab():
    

#adicionando um user

usuarios = {"name":"Victor"}

try:
    add = json.loads(requests.post(url,data=usuarios)._content)
except Exception as inst:
    print inst


if __name__ == "__main__":
    git = Gitlab()
    git.create_project({'name':'PROJETO-API'})
       
    
#criar usuarios
#listar repositorios
#criar projeto
#adicionar um usuario a um grupo







