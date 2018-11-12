from PIL import Image
import random as random
import math as m
imgx = int(input("Enter the dimensions of the square maze.\n\n>>"))
imgy = imgx
amnt = int(input("Enter the amounts of corners you want\n\n>>"))

image = Image.new("RGB",(imgx,imgy))

YELLOW = (255, 255, 0)

# class Pixel():
#     def __init__(self,x,y,z):
#         self.x = random.randint(0,imgx)
#         self.y = random.randint(0,imgy)
#         self.z = z 
#     z = 0
#     while z > amnt:
#       #if self.x == 1 and self.y == 0:
	
#           #image.putpixel((self.x,self.y),(0,255,0))
#         #z+=1
#         #return
#         image.putpixel((self.x,self.y),YELLOW)
#         z+=1
	  
#     def end(self,x,y):
#         image.putpixel((imgx-1,imgy-1),(255,0,0))


image.putpixel((1,0),YELLOW)
image.putpixel((1,1),YELLOW)
	

# def add_pixel_in_direction(direction,):
#     # direction == i
#     if (y-2 > 0):
#         print(px[y-2,x],px[y-2,x] == YELLOW)
#         if px[y-2,x] != YELLOW:
#             image.putpixel((x,y-1),YELLOW)
#             image.putpixel((x,y-2),YELLOW)
#             g+=2
#             px = image.load()
#             print("pixel",i," marked")
#             startmove(x,y-2,g)
#         else:
#             w = 1
#             print("Fail")
#     else:
#         w = 1

def startmove(x,y,g,num_iters = 0):
	print("**In start move!",x,y)
	w, d, s, a = 0,0,0,0
	if num_iters == 5:
		return
	while True:
		px = image.load()
		i = random.randint(1,4)        
		# i
		# if i == 1:
	   # add_pixel_in_direction(i)
		# if i == 2:
			
		# 2 == 
		# 3 == 
		# 4 == 
		print("==================",i,num_iters)
		if i == 1:
			if (y-2 > 0) and px[y-2,x] != YELLOW:
				image.putpixel((x,y-1),YELLOW)
				image.putpixel((x,y-2),YELLOW)
				g+=2
				px = image.load()
				print("pixel",i," marked")
				startmove(x,y-2,g, num_iters+1)
			else:
				w = 1
		elif i == 2:
			if (x+2 < imgx) and px[y,x+2] != YELLOW:
				image.putpixel((x+1,y),YELLOW)
				image.putpixel((x+2,y),YELLOW)
				g+=2
				px = image.load()
				print("pixel",i," marked")
				startmove(x+2,y,g, num_iters+1)
			else:
				d = 1
		elif i == 3 :
			if (y+2 < imgy) and px[y+2,x] != YELLOW:
				image.putpixel((x,y+1),YELLOW)
				image.putpixel((x,y+2),YELLOW)
				g+=2
				px = image.load()
				print("pixel",i," marked")
				startmove(x,y+2,g, num_iters+1)
			else:
				s = 1
		elif i == 4:
			if (x-2 > 0) and px[y,x-2] != YELLOW:
				image.putpixel((x-1,y),YELLOW)
				image.putpixel((x-2,y),YELLOW)
				g+=2
				px = image.load()
				print("pixel",i," marked")
				startmove(x-2,y,g, num_iters+1)
			else:
				a = 1
		print(w,d,s,a)
		if w == 1 and d == 1 and s == 1 and a == 1:
			if (x,y) == (1,1):
			    image.show()
			print("Go back")
			return 
		


startmove(1,1,0)