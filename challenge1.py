from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()
# Function as input for onkey function
# Use keyword argument instead of positional argument
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
