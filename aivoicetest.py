import requests
import json 

page = requests.get("https://api.genny.lovo.ai/v1/tts?text=Hello this is a%20test.As you can tell I'm writing down a paragraph in here for just to see the results&isDefault=false&speaker=638088f9d72424f0cfbdbe59&speakerStyle=638088f9d72424f0cfbdbe5a",)
with open("test.mp3","wb") as f:
    f.write(page.content)