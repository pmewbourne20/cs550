import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# x_points = range(-100,100)
# y_points = range(-100,100)
# p = ax.plot(x_points, y_points, 'b')
# ax.set_xlabel('x-points')
# ax.set_ylabel('y-points')
# ax.set_title('Simple XY point plot')
# plt.show()
import math as m
import random
xinit = 0
yinit = 0
xrand = xinit
yrand = yinit
returns = 0
results = []


def down():
	global yrand
	yrand -= 1
def left():
	global xrand
	xrand -= 1
def up():
	global yrand
	yrand +=1
def right():
	global xrand
	xrand += 1

results = []
def run():
	global returns
	for x in range(11):
		r = random.randint(1,4)
		if r == 1:
			down()
		elif r == 2:
			left()
		elif r == 3:
			up()
		elif r == 4:
			right()
	distance = m.sqrt(((xrand-xinit)**2) + ((yrand-yinit)**2))
	if distance < 4:
		returns += 1
	print(distance)




for x in range(1001):
	run()
print(returns)
print(x)


display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]] += 1

plt.plot(display)