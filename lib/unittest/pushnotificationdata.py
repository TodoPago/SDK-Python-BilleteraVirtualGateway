# -*- coding: utf-8 -*-
class PushNotificationData:

	def get_transaction_ok_response(self):
		return {
				"statusCode":"-1",
				"statusMessage":"OK"
				}

	def get_transaction_fail_response(self):
		return {
				"errorCode":"1014",
				"errorMessage":"Completá este campo.",
				"channel":"11"
				}

	def get_wrong_transaction_response(self):
		return {
				"statusCode":"2070",
				"statusMessage":"Lo sentimos, la referencia a la transacción enviada es inválida."
				}