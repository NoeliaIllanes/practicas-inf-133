import requests

url = 'http://localhost:5000/graphql'
query = """
{
  todas_las_plantas {
    id
    nombre_comun
    especie
    edad
    altura
    frutos
  }
}
"""
response = requests.post(url, json={'query': query})
plants = response.json()['data']['todas_las_plantas']
print(plants)

