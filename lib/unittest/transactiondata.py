# -*- coding: utf-8 -*-
class TransactionsData:

	def get_transaction_ok_response(self):
		return {
				"publicRequestKey":"1cb1567a-08f3-4558-ab7e-2b492236acce",
				"merchantId":"41702",
				"channel":"11"
				}

	def get_transaction_fail_response(self):
		return {
				"errorCode":"1014",
				"errorMessage":"Completá este campo.",
				"channel":"11"
				}

	def get_transaction_702_response(self):
		return {
				'errorCode': '702', 
				'errorMessage': 'Cuenta de vendedor invalida', 
				'channel': '11'
				}
