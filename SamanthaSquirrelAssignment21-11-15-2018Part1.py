#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 21 Chapter 11 Lab; Recreate Example 11-9 from book

import time

#The Reptile class represents a general mammal

class Reptile:
    #The __init__ method accepts an argument
    #for the reptile's species

    def __init__(self, species):
        self.__species = species

    #The showSpecies displays a message
    #Indicating the reptile's species

    def showSpecies(self):
        print("I am a", self.__species)

    #The makeSound is the reptile's
    #way of making a generic sound

    def makeSound(self):
        print("Hissss")

time.sleep(3)
