# Case - study #1
# Developers : Moiseenko V. (%),
#              Torgasheva A. (%),
#              Setskov M. (%).

import turtle
import math

# Figures:
def down_triangle (x, y, a, color):
    # TODO: (Alena) Paint a triangle.
       turtle.up()
       turtle.setposition(x, y)
       turtle.down()
       turtle.color(color)
       turtle.begin_fill()
       turtle.forward(a*math.sqrt(2))
       turtle.right(135)
       turtle.forward(a)
       turtle.right(90)
       turtle.forward(a)
       turtle.right(135)
       turtle.end_fill()

def right_triangle (x, y, a, color):
    #TODO: (Alena) Paint a triangle.
       turtle.up()
       turtle.setposition(x, y)
       turtle.down()
       turtle.color(color)
       turtle.begin_fill()
       turtle.right(45)
       turtle.forward(a)
       turtle.right(90)
       turtle.forward(a)
       turtle.right(135)
       turtle.forward(a*math.sqrt(2))
       turtle.right(90)
       turtle.end_fill()

def rhomb (x, y, z, color):
    # TODO: (Alena) Paint a rhomb.
       turtle.up()
       turtle.setposition(x, y)
       turtle.down()
       turtle.color(color)
       turtle.begin_fill()
       turtle.right(45)
       turtle.forward(z)
       turtle.right(90)
       turtle.forward(z)
       turtle.right(90)
       turtle.forward(z)
       turtle.right(90)
       turtle.forward(z)
       turtle.right(45)
       turtle.end_fill()

def mid_triangle(x, y, z, a, color):
       turtle.up()
       turtle.setposition(x, y)
       turtle.down()
       turtle.right(z)
       turtle.color(color)
       turtle.begin_fill()
       turtle.forward(a*math.sqrt(2))
       turtle.left(135)
       turtle.forward(a)
       turtle.left(90)
       turtle.forward(a)
       turtle.left(135)
       turtle.end_fill()
       turtle.left(z)
    # TODO: (Victoria) Paint a triangle.

def left_triangle(x, y, a, color):
    #TODO: (Victoria) Paint a purple triangle.
       turtle.up()
       turtle.setposition(x,y)
       turtle.down()
       turtle.color(color)
       turtle.begin_fill()
       turtle.right(90)
       turtle.forward(a*math.sqrt(2))
       turtle.right(135)
       turtle.forward(a)
       turtle.right(90)
       turtle.forward(a)
       turtle.right(45)
       turtle.end_fill()

def up_triangle (x, y, a, color):
    # TODO: (Maxim) Paint an blue triangle.
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.color(color)
        turtle.begin_fill()
        turtle.forward(a*math.sqrt(2))
        turtle.left(135)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(135)
        turtle.end_fill()

def parallelogram (x, y, z, a, c, color):
    # TODO: (Maxim) Paint a parallelogram.
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.left(z)
        turtle.color(color)
        turtle.begin_fill()
        turtle.forward(c)
        turtle.left(45)
        turtle.forward(a)
        turtle.left(135)
        turtle.forward(c)
        turtle.left(45)
        turtle.forward(a)
        turtle.end_fill()
        turtle.left(135)
        turtle.right(z)


def square (x, y, z, a, color):
    #TODO (Maxim) Paint a square.
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.right(z)
        turtle.color(color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(a)
            turtle.left(90)
        turtle.end_fill()
        turtle.left(z)


def circle(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(a)
    turtle.end_fill()

# Pictures:
def  rabbit ():
    # TODO: (Victoria) Paint a rabbit.
    # parallelogram()
    # rhomb()
    # up_triangle()
    # mid_triangle()
    # left_triangle()
    # down_triangle()
    # right_triangle()
    pass

def fish ():
    # TODO: (Victoria) Paint a fish.
    # up_triangle()
    # rhomb()
    # parallelogram()
    # down_triangle()
    # mid_triangle()
    # right_triangle()
    # left_triangle()
    pass

def spaceship ():
    # TODO: (Victoria) Paint a spaceship.
    # right_triangle()
    # down_triangle()
    # left_triangle()
    # up_triangle()
    # rhomb()
    # parallelogram()
    # mid_triangle()
    pass

def helicopter ():
    # TODO: (Alena) Paint a helicopter.
    # down_triangle()
    # parallelogram()
    # left_triangle()
    # up_triangle()
    # rhomb()
    # mid_triangle()
    # right_triangle()
    pass

def cock ():
    # TODO: (Alena) Paint a cock.
    up_triangle(-104, 98, 70, "#9932CC")
    turtle.left(45)
    right_triangle(-104, 93, (70 * math.sqrt(2)), "#DC143C")
    mid_triangle(-99 + 70 * math.sqrt(2), 98 - (70 * math.sqrt(2)) * 3 / 2, 0, 70 * math.sqrt(2), "#FF8C00")
    square(-99 + 105 * math.sqrt(2), 103 - (70 * math.sqrt(2)) / 2, 45, (70 * math.sqrt(2)) / 2, "#00BFFF")
    turtle.right(45)
    up_triangle(-99 + 105 * math.sqrt(2), 108, 60, "#9ACD32")
    left_triangle(-109 + 105 * math.sqrt(2) + 2 / 3 * (70 * math.sqrt(2)) / 2,
                  98 - (70 * math.sqrt(2)) / 2 - 2 / 3 * (70 * math.sqrt(2)) / 2,
                  (70 * math.sqrt(2) * math.sqrt(2)) / 3, "#EE82EE")

def  left_running_man ():
    # TODO: (Alena) Paint a running man.
    # rhomb
    # up_triangle
    # left_triangle
    # mid_triangle
    # right_triangle
    # down_triangle
    # parallelogram
    pass

def right_running_man ():
    # TODO: (Maxim) Paint a running man.
    # rhomb
    # up_triangle
    # left_triangle
    # mid_triangle
    # right_triangle
    # down_triangle
    # parallelogram
    pass

def ship ():
    # TODO: (Maxim) Paint ship.
    # rhomb
    # up_triangle
    # left_triangle
    # mid_triangle
    # right_triangle
    # down_triangle
    # parallelogram
    pass

def mainsquare ():
    # TODO: (Maxim) Paint a mainsquare.
    down_triangle(350+(-70.71), 250+140, 100, "#DC143C")
    left_triangle(350+70.71, 250+140, 50, "#9932CC")
    right_triangle(350+(-70.71), 250+140, 100, "#FFD700")
    up_triangle(350+(-34.87), 250+32.616, 50, "#EE82EE")
    rhomb(350+35.85, 250+103.85, 50, "#FF8C00")
    parallelogram(350+(-71.85), 250+(-3.5), 0, 50, 70.71, "#00BFFF")
    mid_triangle(350+71, 250+68, 135, 70.71, 'green')

def main ():
    cock()
    mainsquare()

main()
turtle.done()

#DC143C - красный
#9ACD32 - зеленый
#00BFFF	- синий
#FFD700 - желтый
#FF8C00 - оранжевый
#EE82EE - розовый
#9932CC - фиолетовый