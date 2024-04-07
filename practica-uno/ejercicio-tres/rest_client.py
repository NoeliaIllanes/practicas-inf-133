import requests

def crear_paciente(ci, nombre, apellido, edad, genero, diagnostico=None, doctor=None):
    url = 'http://localhost:8000/pacientes'
    data = {
        'ci': ci,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'genero': genero,
        'diagnostico': diagnostico,
        'doctor': doctor
    }
    response = requests.post(url, json=data)
    return response.json()

def obtener_pacientes():
    url = 'http://localhost:8000/pacientes'
    response = requests.get(url)
    return response.json()


