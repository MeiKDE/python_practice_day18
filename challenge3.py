from turtle import Turtle
import random

t = Turtle()


def angle(sides):
    return 360 / sides


def draw_shape(sides):
    colors = [
        "red",
        "blue",
        "green",
        "yellow",
        "purple",
        "orange",
        "pink",
        "brown",
        "gray",
        "black",
    ]
    t.color(random.choice(colors))
    for i in range(sides):
        t.forward(100)
        t.right(angle(sides))


for i in range(3, 11):
    draw_shape(i)


screen.exitonclick()
