from turtle import Screen
from bar import Bar
from ball import Ball

import time

# Screen setup
screen = Screen()
screen.setup(width=1200,height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

# User1 Paddle
user1_paddle = Bar(570,0)

screen.onkeypress(fun=user1_paddle.move_up,key='Up')
screen.onkeypress(fun=user1_paddle.move_down,key='Down')
# User2 Paddle
user2_paddle = Bar(-570,0)

screen.onkeypress(fun=user2_paddle.move_up,key='w')
screen.onkeypress(fun=user2_paddle.move_down,key='s')

# Ball added
ball = Ball()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


screen.exitonclick()