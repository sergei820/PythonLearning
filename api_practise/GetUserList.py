import json
import jsonpath
import requests

# API URL
url = "https://reqres.in/"
endpoint = "api/users?page=2"

# Send Get Request
response = requests.get(url + endpoint)
# print(response)
# print(response.content)
# print(response.headers)

# Parse the response to JSON format

json_response = json.loads(response.text)
print(json_response)

# Fetch value using Json Path

pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
assert pages[0] == 2