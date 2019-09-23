# Case - study #1
# Developers : Moiseenko V. (%),
#              Torgasheva A. (40%),
#              Setskov M. (25%).

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
    # TODO: (Victoria) Paint a triangle.
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

def fish (x, y):
    # TODO: (Victoria) Paint a fish.
    turtle.left(15)
    parallelogram(-180 + x, 90 + y, 120, 50, 70.71, '#9ACD32')
    turtle.left(120)
    left_triangle(-285 + x, 33.2 + y, 50, '#9932CC')
    turtle.right(90)
    mid_triangle(-230 + x, 35 + y, 0, 50, '#EE82EE')
    turtle.right(45)
    rhomb(-140 + x, 123.3 + y, 50, '#FF8C00')
    turtle.left(135)
    down_triangle(-100 + x, 93.2 + y, 100, '#DC143C')
    turtle.left(180)
    right_triangle(-100 + x, 83.2 + y, 100, '#FFD700')
    turtle.right(45)
    up_triangle(-95 + x, 133.3 + y, 75, '#00BFFF')
    turtle.left(90)

def spaceship (x, y):
    # TODO: (Victoria) Paint a spaceship.
    mid_triangle(-100 + x, 100 + y, 0, 50, '#EE82EE')
    turtle.right(45)
    up_triangle(-100 + x, 95 + y, 70.71, '#00BFFF')
    turtle.left(45)
    right_triangle(-100 + x, 85 + y, 100, '#FFD700')
    turtle.right(90)
    down_triangle(-29.29 + x, 7.4 + y, 100, '#DC143C')
    turtle.right(90)
    rhomb(-100 + x, -140.7 + y, 50, '#FF8C00')
    left_triangle(-140 + x, -180 + y, 50, '#9932CC')
    parallelogram(-20 + x, -70 + y, 90, 50, 70.71, '#9ACD32')

    pass

def helicopter (x, y):
    # TODO: (Alena) Paint a helicopter.
    parallelogram(50 + x, 100 + y, 0, 50, 58.5, "#9ACD32")
    up_triangle(45 - 63 * math.sqrt(2) + x, 100 + y, 63, "#DC143C")
    right_triangle(50 + x, 95 + y, 90, "#00BFFF")
    left_triangle(45 + x, 95 + y, 90, "#FFD700")
    mid_triangle(40 - (90 * math.sqrt(2)) * 1 / 4 - 45 * math.sqrt(2) + x,
                 95 - (90 * math.sqrt(2)) * 3 / 4 + y, 0, 45, "#FF8C00")
    down_triangle(35 - (90 * math.sqrt(2)) * 1 / 4 - 45 * math.sqrt(2) * 3 / 2 + x,
                  95 - (90 * math.sqrt(2)) / 2 + y, 45, "#EE82EE")
    rhomb(30 - (90 * math.sqrt(2)) * 1 / 4 - 45 * math.sqrt(2) * 3 / 2 - 45 * math.sqrt(2) / 4 + x,
          95 - (90 * math.sqrt(2)) / 2 + 45 * math.sqrt(2) * 3 / 4 + y, 45, "#9932CC")

def cock (x, y):
    # TODO: (Alena) Paint a cock.
    up_triangle(-104 + x, 98 + y, 75, "#9932CC")
    turtle.left(45)
    right_triangle(-104 + x, 93 + y, (75 * math.sqrt(2)), "#DC143C")
    mid_triangle(-99 + 75 * math.sqrt(2) + x, 98 - (75 * math.sqrt(2)) * 3 / 2 + y, 0, 75 * math.sqrt(2), "#FF8C00")
    square(-99 + 112.5 * math.sqrt(2) + x, 103 - (75 * math.sqrt(2)) / 2 + y, 45, (75 * math.sqrt(2)) / 2, "#00BFFF")
    turtle.right(45)
    up_triangle(-99 + 112.5 * math.sqrt(2) + x, 108 + y, 55, "#9ACD32")
    left_triangle(-114 + 112.5 * math.sqrt(2) + 2 / 3 * (75 * math.sqrt(2)) / 2 + x,
                  95 - (75 * math.sqrt(2)) / 2 - 2 / 3 * (75 * math.sqrt(2)) / 2 + y,
                  (75 * math.sqrt(2) * math.sqrt(2)) / 3, "#EE82EE")
    parallelogram(-104 + x, 87 + y, -90, (75 * math.sqrt(2)) * math.sqrt(2) / 3, (75 * math.sqrt(2)) * 2 / 3, "#FFD700")

def  left_running_man (x, y):
    # TODO: (Alena) Paint a running man.
    circle(0 + x, 105 + y, 30, "#FF8C00")
    mid_triangle(-95 + x, 100 - 5 + y, 45, 90, "#EE82EE")
    mid_triangle(0 + x, 5 + y, -45, 90, "#00BFFF")
    mid_triangle(60 + x, -60 + y, -135, 60, "#FFD700")
    mid_triangle(39.5 + x, -60 - 5 + y, 45, 36, "#9932CC")
    parallelogram(-47.5 + x, -80 + y, 45, 35, 60, "#DC143C")
    mid_triangle(-30 + x, -67.5 + y, 135, 36, "#9ACD32")

def ship (x, y):
    # TODO: (Maxim) Paint ship.
    right_triangle(-350 + x, -200 + y, 100, "#DC143C")
    mid_triangle(30 - 350 + x, 5 - 200 + y, 225, 30, "#9932CC")
    up_triangle(-350 + x, -200-(5 + 100 * math.sqrt(2)) + y, 50, "#EE82EE")
    rhomb((2.5 + 70.71) - 350 + x, -200 - (2.5 + 70.71) + y, 50, "#FF8C00")
    mid_triangle(-5 - 350 + x, -20 - 200 + y, 135, 100, "#FFD700")
    down_triangle(-30 - 350 + x, -150.42 - 200 + y, 70, "#00BFFF")
    parallelogram(-85 - 350 + x, -150 - 200 + y, 315, 50, 70, "#9ACD32")

def mainsquare (x, y):
    # TODO: (Maxim) Paint a mainsquare.
    down_triangle(-70.71 + x, 140 + y, 100, "#DC143C")
    left_triangle(70.71 + x, 140 + y, 50, "#9932CC")
    right_triangle(-70.71 + x, 140 + y, 100, "#FFD700")
    up_triangle(-34.87 + x, 32.616 + y, 50, "#EE82EE")
    rhomb(35.85 + x, 103.85 + y, 50, "#FF8C00")
    parallelogram(-72 + x, -3.5 + y, 0, 50, 70.71, "#00BFFF")
    mid_triangle(71 + x, 68 + y, 135, 70.71, "#9ACD32")

def main ():
    left_running_man(-50, 125)
    mainsquare(-50, -175)
    helicopter(225, -175)
    fish(-150, -50)
    ship(25, 75)
    cock(-350, 225)
    spaceship(200,-200)
    rabbit(150,100)

main()
turtle.done()

#DC143C - красный
#9ACD32 - зеленый
#00BFFF	- синий
#FFD700 - желтый
#FF8C00 - оранжевый
#EE82EE - розовый
#9932CC - фиолетовый