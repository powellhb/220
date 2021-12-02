"""
Name: Hilary Powell
sales_person.py

Problem: Create a class SalesPerson that encapsulates data for a sales person.

Certification of Autenticity:
I certify that this assignment is entirely my own work and I received help from CSL.
"""

class SalesPerson:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def get_sales(self):
        if self.sales == None:
            return 0
        return self.sales

    def total_sales(self):
        sales = self.get_sales()
        total = 0
        for i in range(len(sales)):
            total += float(sales[i])
        return total

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if self.total_sales > other.total_sales:
            return 1
        elif self.total_sales < other.total_sales:
            return -1
        else:
            return 0

    def __str__(self):
        employee_id = format(self.get_id())
        employee_name = format(self.get_name())
        employee_sales = format(self.total_sales())

        return 'ID - '+employee_id+' Employee - '+employee_name+' Total Sales - $'+employee_sales







