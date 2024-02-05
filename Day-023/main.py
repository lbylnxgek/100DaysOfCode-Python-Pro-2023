import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move, "Up")

car_manager = CarManager()

game_on = True
loop_count = 0
while game_on:
    time.sleep(0.1)
    # print(f"DEBUG: loop_count:{loop_count}")
    # Create new car every 6th loop
    if loop_count % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()
    screen.update()

    loop_count += 1


screen.exitonclick()
