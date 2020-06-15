import json
import config_file

def savetheme(value):
    data={}
    data["theme"]= value
    with open('default.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_theme():
    with open('default.json') as file:
        data = json.load(file)
    return(data["theme"])

def get_theme_data():
    x = get_theme()
    return config_file.Config.theme[x]

