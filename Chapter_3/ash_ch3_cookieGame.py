'''
NCC
Chapter 3
The Fortune Cookie Game

Project: PyTek
Code by: ashNOLOGY

'''

#import the proper libraries
import math
import random

#Name of the game
print("\nThe Fortune Cookie Game"
      "\n-----------------------\n")

#set up 5 fortunes
a = "fortune 1A "
b = "fortune 2B "
c = "fortune 3C "
d = "fortune 4D "
e = "fortune 5E "



#setting up the while loop
answer = "y"
while True:

    #set up a rf to choose a number between 1 & 5
    rf = random.randint(1,5)
    print(rf)

    #I need to associate the random number to a letter
    #The Number to Fortune association If Statement
    if rf == 1:
        print(a)

    elif rf == 2:
        print(b)

    elif rf == 3:
        print(c)

    elif rf == 4:
        print(d)

    else:
        print(e)

    #ask user if they want another
    answer = input("\nWant Another? ")

    #To Exit the While loop - set up the if statement to exit if user says No
    if answer == "n":
        exit()


#Enter to EXIT
input("\nENTER to Exit")