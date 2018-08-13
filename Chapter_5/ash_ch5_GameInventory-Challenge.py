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


# intro
print("\n\t\t\t---------------------"
      "\n\t\t\t| CH5 : Game Inventory | "
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
dd = {"strength": 0, "health": 0, "wisdom": 0, "dexterity": 0}
print(dd)


#-- the user's answer to the While loop
answer = "y"

#-- the answer for add or sub
answer2 = ""

'''
IN THIS SECTION:
-set up a loop for adding / subtracting
-This could be the main loop
-it allows you to do the following:
  Add or Subtract
  To keep repeating those choices
  
////////////////////////
'''
#-- While the Total Points are not 0 (zero), keep going
while (TotalPoints != 0):

    answer2 = int(input("\n1~ to Add [+]  \n2~ to Subtract [-] \n\t\tChoice: "))
    #The ADDING Section
    if(answer2 == 1):
        # Chossing the "key" to change
        userInput = input("\nWhich do you want to change? ")
        # Choosing the amount to change
        userInput2 = int(input("Add how many Points? "))
        # making the change in the dictionary + printing
        dd[userInput] = userInput2
        print(dd)

        # updating Total Points to reflect
        TotalPoints -= userInput2
        print("\t\t\tYou have ", TotalPoints, " left")

    #The SUBTRACTION section
    if(answer2 == 2):
        # choosing the "key" to manipulate
        userInput = input("\nWhich do you want to change? ")
        # choosing how much to take out
        userInput2 = int(input("Subtract how much? "))
        # making the modification to that index
        dd[userInput] -= userInput2
        print(dd)

        # updating Total Points to reflect
        TotalPoints += userInput2
        print("\t\t\tYou now have ", TotalPoints, " points")



    #To go back to the loop if there is still points
    if (TotalPoints != 0):
        answer = input("\nWould you like another? \n\t y/n:  ")
    else:
        print("\nYou Are Out of Points")










# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")
exit()