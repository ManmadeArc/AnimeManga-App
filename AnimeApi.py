import requests
import json
import copy as cp


class AnimeFlv():
    def __init(self):
        self.data={}
        self.Act_Ep={}
        self.Act_servers={}

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


        