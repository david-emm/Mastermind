'''
This game was written as an exercise using the curses module included
in Python 3.12 on a Linux machine. (Linux Mint 22.2) It is written to
run in the Terminal (python3 mastermind.py).

The game uses these emojis, 🔴 🟠 🟢 🔵 🟣 🟡, to represent
the coloured pegs as they negate the need to download images and
are included in the font package used by the Terminal.

The Terminal has a useful zoom feature that can be used to expand
the terminal size and the game, both text and emojis, inside it.
(Use Ctrl++ to expand, or Ctrl+- to reduce).

Mastermind or Master Mind is a code-breaking game for two players
invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and
telecommunications expert. It resembles an earlier pencil and paper
game called Bulls and Cows that may date back a century.

'''

import curses
import random

# The color dictionary
colours: dict[str, str] = {'r': '🔴', 'o': '🟠', 'g': '🟢', 'b': '🔵', 'p':
                        '🟣', 'y': '🟡', 'k': '⚫', 'w': '⚪', 'n': '🟤'}

# Returns an emoji from the player or the hidden code input
def get_colour(c: str) -> str:
    colour: str = colours[c]
    return colour

# The computer's choice - hidden until guessed correctly or game ended
def hidden() -> list:
        alpha:list = []
        for i in range(4):
            choice: str = random.choice('rgbyop')
            alpha.append(get_colour(choice))
            # beta: str = '  '.join(alpha)
        return alpha

# Converts a list (of emojis) into a string
def make_str(beta: list) -> str:
    gamma: str = '  '.join(beta)
    return gamma

# Converts a string into a list
def make_list(beta: str) -> list:
     gamma: list = beta.split()
     return gamma

# Computes computer's answer to the player's input
def answer(hidden: list[str], guess: list[str]) -> list[str]:
    reply: list[str] = []
    a: list[str] = hidden
    b: list[str] = guess
    marka: list[bool] = [False, False, False, False]
    markb: list[bool] = [False, False, False, False]
    choice: str

    for i in range(4):
        if a[i] == b[i]:
            marka[i] = True
            markb[i] = True
            choice = 'k'  # a black peg
            reply.append(get_colour(choice))
    for i in range(4):
        for j in range(4):
            if a[i] != b[j]:
                continue
            elif a[i] == b[j] and marka[i] is False and markb[j] is False:
                marka[i] = True
                markb[j] = True
                choice = 'w'  # a white peg
                reply.append(get_colour(choice))
    while len(reply) < 4:
        reply.append(get_colour('n'))  # brown pegs
    random.shuffle(reply) # mix up order of answer prgs
    return reply

# This window displays the game explanation window and then is deleted
def preview():
    # Add the preview window
    prewin = curses.newwin(11, 70, 3, 5)
    prewin.box()
    # Print colored text
    prewin.addstr(1, 2, 'This is a text based version of MasterMind written in Python 3')
    prewin.addstr(2, 2, 'These emojis, 🔴 🟠 🟢 🔵 🟣 🟡, are used instead of coloured pegs')
    prewin.addstr(3, 2, 'The computer will give you the following hints')
    prewin.addstr(4, 2, '  ⚫ - Black. A colour that is present and is correctly placed ')
    prewin.addstr(5, 2, '  ⚪ - White. A colour that is present but in the wrong place')
    prewin.addstr(6, 2, '  🟤 - Brown. No hints')
    prewin.addstr(7, 2, 'These help pegs do not align with the position of the guess pegs')
    prewin.addstr(8, 8, 'Press the bracketed letters to select the play option', curses.color_pair(1))
    prewin.addstr(9, 28, '(c)ontinue', curses.color_pair(1))
    # Refresh the screen to show the changes
    prewin.refresh()
    # Preview input loop
    while True:
        key = prewin.getch()
        if key == ord('c'):
            prewin.erase()
            prewin.refresh()
            return
# Sets up the 4 game windows
def game():
    # Game variables
    h_code: list = hidden()
    l_code: str = make_str(h_code)
    myguess: str = ''
    guess_line: int  = 1
    help_line:int  = 1
    peg_pos:int = 28
    go_count:int = 0
    peg_count:int = 0
    cover = '⚫  ⚫  ⚫  ⚫'

    # Adds window titles and the covered hidden answer code
    header = curses.newwin(2, 40, 3, 20)
    header.addstr(0, 5, 'Hidden  ' + cover + '  code', curses.color_pair(1))
    header.addstr(1, 5, 'Your Guess', curses.color_pair(2))
    header.addstr(1, 27, 'Help', curses.color_pair(2))
    header.refresh()

    # Adds the 'Your Guess' window
    guess = curses.newwin(10, 20, 5, 20)
    guess.box()
    guess.refresh()

    # Adds the computer's 'Help' window
    help = curses.newwin(10, 20, 5, 40)
    help.box()
    help.refresh()

