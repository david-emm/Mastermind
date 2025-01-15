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
import tkinter as tk
from tkinter import ttk

# A dictionary for the colours
colours: dict[str, str] = {"r": "🔴", "o": "🟠", "g": "🟢", "b": "🔵", "p":
                           "🟣", "y": "🟡", "k": "⚫", "w": "⚪", "n": "🟤"}

# Change size of terminal and clear it
# sys.stdout.write(f"\x1b[8;{10};{10}t")
# os.system('cls||clear')

class App(tk.Tk):
	def __init__(self, size):
		super().__init__()
		self.title('Mastermind')
		self.geometry(f'{size[0]}x{size[1]}')

		self.frame = tk.Frame(self, bg='gray')
		self.frame.pack(expand = True, fill = 'both')
		
		self.mainloop()




app = App((800,600))        

