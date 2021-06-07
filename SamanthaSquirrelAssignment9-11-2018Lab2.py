#Samantha Squirrel
#samantha.squirrel001@albright.edu

import time
#Program Exercsises

#Excersise 1

name = input ('What is your name? ')
addressNumber = input('What is your address number and street? ')
city = input('What city do you live in? ')
state = input('What is the state that your city resides in?' )
zipcode = int(input('What is your zipcode?' ))
print("My full name is ", name)
print("My address number and street is ", addressNumber)
print("The  city I live in is", city)
print("The state that my city resides in is", state)
print("The zipcode of my address is", zipcode)

#Exercise 2
totalSales = float(input('What is the annual total amount of sales this year? '))
annualProfit = totalSales * 23


print("The total amount of profit is $",
      format(annualProfit, ',.2f'),
      sep='')

time.sleep(3)
