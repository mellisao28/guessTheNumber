# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

# initialize global variables used in your code
generatedNum=0
remaining_guess=0
last_game=0

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global generatedNum
    global remaining_guess
    global last_game
    
    # generate secret number
    generatedNum = random.randrange(0, 100)
    
    # decide on max number of guess
    remaining_guess = math.ceil(math.log (100,2))
    
    # save last game stage
    last_game=100
    
    # start a new game
    print "New game, range is from 0 to 100."
    print "Number of remaining guesses is " + str(remaining_guess) + "\n"
    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global generatedNum
    global remaining_guess
    global last_game
    
    # generate secret number
    generatedNum = random.randrange(0, 1000)
    
    # decide on max number of guess
    remaining_guess = math.ceil(math.log (1000,2))
    
     # save last game stage
    last_game=1000
        
     # start a new game
    print "New game, range is from 0 to 1000."
    print "Number of remaining guesses is " + str(remaining_guess) + "\n"
    
# validate input
def validate_inp(guess):
    try:
      num=float(guess)
      return num
    except:
      return False
    
def get_input(guess):
    # main game logic goes here	
    global remaining_guess
    
      
    # Check if player has started the game
    if last_game==0: 
        print "You need to start a game by choosing number ranges (1-100) or (1-1000)\n"
    else:    
        print "Guess was " + guess
        remaining_guess-=1
        
        # validate input, only take numbers (positive or negative)
        guess=validate_inp(guess)
       
        if guess!=False and guess==generatedNum:
            print "Number of remaining guesses is  " + str(remaining_guess) 
            print "Correct!\n"
            restart()
        else:
            if remaining_guess==0:
                print "You ran out of guesses. The number was " + str(generatedNum) + "\n"
                restart()
            else:  
                print "Number of remaining guesses is  " + str(remaining_guess) 
                # only take valid numbers
                if guess<0 or guess>=last_game or guess==False:
                     print "Input a number within [0-"+ str(last_game) + "] range!\n"
                elif guess>generatedNum:
                    print "Lower!\n"
                elif guess<generatedNum:
                    print "Higher!\n"
                else:
                    print "Input a number within [0-"+ str(last_game) + "] range!\n"

# restart game
def restart():
    if last_game==100: range100()
    else: range1000()     
      
# create frame
f=simplegui.create_frame("Guess A Number", 200, 200)

# register event handlers for control elements
f.add_button("Range: 0 - 100", range100, 200)
f.add_button("Range: 0 - 1000", range1000, 200)
f.add_input("Enter a guess", get_input, 200)


# start frame
f.start()

# always remember to check your completed program against the grading rubric
