import sys
sys.path.append("..")
from todopagoconnectorbvg import TodoPagoConnectorBvg
from transactiondata import TransactionsData
from transaction import Transaction
from push import Push
import unittest
from unittest import TestCase
if sys.version_info[0] >= 3 :
	from unittest.mock import patch, Mock
else:
	from mock import patch, Mock, MagicMock

class transactionTest(TestCase):

	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')
	def test_transaction_notification_ok(self, MockTodoPagoConnectorBvg):
		header_http = {
			'Authorization':'TODOPAGO f3d8b72c94ab4a06be2ef7c95490f7d3'
		}

		MTPConnectorBvg = MockTodoPagoConnectorBvg(header_http, "test")

		instanceTransaction = TransactionsData()
		
		MTPConnectorBvg.transactions.return_value = instanceTransaction.get_transaction_ok_response()

		#parameters
		generalData = {}
		generalData["merchant"] = 41702
		generalData["security"] = "PRISMA 8A891C0676A25FBF052D1C2FFBC82DEE"
		generalData["operationDatetime"] = "20160704085736"
		generalData["remoteIpAddress"] = "192.168.11.87"
		generalData["channel"] = "BVTP"

		operationData = {}
		operationData["operationType"] = "Compra"
		operationData["operationID"] = "010617_01"
		operationData["currencyCode"] = "032"
		operationData["concept"] = "compra"
		operationData["amount"] = "999,99"

		availablePaymentMethods = [11]
		operationData["availablePaymentMethods"] = availablePaymentMethods
		operationData["availableBanks"] = []

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

		transactionResponse = MTPConnectorBvg.transactions(transaction) 

		self.assertGreater(len(transactionResponse),0)
		self.assertNotEqual(" ", transactionResponse['publicRequestKey'])

	
	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')
	def test_transaction_notification_fail(self, MockTodoPagoConnectorBvg):
		header_http = {
			'Authorization':'TODOPAGO f3d8b72c94ab4a06be2ef7c95490f7d3'
		}

		MTPConnectorBvg = MockTodoPagoConnectorBvg(header_http, "test")

		instanceTransaction = TransactionsData()
		
		MTPConnectorBvg.transactions.return_value = instanceTransaction.get_transaction_fail_response()

		#parameters
		generalData = {}
		generalData["merchant"] = 41702
		generalData["security"] = "PRISMA 8A891C0676A25FBF052D1C2FFBC82DEE"
		generalData["operationDatetime"] = "20160704085736"
		generalData["remoteIpAddress"] = "192.168.11.87"
		generalData["channel"] = "BVTP"

		operationData = {}
		operationData["operationType"] = "Compra"
		operationData["operationID"] = "010617_01"
		operationData["currencyCode"] = "032"
		operationData["concept"] = "compra"

		availablePaymentMethods = [11]
		operationData["availablePaymentMethods"] = availablePaymentMethods
		operationData["availableBanks"] = []

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

		transactionResponse = MTPConnectorBvg.transactions(transaction) 

		self.assertGreater(len(transactionResponse),0)
		self.assertEqual("1014", transactionResponse['errorCode'])

	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')
	def test_transaction_credentials_702(self, MockTodoPagoConnectorBvg):
		header_http = {
			'Authorization':'TODOPAGO f3d8b72c94ab4'
		}

		MTPConnectorBvg = MockTodoPagoConnectorBvg(header_http, "test")

		instanceTransaction = TransactionsData()
		
		MTPConnectorBvg.transactions.return_value = instanceTransaction.get_transaction_702_response()

		#parameters
		generalData = {}
		generalData["merchant"] = 41702
		generalData["security"] = "PRISMA 8A891C0676A25FBF052D1C2FFBC82DEE"
		generalData["operationDatetime"] = "20160704085736"
		generalData["remoteIpAddress"] = "192.168.11.87"
		generalData["channel"] = "BVTP"

		operationData = {}
		operationData["operationType"] = "Compra"
		operationData["operationID"] = "010617_01"
		operationData["currencyCode"] = "032"
		operationData["concept"] = "compra"
		operationData["amount"] = "999,99"

		availablePaymentMethods = [11]
		operationData["availablePaymentMethods"] = availablePaymentMethods
		operationData["availableBanks"] = []

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

		transactionResponse = MTPConnectorBvg.transactions(transaction) 

		self.assertGreater(len(transactionResponse),0)
		self.assertEqual("702", transactionResponse['errorCode'])

if __name__ == '__main__':
	unittest.main()
