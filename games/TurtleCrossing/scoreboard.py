from turtle import Turtle

FONT = ("Courier", 24, "normal", "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f'level: {self.score}', font=FONT)

    def game_over(self):
        #self.clear()
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)