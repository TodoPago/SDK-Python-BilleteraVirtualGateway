import json, sys, os
sys.path.append(os.path.abspath(".."))
from lib.todopagoconnectorbvg import TodoPagoConnectorBvg
from lib.transaction import *
from lib.user import *
from lib.bvg import *

j_header_http = {
'Authorization':'TODOPAGO 8A891C0676A25FBF052D1C2FFBC82DEE'
}

bvg = TodoPagoConnectorBvg(j_header_http, "test")

generalData = {}
generalData["merchant"] = 41702
generalData["security"] = "TODOPAGO 8A891C0676A25FBF052D1C2FFBC82DEE"
generalData["operationDatetime"] = "20160704085736"
generalData["remoteIpAddress"] = "192.168.11.87"
generalData["channel"] = "BVTP"

operationData = {}
operationData["operationType"] = "Compra"
operationData["operationID"] = "310517_01"
operationData["currencyCode"] = "032"
operationData["concept"] = "compra"
operationData["amount"] = "999,99"

availablePaymentMethods = [1, 42]
#operationData["availablePaymentMethods"] = availablePaymentMethods
operationData["availableBanks"] = [11]

buyerPreselection = {}
buyerPreselection["paymentMethodId"] = 42
buyerPreselection["bankId"] = 11
operationData["buyerPreselection"] = buyerPreselection 

# Esto es no obligatorio , puede mandarse un hash vacio 
technicalData = {}
technicalData["sdk"] = "Python"
technicalData["sdkversion"] = "1.4"
technicalData["lenguageversion"] = "1.8"
technicalData["pluginversion"] = "2.1"
technicalData["ecommercename"] = "DH-gate"
technicalData["ecommerceversion"] = "3.1"
technicalData["cmsversion"] = "2.4"	

transaction = Transaction()
transaction.inicializar(generalData, operationData, technicalData)

transaction = bvg.transactions(transaction) 

print(transaction.getResponse())
