from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

#Funciones que devuelven la suma, resta, multiplicacion y division de 2 numeros

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

# Creamos la ruta del servidor SOAP
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)
#Registro de las funciones suma,resta, multiplicacion y division
#en el servicio SOAP.
server.registerFunction(suma)
server.registerFunction(resta)
server.registerFunction(multiplicacion)
server.registerFunction(division)

# Iniciamos el servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()