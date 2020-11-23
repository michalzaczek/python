from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 260)
        self.color('white')
        self.refresh()

    def refresh(self, pointup=False):
        self.clear()
        if pointup == True:
            self.score += 1
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)