import turtle


def draw_spiral():
    """Draw a colorful spiral using the turtle module."""

    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("black")

    # Create a turtle
    spiral = turtle.Turtle()
    spiral.speed(50)
    spiral.width(2)

    colors = ["red", "yellow", "blue", "green", "purple", "orange"]

    # Draw a spiral
    for i in range(500):
        spiral.pencolor(colors[i % len(colors)])
        spiral.forward(i * 2)
        spiral.left(499)

    # Hide the turtle and display the window
    spiral.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    draw_spiral()
