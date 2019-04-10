import re
import socket
import time

class Transaction:
	generalData=None
	operationData=None
	technicalData=None
	responseData=None
	
	def inicializar(self, generalData, operationData, technicalData):
	    self.generalData=generalData
	    self.operationData=operationData
	    self.technicalData=technicalData
	
	def setResponse(self,response):
		self.responseData = response

	def getResponse(self):
		return self.responseData
		
	def validar(self):
		if 'merchant' not in self.generalData or self.generalData["merchant"] is '':
			raise Exception('Falta dato requerido "merchant"')
		elif not type(self.generalData["merchant"]) == int:
			raise Exception('El campo "merchant" no es numerico"')
	

		if 'security' not in self.generalData or self.generalData["security"] is '':
			raise Exception('Falta dato requerido "security"')
		elif not re.match('^\w+\s\w+$',self.generalData["security"]):
			raise Exception('El campo "security" no es valido"') 	


		if 'operationDatetime' not in self.generalData or self.generalData["operationDatetime"] is '':
			raise Exception('Falta dato requerido "operationDatetime"')
		else:
			try:
				time.strptime(self.generalData["operationDatetime"], '%Y%m%d%H%M%S')
			except ValueError:
				raise Exception('El campo "operationDatetime" no tiene el formato "yyyyMMddHHmmss"') 

			
		if 'remoteIpAddress' not in self.generalData or self.generalData["remoteIpAddress"] is '':
			raise Exception('Falta dato requerido "remoteIpAddress"')
		else: 	
			try:
				socket.inet_aton(self.generalData["remoteIpAddress"])
			except socket.error:
				raise Exception('El dato "remoteIpAddress" no es una IP valida')
			

		if 'channel' not in self.generalData or self.generalData["channel"] is '':
			raise Exception('Falta dato requerido "channel"')
		elif not re.match('^\w+$',self.generalData["channel"]):
			raise Exception('El campo "channel" no es valido"') 	


		if 'operationID' not in self.operationData or self.operationData["operationID"] is '':
			raise Exception('Falta dato requerido "operationID"')
		elif not re.match('^\w+$',self.generalData["channel"]):
			raise Exception('El campo "operationID" no es valido"') 	


		if 'currencyCode' not in self.operationData or self.operationData["currencyCode"] is '':
			raise Exception('Falta dato requerido "currencyCode"')

		
		if 'amount' not in self.operationData or self.operationData["amount"] is '':
			raise Exception('Falta dato requerido "amount"')	
		elif not re.match('^[0-9]+(\,[0-9]{1,2})?$', self.operationData["amount"]):	
			raise Exception('El formato de "amount" no es valido, no include decimales o no esta separado por coma')	
			

		if 'availablePaymentMethods' in self.operationData and not all(isinstance(item, int) for item in self.operationData["availablePaymentMethods"]):
			raise Exception('El array "availablePaymentMethods" tiene que tener solo valores enteros')	


		if 'availableBanks' in self.operationData and not all(isinstance(item, int) for item in self.operationData["availableBanks"]):
			raise Exception('El array "availableBanks" tiene que tener solo valores enteros')

		if 'buyerPreselection' in self.operationData and 'bankId' in self.operationData["buyerPreselection"] and type(self.operationData["buyerPreselection"]["bankId"]) != int:
			raise Exception('Campo "bankId" no es entero')

		if 'buyerPreselection' in self.operationData and 'paymentMethodId' in self.operationData["buyerPreselection"] and type(self.operationData["buyerPreselection"]["paymentMethodId"]) != int:
			raise Exception('Campo "paymentMethodId" no es entero')
