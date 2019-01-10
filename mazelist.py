from PIL import Image 
import random as random
import math as m
imgx = int(input("Enter the dimensions of the square maze.\n\n>>"))
imgy = imgx

def startmove(x,y,num_iters = 0):
	pixels = []
	for i in range(imgy):
		k = ["*"] * (imgx)
		pixels.append(k)
	print("**In start move!",x,y)
	up, right, left, down = 0,0,0,0
	g = 0
	while g<10:
		direction = random.randint(1,4)        
		print("==================",direction,num_iters)
		if direction == 1:
			if (y-2 > 0): 
				print(len(pixels),len(pixels[0]),x,y, "a")
				print(pixels[y-2][x])
				if pixels[y-2][x] == "*":
					print("!!!!!!")
					pixels[y-1][x] = " "
					pixels[y-2][x] = " "
					print("pixel",direction," marked")
					g+=1
					startmove(x,y-2, num_iters+1)
				else:
					up = 1
			# else:
			up = 1
		if direction == 2:
			if (x+2 < imgx):
				print(x,y, "b")
				if pixels[y][x+2] == "*":
					pixels[y][x+1] = " "
					pixels[y][x+2] = " "
					print("pixel",direction," marked")
					startmove(x+2,y,num_iters+1)
				else:
					right = 1
			# else:
			right = 1
		if direction == 3 :
			if (y+2 < imgy):
				print(x,y, "c")
				if pixels[y+2][x] == "*":
					pixels[y+2][x] = " "
					pixels[y+1][x] = " "
					print("pixel",direction," marked")
					startmove(x,y+2, num_iters+1)
				else: 
					down = 1
			# else:
			down = 1
		if direction == 4:
			if (x-2 > 0):
				print(x,y, "direction")
				if pixels[y][x-2] == "*":
					pixels[y][x-1] = " "
					pixels[y][x-2] = " "
					print("pixel",direction," marked")
					startmove(x-2,y, num_iters+1)
				else: 
					left = 1
			# else:
			left = 1
		print(up,right,left,down)
		g+=1
		if up == 1 and right == 1 and left == 1 and down == 1:
			if (x,y) == (1,1):
			    #image.show()
			    for q in range(imgy):
			    	print(pixels[q][imgx])
			print("Go back")
			return
	for q in range(imgy):
		print(*pixels[q][imgx])


startmove(1,5,0)

image.show()