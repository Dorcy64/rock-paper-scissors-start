rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
print("\n")
import random

Dorcy = random.randint(0, 2)

if Dorcy == human :
	print("Its a draw\n")
	if Dorcy == 0 and human == 0:
		print(f"You both chosse rock \n{rock}")
	elif Dorcy == 1 and human ==1:
		print(f"You both chosse paper\n{paper}")
	elif Dorcy == 2 and human ==2:
		print(f"You both chosse scissors\n{scissors}")

elif human == 0 or human == 1 or human == 2:
	if Dorcy == 0 and human == 2 :
		print(f"You chose scissors\n{scissors}")
		print("Dorcy chose rock you loose")
		print(rock)
		
	elif Dorcy == 1 and human == 0:
		print(f"You chose rock\n{rock}")
		print("Dorcy chose paper you loose")
		print(paper)
	elif Dorcy == 2 and human == 1:
		print(f"You chose paper{paper}")
		print("Dorcy chose scissors you loose")
		print(scissors)
	else :
		if Dorcy == 0 :
			print(f"You chose paper {paper}")
			print("You won")
			print("Dorcy chose rock")
			print(rock)
		elif Dorcy == 1 :
			print(f"You chose scissors {scissors}")
			print("You won")
			print("Dorcy chose paper")
			print(paper)
		elif Dorcy == 2 :
			print(f"You chose rock {rock}")
			print("You won")
			print("Dorcy chose scissors")
			print(scissors)
else:
	print("Invalid Number")