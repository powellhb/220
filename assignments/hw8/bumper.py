"""
Name: Hilary Powell
bumper.py

Problem: develop a Python program that uses the graphics package and
practices using decision statements.

Certification of Autenticity:
I certify that this assignment is entirely my own work. I also got help from CSL.
"""
import math
from graphics import *
from random import randint

def main():
    win = GraphWin("Joyride", 500, 500)
    win.setCoords(0, 0, 10, 10)

    ball_one = Circle(Point(randint(1, 8), randint(1, 8)), 2).draw(win)
    ball_two = Circle(Point(randint(1, 8), randint(1, 8)), 2).draw(win)

    ball_one.setFill(get_random_color())
    ball_two.setFill(get_random_color())

    x_move = get_random(0, 10)
    x_2_move = get_random(0, 10)
    y_move = get_random(0, 10)
    y_2_move = get_random(0, 10)

    runs = 0
    while runs < 500:
        ball_one.move(x_move, y_move)
        ball_two.move(x_2_move, y_2_move)

        if did_collide(ball_one, ball_two):
            x_move = x_move * (-1)
            x_2_move = x_2_move * (-1)
            y_move = y_move * (-1)
            y_2_move = y_2_move * (-1)

        if hit_horizontal(ball_one, win):
            y_move = y_move * (-1)
            ball_one.setFill(get_random_color())

        if hit_horizontal(ball_two, win):
            y_2_move = y_2_move * (-1)
            ball_two.setFill(get_random_color())

        if hit_vertical(ball_one, win):
            x_move = x_move * (-1)
            ball_one.setFill(get_random_color())

        if hit_vertical(ball_two, win):
            x_2_move = x_move * (-1)
            ball_two.setFill(get_random_color())

        runs = runs + 1

    win.getMouse()
    win.close()

def get_random(start, end):
    return randint(start, end)

def hit_horizontal(ball, win):
    if ball.getCenter().getX() + ball.getRadius() >= win.getWidth():
        return True
    elif ball.getCenter().getX() + ball.getRadius() <= 0:
        return True
    else:
        return False

def hit_vertical(ball, win):
    if ball.GetCenter().getY() + ball.getRadius() >= win.getHeight():
        return True
    elif ball.getCenter().getY() + ball.getRadius() <= 0:
        return True
    else:
        return False

def did_collide(ball, ball2):
    x = (ball2.getCenter().getX() - ball.getCenter().getX()) ** 2
    y = (ball2.getCenter().getY() - ball.getCenter().getY()) ** 2
    d = math.sqrt(x + y)

    if d <= (ball.getRadius() + ball2.getRadius()):
        return True
    else:
        return False

def get_random_color():
    r_1 = randint(0, 255)
    g_1 = randint(0, 255)
    b_1 = randint(0, 255)
    return color_rgb(r_1, g_1, b_1)

if __name__ == '__main__':
    main()
