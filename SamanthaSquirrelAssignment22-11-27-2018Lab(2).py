#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 22 Chapter 12 Lab Programming Exercise 2: Recursive Multiplication

import time

def main():
    print(repeatedAddition(7, 4))

def repeatedAddition(x,y):
    if x == 1:
        return y
    #Repeats the action mulitple times
    else: return y + repeatedAddition(x-1, y)

    
main()

time.sleep(3)
