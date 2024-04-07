import requests

# URL base del servidor
BASE_URL = 'http://localhost:8000'

# crear un animal
def crear_animal(nombre, especie, genero, edad, peso):
    url = f'{BASE_URL}/animales'
    data = {'nombre': nombre, 'especie': especie, 'genero': genero, 'edad': edad, 'peso': peso}
    response = requests.post(url, json=data)
    return response.json()

#  para listar todos los animales
def obtener_animales():
    url = f'{BASE_URL}/animales'
    response = requests.get(url)
    return response.json()

#  para buscar animales por especie
def buscar_por_especie(especie):
    url = f'{BASE_URL}/animales?especie={especie}'
    response = requests.get(url)
    return response.json()

# Función para buscar animales por género
def buscar_por_genero(genero):
    url = f'{BASE_URL}/animales?genero={genero}'
    response = requests.get(url)
    return response.json()

# Función para actualizar la información de un animal
def actualizar_animal(id, nombre, especie, genero, edad, peso):
    url = f'{BASE_URL}/animales/{id}'
    data = {'nombre': nombre, 'especie': especie, 'genero': genero, 'edad': edad, 'peso': peso}
    response = requests.put(url, json=data)
    return response.json()

# Función para eliminar un animal
def eliminar_animal(id):
    url = f'{BASE_URL}/animales/{id}'
    response = requests.delete(url)
    return response.json()

# Ejemplo de uso del cliente REST
if __name__ == '__main__':
    # Crear un animal
    print(crear_animal('Leo', 'León', 'Macho', 5, 150))

    # Listar todos los animales
    print(obtener_animales())

    # Buscar animales por especie
    print(buscar_por_especie('León'))

    # Buscar animales por género
    print(buscar_por_genero('Hembra'))

    # Actualizar la información de un animal
    print(actualizar_animal(1, 'Leo', 'León', 'Macho', 6, 160))

    # Eliminar un animal
    print(eliminar_animal(1))
