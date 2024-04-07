from zeep import Client

client = Client('http://localhost:8000')

#Se llama las funciones registradas en el servidor SOAP
print ("El resultado de la suma es: ", server.suma(5,10))
print ("El resultado de la resta es: ",server.resta(20,5))
print ("El resultado de la multiplicacion es: ", server.multiplicacion(10,5))
print ("El resultado de la division es: ", server.division(10,3))