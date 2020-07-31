import json
import config_file

def savetheme(value):
    try:
        with open("default.json", "r") as file:
            data=json.load(file)
    except:
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
            data['Anime']=[]
            data['Manga']=[]
            json.dump(data, file, indent=4)
    return(data["theme"])

def get_theme_data():
    x = get_theme()
    return config_file.Config.theme[x]

def add_favorites(title, img):
    data=[]
    with open('default.json','r+') as file:
        data = json.load(file)
        anime={}
        anime["poster"]=img
        anime["title"]=title
        data["Anime"].append(anime)
    
    with open('default.json','w') as file:
        json.dump(data, file, indent=4)

def add_manga(title, img, link):
    data=[]
    with open('default.json','r+') as file:
        data = json.load(file)
        anime={}
        anime["img"]=img
        anime["title"]=title
        anime['link']=link
        data["Manga"].append(anime)
    
    with open('default.json','w') as file:
        json.dump(data, file, indent=4)

def remove_manga(title):
    data=[]
    with open('default.json','r') as file:
        data=json.load(file)
        anime=data['Manga']
        for i in range(len(anime)):
            if anime[i]['title'].strip()== title:
                anime.pop(i)
                break
        data['Manga'] = anime
    with open('default.json','w') as file:
        json.dump(data, file, indent=4)

def remove_favorites(title):
    data=[]
    with open('default.json','r') as file:
        data=json.load(file)
        anime=data['Anime']
        for i in range(len(anime)):
            if anime[i]['title']== title:
                anime.pop(i)
                break
        data['Anime'] = anime
    with open('default.json','w') as file:
        json.dump(data, file, indent=4)

def get_favorites(Anime=True):
    with open('default.json','r') as file:
        data = json.load(file)
        favList=[]
        if Anime:
            for anime in data["Anime"]:
                favList.append(anime['title'])
        else:
            for anime in data["Manga"]:
                favList.append(anime['title'])
        return favList

def get_favorites_full_data(Anime=True):
    data=[]
    with open('default.json','r+') as file:
        data = json.load(file)
    if Anime:
        for anime in data["Anime"]:
                anime['synopsis']=''
        return data["Anime"]
    else:
        return data["Manga"]
    
    
