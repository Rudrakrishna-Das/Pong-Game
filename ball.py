from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.x_val = 10
        self.y_val = 10

    
    def move(self):
        new_x = self.xcor() + self.x_val
        new_y = self.ycor() + self.y_val
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_val *= -1
