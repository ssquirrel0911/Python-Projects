#Samantha Squirrel
#samantha.squirrel001@albright.edu
#Assingment 19 Programming Exercise 2: Car Class

#Main method

import time

from SamanthaSquirrelAssignment19CarClass import Car

def main():
    year = usersYear()
    make = usersMake()
    carAccelerationAndBrake(year, make, speed)



def usersYear():
    #User will input their car year
    year = input("Enter your car year: ")
    return year

def usersMake():
    #User will input their car make
    make = input("Enter your car make: ")
    return make


def carAccelerationAndBrake(year, make):
    #Variable for user's car from other file
    userCar = Car(year, make)

    #Acceleration for user's car
    userCar.acceleration()
    print("The current speed after speeding up is: ", userCar.getSpeed())

    
    #Brakes for user's car
    userCar.brake()
    print("The current speed after braking is: ", userCar.getSpeed())


main()

time.sleep(3)
