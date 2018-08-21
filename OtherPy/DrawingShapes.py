# Python 2.7.13
# Code by: Ash Dawod [AshDev]

# Drawing Shapes
# TURTLE is the module to help draw things

import turtle

# Creating the background window/color
window = turtle.Screen()
window.bgcolor("green")

# Defining the SQUARE function
def draw_square():
    

    # Grabbing and customizing the Square
    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("yellow")
    brad.speed(2)

    # Square While Loop
    square_counter = 0
    while (square_counter < 4):
         brad.forward(100)
         brad.right(90)
         square_counter = square_counter + 1

    

# Defining the CIRCLE function
def draw_circle():
    # Creating a circle
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("black")
    angie.speed(10)
    angie.circle(100)
    

# Defining the TRIANGLE function
def draw_triangle():
    # Grab and customizing Triangle
    paul = turtle.Turtle()
    paul.shape("triangle")
    paul.color("white")
    

    # Triangle Loop
    tri_counter = 0
    while (tri_counter < 3):
        paul.forward(100)
        paul.left(120)
        tri_counter += 1
        
    
    
# Calling Functions
draw_square() # SQUARE
draw_circle() # CRICLE
draw_triangle() # TRIANGLE



# To be able to close the window
window.exitonclick()

'''
////////////////////////
/// COMMENTS AREA  ///
///////////////////////

# Creating a circle
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("black")
    angie.speed(10)
    angie.circle(100)

 # Moving the Turtle
    brad.forward(100) # One
    # To turn him right 90 degrees
    brad.right(90)
    brad.forward(100) # Two
    brad.right(90)
    brad.forward(100) # Three
    brad.right(90)
    brad.forward(100) # Four
    brad.right(90)
    
 

    
'''



    



