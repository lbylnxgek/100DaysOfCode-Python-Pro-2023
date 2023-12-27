def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() and right_is_clear():
        turn_left()
        if front_is_clear():
            build_wall()
            turn_left()
        else:
            turn_around()
            move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
