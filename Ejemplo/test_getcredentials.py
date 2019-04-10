# -*- coding: utf-8 -*-
import os.path, sys, warnings
import json
sys.path.append(os.path.abspath(".."))
from lib.todopagoconnectorbvg import TodoPagoConnectorBvg

j_header_http = {
	'Authorization':'TODOPAGO 86333EFD8AD0C71CEA3BF06D7BDEF90D'
}

bvg = TodoPagoConnectorBvg(j_header_http, "test")

print('--------------------- GET CREDENTIALS ---------------------')

UserAccount = {
    'USUARIO' : "guillermodlucero@gmail.com", 
    'CLAVE' : "1970Stk!"
}

responseGetCredential = bvg.getCredentials(UserAccount)

print(responseGetCredential)
