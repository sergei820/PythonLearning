import json
import jsonpath
import requests

# API URL
url = "https://reqres.in/"
endpoint = "api/users/2"

response = requests.delete(url + endpoint)

print(response.status_code)

assert response.status_code == 204