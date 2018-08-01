'''
NCC
Chapter 4
Challenge 1

Project: PyTek
Code by: ashNOLOGY

'''


'''
-Create a program that prints a list of words in random order.
-It should print ALL the words, but not repeat any.
pg.96+97 have a random word order print function, but it repeats
//length of list
//random
//index / enumeration
'''

#------ The Imports
import math
import random
import os



# Game intro
print("\n\t\tWelcome to Rand-Word"
      "\n\t\t--------------------\n")


'''
SECTION 1
THE WORD LIST
--------------

-Create a list/array of words
-Same range as the numbers
-Enumerate or Index them to know their positions


Variables for this section:
word_list
'''

# the word list
word_list = ['Zion', 'Oligark', 'Tsunami']
print("\nThe word_list is: ", word_list)






'''
SECTION 2
THE RANDOM NUMBER GENERATOR 
+ THE LOOP
-----------------------------

-Depending on the random number, 
 print the word that associates to that number
-Repeat until all the words are printed

**** NOTE ******
-No repeated words are allowed
-There needs to be some kind of check



Variables for this section:
i <-- increment counter for the loop
rand_num <-- generates the random number

'''
i = 0
while (i < 3):
    # random number between 0-2
    rand_num = random.randint(0, 3)

    # check for duplicates
    # x <-- the counter for the check



    # printing the number and the counter
    print("\nin the loop \'rand_num\' is: ", rand_num)
    print("the \'i\' counter is: ", i)



    # increasing the counter by 1
    i = i +1








#ENTER TO EXIT
input("\n\n\t\tENTER to Exit"
      "\n\t\t##############")
