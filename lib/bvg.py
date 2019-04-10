import json
import requests
import sys
from lib.discover import *
from lib.transaction import *
from lib.push import *
from lib.loginbvtp import *


DISCOVER_ENDPOINT = 'bsa/discover/api/BSA/paymentMethod/discover'
TRANSACTION_ENDPOINT = 'ms/tx/v1/bsa'
PUSH_ENDPOINT ='ms/tx/v1/bsa'
LOGINBVTP_ENDPOINT ='api/LoginBVTP'
BUYERPAYMENTMETHOD_ENDPOINT ='ms/transactions/api/BSA/transaction/notificacionPush'

DISCOVER_ENDPOINT_TEST = 'ms/discover/api/BSA/paymentMethod/discover'
TRANSACTION_ENDPOINT_TEST = 'ms/transactions/api/BSA/transaction'
PUSH_ENDPOINT_TEST ='ms/transactions/api/BSA/transaction/notificacionPush'
LOGINBVTP_ENDPOINT_TEST ='api/LoginBVTP'
BUYERPAYMENTMETHOD_ENDPOINT_TEST ='ms/transactions/api/BSA/transaction/notificacionPush'

class BVG:
    def __init__(self, end_point):

        if end_point=="https://portal.integration.todopago.com.ar/":
            self._end_point_discover = end_point + DISCOVER_ENDPOINT_TEST
            self._end_point_transaction = end_point + TRANSACTION_ENDPOINT_TEST
            self._end_point_push = end_point + PUSH_ENDPOINT_TEST
            self._end_point_loginbvtp = end_point + LOGINBVTP_ENDPOINT_TEST
            self._end_point_buyerpaymentmethod = end_point + BUYERPAYMENTMETHOD_ENDPOINT_TEST


        else:
            self._end_point_discover = end_point + DISCOVER_ENDPOINT
            self._end_point_transaction = end_point + TRANSACTION_ENDPOINT
            self._end_point_push = end_point + PUSH_ENDPOINT
            self._end_point_loginbvtp = end_point + LOGINBVTP_ENDPOINT
            self._end_point_buyerpaymentmethod = end_point + BUYERPAYMENTMETHOD_ENDPOINT

            

    def discoverPaymentMethods(self):
        responseJson = requests.get(self._end_point_discover,verify=False)
        discover = Discover()
        discover.paymentMethods = responseJson.json()

        return discover

    def getTransactions(self,transaction):
        transaction.validar()

        dataRequest = {}
        dataRequest["generalData"]   = transaction.generalData
        dataRequest["operationData"] = transaction.operationData
        dataRequest["technicalData"] = transaction.technicalData
        
        jsonData = json.dumps(dataRequest, ensure_ascii=False)

        headers = {'Content-type': 'application/json', 'Authorization': transaction.generalData["security"]}
        responseJson = requests.post(self._end_point_transaction, data=jsonData, headers=headers, verify=False )

        transaction.setResponse(self._getResponseData(responseJson))

        return transaction

    def getNotificationPush(self, push):
        push.validar()

        dataRequestPush = {}
        dataRequestPush["generalData"] = push.generalData
        dataRequestPush["operationData"] = push.operationData
        dataRequestPush["tokenizationData"] = push.tokenizationData

        jsonData = json.dumps(dataRequestPush)
        
        headers = {'Content-Type': 'application/json', 'Authorization':push.generalData["security"]}
        responseJsonPush = requests.post(self._end_point_push, data=jsonData, headers=headers, verify=False )
        
        push.setResponse(self._getResponseData(responseJsonPush))
        
        return push

    def getLoginBvtp(self, loginBvtp):
        jsonData = json.dumps(loginBvtp)
        print jsonData
        sys.exit()
        
        headers = {'Content-Type': 'application/json'}
        responseJsonBvtp = requests.post(self._end_point_loginbvtp, data=jsonData, headers=headers, verify=False )
        
        loginBvtp.setResponse(self._getResponseData(responseJsonBvtp))
        
        return loginBvtp        

    def _getResponseData(self, responseJson):
        if(responseJson.status_code != 200 and responseJson.status_code != 201):
            errResp = responseJson.json()
            raise Exception(errResp)
        
        return responseJson.json()        
