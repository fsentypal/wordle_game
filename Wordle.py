
import random

from WordleWordlist import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

# assigns solution to a random 5 letter word
solution = (random.choice(FIVE_LETTER_WORDS)).upper()

# define a function enter_action
def enter_action(guessedword):
    # define row to get the current row
    row = gw.get_current_row()
    # if the guessed word is the same as the solution word print 'You win!'
    if guessedword == solution:
        gw.show_message('You win!')
    # indexes the solution word and underlays it under the guessed word
    for index, a in enumerate(solution):
        gw.get_square_letter(row, index)
    # indexes the guessed word
    for index, b in enumerate(guessedword):
        # sets the row to the new one after moving on to the next row
        gw.set_square_letter(row, index, b)
        # the letter is the same as the solution letter make the square and keyboard green
        if b == solution[index]:
            gw.set_square_color(row, index, "#66BB66")
            gw.set_key_color(b, "#66BB66")
        # if the letter in solution make the square and keyboard yellow (if the key isn't already green)
        elif b in solution:
            gw.set_square_color(row, index, "#CCBB66")
            if gw.get_key_color(b) != "#66BB66":
                gw.set_key_color(b, "#CCBB66")
        # if the letter isn't in solution make the square and keyboard grey (if the key isn't already green or yellow)
        else:
            gw.set_square_color(row, index, "#999999")
            if gw.get_key_color(b) != "#66BB66" or gw.get_key_color(b) != "#CCBB66":
                gw.set_key_color(b, "#999999")
    # go to the next row
    gw.set_current_row(gw.get_current_row() + 1)

gw = WordleGWindow()
gw.add_enter_listener(enter_action)