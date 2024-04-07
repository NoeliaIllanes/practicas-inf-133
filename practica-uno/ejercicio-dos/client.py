import requests

url = 'http://localhost:5000/plants'
response = requests.get(url)
plants = response.json()
print(plants)

