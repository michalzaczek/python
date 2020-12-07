import pandas as pd
from turtle import Screen
from text import Text
from score import Score

df = pd.read_csv('50_states.csv')
states = df.state.values.tolist()

screen = Screen()
screen.setup(730, 496)
screen.bgpic('blank_states_img.gif')
screen.tracer(0)

score = Score()

while states:
    answer = screen.textinput('Question', 'Type the name of state you know:').title()

    if answer in states:
        state, x, y = df[df.state == answer].values[0]
        Text(state, x, y)
        states.remove(answer)
        score.points += 1
    score.hits += 1
    score.refresh()

    screen.update()

screen.exitonclick()

