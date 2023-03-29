import json
import jsonpath
import requests

# API URL
url = "https://reqres.in/"
endpoint = "api/users"

# Read JSON file

file = open("C:\\Learn\\PythonLearning\\resources\\CreateUser.json",'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

# Make POST request with JSON body

response = requests.post(url + endpoint, request_json)
print(response.content)

assert response.status_code == 201

# Parse response to JSON format
response_json = json.loads(response.text)

# Pick ID using Json Path
id = jsonpath.jsonpath(response_json, 'id')
print(id)       # ['846']
print(id[0])    # 846