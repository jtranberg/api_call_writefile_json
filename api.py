import requests
import json


def api():
    response = requests.get("https://dummyjson.com/products/")
    file = response.json()
    # print(response.json())

    jsonString = json.dumps(file)
    jsonFile = open("products.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
api()

def api2():
    parameters ={"limit":1}
    response = requests.get("https://dummyjson.com/products/", params =parameters)
    file = response.json()
    # print(response.json())

    jsonString = json.dumps(file)
    jsonFile = open("products1.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
api2()
