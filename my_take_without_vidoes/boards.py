from turtle import Turtle

class Board(Turtle):
    def __init__(self, positions):
        self.my_board = []
        self.positions = positions
        self.board_create()
        self.head = self.my_board[0]
        self.tail = self.my_board[-1]

    def board_create(self):
        for position in self.positions:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("black")
            new_segment.penup()
            new_segment.goto(position)
            self.my_board.append(new_segment)

    def move_up(self):

        for i in range(len(self.my_board) - 1, 0, -1):
            new_x = self.my_board[i-1].xcor()
            new_y = self.my_board[i - 1].ycor()
            self.my_board[i].goto(new_x, new_y)

        self.head.setheading(90)
        self.head.forward(20)


    def move_down(self):
        for i in range(len(self.my_board) - 1):
            new_x = self.my_board[i+1].xcor()
            new_y = self.my_board[i + 1].ycor()
            self.my_board[i].goto(new_x, new_y)

        self.tail.setheading(270)
        self.tail.forward(20)






