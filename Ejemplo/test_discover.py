import json, sys, os
sys.path.append(os.path.abspath(".."))
from lib.todopagoconnectorbvg import TodoPagoConnectorBvg

j_header_http = {
'Authorization':'TODOPAGO 86333EFD8AD0C71CEA3BF06D7BDEF90D'
}

bvg = TodoPagoConnectorBvg(j_header_http, "test")

discover = bvg.discover()
print(discover.paymentMethods)