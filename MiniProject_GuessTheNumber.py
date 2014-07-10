# http://www.codeskulptor.org/#user10_d9WCirgJYqFF9vj.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
remaining_guesses = 7
secret_num = 0

# Print the message each time starting a new game
def init():
    global num_range, remaining_guesses, secret_num
    remaining_guesses = math.ceil(math.log(num_range + 1, 2))
    secret_num = random.randrange(num_range)
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", remaining_guesses
    print ""
    
# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts    
    global num_range
    num_range = 100
    init()
    
def range1000():    
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    init()

def get_input(guess):
    # main game logic goes here	
    global remaining_guesses, secret_num    
    guess_num = int(guess)
    remaining_guesses = remaining_guesses - 1
    print "Guess was", guess_num
    print "Number of remaining guesses is", remaining_guesses
    
    if (secret_num == guess_num):
        print "Correct!"
        print ""
        init()
    elif (remaining_guesses == 0):
        print "You ran out of guesses. The number was", secret_num
        print ""
        init()
    elif (secret_num > guess_num):
        print "Higer!"
        print ""
    elif (secret_num < guess_num):
        print "Lower!"
        print ""
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

# start frame
frame.start()

init()

# always remember to check your completed program against the grading rubric
