import graphene

class Plant(graphene.ObjectType):
    id = graphene.Int()
    nombre_comun = graphene.String()
    especie = graphene.String()
    edad = graphene.Int()
    altura = graphene.Int()
    frutos = graphene.Boolean()

class Query(graphene.ObjectType):
    todas_las_plantas = graphene.List(Plant)

    def resolve_todas_las_plantas(root, info):
        
        plants = [
            {'id': 1, 'nombre_comun': 'Rosa', 'especie': 'Rosa spp.', 'edad': 12, 'altura': 50, 'frutos': False},
            {'id': 2, 'nombre_comun': 'Margarita', 'especie': 'Bellis perennis', 'edad': 8, 'altura': 30, 'frutos': False}
        ]
        return [Plant(**plant) for plant in plants]



schema = graphene.Schema(query=Query)

# Ejecutar el servidor GraphQL
from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
