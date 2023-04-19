from moviepy.editor import *
import requests
import json
import pyttsx3
import random
from colorama import Fore
import time
from bs4 import BeautifulSoup

config = json.loads(open("configurer.json","r").read())
wikihowInstances = config["countriesVideoFetch"]
try:
    userAgents = requests.get("https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt").text.split("\n")
except:
    print(Fore.RED,"ERR - NO INTERNET",Fore.RESET)
    exit()


logger = open("all.log","a")

def select_url(allUrls,excludedUrls):
    selected = random.choice(allUrls)
    if selected  in excludedUrls:
        select_url(allUrls,excludedUrls)
    else:
        return selected
def decideURL(lang):

    try:
        oldPages = open(f"memoryCache/{lang}.old.txt","r").read().split("\n")
    except:
        oldPages = []



    try:
        urlDb = open(f"memoryCache/{lang}.txt","r").read().split("\n")

    except:
        try:
            agent = random.choice(userAgents)
            sitemap = requests.get(f"https://{lang}.wikihow.com/sitemap.xml",headers={"User-Agent":agent},allow_redirects=True)
        except Exception as e:
            logger.write(f"{time.ctime(time.time())} | {e} - INTERNET - {lang}")
            print(Fore.RED,f"Couldn't connect to {lang}.wikihow.com, waiting 30 seconds",Fore.RESET)
            time.sleep(30)
            decideURL(lang)

        soup = BeautifulSoup(sitemap.content)
        AllUrl = soup.find_all("loc")
        urlDbWriter = open(f"memoryCache/{lang}.txt","a")
        for a in AllUrl:
            text = a.get_text()
            urlDbWriter.write(text+"\n")

        urlDbWriter.close()
        urlDb = open(f"memoryCache/{lang}.txt", "r").read().split("\n")

    if len(urlDb)> len(oldPages)+1:
        selection = select_url(urlDb,oldPages)
    else:
        return False

    oldlogs = open(f"memoryCache/{lang}.old.txt","a")
    oldlogs.write(selection+"\n")
    oldlogs.close()
    return selection


if __name__ == "__main__":
    selection = decideURL("ar")
    print(selection)







