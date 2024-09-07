from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("purple")
        self.score_displayer()

    def score_displayer(self):
        self.goto((-40, 240))
        self.write(arg=self.l_score, move=False,align="center" ,font=("ariel",50, "normal"))
        self.goto((40, 240))
        self.write(arg=self.r_score, move=False, align="center", font=("ariel", 50, "normal"))

    def l_score_update(self):
        self.clear()
        self.l_score += 1
        self.score_displayer()

    def r_score_update(self):
        self.clear()
        self.r_score += 1
        self.score_displayer()

