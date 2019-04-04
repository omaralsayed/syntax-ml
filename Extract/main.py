from request_connection import url_to_soup, top_answers_stackoverflow
import json
import os

def get_json_obj():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_string = open(os.path.join(dir_path, "data.json")).read()
    json_obj = json.loads(json_string)
    return json_obj

def update_json():
    # read from .JSON file
    json_string = open("data.json").read()
    json_obj = json.loads(json_string)

    for language in json_obj["data"].keys():
        for command in json_obj["data"][language].keys():
            replacer = top_answers_stackoverflow(language + " " + command)
            json_obj["data"][language][command] = replacer 
    array_from_JSON = json_obj["data"][language].keys()
    # write to .JSON file
    # json_obj["data"]["Python"]["for loop"]="blah blah"
    file_out = open("data.json", "w")
    file_out.write(json.dumps(json_obj))

print(get_json_obj())