from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Sssnake_Game')
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.update()
time.sleep(1)


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    snake.move()
    time.sleep(.2)

    if snake.head.distance(food) < 10:
        food.refresh()
        scoreboard.refresh(True)
        snake.expand()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.refresh()

    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            snake.reset()
            scoreboard.refresh()

