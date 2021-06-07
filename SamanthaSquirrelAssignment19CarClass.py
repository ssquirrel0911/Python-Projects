#Samantha Squirrel
#samantha.squirrel001@albright.edu
#Assingment 19 Programming Exercise 2: Car Class

#Car class

class Car:

    #Initializes the attributes
    def __init__(self, year, make):
        self.__yearModel = year
        self.__make = make
        self.__speed = 0

    #Method accepts argument for car year 
    def setYearModel(self, year):
        self.__yearModel = year

    #Method accepts argument for car model
    def setMake(self, make):
        self.__make = make

    #Method accepts argument for speed
    def setMake(self, speed):
        self.__speed = 0

    #Setting get_method returns the year model
    def getYearModel(self):
        return self.__yearModel

    #Setting get_method returns the make
    def getMake(self):
        return self.__make

    #Setting get_method returns the speed
    def getSpeed(self):
        return self.__speed

    #Methods for attributes
    def acceleration(self):
        self.__speed + 5

    def brake(self):
        self.__speed - 5


    
    

