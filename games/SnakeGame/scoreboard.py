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
        else:
            with open('data.txt', 'r') as file:
                self.high_score = int(file.read())
            if self.score > self.high_score:
                self.high_score = self.score
                self.score = 0
                with open('data.txt', 'w') as file:
                    file.write(str(self.high_score))
        self.write(f'Score: {self.score}, Highscore: {self.high_score}', align=ALIGNMENT, font=FONT)
