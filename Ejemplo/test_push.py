import time 
import json
import json, sys, os
sys.path.append(os.path.abspath(".."))
from lib.todopagoconnectorbvg import TodoPagoConnectorBvg
from lib.transaction import *
from lib.push import *

j_header_http = {
'Authorization':'TODOPAGO'
}

bvg = TodoPagoConnectorBvg(j_header_http, "test")

generalData = {}
generalData["merchant"] = 41702
generalData["security"] = "TODOPAGO 8A891C0676A25FBF052D1C2FFBC82DEE"
generalData["remoteIpAddress"] = "192.168.11.87"	
generalData["publicRequestKey"] = "9541ea16-32bb-420a-8409-17609883bebc"
generalData["operationName"] = "Compra"

operationData = {}
operationData["operationDatetime"] = "20160704085736"
operationData["resultCodeMedioPago"] = "-1"
operationData["resultCodeGateway"] = "-1"
operationData["idGateway"] = "8"
operationData["resultMessage"] = "Aprobada"
operationData["ticketNumber"] = "7824"
operationData["codigoAutorizacion"] = "0567"
operationData["currencyCode"] = "032"
operationData["operationID"] = "1234"
operationData["concept"] = "compra"
operationData["amount"] = "999,99"
operationData["facilitiesPayment"] = "03"

tokenizationData = {}
tokenizationData["publicTokenizationField"] = "4540759999996760"
tokenizationData["credentialMask"] = "4510XXXXXXXX0001"

push = Push()
push.inicializar(generalData,operationData, tokenizationData)
push = bvg.push(push)

print(push.getResponse()) 
