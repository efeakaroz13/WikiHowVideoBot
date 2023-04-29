import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

""" 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("sample_in.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("sans-serif.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Sample Text",(255,255,255),font=font)
img.save('sample-out.jpg')
"""

filename = "im.jpg"
title= "1 - Having Fun on Your Own"
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

cv2.imwrite(filename,image)



## Use simsum.ttc to write Chinese.
fontpath = "Montserrat-Regular.ttf" # <== 这里是宋体路径
font = ImageFont.truetype(fontpath, 25)
img_pil = Image.open(filename)
draw = ImageDraw.Draw(img_pil)
draw.text((10, height-45),  title, font = font,fill="black")

img_pil.save("_"+filename)