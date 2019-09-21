# Case - study #1
# Developers : Moiseenko V. (%),
#              Torgasheva A. (%),
#              Seckov M. (%)

import turtle

# Figures:
def up_triangle (x, y, a, c, color):
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

def left_triangle (x, y, a, c, color):
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
    #TODO: (Alena) Paint a triangle.

def rhomb (x, y, z, color):
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
    #TODO: (Alena) Paint a rhomb.

def mid_triangle ():
    # TODO: (Victoria) Paint a triangle.
    pass

def right_triangle ():
    #TODO: (Victoria) Paint a purple triangle.
    pass

def down_triangle ():
    # TODO: (Maxim) Paint an blue triangle.
    pass

def _parallelogram ():
    # TODO: (Maxim) Paint a parallelogram.
    pass
def square():
    #TODO (Maxim) Paint a square.
pass

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
    # down_triangle
    # up_triangle
    # left_triangle
    # right_triangle
    # mid_triangle
    # rhomb
    # parallelogram
    pass

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

def main ():
    pass

main()





