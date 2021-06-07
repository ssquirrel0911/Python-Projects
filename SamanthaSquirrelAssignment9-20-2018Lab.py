#Samantha Squirrel
#samantha.squirrel001@albright.edu

import time

#CSC 141 Lab Assignment Due 9-20-2018

#Algorithm workbench 1

number = 1

while (number < 100 and number > 0):
    number = int(input("Enter a number between 0 and 100: ", )) #User must put in a number between 0 and 100
    product = number * 10
    print("The product is: ", product)#Calculates problem

    if (number <= 0):
        print("The number you input must be greater than 0!")#User must put in a number greater than 100
    elif product > 100:
        print("The product you calculated is over 100.")

print("Good job!")


#Algorithm Workbench 2

again = 'y'




while again == 'y' or again == 'Y':
    numberOne = int(input("Please enter your first number: ", ))#User must input their first number
    numberTwo = int(input("Please enter your second number: ",))#User must input their second number
 

    sumOfNumbers = numberOne + numberTwo



    print("The sum of your numbers entered is: ", sumOfNumbers)

    again = input('Do you want to put in two different numbers? ' +
                  '(Enter y for yes): ')

#Lab Program
keepGoing = 'y'


while keepGoing == 'y':
    rangeNumber = int(input("Please enter a number between 1 and 100: ", )) #User must input a number between 1 and 100
    print("The number you entered in the range is: ", rangeNumber)

    if (rangeNumber > 100):
        print("The number you input is higher than 100!")#User must put in a number less than 100
    elif (rangeNumber < 1):
        print("The number you input is less than 1!")#User must put in a number higher than 1
    elif rangeNumber % 2 == 0:
        print("The number you input is a even number.") #Program will tell user if number entered is odd or even
    else:
        print("The number you input is an odd number.")

keepGoing = input('Do you want to put in a different number in the range? ' +
                  '(Enter y for yes): ')


time.sleep(3)
