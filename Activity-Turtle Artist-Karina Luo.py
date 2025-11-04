# Turtle Artist
# Author: Karina Luo
# 28 October

import turtle
import random
# A one-of-a-kind drawing

wn = turtle.Screen()
wn.bgcolor("#A7ADC6")

t = turtle.Turtle()
t.color("pink")
t.speed(0)
LEAF_COLOURS = {
    "Pink": "#FFC2DD",
    "Green": "#A0CFA9",
    "Orange": "#F4D07B",
    "Blue": "#AAC6DA",
    "e": "#FAD6A5",
    "red": "#F88379",
    "salmon": "#FA8072",
    "lavender": "#B57EDC",
    "periwinkle": "#CCCCFF",
    "blue": "#89CFF0",
    "blue2": "#85B09A",
    "b": "#007BA7",
    "b2": "#8AB9F1",
    "b3": "#ADD8E6",
    "b4": "#CCCCFF",
    "b5": "#AFDBF5",
    "w": "#F5F5F5",
    "w2": "#E5E4E2",
    "wh": "#FFFDD0",
    "wh2": "#FFF8E7",
    "wh3": "#F0FFFF",
}
choices = [
    "Pink",
    "Green",
    "Orange",
    "Blue",
    "e",
    "red",
    "salmon",
    "lavender",
    "periwinkle",
    "blue",
    "blue2",
    "b",
    "b2",
    "b3",
    "b4",
    "b5",
    "w",
    "w2",
    "wh",
    "wh2",
    "wh3",
]


def draw_house():
    t.begin_fill()
    t.right(180)
    t.forward(95)
    t.right(135)
    t.forward(68)
    t.right(90)
    t.forward(65)
    t.end_fill()
    ##recursive???

    t.begin_fill()
    t.color(LEAF_COLOURS[random.choice(choices)])
    t.right(45)
    t.forward(100)
    for i in range(3):
        t.right(90)
        t.forward(96)
    t.end_fill()
    t.pu()


def draw_town(level: int):
    if level > 0:
        t.penup()
        t.goto(random.randint(-900, 900), random.randint(-900, 900))
        t.pendown()
        draw_house()
        draw_town(level - 1)


draw_house()
draw_town(100)
# Your code here

wn.exitonclick()
