from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")

# Create turtle to draw dashed centerline
screen.tracer(0)
center_line = Turtle()
center_line.shape("arrow")
center_line.color("white")
center_line.penup()
center_line.goto(0, 300)
center_line.setheading(270)
center_line.width(2)

# Draw a dashed line
for _ in range(0, 29):
    center_line.forward(10)
    center_line.penup()
    center_line.forward(10)
    center_line.pendown()

center_line.hideturtle()
screen.update()


def paddle_up():
    new_y = r_paddle.ycor() + 20
    r_paddle.goto(r_paddle.xcor(), new_y)


def paddle_down():
    new_y = r_paddle.ycor() - 20
    r_paddle.goto(r_paddle.xcor(), new_y)


# Create right paddle
r_paddle = Turtle()
r_paddle.shape("square")
r_paddle.color("white")
r_paddle.shapesize(stretch_len=1, stretch_wid=5)
r_paddle.penup()
r_paddle.goto(350, 0)
screen.update()

screen.listen()
screen.onkey(paddle_up, "Up")
screen.onkey(paddle_down, "Down")

game_on = True
while game_on:
    screen.update()


screen.exitonclick()
