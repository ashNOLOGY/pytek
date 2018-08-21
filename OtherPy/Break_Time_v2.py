'''
-----------------------------|
Ash of [bini-tek]            |
learn \ make \ share         |
Blog: aobinitek.blogspot.com |
Monday : May.1.2017          |
Python 2.7.13                |
-----------------------------|
'''

#Break Time

#Imports
import time
import webbrowser

#Variables
print("Welcome to the BREAK TIME program")

#The BreakTime function
def BreakTime():
      total_breaks = int(raw_input("\nHow many breaks would you like today?: "))
      hours = int(raw_input("How many hours a part?: "))
      favorite_site = raw_input("Enter the website to go to: ")
      
            
      #Confirmation Message
      print("\nThis is the plan: \n"+str(total_breaks)+" break(s)")
      print(str(hours)+" hour(s) apart")
      print("which will take you to "+favorite_site)
      answer = raw_input("Is this correct? y/n: ")
      if answer == "y":
            break_count = 0
            #Executing The Break
            while(break_count < total_breaks):
                  time.sleep(hours*60)
                  webbrowser.open(favorite_site)
                  break_count += 1
      else:
            ResetTime()
            

#The Reset Time Function
def ResetTime():
      BreakTime()
      
#Call a ResetTime function, which would call the BreakTime
ResetTime()

