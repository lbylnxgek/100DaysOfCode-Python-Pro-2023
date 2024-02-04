from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.draw_centerline()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_delay)
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

    # Detect when ball misses right paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
        scoreboard.update_score()

    # Detect when ball misses left paddle
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        scoreboard.update_score()


screen.exitonclick()
