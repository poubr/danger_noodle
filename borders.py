# drawing borders within the screen (to make it clear where the border under the scoreboard is,
# and the rest of the borders are drawn for the * aesthetic *)

from turtle import Turtle


class Borders(Turtle):
    def __init__(self):
        super().__init__()
        self.color('VioletRed4')
        self.draw_divider()

    # borders must go in increments of twenty for the snake to crawl around them
    # instead of into them (n.b. snake size is 20 pixels)
    # borders won't be centered, I opted for this solution as it makes for better gameplay
    def draw_divider(self):
        self.penup()
        self.hideturtle()
        self.goto(-290, 290)
        self.pendown()
        self.forward(580)
        self.right(90)
        self.forward(580)
        self.right(90)
        self.forward(580)
        self.right(90)
        self.forward(580)
