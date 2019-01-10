import random
choice1 = random.randint(0,1)
if choice1 != 1:
	choice2 = random.randint(0,1)
	if choice2 != 1:
		choice3 = 1
	else:
		choice3 = 0
else:
	choice2 = 0
	choice3 = 0

drpck = input("Choose Door 1, 2, or 3: ")
if drpck = 1:
	if choice3 != 1:
		switch = input("Door 3 Does Not have the prize. Would you like to switch? ")
	else:
		switch = input("Door 2 Does Not have the prize. Would you like to switch? ")
if drpck = 2:
	if choice1 != 1:
		switch = input("Door 1 Does Not have the prize. Would you like to switch? ")
	else:
		switch = input("Door 3 Does Not have the prize. Would you like to switch? ")
if drpck = 3:
	if choice2 != 1:
		switch = input("Door 2 Does Not have the prize. Would you like to switch? ")
	else:
		switch = input("Door 1 Does Not have the prize. Would you like to switch? ")

