'''
NCC
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
      "\n\t\t\t| CH5 : Code Tester | "
      "\n\t\t\t----------------------\n")

'''
Create a POOL with 40 points
Allow the user to add/substract from it
'''

#Total Points
TotalPoints = 40
TakenOut = 0
print("Total Points are: ", TotalPoints)

# The Dictionary
dd = {"s": 0, "h": 0 }
print(dd)

# ADDING to the dictionary
# Chossing the "key" to change
userInput = input("Which do you want to change? ")
# Choosing the amount to change
userInput2 = int(input("Add how many Points? "))
# making the change in the dictionary + printing
dd[userInput] = userInput2
print(dd)


# updating Total Points to reflect
TotalPoints -= userInput2
print("You have ", TotalPoints, " left")


# SUBTRACTING from the Dictionary
# choosing the "key" to manipulate
userInput = input("\nWhich to change next? ")
# choosing how much to take out
userInput2 = int(input("Subtract how much? "))
# making the modification to that index
dd[userInput] -= userInput2
print(dd)

# updating Total Points to reflect
TotalPoints += userInput2
print("You now have ", TotalPoints, " points")










'''
Testing the basic substraction of points
Successful.

userInput = int(input("How much to take out: "))
TakenOut = userInput
TotalPoints = TotalPoints - TakenOut
print("Total Points are now: ",TotalPoints )
print("Points Taken Out: ", TakenOut)
print("New Total Points are: ", TotalPoints)
'''



# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")