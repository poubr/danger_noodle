from turtle import Turtle
import random

# feeding the danger noodle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food_position = None
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('VioletRed4')
        self.speed('fastest')
        self.goto(self.get_food_position())

    # spawns food, surprisingly
    def spawn_food(self, snaky_boi):
        self.food_position = self.get_food_position()

        # making sure the food doesn't spawn under the Snake:
        for body_part in snaky_boi.snaky_bits:
            if body_part.pos() == self.food_position:
                self.food_position = self.get_food_position()
        self.goto(self.food_position)

    # gets the actual coordinates for snaky snacks
    def get_food_position(self):
        # range by 20 makes sure the food is centered
        return (random.randrange(-280, 280, 20)), (random.randrange(-280, 280, 20))
