This is a text based version of MasterMind written in Python Emojis are used to represent coloured pegs.
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
