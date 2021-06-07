#Samantha Squirrel
#samantha.squirrel001@albright.edu


#CSC141 Lab due 9-27-2018

import time

#Chapter 2 Programming Exercise 10 Ingredient Adjuster

regularBatchOfCookies = 48
cupsOfSugar = 1.5
cupsOfButter = 1
cupsOfFlour = 2.75

numberOfCookies = float(input("How many cookies do you wanna make?" )) #User will input the amount of cookies they want to make
print("The amount of cookies you wanna make is", numberOfCookies)

#Converts input
neededCupsOfSugar = (numberOfCookies / regularBatchOfCookies)*\
                    cupsOfSugar
neededCupsOfButter = (numberOfCookies / regularBatchOfCookies)*\
                   cupsOfButter
neededCupsOfFlour = (numberOfCookies / regularBatchOfCookies)*\
                    cupsOfFlour
#Displays the amount of ingredients that will need
print("For " + str(numberOfCookies) + " cookies you will need the amount of" \
      "ingredients you will need is " + \
      format(neededCupsOfSugar, ".2f") + " cups of sugar " + \
      format(neededCupsOfButter, ".2f") + " cups of butter " + \
      format(neededCupsOfFlour, ".2f") + " cups of flour")

#Chapter 3 Programming Exercise 15 Time Calculator

numberofSeconds = int(input('Please enter a number of seconds:')) #User will input the seconds they want to convert

#Converts input
days = int( numberofSeconds / 86400)
hours =int((( numberofSeconds % 86400) / 3600))
minutes = int(((( numberofSeconds % 86400) % 3600) / 60))
seconds = ((( numberofSeconds % 86400) % 3600) % 60)

print()

print(str(days) + " days, " + str(hours) + " hours, " + \
      str(minutes) + " minutes, " + str(seconds) + " seconds." )

#Chapter 4 Programming Exercise 12 Calculating the Factorial of a Number

interger = int(input("Enter a number of choice: ")) #User will input a number of choice

while interger < 1:
    interger = int(input("Enter a positive number of choice: ")) #User must input a positive number of choice

    if interger < 1:
        print("You must put in a positive number!")#Prompt user to put in a positive number

factorial = 1

for positiveNumber in range(1, interger + 1):
    factorial = factorial * positiveNumber

print()
print("The factorial of", interger, "is", factorial)


#Chapter 5 Algorithm workbench 1

def main():
    number = int(input("Enter number of choice to be multiplied by 10: "))
    print("The number you will have multiplied is: ", number)
    timesTen = 10
    showProduct(number)

def showProduct(number):
    result = number * 10
    print(result)

main()
#Chapter 5 Algorithm workbench 2

def main():
    quantity = 12
    showValue(quantity)

def showValue(quantity):
    print(quantity)
    

main()


#Chapter 5 Algorithm workbench 3

def main():
    myFunction(3, 2, 1)
    

def myFunction(valueA, valueB, valueC):
    print(valueA, valueB, valueC)

main()


time.sleep(3)
