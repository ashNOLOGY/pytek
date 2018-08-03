'''
NCC
CHAPTER 4
Random World List

Project: PyTek
Code by: ashNOLOGY

'''




#------ The Imports
import math
import random
import os


# intro
print("\n\t\t\t--------------------"
      "\n\t\t\t| Random Word List | "
      "\n\t\t\t--------------------\n")

#---- Create a word list
word_list = ("zion", "oligarch", "tron")

#---- indexing the word list + printing them out
print("\nThe Indexed word_list \n")
#----- indexing the word_list
for index, x in enumerate(word_list):
    print("At index: ", index, " is: ", x)

print("\n +++++++++++++++\n")

#--- l: increment that is as long as the objects in the list
l = len(word_list)

#--- i: increment is for the while loop
i = 0

#--- picked_nums: the empty list
picked_nums = []

#--- the while loop
while (i < l):

    #----- create a random number generator
    rand_num = random.randint(0,2)
    #-- Check to see if the number is in picked_nums
    if rand_num not in picked_nums:
        # --IF NOT: Add the rand_num to the picked_num list
        picked_nums.append(rand_num)
        print("Randomly Picked Numbers are: ", picked_nums)
        # ---- printing the word associated with choosen number
        print("The word in that index is: ", word_list[rand_num])
        print("\n* * * * *\n")
    else:
        continue

    #-- incrementing the while loop
    i += 1


# outro
input("\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")