from empleado import Empleado, CEO

ceo = CEO("Manuel, Velasquez, 4500")

with open("lista_empleados.txt") as file:
    for line in file:
        ceo.add_employee(line)

print(ceo.empleado_list[0] + ceo.empleado_list[1])

print(ceo)
for empleado in ceo.empleado_list:
    print(empleado)

print("removing empleado by id:")
ceo.remove_employee(2)
for empleado in ceo.empleado_list:
    print(empleado)
print("et voila!")
