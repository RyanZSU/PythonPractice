# http://www.codeskulptor.org/#user10_Yakdej8X6uunZ9D.py

# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    """
    Convert number to a name
    """
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Cannot convert " + str(number) + " to a name"
        return None

    
def name_to_number(name):
    """
    Convert name to a number
    """
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print 'Cannot convert "' + name + '" to a number'
        return None


def rpsls(name): 
    """
    Rock-paper-scissors-lizard-Spock game
    """
    
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)    
    if (player_number == None):
        return None
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5

    # use if/elif/else to determine winner        
    if (difference == 0):
        result = "Player and computer tie!"
    elif (difference >= 1 and difference <= 2):
        result = "Player wins!"
    elif (difference >= 3 and difference <= 4):
        result = "Computer wins!" 
   
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    if (comp_name == None):
        return None
    
    # print results
    print ""
    print "Player chooses " + name
    print "Computer chooses " + comp_name
    print result
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

