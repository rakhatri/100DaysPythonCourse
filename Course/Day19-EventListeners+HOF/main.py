import turtle
from turtle import Turtle, Screen
import random

my_screen = Screen()
#
# def move_forwards():
#     jim.forward(10)
#
#
# def move_backwards():
#     jim.backward(10)
#
#
# def move_counter_clockwise():
#     jim.left(5)
#
#
# def move_clockwise():
#     jim.right(5)
#
#
# def clear_screen():
#     jim.reset()
#
#
# my_screen.listen()
# my_screen.onkey(key="w", fun=move_forwards)
# my_screen.onkey(key="s", fun=move_backwards)
# my_screen.onkey(key="a", fun=move_counter_clockwise)
# my_screen.onkey(key="d", fun=move_clockwise)
# my_screen.onkey(key="c", fun=clear_screen)

is_race_on = False
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -125
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-225, y=y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

print(all_turtles)
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


my_screen.exitonclick()
