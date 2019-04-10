# -*- coding: utf-8 -*-
import requests
import os.path, sys, warnings, copy, json
from suds.client import Client
from lib.bvg import BVG
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def deprecated(func):
	"""This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used."""
	def newFunc(*args, **kwargs):
		warnings.warn("Call to deprecated function %s." % func.__name__,
					  category=DeprecationWarning)
		return func(*args, **kwargs)
	newFunc.__name__ = func.__name__
	newFunc.__doc__ = func.__doc__
	newFunc.__dict__.update(func.__dict__)

	return newFunc

ver= '1.2.0'
restAppend = 'api/'

end_points_base = {
	"test" : "https://portal.integration.todopago.com.ar/",
	"prod" : "https://apis.todopago.com.ar/"
}

keys_order_GBRDT = (
	'MERCHANT',
	'STARTDATE',
	'ENDDATE',
	'PAGENUMBER'
)
keys_order_GBOI = (
	'MERCHANT',
	'OPERATIONID'
)

keys_order_GAPM = {
	'MERCHANT'	
}
#############################################

class TodoPagoConnectorBvg:

	def __init__(self, http_header, mode):
		#mode deberia contener un solo valor, que seria "test" o "prod", pero para mantener retrocompatibilidad se aceptara que manden el wsdl (este se ignorara) y el endpoint
		self._http_header = http_header

		self._end_point = end_points_base[mode]	
		self._end_point_rest_root = end_points_base[mode] + restAppend
		
	
	def discover(self):
		bvg = BVG(self._end_point) 
		discover = bvg.discoverPaymentMethods()

		return discover

	def transactions(self, transaction):
		bvg = BVG(self._end_point)
		transaction = bvg.getTransactions(transaction)

		return transaction

	def push(self, push):
		bvg = BVG(self._end_point)
		push = bvg.getNotificationPush(push)

		return push

	def loginbvtp(self, loginbvtp):
		bvg = BVG(self._end_point)
		loginbvtp = bvg.getLoginBvtp(loginbvtp)

		return loginbvtp

		

	################################################################
	###Methodo publico que devuelve las credenciales###############
	################################################################
	def getCredentials(self, user):
		return self._parse_rest_response(requests.post(self._end_point_rest_root+'Credentials', data = json.dumps(user), headers={'Content-Type':'application/json' ,'Accept' : 'application/json'},verify=False))

	def _parse_rest_response(self, response):
		return dict(response.json())

