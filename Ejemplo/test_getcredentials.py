# -*- coding: utf-8 -*-
import os.path, sys, warnings
import json
sys.path.append(os.path.abspath(".."))
from lib.todopagoconnectorbvg import TodoPagoConnectorBvg

j_header_http = {
	'Authorization':'TODOPAGO 3785cdc853ca4248a62a0f6cbb823e1d'
}

bvg = TodoPagoConnectorBvg(j_header_http, "test")

print('--------------------- GET CREDENTIALS ---------------------')

UserAccount = {
    'USUARIO' : "usertodopago@gmail.com", 
    'CLAVE' : "password"
}

responseGetCredential = bvg.getCredentials(UserAccount)

print(responseGetCredential)
