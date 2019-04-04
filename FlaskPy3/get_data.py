import json
import os

def get_json_obj():
    json_string = open("data.json").read()
    json_obj = json.loads(json_string)
    return json_obj
