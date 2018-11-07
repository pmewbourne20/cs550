from PIL import Image
import random as random
import math as m
imgx, imgy = int(input("Enter the dimensions of the square maze./n/n>>"))
amnt = int(input("Enter the amounts of corners you want\n\n>>"))

image = Image.new("RGB",(imgx,imgy))

class Pixel():
	def __init__(self,x,y,z):
		self.x = random.randint(0,imgx)
		self.y = random.randint(0,imgy)
		self.z = z
	#def nodes(self,x,y,z):  
	#while z > amnt:
	#		self.x = 
	#		self.y = 
      #if self.x == 1 and self.y == 0:
      	#image.putpixel((self.x,self.y),(0,255,0))
        #z+=1
        #return
    #z+=1
    #image.putpixel((self.x,self.y),(255,255,0))
      
	def end(self,x,y):
    	image.putpixel((imgx-1,imgy-1),(255,0,0))
    	
for i in range(imgx):
	for q in range(imgy):
		image.putpixel((i,q),(0,0,0))

image.putpixel((1,0),(0,255,0))
image.putpixel((1,1),(0,255,0))
    
image.show()

def startmove(x,y):
	while True:
    px = image.load()
  	i = random.randint(1,4)
  	if i == 1:
    	if (y-2 > 0) or px[x,y-2] == (255,255,0):
        w = 1
      else:
        for q in range(2):
          image.putpixel((x,y-q),(255,255,0))
        startmove(x,y-2)
  	if i == 2:
    	if (x+2 < imgx) or px[x+2,y] == (255,255,0):
      	d = 1
      else:
        for q in range(2):
          image.putpixel((x+q,y),(255,255,0))
        startmove(x+2,y)
    if i == 3 :
      if (y+2 < imgy) or px[x,y+2] == (255,255,0):
        s = 1
      else:
        for q in range(2):
          image.putpixel((x,y+q),(255,255,0))
      	startmove(x,y+2)
    if i == 4:
      if (x-2 > 0) or (px[x-2,y] == (255,255,0):
        a = 1
      else:
        for q in range(2):
          image.putpixel((x-q,y),(255,255,0))
        startmove(x-2,y)
    if w == 1 and d == 1 and s == 1 and a == 1:
    	return
  
startmove(1,1)
image.show
                       
                       
    