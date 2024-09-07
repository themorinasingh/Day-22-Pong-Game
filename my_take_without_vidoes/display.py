from turtle import Turtle

class Display():
    def __init__(self):
        self.display = Turtle()
        self.display.hideturtle()
        self.display.color("black")

    def game_over(self,winner):
        self.display.write(arg = f"GAME OVER\n{winner} WINS", move=False, align="center", font=("Ariel",25, "normal"))
