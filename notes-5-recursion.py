import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")

k = turtle.Turtle()
k.left(90)
k.penup()
k.goto(0, -200)
k.color("brown")
k.width(10)

k.shape("arrow")  # leaf shapek
k.pendown()
k.left(90)


def drawAtree(level: int, branchLength: float):
    k.speed(0)
    """Draws a tree recursively at a given level
    level- the levels of branches
    branch_length - length of branch in pixels
    """
    k.pendown()
    # if the level if greater than 0:
    if level > 0:
        # 1. move forward branch length
        k.forward(branchLength)
        # 2. Turn left and draw a "smaller tree"
        k.left(47)
        drawAtree(level - 1, branchLength * 0.8)
        # 3. Turn right and draw a "smaller tree"
        k.right(94)
        drawAtree(level - 1, branchLength * 0.8)
        # 4. Return to the Beginning
        k.left(47)
        k.backward(branchLength)
    else:
        # create a leaf
        k.color("green")
        k.stamp()
        k.color("brown")


def draw_complicated_tree(level: int, branch_length: float):
    k.pendown()
    # if the level if greater than 0:
    if level > 0:
        # 1. move forward branch length
        k.forward(branch_length)
        # 2. Turn left and draw a "smaller tree"
        k.left(35)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 3. Turn right and draw a "smaller tree"
        k.right(35)
        draw_complicated_tree(level - 1, branch_length * 0.8)

        k.right(35)
        draw_complicated_tree(level - 1, branch_length * 0.8)

        # 4. Return to the Beginning
        k.left(35)
        k.backward(branch_length)

    else:
        # create a leaf
        k.color("green")
        k.stamp()
        k.color("brown")


def factorial(num: int) -> int:
    """Calculate the factorial of the given num recursively"""
    pass


draw_complicated_tree(6, 225)


wn.exitonclick()
