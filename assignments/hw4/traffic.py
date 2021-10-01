"""
Name: Hilary Powell
traffic.py

Problem: design a program that practices accumulations and nested loops

Certification of Autenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    roads_surveyed = eval(input("How many roads were surveyed? " ))
    total = 0
    for k in range(roads_surveyed):
        days_surveyed = eval(input("How many days was road " + str(k + 1) + " surveyed? "))
        sum = 0
        for j in range(days_surveyed):
            cars_traveled = eval(input("How any cars traveled on day " + str(j + 1) + " ? "))
            sum = sum + cars_traveled
            average = sum / days_surveyed
            total = total + cars_traveled
        print("Road", k + 1, "average vehicles per day: ", average)
    total_avg = total / roads_surveyed
    print("Total number of vehicles traveled on all roads: ", total)
    print("Average number of vehicles per road: ", total_avg)

if __name__ == '__main__':
    main()
