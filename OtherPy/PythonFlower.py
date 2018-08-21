# Python 2.7.13
# Code by: Ash Dawod [AshDev]

# Python Flower
# TURTLE is the module to help draw things
import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    # BRAD to draw SQUARE
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(15)
    # The LOOP to create the flower
    for i in range(1,37):
        draw_square(brad) # draw circle
        brad.right(10) #rotate 10 degrees

       
    window.exitonclick()



draw_art()

