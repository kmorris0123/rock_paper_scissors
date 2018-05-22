import os
import random

os.system('clear')
play = True

print("-Rock, Paper or Scissors Game-")
print("")
while play == True:

	random_choice = random.randint(1,3)
	if random_choice == 1:
		final_choice = "rock"

	if random_choice == 2:
		final_choice = "paper"

	if random_choice == 3:
		final_choice = "scissors"


	print("Enter rock, paper or scissors")
	choice = input("--> ").lower()
	
	if choice == "rock" and final_choice == "rock":
		print("There was no winner, Try Again!")

	elif choice == "paper" and final_choice == "paper":
		print("There was no winner, Try Again!")

	elif choice == "scissors" and final_choice == "scissors":
		print("There was no winner, Try Again!")

	elif choice == "rock" and final_choice == "paper":
		print("You have lost")

	elif choice == "rock" and final_choice == "scissors":
		print("You have won!")

	elif choice == "paper" and final_choice == "scissors":
		print("You have lost!")

	elif choice == "paper" and final_choice == "rock":
		print("You have won!")
	
	elif choice == "scissors" and final_choice == "rock":
		print("You have lost!")

	elif choice == "scissors" and final_choice == "paper":
		print("You have won!")



	play_again = input('Do you want to play again? "Yes" or "No": ').lower()

	if play_again == "yes":
		play = True
		os.system('clear')
	else:

		play = False