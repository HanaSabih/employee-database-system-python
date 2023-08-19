# employee-database-system-python

Employee Database System (100 points)
You are tasked with writing a program that simulates an employee database system. The
project serves two main purposes: to provide practice in writing programs that manipulate
strings, data structures, and files, and to apply sorting and searching algorithms.
The computer first displays a login form. There are two user types in this system:
- Admin
- Users
If the user enters “admin” as username and “admin123123” as password, the system will
show the admin menu. Else, if a normal user logins, a different menu will be shown.
If any user inputs an incorrect combination, the system should display “Incorrect Username
and/or Password”. The user is not allowed to enter more than 5 wrong combinations.
Otherwise, the menu of the system will be displayed.
The System
Your job is to write a script that handles the user interaction component of the system. To
solve the problem, your program must be able to:
● Read one text file and upload all the students into the dictionary of the system
● Implement the basic control structure and manage the details
The file includes several users in the following format:
emp001, cdaoud, 20220802, male, 12000
emp002, manuella, 20220803, female, 1200
....
This file represents the list of employees in the company. Each line contains 5 words: employee
id, username, timestamp of joining (YYYYMMDD), gender, and the last word represents the
salary (integer). You are asked to import that file when the program starts.
The Flow of The System:
A. The employees written inside the text file are imported (loaded) into the data structure of the
program with no intervention and without letting the user know anything.
B. The program starts by greeting the user and asking for their username and password (if the
password was left empty, then it’s a normal employee)
If the user logged in is an admin, the following menu will be displayed:
1. Display Statistics
2. Add an Employee
3. Display all Employees
4. Change Employee’s Salary
5. Remove Employee
6. Raise Employee’s Salary
7. Exit
● If the admin chooses (1), the system should display how many employees are male
and how many employees are female.
● If the admin chooses (2), the system should allow the admin to add a new employee
to the system by specifying the username, gender and the salary only (the
employee id is auto-incremented and the date is automatically taken from the
computer)
● If the admin chooses (3), the system should display all the employees registered in
the system ordered by date (Today, Yesterday, etc).
● If the admin chooses (4), the system should allow the admin to change the salary of
an employee by specifying his/her Id. The system should prompt the admin for the
Employee ID and for the salary. If the employee is found, then the salary is
changed.
● If the admin chooses (5), the system should allow the admin to remove an
employee from the system by asking for the ID
● If the admin chooses (6), the system should ask the user for the employee ID and
the raise percentage (example: 1.05) and the system should increase the
employee’s salary if found.
● If the user chooses (7), the program should exit after saving the information to the
file.
If the user logged in is a normal employee, the following menu will be displayed after
greeting by the following message: “Hi Mr. Charbel” or “Hi Ms. Fatima” (pay attention to
the gender)
1. Check my Salary
2. Exit
● If the user chooses (1), the system should display the salary of the logged-in user.
● If the user chooses (2), the system will terminate and save the timestamp of the
employee's login to a new file.
After each option, the menu is displayed again. The user can use the system multiple
times.