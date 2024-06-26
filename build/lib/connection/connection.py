import json
import requests
from flask import request, jsonify

def connection():
    json_open = open('param.json', 'r')
    json_load = json.load(json_open)
    print(json_load)
    print("\n")

    service_type = json_load['service']['type']
    service_endpoint = json_load['service']['endpoint']

    if(service_type == "pull"):
        #for parameters in json_load["parameters"]:
        #    values.append(parameters)
        parameters = json_load.get('parameters', {})
        print(parameters)
        print("\n")
    response = requests.post(service_endpoint, data=json.dumps(parameters), headers={"Content-Type": "application/json"}, stream=True) 
    print("send requests")

    print (response)
    return response

def extraction():
    json_open = open('i_param.json', 'r')
    json_load = json.load(json_open)
    #print(json_load)
    parameters = json_load.get('parameters', {})
    key_param = parameters.keys()
    print(key_param)
    post_data = request.get_json(force=True)
    key_request = post_data.keys()

    if(key_param == key_request):
        print("Acknowledging the request")
        #print("post_data " + type(post_data))
        return "success", post_data
    else:
        print("Parameter mismatch")
        return "fail", 0