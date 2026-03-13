import requests

def fetch_age_data(name):
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url)
    return response

def fetch_gender_data(name):
    url = f"https://api.genderize.io/?name={name}"
    response = requests.get(url)
    return response

def fetch_country_data(name):
    url = f"https://api.nationalize.io/?name={name}"
    response = requests.get(url)
    return response