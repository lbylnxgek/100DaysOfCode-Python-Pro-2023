from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to Roy G. Biv Speedway: Turtles, start your engines!")

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
            winning_turtle = turtle
            winning_turtle_color = turtle.pencolor()
            winning_turtle.home()
            winning_turtle.right(1350)
            winning_turtle.pencolor("black")
            if user_bet == winning_turtle_color:
                turtle.write(
                    f"The winning turtle is {winning_turtle_color}. Congratulations, you win!    ",
                    align="center",
                    font=("Arial", 8, "normal"),
                    move=True,
                )
            else:
                turtle.write(
                    f"The winning turtle is {winning_turtle_color}. Better luck next time.    ",
                    align="center",
                    font=("Arial", 8, "normal"),
                    move=True,
                )
            # Break out of for loop to avoid multiple winners
            race_on = False
            break

screen.exitonclick()
