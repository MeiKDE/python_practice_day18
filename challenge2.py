from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
# Set the screen size to 800x600
screen.setup(width=800, height=600)


def draw_dashed_line():
    for _ in range(15):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()


screen.title("Dashed Line with Turtle")

# call the function to draw dashed line 50 times

# Run the dashed line drawing 50 times
draw_dashed_line()

screen.exitonclick()  # prevent the window from closing automatically
