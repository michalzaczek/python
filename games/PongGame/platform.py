from turtle import Turtle

class Platform(Turtle):

    def __init__(self, x):
        super().__init__('square')
        self.speed(0)
        self.setheading(90)
        self.penup()
        self.color('white')
        self.shapesize(1, 5)
        self.goto(x, 0)

    def up(self):
        if self.ycor() < 230:
            self.setheading(90)
            self.forward(20)

    def down(self):
        if self.ycor() > -230:
            self.setheading(270)
            self.forward(20)