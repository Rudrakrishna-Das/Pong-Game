from turtle import Screen
from bar import Bar
from ball import Ball
from score import Scorebord
from writing import Write

import time

# Screen setup
screen = Screen()
screen.setup(width=1200,height=600)
screen.bgcolor('black')
screen.colormode(255)
screen.tracer(0)
screen.listen()

# User1 Paddle(right)
user1_paddle = Bar(570,0)

screen.onkeypress(fun=user1_paddle.move_up,key='Up')
screen.onkeypress(fun=user1_paddle.move_down,key='Down')

# User2 Paddle(left)
user2_paddle = Bar(-570,0)

screen.onkeypress(fun=user2_paddle.move_up,key='w')
screen.onkeypress(fun=user2_paddle.move_down,key='s')

# Ball added
ball = Ball()

# Writting Added

write = Write()


def start():
    write.clear()
    score = Scorebord() 
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.movement_speed)
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(user1_paddle) < 50 and ball.xcor() > 540 and ball.xcor() < 570:
            ball.bounce_x()

        if ball.distance(user2_paddle) < 50 and ball.xcor() < -540 and ball.xcor() > -570:
            ball.bounce_x()
        
        if ball.xcor() > 590:
            score.user2_point()
            ball.reset_ball()

        if ball.xcor() < -590:
            score.user1_point()
            ball.reset_ball()


write.game_start()

screen.onkey(key='space',fun=start)
    


screen.exitonclick()