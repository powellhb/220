"""
Name: Hilary Powell
three_door_game.py

Problem: Write a program that draws 3 buttons and have one button as secret door.

Certification of Autenticity:
I certify that this assignment is entirely my own work and I received work from CSL.
"""
from random import randint
from graphics import GraphWin, Rectangle, Text, Point
from button import Button

def main():
    win = GraphWin("Three Door Game", 500, 500)
    win.setCoords(0, 0, 10, 10)
    message = Text(Point(5, 1), "I have a secret door")
    message.draw(win)
    message2 = Text(Point(5, 9), "click to choose my door")
    message2.draw(win)

    door_1 = Button(Rectangle(Point(1, 5), Point(3, 6)), "Door1")
    door_2 = Button(Rectangle(Point(4, 5), Point(6, 6)), "Door2")
    door_3 = Button(Rectangle(Point(7, 5), Point(9, 6)), "Door3")
    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)

    button_list = [door_1, door_2, door_3]

    answer = randint(0, 2)

    user_click = win.getMouse()

    for i in range(len(button_list)):
        if button_list[i].is_clicked(user_click):
            if i == answer:
                message.setText("You Win!")
                message2.setText("Click to close")
                button_list[i].color_button("green")
            else:
                message.setText("You Lost!")
                message2.setText(str(answer) + "is my secret door")
                button_list[i].color_button("red")
    win.getMouse()
    win.close()

main()
