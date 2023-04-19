import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time



filename = "im.jpeg"
title= "こんにちは"
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
fontpath = "simsun.ttc" # <== 这里是宋体路径
font = ImageFont.truetype(fontpath, 30)
img_pil = Image.open(filename)
draw = ImageDraw.Draw(img_pil)
draw.text((5, height-40),  title, font = font,fill="black")

img_pil.save(filename)