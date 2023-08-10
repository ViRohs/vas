
import requests
from bs4 import BeautifulSoup
#from requests_html import HTMLSession

class KifuLoader():
    def load_kifu(self, txt):
        raise NotImplementedError
    
    #ユーザ名の取得 
    #return (先手, 後手)
    def get_users(self):
        raise NotImplementedError
    
    #手数の取得
    def get_move_count(self):
        raise NotImplementedError
    
class SyogiQuestKifuLoader(KifuLoader):
    def __init__(self):
        pass
    
    def set_id(self, id):
        self.id = id

    def load_kifu(self, text):
        try:
            self.text = text
            #print(r.text.splitlines())
            sp = text.splitlines()
            #print(text)
            self.first_player = sp[1][2:].split("(")[0]
            self.second_player = sp[2][2:].split("(")[0]
            self.move_count = len(sp) - 13

            # print(self.first_player)
            # print(self.second_player)
            # print(self.move_count)
            return True
        except:
            return False
        
class SyogiQuestBeta():
    def __init__(self):
        pass

    def set_username(self, username):
        self.username = username

    def get_game_ids(self,minutes,game_count=10):
        map = {10:"10",5:"",2:"2"}

        params = {"userId":self.username,"gtype":"shogi"+map[minutes]}
        r = requests.get("https://c-loft.com/shogi/quest/history/",params=params)
        
        json = r.json()
        ids = [game["id"] for game in json["games"]]
        return ids[:game_count]
    
    def get_kifus(self,ids):
        kifus = []
        for id in ids:
            params = {"id":id}
            r = requests.get("https://c-loft.com/shogi/quest/history/download",params=params)
            kifu = SyogiQuestKifuLoader()
            loadable =  kifu.load_kifu(r.text)
            if not loadable:
                break
            kifu.set_id(id)
            kifus.append(kifu)
        return kifus
