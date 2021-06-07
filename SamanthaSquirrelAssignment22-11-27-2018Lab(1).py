#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 22 Chapter 12 Lab Programming Exercise 1: Recursive Printing

import time

def main():
    printNumbersUpTo(7)
    
def printNumbersUpTo(n):
    #Base case
    if n == 1:
        print(n)

    #Recursive cases
    else:
        printNumbersUpTo(n-1)
        print(n)

#Displays numbers up to 6
printNumbersUpTo(6)

main()


time.sleep(3)

