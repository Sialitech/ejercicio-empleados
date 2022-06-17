from empleado import Empleado

empleado_list = []

with open("lista_empleados.txt") as file:
    for line in file:
        empleado_list.append(Empleado(line))

print(empleado_list[0] + empleado_list[1])

for empleado in empleado_list:
    print(empleado)

print("et voila!")
