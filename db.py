import json

def savetheme(value):
    data={}
    data["theme"]= value
    with open('default.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_theme():
    with open('default.json') as file:
        data = json.load(file)
    print(data["theme"])
    return(data["theme"])