'''
NCC
Dictonary Demo

Project: PyTek
Code by: ashNOLOGY

This is only a test.

'''




#------ The Imports
import os



# intro
print("\n\t\t\t-------------------"
      "\n\t\t\t| Dictionary Demo | "
      "\n\t\t\t-------------------\n")


"""
This test to have create an empty dictionary
Have python read a text file + populate the dictionary
We would then be able to compare user input with the dictionary to find a word
"""

#-- Open + Read a text file
f = open("testfile.txt", "r")
#-- create an empty dictionary
d={}
#-- populate that dictionary from the file
for line in f:
      x = line.split(":") #-- splits at the colon
      a=x[0] #-- x[0] the KEY
      b=x[1] #-- x[1] the VALUE
      c=len(b)-1 #-- to subtract the \n at the end
      b=b[0:c] #-- the VALUE starts at 0 and ends with C calculation
      d[a]=b #-- combines KEY & new VALUE


#-- the English Word varialbe
eng_word = input("enter word: ")

#-- print dictionary using the eng_word variable
print(eng_word, d[eng_word])




#-- print text file
#print(rf)















"""
This is test with the hard coded information
It worked fine
#------ Create the dictionary
#-- Populate the dictionary
dd = {"a":"apple " "// " "ant",
      "b":"banana " "//" "bonanza",
      "c":"cake " "// " "chamelion"}


#--ask the user what they want
userInput = input("enter letter: ")
print(dd[userInput])
"""





# outro
input("\n\n\t\t\t-----------------"
      "\n\t\t\t| ENTER to Exit |"
      "\n\t\t\t-----------------")