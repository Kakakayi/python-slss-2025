import turtle
import random

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("pink")

# TMNT - turtles
# create a turtle called whatever
kaka = turtle.Turtle()
kaka.color("hotpink")
kaka.turtlesize(1)
kaka.shape("turtle")


kaka.speed(0)
# move it around

# heart
# kaka.left(45)
# kaka.forward(25)
# kaka.right(45)
# kaka.forward(50)
# kaka.right(25)
# kaka.forward(25)
# kaka.right(45)
# kaka.forward(55)
# kaka.left(145)
# kaka.forward(55)
# kaka.right(55)
# kaka.forward(25)
# kaka.right(25)
# kaka.forward(50)
# kaka.right(20)
# kaka.forward(25)
# kaka.right(45)
# kaka.forward(25)
# kaka.right(15)
# kaka.forward(25)
# kaka.right(40)
# kaka.forward(200)
# kaka.right(109)
# kaka.forward(205)
# kaka.right(42)
# kaka.forward(45)

# # snowman (body)
# kaka.penup()
# kaka.goto(-100, 150)
# kaka.pendown()
# kaka.circle(100)

# # snowman (head)
# kaka.penup()
# kaka.goto(-140, 315)
# kaka.pendown()
# kaka.circle(60)

# # snowman (eye 1)
# kaka.penup()
# kaka.goto(-180, 320)
# kaka.color("black")
# kaka.pendown()
# kaka.begin_fill()
# kaka.circle(6)
# kaka.end_fill()

# # snowman (eye 2)
# kaka.penup()
# kaka.goto(-210, 320)
# kaka.begin_fill()
# kaka.pendown()
# kaka.circle(6)
# kaka.end_fill()

# # snowman (button 1, 2 3)
# kaka.penup()
# kaka.goto(-188, 200)
# kaka.begin_fill()
# kaka.pendown()
# kaka.circle(8.5)
# kaka.end_fill()
# kaka.penup()

# kaka.goto(-188, 150)
# kaka.begin_fill()
# kaka.pendown()
# kaka.circle(8.5)
# kaka.end_fill()
# kaka.penup()

# kaka.goto(-188, 100)
# kaka.begin_fill()
# kaka.pendown()
# kaka.circle(8.5)
# kaka.end_fill()

# # snowman (carrot nose)
# kaka.penup()
# kaka.goto(-205, 298)
# kaka.color("orange")
# kaka.begin_fill()
# kaka.pendown()
# kaka.right(110)
# kaka.forward(50)
# kaka.right(190)
# kaka.forward(50)
# kaka.left(90)
# kaka.forward(10)
# kaka.end_fill()

# Cookie Making


# Set the colour of our choco chip cookie
def make_cookies(x: int, y: int):
    kaka.color("brown")
    # Draw a circle to represent our cookie
    kaka.shapesize(0.3)
    kaka.shape("circle")
    kaka.pu()
    kaka.setheading(0)  # points east
    kaka.goto(-2 + x, -30 + y)
    kaka.pd()
    kaka.circle(30)
    # Put a chocolate chip at the top-right
    kaka.pu()
    kaka.goto(10 + x, 10 + y)
    kaka.stamp()
    # Put a chocolate chip at the bottom-right
    kaka.goto(10 + x, -10 + y)
    kaka.stamp()
    # Put a choco chip at the bottom-left
    kaka.goto(-10 + x, -10 + y)
    kaka.stamp()
    # Choco chip at the top-left
    kaka.goto(-10 + x, 10 + y)
    kaka.stamp()
    # Chocolate chip in the middle
    kaka.goto(0 + x, 0 + y)
    kaka.stamp()


for _ in range(500):
    x = random.randrange(-500, 500)
    y = random.randrange(-500, 500)
    kaka.speed(0)
    make_cookies(x, y)

make_cookies(0, 0)
make_cookies(100, 100)
make_cookies(-100, 100)
make_cookies(100, -100)
make_cookies(-100, -100)

window.exitonclick()
