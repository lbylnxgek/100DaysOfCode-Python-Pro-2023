from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtles, start your engines!")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []
race_on = False

user_bet = screen.textinput(
    title="Place your bet!",
    prompt="Which turtle will win the race? Enter a color:\n (red, orange, yellow, green, blue, indigo, violet)",
)

# Set initial coordinates for turtles
x_coord = -240
y_coord = -150

for turtle_index in range(0, len(colors)):
    # print(f"coord: {x_coord}, {y_coord}")
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x_coord, y=y_coord)
    all_turtles.append(new_turtle)
    y_coord += 50

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 225:
            winning_turtle = turtle.pencolor()
            race_on = False
            if user_bet == winning_turtle:
                print(
                    f"The winning turtle is {winning_turtle}. Congratulations, you win!"
                )
            else:
                print(f"The winning turtle is {winning_turtle}. Better luck next time.")


screen.exitonclick()
