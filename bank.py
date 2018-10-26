class Bank:
	def __init__(self, PIN, money, openc):
			self.pin = PIN
			self.money = money
			self.openc = openc

	def withdraw(self):
		if self.openc:
			while True:
				pc = input("Please enter your PIN: ")
				if pc == self.pin:
					wa = int(input("Please enter an amount to withdraw: "))
					if wa <= self.money:
						self.money -= wa
						print("Your current balance is $",self.money)
						break
					else:
						print("Your balance is too low.")
				else:
					print("Incorrect PIN. Try again.")
		else:
			print("You need to open an account first.")


	def insert(self):
		if self.openc:
			while True:
				pc = input("Please enter your PIN: ")
				if pc == self.pin:
					ins = int(input("Please enter an amount to insert: "))
					self.money += ins
					print("Your current balance is $",self.money)
					break
				else:
					print("Incorrect PIN. Try again.")
		else:
			print("You need to open an account first.")

	def close(self):
		if self.openc:
			while True:
				pc = input("Please enter your PIN: ")
				if pc == self.pin:
					fq = input("Would you like to close the account? ")
					if fq == "yes":
						self.openc = False
					else:
						self.openc = True
					break


openc = False

xc = input("Type 'open' to open an account: ")
while True:
	if xc == "open":
		openc = True
		PIN = input("Please choose a 4 digit PIN: ")
		money = int(input("Please enter an initial amount of money"))
		break
	else:
		print("That is not an option.")

bank1 = Bank(PIN, money, openc)

while True:
	print("Your balance is $",bank1.money)
	choice = input("Would you like to insert money, withdraw money, or close the account? ")
	if choice == "withdraw":
		bank1.withdraw()
	elif choice == "insert":
		bank1.insert()
	else:
		print("That's not a valid option.")
