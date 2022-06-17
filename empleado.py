import random
import itertools


class Empleado:
    newid = itertools.count(start=1)

    def __init__(self, name, surname):
        self.id = next(Empleado.newid)
        self.name = name
        self.surname = surname
        self.email = "{}.{}@acciona.com".format(name, surname)
        self.pay = random.randint(1500, 2200)

    def pay_rise(self):
        self.pay = round(1.15 * self.pay)

