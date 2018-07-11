'''
NCC
Chapter 2
The Car Salesman Game

Project: PyTek
Code by: ashNOLOGY

'''

#Display the name of the game
print("\nThe Car Salesman Game"
      "\n---------------------\n ")

#Ask user for the ammount they want to pay for a car (convert to int)
car_price = int(input("Enter the price of the car you want: $"))

#Calculate the Tax 10% of the ammount
tax = 0.10 * car_price
print("Tax: $", tax)

#Calculate the License Fee 5% of the ammount
l_fee = 0.05 * car_price
print("License Fee: $", l_fee)

#Add Dealer Prep fee $500
dp_fee = 500
print("Dealer Prep Fee: $", dp_fee)

#Add Desination Charge fee $200
dc_fee = 200
print("Destination Charge Fee: $", dc_fee)

#Display the new price will all the added fees
new_car_price = car_price + tax + l_fee + dp_fee + dc_fee
print("Your grand total is: $", new_car_price)


#ENTER to Exit
input("\nEnjoy your new Ride."
      "\npress ENTER to EXIT")