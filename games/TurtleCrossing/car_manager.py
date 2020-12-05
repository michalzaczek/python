from turtle import Turtle
import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.create_cars()


    def create_cars(self):
        self.cars.append(Car(random.randrange(-240, 260, 1), random.choice(COLORS)))

    def move_cars(self):
        for car in self.cars:
            car.move()