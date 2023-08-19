class Single_Employee:
    def __init__(self, employee_id, username, timestamp, gender, salary):
        self.employee_id = employee_id
        self.username = username
        self.timestamp = timestamp
        self.gender = gender
        self.salary = salary



def read_employees_data_file():
    f = open("employees_data.txt", "r")
    employees = {}
    for x in f:
        employee_id, username, timestamp, gender, salary = x.split(', ')
        employees[employee_id] = Single_Employee(employee_id, username, timestamp, gender, int(salary))
    # print(employees)
    return employees
  
read_employees_data_file()

