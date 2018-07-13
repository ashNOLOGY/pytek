'''
NCC
Chapter 3
The Coin Flip Game

Project: PyTek
Code by: ashNOLOGY

'''
import math
import random

#Name of the Game
print("\nThe Coin Flip Game"
      "\n------------------\n")

#Set up the Heads & Tails as 0
h = 0
t = 0

#ask user how many flips should it do
howMany = int(input("How many flips? "))

#Set up the random FLIPPER to flip 100 times
#While Loop for the flips?

i = 0
while (i < howMany):
    f = random.randint(1,2) #The flip
    # If loop for the Heads & Tails?
    # If its 1 its/add to Heads
    # If its 2 its/add Tails

    if f == 1:
        h = h + 1
    else:
        t = t + 1
    i = i +1
    #print(f)


#Display the result for H & T
print("\nHeads: ", h)
print("Tails: ", t)



#ENTER to Exit
input("\nENTER to EXIT")
