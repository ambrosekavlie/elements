#!/usr/local/bin/python3
# Elements: a small program to make memorizing the elements of the periodic table easy

from constants import *
import json
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
    
    # try to open highscore.json file. If it doesn't exist, make it
    try:
        with open("data.json", 'r') as highscore_file:
            data = json.load(highscore_file)
    except FileNotFoundError:
        with open("data.json", 'w') as highscore_file:
            data = {
                # time taken + 1 so that it counts as highscore. maybe this can be done less awkwardly but it works
                "highscore" : time_taken+1
            }
            json.dump(data, highscore_file)
    
    # time and highscore logic below:
    
    if time_taken < data["highscore"]:
        # if time taken is less than highscore, set new highscore and print highscore message
        data["highscore"] = time_taken
        with open("data.json", 'w') as highscore_file:
            json.dump(data, highscore_file)
        print(f"\nHIGHSCORE! You took {time_taken} seconds to complete the test.")
    else:
        # else, print normal message that is not highscore
        # also print your previous highscore
        print(f"\nYou took {time_taken} seconds to complete the test. Good job!")
        highscore = data["highscore"]
        print(f"Previous highscore: {highscore}")
