import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps = [rock, paper, scissors]

cpu_choice = random.randint(0,2)

user_choice = int(input("Rock(0), Paper(1) or Scissors(2): "))
if user_choice <=2 and user_choice >= 0:
	
	result =[['tie', 'user', 'cpu'],['cpu', 'tie', 'user'],['user', 'cpu', 'tie']]

	decission = result[cpu_choice][user_choice]
	
	print("CPU's choice:")
	print(rps[cpu_choice])
	print("Your choice:")
	print(rps[user_choice])

	if decission == 'tie':
		print("It's Tie.")
	elif decission == 'cpu':
		print("You lose, Try again.")
	else:
		print("You won, Yayyy!")
else:
	print("Enter valid input.")
