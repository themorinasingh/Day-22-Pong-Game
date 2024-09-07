from turtle import Turtle
import random

class Ball():
    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.penup()

    def move(self):
        self.ball.forward(20)

    def deflect(self):
        heading = self.ball.heading()

        new_angle = random.randint(80, 100)
        new_heading = heading + new_angle


        self.ball.setheading(new_heading)





