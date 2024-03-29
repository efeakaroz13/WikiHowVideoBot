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
from modularAI import modularAI
from PIL import ImageFont, ImageDraw, Image
import cv2

aimod = modularAI()



""" 
 
curl 'https://2poo4vxwjc.execute-api.us-east-1.amazonaws.com/prod-wps/tts?e=user%40naturalreaders.com&l=0&r=12&s=0&v=ms&vn=10.1.30&sm=true&ca=true' \
  -H 'sec-ch-ua: "Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'Authorization: AWS4-HMAC-SHA256 Credential=ASIAQCLJGNPXYEYZSA7J/20230429/us-east-1/execute-api/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-security-token, Signature=6c32a9cfa4d63070e8826968ba8035031d9a96737fb9215ccbcdb0eb94bfb511' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  -H 'Content-Type: application/json; charset=UTF-8' \
  -H 'X-Amz-Security-Token: IQoJb3JpZ2luX2VjEGgaCXVzLWVhc3QtMSJIMEYCIQDc+eFTKAt9W75Rofbmrlovy8QaPBTWyRtZcMYqM5eHgwIhAM9tWVvzFd6Eb4Bs8eUgZUdjfQdP2PBWmrWI53bStemJKocGCHEQABoMMDA1MDUyNDYwMDE1Igy3nYLb84hikTpCTv0q5AXbUDBUCmpZv/4vQQCH57a1TbZU144VMT1QxgVAVlIEyN2WiVjK2gIl/0GUUCghTd2eIVyQiN9Hwjr45jtQfJc+0cBAIg6gmrMbfD6Z3QEYujF6z3Kv/dPSHoZn/X9SiXgaeddGBaW42n7pl+Yy93RNRaDxqIXJDanr6z4zMwLYprUA+OzlkyY8ANJUePBjey3VVf1ZYsuLAGYDhdKaBFQLrb1PNLFYKnqll4f9qe4afArtGYeBO5Z6kiKU1hKqLnsNo+wjwT5z0HhZxmNO2wpAcTMKJmGM/tY4ZY4cJLDdjO61mi2RwFeO8sycQ4pLRpNRIFt1MRz6t1Aq59QGOqEMppg/reJS7qVjt0rbiEY0o9A9hf9y54aj4qWvgHqzeY0kO/DnXVjscHZs4qv51L5zXiQOgOoSMZBkoAWKEVvIgF5nrUyOQkPspX0/M8PF6+fXpOqoxsWUjuA86x9TncUtDy1CAggt2rYLsdPgoT3vf63vGjXdLlb5WaOVagd5up6DTZ0tumiwrxc5gCPtifjDCXLblRBLfc+Fs6t+0nByaGVVQk7xwA4HJjCIow349R4FVsAl7uPYB3mnZ/AkrXg9+WrsFGImJzgNqlmdXTM02Efl2vJHMEkSrh+L1oxyOxH2evw9itoM11eNIubiXKMac3WW9rypAI+2QEzDvFkMAtZP57COZqmKAXw6WDDD4OmoGD786Z/qQ77O1B70lvoPchtbs52r5kpIABJGwFaw79fGj6JeGpiCcqvynL3Vvr4pKws8XQmzHpL+USD7CZoP+rcXuNZCj2mR0HX2U2eUstP8XTSZR9E9HwmPVY7aCZJoybwfcAbJ29k5dJSD7ez7CMqwHzyftL6xm8EvY2fLZ69a0WahDUY2795KViQxohhrExmckotYDGdEDqUBSg0LIohlMXXF0BNGmEoqt+33cjYaLTKplzLYWPvDUs+LMSVKlBFLzMwk0uaOtudeLwIG0vsVOjDenLOiBjqGAoqsS4yVZywFC2TPmjJpDdvoJs7KlggZLL+qihdyigucclbf5GAalAfaImpWQ+FXfOqce4A385VTBzxLU5uT0YaK2oyMyxw0fJgBkJObAFfSfYECWMCYmq2HiUfr30wl12Nd07pLb9RuWQVMsStPTsWJ53RT5o6jX0Zu5awXdwboGXUrzYGGaoA6JlkJrDhP5d/mZPbhsvUPPwG0Nbhn6skc5PBYLHVxNdwZaivNbTOfvCZmSWa/dkbnuCUbm+9lN+tfn5v/vSI3ebwSn2ywHLhak0/W+VKNbBjGdWjhbTXMYDGVFvstgw/W/Ggoi3BkFKd3vckt7+oIT6dADmpS7RwVcm3EVGY=' \
  -H 'Referer: https://www.naturalreaders.com/' \
  -H 'x-amz-date: 20230429T075932Z' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw '{"t":"Our Plus subscription includes exclusive features and the use of Plus Voices, our newest and most advanced voices."}' \
  --compressed

"""





