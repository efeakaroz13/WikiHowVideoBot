from PIL import ImageFont, ImageDraw, Image
import cv2

filename = "t1.png"
title= "1 - Having Fun on Your Own and having a good life. and bunch of text to test what happens"
image_top_name = "biker1080.jpg"


image = cv2.imread(filename)
height = image.shape[0]
width = image.shape[1]
fontpath = "../Montserrat-Regular.ttf" 
font = ImageFont.truetype(fontpath, 80)
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





img_pil.save("_"+filename)
