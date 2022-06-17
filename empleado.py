import random


class Empleado:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.email = "{}.{}@acciona.com".format(name, surname)
        self.pay = random.randint(1500, 2200)

    def pay_rise(self):
        self.pay = round(1.15 * self.pay)

