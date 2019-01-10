import random 
import sys
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
