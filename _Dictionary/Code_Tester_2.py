'''
NCC
CODE TESTER

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
print("\n\t\t\t---------------"
      "\n\t\t\t| CODE_TESTER | "
      "\n\t\t\t---------------\n")

#Defining the Clear function
def clear():
      #-- if OS is Windows
      if name == 'nt':
            _=system('clear')
      #-- if OS is Linux
      else:
            _=system('cls')

print('hello word \n' * 5)
sleep(3)
clear()

print("It has been cleared")



# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")