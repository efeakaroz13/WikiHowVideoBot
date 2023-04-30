from PIL import ImageFont, ImageDraw, Image
import cv2

filename = "first.png"
title= "1 - Having Fun on Your Own and having a good life"


image = cv2.imread(filename)
height = image.shape[0]
width = image.shape[1]
fontpath = "../Montserrat-Regular.ttf" 
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
            counter+=1
    draw.text((30, 600+counter*85),  output, font = font,fill="white")
    output =""
    counter+=1
        


img_pil.save("_"+filename)
