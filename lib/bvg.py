import json
import requests
from lib.discover import *
from lib.transaction import *
from lib.push import *

DISCOVER_ENDPOINT = 'bsa/discover/api/BSA/paymentMethod/discover'
TRANSACTION_ENDPOINT = 'ms/tx/v1/bsa'
PUSH_ENDPOINT ='ms/tx/v1/bsa'

class BVG:
    def __init__(self, end_point):
        self._end_point_discover = end_point + DISCOVER_ENDPOINT
        self._end_point_transaction = end_point + TRANSACTION_ENDPOINT
        self._end_point_push = end_point + PUSH_ENDPOINT

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
        responseJsonPush = requests.put(self._end_point_push+"/"+push.generalData["publicRequestKey"], data=jsonData, headers=headers, verify=False )
        
        push.setResponse(self._getResponseData(responseJsonPush))
        
        return push

    def _getResponseData(self, responseJson):
        if(responseJson.status_code != 200 and responseJson.status_code != 201):
            errResp = responseJson.json()
            raise Exception(errResp)
        
        return responseJson.json()        
