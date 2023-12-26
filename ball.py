from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.x_val = 10
        self.y_val = 10
        self.movement_speed = 0.1

    def color_create(self):
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        return(r,g,b)
    
    def move(self):
        new_x = self.xcor() + self.x_val
        new_y = self.ycor() + self.y_val
        self.goto(new_x,new_y)
        self.color(self.color_create())

    def bounce_y(self):
        self.y_val *= -1

    def bounce_x(self):
        self.x_val *= -1
        self.increase_speed()

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
        self.movement_speed = 0.1

    def increase_speed(self):
        self.movement_speed *= 0.9
