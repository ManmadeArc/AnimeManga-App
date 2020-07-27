import TMO


class LectorTMO():
    def __init__(self):
        self.search=[]
        self.populars=[]
        self.Episodes=[]
        self.pictures=[]

    
    def get_populars(self):

        self.populars=TMO.get_populars()
    
    def make_search(self, query):
        self.search=TMO.search(query)
    
    def get_episodes(self, link):
        self.Episodes=TMO.get_episodeList(link)
    
    def get_chapter_info(self, link):
        self.pictures= TMO.get_images(link)
