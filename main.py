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
    # TODO: (Alena) Paint a triangle.
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

def rhomb (x, y, a, color):
    # TODO: (Alena) Paint a rhomb.
       turtle.up()
       turtle.setposition(x, y)
       turtle.down()
       turtle.color(color)
       turtle.begin_fill()
       turtle.right(45)
       turtle.forward(a)
       turtle.right(90)
       turtle.forward(a)
       turtle.right(90)
       turtle.forward(a)
       turtle.right(90)
       turtle.forward(a)
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
    # TODO: (Victoria) Paint a purple triangle.
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
    # TODO (Maxim) Paint a square.
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
    #TODO (Maxim) Paint a circle.
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
    turtle.left(15)
    parallelogram(140, 140, 120, 100, 150, '#9ACD32')
    turtle.right(105)
    square(190, 135, 90, 100, '#FF8C00')
    turtle.left(135)
    down_triangle(-115, -115, 200, '#DC143C')
    turtle.right(270)
    right_triangle(-115, -320, 200, '#FFD700')
    turtle.left(90)
    up_triangle(45, -170, 150, '#00BFFF')
    turtle.right(180)
    left_triangle(55, -220, 100, '#9932CC')
    turtle.right(315)
    mid_triangle(95, -59.3, 180, 100, '#EE82EE')
    pass

def fish ():
    # TODO: (Victoria) Paint a fish.
    turtle.left(15)
    parallelogram(-80, 140, 120, 100, 150, '#9ACD32')
    turtle.left(120)
    left_triangle(-280, 33.2, 100, '#9932CC')
    turtle.right(90)
    mid_triangle(-175, 35, 0, 100, '#EE82EE')
    turtle.right(45)
    rhomb(0, 208.3, 100, '#FF8C00')
    turtle.left(135)
    down_triangle(80, 138.2, 200, '#DC143C')
    turtle.left(180)
    right_triangle(80, 133.2, 200, '#FFD700')
    turtle.right(45)
    up_triangle(85, 233.3, 150, '#00BFFF')

    pass

def spaceship ():
    # TODO: (Victoria) Paint a spaceship.

    pass

def helicopter ():
    # TODO: (Alena) Paint a helicopter.
    parallelogram(50, 100, 0, 50, 65, "#9ACD32")
    up_triangle(45 - 70 * math.sqrt(2), 100, 70, "#DC143C")
    right_triangle(50, 95, 100, "#00BFFF")
    left_triangle(45, 95, 100, "#FFD700")
    mid_triangle(40 - (100 * math.sqrt(2)) * 1 / 4 - 50 * math.sqrt(2),
                 95 - (100 * math.sqrt(2)) * 3 / 4, 0, 50, "#FF8C00")
    down_triangle(35 - (100 * math.sqrt(2)) * 1 / 4 - 50 * math.sqrt(2) * 3 / 2,
                  95 - (100 * math.sqrt(2)) / 2, 50, "#EE82EE")
    rhomb(30 - (100 * math.sqrt(2)) * 1 / 4 - 50 * math.sqrt(2) * 3 / 2 - 50 * math.sqrt(2) / 4,
          95 - (100 * math.sqrt(2)) / 2 + 50 * math.sqrt(2) * 3 / 4, 50, "#9932CC")

def cock (x, y):
    # TODO: (Alena) Paint a cock.
    up_triangle(-104 + x, 98 + y, 50, "#9932CC")
    turtle.left(45)
    right_triangle(-104 + x, 93 + y, (50 * math.sqrt(2)), "#DC143C")
    mid_triangle(-99 + 50 * math.sqrt(2) + x, 98 - (50 * math.sqrt(2)) * 3 / 2 + y, 0, 50 * math.sqrt(2), "#FF8C00")
    square(-99 + 75 * math.sqrt(2) + x, 103 - (50 * math.sqrt(2)) / 2 + y, 45, (50 * math.sqrt(2)) / 2, "#00BFFF")
    turtle.right(45)
    up_triangle(-99 + 75 * math.sqrt(2) + x, 108 + y, 40, "#9ACD32")
    left_triangle(-104 + 75 * math.sqrt(2) + 2 / 3 * (50 * math.sqrt(2)) / 2 + x,
                  98 - (50 * math.sqrt(2)) / 2 - 2 / 3 * (50 * math.sqrt(2)) / 2 + y,
                  (50 * math.sqrt(2) * math.sqrt(2)) / 3, "#EE82EE")
    parallelogram(-104 + x, 87 + y, -90, (50 * math.sqrt(2)) * math.sqrt(2) / 3, (50 * math.sqrt(2)) * 2 / 3, "#FFD700")

def  left_running_man ():
    # TODO: (Alena) Paint a running man.
    circle(0, 105, 30, "#FF8C00")
    mid_triangle(-102.5, 100, 45, 100, "#EE82EE")
    mid_triangle(2.5, 0, -45, 100, "#00BFFF")
    mid_triangle(72.5, -75, -135, 70, "#FFD700")
    mid_triangle(49.5, -80, 45, 46, "#9932CC")
    parallelogram(-52.5, -103, 45, 45, 70, "#DC143C")
    mid_triangle(-30, -86.5, 135, 46, "#9ACD32")

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
    right_triangle(-350, -200, 100, "#DC143C")
    mid_triangle(30-350, 5-200, 225, 30, "#9932CC")
    up_triangle(-350, -200-(5 + 100 * math.sqrt(2)), 50, "#EE82EE")
    rhomb((2.5 + 70.71)-350, -200-(2.5 + 70.71), 50, "#FF8C00")
    mid_triangle(-5-350, -20-200, 135, 100, "#FFD700")
    down_triangle(-30-350, -150.42-200, 70, "#00BFFF")
    parallelogram(-85-350, -150-200, 315, 50, 70, "#9ACD32")

def mainsquare (x, y):
    # TODO: (Maxim) Paint a mainsquare.
    down_triangle(-70.71 + x, 140 - y, 100, "#DC143C")
    left_triangle(70.71 + x, 140 - y, 50, "#9932CC")
    right_triangle(-70.71 + x, 140 - y, 100, "#FFD700")
    up_triangle(-34.87 + x, 32.616 - y, 50, "#EE82EE")
    rhomb(35.85 + x, 103.85 - y, 50, "#FF8C00")
    parallelogram(-72 + x, -3.5 - y, 0, 50, 70.71, "#00BFFF")
    mid_triangle(71 + x, 68 - y, 135, 70.71, "#9ACD32")

def main ():
    mainsquare(-50, 50)
    cock(-200, 150)
    left_running_man()
    helicopter()
    mainsquare()
    ship()

main()
turtle.done()

#DC143C - красный
#9ACD32 - зеленый
#00BFFF	- синий
#FFD700 - желтый
#FF8C00 - оранжевый
#EE82EE - розовый
#9932CC - фиолетовый