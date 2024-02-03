from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


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

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall & bounce
    if ball.collide_with_wall():
        ball.bounce_y()

    # Detect collision with right paddle & change direction
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with left paddle & bounce
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()
