from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('yellow')
        self.shape('square')
        self.pensize(20)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)