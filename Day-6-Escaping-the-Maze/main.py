# Day 6 Final Project: Escaping the Maze
# Built and tested using Reeborg's World
# https://reeborg.ca/
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()

    elif front_is_clear():
        move()

    else:
        turn_left()

