#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 20 Chapter 10 Lab; Programming Exercise 4

#Employee Class

import time

class Employee:

    #The __init__ method initializes the attributes

    def __init__(self, name, IDNumber, department, jobTitle):
        self.__name = name
        self.__IDNumber = IDNumber
        self.__department = department
        self.__jobTitle = jobTitle


    #set_name methods accepts argument for user's name

    def setName(self, name):
        self.__name = name

    #set_IDNumber methods accepts argument for user's IDNumber

    def setIDNumber(self, IDNumber):
        self.__IDNumber = IDNumber

    #set_department methods accepts argument for user's department

    def setDepartment(self, department):
        self.__department = department

    #set_jobTitle methods accepts argument for user's job title

    def setJobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

    #get_name methods method returns name

    def getName(self):
        return self.__name

    #get_IDNumber methods method returns ID Number

    def getIDNumber(self):
        return self.__IDNumber

    #get_department methods returns department

    def getDepartment(self):
        return self.__department

    #get_jobTitle methods returns job title

    def getJobTitle(self):
        return self.__jobTitle

time.sleep(3)   
