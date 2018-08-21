'''
Lesson 7
Inheritence

Remember:
Class Parent
 Class Child

'''


# Defining the PARENT
class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color
# A method with in the PARENT class
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        

# Defining the CHILD class
# It will inherit all the class variables of the PARENT class
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("\nChild Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of toys - "+str(self.number_of_toys))
       

billy_cyrus = Parent("Cyrus", "Blue")
#billy_cyrus.show_info() # calling that PARENT method
miley_cyrus = Child("Cyrus", "Blue", 5) #<- the instance
miley_cyrus.show_info() # <- the methon


    
