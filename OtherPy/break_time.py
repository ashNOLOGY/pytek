#The Take A Break program

#Imports
import time
import webbrowser

#Variables
total_breaks = 3
break_count = 0

print("Program started on: "+time.ctime())
while(break_count < total_breaks):
      time.sleep(5)
      webbrowser.open("https://www.youtube.com/watch?v=4yqX-P6PKkk")
      break_count += 1
      
