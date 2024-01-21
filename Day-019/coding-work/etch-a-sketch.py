from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()


def move_backward():
    timmy.backward(10)


def clear_screen():
    timmy.reset()


def move_forward():
    timmy.forward(10)


def turn_left():
    timmy.left(10)


def turn_right():
    timmy.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
