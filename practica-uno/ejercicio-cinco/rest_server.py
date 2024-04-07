from flask import Flask, jsonify, request

app = Flask(__name__)

#  almacenar los animales
animales = []

# clase Animal
class Animal:
    def __init__(self, id, nombre, especie, genero, edad, peso):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad
        self.peso = peso

# crear un animal
@app.route('/animales', methods=['POST'])
def crear_animal():
    data = request.json
    animal = Animal(len(animales) + 1, data['nombre'], data['especie'], data['genero'], data['edad'], data['peso'])
    animales.append(animal)
    return jsonify({'mensaje': 'Animal creado exitosamente', 'animal': animal.__dict__}), 201

# para listar todos los animales
@app.route('/animales', methods=['GET'])
def obtener_animales():
    return jsonify([animal.__dict__ for animal in animales]), 200

#  para buscar animales por especie
@app.route('/animales', methods=['GET'])
def buscar_por_especie():
    especie = request.args.get('especie')
    animales_por_especie = [animal.__dict__ for animal in animales if animal.especie == especie]
    return jsonify(animales_por_especie), 200

# para buscar animales por género
@app.route('/animales', methods=['GET'])
def buscar_por_genero():
    genero = request.args.get('genero')
    animales_por_genero = [animal.__dict__ for animal in animales if animal.genero == genero]
    return jsonify(animales_por_genero), 200

# para actualizar la información de un animal
@app.route('/animales/<int:id>', methods=['PUT'])
def actualizar_animal(id):
    data = request.json
    for animal in animales:
        if animal.id == id:
            animal.nombre = data['nombre']
            animal.especie = data['especie']
            animal.genero = data['genero']
            animal.edad = data['edad']
            animal.peso = data['peso']
            return jsonify({'mensaje': 'Animal actualizado exitosamente', 'animal': animal.__dict__}), 200
    return jsonify({'mensaje': 'Animal no encontrado'}), 404

# para eliminar un animal
@app.route('/animales/<int:id>', methods=['DELETE'])
def eliminar_animal(id):
    for animal in animales:
        if animal.id == id:
            animales.remove(animal)
            return jsonify({'mensaje': 'Animal eliminado exitosamente', 'animal': animal.__dict__}), 200
    return jsonify({'mensaje': 'Animal no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
