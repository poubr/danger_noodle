# Danger Noodle

Danger Noodle is a basic snake game made with python's turtle module.

This version of the game lets you also keep a track of your high score
via data.txt file even if you close the game.
To reset the high score, when prompted for new game, open data.txt
file and change the score to zero.


# Functionality

main.py
Handles most of the functionality, creates the screen, sets up control input
and runs the game.


border.py
Creates a border around playable area.
Not strictly necessary for functionality, but makes it clearer to see
where the actual walls are (both to separate the scoreboard, and to
make up for some of the turtle's Screen inaccuracies.)


food.py
Spawns food in random position while making sure it doesn't spawn at snake's
current position.


noodle.py
Creates the snake, sets up movement controls, and responsible for extending
and moving the snake.


scoreboard.py
Keeps track of the current score and high score and writes it on the game screen.
Also handles saving high score into data.txt file.

data.txt
High score is saved to this file.



# How to run
You need to have python interpreter installed.
Download the folder and unzip, in terminal (Mac) or command prompt (Windows)
type "python main.py".
