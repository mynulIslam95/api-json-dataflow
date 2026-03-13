import requests

url = "https://api.agify.io/?name=mynul"

response = requests.get(url)

data = response.json()

name = data["name"]
age = data["age"]

print("Name:", name)
print("Predicted age:", age)