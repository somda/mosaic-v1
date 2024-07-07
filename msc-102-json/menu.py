import json

def read_menu_from_json(json_path):
    with open(json_path, 'r') as file:
        menu = json.load(file)
    return menu
