"""
Name: Hilary Powell
weighted_average.py

Problem: develop a Python program that uses numeric data from a text file

Certification of Autenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    in_file_name = open(in_file_name, 'r')
    out_file_name = open(out_file_name, 'w')
    values = in_file_name.readlines()
    weights_grades = []

    for line in in_file_name:
        all_values = line.replace("peyton", "").split(":")
        grades_weights = all_values[1]
        grades_weights = grades_weights.split(" ")
        grades_weights = grades_weights.lstrip("\n")
        names = all_values[0]
        print(grades)

        weighted_avg = 0
        for n in range(len(grades_weights)):
            grades_weights[n] = int(grades_weights)

        for i in range(0, len(grades_weights), 2):
            num_weight = eval(grades_weights[i])
            weights_grades.append(num_weight)

        for i in range(1, len(grades_weights), 2):
            num_grade = eval(grades_weights[i])
            weights_grades.append(num_grade)

        for i in range(len(num_weight)):
            weighted_avg = ((num_weight[i]) * (num_grade[i])) + weighted_avg


        if final_weighted_avg < 100:
            x = "Error: The weights are less than 100."
            out_file_name.write(x)
        elif final_weighted_avg > 100:
            x_2 = 'Error: The weights are greater than 100.'
            out_file_name.write(x_2)
        else:
            x_3 = round(final_weighted_avg, 1)
            out_file_name.write(x_3)
            final_weighted_avg = weighted_avg / 100
            output_students = names + 's average: ' + str(average) + "\n"
            out_file_name.write(output_students)

        total_avg_weight = (sum(weights_grades) / len(weights_grades))
        output = ("\nClass Average", round(total_avg_weight, 1))
        out_file_name.write(output)


    in_file_name.close()
    out_file_name.close()

def main():
    weighted_average("grades.txt", "avg.txt")

main()