class Anton:
    def make_start_page(self,outputfilename,title):
        

        filename = "imageEditShorts/first.png"



        image = cv2.imread(filename)
        height = image.shape[0]
        width = image.shape[1]
        fontpath = "Montserrat-Regular.ttf" 
        font = ImageFont.truetype(fontpath, 80)
        img_pil = Image.open(filename)
        draw = ImageDraw.Draw(img_pil)
        counter = 0
        if len(title)<25:
            draw.text((30, 600),  title, font = font,fill="white")
        else:
            output = ""
            for s in title.split(" "):
                if len(output)+len(s)<25:
                    output = output+" "+s
                    print(output)
                else:

                    draw.text((30, 600+counter*85),  output, font = font,fill="white")
                    output =""
                    output = output+" "+s
                    counter+=1
            draw.text((30, 600+counter*85),  output, font = font,fill="white")
            output =""
            counter+=1
                


        img_pil.save(outputfilename)
        return outputfilename







    def edit(self, image_top_name, number, title):
        title = title.replace("-","")
        if number != None:
            title = str(number)+" - "+title
        else:
            pass 
        """
        image = cv2.imread(filename)
        height = image.shape[0]
        width = image.shape[1]
        print("Height : ", height)
        print("Width : ", width)
        print(image.shape)
        # blur the wikihow logo from bottom 26px

        if len(title) >= 45:
            title = title[:45] + "..."
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (30, height - 20)
        fontScale = 1

        color = (0, 0, 0)

        thickness = 2

        image = cv2.rectangle(
            image, (0, height - 50), (width, height), (255, 255, 255), -1
        )
        image = cv2.putText(
            image,
            f"{number} - {title}",
            org,
            font,
            fontScale,
            color,
            thickness,
            cv2.LINE_AA,
        )

        cv2.imwrite(filename, image)
        """
        filename = random.choice(["imageEditShorts/t1.png","imageEditShorts/t2.png"])




        image = cv2.imread(filename)
        height = image.shape[0]
        width = image.shape[1]
        fontpath = "Montserrat-Regular.ttf" 
        font = ImageFont.truetype(fontpath, 75)
        img_pil = Image.open(filename).convert("RGB")
        draw = ImageDraw.Draw(img_pil)
        counter = 0
        if len(title)<25:
            draw.text((30, 900),  title, font = font,fill="white")
        else:
            output = ""
            for s in title.split(" "):
                if len(output)+len(s)<25:
                    output = output+" "+s
                    print(output)
                else:

                    draw.text((30, 900+counter*85),  output, font = font,fill="white")
                    output =""
                    output = output+" "+s
                    counter+=1
            draw.text((30, 900+counter*85),  output, font = font,fill="white")
            output =""
            counter+=1
                




        img = Image.open(image_top_name, 'r').convert("RGB")
        img_w, img_h = img.size

        bg_w, bg_h = img_pil.size
        offset = ((bg_w - img_w) // 2, 0)
        img_pil.paste(img, offset)
        img_pil.save(image_top_name)


    def __init__(self):
        self.a = ""

    def speak(self, text, lang="en"):

        if len(text) == 0:
            return ""
        
        totext = ""
        splitter = text.split(" ")
        for s in splitter:
            if "http" in s:
                continue
            else:
                totext = totext+s+" " 
        text=totext
        if lang == "en":



            sentences = text.split(".")
            
            
            if len(sentences) == 1:
                sentences = text.split(",")
            if len(sentences) == 1:
                sentences = text.split("-")

            sounds = []
            for s in sentences:
                s = s.replace("&","%26").replace("?","%3F")
                if s == "":
                    continue
                s = s.replace("#"," ")
                if str(s).strip() == "":
                    continue
                sound = requests.get(
                    f"https://api.genny.lovo.ai/v1/tts?text={s}&isDefault=false&speaker=638088f9d72424f0cfbdbe59&speakerStyle=638088f9d72424f0cfbdbe5a",
                    headers={
                        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
                    }
                )
                print(sound.url)
                try:
                    print(json.dumps(json.loads(sound.content),indent=4))
                    continue
                except:
                    pass
                with open(f"OUT{random.randint(1,30000)}.mp3", "wb") as f:
                    f.write(sound.content)
                    filename = f.name
                    sounds.append(filename)
            
            clips = [AudioFileClip(c) for c in sounds]
            final_clip = concatenate_audioclips(clips)
            filenameout = f"OUT{random.randint(1,10000)}.mp3"
            final_clip.write_audiofile(filenameout)
            for s in sounds:
                os.system(f"rm {s}")
            return filenameout

        else:
            tts = gTTS(text, lang=lang)
            filename = f"OUT{random.randint(1,3000)}.mp3"
            tts.save(filename)
            return filename

    def scraper(self, wikihowurl):
        images = []

        page = requests.get(
            wikihowurl,
            headers={"User-Agent": "Mozilla/5.0 Macintel Chrome(107.0.23.23)"},
        )

        soup = BeautifulSoup(page.content, "html.parser")
        try:
            title = soup.find_all("h1")[0].get_text()
        except:
            title = ""

        alllinks = soup.find_all("a", {"class": "ts_trustworthy"})
        for a in alllinks:
            a.parent.parent.decompose()

        idofthething = wikihowurl.split("/")[-1].split(".")[0]
        try:
            steps_first = soup.find_all("div",{"class":"steps"})
            

            for s in steps_first:
               
                allimages = s.find_all("a", {"class": "image"})
                print(len(allimages))
                locimg = []
                for a in allimages:
                    # print(a)
                    try:
                        src = a.find_all("img")[0].get("data-src")
                        src.split("https")[1]

                        step = a.parent.parent.find_all("div", {"class": "step"})[0]
                        try:
                            step_num = int(
                                step.parent.find_all("div", {"class": "step_num"})[0].get_text()
                            )
                        except:
                            step_num = None
                        title2 = step.find_all("b", {"class": "whb"})[0].get_text()
                        text = step.get_text()
                        appendit = True
                        for i in locimg:
                            if i["text"] == text:
                                appendit = False

                        data1 = {
                            "image": src,
                            "text": text,
                            "step_num": step_num,
                            "title": title2,
                        }
                        if appendit == True:
                            locimg.append(data1)

                    except Exception as e:
                        pass

                
                images.append({"output": locimg, "id": idofthething,"title":title+f" Part #{steps_first.index(s)+1}"})
        except Exception as e:
            allimages = soup.find_all("a", {"class": "image"})

        
        
        
        #data = {"output": images, "id": idofthething,"title":title}

        return images









    def makeclip(self, data, lang="en"):
        imgqts = []
        try:
            data["output"]
        except:
            raise ValueError("Please pass the data returned from scraper(<url>) ")
        videooutput = []
        filenamer = []
        stringthing = ["A", "B", "ANT", "ON", "AD", "ASDF"]


        #START IMAGE
        startImage = self.make_start_page(f"start{random.randint(1,123435345345)}.png",data["title"])
        start_soundfile = self.speak(data["title"], lang=lang)
        outputfilename = f"{random.choice(stringthing)}{random.randint(1,234534554645645)}{random.choice(stringthing)}{random.choice(stringthing)}{random.choice(stringthing)}{random.choice(stringthing)}"
        os.system(
            f"""ffmpeg -loop 1 -f image2 -i {startImage} -i {start_soundfile}  -vf fps=30 -pix_fmt yuv420p -vcodec libx264 -shortest {outputfilename}.mp4"""
        )
        imgqts.append(startImage)

        audioclip = AudioFileClip(start_soundfile)
        soundduration = audioclip.duration
        os.system(f"rm {start_soundfile} ")
        os.system(f"rm {startImage} ")
        clip = VideoFileClip(outputfilename + ".mp4")
        clip = clip.subclip(0, soundduration)
        videooutput.append(clip)
        filenamer.append(outputfilename)
        #END OF START IMAGE


        for d in data["output"]:
            text = d["text"]
            text=text.replace("Research source","").replace("X\n","").replace("\n","")
            image = d["image"]
            title = d["title"]
            step_num = d["step_num"]
            print("Summerising")
            print(text)
            text = aimod.summerize(text)
            


            soundfile = self.speak(text, lang=lang)
            print(soundfile)
            # Download the image
            page = requests.get(image.replace("460","550"), stream=True)
            filenameofit = image.split("/")[-1]

            with open(filenameofit, "wb") as f:
                f.write(page.content)
            

            img = cv2.imread(filenameofit, cv2.IMREAD_UNCHANGED)

            print("Original Dimensions : ", img.shape)

            scale_percent = 200  # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)

            # resize image
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

            print("Resized Dimensions : ", resized.shape)
            cv2.imwrite(filenameofit, resized)
            self.edit(filenameofit, step_num, title)
            imgqts.append(filenameofit)

            """
                ffmpeg -loop 1 -i {filenameofit} -i {sounfile} -shortest -acodec copy -vcodec mjpeg {outputfilename}.mp4
                ffmpeg -loop 1 -y -i {filenameofit} -i {soundfile} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {outputfilename}.mp4
                ffmpeg -loop 1 -framerate 24 -t 10 -i image.jpg -i video.mp4 -filter_complex "[0]scale=432:432,setsar=1[im];[1]scale=432:432,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0" out.mp4
                ffmpeg  -i {filenameofit} -i {soundfile} -c:v libx264 -c:a aac -pix_fmt yuv420p -crf 23  -shortest -y {outputfilename}.mp4
                ffmpeg -loop 1 -i {filenameofit} -i {soundfile} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf "scale='iw-mod(iw,2)':'ih-mod(ih,2)',format=yuv420p" -shortest -movflags +faststart {outputfilename}.mp4
                ffmpeg -loop 1 -f image2 -i {filenameofit} -i {soundfile} -vf fps=30 -pix_fmt yuv420p -vcodec libx264 -shortest {outputfilename}.mp4
            """
            print(soundfile)
            audioclip = AudioFileClip(soundfile)
            soundduration = audioclip.duration

            outputfilename = f"{random.choice(stringthing)}{random.randint(1,234534554645645)}{random.choice(stringthing)}{random.choice(stringthing)}{random.choice(stringthing)}{random.choice(stringthing)}"
            os.system(
                f"""ffmpeg -loop 1 -f image2 -i {filenameofit} -i {soundfile}  -vf fps=30 -pix_fmt yuv420p -vcodec libx264 -shortest {outputfilename}.mp4"""
            )
            os.system(f"rm {soundfile} ")
            os.system(f"rm {filenameofit} ")
            clip = VideoFileClip(outputfilename + ".mp4")
            clip = clip.subclip(0, soundduration)
            videooutput.append(clip)

            filenamer.append(outputfilename)
        print(videooutput)
        for image in imgqts:
            os.system(f"rm {image}")
        final = concatenate_videoclips(videooutput)
        theoutputfilename = data["title"] + ".mp4"

        final.write_videofile(
            theoutputfilename,
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
            codec="libx264",
            audio_codec="aac",
        )
        for f in filenamer:
            os.system(f"rm {f}.mp4")
            print(f)

        return {"SCC": True, "output": theoutputfilename}


if __name__ == "__main__":
    myanton = Anton()
    outdata = myanton.scraper("https://www.wikihow.com/7-Signs-of-a-Toxic-Person")
    print(json.dumps(outdata,indent=4))
    #myanton.makeclip(outdata)
