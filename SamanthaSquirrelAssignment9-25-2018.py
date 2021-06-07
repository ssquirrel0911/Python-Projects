#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Chapter 4 Programming Exercises 3, 4, 5, 6, 7, 8 Due 9-25-2018

import time

#Exercise 3

personalBudget = float(input("Enter how much you are going to budget"\
                             " for the month: "))#User will input budget for the month
#Prompts the user to continue a monthly budget if they want
moreExpenses = 'y'

totalPersonalExpense = 0

while moreExpenses == 'y' or moreExpenses == 'y':
    personalExpense = float(input("Enter your required expense $: "))#User will input their expenses
    totalPersonalExpense += personalExpense
    moreExpenses = input("Do you want to plan another monthly budget?: " +
                         "(Enter y for yes, any key for no): ")#Prompts the user to continue a monthly budget if they want

print()    
if totalPersonalExpense > personalBudget:
    print("You were over your budget of","$" + format(personalBudget, ".2f"), \
          "by", "$" + format(totalPersonalExpense - personalBudget, ".2f"))
elif personalBudget > totalPersonalExpense:
    print("You were over your budget of","$" + format(personalBudget, ".2f"), \
          "by", "$" + format(totalPersonalExpense - personalBudget, ".2f"))
else:
    print("You used exactly your month budget of: ", \
          "$" + format(personalBudget, ".2f"), sep ='')
    

#Exercise 4

time = 0
vehicleSpeed = 0
timeTraveled = 0

vehicleSpeed = float(input("Enter the speed of vehicle: "))#User will input their speed
print("The current speed you are going is:", vehicleSpeed, "mph")#Displays the vehicle speed
timeTraveled = int(input("How many hours did you travel in your vehicle? "))#User will input how many hours they traveled
print("The hours you traveled is:", timeTraveled, "hours")#Displays hours user traveled

print("Hour", "\t Distance traveled")
print('--------------------------')

print()
for hour in range(1, timeTraveled + 1):
    distanceTraveled = vehicleSpeed * hour
    print(hour, "\t" , distanceTraveled)


#Exercise 5

totalRainfall = 0.0
monthlyRainfall = 0.0
averageRainfall = 0.0
years = 0
totalMonths = 0

years = int(input("Enter the number of years to be calculated: ", )) #User will input the amount of years they want

for year in range(years):
    print("For year ", year + 1, ":")
    for month in range(12):
        monthlyRainfall = float(input("Enter the amount rainfall" \
                                      "for the month: "))#User will input the average rainfall for the next 12 months
        totalMonths += 1
        totalRainfall += monthlyRainfall

averageRainfall = totalRainfall / totalMonths

print("For ", totalMonths, "months")
print("The total rainfall is: ", format(totalRainfall, ".2f"), "inches")
print("The average monthly rainfall is: ", format(averageRainfall, ".2f"),"inches")

#Exercise 6
farenheit = 0
startTemperature = 0
endTemperature = 21
increment = 1

print("Celsius", "\t Fahrenheit")
print('--------------------------')

print()
for celsius in range(startTemperature, endTemperature, increment):
    fahrenheit = (9 / 5) * celsius + 32
    print(celsius, "\t" , format(farenheit, '.1f'))

#Exercise 7

another = 'y'

while another == 'y' or another == 'Y':
    numberOfDays = int(input('Enter the numbers of days worked: '))#User will put in the number of days they worked
    pay = numberOfDays * 0.01 * 2 #The number of days user input will be multiplied by the value of cents and 2
    print('The pay after number of days worked is: $', format(pay, ',.2f'), sep='')#Will display the sum of pay after days user worked
    another = input('Do you want to put in another number of days? ' +
                '(Enter y for yes): ')#User can input y or Y to loop through program again

#Exercise 8

MAX = 5

total = 0


print('This program calculates the sum of',\
      MAX, 'numbers you will enter.')

while total < 0:
    print('ERROR: The number cannot be negative.')#If the user inputs a negative number, the program will prompt the user to redo it again
    MAX = int(input('Enter positive numbers only'))

for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number
print('The total is', total)




time.sleep(3)
