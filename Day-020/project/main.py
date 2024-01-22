from turtle import Screen
from snake import Snake
import time

# Difficulty level: Smaller number = faster snake
SLEEP_TIME = 1.0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(SLEEP_TIME)

    snake.move()


screen.exitonclick()
