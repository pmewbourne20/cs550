import random 
win = 0
wrongdoor = 0

def redefine():
	global choice
	global prize
	global wrongdoor
	choice = random.randint(1,3)
	prize = random.randint(1,3)
	for x in range(1,4):
		if x != choice and x != prize:
			wrongdoor = x


def noswitch(choice):
	choice = choice

def switch(choice,wrongdoor):
	for x in range(1,4):
		if x != choice and x != wrongdoor:
			choice = x

print("No Switch:")
for x in range(1001):
	redefine()
	noswitch(choice)
	if choice == prize:
		win += 1
print(win, "wins")

print("Switch:")
for x in range(1001):
	redefine()
	switch(choice,wrongdoor)
	if choice == prize:
		win += 1
print(win, "wins")

#I have already learned the monty hall problem, so I know what is happening here. If you decide to switch, ypu raise your odds from 1/3 to 1/2, a huge increase. 