from turtle import Screen
from noodle import Noodle
from food import Food
from borders import Borders
from scoreboard import Scoreboard
import time


# game itself:
def danger_noodle_game():

    # creating screen so we can see our danger noodle
    screen = Screen()
    screen.setup(width=620, height=630)
    screen.bgcolor('MistyRose')
    screen.title('Danger Noodle')
    screen.tracer(0)

    # creating snake, food, score, and border objects
    danger_noodle = Noodle()
    danger_snacks = Food()
    score = Scoreboard()
    borders = Borders()

    game_on = True
    while game_on:
        # creating controls
        # N.B., must be inside while loop for them work if player wants to
        # start a new game without restarting the program
        screen.listen()
        screen.onkey(danger_noodle.up, "Up")
        screen.onkey(danger_noodle.down, "Down")
        screen.onkey(danger_noodle.left, "Left")
        screen.onkey(danger_noodle.right, "Right")
        screen.update()
        time.sleep(0.1)

        danger_noodle.move()

        # has snake snacked:
        if danger_noodle.head.distance(danger_snacks) < 15:
            danger_snacks.spawn_food(danger_noodle)
            score.current_score += 1
            score.update_score()
            danger_noodle.extend_snake()

        # has snake hit wall and died:
        if danger_noodle.head.xcor() > 290 or danger_noodle.head.xcor() < -290 or danger_noodle.head.ycor() > 290 or danger_noodle.head.ycor() < -290:
            game_on = False
            score.game_over()
            danger_noodle.remove_noodle()

        # has snake hit itself and died:
        for noodle in danger_noodle.snaky_bits[1:]:
            if danger_noodle.head.distance(noodle) < 10:
                game_on = False
                score.game_over()
                danger_noodle.remove_noodle()

        # asking player if they want to play a new game (without restarting the program)
        if not game_on:
            new_game = screen.textinput("GAME OVER", "New game? Y/N:").lower()
            if new_game == 'y':
                game_on = True
                danger_noodle.reset()
                score.reset()
            else:
                screen.bye()


if __name__ == "__main__":
    danger_noodle_game()

