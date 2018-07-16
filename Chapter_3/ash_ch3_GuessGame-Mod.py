'''
NCC
Chapter 3
The Guessing Game [mod]

Project: PyTek
Code by: ashNOLOGY

'''
import math
import random

#Name of the Game
print("\nThe Guessing Game : MOD"
      "\n-----------------------"
      "\nYou only get 3 guesses.\n")

#The computer randomly picks a number : cnum
cnum = random.randint(1,5) #range between 1 - 5
print("The Computer is guessing: ", cnum)

#Asks the user to guess [limit this to 3 guesses]
#While Guess is under 3 ... keep going : hgus

hgus = 0 #the number of guesses
answer = 0 #the user's guess

#the WHILE loop
answer = int(input("guess the number: " )) #user's guess
while (hgus < 2):
    #print("\nYou have ",hgus," guesses left")

 #check it against the picked number
    if answer < cnum:
       #answer = 0
       answer = int(input("guess a higher number: " ))  #user's "higher" guess
       hgus = hgus =1

    elif answer > cnum:
       #answer = 0
       answer = int(input("guess a lower number: " ))  #User's guess
       hgus = hgus +1

    elif answer == cnum:
        print("\nYou got it"
              "\n G A M E --- O V E R")
        exit()

   # else:
    #   print("\nYou Lost!")




#Game Over +  EXIT
input("\nG A M E --- O V E R"
      "\nEnter to Exit ")