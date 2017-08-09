import re
import socket
import time

class Push:
	generalData=None
	operationData=None
	tokenizationData=None
	responseData=None

	def inicializar(self, generalData, operationData, tokenizationData):
	    self.generalData=generalData
	    self.operationData=operationData
	    self.tokenizationData=tokenizationData
		
	def setResponse(self,response):
		self.responseData = response

	def getResponse(self):
		return self.responseData
	
	def validar(self):

		if 'operationName' not in self.generalData or self.generalData["operationName"] is '':
			raise Exception('Falta dato requerido "operationName"')
		elif not type(self.generalData["operationName"]) == str:	
			raise Exception('El campo "operationName" no de tipo string')


		if 'security' not in self.generalData or self.generalData["security"] is '':
			raise Exception('Falta dato requerido "security"')
		elif not re.match('^\w+\s\w+$',self.generalData["security"]):
			raise Exception('El campo "security" no es valido"') 	
			

		if 'merchant' not in self.generalData or self.generalData["merchant"] is '':
			raise Exception('Falta dato requerido "merchant"')
		elif not type(self.generalData["merchant"]) == int:
			raise Exception('El campo "merchant" no es numerico"')	


		if 'remoteIpAddress' not in self.generalData or self.generalData["remoteIpAddress"] is '':
			raise Exception('Falta dato requerido "remoteIpAddress"')
		else: 	
			try:
				socket.inet_aton(self.generalData["remoteIpAddress"])
			except socket.error:
				raise Exception('El dato "remoteIpAddress" no es una IP valida')

		if 'security' not in self.generalData or self.generalData["security"] is '':
			raise Exception('Falta dato requerido "security"')
		elif not re.match('^\w+\s\w+$',self.generalData["security"]):
			raise Exception('El campo "security" no es valido"') 


		if 'facilitiesPayment' not in self.operationData or self.operationData["facilitiesPayment"] is '':
			raise Exception('Falta dato requerido "facilitiesPayment"')


		if 'currencyCode' not in self.operationData or self.operationData["currencyCode"] is '':
			raise Exception('Falta dato requerido "currencyCode"')


		if 'operationDatetime' not in self.operationData or self.operationData["operationDatetime"] is '':
			raise Exception('Falta dato requerido "operationDatetime"')
		else:
			try:
				time.strptime(self.operationData["operationDatetime"], '%Y%m%d%H%M%S')
			except ValueError:
				raise Exception('El campo "operationDatetime" no tiene el formato "yyyyMMddHHmmss"')


		if 'currencyCode' not in self.operationData or self.operationData["currencyCode"] is '':
			raise Exception('Falta dato requerido "currencyCode"')


		if 'operationID' not in self.operationData or self.operationData["operationID"] is '':
			raise Exception('Falta dato requerido "operationID"')
		elif not re.match('[a-zA-Z0-9_]',self.operationData["operationID"]):
			raise Exception('El campo "operationID" no es valido"')	


		if 'amount' not in self.operationData or self.operationData["amount"] is '':
			raise Exception('Falta dato requerido "amount"')	
		elif not re.match('^[0-9]+(\,[0-9]{1,2})?$', self.operationData["amount"]):
			raise Exception('El formato de "amount" no es valido, no include decimales o no esta separado por coma')	


		if 'publicTokenizationField' not in self.tokenizationData or self.tokenizationData["publicTokenizationField"] is '':
			raise Exception('Falta dato requerido "publicTokenizationField"')
		elif not re.match('^\w+$',self.tokenizationData["publicTokenizationField"]):
			raise Exception('El campo "publicTokenizationField" no es valido"')
