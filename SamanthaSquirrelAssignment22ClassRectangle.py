#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 22 Rectangle

import time

class Rectangle:
    #The __init__ method accepts arguments for length and width

    def __init__(self, length, width):
        self.__length = length

        self.__width = width

    #The following methods are mutators for the class's data attributes

    def setLength(self, length):
        self.__length = length

    def setWidth(self, width):
        self.__width = width

    #The following mehotds are the acceors for the class's data attributes

    def getLength(self, length):
        return self.__length

    def getWidth(self, width):
        return self.__width



time.sleep(3)
