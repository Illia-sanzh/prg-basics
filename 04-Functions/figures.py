import turtle
def draw_square(length):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()

def draw_square_twice(length):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()

    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()
def draw_triangle(length):
        # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(3):
        pen.forward(length)
        pen.left(120)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()
def draw_triangle_twice(length):
        # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()

    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()
def draw_rectangle(length, width):
        # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(2):
        pen.forward(length)
        pen.right(90)
        pen.forward(width)
        pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()
def draw_rectangle_twice(length, width):
        # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a square
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)

    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()

    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()