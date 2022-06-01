from turtle import Turtle


# keeps track of all the scores

ALIGNMENT = 'left'
FONT = ('Helvetica', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('VioletRed4')
        self.hideturtle()
        self.penup()
        self.setposition(-200, 290)
        self.current_score = 0
        # using a file for high score to preserve it for posterity (i.e. if player closes the program)
        with open('data.txt') as file:
            data = file.read()
            self.high_score = int(data)
        self.update_score()

    # updates score if snake has snacked
    def update_score(self):
        self.clear()
        if self.high_score == 0:
            self.write(arg=f"SCORE: {self.current_score}",
                       move=False, align=ALIGNMENT, font=FONT)
        else:
            self.write(arg=f"SCORE: {self.current_score}    HIGH SCORE: {self.high_score}",
                       move=False, align=ALIGNMENT, font=FONT)

    # shows game over message and check the high score
    def game_over(self):
        self.clear()
        self.setposition(-200, 290)
        if self.current_score > self.high_score:
            self.update_high_score()
            self.write(arg=f"NEW HIGH SCORE! {self.current_score}    GAME OVER",
                       move=False, align=ALIGNMENT, font=FONT)

        else:
            self.write(arg=f"SCORE: {self.current_score}    GAME OVER",
                       move=False, align=ALIGNMENT, font=FONT)

    # saves high score into file
    def update_high_score(self):
        with open('data.txt', 'w') as file:
            file.write(str(self.current_score))
            self.high_score = self.current_score

    # resets if player wishes to continue to party with the noodle
    def reset(self):
        if self.current_score > self.high_score:
            self.update_high_score()
        self.current_score = 0
        self.update_score()



