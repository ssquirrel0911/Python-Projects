#Samantha Squirrel
#samantha.squirrel001@albright.edu

import time

#CSC 141 Assignment Due 9-20-2018

#Algorithm workbench 3

for number in range(0, 1001, 10): #Count will go in cycles of 10s until 1000
    print(number)
print("Good Job!")

#Algorithm workbench 4

total = 0.0

for numbers in range(10):
    numbers = float(input("Please enter a number: "))#User will put in 10 random numbers of choice
    total += numbers
print("This is the total of the numbers you input: ", total)#Will display what the user input

time.sleep(3)
