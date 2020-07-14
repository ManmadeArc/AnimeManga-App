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

def add_favorites(img, title):
    data=[]
    with open('default.json','r+') as file:
        data = json.load(file)
        anime={}
        anime["img"]=img
        anime["title"]=title
        data["favorites"].append(anime)
    
    with open('default.json','w') as file:
        json.dump(data, file, indent=4)

def remove_favorites(title):
    data=[]
    with open('default.json','r') as file:
        data=json.load(file)
        anime=data['favorites']
        for i in range(len(anime)):
            if anime[i]['title']== title:
                anime.pop(i)
                break
        data['favorites'] = anime
    with open('default.json','w') as file:
        json.dump(data, file, indent=4)

def get_favorites():
    with open('default.json','r+') as file:
        data = json.load(file)
        favList=[]
        for anime in data["favorites"]:
            favList.append(anime['title'])
    return favList
