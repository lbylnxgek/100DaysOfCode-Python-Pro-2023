from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Difficulty level: Smaller number = faster snake
SLEEP_TIME = 0.2

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    # Detect collision with wall
    if (
        snake.head.xcor() > 295
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -295
    ):
        game_on = False
        scoreboard.game_over()


screen.exitonclick()
