import datetime

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
            
    # o(n) =>n is the numbers of employees
    def male_female_statistics(self):
        count_male =0
        count_female = 0
        for employee in self.employees.values():
            if employee.gender == "female":
                count_female +=1 
            elif employee.gender == "male":
                count_male +=1
        print(f'there is: {count_male} Male Employees, and {count_female} Female Employees')

    
    def add_single_employee(self):
        employee_id = f"emp{len(self.employees)+1:03}"
        # print(employee_id)
        timestamp = datetime.datetime.now().strftime('%Y%m%d')
        username = input("Enter the username:")      
        gender = input("Enter the gender:")
        salary = input("Enter the salary:")
        self.employees[employee_id] = Single_Employee(employee_id, username, timestamp, gender, int(salary))
        print(f"the new employee {username} was added succefully")



Empolyees_Data().add_single_employee()   
# output ---> 
# Enter the username:wrferf
# Enter the gender:weferf
# Enter the salary:2551
# the new employee wrferf was added succefully

# Empolyees_Data().male_female_statistics()   
# output ====>> there is: 1 Male Employees, and 1 Female Employees
 






# def display_menu():
#     all_data = Empolyees_Data()
#     print("\nWelcome to the Employee Database System")

#     for i in range (5):       
#         user_name = input("Enter username:") 
#         user_password = input("Enter password:")
   
#         if user_name == "admin" and user_password == "admin123123":
#             while True:
#                 print("\nThe admin menu:")
#                 print("1 -> Display female and male statistics")
#                 print("2 -> Add a single employee")
#                 print("3 -> Display all the employees")
#                 print("4 -> Change a specific employee Salary")
#                 print("5 -> Remove a specific employee")
#                 print("6 -> Raise a specific employee's Salary")
#                 print("7 -> Exit")

#                 choice_number = input("Please enter your choice: ")

#                 if choice_number == "1":
#                     print("you choose 1")
#                 elif choice_number == "2":
#                     print("you choose 2")
#                 elif choice_number == "3":
#                     print("you choose 3")
#                 elif choice_number == "4":
#                     print("you choose 4")
#                 elif choice_number == "5":
#                     print("you choose 5")
#                 elif choice_number == "6":
#                     print("you choose 6")
#                 elif choice_number == "7":
#                     print("you choose 7")
#                     break
#                 else:
#                     print("invalid number, please try again")

#         elif user_name == "manuella":
#             print("it is normal user")
#             break
   
    
#         elif i< 4:
#             print(f"Incorrect Username and/or Password. you still have {4-i} trial")
#         else:
#             print("Sorry you are blocked ,you have reached all the trials")

# display_menu()

