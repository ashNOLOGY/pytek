'''
Guess The Number Game v3.0
-----------------
Project: [bini-tek]\\
Code by: Ash Dawod
2018

BRIEF DESCRIPTION
-----------------
In this game, the computer randomly picks a number
The user has to guess the number with limited number of guess.

'''

#--Imports
import math
import random


'''
/////////////////////
Defining the fuction
/////////////////////
'''


'''


#The computer randomly picks a number : computer_rand
computer_rand = random.randint(1,5) #range between 1 - 5
print("The Computer is guessing: ", computer_rand)

#Asks the user to guess [limit this to 3 guesses]
#While Guess is under 3 ... keep going : num_of_guesses

num_of_guesses = 2 #the number of guess 
user_guess = 0 #the user's guess which will be an input


#the WHILE loop
user_guess = int(input("Guess the number: " )) #user's guess
while (0 < num_of_guesses):
    # Show the number of guess you have.
    print("Your number of guesses left: [",num_of_guesses ,"] ")

 #check it against the picked number
    if user_guess == computer_rand:
        print("\nYou got it"
              "\nG A M E --- O V E R")
        exit()

    elif user_guess < computer_rand:
       user_guess = int(input("\nguess a higher number: "))  #prompt user to guess "Higher"
       num_of_guesses = num_of_guesses -1


    elif user_guess > computer_rand:
       user_guess = int(input("\nguess a lower number: "))  #prompt user to guess "Lower"
       num_of_guesses = num_of_guesses -1

    #continue
    #else:
     #   print("You lost, the Number was: ", computer_rand)

'''



'''
////////////////////////////
End of Defining the fuction
///////////////////////////
'''



'''
#Dispaly the Name of the program
print("\nGuess The Number Game v3.0"
      "\n  [bini-tek]\\\\"
      "\n---------------------------\n")



#Setting up the WHILE loop to do 2 main things:
#1: To call the FUNCTION
#2: To ask if the user wants do it again
while_again = 'y' # <-- the user_guess to the loop
while (while_again.lower() == 'y'):
    FUNCTION() <----!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Ask if the user wants to do it again
    while_again = input("\nWould you like to play again? Y/N: ")

#If the user_guess is not 'y'
#Thank the user & Exit
print("\n\n\n- - - - - - - - - - - - "
      "\nThank You / End of Program")
exit()

'''