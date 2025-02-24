#!/usr/bin/env python3

"""
This is a text based version of MasterMind written in Python 3 to run
in a terminal. (python mastermind.py or python3 mastermind.py). These
emoticons 🔴 🟠 🟢 🔵 🟣 🟡 ⚫ ⚪ 🟤 are used to represent the pegs.

A overview of the code:
Colours Dictionary: Maps colour codes to corresponding emoticon.
Terminal Setup: Changes the size of the terminal area and clears it.
Introduction: Provides an introduction to the game and explains
the meaning of emoticons used for hints.
Game Loop: The game is played within a while loop. The computer randomly
generates a hidden code, and the player has up to 8 guesses to figure it out.
Player Input: Takes input from the player, ensuring that they enter
exactly 4 valid color codes.
Answer Function: Compares the player's guess with the hidden code and
generates hints in the form of emoticons.
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

# A dictionary for the colours
colours: dict[str, str] = {"r": "🔴", "o": "🟠", "g": "🟢", "b": "🔵", "p":
                           "🟣", "y": "🟡", "k": "⚫", "w": "⚪", "n": "🟤"}

# Change size of terminal and clear it
sys.stdout.write(f"\x1b[8;{38};{80}t")
os.system('cls||clear')

# Text to tell you what's what
print("\nThis is a text based version of MasterMind written in Python 3.")
print("Emojis are used instead of coloured pegs.")
print("After your guess the program will help you with the following hints")
print("  ⚫ - Black. A colour that is present and is correctly placed. ")
print("  ⚪ - White. A colour that is present but in the wrong place.")
print("  🟤 - Brown. No hints.")
print("These help pegs do not align with the position of the guess pegs.\n")

playagain: bool = True
while playagain:

    hidden_code: list[str] = []  # the hidden code
    guess: list[str] = []  # the players's choice
    prompt: list[str] = []  # the help pegs or prompt
    attempt: int = 0  # number of guessed made by the player
    get: str = "Enter: r for 🔴, o for 🟠, g for 🟢, b for 🔵, p for 🟣, y for 🟡: "

    def get_colour(c: str) -> str:
        colour: str = colours[c]
        return colour

    def playerinput() -> str:
        while True:
            choice: str = ""
            choice = input(str(get))
            if len(choice) != 4:
                print("Enter 4 and only 4 colours.")
            else:
                if len(choice) == 4:
                    contained: list[str] = [x for x in choice if x in "rogbpy"]
                    if len(contained) == 4:
                        return choice
                    else:
                        print("You must only enter r, o, g, b, p or y")

    def answer(hidden: list[str], guess: list[str]) -> list[str]:
        myanswer: list[str] = []
        a: list[str] = hidden
        b: list[str] = guess
        marka: list[bool] = [False, False, False, False]
        markb: list[bool] = [False, False, False, False]
        choice: str

        for i in range(4):
            if a[i] == b[i]:
                marka[i] = True
                markb[i] = True
                choice = "k"  # a black peg
                myanswer.append(get_colour(choice))

        for i in range(4):
            for j in range(4):
                if a[i] != b[j]:
                    continue
                elif a[i] == b[j] and marka[i] is False and markb[j] is False:
                    marka[i] = True
                    markb[j] = True
                    choice = "w"  # a white peg
                    myanswer.append(get_colour(choice))

        while len(myanswer) < 4:
            myanswer.append(get_colour("n"))  # brown pegs
        return myanswer

    # Computer choice - hidden until guessed correctly or game ended
    for i in range(4):
        choice: str = random.choice("rogbpy")
        hidden_code.append(get_colour(choice))

    # Play until you win or make 8 wrong guesses
    while attempt < 8:
        attempt += 1

        # Players choice must be 4 coloured pegs
        choice = playerinput()
        for i in range(4):
            guess.append(get_colour(choice[i]))

        # Computer's prompt to help player to make better guess
        prompt = answer(hidden_code, guess)
        random.shuffle(prompt)

        # Printing guesses and prompts and the next guess
        print(f"Guess {attempt}: Your guess was: {guess[0]}, {guess[1]}, {guess[2]}, {guess[3]}", end='')
        print(f" | My prompt is {prompt[0]}, {prompt[1]}, {prompt[2]}, {prompt[3]}\n")

        # Check for win
        if prompt == ["⚫", "⚫", "⚫", "⚫"]:
            print("Congratulations! Your a winner!")
            print(f"The hidden code was {hidden_code[0]}, {hidden_code[1]}, {hidden_code[2]}, {hidden_code[3]}")
            break
        elif attempt == 8:
            # If no win after 8 attempts
            print("The computer wins")
            print(f"The hidden code was {hidden_code[0]}, {hidden_code[1]}, {hidden_code[2]}, {hidden_code[3]}")
            break
        
        # Attempts < 8? Clear your choice memory for  next go
        guess = []

 
    # End detail
    again: str = input("\nPlay again? \nY for Yes or \nN to Quit: ")
    if len(again) == 0:
        again ="y"
    elif again[0].lower() == "y":
        os.system('cls||clear')
        continue
    else:
        print("\nThank you for playing!")
        print("Bye! 👋\n")
        playagain = False
        sys.stdout.write(f"\x1b[8;{24};{80}t")
