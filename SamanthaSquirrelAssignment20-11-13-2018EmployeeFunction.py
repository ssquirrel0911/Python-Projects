#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 20 Chapter 10 Lab; Programming Exercise 4

#Employee Class function

import time

from SamanthaSquirrelAssignment20EmployeeClass import Employee 

def main():

    #Creates a list for employees
    employees = makeList()

    #Displays data in a list
    print("This is the data that is entered: ")
    displayList(employees)


#makeList function ets data from the user for 3 employees
#Function will return a a list of cell phone objects containing the data

def makeList():

    #Creates empty
    employeeChart = []

    #Adds 3 Employee objects to the list
    #User will input a data for all 3 employees
    print("Enter data for 3 employees.")
    for count in range(1, 4):
        #Get employee data
        print("Employee " + str(count) + ":")
        employeeName = input("Enter employee's name: ")
        employeeIDNumber = int(input("Enter employee's ID Number: "))
        employeeDepartment = input("Enter employee's department: ")
        employeeJobTitle = input("Enter employees's job title: ")
        print()

        #Creates a new Employee object in memory
        #and assigns it to employee variable

        employee = Employee(employeeName, employeeIDNumber, employeeDepartment, employeeJobTitle)

        #Adds objects to the list
        employeeChart.append(employee)

        #Returns list
        return employeeChart

#The displayList function accepts a list containing the objects as an argument
#and displays store data

def displayList(employeeChart):
    for item in employeeChart:
        print(item.getName())
        print(item.getIDNumber())
        print(item.getDepartment())
        print(item.getJobTitle())
        print()

main()
        
time.sleep(3)
