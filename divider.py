from turtle import Turtle

def divide():
    divide = Turtle()
    divide.hideturtle()
    divide.color("black")
    divide.teleport(0,-290)
    divide.setheading(90)
    divide.pensize(9)
    for i in range(0,580,20):
        divide.pendown()
        divide.forward(20)
        divide.penup()
        divide.forward(20)


