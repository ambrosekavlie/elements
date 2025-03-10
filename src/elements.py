#!/usr/local/bin/python3
# Elements: a small program to make memorizing the elements of the periodic table easy

from constants import *
import os
import time

# you win message
def you_win():
    partial = ""
    for i in YOU_WIN_MSG:
        partial += i
        print(partial)
        time.sleep(YOU_WIN_SPEED)

if __name__ == "__main__":
    time1 = time.time()
    os.system("clear")
    i = START_ELEMENT - 1
    print(f"You are at element {i+1}.")
    while i < len(ELEMENTS):
        element = ELEMENTS[i]
        element_input = input()
        if element_input == element:
            # if is correct, move on to next element
            i += 1
        else:
            # if not correct move back SET_BACK elements and clear screen. Display incorrect message.
            input(f"Incorrect, the answer is {element}.")
            os.system("clear")
            # if hardcore mode is true, reset to 0.
            if HARDCORE_MODE:
                i = 0
            else:
                # if false, go back SET_BACK elements
                i -= SET_BACK
            # make sure i is > 0 in case it sets back before Hydrogen we don't go farther than that
            if i <= 0:
                i = 0
                print("You are at element 1.")
            else:
                print(f"You are at element {i+1}. The previous element is {ELEMENTS[i-1]}.")
    time2 = time.time()
    # get time that the test took
    time_taken = time2 - time1
    
    # print you win message
    you_win()
    
    # time and highscore logic below:
    
    # try and catch, if file doesn't exist just count the score as highscore
    try:
        # open file
        with open("highscore", 'r') as highscore_file:
            highscore = (float)(highscore_file.read())
        if time_taken < highscore:
            # if time taken is less than highscore, set new highscore and print highscore message
            highscore = time_taken
            with open("highscore", 'w') as highscore_file:
                highscore_file.write((str)(highscore))
            print(f"\nHIGHSCORE! You took {time_taken} seconds to complete the test.")
        else:
            # else, print normal message that is not highscore
            # also print your previos highscore
            print(f"\nYou took {time_taken} seconds to complete the test. Good job!")
            print(f"Previous highscore: {highscore}")
    except FileNotFoundError:
        # if file not found, print highscore things because t'is first score
        highscore = time_taken
        with open("highscore", 'w') as highscore_file:
            highscore_file.write((str)(highscore))
        print(f"\nHIGHSCORE! You took {time_taken} seconds to complete the test.")
