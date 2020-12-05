from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__('turtle')
        self.setheading(90)
        self.penup()
        self.goto_start()

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(20)