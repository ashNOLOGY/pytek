'''
DICE ROLLER test
DD uses a range of dice:
d6/8/10/20/200, Possibly more.

This will take input from user about the range of the dice

'''

import random


# UI: to generate the range of the dice
def diceRoll():
    diceRange = int(raw_input("Enter Dice Range: "))
    TheDice = random.randint(1,diceRange)
    print("You rolled a "+ str(TheDice)+"\n")

# UI: to keep rolling the dice
def keepRolling():
   while True:
       answer = raw_input("Roll? y or n : " )
       if answer == "y":
           diceRoll()
       else:
            break
    

# calling the function
keepRolling()








               
      
    
    


