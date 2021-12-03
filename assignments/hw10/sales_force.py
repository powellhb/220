"""
Name: Hilary Powell
sales_force.py

Problem: Create a class SalesPerson that encapsulates data for a sales person.

Certification of Autenticity:
I certify that this assignment is entirely my own work and I received help from CSL.
"""

from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        n_file = open(file_name, "r")
        lines = n_file.readlines()
        for i in range(len(lines)):
            fields = lines[i].split(',')
            person = SalesPerson(int(fields[0]), fields[1])
            sales = fields[2].split()
            for sale in sales:
                person.enter_sale(sale)
            self.sales_people.append(person)
        n_file.close()

    def quota_report(self, quota):
        report = []
        for person in self.sales_people:
            report.append([person.get_id(), person.get_name(), person.get_total_sales(), person.get_total_sales() > quota])
        return report

    def top_seller(self):
        best_seller = self.sales_people[0]
        best_sellers = []
        for person in self.sales_people:
            if person.compare_to(best_seller) > 0:
                best_seller = person
                best_sellers = []
            elif person.compare_to(best_seller) == 0:
                best_sellers.append(person)
        best_sellers.append(best_seller)
        return best_sellers

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None


