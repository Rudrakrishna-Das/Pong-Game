from turtle import Turtle

class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.color('lightgreen')
        self.penup()
        self.hideturtle()

    def game_start(self):
        self.color((144,238,144))
        self.write('Space to start',align='center', font=('Arial', 50, 'normal'))