from turtle import Turtle

class Text(Turtle):

    def __init__(self, text, x, y):
        super().__init__()
        #self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(text)
