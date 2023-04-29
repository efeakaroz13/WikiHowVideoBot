import os
import random 
import requests 
from bs4 import BeautifulSoup
import json 
import matplotlib as plt
import cv2
from moviepy.editor import *
from modularAI import modularAI
from gtts import gTTS




class Anton:
    def edit(self,filename,number,title):
        image = cv2.imread(filename)
        height = image.shape[0]
        width = image.shape[1]
        print("Height : ",height)
        print("Width : ",width)
        print(image.shape)
        #blur the wikihow logo from bottom 26px

        if len(title) >= 45:
            title = title[:45]+"..."
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (30, height-20)
        fontScale = 1

        color = (0, 0, 0)

        thickness = 2

        
        image = cv2.rectangle(image, (0,height-50), (width,height), (255,255,255),-1)
        image = cv2.putText(image, f'{number} - {title}', org, font, fontScale, color, thickness, cv2.LINE_AA)


        cv2.imwrite(filename,image)


    def __init__(self):
        self.a = ""
    def speak(self,text,lang="en"):
        if lang == "en":
            text = text.replace(" ","%20")

            sound = requests.get(f"https://murf.ai/Prod/anonymous-tts/audio?name=en-CA-ethan&text={text}")
            with open(f"OUT{random.randint(1,3000)}.mp3","wb") as f:
                f.write(sound.content)
                filename = f.name
                return filename 
        else:
            tts = gTTS(text,lang=lang)
            filename = f"OUT{random.randint(1,3000)}.mp3"
            tts.save(filename)
            return filename
    def scraper(self,wikihowurl):
        images = []
        page = requests.get(wikihowurl,headers={"User-Agent":"Mozilla/5.0 Macintel Chrome(107.0.23.23)"})

        soup = BeautifulSoup(page.content,"html.parser")
        alllinks = soup.find_all("a",{"class":"ts_trustworthy"})
        for a in alllinks:
            a.parent.parent.decompose()
        print(len(alllinks))

        try:
            steps_first = soup.find_all("steps_first")[0]
            allimages = steps_first.find_all("a",{"class":"image"})
        except:
            allimages = soup.find_all("a",{"class":"image"})


        for a in allimages:
            #print(a)
            try:
                src=a.find_all("img")[0].get('data-src')
                src.split("https")[1]
                
                step=  a.parent.parent.find_all("div",{"class":"step"})[0]
                step_num = int(step.parent.find_all("div",{"class":"step_num"})[0].get_text())
                title = step.find_all("b",{"class":"whb"})[0].get_text()
                text = step.get_text()
                appendit=True
                for i in images:
                    if i["text"] == text:
                        appendit = False
                
                data1 = {"image":src,"text":text,"step_num":step_num,"title":title}
                if appendit == True:
                    images.append(data1)

                
            except:
                pass

        idofthething =  wikihowurl.split("/")[-1].split(".")[0]
        data = {"output":images,"id":idofthething}

        return data 
    def makeclip(self,data,lang="en"):
        imgqts = []
        try:
            data["output"]
        except:
            raise ValueError("Please pass the data returned from scraper(<url>) ")
        videooutput = []
        filenamer = []
        for d in data["output"]:
            text= d["text"]
            image = d["image"]
            title = d["title"]
            step_num = d["step_num"]
            soundfile = self.speak(text,lang=lang)
            #Download the image
            page = requests.get(image,stream=True)
            filenameofit = image.split("/")[-1]
            
            with open(filenameofit,"wb") as f:
                f.write(page.content)
            stringthing = ["A","B","ANT","ON","AD","ASDF"]
            





            img = cv2.imread(filenameofit, cv2.IMREAD_UNCHANGED)
 
            print('Original Dimensions : ',img.shape)
            
            scale_percent = 200 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            
            # resize image
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            
            print('Resized Dimensions : ',resized.shape)
            cv2.imwrite(filenameofit,resized)
            self.edit(filenameofit,step_num,title)
            imgqts.append(filenameofit)


            

            """
                ffmpeg -loop 1 -i {filenameofit} -i {sounfile} -shortest -acodec copy -vcodec mjpeg {outputfilename}.mp4
                ffmpeg -loop 1 -y -i {filenameofit} -i {soundfile} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {outputfilename}.mp4
                ffmpeg -loop 1 -framerate 24 -t 10 -i image.jpg -i video.mp4 -filter_complex "[0]scale=432:432,setsar=1[im];[1]scale=432:432,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0" out.mp4
                ffmpeg  -i {filenameofit} -i {soundfile} -c:v libx264 -c:a aac -pix_fmt yuv420p -crf 23  -shortest -y {outputfilename}.mp4
                ffmpeg -loop 1 -i {filenameofit} -i {soundfile} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf "scale='iw-mod(iw,2)':'ih-mod(ih,2)',format=yuv420p" -shortest -movflags +faststart {outputfilename}.mp4
                ffmpeg -loop 1 -f image2 -i {filenameofit} -i {soundfile} -vf fps=30 -pix_fmt yuv420p -vcodec libx264 -shortest {outputfilename}.mp4
            """
            audioclip = AudioFileClip(soundfile)
            soundduration = audioclip.duration

            outputfilename = f"{random.choice(stringthing)}{random.randint(1,234534554645645)}{random.choice(stringthing)}{random.choice(stringthing)}{random.choice(stringthing)}{random.choice(stringthing)}"
            os.system(f"""ffmpeg -loop 1 -f image2 -i {filenameofit} -i {soundfile} -vf fps=30 -pix_fmt yuv420p -vcodec libx264 -shortest {outputfilename}.mp4""")
            os.system(f"rm {soundfile} ")
            os.system(f"rm {filenameofit} ")
            clip = VideoFileClip(outputfilename+".mp4")
            clip = clip.subclip(0,soundduration)
            videooutput.append(clip)

            filenamer.append(outputfilename)
        print(videooutput)
        for image in imgqts:
            os.system(f"rm {image}")
        final = concatenate_videoclips(videooutput)
        theoutputfilename = data["id"]+".mp4"

        final.write_videofile(theoutputfilename,temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")
        for f in filenamer:
            os.system(f"rm {f}.mp4")
            print(f)

        return {"SCC":True,"output":theoutputfilename}





            
            





if __name__ =="__main__":
    myanton = Anton()
    outdata=myanton.scraper("https://www.wikihow.com/Increase-Your-Brain-Power")
    myanton.makeclip(outdata)
    
