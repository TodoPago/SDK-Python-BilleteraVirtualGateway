import sys
sys.path.append("..")
from todopagoconnectorbvg import TodoPagoConnectorBvg
from credentialsdata import CredentialsData
import unittest
from unittest import TestCase
if sys.version_info[0] >= 3 :
	from unittest.mock import patch, Mock
else:
	from mock import patch, Mock, MagicMock


class CredentialsTest(TestCase):
	
	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')
	def test_get_credentials_ok(self, MockTodoPagoConnectorBvg):
		j_header_http = {
			'Authorization':'TODOPAGO 18ea370805e7471da5ea8c6879b61f22'
		}

		MTPConnectorBvg = MockTodoPagoConnectorBvg(j_header_http, "test")

		instanceCredential = CredentialsData()

		MTPConnectorBvg.getCredentials.return_value = instanceCredential.get_credentials_ok_response()

		UserAccount = {
			'USUARIO' : "usuario@gmail.com", 
			'CLAVE' : "2017todopago"
		}

		responseGetCredential = MTPConnectorBvg.getCredentials(UserAccount)

		self.assertEquals(responseGetCredential['Credentials']['resultado']['codigoResultado'], 0)
		self.assertTrue(len(responseGetCredential['Credentials']['merchantId']))
		self.assertTrue(len(responseGetCredential['Credentials']['APIKey']))
	
	
	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')	
	def test_get_credentials_user_empty(self, MockTodoPagoConnectorBvg):
		j_header_http = {
			'Authorization':'TODOPAGO 18ea370805e7471da5ea8c6879b61f22'
		}

		MTPConnectorBvg = MockTodoPagoConnectorBvg(j_header_http, "test")

		instanceCredential = CredentialsData()

		MTPConnectorBvg.getCredentials.return_value = instanceCredential.get_credentials_wrong_user_response()

		UserAccount = {
			'USUARIO' : "usuario@gmail.com", 
			'CLAVE' : "2017todopago"
		}

		responseGetCredential = MTPConnectorBvg.getCredentials(UserAccount)

		self.assertEquals(responseGetCredential['Credentials']['resultado']['codigoResultado'], 1050)
		self.assertFalse(len(responseGetCredential['Credentials']['merchantId']))
		self.assertFalse(len(responseGetCredential['Credentials']['APIKey']))

	
	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')		
	def test_get_credentials_pass_empty(self, MockTodoPagoConnectorBvg):		
		j_header_http = {
			'Authorization':'TODOPAGO 18ea370805e7471da5ea8c6879b61f22'
		}

		MTPConnectorBvg = MockTodoPagoConnectorBvg(j_header_http, "test")

		instanceCredential = CredentialsData()
		
		MTPConnectorBvg.getCredentials.return_value = instanceCredential.get_credentials_wrong_password_response()

		UserAccount = {
			'USUARIO' : "usuario@gmail.com", 
			'CLAVE' : ""
		}

		responseGetCredential = MTPConnectorBvg.getCredentials(UserAccount)
		
		self.assertEquals(responseGetCredential['Credentials']['resultado']['codigoResultado'], 1055)
		self.assertFalse(len(responseGetCredential['Credentials']['merchantId']))
		self.assertFalse(len(responseGetCredential['Credentials']['APIKey']))
	

if __name__ == '__main__':
	unittest.main()
