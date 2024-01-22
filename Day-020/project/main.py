from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
all_segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    all_segments.append(new_segment)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.5)
    for seg_num in range(len(all_segments) - 1, 0, -1):
        all_segments[seg_num].goto(all_segments[seg_num - 1].pos())
    all_segments[0].forward(20)


screen.exitonclick()
