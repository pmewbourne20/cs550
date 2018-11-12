from PIL import Image
import random as random
import math as m
imgx = int(input("Enter the dimensions of the square maze.\n\n>>"))
imgy = imgx
#amnt = int(input("Enter the amounts of corners you want\n\n>>"))

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

def startmove(x,y,num_iters = 0):
	print("**In start move!",x,y)
	up, right, left, down = 0,0,0,0
	cram = 0
	if num_iters == 5:
		return
	while cram < 50:
		pixels = image.load()
		direction = random.randint(1,4)        
		print("==================",direction,num_iters)
		if direction == 1:
			if (y-2 > 0) and pixels[y-2,x] != YELLOW:
				image.putpixel((x,y-1),YELLOW)
				image.putpixel((x,y-2),YELLOW)
				pixels = image.load()
				print("pixel",direction," marked")
#				startmove(x,y-2, num_iters+1)
			else:
				up = 1
		elif direction == 2:
			if (x+2 < imgx) and pixels[y,x+2] != YELLOW:
				image.putpixel((x+1,y),YELLOW)
				image.putpixel((x+2,y),YELLOW)
				pixels = image.load()
				print("pixel",direction," marked")
#				startmove(x+2,y,num_iters+1)
			else:
				right = 1
		elif direction == 3 :
			if (y+2 < imgy) and pixels[y+2,x] != YELLOW:
				image.putpixel((x,y+1),YELLOW)
				image.putpixel((x,y+2),YELLOW)
				px = image.load()
				print("pixel",direction," marked")
#				startmove(x,y+2,num_iters+1)
			else:
				down = 1
		elif direction == 4:
			if (x-2 > 0) and pixels[y,x-2] != YELLOW:
				image.putpixel((x-1,y),YELLOW)
				image.putpixel((x-2,y),YELLOW)
				pixels = image.load()
				print("pixel",direction," marked")
#				startmove(x-2,y,num_iters+1)
			else:
				left = 1
		print(up,right,left,down)
		if up == 1 and right == 1 and left == 1 and down == 1:
			if (x,y) == (1,1):
			    image.show()
			print("Go back")
			return 
		cram += 1
		


startmove(1,1,0)
image.show()