import json, sys, os
sys.path.append(os.path.abspath(".."))
from lib.todopagoconnectorbvg import TodoPagoConnectorBvg

j_header_http = {
'Authorization':'TODOPAGO ba8821a62ef8431db87558f545674533'
}

bvg = TodoPagoConnectorBvg(j_header_http, "test")

discover = bvg.discover()
print(discover.paymentMethods)