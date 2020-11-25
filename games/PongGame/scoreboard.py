from turtle import Turtle

FONT = ('Courier New', 70, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align='center', font=FONT)
        self.goto(100, 200)
        self.write(self.p2_score, align='center', font=FONT)