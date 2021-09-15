"""
Name: Hilary Powell
interest.py

Problem: develop a simple Python program that asks for input, does arithmetic, and provides output

Certification of Autenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    print("This program computes the monthly interest charge on a credit card account")
    prebal = eval(input("input the previous balance on the credit card statement: "))
    paydate = eval(input("input the day the payment was made "))
    payment = eval(input("input the payment amount"))
    annualint = eval(input("input the annual interest rate"))
    a_1 = prebal * 31
    b_1 = payment * (31 - paydate)
    c_1 = a_1 - b_1
    d_1 = c_1 / 31
    print("the monthly interest charge is $", round(d_1 * ((annualint/100) / 12), 2))
