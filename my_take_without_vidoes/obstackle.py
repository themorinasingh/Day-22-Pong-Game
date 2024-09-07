from turtle import Turtle

class Obstackle():
    def __init__(self, positions):
        self.obstacle = []
        self.positions = positions
        self.draw_obstacle()

    def draw_obstacle(self):
        for position in self.positions:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("black")
            new_segment.goto(position)
            self.obstacle.append(new_segment)