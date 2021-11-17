"""
Name: Hilary Powell
button.py

Problem: Create a class Button that encapsulates data for a button shown in GUI.

Certification of Autenticity:
I certify that this assignment is entirely my own work and I received help from CSL.
"""
from graphics import Text


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p_1 = self.shape.getP1()
        p_2 = self.shape.getP2()
        if (p_1.getY() <= point.getY() <= p_2.getY()) and \
                (p_2.getX() >= point.getX() >= p_1.getX()):
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
