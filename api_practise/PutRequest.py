import json
import jsonpath
import requests

# API URL
url = "https://reqres.in/"
endpoint = "api/users/2"

# Read JSON file

file = open("C:\\Learn\\PythonLearning\\resources\\UpdateUser.json",'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

# Make POST request with JSON body

response = requests.put(url + endpoint, request_json)
print(response.content)

assert response.status_code == 200

# Parse response to JSON format
response_json = json.loads(response.text)

# Pick ID using Json Path
update_time = jsonpath.jsonpath(response_json, 'updatedAt')
print(update_time)