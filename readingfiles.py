employee_file = open("employees.txt", "a")
if employee_file.readable():
    print(employee_file.read())
    employee_file.close()

employee_file.write("\nKelly - Customer Service")



