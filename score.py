from turtle import Turtle

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.user1_score = 0
        self.user2_score = 0        
        self.update_score()

    def update_score(self):
        self.clear()
        self.color('orange')
        self.goto(x=-200,y=200)       
        self.write(f"{self.user2_score}",align='center', font=('Arial', 50, 'normal'))
        
        self.color('yellow')
        self.goto(x=200,y=200)       
        self.write(f"{self.user1_score}",align='center', font=('Arial', 50, 'normal'))

    def user1_point(self):
        self.user1_score += 1
        self.update_score()

    def user2_point(self):
        self.user2_score += 1
        self.update_score()


        