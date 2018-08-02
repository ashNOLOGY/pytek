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
print("\n\t\t\t---------------"
      "\n\t\t\t| CODE_TESTER | "
      "\n\t\t\t---------------\n")

#---- Create a word list
word_list = ("zion", "oligarch", "tron")

#---- indexing the word list + printing them out
print("\nThe Indexed word_list \n")
#----- indexing the word_list
for index, x in enumerate(word_list):
    print("at index: ", index, " is: ", x)

print("\n +++++++++++++++")



#----- create a random number generator
rand_num = random.randint(0,2)
print("\nThe random index number: ", rand_num)

#---- printing the word associated with choosen number
print("The word in that index is: ", word_list[rand_num])
print("\n* * * * *\n")













# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")