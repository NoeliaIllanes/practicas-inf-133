from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    diagnostico = db.Column(db.String(100), nullable=True)
    doctor = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Paciente(ci={self.ci}, nombre={self.nombre}, apellido={self.apellido}, edad={self.edad}, genero={self.genero}, diagnostico={self.diagnostico}, doctor={self.doctor})>'

class PacienteBuilder:
    def __init__(self):
        self.ci = None
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.genero = None
        self.diagnostico = None
        self.doctor = None

    def set_ci(self, ci):
        self.ci = ci
        return self

    def set_nombre(self, nombre):
        self.nombre = nombre
        return self

    def set_apellido(self, apellido):
        self.apellido = apellido
        return self

    def set_edad(self, edad):
        self.edad = edad
        return self

    def set_genero(self, genero):
        self.genero = genero
        return self

    def set_diagnostico(self, diagnostico):
        self.diagnostico = diagnostico
        return self

    def set_doctor(self, doctor):
        self.doctor = doctor
        return self

    def build(self):
        return Paciente(ci=self.ci, nombre=self.nombre, apellido=self.apellido, edad=self.edad, genero=self.genero, diagnostico=self.diagnostico, doctor=self.doctor)

@app.route('/pacientes', methods=['POST'])
def crear_paciente():
    data = request.json
    paciente_builder = PacienteBuilder()
    paciente = paciente_builder.set_ci(data['ci']).set_nombre(data['nombre']).set_apellido(data['apellido']).set_edad(data['edad']).set_genero(data['genero']).set_diagnostico(data.get('diagnostico')).set_doctor(data.get('doctor')).build()
    db.session.add(paciente)
    db.session.commit()
    return jsonify({'mensaje': 'Paciente creado exitosamente', 'paciente': paciente.__dict__}), 201

@app.route('/pacientes', methods=['GET'])
def obtener_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([paciente.__dict__ for paciente in pacientes]), 200

if __name__ == '__main__':
    app.run(debug=True)
