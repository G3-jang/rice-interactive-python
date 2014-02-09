#G3 Interactive Python
#2 Guess the number
import random
import simplegui
import math

# initialize global variables used in your code
secret_num = 0
rem_guess = 7
range_value = 1



print "Hi there!"
print ("\nWell , I'm thinking of a number ")
print ("\nTry guessin it !")


def new_game():
    
    global secret_num
    if range_value==1:
        range100()
    else:
        
        range1000()
        
    


# define event handlers for control panel
def range100():
    
    print "\nNew game! Range is from 0 to 100. "
    global secret_num,rem_guess,range_value
    rem_guess=7
    range_value = 1
    print ("Number of remaining guesses is : ", rem_guess)
    secret_num = random.randint(0,100)
    return secret_num
       
   

def range1000():
    print "\nNew game! Range is from 0 to 1000. "
    
    global secret_num,rem_guess,range_value
    rem_guess=10
    range_value=0
    print ("Number of remaining guesses is : ", rem_guess)
    secret_num = random.randint(0,1000)
    return secret_num
       
    
    
def get_input(guess):
    print "\nYour guess :" , guess
    global secret_num,rem_guess,range_value
    guess = int(guess)
    rem_guess = rem_guess-1
    print ("Number of remaining guesses is : ", rem_guess)
    
    if guess>100 and range_value==1:
        print "Your guess is out of range , Guess from 0 to 100"
        
    elif range_value==0 and guess>1000:
        print "Your guess is out of range , Guess from 0 to 1000"
    
    
    if secret_num < guess:
        if rem_guess==0:
            print "\nSorry , You ran out of guesses"
            print "The correct number is",secret_num 
            print "\n Try again!"
            new_game()
        else:
            print "Lower"
            
       
    elif secret_num > guess:
        if rem_guess==0:
            print "\nSorry , You ran out of guesses"
            print "The correct number is",secret_num 
            print "\n Try again!"
            new_game()
        else:
            print "Higher"
            
    
    else:
        print "\nYou're right , Fantastic job!!"
        new_game()
    

    
    

# create frame
frame = simplegui.create_frame("Guess the Number", 300, 300)



# register event handlers for control elements

inp = frame.add_input('Enter your guess:' , get_input ,200)
hund = frame.add_button('Range 0 to 100:' , range100 , 200)
thous = frame.add_button('Range 0 to 1000:' , range1000 , 200)
new = frame.add_button('Restart', new_game , 100)


# call new_game and start frame
frame.start()
new_game()

