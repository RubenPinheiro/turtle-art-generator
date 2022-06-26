from turtle import Turtle, Screen
from random import random, choice

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.speed(0)
turns = [1, 2, 3, 4]
sides = 3


def change_color():
    r = random()
    g = random()
    b = random()

    return timmy.pencolor(r, g, b)


"""Geometry NFT"""
# while sides < 11:
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(360 / sides)
#
#     change_color()
#     sides += 1

"""Random Walk NFT"""
# for i in range(300):
#     n_turns = choice(turns)
#     change_color()
#     for _ in range(n_turns):
#         timmy.right(90)
#     timmy.forward(25)
#     timmy.pensize(15)

"""Spirograph NFT"""
for i in range(120):
    timmy.circle(100)
    timmy.right(3)
    change_color()


























screen = Screen()
screen.exitonclick()
