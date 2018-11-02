from PIL import Image
import random as random
imgx = 512
imgy = 512
image = Image.new("RGB",(imgx,imgy))

class Pixel:
	def __init__(self,x,y,checked):
		self.x = random.randint(imgx)
		self.y = random.randint(imgy)
		self.checked = False

for i in range(imgx):
	for q in range(imgy):
		image.putpixel((i,q),(0,0,0))

image.show()