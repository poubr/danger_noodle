from turtle import Turtle

# creating our danger noodle boi

# constants for easy adjustments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
ONE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# creating the snaky boi
class Snake:
    def __init__(self):
        self.snaky_bits = []
        self.create_snake()
        self.head = self.snaky_bits[0]

    # adds the first three bits of snake based on starting points
    def create_snake(self):
        for coordinate in STARTING_POSITIONS:
            self.add_snake_bit(coordinate)

    # creating the actual snake bits
    def add_snake_bit(self, coordinate):
        bit = Turtle(shape='square')
        bit.color('thistle4')
        bit.penup()
        bit.goto(coordinate)
        self.snaky_bits.append(bit)

    # extends snaky boi when he successfully snacks on food
    def extend_snake(self):
        self.add_snake_bit(self.snaky_bits[-1].position())

    # moving snaky and defining control:
    def move(self):
        for bit in range(len(self.snaky_bits) - 1, 0, -1):
            new_x = self.snaky_bits[bit - 1].xcor()
            new_y = self.snaky_bits[bit - 1].ycor()
            self.snaky_bits[bit].goto(new_x, new_y)
        self.head.forward(ONE_STEP)

    # controls setup
    def up(self):
        if self.head.heading() != DOWN:  # to prevent snake from turning on itself
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # deletes (transfers) the danger noodle from the screen
    def remove_noodle(self):
        for bit in self.snaky_bits:
            bit.goto(-1000, -1000)
        self.snaky_bits.clear()

    # resets snaky boi if players be playing (new game)
    def reset(self):
        self.create_snake()
        self.head = self.snaky_bits[0]

