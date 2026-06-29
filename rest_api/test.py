import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/1/'   # Use an existing Product ID

data = requests.get(BASE_URL + ENDPOINT)

print(data)
print(data.status_code)
print(data.json())