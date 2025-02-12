from turtle import Turtle, Screen
from random import Random

jimmy = Turtle()
jimmy.shape("classic")
jimmy.color("black")
random = Random()
screen = Screen()
screen.colormode(255)


def square():
    for _ in range(4):
        jimmy.forward(100)
        jimmy.right(90)


def dashed_line():
    for _ in range(25):
        jimmy.forward(10)
        jimmy.penup()
        jimmy.forward(10)
        jimmy.pendown()


def shapes():
    jimmy.pensize(1)
    for sides in range(3, 11):
        red = random.randint(1, 255)
        green = random.randint(1, 255)
        blue = random.randint(1, 255)
        jimmy.pencolor(red, green, blue)
        for _ in range(sides):
            jimmy.forward(100)
            jimmy.right(360/sides)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def random_walk():
    jimmy.pensize(15)
    jimmy.speed(0)
    angles = [0, 90, 180, 270]
    for _ in range(200):
        jimmy.pencolor(random_color())
        jimmy.forward(30)
        angle = random.choice(angles)
        jimmy.setheading(angle)
        print(angle)


def spirograph():
    jimmy.speed(0)
    for angle in range(0, 361, 5):
        jimmy.pencolor(random_color())
        jimmy.circle(100)
        jimmy.setheading(angle)


spirograph()




















screen.exitonclick()