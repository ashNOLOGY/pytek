'''
CODE TESTER
Chapter 6

Project: PyTek
Code by: ashNOLOGY

'''




#------ The Imports
import math
import random
from os import system , name
from subprocess import call
from time import sleep


# intro
print("\n\t\t\t-----------------------"
      "\n\t\t\t| CH6 Counter [v2.0] | "
      "\n\t\t\t-----------------------\n")

#-- DEFINING THE ask_num FUNCTION
def ask_num():
    print("The ask_num() Function goes Here")




#-- The main While Loop
while_answer = input("Start? y/n: ")
if_answer = ""
while (while_answer == 'y'):
    #-- The IF Statement
    if_answer = input("\nRun the ask_num()? y/n: ")
    if (if_answer == 'y'):
        ask_num()
    else:
        print("you pressed No")

    while_answer = input("\nWould you like another?"
                   "\ny/n : ")




# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")