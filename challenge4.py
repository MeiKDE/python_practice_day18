from turtle import Turtle, Screen
import random

screen = Screen()
liz = Turtle()
screen.colormode(255)


### Random Walk ###
# random color generator
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]  # 0: North, 90: East, 180: South, 270: West
liz.pensize(15)
liz.speed("fastest")

for _ in range(200):
    liz.color(random_color())
    liz.forward(30)
    liz.setheading(random.choice(directions))

screen.exitonclick()
