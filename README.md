<a name="inicio"></a>
Todo Pago - módulo SDK-Python para conexión con gateway de pago
=======

+ [Instalación](#instalacion)
   + [Versiones de Python soportadas](#Versionesdepysoportadas)
   + [Generalidades](#general)
+ [Uso](#uso)
    + [Inicializar la clase correspondiente al conector](#initconector)
    + [Ambientes](#test)
    + [Billetera Virtual para Gateway](#bvg)
      + [Diagrama de secuencia](#bvg-uml)
      + [Discover](#bvg-discover)
      + [Transaction](#bvg-transaction)
      + [Notificacion Push](#bvg-push)
      + [Obtener Credenciales](#credenciales)

<a name="instalacion"></a>
## Instalación
Se recomienda descargar la ultima version del SDK desde Github, luego de descargar el paquete se debe instanciar la clase TodoPagoConnectorBvg dentro de la carpeta lib con los parametros indicados en la seccion "inicializar la clase correspondiente".

#### Librerias a instalar:
> pip install unittest #test unitarios


<a name="Versionesdepysoportadas"></a>

#### 1. Versiones de Python soportadas
La versión implementada de la SDK, esta testeada para versiones desde Python 2.7 en adelante.

<a name="general"></a>
#### 2. Generalidades
Esta versión soporta únicamente pago en moneda nacional argentina (CURRENCYCODE = 32).
Todos los métodos devuelven la respuesta en forma de diccionario.
[<sub>Volver a inicio</sub>](#inicio)

<a name="uso"></a>

## Uso
<a name="initconector"></a>
### Inicializar la clase correspondiente al conector (TodoPagoConnectorBvg).

- crear un JSON con los http header suministrados por todo pago
```python
j_header_http = {
    "Authorization":"PRISMA f3d8b72c94ab4a06be2ef7c95490f7d3"
}
```
- crear una instancia de la clase TodoPago para hacer pruebas en el ambiente developers se pasa como modo "test" y para producción "prod".

```python
bvg = TodoPagoConnectorBvg(j_header_http, 'test')

```

<a name="caracteristicas"></a>
## Características

<a name="bvg"></a>
### Billetera Virtual para Gateway
<p>La Billetera Virtual para Gateways es la versión de Todo Pago para los comercios que permite utilizar los servicios de la billetera TodoPago dentro de los e-commerce, respetando y manteniendo sus respectivas promociones con bancos y marcas y números de comercio (métodos de adquirencia). Manteniendo su Gateway de pago actual, y utilizando BVG para la selección del medio de pago y la tokenizacion de la información para mayor seguridad en las transacciones.</p>

<a name="bvg-uml"></a>
#### Diagrama de secuencia
![Diagrama de Secuencia BVG](http://www.plantuml.com/plantuml/png/ZL9BJiCm4Dtd5BDi5roW2oJw0I7ngMWlC3ZJOd0zaUq4XJknuWYz67Q-JY65bUNHlFVcpHiKZWqib2JjACdGE2baXjh1DPj3hj187fGNV20ZJehppTNWVuEEth5C4XHE5lxJAJGlN5nsJ323bP9xWWptQ42mhlXwQAlO0JpOTtZSXfMNT0YFcQzhif1MD0oJfRI22pBJdYYm1jnG-ubinjhZjcXUoQ654kQe1TiafG4srczzpE0-9-iC0f-CSDPgQ3v-wQvtLAVskTB5yHE156ISofG33dEVdFp0ccYoDQXje64z7N4P1iN_cRgZmkU8yH48Gm4JLIA3VJM0UIzrRob2H6s_xl1PAaME38voRqYH28l6DgzJqjxpaegSLE6JvJVIthZNu7BW83BVtAp7hVqTLcVezrr3Eo_jORVD8wTaoERAOHMKgXEErjwI_CpvLk_yS1ZX6pXCrhbzUM0dTsKJRoJznsMUdwOZYMirnpS0)

Para acceder al servicio, los vendedores podrán adherirse en el sitio exclusivo de Botón o a través de su ejecutivo comercial. En estos procesos se generará el usuario y clave para este servicio.

<a name="bvg-discover"></a>
##### Discover

<p>El método discover permite conocer los medios de pago disponibles</p>

+ Instanciar el conector
+ Instanciar el la clase Discover
+ Se pasa Discover por parametro al metodo discoverPaymentMethods del conector. Este devuelve el objeto Discover con los medios de pago asignados en el atributo paymentMethods Ejemplo:

```python
####################################  DiscoverPaymentMethods   ############################################
from lib.todopagoconnectorbvg import TodoPagoConnectorBvg
import json

j_header_http = {
'Authorization':'TODOPAGO 1540601877EB2059EF50240E46ABD10E'
}

bvg = TodoPagoConnector(j_header_http, "test")

discover = bvg.discoverPaymentMethods()
print(discover.paymentMethods)
```

El contenido de la respuesta es la siguiente:

 Descripción | Tipo de dato | Ejemplo |		     |
-------------|------------------------|--------------|--------
id           | Id del medio de pago   | numérico     | 42
nombre       | Marca de la tarjeta    | string       | "VISA"
tipo         | Tipo de medio de pago  | string       | "Crédito"
idBanco      | Id del banco           | numérico     | 10
nombreBanco  | Nombre del banco       | string       | "Banco Ciudad"

<a name="bvg-transaction"></a>
##### Transaction

<p>El método transaction permite registrar una transacción.</p>

+ Instanciar el conector
+ Instanciar la clase Transaction
+ Se pasa por parametro el objeto Transaction al metodo transactions del conector. Esto devuelve el objeto Transaction con la respuesta de la consulta en el atributo response. Ejemplo:

```python
#######################################    TRANSACTION   ##################################################
from lib.todopagoconnectorbvg import TodoPagoConnectorBvg
from lib.transaction import *
from lib.user import *
from lib.bvg import *
import json


j_header_http = {
'Authorization':'TODOPAGO 1540601877EB2059EF50240E46ABD10E'
}

j_wsdls = {
'Operations': 'Operations',
'Authorize': 'Authorize'
}


bvg = TodoPagoConnectorBvg(j_header_http, "test")

generalData = {}
generalData["merchant"] = "1"
generalData["security"] = "PRISMA 86333EFD8AD0C71CEA3BF06D7BDEF90D"
generalData["operationDatetime"] = "201604251556134"
generalData["remoteIpAddress"] = "192.168.11.87"
generalData["channel"] = "BVTP"

operationData = {}
operationData["operationType"] = "Compra"
operationData["operationID"] = "1234"
operationData["currencyCode"] = "032"
operationData["concept"] = "compra"
operationData["amount"] = "999,99"

availablePaymentMethods = ["1", "42"]
operationData["availablePaymentMethods"] = availablePaymentMethods

buyerPreselection = {}
buyerPreselection["paymentMethodId"] = "42"
buyerPreselection["bankId"] = "11"
operationData["buyerPreselection"] = buyerPreselection


# Esto es no obligatorio , puede mandarse un hash vacio
technicalData = {}
technicalData["sdk"] = "Ruby"
technicalData["sdkversion"] = "1.4"
technicalData["lenguageversion"] = "1.8"
technicalData["pluginversion"] = "2.1"
technicalData["ecommercename"] = "DH-gate"
technicalData["ecommerceversion"] = "3.1"
technicalData["cmsversion"] = "2.4"



transaction = Transaction()
transaction.inicializar(generalData, operationData, technicalData)

transaction = bvg.transactions(transaction)

print(transaction)
```

#### Datos de referencia

<table>
<tr><th>Nombre del campo</th><th>Required/Optional</th><th>Data Type</th><th>Comentarios</th></tr>
<tr><td>security</td><td>Required</td><td>String</td><td>Campo de autorización que deberá contener el valor del api key de la cuenta del vendedor (Merchant)</td></tr>
<tr><td>operationDatetime</td><td>Required</td><td>String</td><td>Fecha Hora de la invocación en Formato yyyyMMddHHmmssSSS</td></tr>
<tr><td>remoteIpAddress</td><td>Required</td><td>String</td><td>IP desde la cual se envía el requerimiento</td></tr>
<tr><td>merchant</td><td>Required</td><td>String</td><td>ID de cuenta del vendedor</td></tr>
<tr><td>operationType</td><td>Optional</td><td>String</td><td>Valor fijo definido para esta operatoria de integración</td></tr>
<tr><td>operationID</td><td>Required</td><td>String</td><td>ID de la operación en el eCommerce</td></tr>
<tr><td>currencyCode</td><td>Required</td><td>String</td><td>Valor fijo 32</td></tr>
<tr><td>concept</td><td>Optional</td><td>String</td><td>Especifica el concepto de la operación</td></tr>
<tr><td>amount</td><td>Required</td><td>String</td><td>Formato 999999999,99</td></tr>
<tr><td>availablePaymentMethods</td><td>Optional</td><td>Array</td><td>Array de Strings obtenidos desde el servicio de descubrimiento de medios de pago. Lista de ids de Medios de Pago habilitados para la transacción. Si no se envía están habilitados todos los Medios de Pago del usuario.</td></tr>
<tr><td>availableBanks</td><td>Optional</td><td>Array</td><td>Array de Strings obtenidos desde el servicio de descubrimiento de medios de pago. Lista de ids de Bancos habilitados para la transacción. Si no se envía están habilitados todos los bancos del usuario.</td></tr>
<tr><td>buyerPreselection</td><td>Optional</td><td>BuyerPreselection</td><td>Preselección de pago del usuario</td></tr>
<tr><td>sdk</td><td>Optional</td><td>String</td><td>Parámetro de versión de API</td></tr>
<tr><td>sdkversion</td><td>Optional</td><td>String</td><td>Parámetro de versión de API</td></tr>
<tr><td>lenguageversion</td><td>Optional</td><td>String</td><td>Parámetro de versión de API</td></tr>
<tr><td>pluginversion</td><td>Optional</td><td>String</td><td>Parámetro de versión de API</td></tr>
<tr><td>ecommercename</td><td>Optional</td><td>String</td><td>Parámetro de versión de API</td></tr>
<tr><td>ecommerceversion</td><td>Optional</td><td>String</td><td>Parámetro de versión de API</td></tr>
<tr><td>cmsversion</td><td>Optional</td><td>String</td><td>Parámetro de versión de API</td></tr>
</table>
<br>
<strong>BuyerPreselection</strong>
<br>
<table>
<tr><th>Nombre del campo</th><th>Data Type</th><th>Comentarios</th></tr>
<tr><td>paymentMethodId</td><td>String</td><td>Id del medio de pago seleccionado</td></tr>
<tr><td>bankId</td><td>String</td><td>Id del banco seleccionado</td></tr>
</table>

<a name="bvg-push"></a>
##### Notificacion Push

<p>El método pushnotify permite registrar la finalización de una transacción.</p>

+ Instanciar el conector
+ Instanciar la clase PushNotification
+ Se pasa por parametro el objeto PushNotification al metodo PushNotification del conector. Esto devuelve el objeto PushNotification con la respuesta de la consulta en el atributo response. Ejemplo:

```python
from lib.todopagoconnectorbvg import TodoPagoConnectorBvg
from lib.transaction import *
import time
import json

class Clase:
    key=None
    def __init__(self, transaction):
        self.key = transaction["publicRequestKey"]


j_header_http = {
'Authorization':'PRISMA 86333EFD8AD0C71CEA3BF06D7BDEF90D'
}

bvg = TodoPagoConnectorBvg(j_header_http, "test")

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

availablePaymentMethods = [1, 42]
operationData["availablePaymentMethods"] = availablePaymentMethods
operationData["availableBanks"] = []

buyerPreselection = {}
buyerPreselection["paymentMethodId"] = "42"
buyerPreselection["bankId"] = 11
operationData["buyerPreselection"] = buyerPreselection 
# Esto es no obligatorio , puede mandarse un hash vacio
technicalData = {}
technicalData["sdk"] = "Python"
technicalData["sdkversion"] = "1.4"
technicalData["lenguageversion"] = "1.8"
technicalData["pluginversion"] = "2.1"
technicalData["ecommercename"] = "DH-gate"
technicalData["ecommerceversion"] = "3.1"
technicalData["cmsversion"] = "2.4"

tokenizationData = {}
tokenizationData["publicTokenizationField"] = "sydguyt3e862t76ierh76487638rhkh7"
tokenizationData["credentialMask"] = "4510XXXXX00001"

transaction = Transaction()
transaction.inicializar(generalData, operationData, technicalData)

transaction = bvg.transactions(transaction)

print(transaction.getResponse())

```

#### Datos de referencia

<table>
<tr><th>Nombre del campo</th><th>Required/Optional</th><th>Data Type</th><th>Comentarios</th></tr>
<tr><td>Security</td><td>Required</td><td>String</td><td>Authorization que deberá contener el valor del api key de la cuenta del vendedor (Merchant). Este dato viaja en el Header HTTP</td></tr>
<tr><td>Merchant</td><td>Required</td><td>String</td><td>ID de cuenta del comercio</td></tr>
<tr><td>RemoteIpAddress</td><td>Optional</td><td>String</td><td>IP desde la cual se envía el requerimiento</td></tr>
<tr><td>PublicRequestKey</td><td>Required</td><td>String</td><td>publicRequestKey de la transacción creada. Ejemplo: 710268a7-7688-c8bf-68c9-430107e6b9da</td></tr>
<tr><td>OperationName</td><td>Required</td><td>String</td><td>Valor que describe la operación a realizar, debe ser fijo entre los siguientes valores: “Compra”, “Devolucion” o “Anulacion”</td></tr>
<tr><td>ResultCodeMedioPago</td><td>Optional</td><td>String</td><td>Código de respuesta de la operación propocionado por el medio de pago</td></tr>
<tr><td>ResultCodeGateway</td><td>Optional</td><td>String</td><td>Código de respuesta de la operación propocionado por el gateway</td></tr>
<tr><td>idGateway</td><td>Optional</td><td>String</td><td>Id del Gateway que procesó el pago. Si envían el resultCodeGateway, es obligatorio que envíen este campo</td></tr>
<tr><td>ResultMessage</td><td>Optional</td><td>String</td><td>Detalle de respuesta de la operación.</td></tr>
<tr><td>OperationDatetime</td><td>Required</td><td>String</td><td>Fecha Hora de la operación en el comercio en Formato yyyyMMddHHmmssMMM</td></tr>
<tr><td>TicketNumber</td><td>Optional</td><td>String</td><td>Numero de ticket generado</td></tr>
<tr><td>CodigoAutorizacion</td><td>Optional</td><td>String</td><td>Codigo de autorización de la operación</td></tr>
<tr><td>CurrencyCode</td><td>Required</td><td>String</td><td>Valor fijo 32</td></tr>
<tr><td>OperationID</td><td>Required</td><td>String</td><td>ID de la operación en el eCommerce</td></tr>
<tr><td>Amount</td><td>Required</td><td>String</td><td>Formato 999999999,99</td></tr>
<tr><td>FacilitiesPayment</td><td>Required</td><td>String</td><td>Formato 99</td></tr>
<tr><td>Concept</td><td>Optional</td><td>String</td><td>Especifica el concepto de la operación dentro del ecommerce</td></tr>
<tr><td>PublicTokenizationField</td><td>Required</td><td>String</td><td></td></tr>
<tr><td>CredentialMask</td><td>Optional</td><td>String</td><td></td></tr>
</table>

[<sub>Volver a inicio</sub>](#inicio)



<a name="credenciales"></a>
#### Obtener credenciales
El SDK permite obtener las credenciales "Authentification", "MerchandId" y "Security" de la cuenta de Todo Pago, ingresando el usuario y contraseña.<br>
Esta funcionalidad es útil para obtener los parámetros de configuración dentro de la implementación.

- Crear una instancia de la clase User:
```python

j_header_http = {
	'Authorization':''
}

tpc = TodoPagoConnector(j_header_http, "test")

#usario de TodoPago
datosUsuario = {
	'USUARIO' : "usuario@todopago.com.ar",
	'CLAVE' : "contraseña"
}

#este método devuelve un json con las credenciales
tpc.getCredentials(userCredenciales);

```
**Observación**: El Security se obtiene a partir de apiKey, eliminando TODOPAGO de este último.

[<sub>Volver a inicio</sub>](#inicio)
<br>
