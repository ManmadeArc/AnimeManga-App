import TMO


class LectorTMO():
    def __init__(self):
        self.search=[]
        self.populars=[]
        self.Episodes=[]
        self.pictures=[]

    
    def need_refresh(self):
        if self.populars==[]:
            return True
        else:
            if self.populars[0]==TMO.get_last_popular():
                return False
            else:
                return True

    def get_populars(self):
        print(self.need_refresh())
        if  self.need_refresh():
            self.populars=TMO.get_populars()
        
    
    def make_search(self, query):
        self.search=TMO.search(query)
    
    def get_episodes(self, link):
        self.Episodes=TMO.get_episodeList(link)
    
    def get_chapter_info(self, link):
        self.pictures= TMO.get_images(link)
