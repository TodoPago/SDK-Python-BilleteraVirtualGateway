import sys
sys.path.append("..")
from todopagoconnectorbvg import TodoPagoConnectorBvg
from pushnotificationdata import PushNotificationData
from push import Push
import unittest
from unittest import TestCase
if sys.version_info[0] >= 3 :
	from unittest.mock import patch, Mock
else:
	from mock import patch, Mock, MagicMock

class PushNotificationTest(TestCase):

	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')
	def test_push_notification_ok(self, MockTodoPagoConnectorBvg):
		header_http = {
			'Authorization':'TODOPAGO f3d8b72c94ab4a06be2ef7c95490f7d3'
		}

		TPConnectorBvg = MockTodoPagoConnectorBvg(header_http, "test")

		instancePushData = PushNotificationData()
		
		TPConnectorBvg.push.return_value = instancePushData.get_transaction_ok_response()

		generalData = {}
		generalData["merchant"] = 41702
		generalData["security"] = "TODOPAGO 8A891C0676A25FBF052D1C2FFBC82DEE"
		generalData["remoteIpAddress"] = "192.168.11.87"	
		generalData["publicRequestKey"] = "2869c611-a55a-49d5-9be2-3137c95321zz"
		generalData["operationName"] = "Compra"
		generalData["operationDatetime"] = "20160704085736"

		operationData = {}
		operationData["resultCodeMedioPago"] = "-1"
		operationData["resultCodeGateway"] = "-1"
		operationData["idGateway"] = "8"
		operationData["resultMessage"] = "Aprobada"
		operationData["ticketNumber"] = "7866463542424"
		operationData["codigoAutorizacion"] = "455422446756567"
		operationData["currencyCode"] = "032"
		operationData["operationID"] = "1234"
		operationData["concept"] = "compra"
		operationData["amount"] = "999,99"
		operationData["facilitiesPayment"] = "03"

		availablePaymentMethods = [11]
		operationData["availablePaymentMethods"] = availablePaymentMethods
		operationData["availableBanks"] = []

		buyerPreselection = {}
		buyerPreselection["paymentMethodId"] = "42"
		buyerPreselection["bankId"] = 11
		operationData["buyerPreselection"] = buyerPreselection 

		tokenizationData = {}
		tokenizationData["publicTokenizationField"] = "sydguyt3e862t76ierh76487638rhkh7"
		tokenizationData["credentialMask"] = "4510XXXXX00001"

		push = Push()
		push.inicializar(generalData, operationData, tokenizationData)

		transactionResponse = TPConnectorBvg.push(push) 

		self.assertGreater(len(transactionResponse),0)
		self.assertEqual("OK", transactionResponse['statusMessage'])

	
	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')
	def test_push_notification_fail(self, MockTodoPagoConnectorBvg):
		header_http = {
			'Authorization':'TODOPAGO f3d8b72c94ab4a06be2ef7c95490f7d3'
		}

		TPConnectorBvg = MockTodoPagoConnectorBvg(header_http, "test")

		instancePushData = PushNotificationData()
		
		TPConnectorBvg.push.return_value = instancePushData.get_transaction_fail_response()

		generalData = {}
		generalData["merchant"] = 41702
		generalData["security"] = "TODOPAGO 8A891C0676A25FBF052D1C2FFBC82DEE"
		generalData["remoteIpAddress"] = "192.168.11.87"	
		generalData["publicRequestKey"] = "2869c611-a55a-49d5-9be2-3137c95321zz"
		generalData["operationName"] = "Compra"
		generalData["operationDatetime"] = "20160704085736"

		operationData = {}
		operationData["resultCodeMedioPago"] = "-1"
		operationData["resultCodeGateway"] = "-1"
		operationData["idGateway"] = "8"
		operationData["resultMessage"] = "Aprobada"
		operationData["ticketNumber"] = "7866463542424"
		operationData["codigoAutorizacion"] = "455422446756567"
		operationData["currencyCode"] = "032"
		operationData["operationID"] = "1234"
		operationData["concept"] = "compra"
		operationData["facilitiesPayment"] = "03"

		availablePaymentMethods = [11]
		operationData["availablePaymentMethods"] = availablePaymentMethods
		operationData["availableBanks"] = []

		buyerPreselection = {}
		buyerPreselection["paymentMethodId"] = "42"
		buyerPreselection["bankId"] = 11
		operationData["buyerPreselection"] = buyerPreselection 

		tokenizationData = {}
		tokenizationData["publicTokenizationField"] = "sydguyt3e862t76ierh76487638rhkh7"
		tokenizationData["credentialMask"] = "4510XXXXX00001"

		push = Push()
		push.inicializar(generalData, operationData, tokenizationData)

		transactionResponse = TPConnectorBvg.push(push) 

		self.assertGreater(len(transactionResponse),0)
		self.assertEqual("1014", transactionResponse['errorCode'])
	
	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')
	def test_get_credentials_702(self, MockTodoPagoConnectorBvg):
		header_http = {
			'Authorization':'TODOPAGO f3d8b72c94ab4a06be2ef7c95490f7d3'
		}

		TPConnectorBvg = MockTodoPagoConnectorBvg(header_http, "test")

		instancePushData = PushNotificationData()
		
		TPConnectorBvg.push.return_value = instancePushData.get_wrong_transaction_response()

		generalData = {}
		generalData["merchant"] = 41702
		generalData["security"] = "TODOPAGO 8A891C0676A25FBF052D1C2FFBC82DEE"
		generalData["remoteIpAddress"] = "192.168.11.87"	
		generalData["publicRequestKey"] = "2869c611-a55a-49d5-9be2-3137c95321zz"
		generalData["operationName"] = "Compra"
		generalData["operationDatetime"] = "20160704085736"

		operationData = {}
		operationData["resultCodeMedioPago"] = "-1"
		operationData["resultCodeGateway"] = "-1"
		operationData["idGateway"] = "8"
		operationData["resultMessage"] = "Aprobada"
		operationData["ticketNumber"] = "7866463542424"
		operationData["codigoAutorizacion"] = "455422446756567"
		operationData["currencyCode"] = "032"
		operationData["operationID"] = "1234"
		operationData["concept"] = "compra"
		operationData["amount"] = "999,99"
		operationData["facilitiesPayment"] = "03"

		availablePaymentMethods = [11]
		operationData["availablePaymentMethods"] = availablePaymentMethods
		operationData["availableBanks"] = []

		buyerPreselection = {}
		buyerPreselection["paymentMethodId"] = "42"
		buyerPreselection["bankId"] = 11
		operationData["buyerPreselection"] = buyerPreselection 

		tokenizationData = {}
		tokenizationData["publicTokenizationField"] = "sydguyt3e862t76ierh76487638rhkh7"
		tokenizationData["credentialMask"] = "4510XXXXX00001"

		push = Push()
		push.inicializar(generalData, operationData, tokenizationData)

		transactionResponse = TPConnectorBvg.push(push) 

		self.assertGreater(len(transactionResponse),0)
		self.assertEqual("2070", transactionResponse['statusCode'])

if __name__ == '__main__':
	unittest.main()
