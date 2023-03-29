import requests

url = "https://reqres.in/"
endpoint = "api/users?page=2"

response = requests.get(url + endpoint)
print(response)