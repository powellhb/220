"""
Name: Hilary Powell
vigenere.py

Problem: write a program to implement a Vigenere cipher

Certification of Autenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

def main():
    win = GraphWin("Vigenere", 500, 500)
    win.setCoords(0, 0, 10, 10)
    # input
    Text(Point(2, 9), "Message to code").draw(win)
    Text(Point(2, 8), "Enter Keyword").draw(win)
    message_input = Entry(Point(6,9), 25)
    message_input.draw(win)
    keyword_input = Entry(Point(5, 8), 14)
    keyword_input.draw(win)
    output = Text(Point(5, 3), "")
    output.draw(win)

    # button
    encode_button = Text(Point(5, 3), "Encode")
    button_outline = Rectangle(Point(3, 4), Point(7, 2))
    encode_button.draw(win)
    button_outline.draw(win)

    win.getMouse()

    # undraw button
    encode_button.undraw()
    button_outline.undraw()
    encode_button.undraw()
    button_outline.undraw()

    a = message_input.getText()
    b = keyword_input.getText()

    #output
    output.setText("RESULTING MESSAGE")
    code(a, b)
    win.getMouse()

    end_message = Text(Point(5, 1), "Click anywhere to quit")
    end_message.draw(win)
    win.getMouse()
    win.close()

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i] % len(key))
        return("".join(key))

def code(string, key):
    coded_text = coded_text.upper()
    coded_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        coded_text.append(chr(x))
    return("".join(coded_text))

if __name__ == '__main__':
    main()