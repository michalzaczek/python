from turtle import Screen, Turtle
from platform import Platform
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH, HEIGHT = 800, 600

def draw_line():
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.color('white')

    t.goto(0, -HEIGHT/2)
    t.setheading(90)
    while t.ycor() < HEIGHT/2:
        t.forward(20)
        t.pendown()
        t.forward(10)
        t.penup()

screen = Screen()
screen.title('Pong Game')
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.tracer(0)


player1 = Platform(-WIDTH/2+50)
player2 = Platform(WIDTH/2-50)

screen.listen()
screen.onkeypress(player1.up, 'w')
screen.onkeypress(player1.down, 's')
screen.onkeypress(player2.up, 'Up')
screen.onkeypress(player2.down, 'Down')

draw_line()
ball = Ball()
scoreboard = Scoreboard()
t = .05

game_on = True
while game_on:
    time.sleep(t)
    screen.update()
    ball.move()

    #detect collision with horizontal bands
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y *= -1

    #detec collision with player platform
    if (ball.xcor() == -330 and ball.distance(player1) <= 60) or (ball.xcor() == 330 and ball.distance(player2) <= 60):
        ball.x *= -1
        t *= .9

    #detect collision with vertical bands
    if ball.xcor() > 380:
        scoreboard.p1_score += 1
        scoreboard.update()
        ball.new_ball()
        t = .05
    if ball.xcor() < -380:
        scoreboard.p2_score += 1
        scoreboard.update()
        ball.new_ball()
        t = .05



screen.exitonclick()