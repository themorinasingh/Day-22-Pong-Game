from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

#screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("gold")
screen.title("PONNG!")
screen.tracer(0)

#paddle setup
l_paddle = Paddle((-360,0))
r_paddle = Paddle((350, 0))

#ball setup
ball = Ball()
#adding controls to move paddle up and down

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

#game on/off functionality
game_is_on = True

#keeping score
scoreboard = Score()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collision wth walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detecting collision with paddle
    if ball.distance(r_paddle) < 54 and ball.xcor() > 320:
        ball.bounce_x()


    if ball.distance(l_paddle) < 54 and ball.xcor() < -320:
        ball.bounce_x()

    #ball out of bounds situation, we need to check if the ball goes behind the paddle
    if ball.xcor() > 380 :
        time.sleep(.05)
        ball.reset_position()
        scoreboard.l_score_update()
        speed = .1

    if ball.xcor() < -380:
        time.sleep(.05)
        ball.reset_position()
        scoreboard.r_score_update()
        speed = .1



screen.exitonclick()