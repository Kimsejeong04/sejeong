from turtle import *
from random import *

x, y, radius = 0, 0, 0
colorList = ['red', 'yellow', 'green', 'orange', 'blue', 'violet', 'tan', 'brown', 'navy', 'cyan']

setup(1200, 800)
bgcolor("black")
speed(0)

for i in range(30):
    x = randint(-500, 500)
    y = randint(-400, 300)
    radius = randint(80, 130)
    penup()
    goto(x, y)
    pendown()
    color(choice(colorList))
    begin_fill()
    circle(radius)
    end_fill()