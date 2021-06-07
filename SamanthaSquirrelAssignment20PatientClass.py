#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 20 Chapter 10 Programming Exercise 6; Patient Charges

import time

class Patient:

    #The __init__ method initializes the attributes

    def __init__(self, fullName, fullAddress, phoneNumber, emergencyContact):
        self.__fullName = fullName
        self.__fullAddress = fullAddress
        self.__phoneNumber = phoneNumber
        self.__emergencyContact = emergencyContact


    #set_fullName methods accepts argument for user's full name

    def setFullName(self, fullName):
        self.__fullName = fullName

    #set_fullAddress methods accepts argument for user's full address

    def setFullAddress(self, fullAddress):
        self.__fullAddress = fullAddress

    #set_phoneNumber methods accepts argument for user's phone number

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    #set_emergencyContact methods accepts argument for user's emergency contact

    def setEmergencyContact(self, emergencyContact):
        self.__emergencyContact = emergencyContact

    #get_fullName methods method returns full name

    def getFullName(self):
        return self.__fullName

    #get_fullAddress methods method returns full address

    def getFullAddress(self):
        return self.__fullAddress

    #get_phoneNumber methods returns phone number

    def getPhoneNumber(self):
        return self.__phoneNumber
    
    #get_emergencyContact methods returns emergency contact

    def getEmergencyContact(self):
        return self.__emergencyContact



time.sleep(3)
