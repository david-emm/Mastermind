#!/usr/bin/env python3hints

"""
This is a text based version of MasterMind written in Python 3.
Emojis are used to represent coloured pegs.
A overview of the code:
Colours Dictionary: Maps colour codes to corresponding emojis.
Terminal Setup: Changes the size of the terminal and clears it.
Introduction: Provides an introduction to the game and explains
the meaning of emojis used for hints.
Game Loop: The game is played within a while loop. The computer randomly
generates a hidden code, and the player has up to 8 guesses
to figure it out.
Player Input: Takes input from the player, ensuring that they enter
exactly 4 valid color codes.
Answer Function: Compares the player's guess with the hidden code and
generates hints in the form of emojis.
Game Progress: Prints the player's current guess, the hints provided
by the program, and prompts for the next guess.
Winning Check: Checks if the player has guessed the correct code,
and if so, declares the player as the winner.
Play Again: Asks the player if they want to play again.
If yes, the game continues; otherwise, it exits.
Exit: Displays a farewell message and exits the program when the player
decides not to play again.
"""

import os
import sys
import random


# A dictionary for the colours.
colours: list[str] = {"r": "🔴", "o": "🟠", "g": "🟢", "b": "🔵", "p": 
			"🟣", "y": "🟡", "1": "⚫", "2": "⚪", "3": "🟤" }

# Change size of terminal and clear it.
sys.stdout.write(f"\x1b[8;{40};{100}t")
# Text to tell you what's what.
print("\nThis is a text based version of MasterMind written in Python 3.")
print("Emojis are used instead of coloured pegs.")
print("After your guess the program will help you with the following hints")
print("  ⚫ - Black. A colour is present and is correctly placed. ")
print("  ⚪ - White. A colour is present but in the wrong place.")
print("  🟤 - Brown. A colour is not in the answer.")
print("These help pegs do not indicate the position of the guess pegs.\n")
print("Enter 4 colours - back space may be used to correct entry.")

playagain = True
while playagain:
	
	mychoice: list[str] = []
	yourchoice: list[str] = []
	myprompt: list[str] = []
	guess: int = 0
	
	def get_colour(c: str) -> str:
		colour: str = colours[c]
		return colour

	def playerinput() -> str:
		while True:
			choice: str = ""
			choice = input("Enter: r for 🔴, o for 🟠, g for 🟢, b for 🔵, p for 🟣, y for 🟡: " )
			if len(choice) != 4:
				print("Enter 4 and only 4 colours.")
				continue
			for i in range(4):
				if choice[i] not in ("rogbpy") or choice == '':
					print("You must only enter r, o, g, b, p or y")
			else:
				
				return choice 
				
	def answer(hidden: list[str], guess: list[str]) -> list[str]:
		myanswer: list[str]= []
		a: list[str] = hidden
		b:list[str] = guess
		marka: list[bool] = [False, False, False, False] 
		markb: list[bool] = [False, False, False, False] 
		choice: str
		
		for i in range(4):
			for j in range(4):
				if a[i] == b[j] and (marka[i] == True or markb[j] == True):
					continue
				elif a[i] == b[j] and i == j:
					marka[i] = True
					markb[j] = True 
					choice = "1"
					myanswer.append(get_colour(choice))
				elif a[i] == b[j]:
					marka[i] = True
					markb[j] = True 
					choice = "2"
					myanswer.append(get_colour(choice))

		while len(myanswer) < 4:
			myanswer.append(get_colour("3"))
		return myanswer
				
	# Computer choice - hidden until guessed correctly or game ended.
	for i in range(4):
		choice: list[str] = random.choice("rogbpy")
		mychoice.append(get_colour(choice))
	# ~ mychoice = ["🔴", "🟠", "🔴", "🟡"]
	
	# Play until you win or make 8 wrong guesses.
	while guess < 8:
		guess += 1

		# Players choice must be 4 coloured pegs.
		choice:list[str] = playerinput()
		for i in range(4):
			yourchoice.append(get_colour(choice[i]))

		# Computer's prompt to help player to make better guess.
		myprompt = answer(mychoice, yourchoice)

		# Printing guesses and prompts and the next guess   
		print(f"\nThis is your quess {guess}")
		print(f"Your choice is {yourchoice[0]}, {yourchoice[1]}, {yourchoice[2]}, {yourchoice[3]}, | My prompt is {myprompt[0]}, {myprompt[1]}, {myprompt[2]}, {myprompt[3]}\n")
		
		# Check for win
		if myprompt == ["⚫", "⚫", "⚫", "⚫"]:
			print("Congratulations! Your a winner!")
			break 
		
		# Clear yourchoice memory for  next go.
		yourchoice = []
 
	print(f"The hidden code was {mychoice[0]}, {mychoice[1]}, {mychoice[2]}, {mychoice[3]}")

	# End detail
	playagain: str = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

	if playagain.lower() == "y":
		os.system('cls||clear')
		continue
	else:
		print("\nThank you for playing!")
		print("Bye! 👋\n")
		playagain = False


