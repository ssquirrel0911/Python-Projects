#Samantha Squirrel
#CSC 141 Chapter 5 Lab
#Assignment 10 due 10-4-2018

import time

#Programming Exercise 1

def main():
    kilometers = float(input("Enter a number of kilometers of choice: ", ))#User will input kilometer number of choice

    kilometersToMiles(kilometers)

def kilometersToMiles(kilometers):
    miles = kilometers * 0.6214 #Converts users input
    print("This converts to ",
          format(miles, ',.2f'),
          sep='')#Displays the input after conversion

main()

time.sleep(3)
