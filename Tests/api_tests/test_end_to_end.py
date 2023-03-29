import requests
import json
import jsonpath

def test_add_new_data():
    APP_URL = "http://www.thetestingworld.com/api/studentsDetails"
    file = open("C:/Learn/PythonLearning/resources/StudentDetails.json", 'r')
    request_json = json.loads(file.read())
    response = requests.post(APP_URL, request_json)
    print(response.text)
    # id = jsonpath.jsonpath(response.json(), 'id')
    # print(id[0])