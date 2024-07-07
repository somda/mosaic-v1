import requests
import json

AUTH_URL = "http://localhost:3000/api/v1/oauth/token"
OFFERS_URL = "http://localhost:3000/api/v1/microservice/offers"

def get_access_token():
    payload = json.dumps({
        "grant_type": "password",
        "email": "microservice_01@example.com",
        "password": "password",
        "client_id": "-va7X0e6ijZX5ngIXvgQu-EUuLhrCVBnGxo4xiEw-a8",
        "client_secret": "ZD3Zut-Fb0FyLucg48LfZuBNWA7jsnnDvynyqmB6pn0"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(AUTH_URL, headers=headers, data=payload)
    response_data = response.json()
    return response_data['access_token']

def get_offers():
    token = get_access_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(OFFERS_URL, headers=headers)
    return response.json()
