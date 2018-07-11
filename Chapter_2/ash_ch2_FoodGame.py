'''
NCC
Chapter 2
The Food Game

Project: PyTek
Code by: ashNOLOGY

'''

#Display name of the game
print("\nWelcome to the Favorite Food game \n"
      "--------------------------------- \n")



#Ask the user for 1st Fav Food : ff_1
ff_1 = input("Enter your 1st Favorite Food: ")

#Ask the user for 2nd Fav Food : ff_2
ff_2 = input("Enter your 2nd Favorite Food: ")

#Dispaly NEW fav food : nf  [food 1 + food 2]
nf = ff_1 + ff_2
print("Your new Favorite Food is: ", nf)


#Enter to Exit
input("\nGame Over: press ENTER to exit")