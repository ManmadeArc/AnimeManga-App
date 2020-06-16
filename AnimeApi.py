import requests
import json


class AnimeFlv():
    def __init(self):
        self.data={}

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
    
