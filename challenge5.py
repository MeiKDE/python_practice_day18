# Make Spirograph using Turtle Graphics
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
t.color(random_color())
t.circle(100)

print(f"printing heading: {t.heading()}")


# Set size of gap between circles as function of radius
def draw_spirograph(size_of_gap):
    """Making sure the gap between circles is proportional to the radius of the circle"""
    # Draw spirograph, Repeat the following steps 10 times
    for _ in range(int(360 / size_of_gap)):
        # set the heading
        t.setheading(t.heading() + size_of_gap)
        t.color(random_color())
        t.circle(100)


draw_spirograph(10)
s.exitonclick()
