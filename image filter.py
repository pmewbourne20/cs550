from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


import sys

image = Image.open(sys.argv[1])
imgx, imgy = image.size


def graphicdesign(imgx,imgy):
	img2 = Image.open("frog.jpg") 
	width,height = img2.size

	sixthx = int((imgx)/6)
	sixthy = int((imgy)/6)

	img2 = img2.resize((sixthx,sixthy))
	image.paste(img2, (imgx-(2*sixthx), sixthy)) 

	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype("papyrus.ttf", int((imgx)/30))
	draw.text((sixthx, 2*sixthy),"Graphic Design is my passion",(255,0,0),font=font)
		
#Saved in the same relative location 
	image.save("New Photo.jpg") 




graphicdesign(imgx,imgy)
image.show()