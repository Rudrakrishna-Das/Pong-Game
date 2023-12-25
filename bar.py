from turtle import Turtle

class Bar(Turtle):
    def __init__(self,x_val,y_val):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(x_val,y_val)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(),new_y)