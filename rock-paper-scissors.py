#G3 Interactive Python
#1 Rock-paper-scissor

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
# for git test 

def number_to_name(number):
    # fill in your code below
    if number == 0:
        result = "rock"
    elif number == 1:
        result = "Spock"
    elif number == 2:
        result = "paper"
    elif number == 3:
        result = "lizard"
    elif number == 4:
        result = "scissors"
    else:
        result = "Not a valid Number"
    return result
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == 'rock':
        result = 0
    elif name == 'Spock':
        result =  1
    elif name == 'paper':
        result = 2
    elif name == 'lizard':
        result = 3
    elif name == 'scissors':
        result = 4
    else:
        result = "Not a valid String"
    return result
    

    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(player_guess): 
    # fill in your code below
    import random

    # convert name to player_number using name_to_number
    player_number = name_to_number(player_guess)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number)% 5
    
    print ""
    print "Player chooses " + player_guess
    print "Computer chooses " + number_to_name(comp_number)
    

    # use if/elif/else to determine winner
    if difference == 1 or difference == 2:
        print "Player wins!"
        
    elif difference == 0:
        print "Player and Computer tie!"
        
    else:
        print "Computer wins!"
    

    # convert comp_number to name using number_to_name
    
    
    
    # print results
    
   
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

