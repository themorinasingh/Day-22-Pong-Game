from turtle import Screen, Turtle
from boards import Board
import time
from ball import Ball
from display import Display
from divider import divide
from obstackle import Obstackle

screen = Screen()
screen.bgcolor("gold")
screen.setup(width=600,height=600)
screen.tracer(0)
divide()

#creating boards
board_1 = Board([(280,20), (280,0), (280, -20)])
board_2 = Board([(-280,20), (-280,0), (-280, -20)])
#creating ball
ball = Ball()
#creating a sequence for message at the end
message = Display()
#creating obstacle
obstacle_1 = Obstackle([(-30, 240),(-60, 240),(-30, 260),(-60, 260),(-30, 280),(-60, 280), (-45, 240),(-45, 280)])
obstacle_2 = Obstackle([(30, 280), (30, 260), (30,240)])

screen.listen()
#making board 1 move up and down
screen.onkey(fun=board_1.move_up, key='Up')
screen.onkey(fun=board_1.move_down, key='Down')
#making board 2 move up and down
screen.onkey(fun=board_2.move_up, key='w')
screen.onkey(fun=board_2.move_down, key='s')


game_is_on = True

while game_is_on:
    time.sleep(.08)
    screen.update()
    ball.move()

    for board in board_1.my_board:
        if board.distance(ball.ball) < 15 :
            ball.deflect()

    for board in board_2.my_board:
        if board.distance(ball.ball) < 15 :
            ball.deflect()

    for obstacle in obstacle_1.obstacle:
        if obstacle.distance(ball.ball) < 15 :
            ball.deflect()

    for obstacle in obstacle_2.obstacle:
        if obstacle.distance(ball.ball) < 15 :
            ball.deflect()

    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.deflect()

    if ball.ball.xcor() > 300 or ball.ball.xcor() < -300:
        game_is_on = False
        if ball.ball.xcor() > 300:
            message.game_over("LEFT")
        elif ball.ball.xcor() < -300:
            message.game_over("RIGHT")








screen.exitonclick()