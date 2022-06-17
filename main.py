from empleado import Empleado, CEO

ceo = CEO("Manuel, Velasquez, 4500")

with open("lista_empleados.txt") as file:
    for line in file:
        ceo.add_employee(line)

print(ceo.empleado_list[0] + ceo.empleado_list[1])

print(ceo)
ceo.print_empleados()

print("removing empleado by id: 2")
ceo.remove_employee(2)
ceo.print_empleados()

print("et voila!")
