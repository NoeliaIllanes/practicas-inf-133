from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/plants', methods=['GET'])
def get_plants():
    
    plants = [
        {'id': 1, 'nombre_comun': 'Rosa', 'especie': 'Rosa spp.', 'edad': 12, 'altura': 50, 'frutos': False},
        {'id': 2, 'nombre_comun': 'Margarita', 'especie': 'Bellis perennis', 'edad': 8, 'altura': 30, 'frutos': False}
    ]
    return jsonify(plants)



if __name__ == '__main__':
    app.run(debug=True)
