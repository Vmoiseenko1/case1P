# Case - study #1
# Developers : Moiseenko V. (%),
#              Torgasheva A. (%),
#              Setskov M. (%).

import turtle

# Figures:
def down_triangle (x, y, a, c, color):
    # TODO: (Alena) Paint a triangle.
       turtle.up()
       turtle.setposition(x, y)
       turtle.down()
       turtle.color(color)
       turtle.begin_fill()
       turtle.forward(c)
       turtle.right(135)
       turtle.forward(a)
       turtle.right(90)
       turtle.forward(a)
       turtle.right(135)
       turtle.end_fill()

def right_triangle (x, y, a, c, color):
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
       turtle.forward(c)
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

def mid_triangle(x,y,a,c,color):
    # TODO: (Victoria) Paint a triangle.
       turtle.up()
       turtle.setposition(x,y)
       turtle.down()
       turtle.color(color)
       turtle.begin_fill()
       turtle.right(45)
       turtle.forward(a)
       turtle.right(135)
       turtle.forward(c)
       turtle.right(135)
       turtle.forward(a)
       turtle.right(45)
       turtle.end_fill()

def left_triangle(x,y,a,c, color):
    #TODO: (Victoria) Paint a purple triangle.
       turtle.up()
       turtle.setposition(x,y)
       turtle.down()
       turtle.color(color)
       turtle.begin_fill()
       turtle.right(90)
       turtle.forward(c)
       turtle.right(135)
       turtle.forward(a)
       turtle.right(90)
       turtle.forward(a)
       turtle.right(45)
       turtle.end_fill()

def up_triangle (x, y, a, c, color):
    # TODO: (Maxim) Paint an blue triangle.
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.color(color)
        turtle.begin_fill()
        turtle.forward(c)
        turtle.left(135)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(135)
        turtle.end_fill()

def _parallelogram (x, y, z, a, c, color):
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


def square (x, y, a, color):
    #TODO (Maxim) Paint a square.
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.color(color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(a)
            turtle.left(90)
        turtle.end_fill()

def circle(x, y, a, color):
       turtle.up()
       turtle.setposition(x, y)
       turtle.down()
       turtle.color(color)
       turtle.begin_fill()
       turtle.circle(a)
       turtle.end_fill()

up_triangle(-64, 98, 52.43, 70, "#9932CC")
up_triangle(35, 95, 33, 40, "#FFD700")
square(30, 64, 30, "#DC143C")
turtle.done()