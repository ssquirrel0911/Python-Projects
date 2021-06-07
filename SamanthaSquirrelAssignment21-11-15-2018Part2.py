#Samantha Squirrel
#samantha.squirrel001@albright.edy

#Assignment 21 Chapter 11 Lab; Recreate Example 11-9 from book

#The turtle class is a subclass of the reptile class

import time

class Turtle(Reptile):
    #The __init__ method calls the superclass's
    #__init__ method passing "Turtle" as the species

    def __init__(self):
        Reptile.__init__(self, "Turtle")

    #The makeSound method overrides the superclass's
    #makeSound method

    def makeSound(self):
        print("Squeak!")#Yes, turtles squeak

time.sleep(3)
