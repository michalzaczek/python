import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
screen.onkeypress(player.move, 'Up')
car_manager = CarManager()
t = .1

game_is_on = True
while game_is_on:
    time.sleep(t)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    player_x = int(player.xcor())
    player_y = int(player.ycor())


    if player.ycor() > 280:
        scoreboard.update()
        player.goto_start()
        t *= .9

    for car in car_manager.cars:
        car_x = int(car.xcor())
        car_y = int(car.ycor())
        if player_x in range(car_x-25, car_x+25) and player_y in range(car_y-10, car_y+10):
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
