"""
Name: Hilary Powell
mean.py

Problem: design a program that outputs the RMS Average, the Harmonic Mean and the Geometric Mean

Certification of Autenticity:
I certify that this assignment is entirely my own work.
"""
#the program will output the rms average, the harmonic mean and the geometric mean
#the inputs will be a set of numbers and the outputs will be the rms average, the harmonic mean, and the geometric mean
#first we need to have an area where we can print the amount of values that will need to be entered
#then create an area that will print a space where you can enter each of those values
#then have python calculate the three different means of those values entered

import math

def main():
    print("This program computes the RMS Average, Harmonic Mean, and Geometric Mean respectively")
    number_of_values = eval(input("enter the values to be entered: " ))
    sum = 0
    geometric = 1
    for n in range(number_of_values):
        value = eval(input("enter value: "))
        sum = sum + value
        sum_rms = values ** 2
    rms = round(math.sqrt(rms accumulator), 3)
    print(rms)
    harmonic_mean = 1 / (number_of_values/sum)
    print(harmonic_mean)
    geometric_mean = round((value)**(1/number_of_values), 3)
    print(geometric_mean)

if __name__ == '__main__':
    main()