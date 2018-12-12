import sqlite3
import os 
import re

def getEpisode(str):
    # https://kissanime.ru/Anime/
    # Seishun-Buta-Yarou-wa-Bunny-Girl-Senpai-no-Yume-wo-Minai/
    # Episode-010?id=152973&s=default
    return str.split("?")[0].split('-')[1]
    

data_path = os.path.expanduser('~')+"/AppData/Local/Google/Chrome/User Data/Default"
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'history')
conn = sqlite3.connect(history_db)
c = conn.cursor()
sql = "SELECT url FROM urls"
c.execute(sql)
res = [i[0] for i in c.fetchall()]
# res_ac = [i[0] for i in res]
# print(res[-1])
d_c = dict()
for url in res:
    if url.find("https://kissanime.ru/Anime") >= -1:
        url_split = url.split("/")
        if "Anime" in url_split:
            d_c[url_split[url_split.index("Anime")+1]] = getEpisode(url_split[-1])
    # elif url.find(https://gogoanimes.co/sora-to-umi-no-aida-episode-11)
for tup in d_c.items():
    print(tup)
