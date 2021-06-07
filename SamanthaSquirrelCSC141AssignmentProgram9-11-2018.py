#Samantha Squirrel
#samantha.squirrel001@albright.edu
import time

#Programming Exercises Chapter 2
#Exercise 3

acreLandSize = 43560
totalSquareFeet = int(input("What is your the total amount" + \
                            " of square feet?", ))
totalAcres = ( totalSquareFeet / acreLandSize ) * 1

print("My total amount of square feet in acres is", totalAcres)

#Exercise 4

itemOne = 0
itemTwo = 0
itemThree = 0
itemFour = 0
itemFive = 0
total = 0
tax = 0

itemOne = int(input("What is the price of your first item?" ))
itemTwo = int(input("What is the price of your second item?" ))
itemThree = int(input("What is the price of your third item?" ))
itemFour = int(input("What is the price of your fourth item?" ))
itemFive = int(input("What is the price of your fifth item?" ))
total = itemOne + itemTwo + itemThree + itemFour + itemFive
tax = total * .07
total = tax + total

print("The price of my first item is", itemOne)
print("The price of my second item is", itemTwo)
print("The price of my third item is", itemThree)
print("The price of my fourth item is", itemFour)
print("The price of my fifth item is", itemFive)
print("The total price of my sale is", total)

#Exercise 5

speed = 0
time = 0

speed = int(input("What is the speed your car traveled?"))
time = float(input("What is the time that your car traveled?"))

distance = speed * time

print("The speed I traveled was", speed)
print("The time I traveled was", time)
print("The speed and time to make the distance was", distance)

#Exercise 6

purchaseAmount = 0
fullTax = 0.075
total = 0

purchaseAmount = float(input("What is your full purchase amount?", ))
total = purchaseAmount * fullTax

print("My purchase amount before taxes is", purchaseAmount)
print("My full purchase including taxes is", total)

#Exercise 7

milesDriven = float(input("What is the number of miles you've driven?", ))
gallonsOfGasUsed = float(input("How much gallons did you use?", ))
milesPerGallon = milesDriven / gallonsofGasUsed

print("My car's miles-per-gallon is", milesPerGallon)

#Exercise 8

mealCharge = float(input("What was the total of your restaurant bill?", ))
tip = 0.18 * mealCharge
salesTax = 0.07 * mealCharge
total = mealCharge + tip + salesTax

print("My restaurant bill including tip and tax is", total)


#Exercise 9

Celsius = int(input("What is the temperature right now?", ))
Fahrenheit = (Celsius * 9)/5 + 32

print("The temperature right now is", Celsius)
print("The temperature in Fahrenheit is", Fahrenheit)




time.sleep(3)
