import requests
import json
import copy as cp
import tioanime
from urllib.parse import unquote


class AnimeFlv():
    def __init(self):
        self.data={}
        self.Act_Ep={}
        self.Act_servers={}
        self.search={}
        self.Episodes={}
        self.servers={}


    def refresh_data(self):
        animes=tioanime.get_latest_episodes()    
        self.data=animes

    def get_anime_titles(self):
        animelist = []
        for name in self.data["episodes"]:
            animelist.append(name["title"])
        return animelist
    
    def act_data(self):
        return self.data["episodes"]
    
    def get_recent_servers(self, id):
        Data={}
        for Info in self.data["episodes"]:
            if Info["id"] == id:
            
                Data= cp.deepcopy(Info)
                del Data["poster"]

        self.Act_Ep = Data
        self.Act_servers= Data.get('servers',[])
    
    def search_Anime(self,Anime):
        aniList=tioanime.search(Anime)
        
        self.search=aniList


    def get_episodes(self,id):
        
        completed=False

        while not completed:
            try:
                for epiList in self.search['search']:
                    if epiList.get('title') == id:
                        self.Episodes=epiList
                        completed=True
            except:
                self.search_Anime(id)
            if not completed:
                self.search_Anime(id)

        

    
    def get_servers_id(self,id):
        self.servers=tioanime.get_servers(id,True)
        self.servers['title']=""
        self.servers['episode']=""
    
    def verify_name(self,name):
        (name)
        caracteres="abcdefghijklmnopqrstuvwxyz1234567890"
        palabra=list(name)
        x=0
        for i in palabra:
            if i.lower() not in caracteres:
                palabra[x]=' '
            x= x+1
        palabra=''.join(palabra)
        return palabra
       





        