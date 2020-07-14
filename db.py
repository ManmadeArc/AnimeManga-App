import json
import config_file

def savetheme(value):
    data={}
    data["theme"]= value
    with open('default.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_theme():
    try:
        with open('default.json') as file:
            data = json.load(file)
    except:
        with open('default.json', 'w') as file:
            data={}
            data["theme"]="komi"
            data['favorites']=[]
            json.dump(data, file, indent=4)
    return(data["theme"])

def get_theme_data():
    x = get_theme()
    return config_file.Config.theme[x]

def add_favorites(idx, title):
     
    with open('default.json','a') as file:
            data = json.load(file)
            anime={}
            anime["id"]=idx
            anime["title"]=title
            data["favorites"].append(anime)
            json.dump(data, file, indent=4)

def remove_favorites(title):
    with open('default.json','a') as file:
        data=json.load(file)
        anime=data['favorites']
        for i in range(len(anime)):
            if anime[i]['title']== title:
                anime.pop(i)
        data['favorites'] = anime
        json.dump(data, file, indent=4)
