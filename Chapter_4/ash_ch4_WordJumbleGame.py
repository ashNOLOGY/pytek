'''
NCC
Chapter 4
The Word Jumble Game

Project: PyTek
Code by: ashNOLOGY

'''

#------ The Imports
import math
import random
import os

#Greeting the player
print("\n\t\t\tWelcome to the Word Jumble Game"
      "\n\t\t\t-------------------------------")


'''
SECTION 1
-We create a list of words
-We have python randomly choose a word from that list
'''



#Creating the sequence of the words
words = ("python", "easy", "ash")

#Pick a word at random from "words"
random_word = random.choice(words)
#Setting up the "correct" // the randomly choosen word to be tested against
correct = random_word

#checking to make sure CORRECT is picking up a word
print("The correct word is: [ ", correct, " ]")


'''
SECTION 2
-We take the Random Word and Jumble it
'''

#Jumble will store the newly jumbled word
jumble = ""
new_random_word = ""

#setting up the WHILE loop
while random_word:
    #finding the length of the randwom_word, and randomly choosing a position
    position = random.randrange(len(random_word))
    print("The position is: ", position)

    #adding to the jumble
    jumble += random_word[position]
    print("\nThe Jumble word is: ", jumble)

    #random_word = random_word[:position] + random_word[(position + 1)]
    #print("\n New Random Word is: ", new_random_word)






    #creating the new jumbled word




#print("\nThe New Random Word is: ", new_random_word)


#ENTER to Exit
input("\n\n\t\t\tEnter to Exit")

