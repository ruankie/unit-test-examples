import json

def read_json(file_path):
    with open(file_path) as file_contents:
        json_data = json.load(file_contents)
    return json_data