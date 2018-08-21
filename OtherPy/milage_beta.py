'''
-----------------------------|
Ash of [bini-tek]            |
learn \ make \ share         |
Blog: aobinitek.blogspot.com |
Thursday: May/4/2017         |
-----------------------------|

Milage BETA
Testing the idea
Program Name: Milage_BETA
//////////////////////////////////

'''
# No "imports" were needed


# Global Variable
intake = raw_input("Name of File: ")
total_milage = 0



# /////////////
# The Functions
# /////////////
def testTEXT():
    saveFile = open(intake+".txt", 'w')
    saveFile.write(str(intake))
    saveFile.write("\n \n")
    saveFile.close() # to close the text file
    moreText()
    
    
def moreText():
    #intake2 = 0    
    intake2 = int(raw_input("Enter Milage: "))
    saveFile = open(intake+".txt", 'a')
    saveFile.write(str(intake2))
    milage = intake2
    #total_milage = (intake2 + milage)
    saveFile.write("\n")
    #print("Total Milage is: "+str(total_milage))
    saveFile.close() # to close the text file
    moreMORE()

    
def moreMORE():
    answer = raw_input("\nMore info? y/n: ")
    if answer == "y":
       moreText()
    else:
        answer2 = raw_input("\nRead File? y/n: ")
        if answer2 == "y":
            readFile() # calling the read file
        else:
            raw_input("\nFile Closed. \nHit enter to exit.")
            
              

def readFile():
    readMe = open(intake+".txt", 'r')
    print("\n\n")
    print readMe.read()
    
    raw_input("\nHit enter to exit")
    readMe.close()
        
          

# /////////////////////////
# Calling the Main function
# /////////////////////////
testTEXT()

'''
////////////////
 The COMMENT Section
///////////////////


# Writing / Creating a txt file
text = "Hello there, can you see me?"
saveFile = open ("wa-test.txt", 'w')
saveFile.write(text) # <-- can this call a function?
saveFile.write("\n")


# Appending the same file
textTwo = "Second Line of text"
saveFile = open("wa-test.txt", 'a')
saveFile.write(textTwo) 
saveFile.write("\n")




'''
