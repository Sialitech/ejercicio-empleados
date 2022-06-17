from empleado import CEO

ceo = CEO("Manuel, Velasquez, 4500")

with open("lista_empleados.txt") as file:
    for line in file:
        ceo.add_employee(line)

print("sum of salaries: ", ceo.employee_list[0] + ceo.employee_list[1])

print(ceo)
ceo.print_employees()

print("removing empleado by id: 2")
ceo.remove_employee(2)
ceo.print_employees()

print("et voila!")
