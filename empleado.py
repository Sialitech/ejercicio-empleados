import random
import itertools


class Empleado:
    newid = itertools.count(start=1)

    def __init__(self, name, surname, pay):
        self.id = next(Empleado.newid)
        self.name = name
        self.surname = surname
        self.email = "{}.{}@acciona.com".format(name, surname)
        self.pay = int(pay)

    def __str__(self):
        return "El empleado {} {} cobra {}".format(self.name, self.surname, self.pay)

    def __add__(self, other):
        return other.pay + self.pay

    def pay_rise(self):
        self.pay = round(1.15 * self.pay)

