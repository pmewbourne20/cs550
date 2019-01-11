import random 
import sys
import matplotlib.pyplot as plt

trials = sys.argv[1]
trials = int(trials)/10
table = []

for x in range(1,3):
	print(x)
for i in range(2):
	k = [0]*11
	table.append(k)

for i in range(11):
	table[0][i] = i

results = []
for j in range(1000):
	total = 0
	for i in range(10):
	 	flip = random.randint(0,1)
	 	total += flip
	results.append(total)

for q in range(int(trials)):
	heads = 0
	for i in range(10):
		x = random.randint(0,1)
		if x == 1:
			heads += 1
		placement = heads
	table[1][placement] += 1

for x in table:
	print(*x)

display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]] += 1

x_axis = [x for x in range(11)]
data2 = [y for y in range(5,16)]

#plt.plot(x_axis, display, 'b*', x_axis, data2, 'r^')
plt.bar(x_axis, display, color=(0.5,0.5,0.2,1))
plt.ylabel("Number of Trials")
plt.xlabel("Numebr of Heads")
plt.show()
