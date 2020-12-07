from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-360, 220)
        self.points = 0
        self.hits = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'{self.points}/51 out of {self.hits} hits', align="left", font=("Arial", 18, "normal"))
