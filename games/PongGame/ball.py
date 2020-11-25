from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pensize(20)
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x = -10
        self.y = -10

    def new_ball(self):
        self.x *= -1
        self.y *= random.choice([-1, 1])
        self.goto(0, 0)

    def move(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)
