employee_file = open("employees.txt", "r")

print(employee_file.readable())

for employee in employee_file.readlines():
    print(employee)

# print(employee_file.read())
# print(employee_file.readlines()[2])
employee_file.close()