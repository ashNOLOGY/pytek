'''
NCC
CHAPTER 4
The Counter

Project: PyTek
Code by: ashNOLOGY

'''




#------ The Imports
import math
import random
import os


# intro
print("\n\t\t\t---------------"
      "\n\t\t\t| The Counter  | "
      "\n\t\t\t---------------\n")

# Ask the user for a Starting number
start_num = int(input("Please enter START number: "))

# Ask the user for an Ending number
end_num = int(input("Please enter END number: "))

# Ask the user for the Increment
step_num = int(input("Please enter STEP number: "))


print("\nYour START is:", start_num,
      "\nYour END is:", end_num,
      "\nYour STEP is: ", step_num)

#result = [start_num : end_num : step_num]
#print("\nYour results are: ", result )
result = list(range(start_num,end_num,step_num))
print("\nYour results are:", result)


# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")