#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 22 Polygon class

import time

class Polygon(Rectangle):

    #The __init method accepts arguments for the
    #Polygons length and width
    
    def __init__(self, length, width):
        #Call the superclass's __init__ method and pass arguments
        Rectangle.__init__(self, length, width)

        #Initilizae the __area attribute
        self.__area = area

    #The setArea method is the mutator for the __area attribute

    def setArea(self, area):
        self.__area = area

    #The getArea method is he accessor for the __area attribute

    def getArea(self):
        return self.__area

time.sleep(3)
