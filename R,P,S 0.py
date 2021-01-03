import random
y = 5
x = 5
ys = 0
cs = 0

def intro():
	print("WELCOME to the rock paper scissors game ")
	print('Use help or "h" for more details')
	
intro()

while y > 0:
	try:
		limit = int(input(">Set the winning point :"))
		break
	except ValueError:
		print(">invalid input please input a number")
	
	
print("Lets begin...")

while x > 0:
	you = input("> ").lower()
	c = ["rock","paper","scissors"]
	comp = random.choice(c)
	

	if you == "help" or you == "h":
		print('Use "r" for rock')
		print('Use "p" for paper')
		print('Use "s" for scissors')
		
		
	elif you != "r" and you != "p"and you != "s":
		print("You FOOL use help for more details")
	
	elif you == "r":
		print("> " + comp)
		
		if comp == "scissors":
			print("You destroyed the scissors")
			ys += 1
			print(f"Your point(s): {ys}")
			print(f"Opponent's point(s): {cs}")
				
	
		elif comp == "paper":
			print("The paper covered your rock(game's logic)")
			cs +=1
			print(f"Opponent's point(s): {cs}")
			print(f"Your point(s): {ys}")
		
					
		elif comp == "rock":
			print("Its a draw")
			print(f"Your point(s): {ys}")
			print(f"Opponent's point(s): {cs}")
			
	elif you == "p":
		print("> " + comp)
		
		if comp == "rock":
			print("The game's logic made you win")
			ys += 1
			print(f"Your point(s): {ys}")
			print(f"Opponent's point(s): {cs}")
				

		
		elif comp == "scissors":
			print("The scissors tore your paper into pieces")
			cs += 1
			print(f"Your opponent's point(s): {cs}")
			print(f"Your point(s): {ys}")
			
				
		elif comp == "paper":
			print("Its a draw")
			print(f"Your point(s): {ys}")
			print(f"Your opponent's point(s): {cs}")
		
	elif you == "s":
		print("> " + comp)
		
		if comp == "paper":
			print("You tore the papers ")
			ys += 1
			print(f"Your point(s): {ys}")
			print(f"Your opponent's point(s): {cs}")
				
				
		elif comp == "rock":
			print("The rock destroyed your scissors")
			cs += 1
			print(f"Your opponent's point(s): {cs}")
			print(f"Your point(s): {ys}")
				
		elif comp == "scissors":
			print("Its a draw")
			print(f"Your point(s): {ys}")
			print(f"Opponent's point(s): {cs}")
	
	if  ys == limit:
		print("You WIN!!")
		break
	
			
	if cs == limit:
		print("You LOSE! the opponent reached "+str(limit)+" point(s)")
		break
	

if ys > cs:
	with open("rps_score.txt", "a") as d:
		d.write(f"\n\n>Winning point(s): {limit} \nYour point(s): {ys} \n opponent's point(s): {cs} \nResult: You won")

elif ys < cs:
	with open("rps_score.txt", "a") as d2:
		d2.write(f"\n\n>Winning point(s): {limit} \nYour point(s): {ys} \n opponent's point(s): {cs} \nResult: You lost")
		






