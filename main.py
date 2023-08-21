class Single_Employee:
    def __init__(self, employee_id, username, timestamp, gender, salary):
        self.employee_id = employee_id
        self.username = username
        self.timestamp = timestamp
        self.gender = gender
        self.salary = salary



class Empolyees_Data():
    def __init__(self):
        self.employees = {}
        self.read_employees_data_file()


    # o(n) => n =the number of lines
    def read_employees_data_file(self):
        f = open("employees_data.txt", "r")
        for x in f:
            employee_id, username, timestamp, gender, salary = x.split(', ')
            self.employees[employee_id] = Single_Employee(employee_id, username, timestamp, gender, int(salary))
            





def display_menu():
    all_data = Empolyees_Data()
    print("\nWelcome to the Employee Database System")

    for i in range (5):       
        user_name = input("Enter username:") 
        user_password = input("Enter password:")
   
        if user_name == "admin" and user_password == "admin123123":
            print("it is admin")
            break

        elif user_name == "manuella":
            print("it is normal user")
            break
   
    
        if i< 4:
            print(f"Incorrect Username and/or Password. you still have {4-i} trial")
        else:
            print("Sorry you are blocked ,you have reached all the trials")

display_menu()

