from moviepy.editor import *
import requests
import json
import random
from colorama import Fore
import time
from bs4 import BeautifulSoup
from anton import Anton
from multiprocessing import Process 


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
            URL = config["pages"][lang]
            sitemap = requests.get(f"{URL}/sitemap.xml",headers={"User-Agent":agent},allow_redirects=True)
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

def task(language):

    selection = decideURL(language)
    print(selection)
    myanton = Anton()
    outdata = myanton.scraper(selection)
    output = myanton.makeclip(outdata, lang=language)["output"]
    try:
        os.listdir("out")
    except:
        os.system("mkdir out")


    try:
        os.listdir("out/"+language)
    except:
        os.system(f"mkdir out/{language}")

    os.system(f"mv '{output}' out/{language}")
    print(output)


if __name__ == "__main__":
    videoFetchLanguages = config["countriesVideoFetch"]
    task("en")
"""

if __name__ == "__main__":
    videoFetchLanguages = config["countriesVideoFetch"]
    while True:
        

        if len(videoFetchLanguages) == 0:
            print(Fore.RED,"Enter Language codes to config.")
        if len(videoFetchLanguages)<2:
            print(f"STARTING TASK FOR {videoFetchLanguages[0]} ")
            task(videoFetchLanguages[0])

        else:
            lan1 = random.choice(videoFetchLanguages)
            videoFetchLanguages.remove(lan1)
            lan2 = random.choice(videoFetchLanguages)
            print(f"STARTING TASK FOR {lan1},{lan2} ")
            p1 = Process(target=task,args=(lan1,))
            p2 = Process(target=task,args=(lan2,))
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            break

"""
    







