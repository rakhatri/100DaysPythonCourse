# import colorgram
#
# colors = colorgram.extract("image.jpg", 1000)
#
# color_list = []
# for color in colors:
#     color_values = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colors_list.append(color_values)
#
# print(color_list)
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [(234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34), (131, 217, 230), (183, 17, 9), (12, 96, 52), (166, 182, 235), (242, 167, 153), (10, 85, 102), (252, 5, 48), (66, 94, 8), (248, 13, 10), (14, 48, 249)]
y_coordinate = 0
tim.speed("fastest")
tim.hideturtle()
tim.penup()
for y in range(10):
    for x in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    y_coordinate += 50
    tim.setposition(0, y_coordinate)

screen.exitonclick()
