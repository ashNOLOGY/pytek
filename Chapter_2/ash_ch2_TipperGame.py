'''
NCC
Chapter 2
The Tipper Game

Project: PyTek
Code by: ashNOLOGY

'''

#Display the name of the game
print("\nWelcome to the Tipper "
      "\n---------------------\n")
#Ask the user for the Bill amount (convert to int)
bill = int(input("Ammount of the Bill: "))

#Calculate 15% tip : 0.15 x bill
tip15 = 0.15 * bill
print("15% tip is: $", tip15)

#Calculate 20% tip : 0.20 x bill
tip20 = 0.20 * bill
print("20% tip is: $", tip20)

#Display the total amount + 15% tip
bill15 = bill + tip15
print("\nAmmount plus 15% tip is: $", bill15)

#Display the total amount + 20% tip
bill20 = bill + tip20
print("Ammount plus 20% tip is: $", bill20)


#ENTER to EXIT
input("\nThanks for Tipping "
      "\npress ENTER to EXIT")
