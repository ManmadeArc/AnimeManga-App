import requests
import json
import copy as cp
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
        animes= requests.get("https://animeflv.chrismichael.now.sh/api/v1/LatestEpisodesAdded")
        while int(animes.status_code) != 200:
            animes= requests.get("https://animeflv.chrismichael.now.sh/api/v1/LatestEpisodesAdded")     
        self.data= animes.json()

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
        aniList=requests.get("https://animeflv.chrismichael.now.sh/api/v1/Search/"+str(Anime))
        
        self.search=aniList.json()


    def get_episodes(self,id):
        for epiList in self.search['search']:
            if epiList.get('title') == id:
                self.Episodes=epiList
                self.Episodes['episodes'].pop(0)
    
    def get_servers_id(self,id,title, episode):
        servers=requests.get("https://animeflv.chrismichael.now.sh/api/v1/GetAnimeServers/"+str(id))
        self.servers=servers.json()
        self.servers['title']=unquote(title)
        self.servers['episode']=episode
        with open('search.json', 'w') as file:
            json.dump(self.servers, file, indent=4)
       





        