# import colorgram
#
# colors = colorgram.extract('damien-hirst-bromobenzotrifluoride.jpg', 40)
# color_tuple = list(tuple((color.rgb.r, color.rgb.g, color.rgb.b)) for color in colors)
# print(color_tuple)
# print(len(color_tuple))

color_list=[(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
 (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150),
 (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84),
 (120, 41, 33), (170, 203, 205), (223, 178, 169), (162, 168, 75), (117, 122, 148), (185, 188, 206), (88, 141, 158)]

from turtle import Turtle, Screen
import random

Little_turtle= Turtle()
Little_turtle.shape("classic")
Little_turtle.color("black")
Little_turtle.speed(speed=0)
Little_turtle.pensize(20)
screen=Screen()
screen.colormode(255)
y_position_turtle=-200
Little_turtle.penup()

def dot_row():
    for i in range(10):
        rgb = random.choice(color_list)
        Little_turtle.dot(30, rgb)
        Little_turtle.forward(50)

for i in range(10):
    Little_turtle.goto(-200,y_position_turtle)
    dot_row()
    y_position_turtle += 50

screen.exitonclick()