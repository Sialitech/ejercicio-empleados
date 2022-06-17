import random
import itertools


class Empleado:
    newid = itertools.count(start=1)

    def __init__(self, data):
        data_list = data.split(",")
        self.id = next(Empleado.newid)
        self.name = data_list[0].strip()
        self.surname = data_list[1].strip()
        self.pay = int(data_list[2].strip())
        self.email = "{}.{}@acciona.com".format(self.name, self.surname)

    def __str__(self):
        return "El empleado {} {} cobra {}".format(self.name, self.surname, self.pay)

    def __add__(self, other):
        return other.pay + self.pay

    def pay_rise(self):
        self.pay = round(1.15 * self.pay)


class CEO(Empleado):

    def __init__(self, data):
        Empleado.__init__(self,data)
        self.empleado_list = []

    def __str__(self):
        return "El CEO {} {} cobra {}".format(self.name, self.surname, self.pay)

    def add_employee(self, data_employee):
        self.empleado_list.append(Empleado(data_employee))

    def remove_employee(self, employee_id):
        self.empleado_list.remove(self.empleado_list[employee_id])

    def print_empleados(self):
        for empleado in self.empleado_list:
            print(empleado)

