from game import Game
import curses


# This is the file that runs when you click "▶ Run"
# All this file does is pass our Game class to a curses method.
# Curses is a python library for interacting with the terminal,
# which our snake games does.
curses.wrapper(Game)