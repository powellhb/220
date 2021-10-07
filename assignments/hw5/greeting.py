"""
Name: Hilary Powell
greeting.py

Problem: develop a program that uses the author's graphics package

Certification of Autenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

def main():
    win = GraphWin("Draw a Heart", 700, 500)

    point_a = Point(320, 300)
    point_b = Point(250, 200)
    point_c = Point(250, 175)
    point_d = Point(250, 150)
    point_e = Point(275, 140)
    point_f = Point(290, 140)
    point_g = Point(320, 180)
    point_h = Point(350, 140)
    point_i = Point(365, 140)
    point_j = Point(390, 150)
    point_k = Point(390, 175)
    point_l = Point(390, 200)
    point_m = Point(320, 300)

    polygon_a = Polygon(point_a, point_b, point_c, point_d, point_e, point_f, point_g, point_h, point_i, point_j,
                       point_k, point_l, point_m)
    polygon_a.setFill("red")
    polygon_a.draw(win)

    point_n = Point(100, 400)
    point_r = Point(200, 300)

    line_a = Line(point_n, point_r)
    line_a.setArrow("last")
    line_a.draw(win)

    for i in range(15):
        line_a.move(30, -30)
        time.sleep(0.25)

    message = Text(Point(320, 100), "Happy Valentine's Day!")
    message.setTextColor("magenta")
    message.draw(win)
    win.getMouse()

if __name__ == '__main__':
    main()