# Add the player's window and starts the game
    player = curses.newwin(5, 69, 15, 6)
    player.box()
    player.addstr(1, 3,'Choose (r) : 🔴, (o) : 🟠, (g) : 🟢, (b) : 🔵, (p): 🟣, (y): 🟡', curses.color_pair(2))
    player.addstr(3, 12,'Your choice is ', curses.color_pair(1))
    player.refresh()

# Input loop
    # Generates a new hidden code and only plays for 8 gos
    while go_count < 8:
        key = player.getch()
        if key == ord('q'):
            player.addstr(1, 1,'                      Thank you for playing!                       ', curses.color_pair(1))
            player.addstr(3, 12,'                    Bye! 👋                         ', curses.color_pair(1))
            player.refresh()
            curses.napms(1000)
            quit()
        if peg_count < 4:
            if chr(key) in 'rogbpy':
                peg = get_colour(chr(key))
                player.addstr(3, peg_pos, peg)
                peg_pos += 4
                key = ''
                player.refresh()
                peg_count += 1
        if peg_count == 4:
            player.addstr(3, 44, '(Enter) or rejec(t)', curses.color_pair(1))
            if key == ord('q'):
                player.addstr(1, 1,'                      Thank you for playing!                       ', curses.color_pair(1))
                player.addstr(3, 12,'                    Bye! 👋                         ', curses.color_pair(1))
                player.refresh()
                curses.napms(1000)
                quit()
            if key == ord('t'):
                player.addstr(3, 12,'Your choice is                                         ', curses.color_pair(1))
                peg_count = 0
                peg_pos = 28
                myguess = ''
                player.refresh()
                continue
            if key == 10: # Use 10 as the Enter key code (curses.KEY_ENTER) is unreliable
                # Get a substring of length 22 starting from player line (3,28)
                byte_data = player.instr(3, 28, 22)
                # Convert bytes to list
                myguess = byte_data.decode('utf-8')
                # Add myguess to guess window
                guess.addstr(guess_line, 3, myguess)
                guess.refresh()
                guess_line +=1
                helper = make_str(answer(h_code, make_list(myguess)))
                help.addstr(help_line, 3, helper)
                help.refresh()
                help_line +=1
                go_count +=1
                if helper == '⚫  ⚫  ⚫  ⚫':
                    player.erase()
                    player = curses.newwin(5, 69, 15, 6)
                    player.box()
                    player.addstr(1, 16, 'Congratulations! You are the winner!', curses.color_pair(1))
                    player.addstr(3, 25, '(a)gain? or (q)uit', curses.color_pair(1))
                    player.refresh()
                    header.addstr(0, 13, l_code)
                    header.refresh()
                    key = player.getch()
                    if key == ord('a'):
                        game()
                    if key == ord('q'):
                       player.addstr(1, 1,'                      Thank you for playing!                       ', curses.color_pair(1))
                       player.addstr(3, 12,'                    Bye! 👋                         ', curses.color_pair(1))
                       player.refresh()
                       curses.napms(1000)
                       quit()
                elif go_count == 8:
                    player.erase()
                    player = curses.newwin(5, 69, 15, 6)
                    player.box()
                    player.addstr(1, 22, 'Hard luck, the computer wins', curses.color_pair(1))
                    player.addstr(3, 25, '(a)gain? or (q)uit', curses.color_pair(1))
                    player.refresh()
                    header.addstr(0, 13, l_code)
                    header.refresh()
                    key = header.getch()
                    if key == ord ('a'):
                        game()
                    if key == ord('q'):
                       player.addstr(1, 1,'                      Thank you for playing!                       ', curses.color_pair(1))
                       player.addstr(3, 12,'                    Bye! 👋                         ', curses.color_pair(1))
                       player.refresh()
                       curses.napms(1000)
                       quit()
                else:
                    player.addstr(3, 12,'Your choice is                                     ', curses.color_pair(1))
                    peg_count = 0
                    peg_pos = 28
                    myguess = ''
                    player.refresh()
                    continue

def main(stdscr):
    # Initialize color
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    # Clear screen
    stdscr.clear()
    # Hide cursor
    curses.curs_set(0)
    # Title
    stdscr.addstr(1, 31, "David's Mastermind", curses.color_pair(3))
    stdscr.refresh()
    # First show the game explanation window
    preview()
    # Now play the game until the player wins of runs out of goes
    game()

curses.wrapper(main)
