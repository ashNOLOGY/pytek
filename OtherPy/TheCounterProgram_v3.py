'''
The Counter Program
Project: [bini-tek]\\
Coded by: Ash Dawod
Aug/2018

# # # # # #

The program allows the user to count, forward or backward
Using any "STEP" wanted, to count every 2, 4, 7, 350
'''




#------ The Imports
import math
import random
from os import system , name
from time import sleep




''' 
///////////////////////
Defining The Functions
//////////////////////
'''

#-- The clear() FUNCTION
#-----------------------
def clear():
    if name == 'nt':
        # for Windows OS
        print("\n" * 15)
    else:
        _= system('clear')  # <-- for Linus / Mac

########################





#-- The Instrucions() Function
def instructions():
    #-- Clear the Screen
    clear()

    #-- Display the instructions
    print("\nINSTRUCTIONS"
          "\n------------"
          "\n"
          "\n-This program allows you to count in any range"
          "\n-Forward or Backward"
          "\n-To count BACKWARD:"
          "\n\t*Make sure to put the large number first"
          "\n\t*And to use \'negative\' STEP, ie: -1, -2, ect. "
          "\n\n\n")

    #-- Give the main_choices()
    main_choices()


########################









#-- The counter_program() FUNCTION
#-----------------------
def counter_program():
    # Clear the screen
    clear()

    # Ask the user for a Starting number
    start_num = int(input("Please enter START number: "))

    # Ask the user for an Ending number
    end_num = int(input("Please enter END number: "))

    # Ask the user for the Increment
    step_num = int(input("Please enter STEP number: "))

    print("\nYour START is:", start_num,
          "\nYour END is:", end_num,
          "\nYour STEP is: ", step_num)

    # result = [start_num : end_num : step_num]
    # print("\nYour results are: ", result )
    result = list(range(start_num, end_num, step_num))
    print("\nYour results are:", result)

'''
I need a looping mechanizm for this function
Either and IF or a WHILE loop
s
    #-- Check if the users wants to do it again
    uI_again = "n"
    uI_again = input("Would you like to do it agian? y/n: ")
    if (uI_again == 'y' or 'Y'):
        #-- run the function again
        counter_program()
    #if (uI_again == 'n' or 'N'):
        #-- print message + wait 2 seconds + clear screen + main choices
        #print("You've selected No")
        #sleep(2)
     #   clear()
     #   main_choices()
    else:
        print("That is not an option")
        main_choices()


'''



########################





#-- The main_choices() FUNCTION
#------------------------------

# variables for this function
def main_choices():
    print("\n"
          "Main Choices"
          "\n------------"
          "\n1. Instructions"
          "\n2. Start the Counter program"
          "\n3. Clear the Screen"
          "\n4. Exit")



    uI_mainChoice = "" # <-- the user's input
    #-- Getting the Users Input for their Main Choice
    uI_mainChoice = int(input("What is your choice: "))

    #-- the IF Statement for the Main Choice option
    if (uI_mainChoice == 1):
        #-- Present the instructions
        instructions()
    if (uI_mainChoice == 2):
        #-- run the Counter program
        counter_program()
    if (uI_mainChoice == 3):
        #-- clear the screen
        clear()
        main_choices()
    if (uI_mainChoice == 4):
        #-- Print Good Bye, and exit after 2 seconds
        print("Good Bye")
        sleep(2)
        exit()

    else:
        #-- if Option is not 1-4, print this and go back to Main Choices
        print("That is not an option")
        main_choices()

####################################






'''
////////////////////////////
END of Function Definitions
////////////////////////////
////////////////////////////
'''


#-- The Program Title
print("\n\t\t\t------------------------------"
      "\n\t\t\t| The Counter Program [v3.0] | "
      "\n\t\t\t|      [bini-tek]\\\\          |"
      "\n\t\t\t------------------------------\n")



#-- Calling the function
#-- Display the main_choices()
main_choices()








# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")