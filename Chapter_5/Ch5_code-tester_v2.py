'''
NCC : CH 5.
CODE TESTER

Project: PyTek
Code by: ashNOLOGY

'''




#------ The Imports
import math
import random
import os

'''
#-- to clear the screen
#-- for Windows
clear = lambda: os.system('cls')
clear()


#-- to clear the screen
#- Linus systems
clear = lambda: os.system('clear') 
clear()
'''

# intro
print("\n\t\t\t---------------------"
      "\n\t\t\t| CH5 : Code Tester | "
      "\n\t\t\t----------------------\n")

'''
Create a POOL with 40 points
Allow the user to add/substract from it
'''




'''
IN THIS SECTION:
-Testing out the while loop
-Creating the dictionay
-ADDING to the dictionary
///////////////////////////////////////
'''




#Total Points
TotalPoints = 40
TakenOut = 0
print("Total Points are: ", TotalPoints, "\n")

# The Dictionary
dd = {"Strength": 0, "Health": 0, "Wisdom": 0}
print(dd)

#-- the user's answer to the While loop
answer = "y"

#-- the answer for add or sub
answer2 = ""


#--  the answer for S / H / W
answer3 = ""

'''
IN THIS SECTION:
-set up a loop for adding / subtracting
-This could be the main loop
-it allows you to do the following:
  Add or Subtract
  To keep repeating those choices
  
////////////////////////
'''

while (answer == 'y'):
    answer2 = int(input("\n1~ to Add [+]  \n2~ to Subtract [-] \n\t\tChoice: "))

    # /////////////////////////////////
    #The ADDING Section
    if(answer2 == 1):
        # --Showing the user the correct SIMPLE choices
        print("\ns- Strength"
              "\nh- Health"
              "\nw- Wisdom")

        # Choosing the "key" to change
        userInput = input("\nWhich do you want to change? s/h/w: ")


        # -- this will be the "Value" change
        userInput2 = int(input("Add how many Points? "))

        # -- the IF STATEMENT
        # -- depending on the choice, it will make that
        if (userInput == 's'):
            dd["Strength"] += userInput2
        if (userInput == 'h'):
            dd["Health"] += userInput2
        if (userInput == 'w'):
            dd["Wisdom"] += userInput2

        # -- printing the updated dictionary
        print("\n Updated Information \n", dd)

        # updating Total Points to reflect
        TotalPoints -= userInput2
        print("\t\t\tYou have ", TotalPoints, " left")





    #/////////////////////////////////
    #The SUBTRACTION section
    if(answer2 == 2):
        # --Showing the user the correct SIMPLE choices
        print("\ns- Strength"
              "\nh- Health"
              "\nw- Wisdom")

        # Choosing the "key" to change
        userInput = input("\nWhich do you want to change? s/h/w: ")
        userInput.lower()

        # -- this will be the "Value" change
        userInput2 = int(input("Add how many Points? "))

        # -- the IF STATEMENT
        # -- depending on the choice, it will make that
        if (userInput == 's'):
            dd["Strength"] -= userInput2
        if (userInput == 'h'):
            dd["Health"] -= userInput2
        if (userInput == 'w'):
            dd["Wisdom"] -= userInput2

        # -- printing the updated dictionary
        print("\n Updated Information \n", dd)

        # updating Total Points to reflect
        TotalPoints += userInput2
        print("\t\t\tYou have ", TotalPoints, " left")



    #To go back to the loop
    answer = input("\nWould you like another? \n\t y/n:  ")







# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")
exit()