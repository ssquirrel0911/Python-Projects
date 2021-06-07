#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 20 Chapter 10 Programming Exercise 6; Patient Charges

import time

class Procedure:

    #The __init__ method initializes the attributes

    def __init__(self, procedureName, dateOfProcedure, practitioner, charge):
        self.__procedureName = procedureName
        self.__dateOfProcedure = dateOfProcedure
        self.__practitioner = practitioner
        self.__charge = charge


    #set_procedureName methods accepts argument for user's procedure name

    def setProcedureName(self, procedureName):
        self.__procedureName = procedureName

    #set_dateOfProcedure methods accepts argument for user's date of procedure

    def setDateOfProcedure(self, dateOfProcedure):
        self.__dateOfProcedure = dateOfProcedure

    #set_practitioner methods accepts argument for user's practioner

    def setPractitioner(self, practitioner):
        self.__practitioner = practitioner

    #set_emergencyContact methods accepts argument for user's charge

    def setCharge(self, charge):
        self.__charge = charge

    #get_procedureName methods method returns procedure name

    def getProcedureName(self):
        return self.__procedureName

    #get_dateOfProcedure methods method returns date of procedure

    def getDateOfProcedure(self):
        return self.__dateOfProcedure

    #get_phoneNumber methods returns practitioner

    def getPractitioner(self):
        return self.__practitioner
    
    #get_emergencyContact methods returns charge

    def getCharge(self):
        return self.__charge




time.sleep(3)

