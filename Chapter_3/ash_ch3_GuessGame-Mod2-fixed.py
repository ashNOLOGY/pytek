'''
NCC + GitKraken
Chapter 3
The Guessing Game [mod // v2]

Project: PyTek
Code by: ashNOLOGY

'''
import math
import random

#Name of the Game
print("\nThe Guessing Game : MOD"
      "\n-----------------------"
      "\n\n")

#The computer randomly picks a number : cnum
cnum = random.randint(1,5) #range between 1 - 5
print("The Computer is guessing: ", cnum)

#Asks the user to guess [limit this to 3 guesses]
#While Guess is under 3 ... keep going : hgus

hgus = 3 #the number of guesses
answer = 0 #the user's guess


#the WHILE loop
answer = int(input("guess the number: " )) #user's guess
while (0 < hgus):
    # Show the number of guess you have.
    print("Your number of guesses left: [",hgus,"] ")

 #check it against the picked number
    if answer < cnum:
       #answer = 0
       answer = int(input("\nguess a higher number: "))  #user's "higher" guess
       hgus = hgus -1


    if answer > cnum:
       #answer = 0
       answer = int(input("\nguess a lower number: "))  #User's guess
       hgus = hgus -1

    if answer == cnum:
        print("\nYou got it"
              "\nG A M E --- O V E R")
        exit()

    #continue
    #else:
     #   print("You lost, the Number was: ", cnum)




#Game Over +  EXIT
input("\nG A M E --- O V E R"      
      "\nEnter to Exit ")