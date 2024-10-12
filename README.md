# Turtle Graphics Challenges

This project contains a series of Python challenges using the `turtle` module for graphics. Each challenge explores a different aspect of turtle graphics, from drawing basic shapes to more advanced animations like spirographs and random walks.

## Table of Contents

1. [Square Drawing with Turtle](#1-square-drawing-with-turtle)
2. [Dashed Line Drawing](#2-dashed-line-drawing)
3. [Polygon Drawing with Random Colors](#3-polygon-drawing-with-random-colors)
4. [Random Walk with Random Colors](#4-random-walk-with-random-colors)
5. [Spirograph](#5-spirograph)

---

### 1. Square Drawing with Turtle

This challenge draws a square using the turtle graphics.

```python
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("#FFC0CB")

for i in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()

### 2. Dashed Line Drawing
In this challenge, the turtle draws a dashed line.
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.setup(width=800, height=600)

def draw_dashed_line():
    for _ in range(15):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()

screen.title("Dashed Line with Turtle")
draw_dashed_line()
screen.exitonclick()

### 3. Polygon Drawing with Random Colors
This challenge draws polygons with sides from 3 to 10, each with a random color.

from turtle import Turtle, Screen
import random

screen = Screen()
t = Turtle()

def angle(sides):
    return 360 / sides

def draw_shape(sides):
    colors = [
        "red", "blue", "green", "yellow", "purple", 
        "orange", "pink", "brown", "gray", "black"
    ]
    t.color(random.choice(colors))
    for i in range(sides):
        t.forward(100)
        t.right(angle(sides))

for i in range(3, 11):
    draw_shape(i)

screen.exitonclick()


### 4. Random Walk with Random Colors
This challenge has the turtle perform a random walk, changing direction and color randomly.

from turtle import Turtle, Screen
import random

screen = Screen()
liz = Turtle()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
liz.pensize(15)
liz.speed("fastest")

for _ in range(200):
    liz.color(random_color())
    liz.forward(30)
    liz.setheading(random.choice(directions))

screen.exitonclick()


### 5. Spirograph
In this challenge, the turtle draws a spirograph with random colors, adjusting the gap between circles.

from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

s.colormode(255)
t.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.setheading(t.heading() + size_of_gap)
        t.color(random_color())
        t.circle(100)

draw_spirograph(10)
s.exitonclick()
