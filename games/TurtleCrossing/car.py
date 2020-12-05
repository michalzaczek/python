from turtle import Turtle

class Car(Turtle):

    def __init__(self, y, color):
        super().__init__('square')
        self.color(color)
        self.penup()
        self.shapesize(1, 2)
        self.setheading(180)
        self.goto(310, y)

    def move(self):
        self.forward(5)
        if self.xcor() < -300:
            del self