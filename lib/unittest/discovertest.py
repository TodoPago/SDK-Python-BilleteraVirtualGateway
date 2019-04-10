import sys
sys.path.append("..")
from todopagoconnectorbvg import TodoPagoConnectorBvg
from discoverdata import DiscoverData
import unittest
from unittest import TestCase
if sys.version_info[0] >= 3 :
	from unittest.mock import patch, Mock
else:
	from mock import patch, Mock, MagicMock

class discoverTest(TestCase):

	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')
	def test_discover_response_ok(self, MockTodoPagoConnectorBvg):
		header_http = {
			'Authorization':'TODOPAGO 18ea370805e7471da5ea8c6879b61f22'
		}

		MTPConnector = MockTodoPagoConnectorBvg(header_http, "test")

		instanceDiscover = DiscoverData()

		MTPConnector.discover.return_value = instanceDiscover.get_discover_ok_response()

		discoverResponse = MTPConnector.discover()

		self.assertGreater(len(discoverResponse[0]),0)
	
	@patch('todopagoconnectorbvg.TodoPagoConnectorBvg')
	def test_get_discover_fail_response(self, MockTodoPagoConnectorBvg):
		header_http = {
			'Authorization':'TODOPAGO f3d8b72c94ab4a06be2ef7c95490f7d3'
		}

		MTPConnector = MockTodoPagoConnectorBvg(header_http, "test")

		instanceDiscover = DiscoverData()
		
		MTPConnector.discover.return_value = instanceDiscover.get_discover_fail_response()

		discoverResponse = MTPConnector.discover()

		self.assertEqual(len(discoverResponse), 0)

if __name__ == '__main__':
	unittest.main()
