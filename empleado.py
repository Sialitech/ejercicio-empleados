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

