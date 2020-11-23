from turtle import Screen, Turtle

MOVE_DISTANCE = 20
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270
POSITIONS = [(40, 0), (20, 0), (0, 0)]

class Snake():

    def __init__(self):

        self.squares = []
        for i in range(3):
            self.add_square(POSITIONS[i])
        self.head = self.squares[0]

    def add_square(self, position):
        square = Turtle('square')
        square.speed(0)
        square.penup()
        square.color('white')
        square.pensize(20)
        square.goto(position)
        self.squares.append(square)

    def expand(self):
        self.add_square(self.squares[-1].position())


    def move(self):

        for n in range(len(self.squares)-1, 0, -1):
            new_x = self.squares[n-1].xcor()
            new_y = self.squares[n-1].ycor()
            self.squares[n].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)